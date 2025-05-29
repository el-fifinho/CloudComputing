# from sqlalchemy import Column, BigInteger, DateTime, Numeric, Enum, ForeignKey, CHAR
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# import enum
# from app.core.database import Base

# class RentalStatus(enum.Enum):
#     pending = "pending"
#     confirmed = "confirmed"
#     cancelled = "cancelled"
#     completed = "completed"

# class Rental(Base):
#     __tablename__ = "rentals"

#     rental_id = Column(BigInteger, primary_key=True, index=True)
#     field_id = Column(BigInteger, ForeignKey("fields.field_id", ondelete="CASCADE"), nullable=False)
#     renter_id = Column(CHAR(36), nullable=False)
#     availability_id = Column(BigInteger, ForeignKey("availabilities.availability_id", ondelete="SET NULL"), nullable=True)
#     start_time = Column(DateTime(timezone=True), nullable=False)
#     end_time = Column(DateTime(timezone=True), nullable=False)
#     price = Column(Numeric(10,2), nullable=False)
#     status = Column(Enum(RentalStatus), nullable=False, default=RentalStatus.pending)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
#     updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

#     field = relationship("Field", back_populates="rentals")
#     reviews = relationship("Review", back_populates="rental", uselist=False)

from sqlalchemy import Column, BigInteger, DateTime, Numeric, Enum, ForeignKey, CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

class RentalStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class Rental(Base):
    __tablename__ = "rentals"

    rental_id = Column(BigInteger, primary_key=True, index=True)
    field_id = Column(BigInteger, ForeignKey("fields.field_id", ondelete="CASCADE"), nullable=False)
    renter_id = Column(CHAR(36), nullable=False)
    availability_id = Column(BigInteger, ForeignKey("availabilities.availability_id", ondelete="SET NULL"), nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    status = Column(Enum(RentalStatus), nullable=False, default=RentalStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    field = relationship("Field", back_populates="rentals")
    reviews = relationship("Review", back_populates="rental", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="rental", cascade="all, delete-orphan")