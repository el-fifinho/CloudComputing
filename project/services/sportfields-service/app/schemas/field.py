from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FieldBase(BaseModel):
    name: str
    description: Optional[str] = None
    price_per_hour: float
    sport_id: int  # reference to Sport

class FieldCreate(FieldBase):
    venue_id: int

class FieldUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price_per_hour: Optional[float] = None
    sport_id: Optional[int] = None

class FieldRead(FieldBase):
    field_id: int
    venue_id: int
    created_at: datetime
    updated_at: datetime
    # Optional nested:
    # sport: SportRead
    # venue: VenueRead

    class Config:
        orm_mode = True