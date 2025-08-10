from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId



class Pet(BaseModel):

    name: str
    age: int
    price: float
    breed: str
    description: str
    image_url: str
    species: str
    gender: str
    size: str
    status: str = "adoptable"
    is_adopted: bool = False

    class Config:

        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Fluffy",
                "age": 2,
                "price": 299.99,
                "breed": "Persian Cat",
                "description": "A lovely and playful Persian cat",
                "image_url": "https://images.unsplash.com/photo-1574158622682-e40e69881006",
                "species": "Cat",
                "gender": "Female",
                "size": "Medium",
                "status": "adoptable",
                "is_adopted": False
            }
        }


class PetResponse(BaseModel):
    id: str = Field(alias="id")
    name: str
    age: int
    price: float
    breed: str
    description: str
    image_url: str
    species: str
    gender: str
    size: str
    status: str
    is_adopted: bool



class Adoption(BaseModel):
    pet_id: str
    adopted_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "pet_id": "507f1f77bcf86cd799439011",
                "adopted_at": "2024-01-15T12:00:00"
            }
        }


class Favorite(BaseModel):
    pet_id: str
    added_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "pet_id": "507f1f77bcf86cd799439011",
                "added_at": "2024-01-15T12:00:00"
            }
        }


class PaginatedResponse(BaseModel):
    pets: list[PetResponse]
    total: int
    page: int
    limit: int
    total_pages: int


class AdoptionResponse(BaseModel):
    message: str
    pet_id: str
    adopted_at: datetime


class FavoriteResponse(BaseModel):
    message: str
    pet_id: str
    added_at: Optional[datetime] = None