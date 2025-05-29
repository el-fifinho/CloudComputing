from sqlalchemy.orm import Session

from app.models.notification import Notification

class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(
        self,
        owner_id: str,
        only_unread: bool = False
    ) -> list[Notification]:
        query = self.db.query(Notification).filter(Notification.owner_id == owner_id)
        if only_unread:
            query = query.filter(Notification.is_read == False)
        return query.order_by(Notification.created_at.desc()).all()

    def mark_as_read(
        self,
        notification_id: int
    ) -> Notification | None:
        notif = (
            self.db.query(Notification)
            .filter(Notification.notification_id == notification_id)
            .first()
        )
        if not notif:
            return None
        notif.is_read = True
        self.db.commit()
        self.db.refresh(notif)
        return notif