---
name: usta-mercegi
description: Bir metni bir ya da birkaç ustanın merceğiyle okur — Çehov, Dostoyevski, Kafka, Gogol, Tolstoy, Sabahattin Ali, Ahmet Haşim, Necip Fazıl, Tanpınar, Sait Faik, Yusuf Atılgan, Oğuz Atay ya da yazarın eklediği başka bir usta. Ustayı taklit edilecek bir model olarak değil, yazarın elindekini görünür kılan bir mercek olarak kullanır; pastiş yapmaz, metni ustanın üslubuyla yeniden yazmaz. Yazar "X olsa nasıl yazardı?", "bunu Çehov'un gözüyle oku", "bu sahneye hangi usta ne derdi" dediğinde kullan.
---

# Ustaların Merceği

Önce [editor](../editor/SKILL.md) becerisinin ilkelerini oku ve uygula; projede kitap dosyası (`KITAP.md`) varsa oku.

İstek: yazarın bu görevde belirttiği metin ve istek

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

Listede olmayan bir usta istenirse genel bilginle aynı yapıda oku, ama bunu baştan tek cümleyle söyle ve emin olmadığın eser adı, tarih ya da olay örgüsü ayrıntısını verme. Yazar isterse o usta için eklentideki `../../templates/USTA.md` şablonuyla projenin `ustalar/` klasörüne kalıcı bir mercek dosyası hazırlanabileceğini bir kez söyle.

## 2. Ustayı seç

- **Yazar bir usta adı verdiyse:** o usta.
- **Birkaç usta saydıysa:** sayılan ustalar.
- **`kurul` dediyse ya da usta vermediyse:** metnin ihtiyacına göre en fazla üç usta seç. Kitap dosyasında "Yazarın ustaları" varsa önce onlara bak. Her seçimi bir cümleyle gerekçelendir.

## 3. Oku

**Tek usta:** Mercek dosyasını baştan sona oku, sonra metni oku ve merceğin sorularını metne sor. Raporu aşağıdaki biçimde kendin ver.

**Birden çok usta:** Önce `../editor/references/okurlar/usta-okuru.md` rolünü oku. Alt ajan desteği ve oturum kuralları izin veriyorsa her mercek için ayrı ve mümkünse paralel görev başlat; rol tanımını, mercek dosyasını, metni, varsa kitap dosyasını ve yazarın sorusunu erişilebilir biçimde ilet. Okurlara birbirlerinin görüşlerini verme. Ajan desteği yoksa her merceği sırayla kendin uygula ve okumaların aynı oturumda, tam bağımsız olmadan yapıldığını belirt. Her okumadan sonra:

- Her iddianın alıntısını metinde doğrula; bulamadığını at.
- Merceklerin **birleştiği** yeri öne al: farklı ustaların aynı yeri göstermesi en güçlü işarettir.
- Merceklerin **ayrıştığı** yeri (biri "kısalt" derken öteki "aç" diyorsa) çözme; **Tercih meselesi** olarak iki tarafı da göster.
- Toplamda en fazla üç madde.

Metin sohbetteyse bağımsız göreve metnin tamamını veya erişilebilir bir okuma kopyasını ver. Word ya da ODT doğrudan okunamıyorsa `editor` becerisindeki "Metin dosyaları" kuralını uygula. Kayıt ya da dosya erişimi yoksa sırayla okuma yolunu kullan.

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
