# from sqlalchemy import Column, BigInteger, DateTime, Boolean, ForeignKey
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Availability(Base):
#     __tablename__ = "availabilities"

#     availability_id = Column(BigInteger, primary_key=True, index=True)
#     field_id = Column(BigInteger, ForeignKey("fields.field_id", ondelete="CASCADE"), nullable=False)
#     start_time = Column(DateTime(timezone=True), nullable=False)
#     end_time = Column(DateTime(timezone=True), nullable=False)
#     is_cancelled = Column(Boolean, nullable=False, default=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

#     field = relationship("Field", back_populates="availabilities")

from sqlalchemy import Column, BigInteger, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Availability(Base):
    __tablename__ = "availabilities"

    availability_id = Column(BigInteger, primary_key=True, index=True)
    field_id = Column(BigInteger, ForeignKey("fields.field_id", ondelete="CASCADE"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    is_cancelled = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationship
    field = relationship("Field", back_populates="availabilities")