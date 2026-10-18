---
name: kitap-kur
description: Projede kitaba özgü kısa bir KITAP.md hatırlatma dosyası hazırlar — çekirdek, kapanmış kararlar, karakter sesleri, yazım kararları, kapanmış bölümler. Yazar editörü kendi eserine tanıtmak istediğinde kullan.
disable-model-invocation: true
---

Önce `editor` becerisinin ilkelerini uygula (yüklü değilse yükle).

Projede `KITAP.md` varsa oku ve yalnızca yazarın değiştirmek istediği yerleri güncelle. Yoksa `${CLAUDE_PLUGIN_ROOT}/templates/KITAP.md` şablonunu temel al.

Önce metinden çıkarabildiğini çıkar: yazar bölüm dosyalarını gösterdiyse kitap adını, karakterleri, diyalog biçimini ve sık yazım tercihlerini metinden öner. Sonra yazara yalnızca metinden çıkaramadığın şeyleri sor, birkaç soruyu tek mesajda topla: kapanmış kararlar, kapanmış bölümler, söylenmeyen soru ya da proje cümlesi, kaçınılacak kaynaklar.

Dosya kısa kalmalı (bir iki sayfa): bu bir hatırlatmadır, karakter ya da dünya kitabı değildir. Yazarın boş bıraktığı başlıkları sil. Yazmadan önce taslağı göster ve onay al.
