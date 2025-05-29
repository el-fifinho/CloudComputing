# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from app.core.database import SessionLocal
# from app.core.security import get_current_user
# from app.repositories.field_repository import FieldRepository
# from app.repositories.availability_repository import AvailabilityRepository
# from app.repositories.rental_repository import RentalRepository
# from app.repositories.notification_repository import NotificationRepository
# from app.schemas.field import FieldRead, FieldUpdate
# from app.schemas.availability import AvailabilityCreate, AvailabilityRead
# from app.schemas.rental import RentalRead
# from app.schemas.notification import NotificationRead

# router = APIRouter(prefix="/owners", tags=["owner"])

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/me/fields", response_model=List[FieldRead])
# def list_my_fields(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all fields owned by the current owner."""
#     repo = FieldRepository(db)
#     return repo.get_by_owner(current_user["user_id"])

# @router.get("/fields/{field_id}", response_model=FieldRead)
# def get_field(
#     field_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Get full details for an owned field."""
#     repo = FieldRepository(db)
#     field = repo.get_by_id(field_id)
#     if not field or field.owner_id != current_user["user_id"]:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
#     return field

# @router.put("/fields/{field_id}", response_model=FieldRead)
# def update_field(
#     field_id: int,
#     field_in: FieldUpdate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Update metadata for an owned field."""
#     repo = FieldRepository(db)
#     return repo.update(field_id, field_in)

# @router.get("/fields/{field_id}/availabilities", response_model=List[AvailabilityRead])
# def list_availabilities(
#     field_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List availability slots for an owned field."""
#     repo = AvailabilityRepository(db)
#     return repo.get_for_field(field_id, owner_id=current_user["user_id"])

# @router.post("/fields/{field_id}/availabilities", response_model=AvailabilityRead, status_code=status.HTTP_201_CREATED)
# def create_availability(
#     field_id: int,
#     avail_in: AvailabilityCreate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Create a new availability window."""
#     repo = AvailabilityRepository(db)
#     return repo.add(field_id=field_id, start_time=avail_in.start_time, end_time=avail_in.end_time)

# @router.patch("/availabilities/{availability_id}", response_model=AvailabilityRead)
# def cancel_availability(
#     availability_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Cancel an existing availability slot."""
#     repo = AvailabilityRepository(db)
#     return repo.cancel(availability_id)

# @router.get("/me/rentals", response_model=List[RentalRead])
# def list_rentals(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all rentals for this owner's fields."""
#     repo = RentalRepository(db)
#     return repo.get_for_owner(current_user["user_id"])

# @router.patch("/rentals/{rental_id}/cancel", response_model=RentalRead)
# def cancel_rental(
#     rental_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Allow the owner to cancel a rental."""
#     repo = RentalRepository(db)
#     return repo.cancel(rental_id)

# @router.get("/me/notifications", response_model=List[NotificationRead])
# def list_notifications(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all notifications for the current owner."""
#     repo = NotificationRepository(db)
#     return repo.list(current_user["user_id"])

# @router.patch("/notifications/{notification_id}/read", response_model=NotificationRead)
# def mark_notification_read(
#     notification_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Mark a notification as read."""
#     repo = NotificationRepository(db)
#     return repo.mark_as_read(notification_id)

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from app.core.database import SessionLocal
# from app.core.security import get_current_user
# from app.repositories.field_repository import FieldRepository
# from app.repositories.availability_repository import AvailabilityRepository
# from app.repositories.rental_repository import RentalRepository
# from app.repositories.notification_repository import NotificationRepository
# from app.schemas.field import FieldRead, FieldUpdate
# from app.schemas.availability import AvailabilityCreate, AvailabilityRead
# from app.schemas.rental import RentalRead
# from app.schemas.notification import NotificationRead

# router = APIRouter(tags=["owner"])

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/owners/me/fields/", response_model=List[FieldRead])
# def list_my_fields(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all fields owned by the current owner."""
#     repo = FieldRepository(db)
#     return repo.get_by_owner(current_user["user_id"])

# @router.get("/owners/fields/{field_id}/", response_model=FieldRead)
# def get_field(
#     field_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Get full details for an owned field."""
#     repo = FieldRepository(db)
#     field = repo.get_by_id(field_id)
#     if not field or field.venue.owner_id != current_user["user_id"]:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
#     return field

# @router.put("/owners/fields/{field_id}/", response_model=FieldRead)
# def update_field(
#     field_id: int,
#     field_in: FieldUpdate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Update metadata for an owned field."""
#     repo = FieldRepository(db)
#     return repo.update(field_id, field_in)

# @router.get("/owners/fields/{field_id}/availabilities/", response_model=List[AvailabilityRead])
# def list_availabilities(
#     field_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List availability slots for an owned field."""
#     repo = AvailabilityRepository(db)
#     return repo.get_for_field(field_id, owner_id=current_user["user_id"])

