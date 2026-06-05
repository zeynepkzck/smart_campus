from domain.interfaces.i_notification import INotification

class EmailNotification(INotification):
    def send(self, recipient: str, message: str):
        print(f"📧 E-POSTA GÖNDERİLDİ")
        print(f"   Alıcı  : {recipient}")
        print(f"   Mesaj  : {message}")
        print()

class SMSNotification(INotification):
    def send(self, recipient: str, message: str):
        print(f"📱 SMS GÖNDERİLDİ")
        print(f"   Alıcı  : {recipient}")
        print(f"   Mesaj  : {message}")
        print()

class PushNotification(INotification):
    def send(self, recipient: str, message: str):
        print(f"🔔 MOBİL BİLDİRİM GÖNDERİLDİ")
        print(f"   Alıcı  : {recipient}")
        print(f"   Mesaj  : {message}")
        print()