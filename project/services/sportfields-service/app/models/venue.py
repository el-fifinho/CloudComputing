# from sqlalchemy import Column, BigInteger, String, Text, DateTime, CHAR
# from sqlalchemy.sql import func
# from app.core.database import Base

# class Venue(Base):
#     __tablename__ = "venues"

#     venue_id = Column(BigInteger, primary_key=True, index=True)
#     owner_id = Column(CHAR(36), nullable=False)
#     name = Column(String(150), nullable=False)
#     description = Column(Text, nullable=True)
#     address = Column(String(255), nullable=True)
#     city = Column(String(100), nullable=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
#     updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

from sqlalchemy import Column, BigInteger, String, Text, DateTime, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Venue(Base):
    __tablename__ = "venues"

    venue_id = Column(BigInteger, primary_key=True, index=True)
    owner_id = Column(CHAR(36), nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship: one venue has many fields
    fields = relationship("Field", back_populates="venue", cascade="all, delete-orphan")