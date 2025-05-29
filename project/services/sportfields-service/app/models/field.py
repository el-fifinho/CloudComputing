# from sqlalchemy import Column, BigInteger, Integer, String, Text, Numeric, DateTime, ForeignKey
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Field(Base):
#     __tablename__ = "fields"

#     field_id = Column(BigInteger, primary_key=True, index=True)
#     venue_id = Column(BigInteger, ForeignKey("venues.venue_id", ondelete="CASCADE"), nullable=False)
#     sport_id = Column(Integer, ForeignKey("sports.sport_id", ondelete="RESTRICT"), nullable=False)
#     name = Column(String(120), nullable=False)
#     description = Column(Text, nullable=True)
#     price_per_hour = Column(Numeric(10, 2), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
#     updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

#     venue = relationship("Venue", back_populates="fields")
#     sport = relationship("Sport", back_populates="fields")

from sqlalchemy import Column, BigInteger, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Field(Base):
    __tablename__ = "fields"

    field_id = Column(BigInteger, primary_key=True, index=True)
    venue_id = Column(BigInteger, ForeignKey("venues.venue_id", ondelete="CASCADE"), nullable=False)
    sport_id = Column(Integer, ForeignKey("sports.sport_id", ondelete="RESTRICT"), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=True)
    price_per_hour = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    venue = relationship("Venue", back_populates="fields")
    sport = relationship("Sport", back_populates="fields")
    availabilities = relationship("Availability", back_populates="field", cascade="all, delete-orphan")
    rentals = relationship("Rental", back_populates="field", cascade="all, delete-orphan")