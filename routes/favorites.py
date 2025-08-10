from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from bson import ObjectId

from database.database import get_database, convert_object_id
from models.models import FavoriteResponse, Favorite, PetResponse

router = APIRouter()


@router.post("/favorite/{pet_id}", response_model=FavoriteResponse, status_code=status.HTTP_201_CREATED)
async def add_favorite(pet_id: str):
    db = get_database()
    
    if not ObjectId.is_valid(pet_id):
        raise HTTPException(status_code=400, detail="Invalid pet ID format")
    
    pet = await db.pets.find_one({"_id": ObjectId(pet_id)})
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    existing_favorite = await db.favorites.find_one({"pet_id": pet_id})
    if existing_favorite:
        raise HTTPException(status_code=400, detail="Pet is already in favorites")
    
    added_at = datetime.utcnow()
    favorite = Favorite(pet_id=pet_id, added_at=added_at)
    await db.favorites.insert_one(favorite.dict())
    
    return FavoriteResponse(
        message="Pet added to favorites",
        pet_id=pet_id,
        added_at=added_at
    )


@router.delete("/favorite/{pet_id}", response_model=FavoriteResponse, status_code=status.HTTP_200_OK)
async def remove_favorite(pet_id: str):
    db = get_database()
    
    if not ObjectId.is_valid(pet_id):
        raise HTTPException(status_code=400, detail="Invalid pet ID format")
    
    result = await db.favorites.delete_one({"pet_id": pet_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pet not found in favorites")
    
    return FavoriteResponse(
        message="Pet removed from favorites",
        pet_id=pet_id
    )


@router.get("/favorites", status_code=status.HTTP_200_OK)
async def get_favorites():
    db = get_database()
    
    cursor = db.favorites.find().sort("added_at", -1)
    favorites = await cursor.to_list(length=None)
    
    favorite_pets = []
    for favorite in favorites:
        pet = await db.pets.find_one({"_id": ObjectId(favorite["pet_id"])})
        if pet:
            pet = convert_object_id(pet)
            pet_response = PetResponse(**pet)
            favorite_pets.append({
                "pet": pet_response.dict(),
                "added_at": favorite["added_at"]
            })
    
    return favorite_pets