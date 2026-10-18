---
name: yayinevi-dosyasi
description: Bir eseri yayınevine göndermek için dosya hazırlar — kitap kimliği (tür, kelime sayısı, tek cümlelik ve tek paragraflık öz), sinopsis, tanıtım mektubu, yazar biyografisi, örnek bölüm seçimi, arka kapak yazısı ve gönderim kontrol listesi; sonunda dosyayı bir yayınevi okurunun gözüyle sınar. İstenirse kapak brief'i ve tanıtım bülteni de hazırlar. Yazar "yayınevine göndereceğim", "sinopsis yaz", "tanıtım mektubu", "arka kapak yazısı" dediğinde kullan.
argument-hint: "[tam | sinopsis | mektup | biyografi | arka-kapak | kapak-brief | bulten | sina] [yayınevi adı]"
allowed-tools: Skill, Read, Glob, Grep, Write, Edit, Agent, WebSearch, WebFetch, Bash(wc:*), Bash(mkdir:*), Bash(textutil:*), Bash(pandoc:*)
---

# Yayınevi Dosyası

Önce `editor` becerisinin ilkelerini uygula (yüklü değilse yükle) ve projede kitap dosyası (`KITAP.md`) varsa oku.

İstek: $ARGUMENTS

Bu komut romanın metnini değil, **eseri yayınevine taşıyan metinleri** hazırlar. Bunlar yazarın adına gidecek belgelerdir; bu yüzden:

- Her belge **taslaktır.** Başına `> TASLAK — göndermeden önce okuyun, kendi sesinize göre düzeltin ve onaylayın.` satırını koy.
- **Hiçbir şey uydurma.** Yazar hakkında bilgi, ödül, yayın geçmişi, okur yorumu, övgü cümlesi, satış ya da yayınevi bilgisi uydurulmaz. Bilmediğin her şey için yer tutucu bırak: `[ad soyad]`, `[önceki yayınlar]`, `[bu yayınevini seçme nedeniniz]`.
- **Kişisel iletişim bilgisi isteme.** Telefon, adres ve e-posta için yalnızca yer tutucu bırak; yazar kendisi doldurur.
- Belgeler eserin tonunu yansıtmalı, ama yazarın sesini **taklit etmemeli**. Eserden alıntı gerekiyorsa yazarın kendi cümlesini olduğu gibi kullan.
- Yazara gereksiz izin soruları çıkmasın: dosya bulmak için Glob, okumak için Read, düzeltmek için Edit kullan. Kabuk komutlarını yalnızca dönüştürme, kelime sayımı ve klasör oluşturma için kullan.

## 1. Neyi hazırlayacağını belirle

- `tam` ya da boş: kitap kimliği, sinopsis, tanıtım mektubu, yazar biyografisi, örnek bölüm seçimi, arka kapak, kontrol listesi ve sınama.
- Tek parça istendiyse (`sinopsis`, `mektup`, `biyografi`, `arka-kapak`, `kapak-brief`, `bulten`, `sina`) yalnızca onu hazırla; gerekiyorsa önceki belgeleri `yayinevi-dosyasi/` klasöründen oku.
- Kapak brief'i ve tanıtım bülteni yalnızca istenirse hazırlanır; ikisini de çoğu zaman yayınevi üstlenir.
- Kitap dosyasında başlık ya da kapak "kapanmış karar" olarak geçiyorsa bunları yeniden açma.

## 2. Metni hazırla ve ölç

- Eserin bölüm dosyalarını bul ve sıraya koy (dosya adlarındaki numaraya ya da yazarın verdiği sıraya göre; emin değilsen tek soruyla sor). En son sürüm esastır; dosya adına güvenme. `yazihane-raporlari/` ve `yayinevi-dosyasi/` klasörlerindeki dosyalar eserin metni değildir.
- Word ya da ODT dosyalarını `editor` becerisindeki "Metin dosyaları" kuralıyla düz metne çevir.
- Kelime sayısını ölç (`wc -w`); kitap kimliğinde yuvarlayarak ver (ör. "yaklaşık 72.000 kelime"). Eser bitmemişse bunu söyle: yayınevleri edebî eserlerde çoğunlukla tamamlanmış dosya ister.

## 3. Bölüm haritası çıkar

Sinopsis ve arka kapak eserin **tamamına** dayanmalıdır.

