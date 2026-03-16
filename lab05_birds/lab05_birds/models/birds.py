from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.species import Species
    from models.birdspotting import Birdspotting

class BirdBase(SQLModel):
    nickname: str
    ring_code: str
    age: int

class Bird(BirdBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    species_id: int = Field(foreign_key="species.id")
    species: Optional["Species"] = Relationship(back_populates="birds")
    sightings: list["Birdspotting"] = Relationship(back_populates="bird")

class BirdCreate(BirdBase):
    species_id: int

class BirdRead(BirdBase):
    id: int
    species_id: int
