from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
url = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@mongo:27017/playlist?authSource=admin"
client = AsyncIOMotorClient(url)
db = client.playlist