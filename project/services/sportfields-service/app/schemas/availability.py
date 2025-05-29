from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AvailabilityBase(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilityCreate(AvailabilityBase):
    pass

class AvailabilityRead(AvailabilityBase):
    availability_id: int
    field_id: int
    is_cancelled: bool
    created_at: datetime

    class Config:
        orm_mode = True