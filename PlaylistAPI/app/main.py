from fastapi import FastAPI
from controller import playlist_controller

app = FastAPI(root_path="/playlistapi")

app.include_router(playlist_controller.router)