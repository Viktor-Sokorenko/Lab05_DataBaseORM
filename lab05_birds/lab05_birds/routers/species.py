from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from database import get_session
from models.species import Species, SpeciesCreate
from repositories.species import SpeciesRepository

router = APIRouter(prefix="/species", tags=["Species"])

def get_species_repository(session: Annotated[Session, Depends(get_session)]) -> SpeciesRepository:
    return SpeciesRepository(session)

@router.get("/", response_model=list[Species], summary="Get all species")
async def get_species(repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Return all bird species from the database."""
    return repo.get_all()

@router.get("/{species_id}", response_model=Species, summary="Get one species")
async def get_one_species(species_id: int, repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Return one species by id."""
    item = repo.get_one(species_id)
    if not item:
        raise HTTPException(status_code=404, detail="Species not found.")
    return item

@router.post("/", response_model=Species, status_code=status.HTTP_201_CREATED, summary="Create a species")
async def add_species(species: SpeciesCreate, repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Insert a new species into PostgreSQL."""
    return repo.insert(species)
