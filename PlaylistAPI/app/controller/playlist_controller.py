from fastapi import APIRouter
from typing import List
from service.playlist_service import PlaylistService
from repository.playlist_repository import PlaylistRepository
from schema.playlist_schema import PlaylistCreate

router = APIRouter(prefix="/playlist", tags=["playlist"])

playlist_repository = PlaylistRepository()
playlist_service = PlaylistService(playlist_repository)

@router.get("/")
async def get_playlists():
    playlists = await playlist_service.get_playlists()
    return playlists

@router.get("/{id}")
async def get_playlist_by_id(id: str):
    playlist = await playlist_service.get_playlist_by_id(id)
    return playlist

@router.get("/user/{user_id}")
async def get_playlists_by_user_id(user_id: int):
    playlists = await playlist_service.get_playlists_by_user_id(user_id)
    return playlists

@router.post("/")
async def save_playlist(playlist: PlaylistCreate):
    return await playlist_service.save_playlist(playlist)