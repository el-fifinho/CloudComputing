from sqlalchemy.orm import Session
from datetime import datetime

from app.models.rental import Rental, RentalStatus
from app.models.availability import Availability
from app.models.field import Field
from app.models.venue import Venue

class RentalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        field_id: int,
        renter_id: str,
        start_time: datetime,
        end_time: datetime,
        price: float
    ) -> Rental:
        rental = Rental(
            field_id=field_id,
            renter_id=renter_id,
            start_time=start_time,
            end_time=end_time,
            price=price,
            status=RentalStatus.confirmed
        )
        self.db.add(rental)
        # Mark corresponding availability as cancelled
        (
            self.db.query(Availability)
            .filter(
                Availability.field_id == field_id,
                Availability.start_time <= start_time,
                Availability.end_time >= end_time
            )
            .update({"is_cancelled": True})
        )
        self.db.commit()
        self.db.refresh(rental)
        return rental

    def get_history(self, renter_id: str) -> list[Rental]:
        return (
            self.db.query(Rental)
            .filter(
                Rental.renter_id == renter_id,
                Rental.status == RentalStatus.completed
            )
            .order_by(Rental.start_time.desc())
            .all()
        )

    def get_for_owner(self, owner_id: str) -> list[Rental]:
        return (
            self.db.query(Rental)
            .join(Field, Rental.field_id == Field.field_id)
            .join(Venue, Field.venue_id == Venue.venue_id)
            .filter(Venue.owner_id == owner_id)
            .all()
        )

    def cancel(self, rental_id: int) -> Rental | None:
        rental = (
            self.db.query(Rental)
            .filter(Rental.rental_id == rental_id)
            .first()
        )
        if not rental:
            return None
        rental.status = RentalStatus.cancelled
        self.db.commit()
        self.db.refresh(rental)
        return rental