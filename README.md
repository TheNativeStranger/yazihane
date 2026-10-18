# Yazıhane — Roman Yayın Kurulu

*Literary Editor & Book Coach*

Yazıhane, Türkçe yazan her yazar için hazırlanmış bir Claude eklentisidir. Romanınızı ya da öykünüzü bir yayınevinin yayın kurulu gibi okur: birbirinden bağımsız altı okur aynı bölümü okur, bir baş editör görüşlerini doğrulayıp en fazla üç karara indirir. Ayrıca ustaların merceğiyle okur, imla ve süreklilik denetler, yayınevine gidecek dosyanızı hazırlar.

**Yazıhane yazarın yerine yazmaz.** Değerlendirir, gösterir, önerir. Eserin son metni her zaman sizin cümlelerinizdir; sesiniz korunur.

**Hiçbir kitaba bağlı değildir.** Eklentinin içinde belirli bir esere ait bilgi yoktur. Kitabınıza dair ne varsa sizin klasörünüzde durur: bölüm dosyalarınız, isterseniz kısa bir `KITAP.md` ve Yazıhane'nin raporları.

## Hızlı başlangıç

1. Eklentiyi kurun (aşağıda).
2. Eserinizin bulunduğu klasörü Claude'da açın. Bölümleriniz .docx, .md, .txt ya da PDF olabilir.
3. İsterseniz `/yazihane:kitap-kur` ile eserinizi Yazıhane'ye tanıtın. Bu adım isteğe bağlıdır.
4. Bir bölümü kurula okutun: `/yazihane:yayin-kurulu bolum-01.docx`

Komut yazmak zorunda değilsiniz: "Şu bölüme bir bakar mısın?" demeniz de yeterli. Yazıhane varsayılan olarak metni yeniden yazmadan değerlendirir.

## Yayın kurulu

`/yazihane:yayin-kurulu bolum-05.docx` bir bölümü altı bağımsız okura aynı anda okutur. Okurlar birbirinin görüşünü görmez. Baş editör her iddiayı metinde doğrular, aynı meseleleri birleştirir, okurların ayrıştığı yerleri "karar sizin" diye iki taraflı gösterir ve en fazla üç karar çıkarır. Tam rapor `yazihane-raporlari/` klasörüne kaydedilir.

| Okur | Ne yapar |
|---|---|
| Beta okur | İlk kez okuyan okurun tepkisi; düzeltme önermez |
| Geliştirme editörü | Hikâye, yapı, sahne işlevi, karakter, tempo |
| Satır editörü | Ritim, tekrar, klişe, belirsiz özne |
| Redaktör | TDK'ya göre imla ve süreklilik |
| Olgu denetçisi | Alıntı, atıf, tarih ve ayrıntı doğrulama |
| Yayınevi okuru | Okur raporu: ses, okur kitlesi, kabul / revizyon / ret |

`hızlı` eklerseniz yalnızca beta okur, geliştirme editörü ve yayınevi okuru çalışır. `usta:cehov` eklerseniz kurula bir ustanın merceği de katılır.

## Ustaların merceği

`/yazihane:usta-mercegi cehov bolum-05.docx` bir bölümü bir ustanın gözüyle okur. Ustalar taklit edilecek model değil, metninizde zaten olanı ve olabilecek olanı görünür kılan mercektir; Yazıhane metni ustanın üslubuyla yeniden yazmaz.

Hazır mercekler: **Çehov, Dostoyevski, Kafka, Gogol, Tolstoy, Sabahattin Ali, Ahmet Haşim, Necip Fazıl, Tanpınar, Sait Faik, Yusuf Atılgan, Oğuz Atay.** Her mercekte ustanın tekniği, metne sorulacak sorular, ustadan yanlış öğrenmenin tuzakları ve çalışılacak eserler vardır.

- Birkaç usta: `/yazihane:usta-mercegi cehov,tolstoy bolum-05.docx` — her usta ayrı okur, sonra merceklerin birleştiği ve ayrıştığı yer gösterilir.
- Seçimi Yazıhane'ye bırakmak: `/yazihane:usta-mercegi kurul bolum-05.docx` — metne en uygun en fazla üç usta.
- Kendi ustanızı eklemek: `templates/USTA.md` şablonunu eserinizin klasöründe `ustalar/<usta-adi>.md` olarak kaydedin.

