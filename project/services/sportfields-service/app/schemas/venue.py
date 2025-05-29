from pydantic import BaseModel
from datetime import datetime

class VenueRead(BaseModel):
    venue_id: int
    owner_id: str
    name: str
    description: str | None
    address: str | None
    city: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True