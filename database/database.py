from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Dict, Any
import os

client: Optional[AsyncIOMotorClient] = None
database = None


async def connect_to_mongo():
    global client, database
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(mongo_url)
    database = client.pet_adoption_db
    print("Connected to MongoDB")


async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Disconnected from MongoDB")


def get_database():
    return database


def convert_object_id(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Convert MongoDB _id to id for API responses"""
    if doc and "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc