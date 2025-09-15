from fastapi import APIRouter, Depends
from typing import List
from app.schema.user import User as UserSchema, UserCreate
from app.service.user_service import UserService
from app.repository.user_repository import UserRepository
from app.security.auth import verify_token

router = APIRouter()

user_repository = UserRepository()
user_service = UserService(user_repository)

@router.get("/users", response_model=List[UserSchema])
def get_users(token_data: dict = Depends(verify_token)):
    return user_service.get_all_users()

@router.get("/users/{id}", response_model=UserSchema)
def get_user_by_id(id: int, token_data: dict = Depends(verify_token)):
    return user_service.get_user_by_id(id)

@router.post("/users", response_model=UserSchema)
def create_user(user: UserCreate, token_data: dict = Depends(verify_token)):
    return user_service.create_user(user)