- Toplam metin yaklaşık 20.000 kelimenin altındaysa bölümleri kendin, sırasıyla ve baştan sona oku.
- Daha uzunsa bölümleri sırayı bozmadan yaklaşık 20.000 kelimelik gruplara ayır ve her grup için `bolum-ozetcisi` ajanını **tek mesajda, paralel** olarak başlat (alt ajan türü `yazihane:bolum-ozetcisi`; ortam ön eksiz adı kullanıyorsa `bolum-ozetcisi`). Her ajana dosyaların mutlak yollarını ve varsa kitap dosyasının yolunu ver.
- **Agent aracı yoksa** (ör. claude.ai sohbeti) haritayı bölüm bölüm kendin çıkar; eser sohbete sığmıyorsa bunu söyle ve Cowork ya da Claude Code'u öner.
- Haritayı `yazihane-raporlari/bolum-haritasi-<YYYY-AA-GG>.md` dosyasına kaydet ve başına şunu yaz: `Çalışma notu — kanon değildir; metin değişince yeniden çıkarılır.`

## 4. Belgeleri yaz

Her belgeden önce bu becerinin `rehber/` klasöründeki ilgili rehberi oku. Belgeleri proje kökünde `yayinevi-dosyasi/` klasörüne yaz:

| Dosya | İçerik | Rehber |
|---|---|---|
| `00-kontrol-listesi.md` | Göndermeden önce bakılacaklar ve "Sizden gerekenler" | `rehber/kontrol-listesi.md` |
| `01-kitap-kimligi.md` | Tür, uzunluk, tek cümlelik öz, tek paragraflık öz, okur kitlesi, benzer eserler | `rehber/sinopsis.md` |
| `02-tanitim-mektubu.md` | Yayınevine sunuş mektubu | `rehber/tanitim-mektubu.md` |
| `03-sinopsis.md` | Sonu da anlatan bir iki sayfalık özet | `rehber/sinopsis.md` |
| `04-yazar-biyografisi.md` | 50–100 kelimelik, üçüncü tekil kısa biyografi | `rehber/tanitim-mektubu.md` |
| `05-ornek-bolumler.md` | Gönderilecek bölümler ve gerekçesi | `rehber/kontrol-listesi.md` |
| `06-arka-kapak.md` | En fazla iki seçenek | `rehber/arka-kapak.md` |
| `kapak-brief.md`, `tanitim-bulteni.md` | Yalnızca istenirse | `rehber/kapak-ve-bulten.md` |

Yazar bir yayınevi adı verdiyse ve web araması mümkünse, o yayınevinin kendi sitesindeki dosya gönderim koşullarını ara; bulduğunu kaynağıyla kontrol listesine yaz. Bulamazsan uydurma; yazara yayınevinin sitesine bakmasını söyle.

## 5. Dosyayı sına

Tanıtım mektubu, sinopsis ve örnek bölümler hazır olunca `yayinevi-okuru` ajanını çalıştır (alt ajan türü `yazihane:yayinevi-okuru`). Ona bu belgelerin ve örnek bölümlerin mutlak yollarını ver ve şunu sor: "Bu, yayınevine gelmiş bir dosya. Mektup ve sinopsis seni örnek bölümlere taşıyor mu? Örnek bölümler sinopsisin vaadini karşılıyor mu? Dosyanın tamamını ister miydin? Okur raporunu kendi biçiminle ver." Raporu `yayinevi-dosyasi/07-yayinevi-okuru-raporu.md` dosyasına kaydet. Agent aracı yoksa sınamayı yayınevi okurunun gözüyle kendin yap ve raporda bunu belirt.

Okurun raporunda belgelerle (mektup, sinopsis, arka kapak) ilgili Kesin sorun varsa belgeyi düzelt ve neyi düzelttiğini söyle. Sorun romanın metnindeyse metne dokunma; yazara bildir.

## 6. Kısa sun

Sohbette telefonda okunacak ölçüde bir özet ver:

- Hazırlanan belgeler ve klasörün yolu.
- Tek cümlelik öz: yazarın ilk göreceği şey bu olsun.
- Yayınevi okurunun hükmü, bir iki cümle.
- **Sizden gerekenler:** yer tutucuların listesi (biyografi bilgileri, yayınevini seçme nedeni, iletişim bilgileri, benzer eserlerin onayı).

Belgeleri Word olarak isteyen yazar için: `pandoc` varsa `.docx`'e çevir; yoksa macOS'ta `textutil -format txt -convert docx` ile çevrilebileceğini, ama biçimin sade kalacağını söyle.
