# Toplu kurulun okuma sözleşmesi

Bu dosya, “yayın kurulu olarak değerlendir” komutunun bütün modlarını tek rapora bağlar. Kullanıcının tek başına okur/imla vb. istemesi tam kurul çağrısı değildir.

## Çalışma sırası

1. Güncel metni, KITAP.md sınırlarını, değerlendirilen bölümleri ve taslak/notları belirle. Satır/paragraf konumlarını sabitle. Ölçümleri bir kez aynı kaynak üzerinden hesapla.
2. Önce önerisiz okur tepkisini kaydet; sonradan editoryal teşhisleri onun ağzına yerleştirme.
3. Editör, geliştirme/danışman, satır, imla, süreklilik, olgu ve yayınevi rollerini kendi ölçütleriyle uygula. Yüklü `yayin-kurulu` kaynaklarından rol tariflerini oku. Uzman unvanları gerçek insan katılımı anlamına gelmez.
4. İki yapı şablonunu ayrı ayrı oku. Ortak saat konumu için metindeki son kanonik olayı kullan; ikisini aynı dilime zorlama. Örtük, farklı, bilinçli atlanan, yazılmamış ve okunmamış durumlarını ayır.
5. Yüklü `usta-mercegi` içindeki `ustalar/tolstoy.md`, `ustalar/ahmet-hasim.md`, `ustalar/sabahattin-ali.md` dosyalarını tam oku. Projenin bu üçü için açıkça verdiği mercek varsa onu esas al. Diğer ustaları toplu çağrıya ekleme.
6. En önemli teknik meseleyi göstermek yararlıysa kısa, etiketli iskele üret. Gerekmediyse `state: not_needed` ve nedenini yaz. Kullanıcının romanından uzun yeniden yazım yapma.
7. Alıntıları ve bütün kesin iddiaları metinde doğrula. Bulamadığın alıntıyı at; kanıt yetersizse iddiayı sınırlı/değerlendirilmedi yap. İmla kuralında emin olmadığında TDK kaynağını kontrol et; olguda doğrulamadığını doğrulanmış sayma.
8. Aynı meseleyi rol sayısı kadar çoğaltma. Birleşen bulguları tek kararda topla; ayrışmaları tercih olarak göster. En fazla üç ana karar; ayrıntıda bütün doğrulanmış satır/imla yerleri kalır.

## Üç mercek için odak

- **Tolstoy:** sahne içinde değişen iç hâl; kararın bedeli; ayrıntının karakterle ahlaki ilişkisi. Anlatıcıyı vaaza veya her şeyi bilen bir sese çekme.
- **Ahmet Haşim:** ses, ritim, ışık, günün saati, duygunun telkini; tekrarın derinleşmesi. Romanı şiire boğma veya süs ekleme.
- **Sabahattin Ali:** görünür kişi ile iç dünya arasındaki fark; kendine mazeret bulan karakter; düzenin somut ilişkileri. Melodram ve tezli açıklama ekleme.

Bu odaklar yüklü kaynakları okumaya alternatif değildir. Ustalar “şöyle derdi” biçiminde uydurma doğrudan konuşmaz; mevcut metindeki bir tercihi görünür kılar.

## Dashboard bağlantısı

`mode: kurul` dosyasında şu modüller bulunmalı: `editor`, `gelistirme`, `satir`, `imla`, `sureklilik`, `okur`, `yayinevi`, `yapi`, `iskele`, `olgu`, `tolstoy`, `ahmet-hasim`, `sabahattin-ali`. Her biri `complete`, `limited`, `not_run` veya `not_needed` durumundadır. Çalıştırılamayan inceleme kartını yok etme; eksikliği göster.

Dört ana bakış: `opinions.editor`, `opinions.danisman`, `opinions.okur`, `opinions.yayinevi`. Ayrıntılı modüller bunların yerine geçmez. Okur kartında düzeltme önerisi bulunmaz. Danışman kartı yapı, davranış ve tempoyu özetler. Yayınevi kartı yalnız incelenen kapsam için hüküm verir.

Bir inceleme sırayla aynı model tarafından yapıldıysa `reading_mode: same_session`; gerçekten bağımsız görevler çalıştıysa `independent`. Rol sayısını bağımsız insan okur sayısı gibi gösterme.
