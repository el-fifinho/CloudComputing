from pydantic import BaseModel
from datetime import datetime

class SportRead(BaseModel):
    sport_id: int
    name: str
    description: str | None
    created_at: datetime

    class Config:
        orm_mode = True