# Yazıhane'yi ChatGPT eklentisi olarak yayımlama

Bu depo, Claude ile aynı editoryal kaynakları kullanan taşınabilir bir OpenAI eklenti paketi üretir. Paket yalnızca becerilerden oluşur; MCP sunucusu, ayrı hesap, API anahtarı veya barındırılan uygulama gerektirmez. Dosya ve web işlemlerini kullanılan ortam sağlar.

**Durum:** Paket hazırlığı, OpenAI'ye yükleme, inceleme ve katalogda yayımlama ayrı aşamalardır. Bu dosyanın varlığı onay veya yayında olma anlamına gelmez. Başvuru öncesinde kurulu paketle gerçek ChatGPT denemesi yapılmalıdır.

## Paketi üret

Python 3.9 veya üzeriyle depo kökünde:

```bash
python3 scripts/package_openai.py --check
python3 scripts/package_openai.py
```

Çıktı: `dist/yazihane-openai-0.8.0.zip`.

Betik manifest sürümlerini, katalog metni sınırlarını, beceri başlıklarını, paket içi yolları ve simgeyi denetler. Arşive yalnızca `plugin.json`, `LICENSE`, `skills/`, `templates/` ve `assets/` girer. Git geçmişi, Claude ajan kayıtları, geliştirici betikleri, değerlendirme belgeleri ve kullanıcı eserleri dağıtımın parçası değildir. Kullanıcı metinlerini bu kaynak klasörlerine koymayın.

Yerel doğrulama, OpenAI'nin otomatik taramasının veya gerçek ortam testinin yerine geçmez.

## Kurulu paketi dene

OpenAI'nin [tam eklenti test rehberindeki](https://developers.openai.com/plugins/deploy/connect-chatgpt) yerel marketplace yolunu kullanın. Ortamın desteklediği yerel marketplace kaydında bu paketin kökünü kaynak gösterin; ChatGPT masaüstü uygulaması `.claude-plugin/marketplace.json` uyumluluk yolunu da destekler. Son kullanıcı kurulumu ile geliştirici testini birbirine karıştırmayın.

Temiz bir sohbette eklentiyi etkinleştirip `evals/cases.md` içindeki doğrudan, dolaylı, devam ve sınır örneklerini deneyin. Özellikle sırayla okuma, eksik roman, web araması olmadan doğrulama ve dosya kaydedememe davranışlarını gözleyin. Çıktıları, kullanılan ortamı ve hangi araçların mevcut olduğunu kaydedin.

## OpenAI'ye başvur

Dört katalog bağlantısı kök manifestte tanımlıdır: yayıncıyı ve eklentiyi tanıtan README, GitHub Issues destek sayfası, [Gizlilik Politikası](PRIVACY.md) ve [Kullanım Koşulları](TERMS.md). Sayfalar herkese açık `codex/chatgpt-plugin` dalında yayımlanmıştır. Bu dalı kaldırmadan önce katalog bağlantılarını kalıcı yeni konumlarına taşıyın. Yayıncı bireysel geliştirici Ali Osman Akçaoğlu'dur; 0.8.0 sürümü ücretsizdir ve yayıncı kullanıcı metinlerini ayrıca toplamaz, saklamaz veya paylaşmaz. Bu açıklama kullanılan yapay zekâ platformunun işlemesini veya isteğe bağlı web sorgularını kapsam dışı bırakmaz; ayrıntılar gizlilik politikasındadır. Paket, mevcut simgenin 512 × 512 PNG sürümünü kullanır.

1. [OpenAI eklenti başvuru rehberini](https://developers.openai.com/plugins/deploy/submission) açın ve oradaki **Plugins** bağlantısını izleyin. Eklentinin sahibi olacak organizasyon ve projeyi seçin.
2. Başvuruyu yapacak hesap organizasyon sahibi olmalı veya **Apps Management Write** yetkisine sahip olmalıdır. Katalogdaki yayıncı adı için bireysel ya da işletme kimlik doğrulamasını tamamlayın.
3. **Upload new or existing plugin → Upload plugin** ile üretilen ZIP'i yükleyin. Eski arayüzde yol **Create plugin → Skills only** olarak görünebilir. Yazıhane için MCP bağlantısı eklemeyin.
4. Katalog adı, açıklama, yayıncı, kategori, simge ve örnek isteklerin doğru aktarıldığını kontrol edin. Temel açıklama İngilizcedir; Türkçe çeviri de pakette bulunur. Güncel rehber çevirilerin içe aktarıldığını, fakat katalog görünümüne henüz yansımayabileceğini belirtir.
5. **Metadata & Skills** taramasındaki bulguları inceleyin. Düzeltmeler paket dosyalarında yapılır; yeni ZIP yüklenir. Yerel denetimden geçen bir paket yine de tarama bulgusu alabilir.
6. Kurulu paketin denemelerini tamamlayıp **Submit for review** adımındaki gerekli beyanları hesap sahibi olarak değerlendirin. Yalnızca beceri içeren eklentiler için MCP'ye özgü sekiz test vakası ve demo videosu istenmez; genel katalog uygunluğu ve inceleme yine gereklidir.
7. Onay sonrasında **Publish plugin** ile yayımlayın. Herkese açık eklenti bağlantısını ancak katalog gerçekten yayımlandığında README'ye ekleyin.

`publication.countries: []` paket düzeyinde ülke kısıtlaması koymaz. Hizmetin desteklediği ülkeler, hesap planı, çalışma alanı ve cihaz desteği ayrıca geçerlidir; bu paket herkese sınırsız veya ücretsiz erişim vaadi vermez.

Geliştirici kimliği, hesap yetkileri, başvuru beyanları ve OpenAI'nin inceleme kararı GitHub dosyalarıyla tamamlanamaz. Bu adımlar hesap sahibinin başvuru portalında yapılır.

## Güncelle

Ortak becerileri `skills/` içinde düzenleyin. Claude ajanları bu ortak rol kaynaklarına yönlenir; ikinci bir okur prosedürü kopyası tutmayın. Sürümü hem kök `plugin.json` hem `.claude-plugin/plugin.json` içinde yükseltin; paketi yeniden üretin. OpenAI'de mevcut eklentiye yeni ZIP yükleyerek inceleme ve yayımlama akışını izleyin.

## Resmî kaynaklar

- [Claude eklentisini OpenAI'ye taşıma](https://developers.openai.com/plugins/guides/submit-claude-plugin)
- [Taşınabilir manifest ve paket düzeni](https://developers.openai.com/plugins/build/plugins)
- [Paket yükleme ve yayımlama alanları](https://developers.openai.com/plugins/deploy/submission)
- [Kurulu eklentiyi test etme](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Katalog ilkeleri](https://developers.openai.com/plugins/plugin-guidelines)

Bu yönlendirme 19 Ekim 2026 tarihinde kontrol edilen belgelere dayanır. Başvuru anında güncel gereksinimleri tekrar kontrol edin.
