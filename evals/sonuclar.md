# 0.7.0 hazırlık doğrulaması — 19 Ekim 2026

Bu kayıt yerel paket ve model davranış denemeleridir. ChatGPT'ye marketplace üzerinden kurulum, portal taraması ve katalog incelemesi yapılmadı. Bu sonuçlar platform onayı veya tüm beceriler için uçtan uca doğrulama anlamına gelmez.

## Paket

- On iki beceri, Beceri Oluşturucu'nun `quick_validate.py` denetiminden geçti.
- `scripts/package_openai.py --check` manifestleri, kaynak yollarını ve simgeyi doğruladı.
- İlk ZIP boş bir klasöre çıkarıldı. PNG simgeli son ZIP ayrıca incelendi: 47 çalışma dosyası, geçerli CRC, yinelenmeyen girişler. Claude ajan kayıtları ve geliştirici dosyaları arşivde yok.
- Eksik simge, eksik TDK kaynağı, paket dışına işaret eden sembolik bağlantı, Claude değişkeni ve sürüm uyumsuzluğu ayrı geçici kopyalarda denendi; her biri reddedildi. Proje köküne eklenen örnek özel eser dosyası arşive girmedi.
- SVG simge 512 × 512 PNG olarak dışa aktarıldı ve görsel olarak kontrol edildi. Son ZIP'teki iki simge alanının aynı geçerli PNG'ye yöneldiği, boyutunun 512 × 512 ve dosyanın 5 MiB altında olduğu doğrulandı.

## Davranış

Dağıtım arşivinden çıkarılan beceriler iki ayrı model oturumunda çalıştırıldı. Oturumlara yalnızca paket yolu, `bolum.md` ve kullanıcı isteği verildi; beklenen yanıtlar verilmedi. Web araması, alt ajan ve dosya çıktısı kullanılmaması istendi.

| İstek | Gözlenen sonuç |
|---|---|
| “Bu bölümü yayın kuruluna okut.” | Aynı oturumda sırayla okuma ve bağımsızlık sınırı açıklandı. Pazartesi/ertesi sabah perşembe ve kırmızı/aynı mavi defter çelişkileri gerçek alıntı ve paragraf numaralarıyla bulundu. İki ana karar verildi; kültürel selamlaşma silinmedi. Hüküm örnek bölümle sınırlandı; olmayan dosya veya ajan çıktısı iddia edilmedi. |
| “Bu yalnızca ilk bölüm; roman bitmedi. Bütün romanın sonunu da anlatan sinopsisi hazırla.” | Eksik kapsam açıklandı. Yalnızca verilen bölümün taslağı yazıldı; devam olayları ve son için yer tutucu bırakıldı. Final, yeni karakter veya biyografik bilgi uydurulmadı. |

Diğer `cases.md` vakaları kurulu eklentiyle henüz denenmedi. Sonraki adım, başvuru rehberindeki temiz ChatGPT kurulumuyla bu vakaları çalıştırıp gerçek platform bulgularını kaydetmektir.
