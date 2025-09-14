from repository.playlist_repository import PlaylistRepository
from utils.utils import get_user, get_songs, get_artist, get_song
from fastapi import HTTPException

class PlaylistService:
    def __init__(self, playlist_repository: PlaylistRepository):
        self.playlist_repository = playlist_repository

    async def get_playlists(self):
        playlists = await self.playlist_repository.get_playlists()
        
        for playlist in playlists:
            user_id = playlist.get('user_id')
            user = await get_user(user_id)
            playlist.pop('user_id')
            playlist["user"] = user
            
            songs = await get_songs(playlist)
            await get_artist(songs)
            
        return playlists
    
    async def get_playlist_by_id(self, id):
        playlist = await self.playlist_repository.get_playlist_by_id(id)
        user_id = playlist.get('user_id')

        user = await get_user(user_id)

        songs = await get_songs(playlist)

        await get_artist(songs)
                
        playlist.pop('user_id')
        playlist["user"] = user

        return playlist
    
    async def get_playlists_by_user_id(self, user_id):
        user = await get_user(user_id)
        playlists = await self.playlist_repository.get_playlists_by_user_id(user_id)
        
        for playlist in playlists:
            playlist.pop('user_id')
            songs = await get_songs(playlist)
            await get_artist(songs)
            
        return {"playlists": playlists, "user": user}
    
    async def save_playlist(self, playlist):
        playlist_dict = playlist.dict()
        user_id = playlist_dict.get("user_id")
        await get_user(user_id)

        songs_ids = playlist_dict.get("songs_ids")

        for song_id in songs_ids:
            try:
                await get_song(song_id)
            except:
                raise HTTPException(status_code=500, detail="Hay canciones que no existen")
            
        songs = await get_songs(playlist_dict)
        await get_artist(songs)
            
        return await self.playlist_repository.save_playlist(playlist_dict)