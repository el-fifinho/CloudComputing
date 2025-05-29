from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewCreate(BaseModel):
    rating: int
    comment: Optional[str] = None

class ReviewRead(ReviewCreate):
    review_id: int
    rental_id: int
    reviewer_id: str
    created_at: datetime

    class Config:
        orm_mode = True