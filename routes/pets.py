from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from bson import ObjectId
import math

from database.database import get_database, convert_object_id
from models.models import PetResponse, PaginatedResponse

router = APIRouter()


@router.get("/", response_model=PaginatedResponse)
async def get_pets(
    search: Optional[str] = Query(None, description="Search pets by name"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page")
):
    db = get_database()
    
    query = {}
    if search:
        query["$or"] = [
        {"name": {"$regex": search, "$options": "i"}},
        {"breed": {"$regex": search, "$options": "i"}},
        {"species": {"$regex": search, "$options": "i"}},
        ]
    
    skip = (page - 1) * limit
    
    cursor = db.pets.find(query).skip(skip).limit(limit)
    pets = await cursor.to_list(length=limit)
    
    total = await db.pets.count_documents(query)
    total_pages = math.ceil(total / limit)
    
    pets_response = []
    for pet in pets:
        pet = convert_object_id(pet)
        pets_response.append(PetResponse(**pet))
    
    return PaginatedResponse(
        pets=pets_response,
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )


@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(pet_id: str):
    db = get_database()
    
    if not ObjectId.is_valid(pet_id):
        raise HTTPException(status_code=400, detail="Invalid pet ID format")
    
    pet = await db.pets.find_one({"_id": ObjectId(pet_id)})
    
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    pet = convert_object_id(pet)
    return PetResponse(**pet)