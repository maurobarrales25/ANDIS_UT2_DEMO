from typing import List
from fastapi import HTTPException
import httpx

def serialize_object_id(doc):
    if doc is None:
        return None
    doc["_id"] = str(doc["_id"])
    return doc

def serialize_object_ids(docs: List):
    return [serialize_object_id(doc) for doc in docs]

async def get_user(user_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://user-api:8000/api/users/{str(user_id)}")
        data = response.json()

        if data.get("detail"):
            raise HTTPException(status_code=500, detail="Este usuario no existe")
        return data
    
async def get_songs(playlist):
    async with httpx.AsyncClient() as client:
        songs = []
        songs_id = playlist.get('songs_ids')

        for song_id in songs_id:
            response = await client.get(f"http://artist-api:8080/artistapi/song/by-id?id={str(song_id)}")
            data_songs = response.json()
            songs.append(data_songs)
            
        playlist.pop('songs_ids')
        playlist["songs"] = songs
    
    return songs


async def get_artist(songs):
    async with httpx.AsyncClient() as client:
        for artist in songs:
            response = await client.get(f"http://artist-api:8080/artistapi/artist/by-id?id={artist.get('artistID')}")
            data_artists = response.json()
            artist["artist"] = data_artists
            artist.pop('artistID')
            artist.pop('albumID')

async def get_song(song_id):
    async with httpx.AsyncClient() as client:

        response = await client.get(f"http://artist-api:8080/artistapi/song/by-id?id={str(song_id)}")

        data = response.json()

        if data.get("status"):
            raise HTTPException(status_code=500, detail="Esta cancion no existe")
        return data