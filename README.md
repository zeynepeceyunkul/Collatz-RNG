# Collatz Tabanlı Rastgele Sayı Üreteci (0–29)

Bu proje, kriptoloji dersi kapsamında geliştirilen **eğitim amaçlı bir rastgele sayı üretecidir (RNG)**.  
Üreteç, **Collatz dinamiğini (3x+1 problemi)** temel alır ve **0–29 aralığında** sayı üretir.

> ⚠️ Not: Bu RNG **kriptografik olarak güvenli değildir**.  
> Bilerek kırılabilir şekilde tasarlanmıştır ve dersin “rastgele sayı üreteci kırma” bölümünde kullanılmak üzere hazırlanmıştır.

---

## 🎯 Projenin Amacı

- Rastgele sayı üretme mantığını anlamak  
- Kaotik matematiksel süreçlerin RNG’de nasıl kullanılabileceğini göstermek  
- Üretilen sayıların **öngörülebilirliğini (zayıflığını)** analiz edebilmek  
- RNG kırma (break) kavramını uygulamalı olarak göstermek  

---

## 🧠 Kullanılan Yaklaşım

- Başlangıç değeri (**seed**) alınır  
- Seed, belirli sayıda **Collatz adımı** ile dönüştürülür  
- Ortaya çıkan değer basit bir 32-bit karıştırma (mixing) fonksiyonundan geçirilir  
- Çıktı, **rejection sampling** yöntemiyle 0–29 aralığına indirgenir  

Bu yapı, düzensiz (chaotic) davranış üretse de **kriptografik olarak güvenli değildir**.

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.10+**
- Collatz matematiksel dönüşümü
- Basit 32-bit non-cryptographic mixing
- Standart Python kütüphaneleri

Ek bir harici kütüphane kullanılmamıştır.

---

## 📂 Proje Yapısı

