from abc import ABC, abstractmethod

class IAnnouncement(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_content(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass