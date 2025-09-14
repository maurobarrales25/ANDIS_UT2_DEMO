from database.database import db
from utils.utils import serialize_object_id, serialize_object_ids
from bson import ObjectId
from fastapi import HTTPException

class PlaylistRepository:
    def __init__(self):
        pass

    async def get_playlists(self):
        playlists_cursor = db.get_collection("playlist").find()
        playlists = await playlists_cursor.to_list()

        return serialize_object_ids(playlists)
    
    async def get_playlist_by_id(self, id):
        try:
            playlist = await db.get_collection("playlist").find_one({"_id": ObjectId(id)})
        except:
            raise HTTPException(status_code=500, detail="Playlist no encontrada")
        
        return serialize_object_id(playlist)

    async def get_playlists_by_user_id(self, user_id):
        playlists_cursor = db.get_collection("playlist").find({"user.id": user_id})
        playlists = await playlists_cursor.to_list()

        if len(playlists) == 0:
            raise HTTPException(status_code=500, detail="No tiene ninguna playlist este usuario")

        return serialize_object_ids(playlists)

    async def save_playlist(self, playlist):
        result = await db.get_collection("playlist").insert_one(playlist)
        return await self.get_playlist_by_id(result.inserted_id)