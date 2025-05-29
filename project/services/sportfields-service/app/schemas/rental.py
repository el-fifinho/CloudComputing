from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class RentalStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class RentalBase(BaseModel):
    field_id: int
    start_time: datetime
    end_time: datetime
    price: float

class RentalCreate(RentalBase):
    pass

class RentalRead(RentalBase):
    rental_id: int
    renter_id: str
    availability_id: Optional[int]
    status: RentalStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True