from domain.interfaces.i_announcement import IAnnouncement
from domain.models.announcements import (
    ExamAnnouncement,
    EventAnnouncement,
    FoodMenuAnnouncement,
    LibraryAnnouncement
)

class AnnouncementFactory:
    @staticmethod
    def create(announcement_type: str, title: str, content: str) -> IAnnouncement:
        types = {
            "sinav": ExamAnnouncement,
            "etkinlik": EventAnnouncement,
            "yemekhane": FoodMenuAnnouncement,
            "kutuphane": LibraryAnnouncement
        }

        cls = types.get(announcement_type.lower())
        if cls is None:
            raise ValueError(f"Geçersiz duyuru tipi: {announcement_type}")
        return cls(title, content)