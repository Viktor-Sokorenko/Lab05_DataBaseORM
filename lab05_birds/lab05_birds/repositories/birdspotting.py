from fastapi import HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from models.birdspotting import Birdspotting, BirdspottingCreate
from models.birds import Bird

class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Birdspotting).options(
            selectinload(Birdspotting.bird).selectinload(Bird.species)
        )
        return self.session.exec(statement).all()

    def get_one(self, birdspotting_id: int):
        statement = (
            select(Birdspotting)
            .where(Birdspotting.id == birdspotting_id)
            .options(selectinload(Birdspotting.bird).selectinload(Bird.species))
        )
        return self.session.exec(statement).first()

    def insert(self, payload: BirdspottingCreate):
        bird = self.session.get(Bird, payload.bird_id)
        if not bird:
            raise HTTPException(status_code=400, detail="bird_id does not exist.")

        item = Birdspotting.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item
