from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from models.birds import BirdRead

class BirdspottingBase(SQLModel):
    bird_id: int
    spotted_at: datetime
    location: str
    observer_name: str
    notes: Optional[str] = None

class Birdspotting(BirdspottingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bird: Optional["Bird"] = Relationship(back_populates="sightings")

class BirdspottingCreate(BirdspottingBase):
    pass

class BirdspottingRead(BirdspottingBase):
    id: int

class BirdspottingReadWithBird(BirdspottingRead):
    bird: Optional[BirdRead] = None
