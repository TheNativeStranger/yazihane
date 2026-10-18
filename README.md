# Yazıhane — Roman Yayın Kurulu

*Literary Editor & Book Coach*

Yayıncı: Ali Osman Akçaoğlu, bireysel geliştirici.

Yazıhane, Türkçe yazan her yazar için hazırlanmış bir editör eklentisidir. Romanınızı ya da öykünüzü bir yayınevinin yayın kurulu gibi okur: altı farklı okur bakışını bir araya getirir, bir baş editör görüşleri doğrulayıp en fazla üç karara indirir. Ortam bağımsız alt ajanları destekliyorsa okumalar ayrı görevlerle, desteklemiyorsa aynı oturumda sırayla yapılır ve bu belirtilir. Ayrıca ustaların merceğiyle okur, imla ve süreklilik denetler, yayınevine gidecek dosyanızı hazırlar.

**0.7.0:** Claude kurulumu yanında ChatGPT ve Codex için taşınabilir, yalnızca becerilerden oluşan OpenAI paketi hazırlanabilir. OpenAI dizinine başvuru ve yayımlama henüz bu depodaki dosyalarla tamamlanmış sayılmaz. [ChatGPT yayımlama rehberi](docs/CHATGPT_YAYINLAMA.md).

**Yazıhane yazarın yerine yazmaz.** Değerlendirir, gösterir, önerir. Eserin son metni her zaman sizin cümlelerinizdir; sesiniz korunur.

**Hiçbir kitaba bağlı değildir.** Eklentinin içinde belirli bir esere ait bilgi yoktur. Kitabınıza dair ne varsa sizin klasörünüzde durur: bölüm dosyalarınız, isterseniz kısa bir `KITAP.md` ve Yazıhane'nin raporları.

## Hızlı başlangıç

1. Eklentiyi kurun (aşağıda).
2. Eserinizin dosyasını ekleyin veya metni yapıştırın; klasör erişimi olan bir ortamda eser klasörünüzü açabilirsiniz. Desteklenen biçimler kullanılan ortamın araçlarına bağlıdır.
3. İsterseniz `/yazihane:kitap-kur` ile eserinizi Yazıhane'ye tanıtın. Bu adım isteğe bağlıdır.
4. Bir bölümü kurula okutun: `/yazihane:yayin-kurulu bolum-01.docx`

Komut yazmak zorunda değilsiniz: "Şu bölüme bir bakar mısın?" demeniz de yeterli. Yazıhane varsayılan olarak metni yeniden yazmadan değerlendirir.

## Yayın kurulu

Claude'da `/yazihane:yayin-kurulu bolum-05.docx`, ChatGPT'de ise Yazıhane seçiliyken "Bu bölümü yayın kuruluna okut" isteği altı okur bakışını çalıştırır. Bağımsız görevler kullanılabildiğinde okurlar birbirinin görüşünü görmez. Baş editör her iddiayı metinde doğrular, aynı meseleleri birleştirir, okurların ayrıştığı yerleri "karar sizin" diye iki taraflı gösterir ve en fazla üç karar çıkarır. Dosya çıktısı destekleniyorsa tam rapor ayrı çıktı olarak kaydedilir; yerel projede `yazihane-raporlari/` kullanılır. Çıktı aracı yoksa rapor sohbette sunulur.

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

## Yapı haritası

`/yazihane:yapi-haritasi vogler` romanınızın yapısını Christopher Vogler'in on iki aşamalı **Yazarın Yolculuğu** şablonuna göre haritalar; `campbell` derseniz Joseph Campbell'ın on yedi aşamalı **Kahramanın Sonsuz Yolculuğu** kullanılır. Yalnızca siz istediğinizde çalışır.

Her aşama için romanda nerede olduğunu (bölüm ve kısa alıntıyla) ve dört durumdan birini gösterir: **metinde var**, **örtük** (işlevini başka bir sahne görüyor), **metinde yok** ya da **bilerek farklı**. Harita bir reçete değildir: Bir aşamanın olmaması tek başına kusur sayılmaz. Yazıhane yalnızca o aşamanın işlevi hiçbir yerde karşılanmıyor ve bu okuru kaybettiriyorsa bunu bir sorun olarak söyler. Roman bitmemişse hikâyenin şu an hangi aşamada olduğunu gösterir; önündeki aşamaları reçete olarak değil, olasılık olarak sıralar.

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
| `/yazihane:yapi-haritasi` | Campbell ya da Vogler şablonuna göre yapı haritası |
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

### ChatGPT ve Codex

OpenAI paketi için depo kökünde Python 3.9 veya üzeriyle:

```bash
python3 scripts/package_openai.py --check
python3 scripts/package_openai.py
```

İkinci komut `dist/yazihane-openai-0.7.0.zip` oluşturur. Paketin kökünde `plugin.json`, `skills/`, `templates/`, `assets/` ve lisans bulunur; Claude'a özgü ajan kayıtları pakete alınmaz. Okur prosedürleri becerilerin içindeki ortak kaynaklardan okunur.

