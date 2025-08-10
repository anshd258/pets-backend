from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from database.database import connect_to_mongo, close_mongo_connection
from routes import pets, adoptions, favorites
from core.utils.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()


app = FastAPI(
    title="Pet Adoption API",
    description="Backend API for Pet Adoption Application",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pets.router, prefix="/pets", tags=["pets"])
app.include_router(adoptions.router, tags=["adoptions"])
app.include_router(favorites.router, tags=["favorites"])


@app.get("/")
async def root():
    return {"message": "Pet Adoption API", "version": "1.0.0"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
