---
name: yayin-kurulu
description: Bir bölümü ya da dosyayı beta okur, geliştirme editörü, satır editörü, redaktör, olgu denetçisi ve yayınevi okuru açısından değerlendirir; baş editör olarak en fazla üç karara indirir. Ortam destekliyorsa okumaları bağımsız görevlerle, desteklemiyorsa aynı oturumda sırayla yapar. Yazar "kurula okut", "bütün okurlar baksın", "yayına hazır mı" dediğinde kullan.
---

**Toplu çağrı:** “Yayın kurulu olarak değerlendir” isteği, [dashboard](../dashboard/SKILL.md) akışıyla bu rollerin yanında iki yapı haritasını, yalnız Tolstoy/Ahmet Haşim/Sabahattin Ali merceklerini, etiketli kısa iskeleyi ve HTML/PDF raporunu birleştirir. Dashboard zaten yürütülüyorsa tekrar başlatma; burada yalnız istenen rol okumalarını tamamla. `hızlı` veya tek mod isteğinde açık kapsam önceliklidir.

# Yayın Kurulu

Önce [editor](../editor/SKILL.md) becerisinin ilkelerini oku ve uygula. Bu komutta sen **baş editörsün**: okurları toplar, raporlarını doğrular ve yazara tek bir karar metni sunarsın. Metni yeniden yazmazsın.

İstek: yazarın bu görevde belirttiği metin ve istek

## 1. Metni ve kitap dosyasını belirle

- Okunacak metin, isteğin içinde verilen dosyalar, ekler veya yapıştırılmış metindir. Bağımsız okurlara görev vereceksen ve metin sohbetteyse erişebilecekleri ayrı bir okuma kopyası oluştur veya göreve metnin tamamını aktar. Böyle bir araç yoksa aynı oturumda sırayla oku. Hiç metin yoksa hangi metnin okunacağını tek soruyla sor.
- Word ya da ODT doğrudan okunamıyorsa `editor` becerisindeki "Metin dosyaları" kuralını uygula; okurlara gerçekten erişebilecekleri metni ver.
- Projede kitap dosyasını ara: `KITAP.md`, `kitap.md`, `.claude/KITAP.md`. Bulduğun yolu okurlara ilet.
- Birden fazla sürüm varsa en son sürüm esastır; dosya adına güvenme.

## 2. Kurulu seç

- Varsayılan, **tam kurul**: `beta-okur`, `gelistirme-editoru`, `satir-editoru`, `redaktor`, `olgu-denetcisi`, `yayinevi-okuru`.
- `hızlı`: `beta-okur`, `gelistirme-editoru`, `yayinevi-okuru`.
- Yazar okur adlarını saydıysa yalnızca onlar.
- Yazar `usta:<ad>` eklediyse (ör. `usta:cehov` ya da `usta:cehov,tolstoy`), her usta için bir `usta-okuru` da kurula katılır; en fazla üç usta. Mercek dosyasını önce projedeki `ustalar/` klasöründe, sonra `usta-mercegi` becerisinin `ustalar/` klasöründe ara (bu becerinin klasörünün kardeşi: `../usta-mercegi/ustalar/`; dosya adları `cehov.md`, `sabahattin-ali.md` biçimindedir).
- Kitap dosyasında yapısal olarak kapanmış sayılan bölümler için `gelistirme-editoru` yalnızca karakter doğruluğuna baksın; bunu ona söyle.
- Metinde doğrulanacak alıntı, tarih ya da olgusal ayrıntı yoksa `olgu-denetcisi` kısa bir rapor döner; yine de çağır.

## 3. Okurları çalıştır

Her seçilen okurun tam rolünü `../editor/references/okurlar/<okur-adı>.md` dosyasından oku. Bu dosyalar paket içi kaynaklardır; ChatGPT'ye özel ajan türleri kaydetmez. Alt ajan desteği ve oturum kuralları izin veriyorsa her rolü ayrı ve mümkünse paralel bir görev olarak başlat; göreve rol dosyasını da ver. Ajan desteği yoksa aynı kaynaklarla okumaları sırayla kendin yap ve bu okumaların tam bağımsız olmadığını rapor başında belirt. Claude Code'daki kayıtlı okur ajanları da aynı rol dosyalarını kullanır.

