# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from app.core.database import SessionLocal
# from app.core.security import get_current_user
# from app.repositories.field_repository import FieldRepository
# from app.repositories.rental_repository import RentalRepository
# from app.repositories.review_repository import ReviewRepository
# from app.schemas.field import FieldRead
# from app.schemas.rental import RentalCreate, RentalRead
# from app.schemas.review import ReviewCreate, ReviewRead

# router = APIRouter(prefix="/fields", tags=["simple-user"])

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/", response_model=List[FieldRead])
# def search_fields(
#     name: str = None,
#     sport_id: int = None,
#     city: str = None,
#     start_time: str = None,
#     end_time: str = None,
#     db: Session = Depends(get_db)
# ):
#     """
#     Search for fields by optional filters: name, sport, city, availability window.
#     """
#     repo = FieldRepository(db)
#     return repo.search(name=name, sport_id=sport_id, city=city, start_time=start_time, end_time=end_time)

# @router.get("/{field_id}", response_model=FieldRead)
# def get_field_details(
#     field_id: int,
#     db: Session = Depends(get_db)
# ):
#     """Get full details for a single field."""
#     repo = FieldRepository(db)
#     field = repo.get_by_id(field_id)
#     if not field:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
#     return field

# @router.post("/rentals", response_model=RentalRead, status_code=status.HTTP_201_CREATED)
# def book_field(
#     rental_in: RentalCreate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Create a rental for the current simple user."""
#     repo = RentalRepository(db)
#     rental = repo.create(
#         field_id=rental_in.field_id,
#         renter_id=current_user["user_id"],
#         start_time=rental_in.start_time,
#         end_time=rental_in.end_time,
#         price=rental_in.price
#     )
#     return rental

# @router.get("/users/me/rentals", response_model=List[RentalRead])
# def get_my_rentals(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Fetch past and current rentals for the logged-in simple user."""
#     repo = RentalRepository(db)
#     return repo.get_history(current_user["user_id"])

# @router.post("/rentals/{rental_id}/reviews", response_model=ReviewRead)
# def add_review(
#     rental_id: int,
#     review_in: ReviewCreate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Leave a review for a completed rental."""
#     # You may add logic to verify rental status == completed
#     repo = ReviewRepository(db)
#     review = repo.add(
#         rental_id=rental_id,
#         reviewer_id=current_user["user_id"],
#         rating=review_in.rating,
#         comment=review_in.comment
#     )
#     return review

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.repositories.field_repository import FieldRepository
from app.repositories.rental_repository import RentalRepository
from app.repositories.review_repository import ReviewRepository
from app.schemas.field import FieldRead
from app.schemas.rental import RentalCreate, RentalRead
from app.schemas.review import ReviewCreate, ReviewRead

router = APIRouter(tags=["simple-user"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/fields/", response_model=List[FieldRead])
def search_fields(
    name: str = None,
    sport_id: int = None,
    city: str = None,
    start_time: str = None,
    end_time: str = None,
    db: Session = Depends(get_db)
):
    """
    Search for fields by optional filters: name, sport, city, availability window.
    """
    repo = FieldRepository(db)
    return repo.search(name=name, sport_id=sport_id, city=city, start_time=start_time, end_time=end_time)

@router.get("/fields/{field_id}", response_model=FieldRead)
def get_field_details(
    field_id: int,
    db: Session = Depends(get_db)
):
    """Get full details for a single field."""
    repo = FieldRepository(db)
    field = repo.get_by_id(field_id)
    if not field:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
    return field

@router.post("/rentals/", response_model=RentalRead, status_code=status.HTTP_201_CREATED)
def book_field(
    rental_in: RentalCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a rental for the current simple user."""
    repo = RentalRepository(db)
    rental = repo.create(
        field_id=rental_in.field_id,
        renter_id=current_user["user_id"],
        start_time=rental_in.start_time,
        end_time=rental_in.end_time,
        price=rental_in.price
    )
    return rental

@router.get("/users/me/rentals/", response_model=List[RentalRead])
def get_my_rentals(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Fetch past and current rentals for the logged-in simple user."""
    repo = RentalRepository(db)
    return repo.get_history(current_user["user_id"])

@router.post("/rentals/{rental_id}/reviews/", response_model=ReviewRead)
def add_review(
    rental_id: int,
    review_in: ReviewCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Leave a review for a completed rental."""
    repo = ReviewRepository(db)
    review = repo.add(
        rental_id=rental_id,
        reviewer_id=current_user["user_id"],
        rating=review_in.rating,
        comment=review_in.comment
    )
    return review