Geliştirme sırasında paketi yerel marketplace desteğiyle kurup temiz bir sohbette deneyin; [resmî test rehberi](https://developers.openai.com/plugins/deploy/connect-chatgpt) kurulumu açıklar. Genel dizinde bulunabilmesi için doğrulanmış geliştirici kimliğiyle OpenAI'ye yüklenmesi, kontrollerin tamamlanması ve onay sonrası yayımlanması gerekir. Ayrıntılar [yayımlama rehberinde](docs/CHATGPT_YAYINLAMA.md). Henüz bir herkese açık ChatGPT kurulum bağlantısı yoktur.

### Claude

**Claude uygulamasında (sohbet ve Cowork):** **Customize → Plugins** bölümünü açın, **Add marketplace** seçin, `isuiteapp/yazihane` yazın ve Yazıhane'yi kurun. Hesabınıza kurulan eklenti Claude Code'da da görünür.

**Claude Code'da ya da Claude masaüstü uygulamasının Code sekmesinde:**

```
/plugin marketplace add isuiteapp/yazihane
/plugin install yazihane@yazihane
```

GitHub'a erişmeden kurmak isterseniz [Sürümler](https://github.com/isuiteapp/yazihane/releases) sayfasından zip dosyasını indirin; Claude uygulamasında **Upload plugin** ile yükleyebilir ya da açtığınız klasörün yolunu Claude Code'daki ilk komutta `isuiteapp/yazihane` yerine yazabilirsiniz.

İlk kullanımlarda Claude; Word dosyalarınızı okuma kopyasına çevirmek, kelime saymak ve rapor klasörü oluşturmak için izin isteyebilir. Bunlar yalnızca okuma ve kopya oluşturma işlemleridir; özgün dosyalarınız değiştirilmez.

## Ortama göre davranış

| Özellik | Araçlar mevcutsa | Araçlar yoksa |
|---|---|---|
| Yayın kurulu ve usta kurulu | Bağımsız alt görevlerle okuma | Aynı oturumda sırayla okuma; bağımsızlık sınırı belirtilir |
| Bölüm dosyaları | İzin verilen dosya veya eklerden okuma | Metni sohbete yapıştırma |
| Rapor ve yayınevi dosyası | Ayrı dosya çıktısı | Sohbette metin çıktısı |
| Olgu doğrulama | Kaynak arama ve sayfa okuma | Doğrulanamadı etiketi; kaynak uydurulmaz |
| Bütün romanın sinopsisi | Tam metne dayanan bölüm haritası | Eksik bölümler belirtilir ve kapsamı sınırlı taslak verilir |

Claude'daki `/yazihane:...` yazımı bütün ortamlarda kayıtlı bir slash komutu olduğu anlamına gelmez. ChatGPT'de doğal dilde istek yeterlidir; kullanılabilir araçları ve eklenti erişimini hesap ile çalışma alanı belirler.

## Ne çalıştırır, nereye bağlanır

- Çalışan eklenti yalnızca talimat dosyaları, kaynaklar, şablonlar ve simgeden oluşur. Kendi sunucusu, MCP bağlantısı veya kancası yoktur. Paketleme betiği yalnızca geliştiricinin hazırlık aracıdır; eklenti çalışırken yürütülmez.
- Metninizi kullandığınız ortamın dosya araçlarıyla okur. Dönüştürme gerekiyorsa mevcut belge araçlarını; yerel ortamda kuruluysa `textutil` veya `pandoc` kullanabilir.
- Raporları ayrı çıktı olarak verir; yerel projede `yazihane-raporlari/` ve `yayinevi-dosyasi/` kullanılır. Açık dosya düzenleme isteği olmadan özgün eseri değiştirmez.
- Olgu denetçisi, alıntıları ve olgusal ayrıntıları doğrulamak için ortamın web araması ve sayfa okuma araçlarını kullanabilir; arama sorgularında metninizden kısa ifadeler geçebilir. Yayınevi dosyası, adını verdiğiniz yayınevinin koşullarını araştırabilir. İşleme ve saklama koşulları kullandığınız yapay zekâ hizmetinin ayarlarına ve politikalarına tabidir.

## Kullanım maliyeti

Yazıhane'nin bu sürümü ücretsizdir; yayıncı eklenti kullanımı için ücret almaz. Eklenti içinde satın alma, ödeme veya abonelik akışı bulunmaz.

Yayın kurulu aynı metni birden fazla açıdan, yayınevi dosyası ise bütün eseri okur. Bunlar tek moda göre daha fazla model kullanımı gerektirebilir; kota ve ücret kullanılan hizmetin planına bağlıdır. Eklentinin kendi haricî API anahtarı veya sunucusu yoktur. Daha kısa bir okuma için tek modları (`okur`, `satir`, `imla`) ya da `hızlı` kurulu seçebilirsiniz.

## Geri bildirim

Hata bildirmek ya da öneride bulunmak için GitHub'daki [Issues](https://github.com/isuiteapp/yazihane/issues) bölümünü kullanabilirsiniz.

## Lisans

MIT. Yazıhane'yi kullanabilir, değiştirebilir ve paylaşabilirsiniz; yalnızca lisans metnini ve yazarın adını koruyun. Ayrıntı için [LICENSE](LICENSE) dosyasına bakın.

[Gizlilik Politikası](docs/PRIVACY.md) · [Kullanım Koşulları](docs/TERMS.md)

## In English

Yazıhane ("the writing room") is a fiction-editing plugin with a Claude-compatible installation and a portable skills-only package for ChatGPT and Codex. Six reader perspectives review a chapter, and a chief editor verifies the findings and reduces them to at most three decisions. Separate readers require host subagent support; otherwise readings run sequentially in one session with an explicit disclosure. It also offers twelve literary lenses, spelling and continuity review, publisher submission drafts, and on-request Campbell/Vogler structure maps. It preserves the writer's voice and does not rewrite unasked. Instructions and reports default to Turkish. Public OpenAI directory availability requires submission, review and publication; this repository does not establish that approval.
