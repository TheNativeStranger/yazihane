# Yerel veri sözleşmesi

Ara dosyalar kullanıcının metnini içerir: geçici çalışma alanında tut, herkese açık depoya koyma. Çıktı HTML'si bütün romanı içermez; yalnızca ölçümler, yorumlar ve seçilmiş kanıt alıntıları gömülür. Betikler dış servis kullanmaz.

## Manifest → ölçümler

```json
{
  "project": {"title": "Eser adı", "demo": false},
  "include_drafts_in_repetitions": false,
  "ignore_words": ["yazarın", "hariç-tuttuğu"],
  "chapters": [
    {"id": "b1", "title": "1. Bölüm", "kind": "prose", "evaluated": true, "locked": false,
     "source": "metin.docx", "start": 1, "end": 25, "omit": [12]},
    {"id": "b2", "title": "2. Bölüm", "kind": "draft", "evaluated": false,
     "paragraphs": [{"number": 26, "text": "Yazarın gerçek taslak metni."}]},
    {"id": "b3", "title": "Yazarın belirttiği yazılmamış bölüm", "kind": "missing"}
  ]
}
```

`source` manifest klasörüne göre veya mutlak yoldur. `start/end` çıkarılmış, başlıklar hariç paragraf numaralarıdır; iki sınır dahil. Aynı metin aralıklarını farklı bölümlere iki kez koyma. `paragraphs` verilirse kaynak aralığı yerine doğrudan bunlar kullanılır; sade metin dizisi de kabul edilir. Başlık satırını paragraf gövdesine koyma. `.docx` biçimli başlıklar ve `.md` # başlıkları otomatik dışlanır. Düz TXT'de bölüm başlıklarını inceleyip açıkça dışla. PDF sayfa akışı düzgün okunamıyorsa sayma; doğrulanmış OCR veya DOCX kullan.

Türler: `prose` (gerçek anlatı), `draft`, `note` (yorum dahil), `raw` (henüz anlatı olarak kabul edilmemiş metin), `missing` (yazarın açıkça belirttiği, metni olmayan bölüm). `missing` için `source/paragraphs` verme. Kaynak biçimi türü belirlemez. Okunmayan anlatıya `evaluated:false` ver. `locked:true` kapanmış yapıyı belirtir; yeniden açılmasına izin vermez.

`metrics.json` bütün kaynak paragrafları, bölüm sayaçları, tekrar adayları ve `metrics_sha256` içerir. Özet, kendi alanı hariç bütün ölçüm JSON'unun UTF-8, sıralı anahtarlarla SHA-256 değeridir; gösterici içeriği yeniden doğrular. Tekrar taraması varsayılan olarak yalnız `evaluated:true, kind:prose` alanında yapılır. Taslakları ancak kullanıcı açıkça dahil ederse ekle. Başlık/not/yorum/iskele sayıları anlatı sayısına karışmaz. `all_words` kaynak türlerinin toplamıdır; anlatı kelimesiyle aynı şey değildir.

## Ölçümler + editoryal okuma → analysis.json

```json
{
  "schema_version": 1,
  "mode": "dashboard",
  "metrics_sha256": "ÖLÇÜM_DOSYASINDAKİ_DEĞER",
  "generated_at": "2026-10-19",
  "coverage_note": "Yalnız 1. bölüm okundu. 2. bölüm taslak; romanın sonu değerlendirilmedi.",
  "reading_mode": "same_session",
  "verdict": "Kapsamla sınırlı ortak hüküm.",
  "current": {
    "chapter": "b1", "campbell": [1], "vogler": [2],
    "summary": "Son kanonik olay çağrı işlevi görüyor; devamı henüz okunmadı.",
    "evidence": [{"chapter":"b1", "paragraph":4, "quote":"Paragrafta aynen bulunan kısa alıntı"}]
  },
  "chapter_reviews": [
    {"chapter":"b1", "status":"green", "note":"İşlevin neden çalıştığı.",
     "evidence":[{"chapter":"b1", "paragraph":4, "quote":"Paragrafta aynen bulunan kısa alıntı"}]}
  ],
  "maps": {
    "campbell": [{"id":1,"status":"green","assessment":"present","chapters":["b1"],
      "note":"Bu çağrı işlevi şu olayla kuruluyor.","evidence":[{"chapter":"b1","paragraph":4,"quote":"Paragrafta aynen bulunan kısa alıntı"}]}],
    "vogler": []
  },
  "opinions": {
    "editor": {"state":"complete","summary":"Kısa editör yorumu.","evidence":[]},
    "danisman": {"state":"limited","summary":"Kurgu, davranış ve tempoya ilişkin kapsamlı olmayan yorum.","evidence":[]},
    "okur": {"state":"complete","summary":"Merak ettim; burada koptum. Öneri verilmez.","evidence":[]},
    "yayinevi": {"state":"limited","summary":"Yalnız okunan örnek üzerinden simülasyon.","evidence":[]}
  },
  "decisions": [{"label":"Tercih meselesi","text":"Bir ana mesele.","evidence":[]}],
  "disagreements": "Görüş ayrılığı varsa; yoksa alanı kaldır.",
  "modules": [{"id":"editor","state":"complete","summary":"Kapsamı belirli sonuç.",
    "findings":[{"label":"Çalışan","text":"Doğrulanmış bulgu.","evidence":[]}]}]
}
```

