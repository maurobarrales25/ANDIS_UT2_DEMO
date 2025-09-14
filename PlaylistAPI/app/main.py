from fastapi import FastAPI
from controller import playlist_controller

app = FastAPI()

app.include_router(playlist_controller.router)