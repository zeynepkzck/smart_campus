from domain.interfaces.i_observer import IObserver
from application.services.logger import Logger

class AnnouncementPublisher:
    def __init__(self):
        self._observers = []
        self._logger = Logger()

    def subscribe(self, observer: IObserver):
        self._observers.append(observer)
        self._logger.log(f"Yeni observer eklendi: {observer.__class__.__name__}")

    def unsubscribe(self, observer: IObserver):
        self._observers.remove(observer)
        self._logger.log(f"Observer çıkarıldı: {observer.__class__.__name__}")

    def publish(self, announcement):
        self._logger.log(f"Duyuru yayınlanıyor: {announcement.get_title()}")
        print(f"\n{'='*50}")
        print(f"📢 YENİ DUYURU YAYINLANDI!")
        print(f"   Tip    : {announcement.get_type()}")
        print(f"   Başlık : {announcement.get_title()}")
        print(f"{'='*50}\n")

        for observer in self._observers:
            observer.update(announcement)

        self._logger.log(f"Duyuru tüm kullanıcılara iletildi: {announcement.get_title()}")