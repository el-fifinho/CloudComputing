from sqlalchemy.orm import Session

from app.models.review import Review

class ReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(
        self,
        rental_id: int,
        reviewer_id: str,
        rating: int,
        comment: str | None = None
    ) -> Review:
        review = Review(
            rental_id=rental_id,
            reviewer_id=reviewer_id,
            rating=rating,
            comment=comment
        )
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review