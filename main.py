from domain.models.users import Student, Teacher
from infrastructure.factories.announcement_factory import AnnouncementFactory
from infrastructure.factories.notification_factory import NotificationFactory
from application.observers.observers import StudentObserver, TeacherObserver
from application.services.announcement_publisher import AnnouncementPublisher
from application.services.logger import Logger

def main():
    print("\n" + "="*50)
    print("   AKILLI KAMPÜS BİLDİRİM SİSTEMİ")
    print("="*50 + "\n")

    # --- 1. Singleton test ---
    print("--- Singleton Pattern Testi ---")
    logger1 = Logger()
    logger2 = Logger()
    print(f"logger1 ve logger2 aynı nesne mi? {logger1 is logger2}\n")

    # --- 2. Kullanıcılar oluşturuluyor ---
    print("--- Kullanıcılar Oluşturuluyor ---")
    ogrenci1 = Student("Ahmet Yılmaz", "ahmet@uni.edu", "5551234567", "2021001")
    ogrenci2 = Student("Ayşe Kara", "ayse@uni.edu", "5557654321", "2021002")
    ogretmen1 = Teacher("Dr. Mehmet Öz", "mehmet@uni.edu", "5559876543", "Bilgisayar Müh.")

    # --- 3. Bildirim tercihleri ---
    print("--- Bildirim Tercihleri Belirleniyor ---")
    ogrenci1.add_notification_preference("email")
    ogrenci1.add_notification_preference("push")
    ogrenci2.add_notification_preference("sms")
    ogretmen1.add_notification_preference("email")
    ogretmen1.add_notification_preference("sms")

    # --- 4. Observer'lar oluşturuluyor ---
    print("\n--- Observer'lar Sisteme Ekleniyor ---")
    publisher = AnnouncementPublisher()
    publisher.subscribe(StudentObserver(ogrenci1))
    publisher.subscribe(StudentObserver(ogrenci2))
    publisher.subscribe(TeacherObserver(ogretmen1))

    # --- 5. Factory ile duyuru oluşturuluyor ---
    print("\n--- Factory ile Duyuru Oluşturuluyor ---")
    sinav_duyurusu = AnnouncementFactory.create(
        "sinav",
        "Vize Sınavı Tarihi Değişti",
        "BİL 3204 vize sınavı 20 Ocak'tan 25 Ocak'a ertelendi."
    )

    etkinlik_duyurusu = AnnouncementFactory.create(
        "etkinlik",
        "Bahar Şenliği",
        "Kampüs bahar şenliği 1 Mayıs'ta başlıyor!"
    )

    # --- 6. Duyurular yayınlanıyor ---
    publisher.publish(sinav_duyurusu)
    publisher.publish(etkinlik_duyurusu)

    # --- 7. Tüm loglar gösteriliyor ---
    print("\n" + "="*50)
    print("   SİSTEM LOGLARI")
    print("="*50)
    logger = Logger()
    for log in logger.get_all_logs():
        print(log)

if __name__ == "__main__":
    main()