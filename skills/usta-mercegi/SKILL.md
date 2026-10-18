---
name: usta-mercegi
description: Bir metni bir ya da birkaç ustanın merceğiyle okur — Çehov, Dostoyevski, Kafka, Gogol, Tolstoy, Sabahattin Ali, Ahmet Haşim, Necip Fazıl, Tanpınar, Sait Faik, Yusuf Atılgan, Oğuz Atay ya da yazarın eklediği başka bir usta. Ustayı taklit edilecek bir model olarak değil, yazarın elindekini görünür kılan bir mercek olarak kullanır; pastiş yapmaz, metni ustanın üslubuyla yeniden yazmaz. Yazar "X olsa nasıl yazardı?", "bunu Çehov'un gözüyle oku", "bu sahneye hangi usta ne derdi" dediğinde kullan.
argument-hint: "<usta | usta1,usta2 | kurul> [dosya]"
---

# Ustaların Merceği

Önce `editor` becerisinin ilkelerini uygula (yüklü değilse yükle) ve projede kitap dosyası (`KITAP.md`) varsa oku.

İstek: $ARGUMENTS

Ustalar taklit edilecek model değil, **yazarın elindekini görünür kılan mercektir.** Merceğin işi, yazarın metninde zaten olanı ve olabilecek olanı göstermektir; yazarı bir ustanın üslubuna çekmek değil.

## 1. Merceği bul

Her mercek dosyasında ustanın ne öğrettiği, metne sorulacak sorular, ustadan yanlış öğrenmenin tuzakları ve çalışılacak eserler vardır.

1. Önce projede yazarın kendi eklediği mercekleri ara: proje kökündeki `ustalar/` klasörü.
2. Sonra bu becerinin klasöründeki `ustalar/` klasörüne bak:

| Usta | Dosya |
|---|---|
| Anton Çehov | `ustalar/cehov.md` |
| Fyodor Dostoyevski | `ustalar/dostoyevski.md` |
| Franz Kafka | `ustalar/kafka.md` |
| Nikolay Gogol | `ustalar/gogol.md` |
| Lev Tolstoy | `ustalar/tolstoy.md` |
| Sabahattin Ali | `ustalar/sabahattin-ali.md` |
| Ahmet Haşim | `ustalar/ahmet-hasim.md` |
| Necip Fazıl Kısakürek | `ustalar/necip-fazil.md` |
| Ahmet Hamdi Tanpınar | `ustalar/tanpinar.md` |
| Sait Faik Abasıyanık | `ustalar/sait-faik.md` |
| Yusuf Atılgan | `ustalar/yusuf-atilgan.md` |
| Oğuz Atay | `ustalar/oguz-atay.md` |

Yazar ustanın adını farklı yazabilir (Çehof, Dostayevski, Haşim, N. Fazıl); ne kastettiği açıksa sorma.

Listede olmayan bir usta istenirse genel bilginle aynı yapıda oku, ama bunu baştan tek cümleyle söyle ve emin olmadığın eser adı, tarih ya da olay örgüsü ayrıntısını verme. Yazar isterse o usta için eklentideki `templates/USTA.md` şablonuyla projenin `ustalar/` klasörüne kalıcı bir mercek dosyası hazırlanabileceğini bir kez söyle.

## 2. Ustayı seç

- **Yazar bir usta adı verdiyse:** o usta.
- **Birkaç usta saydıysa:** sayılan ustalar.
- **`kurul` dediyse ya da usta vermediyse:** metnin ihtiyacına göre en fazla üç usta seç. Kitap dosyasında "Yazarın ustaları" varsa önce onlara bak. Her seçimi bir cümleyle gerekçelendir.

## 3. Oku

**Tek usta:** Mercek dosyasını baştan sona oku, sonra metni oku ve merceğin sorularını metne sor. Raporu aşağıdaki biçimde kendin ver.

