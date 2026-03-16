from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.birds import Bird

class SpeciesBase(SQLModel):
    name: str
    scientific_name: str
    family: str
    conservation_status: str
    wingspan_cm: Decimal

class Species(SpeciesBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    birds: list["Bird"] = Relationship(back_populates="species")

class SpeciesCreate(SpeciesBase):
    pass
