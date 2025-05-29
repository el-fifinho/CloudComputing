from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, not_
from datetime import datetime

from app.models.field import Field
from app.models.venue import Venue
from app.models.sport import Sport
from app.models.availability import Availability
from app.models.rental import Rental

class FieldRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, field_id: int) -> Field | None:
        return (
            self.db.query(Field)
            .filter(Field.field_id == field_id)
            .first()
        )

    def get_by_owner(self, owner_id: str) -> list[Field]:
        return (
            self.db.query(Field)
            .join(Venue, Field.venue_id == Venue.venue_id)
            .filter(Venue.owner_id == owner_id)
            .all()
        )

    def search(
        self,
        name: str = None,
        sport_id: int = None,
        city: str = None,
        start_time: datetime = None,
        end_time: datetime = None
    ) -> list[Field]:
        query = (
            self.db.query(Field)
            .join(Venue, Field.venue_id == Venue.venue_id)
            .join(Sport, Field.sport_id == Sport.sport_id)
        )
        if name:
            query = query.filter(Field.name.ilike(f"%{name}%"))
        if sport_id:
            query = query.filter(Field.sport_id == sport_id)
        if city:
            query = query.filter(Venue.city == city)

        if start_time and end_time:
            # Available slot covers requested window
            subq = (
                self.db.query(Availability.field_id)
                .filter(
                    Availability.field_id == Field.field_id,
                    Availability.start_time <= start_time,
                    Availability.end_time >= end_time
                )
                .subquery()
            )
            # No overlapping confirmed rentals
            conflict = (
                self.db.query(Rental)
                .filter(
                    Rental.field_id == Field.field_id,
                    Rental.status != 'cancelled',
                    not_(
                        or_(
                            Rental.end_time <= start_time,
                            Rental.start_time >= end_time
                        )
                    )
                )
                .exists()
            )
            query = query.filter(Field.field_id.in_(subq)).filter(~conflict)

        return query.all()

    def update(self, field_id: int, field_in) -> Field | None:
        field = self.get_by_id(field_id)
        if not field:
            return None
        for attr, value in field_in.dict(exclude_unset=True).items():
            setattr(field, attr, value)
        self.db.commit()
        self.db.refresh(field)
        return field