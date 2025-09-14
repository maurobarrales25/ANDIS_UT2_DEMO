import os
import logging
import asyncio
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError, jwk
from jose.utils import base64url_decode
import httpx

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
security = HTTPBearer()

# Config desde .env
KEYCLOAK_INTERNAL_URL = os.environ.get("KEYCLOAK_URL", "http://keycloak:8080")
KEYCLOAK_REALM = os.environ.get("KEYCLOAK_REALM", "demo-realm")
KEYCLOAK_ISSUER = os.environ.get("KEYCLOAK_ISSUER", f"http://localhost:8080/realms/{KEYCLOAK_REALM}")
KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID", "demo-client")
KEYCLOAK_AUDIENCE = os.environ.get("KEYCLOAK_AUDIENCE", KEYCLOAK_CLIENT_ID)
KEYCLOAK_CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET", "")

# Cache / retries (por si el servicio no funciona bien)
public_keys_cache = {}
cache_timestamp = None
CACHE_DURATION = 3600
JWKS_RETRIES = int(os.environ.get("JWKS_RETRIES", "8"))
JWKS_RETRY_DELAY = int(os.environ.get("JWKS_RETRY_DELAY", "2"))

async def get_keycloak_public_keys():
    global public_keys_cache, cache_timestamp
    if cache_timestamp and (datetime.now().timestamp() - cache_timestamp) < CACHE_DURATION:
        return public_keys_cache

    jwks_url = f"{KEYCLOAK_INTERNAL_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/certs"
    for attempt in range(1, JWKS_RETRIES + 1):
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(jwks_url, timeout=5.0)
                resp.raise_for_status()
                jwks = resp.json()
                keys = {k.get("kid"): k for k in jwks.get("keys", []) if k.get("kid")}
                public_keys_cache = keys
                cache_timestamp = datetime.now().timestamp()
                logger.info(f"Fetched {len(keys)} JWKS keys from Keycloak (attempt {attempt})")
                return keys
        except Exception as e:
            logger.warning(f"Attempt {attempt}/{JWKS_RETRIES} to fetch JWKS failed: {e}")
            if attempt < JWKS_RETRIES:
                await asyncio.sleep(JWKS_RETRY_DELAY)
            else:
                logger.error("All attempts to fetch public keys failed")
                if public_keys_cache:
                    logger.info("Using cached public keys")
                    return public_keys_cache
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                    detail="Unable to fetch public keys from Keycloak after retries")

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials
    try:
        header = jwt.get_unverified_header(token)
        alg = (header.get("alg") or "").upper()
        kid = header.get("kid")
        logger.info(f"Token header alg={alg}, kid={kid}")

        # ---------------- HS* case (HMAC) ----------------
        if alg.startswith("HS"):
            if not KEYCLOAK_CLIENT_SECRET:
                raise HTTPException(status_code=500, detail="Client secret not configured for HS token verification")

            # Valida con el secret del .env
            try:
                payload = jwt.decode(
                    token,
                    KEYCLOAK_CLIENT_SECRET,
                    algorithms=[alg],
                    audience=KEYCLOAK_AUDIENCE,
                    issuer=KEYCLOAK_ISSUER
                )
                if payload.get("azp") != KEYCLOAK_CLIENT_ID:
                    logger.warning(f"Token azp='{payload.get('azp')}' != expected '{KEYCLOAK_CLIENT_ID}'")
                return payload
            except JWTError as e:
                # Usar el aud dentro del token si es distinto
                try:
                    preview = jwt.get_unverified_claims(token)
                    token_aud = preview.get("aud")
                    if token_aud and token_aud != KEYCLOAK_AUDIENCE:
                        payload = jwt.decode(token, KEYCLOAK_CLIENT_SECRET, algorithms=[alg], audience=token_aud, issuer=KEYCLOAK_ISSUER)
                        return payload
                except Exception:
                    pass
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token (HS): {str(e)}")

        # ---------------- RS* case (RSA) ----------------
        if alg.startswith("RS"):
            public_keys = await get_keycloak_public_keys()
            logger.info(f"Available JWKS kids: {list(public_keys.keys())}")
            if not kid or kid not in public_keys:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid key ID")
            key_data = public_keys[kid]
            jwk_obj = jwk.construct(key_data)
            pem = jwk_obj.to_pem().decode()
            try:
                payload = jwt.decode(
                    token,
                    pem,
                    algorithms=[alg],
                    audience=KEYCLOAK_AUDIENCE,
                    issuer=KEYCLOAK_ISSUER
                )
                if payload.get("azp") != KEYCLOAK_CLIENT_ID:
                    logger.warning(f"Token azp='{payload.get('azp')}' != expected '{KEYCLOAK_CLIENT_ID}'")
                return payload
            except JWTError as e:
                try:
                    preview = jwt.get_unverified_claims(token)
                    token_aud = preview.get("aud")
                    if token_aud:
                        payload = jwt.decode(token, pem, algorithms=[alg], audience=token_aud, issuer=KEYCLOAK_ISSUER)
                        return payload
                except Exception:
                    pass
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token (RS): {str(e)}")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unsupported token alg: {alg}")

    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token claims: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error verifying token: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