**Birden çok usta:** Her usta için `usta-okuru` ajanını **tek mesajda, paralel** olarak Agent aracıyla başlat (alt ajan türü `yazihane:usta-okuru`; ortam ön eksiz adı kullanıyorsa `usta-okuru`). Her birine şunları ver: mercek dosyasının **mutlak yolu**, okunacak metnin mutlak yolları, varsa kitap dosyasının yolu ve yazarın sorusu. Okurlara birbirlerinin merceğini verme. **Agent aracı yoksa** (ör. claude.ai sohbeti) her ustanın mercek dosyasını sırayla okuyup merceği kendin uygula; `editor` becerisindeki "Çalışma ortamı" kuralına uy. Raporlar gelince:

- Her iddianın alıntısını metinde doğrula; bulamadığını at.
- Merceklerin **birleştiği** yeri öne al: farklı ustaların aynı yeri göstermesi en güçlü işarettir.
- Merceklerin **ayrıştığı** yeri (biri "kısalt" derken öteki "aç" diyorsa) çözme; **Tercih meselesi** olarak iki tarafı da göster.
- Toplamda en fazla üç madde.

Metin sohbete yapıştırılmışsa ve ajan çalıştıracaksan önce proje kökünde `yazihane-raporlari/metin-<YYYY-AA-GG>.md` dosyasına kaydet; ajanlar sohbeti göremez. Metin Word ya da ODT dosyasıysa önce `editor` becerisindeki "Metin dosyaları" kuralıyla düz metne çevir.

## 4. Rapor biçimi

```
## <Usta> merceğiyle
**Bu mercek neye bakar:** <bir cümle>
**Metninizde zaten olan:** <1–2 madde; "bu zaten metinde var, güçlendirebiliriz">
**Merceğin gösterdiği:** <en fazla üç madde; her biri [Etiket] başlık — yer + kısa alıntı — ustanın hangi tekniğiyle ilgili olduğu>
**Bu metin için tuzak:** <bir cümle: bu ustadan bu metne yanlış ne taşınabilir>
**Okuma önerisi:** <tek eser ya da bölüm, ve neden>
```

Yeri her zaman paragraf numarasıyla ver (boş satırla ayrılmış blokları baştan say; başlıklar sayılmaz). Merceğin dışında gözüne çarpan Kesin sorunları (süreklilik, imla, olgu) en sona, en fazla üç kısa satırla ekle; ayrıntıyı ilgili moda bırak.

Birden çok usta okuduysan önce birleşik özeti ver (birleşen yer, ayrışan yer, en fazla üç madde), sonra her merceği kısa tut. Cevap telefonda okunacak ölçüde kalsın.

## "X olsa nasıl yazardı?" sorusu

Ustanın bu sahnede vereceği **kararları** anlat: sahneye nereden girerdi, neyi dışarıda bırakırdı, kimin gözünden bakardı, nerede bitirirdi, neyi söyletmezdi. Sahneyi ustanın üslubuyla **yeniden yazma.** Yazar açıkça örnek isterse `iskele` kurallarına uy: başına etiket koy, yazarın sahnesini değil **ilgisiz bir durumu** kullan, kısa tut, ustayı taklit etme, yalnızca tekniği göster.

## Kurallar

- **Yazarın sesi kazanır.** Ustanın sesi ile yazarın sesi çatışıyorsa yazarın sesini koru ve bunu açıkça söyle. "Çehov böyle yapardı, siz de yapın" değil; "Çehov'un merceği şunu görünür kılıyor, karar sizin."
- **Mercek zanaat içindir.** Ustanın hayatı, dünya görüşü ya da siyasi tartışmalar yazar sormadıkça konuşulmaz.
- **Alıntı yapma.** Ustanın tekniğini kendi cümlelerinle anlat; zorunluysa en fazla bir kısa ifade. Telif koruması süren eserlerden (ör. Necip Fazıl, Tanpınar, Atılgan, Atay) hiç alıntı yapma; kamu malı eserlerin Türkçe çevirileri de çevirmenlerinin telifindedir.
- **Bilgide dürüst ol.** Mercek dosyasının dışına çıkarken emin olmadığın eser adı, tarih ya da olay örgüsü ayrıntısı verme.
- **Uydurma ayrıntı önerme.** Ustanın tekniğini uygulamak için ayrıntı gerekiyorsa onu metnin kendi malzemesinden çıkar.
