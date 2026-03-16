from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import start_db
from routers.species import router as species_router
from routers.birds import router as birds_router
from routers.birdspotting import router as birdspotting_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_db()
    yield

app = FastAPI(
    title="Bird API",
    version="1.0.0",
    lifespan=lifespan,
    description="A FastAPI + SQLModel project with Species, Birds and Birdspotting resources.",
)

@app.get("/", summary="Root test route")
async def root():
    """Simple test route to verify the API is running."""
    return {"message": "Hello World"}

app.include_router(species_router)
app.include_router(birds_router)
app.include_router(birdspotting_router)
