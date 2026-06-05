from domain.interfaces.i_notification import INotification
from infrastructure.notifications.notifications import (
    EmailNotification,
    SMSNotification,
    PushNotification
)

class NotificationFactory:
    @staticmethod
    def create(notification_type: str) -> INotification:
        types = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification
        }

        cls = types.get(notification_type.lower())
        if cls is None:
            raise ValueError(f"Geçersiz bildirim tipi: {notification_type}")
        return cls()