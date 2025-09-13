from fastapi import HTTPException
from app.repository.user_repository import UserRepository
from app.schema.user import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_id(self, id: int):
        user = self.user_repository.get_user_by_id(id)
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    def create_user(self, user_create: UserCreate):
        return self.user_repository.save(user_create)