# Simple Port Scanner (TCP) 

Bu proje, ağ güvenliği temellerini anlamak ve Python ile soket programlama (socket programming) pratiği yapmak amacıyla geliştirilmiş temel seviye bir port tarama aracıdır.

## Özellikler
- **TCP Bağlantı Analizi:** Hedef IP veya alan adı üzerindeki portların durumunu kontrol eder.
- **Hata Yönetimi:** Geçersiz hostname veya ağ bağlantı kopuklukları gibi durumları yakalar.
- **Kullanıcı Dostu Arayüz:** Terminal üzerinden temiz ve okunabilir çıktı verir.
- **Hız Optimizasyonu:** `timeout` parametresi ile gereksiz beklemelerin önüne geçer.

## Teknik Detaylar
Bu araç Python'un yerleşik `socket` kütüphanesini kullanır. Herhangi bir ek kütüphane kurulumu gerektirmez, bu da onu taşınabilir ve hafif (lightweight) kılar.

- **Dil:** Python 
- **Kütüphane:** `socket`, `datetime`, `sys`

## Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/arsoybilal/simple-port-scanner.git