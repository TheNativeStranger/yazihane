---
name: yayinevi-dosyasi
description: Bir eseri yayınevine göndermek için dosya hazırlar — kitap kimliği (tür, kelime sayısı, tek cümlelik ve tek paragraflık öz), sinopsis, tanıtım mektubu, yazar biyografisi, örnek bölüm seçimi, arka kapak yazısı ve gönderim kontrol listesi; sonunda dosyayı bir yayınevi okurunun gözüyle sınar. İstenirse kapak brief'i ve tanıtım bülteni de hazırlar. Yazar "yayınevine göndereceğim", "sinopsis yaz", "tanıtım mektubu", "arka kapak yazısı" dediğinde kullan.
---

# Yayınevi Dosyası

Önce [editor](../editor/SKILL.md) becerisinin ilkelerini oku ve uygula; projede kitap dosyası (`KITAP.md`) varsa oku.

İstek: yazarın bu görevde belirttiği metin ve istek

Bu komut romanın metnini değil, **eseri yayınevine taşıyan metinleri** hazırlar. Bunlar yazarın adına gidecek belgelerdir; bu yüzden:

- Her belge **taslaktır.** Başına `> TASLAK — göndermeden önce okuyun, kendi sesinize göre düzeltin ve onaylayın.` satırını koy.
- **Hiçbir şey uydurma.** Yazar hakkında bilgi, ödül, yayın geçmişi, okur yorumu, övgü cümlesi, satış ya da yayınevi bilgisi uydurulmaz. Bilmediğin her şey için yer tutucu bırak: `[ad soyad]`, `[önceki yayınlar]`, `[bu yayınevini seçme nedeniniz]`.
- **Kişisel iletişim bilgisi isteme.** Telefon, adres ve e-posta için yalnızca yer tutucu bırak; yazar kendisi doldurur.
- Belgeler eserin tonunu yansıtmalı, ama yazarın sesini **taklit etmemeli**. Eserden alıntı gerekiyorsa yazarın kendi cümlesini olduğu gibi kullan.
- Ortamın mevcut dosya okuma, ölçme ve çıktı araçlarını kullan; belirli araç adları veya kurulu programlar varsayma. Dosya yazılamıyorsa belgeleri sohbette ayrı başlıklarla ver. Bir yayınevine gönderme işlemi bu becerinin kapsamında değildir.

## 1. Neyi hazırlayacağını belirle

- `tam` ya da boş: kitap kimliği, sinopsis, tanıtım mektubu, yazar biyografisi, örnek bölüm seçimi, arka kapak, kontrol listesi ve sınama.
- Tek parça istendiyse (`sinopsis`, `mektup`, `biyografi`, `arka-kapak`, `kapak-brief`, `bulten`, `sina`) yalnızca onu hazırla; gerekiyorsa önceki belgeleri `yayinevi-dosyasi/` klasöründen oku.
- Kapak brief'i ve tanıtım bülteni yalnızca istenirse hazırlanır; ikisini de çoğu zaman yayınevi üstlenir.
- Kitap dosyasında başlık ya da kapak "kapanmış karar" olarak geçiyorsa bunları yeniden açma.

## 2. Metni hazırla ve ölç

- Eserin bölüm dosyalarını bul ve sıraya koy (dosya adlarındaki numaraya ya da yazarın verdiği sıraya göre; emin değilsen tek soruyla sor). En son sürüm esastır; dosya adına güvenme. `yazihane-raporlari/` ve `yayinevi-dosyasi/` klasörlerindeki dosyalar eserin metni değildir.
- Word ya da ODT dosyalarını `editor` becerisindeki "Metin dosyaları" kuralıyla düz metne çevir.
- Araç varsa kelime sayısını ölç; kitap kimliğinde yuvarlayarak ver (ör. "yaklaşık 72.000 kelime"). Araç yoksa sayı tahmin olduğunu belirt veya güvenilir değilse boş bırak. Eser bitmemişse bunu belirt; gönderim koşullarını ilgili yayınevinin kaynağından kontrol et.

## 3. Bölüm haritası çıkar

Sinopsis ve arka kapak eserin **tamamına** dayanmalıdır.

- Toplam metin yaklaşık 20.000 kelimenin altındaysa bölümleri kendin, sırasıyla ve baştan sona oku.
- Daha uzunsa önce `../editor/references/okurlar/bolum-ozetcisi.md` rolünü oku. Bölümleri bağlama sığacak, sırası korunan gruplar halinde işle. Alt ajan desteği ve oturum kuralları izin veriyorsa her gruba ayrı görev ver; rolü, metni ve varsa kitap dosyasını erişilebilir biçimde ilet.
- **Alt ajan desteği yoksa** haritayı bölüm bölüm kendin çıkar. Okunamayan ya da eksik bölüm varsa belirt ve tam eser sinopsisi yerine kapsamı sınırlı taslak ver; eksik olayları ve sonu uydurma. 20.000 kelime teknik bir bağlam garantisi değildir.
- Haritayı ayrı çıktı olarak kaydet; yerel projede `yazihane-raporlari/bolum-haritasi-<YYYY-AA-GG>.md` kullan. Çıktı aracı yoksa sohbette ver. Başına şunu yaz: `Çalışma notu — kanon değildir; metin değişince yeniden çıkarılır.`

## 4. Belgeleri yaz

Her belgeden önce bu becerinin `rehber/` klasöründeki ilgili rehberi oku. Dosya çıktısı destekleniyorsa belgeleri ayrı çıktı olarak kaydet; yerel projede `yayinevi-dosyasi/` klasörünü kullan. Çıktı aracı yoksa aynı sırayla sohbette sun:

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

Tanıtım mektubu, sinopsis ve örnek bölümler hazır olunca `../editor/references/okurlar/yayinevi-okuru.md` rolünü oku. Gerçek alt ajan desteği ve oturum kuralları izin veriyorsa rolü ve belgeleri erişilebilir biçimde ayrı göreve ver; yoksa sınamayı aynı oturumda kendin yap ve bunu belirt. Soru: "Bu, yayınevine gelmiş bir dosya. Mektup ve sinopsis seni örnek bölümlere taşıyor mu? Örnek bölümler sinopsisin vaadini karşılıyor mu? Dosyanın tamamını ister miydin? Okur raporunu kendi biçiminle ver." Raporu ayrı çıktı olarak kaydet; yerel projede `yayinevi-dosyasi/07-yayinevi-okuru-raporu.md` kullan. Çıktı aracı yoksa sohbette sun.

Okurun raporunda belgelerle (mektup, sinopsis, arka kapak) ilgili Kesin sorun varsa belgeyi düzelt ve neyi düzelttiğini söyle. Sorun romanın metnindeyse metne dokunma; yazara bildir.

## 6. Kısa sun

Sohbette telefonda okunacak ölçüde bir özet ver:

- Hazırlanan belgeler ve klasörün yolu.
- Tek cümlelik öz: yazarın ilk göreceği şey bu olsun.
- Yayınevi okurunun hükmü, bir iki cümle.
- **Sizden gerekenler:** yer tutucuların listesi (biyografi bilgileri, yayınevini seçme nedeni, iletişim bilgileri, benzer eserlerin onayı).

Belgeleri Word olarak isteyen yazar için ortamın mevcut belge oluşturma aracını kullan. Araç yoksa `pandoc` ya da macOS'ta `textutil` yalnızca kuruluysa kullanılabilir. Hiçbiri yoksa Word dosyası oluşturduğunu söyleme; kopyalanabilir metin sun.