# @router.post("/owners/fields/{field_id}/availabilities/", response_model=AvailabilityRead, status_code=status.HTTP_201_CREATED)
# def create_availability(
#     field_id: int,
#     avail_in: AvailabilityCreate,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Create a new availability window."""
#     repo = AvailabilityRepository(db)
#     return repo.add(field_id=field_id, start_time=avail_in.start_time, end_time=avail_in.end_time)

# @router.patch("/owners/availabilities/{availability_id}/", response_model=AvailabilityRead)
# def cancel_availability(
#     availability_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Cancel an existing availability slot."""
#     repo = AvailabilityRepository(db)
#     return repo.cancel(availability_id)

# @router.get("/owners/me/rentals/", response_model=List[RentalRead])
# def list_rentals(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all rentals for this owner's fields."""
#     repo = RentalRepository(db)
#     return repo.get_for_owner(current_user["user_id"])

# @router.patch("/owners/rentals/{rental_id}/cancel/", response_model=RentalRead)
# def cancel_rental(
#     rental_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Allow the owner to cancel a rental."""
#     repo = RentalRepository(db)
#     return repo.cancel(rental_id)

# @router.get("/owners/me/notifications/", response_model=List[NotificationRead])
# def list_notifications(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """List all notifications for the current owner."""
#     repo = NotificationRepository(db)
#     return repo.list(current_user["user_id"])

# @router.patch("/owners/notifications/{notification_id}/read/", response_model=NotificationRead)
# def mark_notification_read(
#     notification_id: int,
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Mark a notification as read."""
#     repo = NotificationRepository(db)
#     return repo.mark_as_read(notification_id)

# services/sportfields-service/app/routers/owner.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.repositories.field_repository import FieldRepository
from app.repositories.availability_repository import AvailabilityRepository
from app.repositories.rental_repository import RentalRepository
from app.repositories.notification_repository import NotificationRepository
from app.schemas.field import FieldRead, FieldUpdate
from app.schemas.availability import AvailabilityCreate, AvailabilityRead
from app.schemas.rental import RentalRead
from app.schemas.notification import NotificationRead

router = APIRouter(tags=["owner"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/owners/me/fields/", response_model=List[FieldRead])
def list_my_fields(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all fields owned by the current owner."""
    repo = FieldRepository(db)
    return repo.get_by_owner(current_user["user_id"])

@router.get("/owners/fields/{field_id}/", response_model=FieldRead)
def get_field(
    field_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get full details for an owned field."""
    repo = FieldRepository(db)
    field = repo.get_by_id(field_id)
    if not field or field.venue.owner_id != current_user["user_id"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
    return field

@router.put("/owners/fields/{field_id}/", response_model=FieldRead)
def update_field(
    field_id: int,
    field_in: FieldUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update metadata for an owned field."""
    # Verify ownership
    repo_field = FieldRepository(db)
    field = repo_field.get_by_id(field_id)
    if not field or field.venue.owner_id != current_user["user_id"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
    return repo_field.update(field_id, field_in)

@router.get("/owners/fields/{field_id}/availabilities/", response_model=List[AvailabilityRead])
def list_availabilities(
    field_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List availability slots for an owned field."""
    # Verify ownership
    field = FieldRepository(db).get_by_id(field_id)
    if not field or field.venue.owner_id != current_user["user_id"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
    repo = AvailabilityRepository(db)
    return repo.get_for_field(field_id)

@router.post("/owners/fields/{field_id}/availabilities/", response_model=AvailabilityRead, status_code=status.HTTP_201_CREATED)
def create_availability(
    field_id: int,
    avail_in: AvailabilityCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new availability window."""
    # Verify ownership
    field = FieldRepository(db).get_by_id(field_id)
    if not field or field.venue.owner_id != current_user["user_id"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Field not found or unauthorized")
    repo = AvailabilityRepository(db)
    return repo.add(field_id=field_id, start_time=avail_in.start_time, end_time=avail_in.end_time)

@router.patch("/owners/availabilities/{availability_id}/", response_model=AvailabilityRead)
def cancel_availability(
    availability_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cancel an existing availability slot."""
    repo = AvailabilityRepository(db)
    return repo.cancel(availability_id)

@router.get("/owners/me/rentals/", response_model=List[RentalRead])
def list_rentals(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all rentals for this owner's fields."""
    repo = RentalRepository(db)
    return repo.get_for_owner(current_user["user_id"])

@router.patch("/owners/rentals/{rental_id}/cancel/", response_model=RentalRead)
def cancel_rental(
    rental_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Allow the owner to cancel a rental."""
    repo = RentalRepository(db)
    return repo.cancel(rental_id)

@router.get("/owners/me/notifications/", response_model=List[NotificationRead])
def list_notifications(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all notifications for the current owner."""
    repo = NotificationRepository(db)
    return repo.list(current_user["user_id"])

@router.patch("/owners/notifications/{notification_id}/read/", response_model=NotificationRead)
def mark_notification_read(
    notification_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mark a notification as read."""
    repo = NotificationRepository(db)
    return repo.mark_as_read(notification_id)