Yukarıdaki JSON çalıştırılacak örnek veri değildir; gerçek alıntıyla doldur. `evidence` listelerinin her alıntısı belirtilen kaynak paragrafta aynen bulunmalı (boşluk farkı dışında). İddia olmayan kısa genel özet kanıtsız olabilir; belirli metin iddiasına kaynak ekle. Siyah konum işareti ve yeşil/sarı aşamalar okunmuş anlatıdan kanıt ister. Taslak/not/ham/okunmamış bölüm yeşil veya sarı olamaz. Kırmızı bir bölüm `kind:missing` değilse gerçek işlev eksikliği notuyla açıklanır; renk okunduğunu varsaydırmamalı.

### Aşama değerlendirmeleri

| status | assessment |
|---|---|
| green | present, implicit, different |
| yellow | revision |
| red | missing, not_written |
| gray | draft, unassessed |

`chapters` çoklu bölüm kimliği alır, bütün kanıt kimliklerini kapsar. Aşama numaraları `assets/frameworks.json` içindeki tanımlarla aynıdır. Eksik bırakılan aşamalar **gri/değerlendirilmedi** olur; otomatik kırmızıya dönüşmez. İşlevin eksik olduğunu söylemek için yeterli kapsam okunmalıdır. Sonraki aşamalar henüz planlanmadıysa “yazılmadı” diye uydurma plan ekleme. `current` belirsizse model listelerini boş bırak; `summary` ile açıkla. Birden fazla gerçek aday verilebilir, ancak ileri aşamayı otomatik seçme.

### Modüller ve kararlar

`mode:kurul` için [kurul.md](kurul.md) içindeki **13 modülün hepsi** bulunmalı; her biri dürüst durum ve özet taşır. Varsayılan üç usta aynen korunur. Modül durumları: `complete`, `limited`, `not_run`, `not_needed`. Başka bir usta açıkça istenirse sözleşmeyi sessizce geçersiz kılma; bu özel raporu ayrı `mode:dashboard` incelemesi olarak ekle veya betiği kullanıcı isteğine göre genişlet.

`findings` sınırsız ayrıntı listesi; `decisions` en fazla üç ortak ana meseledir. Etiketler: `Kesin sorun`, `Tercih meselesi`, `Ben olsam değiştirirdim`, `Çalışan`, `Okur tepkisi`, `Bilgi`. Kurulun en önemli sorunlarını seç; bulgu yoksa uydurup üçe tamamlama.

İskele modülüne `sample` ve kısa `technique` eklenebilir. Gösterici her iki çıktıda otomatik **[ÖRNEK / İSKELE — kanon değildir]** etiketi koyar. Kaynak kelime/tekrar hesabına alınmaz.

### Çıktı

`render.py` önce alıntıları, kapsamı, kimlikleri ve renk uyumunu doğrular. Başarısız doğrulamayı veri oynayarak gizleme; kaynak/yorum eşleşmesini düzelt. Varsayılan iki dosya üretir; `--html-only` yalnız açık eksiklik bildirilen bir yedektir. HTML JavaScript, CSS ve rapor verisini yerel gömer; CDN ve uzak API yoktur. PDF, gömülü DejaVu fontları ve vektör saatler kullanır; ekran görüntüsü değildir. Uzun raporlarda çok sayfaya bölünür. PDF için `reportlab`, PDF girdisi için `pypdf` bulunmalıdır. Yalnız eksik bağımlılığı mevcut ortamın normal paket yöntemleriyle yükle; anahtar veya hesap gerektirmez.
