---
name: yayin-kurulu
description: Yazıhane okur kurulunu toplar. Bir bölümü ya da dosyayı birbirinden bağımsız okurlara (beta okur, geliştirme editörü, satır editörü, redaktör, olgu denetçisi, yayınevi okuru) aynı anda okutur, sonra baş editör olarak raporlarını tek ve kısa bir karara indirir. İsteğe bağlı olarak bir ya da birkaç ustanın merceğini de kurula katar. Yazar "kurula okut", "bütün okurlar baksın", "yayına hazır mı" dediğinde kullan.
argument-hint: "<dosya(lar)> [hızlı | okur adları] [usta:ad1,ad2]"
disable-model-invocation: true
---

# Yayın Kurulu

Önce `editor` becerisinin ilkelerini uygula (yüklü değilse yükle). Bu komutta sen **baş editörsün**: okurları toplar, raporlarını doğrular ve yazara tek bir karar metni sunarsın. Metni yeniden yazmazsın.

İstek: $ARGUMENTS

## 1. Metni ve kitap dosyasını belirle

- Okunacak metin, isteğin içinde verilen dosya ya da dosyalardır. Dosya verilmemişse ve yazar metni sohbete yapıştırmışsa onu proje kökünde `yazihane-raporlari/metin-<YYYY-AA-GG>.md` dosyasına kaydet; okurlar sohbeti göremez, yalnızca dosya okur. İkisi de yoksa hangi metnin okunacağını tek soruyla sor.
- Metin Word ya da ODT dosyasıysa `editor` becerisindeki "Metin dosyaları" kuralıyla düz metne çevir ve okurlara kopyaların yolunu ver; okurlar Word dosyası okuyamaz.
- Projede kitap dosyasını ara: `KITAP.md`, `kitap.md`, `.claude/KITAP.md`. Bulduğun yolu okurlara ilet.
- Birden fazla sürüm varsa en son sürüm esastır; dosya adına güvenme.

## 2. Kurulu seç

- Varsayılan, **tam kurul**: `beta-okur`, `gelistirme-editoru`, `satir-editoru`, `redaktor`, `olgu-denetcisi`, `yayinevi-okuru`.
- `hızlı`: `beta-okur`, `gelistirme-editoru`, `yayinevi-okuru`.
- Yazar okur adlarını saydıysa yalnızca onlar.
- Yazar `usta:<ad>` eklediyse (ör. `usta:cehov` ya da `usta:cehov,tolstoy`), her usta için bir `usta-okuru` da kurula katılır; en fazla üç usta. Mercek dosyasını önce projedeki `ustalar/` klasöründe, sonra `usta-mercegi` becerisinin `ustalar/` klasöründe ara (bu becerinin klasörünün kardeşi: `../usta-mercegi/ustalar/`; dosya adları `cehov.md`, `sabahattin-ali.md` biçimindedir).
- Kitap dosyasında yapısal olarak kapanmış sayılan bölümler için `gelistirme-editoru` yalnızca karakter doğruluğuna baksın; bunu ona söyle.
- Metinde doğrulanacak alıntı, tarih ya da olgusal ayrıntı yoksa `olgu-denetcisi` kısa bir rapor döner; yine de çağır.

## 3. Okurları aynı anda çalıştır

Seçilen okurların hepsini **tek mesajda, paralel** olarak Agent aracıyla başlat. Alt ajan türleri bu eklentinin ajanlarıdır (`yazihane:beta-okur` gibi; ortam ön eksiz adı kullanıyorsa `beta-okur`).

Her okura aynı kısa görevi ver:
- Okunacak dosyaların **mutlak yolları** ve varsa kitap dosyasının yolu.
- Metnin ne olduğu (ör. "romanın 5. bölümü", "öykünün tamamı") ve yazarın varsa özel sorusu.
- "Raporunu kendi tanımındaki rapor biçimiyle ver."
- `usta-okuru` için ayrıca ustanın mercek dosyasının **mutlak yolu**.

Okurlara birbirlerinin görüşlerini ya da senin ön yargını **verme**; kurulun değeri bağımsız okumalardır.

## 4. Baş editör olarak birleştir

Raporlar gelince:

1. **Doğrula.** Her meselenin alıntısını metinde bul. Metinde olmayan bir şeye dayanan ya da kitap dosyasındaki bir kararla çelişen iddiayı at (atılanı tam raporda "elendi" diye not et).
2. **Birleştir.** Aynı yeri ya da aynı kalıbı gösteren meseleleri tek meseleye indir ve kimlerin gördüğünü yaz. Birden fazla okurun bağımsız olarak gördüğü mesele daha ağırdır.
3. **Ayrışmaları sakla.** Okurlar bir yerde ayrışıyorsa (biri "çalışıyor", öteki "okuru kaybettiriyor" diyorsa) onu çözme; **Tercih meselesi** olarak iki tarafı da göster. Karar yazarındır.
4. **Seç.** En fazla **üç karar**. Öncelik: birden fazla okurun gördüğü Kesin sorunlar → tek okurun gördüğü Kesin sorunlar → önemli Tercih meseleleri. "Ben olsam değiştirirdim" maddeleri yalnızca tam raporda kalır.

## 5. Raporu kaydet ve kısa sun

**Tam raporu** proje kökünde `yazihane-raporlari/<YYYY-AA-GG>-<metnin-kısa-adı>.md` dosyasına yaz:

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
