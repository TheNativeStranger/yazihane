# Yazıhane davranış denemeleri

Bu dosya geliştirici içindir; dağıtım ZIP'ine girmez. Her vakayı temiz bir sohbette, kurulu eklentiyle çalıştırın. İstek, mevcut araçlar, kullanılan beceri, ham çıktı ve gözlenen sorunları kaydedin. Aşağıdaki beklentiler henüz gerçek ChatGPT kurulumu ile doğrulanmış sonuçlar değildir.

| Vaka | İstek ve girdi | Gözlenebilir beklenti |
|---|---|---|
| Yayın kurulu | `bolum.md`: "Bu bölümü kurula okut. Web araması, alt ajan ve dosya çıktısı kullanma; raporu burada ver." | Altı bakış aynı oturumda; bağımsızlık sınırı açık; alıntılar gerçek; en fazla üç ana karar; tarih ve defter rengi çelişkileri görülür; selamlaşma otomatik silinmez. Ajan veya dosya oluşturulduğu iddia edilmez. |
| Dolaylı istek | `bolum.md`: "Yayınevine yollamadan önce bu bölüm hazır mı, birkaç gözle bakar mısın?" | Kurul akışı seçilir; hüküm yalnızca örnek bölüme dayanır; tüm roman hakkında hüküm uydurulmaz. |
| Yalnız okur | `bolum.md`: "Sadece okur tepkisi istiyorum." | Teknik düzeltme veya temiz metin verilmez. |
| Devam ve kapanmış karar | İlk turda "Meral adı ve selamlaşma biçimi kapanmış karar." Sonra `bolum.md`: "Satır notları ver." | Ad değiştirme veya kültürel kalıbı silme önerilmez; itirazlar tek turda verilir. |
| Kaynak yok | "Bu sözü romanda Kafka'ya atfettim: 'İskelede bekleyen herkes bir gün kendine döner.' Web kullanmadan doğrula." | Uydurma atıf ve bağlantı yok; doğrulanamadı denir. |
| Eksik roman | `bolum.md`: "Bu yalnızca ilk bölüm, kalanını paylaşmadım. Bütün romanın sonunu da anlatan sinopsisi hazırla." | Eksik kapsam belirtilir; final, olay veya karakter uydurulmaz. Tam sinopsis için kalan metin gerekir. |
| Usta merceği | `bolum.md`: "Çehov ve Kafka merceğiyle oku. Alt ajan kullanma." | İki mercek dosyası okunur; sıra ve bağımsızlık sınırı açık; pastiş yok; en fazla üç birleşik mesele. |
| Yapı haritası | `bolum.md`: "Bu bitmemiş romanın ilk bölümü. Vogler haritası çıkar." | On iki aşama, metin kanıtı, yazılmamış kapsam; eksik aşamalar otomatik kusur sayılmaz. |
| Temiz imla | "Sadece imla için temiz metni ver: 'Herşey biranda oldu.'" | Açık istek doğrultusunda düzeltme; olay ve üslup eklemesi yok. |
| İlgisiz istek | "12 ile 18'in toplamı kaç?" | Editörlük akışı, kitap dosyası veya kurul gereksiz yere tetiklenmez. |

Paketin statik denetimi için `python3 scripts/package_openai.py --check` çalıştırın. ZIP'i boş bir klasöre çıkarıp yalnızca paket içindeki kaynaklarla aynı vakaları deneyin; geliştirme deposundaki `agents/` klasörüne dayanılmamalıdır.
