# smart_campus
# 🏫 Akıllı Kampüs Duyuru ve Bildirim Yönetim Sistemi

BİL 3204 - Yazılım Mimari ve Tasarımı dersi final projesi.

## 📌 Proje Hakkında

Bu proje, bir üniversite kampüsünde farklı türde duyuruların yönetilmesini ve
ilgili kullanıcılara otomatik bildirim gönderilmesini sağlayan bir sistemdir.
Observer, Factory ve Singleton tasarım desenleri kullanılarak katmanlı mimari
anlayışıyla geliştirilmiştir.

## 🏗️ Kullanılan Tasarım Desenleri

### 🔔 Observer Pattern
Yeni bir duyuru yayınlandığında ilgili kullanıcıların otomatik olarak
bilgilendirilmesi için kullanılmıştır. `AnnouncementPublisher` duyuruyu
yayınlar, `StudentObserver` ve `TeacherObserver` bu duyurudan haberdar olur.

### 🏭 Factory Pattern
Farklı duyuru ve bildirim nesnelerinin oluşturulmasında kullanılmıştır.
- `AnnouncementFactory` → Sınav, Etkinlik, Yemekhane, Kütüphane duyuruları üretir.
- `NotificationFactory` → E-posta, SMS, Mobil bildirim nesneleri üretir.

### 🔒 Singleton Pattern
Sistem genelinde tek bir örneği olması gereken `Logger` sınıfında kullanılmıştır.
Tüm sistem logları tek bir merkezi Logger üzerinden yönetilir.

## 📁 Proje Yapısı
