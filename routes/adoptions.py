from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId

from database.database import get_database, convert_object_id
from models.models import AdoptionResponse, Adoption, PetResponse

router = APIRouter()


@router.post("/adopt/{pet_id}", response_model=AdoptionResponse)
async def adopt_pet(pet_id: str):
    db = get_database()
    
    if not ObjectId.is_valid(pet_id):
        raise HTTPException(status_code=400, detail="Invalid pet ID format")
    
    pet = await db.pets.find_one({"_id": ObjectId(pet_id)})
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    if pet.get("is_adopted", False):
        raise HTTPException(status_code=400, detail="Pet is already adopted")
    
    adopted_at = datetime.utcnow()
    
    await db.pets.update_one(
        {"_id": ObjectId(pet_id)},
        {"$set": {"is_adopted": True}}
    )
    
    adoption = Adoption(pet_id=pet_id, adopted_at=adopted_at)
    await db.adoptions.insert_one(adoption.dict())
    
    return AdoptionResponse(
        message="Pet adopted successfully",
        pet_id=pet_id,
        adopted_at=adopted_at
    )


@router.get("/history")
async def get_adoption_history():
    db = get_database()
    
    cursor = db.adoptions.find().sort("adopted_at", -1)
    adoptions = await cursor.to_list(length=None)
    
    adopted_pets = []
    for adoption in adoptions:
        pet = await db.pets.find_one({"_id": ObjectId(adoption["pet_id"])})
        if pet:
            pet = convert_object_id(pet)
            pet_response = PetResponse(**pet)
            adopted_pets.append({
                "pet": pet_response.dict(),
                "adopted_at": adoption["adopted_at"]
            })
    
    return adopted_pets