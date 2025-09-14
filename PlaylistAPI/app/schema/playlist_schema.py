from pydantic import BaseModel, Field
from typing import List

class PlaylistBase(BaseModel):
    name: str
    user_id: int
    songs_ids: List[int]

class PlaylistCreate(PlaylistBase):
    pass