## Yayınevi dosyası

`/yazihane:yayinevi-dosyasi` eserinizi yayınevine göndermek için gereken belgeleri hazırlar ve `yayinevi-dosyasi/` klasörüne koyar:

- kitap kimliği: tür, uzunluk, tek cümlelik ve tek paragraflık öz, okur kitlesi
- sinopsis: sonu da anlatan bir iki sayfa
- tanıtım mektubu ve kısa yazar biyografisi
- örnek bölüm seçimi ve arka kapak yazısı (en fazla iki seçenek)
- gönderim kontrol listesi

Sonra dosyayı bir yayınevi okurunun gözüyle sınar: Mektup ve sinopsis onu örnek bölümlere taşıyor mu, dosyanın tamamını ister mi?

Belgelerin hepsi **taslaktır**. Yazıhane sizin hakkınızda, yayınevi hakkında ya da kitabınız için hiçbir bilgi, övgü ya da ödül uydurmaz; bilmediği her şeye yer tutucu bırakır ve sonunda bir "Sizden gerekenler" listesi verir. Tek bir parça da isteyebilirsiniz: `sinopsis`, `mektup`, `biyografi`, `arka-kapak`, `kapak-brief`, `bulten`. Bir yayınevinin adını verirseniz o yayınevinin dosya gönderim koşullarını da arar. Uzun romanlarda bölümler paralel okunur ve bir bölüm haritası çıkarılır; sinopsis bütün esere dayanır.

## Tek tek çalışma modları

| Komut | Ne yapar |
|---|---|
| `/yazihane:okur` | Yalnızca okur tepkisi |
| `/yazihane:gelistirme` | Hikâye ve yapı üzerine en fazla üç ana mesele |
| `/yazihane:satir` | Bütün itirazlar tek seferde (`temiz` derseniz temiz metin) |
| `/yazihane:imla` | TDK'ya göre yazım ve noktalama |
| `/yazihane:sureklilik` | Zaman, mekân, kim neyi biliyor, nesneler, yaşlar |
| `/yazihane:iskele` | Yalnızca istenince, etiketli örnek metin |
| `/yazihane:usta-mercegi` | Bir ya da birkaç ustanın merceğiyle okuma |
| `/yazihane:yayinevi-dosyasi` | Yayınevine gönderilecek dosyayı hazırlar |
| `/yazihane:kitap-kur` | Eseriniz için kısa bir `KITAP.md` hazırlar |

## Kitap dosyası

Eserinizin klasörüne isterseniz bir `KITAP.md` koyabilirsiniz (`templates/KITAP.md` şablonu ya da `/yazihane:kitap-kur`). Kapanmış kararlarınız, karakter sesleri, yazım tercihleriniz, kapanmış bölümleriniz ve ustalarınız orada durur. Kitap dosyası Yazıhane'nin genel ilkeleriyle çelişirse sizin dosyanız kazanır. Dosya yoksa Yazıhane genel ilkelerle çalışır.

## Yazıhane'nin ilkeleri

- Metni istenmeden yeniden yazmaz. Örnek metin yalnızca istenince ve "örnek" etiketiyle verilir.
- Bulduklarını üç etiketle ayırır: **Kesin sorun**, **Tercih meselesi**, **Ben olsam değiştirirdim**. Varsayılan olarak en fazla üç ana mesele söyler; çalışan şeyi de adıyla söyler.
- Sesinizi atölye yazarlığının ya da çeviri romanların düz dokusuna çekmez; selam, dua, hâl hatır gibi kültürel kalıpları silmez.
- Hiçbir bilgi, övgü, ödül ya da kaynak uydurmaz; bilmediğini yer tutucuyla bırakır.
- Ustalardan alıntı yapmaz; telif haklarına saygı gösterir.
- İmlada ölçü TDK'dır; bilinçli üslup tercihlerinizi düzeltmez, sorar.

## Kurulum

**Claude uygulamasında (sohbet ve Cowork):** **Customize → Plugins** bölümünü açın, **Add marketplace** seçin, `isuiteapp/yazihane` yazın ve Yazıhane'yi kurun. Hesabınıza kurulan eklenti Claude Code'da da görünür.

**Claude Code'da ya da Claude masaüstü uygulamasının Code sekmesinde:**

