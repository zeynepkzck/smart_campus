from domain.interfaces.i_observer import IObserver
from infrastructure.factories.notification_factory import NotificationFactory

class StudentObserver(IObserver):
    def __init__(self, student):
        self.student = student

    def update(self, announcement):
        print(f"\n👤 {self.student} duyurudan haberdar edildi:")
        print(f"   Duyuru Tipi : {announcement.get_type()}")
        print(f"   Başlık      : {announcement.get_title()}")
        print(f"   İçerik      : {announcement.get_content()}")
        print()

        for preference in self.student.notification_preferences:
            notification = NotificationFactory.create(preference)
            notification.send(
                recipient=self.student.email,
                message=f"{announcement.get_type()}: {announcement.get_title()}"
            )

class TeacherObserver(IObserver):
    def __init__(self, teacher):
        self.teacher = teacher

    def update(self, announcement):
        print(f"\n👨‍🏫 {self.teacher} duyurudan haberdar edildi:")
        print(f"   Duyuru Tipi : {announcement.get_type()}")
        print(f"   Başlık      : {announcement.get_title()}")
        print(f"   İçerik      : {announcement.get_content()}")
        print()

        for preference in self.teacher.notification_preferences:
            notification = NotificationFactory.create(preference)
            notification.send(
                recipient=self.teacher.email,
                message=f"{announcement.get_type()}: {announcement.get_title()}"
            )