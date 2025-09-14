from fastapi import FastAPI
from app.controller import user_controller
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(user_controller.router, prefix="/api", tags=["users"])