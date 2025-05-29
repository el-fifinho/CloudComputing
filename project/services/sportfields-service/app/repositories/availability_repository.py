from sqlalchemy.orm import Session
from datetime import datetime

from app.models.availability import Availability

class AvailabilityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_for_field(self, field_id: int) -> list[Availability]:
        return (
            self.db.query(Availability)
            .filter(Availability.field_id == field_id)
            .all()
        )

    def add(
        self,
        field_id: int,
        start_time: datetime,
        end_time: datetime
    ) -> Availability:
        avail = Availability(
            field_id=field_id,
            start_time=start_time,
            end_time=end_time
        )
        self.db.add(avail)
        self.db.commit()
        self.db.refresh(avail)
        return avail

    def cancel(self, availability_id: int) -> Availability | None:
        avail = (
            self.db.query(Availability)
            .filter(Availability.availability_id == availability_id)
            .first()
        )
        if not avail:
            return None
        avail.is_cancelled = True
        self.db.commit()
        self.db.refresh(avail)
        return avail