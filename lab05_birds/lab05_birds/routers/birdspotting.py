from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from database import get_session
from models.birdspotting import BirdspottingCreate, BirdspottingReadWithBird
from repositories.birdspotting import BirdspottingRepository

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])

def get_birdspotting_repository(session: Annotated[Session, Depends(get_session)]) -> BirdspottingRepository:
    return BirdspottingRepository(session)

@router.get("/", response_model=list[BirdspottingReadWithBird], summary="Get all birdspotting records")
async def get_birdspotting(repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    """Return all birdspotting observations with the linked bird."""
    return repo.get_all()

@router.get("/{birdspotting_id}", response_model=BirdspottingReadWithBird, summary="Get one birdspotting record")
async def get_one_birdspotting(birdspotting_id: int, repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    """Return one birdspotting observation by id, including its bird."""
    item = repo.get_one(birdspotting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Birdspotting record not found.")
    return item

@router.post("/", response_model=BirdspottingReadWithBird, status_code=status.HTTP_201_CREATED, summary="Create a birdspotting record")
async def add_birdspotting(birdspotting: BirdspottingCreate, repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    """Insert a new observation linked to an existing bird."""
    return repo.insert(birdspotting)
