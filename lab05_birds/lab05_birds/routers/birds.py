from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from database import get_session
from models.birds import Bird, BirdCreate
from repositories.birds import BirdRepository

router = APIRouter(prefix="/birds", tags=["Birds"])

def get_bird_repository(session: Annotated[Session, Depends(get_session)]) -> BirdRepository:
    return BirdRepository(session)

@router.get("/", response_model=list[Bird], summary="Get all birds")
async def get_birds(repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Return all birds and their linked species."""
    return repo.get_all()

@router.get("/{bird_id}", response_model=Bird, summary="Get one bird")
async def get_one_bird(bird_id: int, repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Return one bird by id."""
    item = repo.get_one(bird_id)
    if not item:
        raise HTTPException(status_code=404, detail="Bird not found.")
    return item

@router.post("/", response_model=Bird, status_code=status.HTTP_201_CREATED, summary="Create a bird")
async def add_bird(bird: BirdCreate, repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Insert a bird linked to an existing species."""
    return repo.insert(bird)
