from fastapi import HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from models.birds import Bird, BirdCreate
from models.species import Species

class BirdRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Bird).options(selectinload(Bird.species))
        return self.session.exec(statement).all()

    def get_one(self, bird_id: int):
        statement = select(Bird).where(Bird.id == bird_id).options(selectinload(Bird.species))
        return self.session.exec(statement).first()

    def insert(self, payload: BirdCreate):
        species = self.session.get(Species, payload.species_id)
        if not species:
            raise HTTPException(status_code=400, detail="species_id does not exist.")

        existing = self.session.exec(select(Bird).where(Bird.ring_code == payload.ring_code)).first()
        if existing:
            raise HTTPException(status_code=409, detail="ring_code must be unique.")

        item = Bird.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item
