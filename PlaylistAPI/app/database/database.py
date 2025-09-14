from motor.motor_asyncio import AsyncIOMotorClient
import os

url = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(url)
db = client.playlist