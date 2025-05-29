# from sqlalchemy import Column, BigInteger, CHAR, Text, Boolean, DateTime, ForeignKey
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Notification(Base):
#     __tablename__ = "notifications"

#     notification_id = Column(BigInteger, primary_key=True, index=True)
#     owner_id = Column(CHAR(36), nullable=False)
#     rental_id = Column(BigInteger, ForeignKey("rentals.rental_id", ondelete="CASCADE"), nullable=False)
#     message = Column(Text, nullable=False)
#     is_read = Column(Boolean, nullable=False, default=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

#     rental = relationship("Rental", back_populates="notifications")

from sqlalchemy import Column, BigInteger, CHAR, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(BigInteger, primary_key=True, index=True)
    owner_id = Column(CHAR(36), nullable=False)
    rental_id = Column(BigInteger, ForeignKey("rentals.rental_id", ondelete="CASCADE"), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationship
    rental = relationship("Rental", back_populates="notifications")