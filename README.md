# Collatz Tabanlı Rastgele Sayı Üreteci (0–29)

Bu proje, kriptoloji dersi kapsamında geliştirilen **eğitim amaçlı bir rastgele sayı üretecidir (RNG)**.  
Algoritma, **Collatz (3x+1) problemi** temel alınarak tasarlanmıştır ve **0–29 aralığında** sayı üretir.

> ⚠️ Bu algoritma **kriptografik olarak güvenli değildir**.  
> Bilerek kırılabilir şekilde tasarlanmış olup, dersin “rastgele sayı üreteci kırma” kısmı için uygundur.

---

## 🎯 Projenin Amacı

- Rastgele sayı üretiminin temel mantığını kavramak  
- Kaotik matematiksel süreçlerin RNG tasarımında nasıl kullanılabileceğini göstermek  
- Deterministik algoritmaların neden kriptografik olarak zayıf olduğunu göstermek  
- RNG kırma (break) mantığını uygulamalı olarak açıklamak  

---

## 🔁 Algoritmanın Akış Şeması (Flowchart)

Aşağıda algoritmanın akış şeması yer almaktadır:

```text
flowchart TD
    A([Start]) --> B[/Input Seed/]
    B --> C[Initialize state = seed]

    C --> D[Set x = state]
    D --> E{Repeat 12 times}

    E --> F{Is x even?}
    F -- Yes --> G[x = x / 2]
    F -- No --> H[x = 3x + 1]

    G --> I[x = x + constant]
    H --> I

    I --> E

    E --> J[Apply mixing: mix(x XOR state)]
    J --> K[Update state = mix(output + constant)]
    K --> L[Generate 32-bit number]

    L --> M{Rejection sampling valid?}
    M -- No --> D
    M -- Yes --> N[Reduce to range 0–29 (modulo)]

    N --> O[/Output random number/]
    O --> P([End])
```

---

## 🧠 Algoritmanın Sözde Kodu (Pseudocode)
```text
INPUT seed
state ← seed

FUNCTION next_random():
    x ← state

    REPEAT 12 TIMES:
        IF x is even THEN
            x ← x / 2
        ELSE
            x ← 3x + 1
        END IF
        x ← x + constant
    END REPEAT

    output ← mix(x XOR state)
    state ← mix(output + constant)

    RETURN output
END FUNCTION

FUNCTION next_random_mod_30():
    LOOP:
        r ← next_random()
        IF r < largest_multiple_of_30_within_2^32 THEN
            RETURN r MOD 30
        END IF
    END LOOP
END FUNCTION
```

---

## 🛠 Kullanılan Teknolojiler
- Python 3.10+

- Collatz matematiksel dönüşümü

- 32-bit non-cryptographic mixing

- Rejection sampling (mod bias azaltma)

- Harici kütüphane kullanılmamıştır.

---

## 📂 Proje Yapısı
```
collatz-rng/
├── rng.py          # Rastgele sayı üreteci algoritması
├── demo.py         # RNG çıktısını gösteren demo
├── break_demo.py   # RNG kırma (seed tahmini) demosu
├── README.md
```

---

## ▶️ Çalıştırma
### RNG çıktısını görmek için:
```text
python demo.py
```
### RNG’nin kırılabildiğini göstermek için:
```text
python break_demo.py
```
### 📊 Örnek Çıktı
demo.py çalıştırıldığında elde edilen örnek çıktı:

```text
Seed: 1715938421
Çıktılar (0–29):
[12, 4, 19, 7, 25, 3, 18, 0, 22, 9, 14, 6, 28, 11, 1, 20, 8, 24, 16, 5]
```
Bu çıktı:

- 0–29 aralığında sayı üretildiğini

- Algoritmanın deterministik olduğunu

- Aynı seed ile aynı dizinin üretilebildiğini göstermektedir

## 🔓 Algoritmanın Kırılabilirliği (Break Analysis)
Bu algoritma kriptografik değildir çünkü:

- Deterministiktir

* Seed uzayı küçültülebilir

- İlk birkaç çıktı gözlemlendiğinde brute-force yöntemiyle seed tahmini yapılabilir

- Bu durum break_demo.py dosyasında uygulamalı olarak gösterilmiştir.