Her okura aynı kısa görevi ver:
- Okunacak dosyaların erişilebilir yolları veya metnin tamamı; varsa kitap dosyası ve okurun rol dosyası.
- Metnin ne olduğu (ör. "romanın 5. bölümü", "öykünün tamamı") ve yazarın varsa özel sorusu.
- "Raporunu kendi tanımındaki rapor biçimiyle ver."
- `usta-okuru` için ayrıca ustanın mercek dosyasının **mutlak yolu**.

Okurlara birbirlerinin görüşlerini ya da senin ön yargını **verme**; kurulun değeri bağımsız okumalardır.

**Alt ajan desteği yoksa** `editor` becerisindeki "Çalışma ortamı" kuralına göre, her rolün kaynak dosyasını kullanarak sırayla oku; kapsamları şöyledir:
- **Beta okur:** yalnızca hissedilen okur tepkisi; düzeltme yok.
- **Geliştirme editörü:** hikâye, yapı, sahne işlevi, karakter doğruluğu; en fazla üç mesele.
- **Satır editörü:** ritim, tekrar, klişe, belirsiz özne; bütün itirazlar tek seferde.
- **Redaktör:** TDK'ya göre imla ve süreklilik; düzeltme tablosu.
- **Olgu denetçisi:** alıntı, atıf ve olguların doğrulanması; web araması yoksa "doğrulanamadı" de, uydurma.
- **Yayınevi okuru:** okur raporu; kabul, revizyonla kabul ya da ret.
- **Usta okuru** (istendiyse): ustanın merceğiyle okuma; taklit yok.

## 4. Baş editör olarak birleştir

Raporlar gelince:

1. **Doğrula.** Her meselenin alıntısını metinde bul. Metinde olmayan bir şeye dayanan ya da kitap dosyasındaki bir kararla çelişen iddiayı at (atılanı tam raporda "elendi" diye not et).
2. **Birleştir.** Aynı yeri ya da aynı kalıbı gösteren meseleleri tek meseleye indir ve kimlerin gördüğünü yaz. Birden fazla okurun bağımsız olarak gördüğü mesele daha ağırdır.
3. **Ayrışmaları sakla.** Okurlar bir yerde ayrışıyorsa (biri "çalışıyor", öteki "okuru kaybettiriyor" diyorsa) onu çözme; **Tercih meselesi** olarak iki tarafı da göster. Karar yazarındır.
4. **Seç.** En fazla **üç karar**. Öncelik: birden fazla okurun gördüğü Kesin sorunlar → tek okurun gördüğü Kesin sorunlar → önemli Tercih meseleleri. "Ben olsam değiştirirdim" maddeleri yalnızca tam raporda kalır.

## 5. Raporu kaydet ve kısa sun

**Tam raporu** dosya çıktısı destekleniyorsa ayrı bir çıktı olarak kaydet; yerel projede `yazihane-raporlari/<YYYY-AA-GG>-<metnin-kısa-adı>.md` kullan. Yazma aracı yoksa raporu sohbette sun. Biçim:

```
# Yayın Kurulu — <metin> · <tarih>
## Kurulun hükmü
## Çalışanlar
## Üç karar
## Ayrışmalar
## Redaksiyon ve doğrulama özeti
## Okur raporları
<her okurun raporu, değiştirmeden>
## Elenen iddialar
```

**Sohbette** yalnızca telefonda okunacak ölçüde bir özet ver:

- **Kurulun hükmü:** bir iki cümle (yayınevi okurunun önerisi dahil).
- **Çalışanlar:** bir iki madde, "Bu çalışıyor, çünkü…".
- **Üç karar:** her biri etiketiyle, bir iki cümle, kimlerin gördüğü.
- **Ayrışma:** varsa en önemlisi, tek madde.
- **Redaksiyon:** "<n> imla düzeltmesi, <n> süreklilik notu, <n> doğrulama" ve tam raporun yolu.

Ödev, çalışma planı ya da verimlilik tavsiyesi verme. Metni yeniden yazma. Yazar bir kararı açmak isterse o meseleye ilgili okurun raporundan derinleş.
