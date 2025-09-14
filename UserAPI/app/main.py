from fastapi import FastAPI
from app.controller import user_controller
from dotenv import load_dotenv

app = FastAPI(root_path="/usersapi")
app.include_router(user_controller.router, prefix="/api", tags=["users"])