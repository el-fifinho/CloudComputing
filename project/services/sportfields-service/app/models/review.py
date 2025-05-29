# from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, ForeignKey, CHAR
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Review(Base):
#     __tablename__ = "reviews"

#     review_id = Column(BigInteger, primary_key=True, index=True)
#     rental_id = Column(BigInteger, ForeignKey("rentals.rental_id", ondelete="CASCADE"), nullable=False, unique=True)
#     reviewer_id = Column(CHAR(36), nullable=False)
#     rating = Column(Integer, nullable=False)
#     comment = Column(Text, nullable=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

#     rental = relationship("Rental", back_populates="reviews")

from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, ForeignKey, CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(BigInteger, primary_key=True, index=True)
    rental_id = Column(BigInteger, ForeignKey("rentals.rental_id", ondelete="CASCADE"), nullable=False, unique=True)
    reviewer_id = Column(CHAR(36), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationship
    rental = relationship("Rental", back_populates="reviews")