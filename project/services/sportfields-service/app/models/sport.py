# from sqlalchemy import Column, Integer, String, Text, DateTime
# from sqlalchemy.sql import func
# from app.core.database import Base

# class Sport(Base):
#     __tablename__ = "sports"

#     sport_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), unique=True, nullable=False)
#     description = Column(Text, nullable=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Sport(Base):
    __tablename__ = "sports"

    sport_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationship: one sport has many fields
    fields = relationship("Field", back_populates="sport", cascade="all, delete-orphan")