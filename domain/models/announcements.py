from domain.interfaces.i_announcement import IAnnouncement

class ExamAnnouncement(IAnnouncement):
    def __init__(self, title: str, content: str):
        self._title = title
        self._content = content

    def get_title(self) -> str:
        return self._title

    def get_content(self) -> str:
        return self._content

    def get_type(self) -> str:
        return "SINAV DUYURUSU"


class EventAnnouncement(IAnnouncement):
    def __init__(self, title: str, content: str):
        self._title = title
        self._content = content

    def get_title(self) -> str:
        return self._title

    def get_content(self) -> str:
        return self._content

    def get_type(self) -> str:
        return "ETKİNLİK DUYURUSU"


class FoodMenuAnnouncement(IAnnouncement):
    def __init__(self, title: str, content: str):
        self._title = title
        self._content = content

    def get_title(self) -> str:
        return self._title

    def get_content(self) -> str:
        return self._content

    def get_type(self) -> str:
        return "YEMEKHANE DUYURUSU"


class LibraryAnnouncement(IAnnouncement):
    def __init__(self, title: str, content: str):
        self._title = title
        self._content = content

    def get_title(self) -> str:
        return self._title

    def get_content(self) -> str:
        return self._content

    def get_type(self) -> str:
        return "KÜTÜPHANE DUYURUSU"