```
/plugin marketplace add isuiteapp/yazihane
/plugin install yazihane@yazihane
```

GitHub'a erişmeden kurmak isterseniz [Sürümler](https://github.com/isuiteapp/yazihane/releases) sayfasından zip dosyasını indirin; Claude uygulamasında **Upload plugin** ile yükleyebilir ya da açtığınız klasörün yolunu Claude Code'daki ilk komutta `isuiteapp/yazihane` yerine yazabilirsiniz.

İlk kullanımlarda Claude; Word dosyalarınızı okuma kopyasına çevirmek, kelime saymak ve rapor klasörü oluşturmak için izin isteyebilir. Bunlar yalnızca okuma ve kopya oluşturma işlemleridir; özgün dosyalarınız değiştirilmez.

## Nerede çalışır

| | Claude Code | Cowork | Sohbet (claude.ai) |
|---|---|---|---|
| Tek tek modlar (okur, satır, imla, süreklilik…) | Evet | Evet | Evet |
| Yayın kurulu ve usta kurulu | Bağımsız okurlar aynı anda okur | Bağımsız okurlar aynı anda okur | Okurlar sırayla tek oturumda okur; bağımsızlık sınırlıdır |
| Bölüm dosyaları | Klasörünüzden okunur (.docx dahil) | Klasörünüzden okunur | Metni yapıştırın ya da dosyayı ekleyin |
| Bütün bir romanın sinopsisi | Evet | Evet | Uzun eserlerde sınırlı; Cowork ya da Claude Code önerilir |

## Ne çalıştırır, nereye bağlanır

- Yazıhane yalnızca talimat dosyalarından (beceriler ve okur tanımları) oluşur. Kendi sunucusu, bağlantısı (MCP), kancası ya da programı yoktur; hiçbir yere kendiliğinden veri göndermez.
- Metninizi Claude'un dosya okuma araçlarıyla okur. Word, ODT ya da RTF dosyalarının düz metin kopyasını çıkarmak için macOS'ta `textutil`, kuruluysa `pandoc`; kelime saymak için `wc` komutunu çalıştırır.
- Raporları eserinizin klasöründe `yazihane-raporlari/` ve `yayinevi-dosyasi/` klasörlerine yazar. Özgün dosyalarınızı değiştirmez.
- Olgu denetçisi, alıntıları ve olgusal ayrıntıları doğrulamak için Claude'un web araması ve sayfa okuma araçlarını kullanır; arama sorgularında metninizden kısa ifadeler geçebilir. Yayınevi dosyası, adını verdiğiniz yayınevinin dosya gönderim koşullarını bulmak için web araması yapabilir.

## Kullanım maliyeti

Yayın kurulu altı okuru aynı anda çalıştırır; yayınevi dosyası bütün eseri okur. Bu iki komut, Claude kullanım kotanızdan sıradan bir sohbete göre birkaç kat fazla harcar. Günlük çalışmada tek modları (`okur`, `satir`, `imla`) ya da `hızlı` kurulu kullanın; tam kurulu bir bölümü bitirdiğinizde çalıştırın.

## Geri bildirim

Hata bildirmek ya da öneride bulunmak için GitHub'daki [Issues](https://github.com/isuiteapp/yazihane/issues) bölümünü kullanabilirsiniz.

## Lisans

MIT. Yazıhane'yi kullanabilir, değiştirebilir ve paylaşabilirsiniz; yalnızca lisans metnini ve yazarın adını koruyun. Ayrıntı için [LICENSE](LICENSE) dosyasına bakın.

## In English

Yazıhane ("the writing room") is a Claude plugin for Turkish-language fiction writers. It works like a publishing house's editorial board: six independent readers (beta reader, developmental editor, line editor, copy editor following the Turkish Language Association rules, fact-checker and publisher's reader) review a chapter, and a chief editor verifies their findings and reduces them to at most three decisions. It can also read a text through the lens of twelve masters (Chekhov, Dostoevsky, Kafka, Gogol, Tolstoy and major Turkish writers) without imitating them, and it prepares a submission package for publishers (synopsis, cover letter, author bio, back-cover copy, checklist). It never rewrites the author's text unasked, never invents facts, credentials or praise, and protects the author's own voice. All instructions and output are in Turkish.
