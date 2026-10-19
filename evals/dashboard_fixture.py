"""Synthetic visual fixture. Never a review of the user's manuscript."""
from pathlib import Path
import argparse
import sys
import json


def fixture(analyzer):
    manifest = {"project": {"title": "Eşik · Yayın kurulu görsel provası", "demo": True}, "chapters": [
        {"id":"b1", "title":"01 / Mektup", "kind":"prose", "paragraphs":[
            "Selin her sabah aynı saatte dükkânın kepengini kaldırırdı. Sokak henüz karanlıktı. Tahta masada annesinden kalan defter dururdu; Selin onu açmaz, yalnızca masanın kenarına iterdi.",
            "O sabah kapının altından bir mektup buldu. Zarfta tek bir cümle vardı: Köprü yıkılmadan karşıya geç. Mektubu masanın üzerine bıraktı. Kapının önünde uzun süre bekledi.",
            "Sanki sokak susmuş gibi geldi ona. İçerideki saat çalışıyordu. İçerideki saat her zamanki sesini çıkarıyordu; yine de Selin, mektubun geldiği sabah bu sesi ilk defa duyduğunu düşündü."]},
        {"id":"b2", "title":"02 / Bekleyiş", "kind":"prose", "paragraphs":[
            "Gitmek istemiyordu. Dükkânı bırakamazdı. Neden bırakamadığını düşünmedi; kapının önünde uzun süre bekledi. Karşı kıyıda ne olduğunu bilmediği için yerinden kıpırdamamayı seçti.",
            "Mektubu masanın üzerine bıraktı. Sanki sokak susmuş gibi geldi ona. Hem kalmak hem gitmek istiyordu. Herşey yerli yerindeydi; eksilen bir şey yoktu.",
            "Kapının önünde uzun süre bekledi. Gitmemek için dükkânı öne sürüyordu, ama son müşterinin ne zaman geldiğini hatırlayamıyordu. Akşam olurken mektubu yeniden eline aldı."]},
        {"id":"b3", "title":"03 / Anahtar", "kind":"prose", "paragraphs":[
            "Yaşlı komşusu kapının eşiğine oturdu. Selin'e bir anahtar uzattı. Karşı kıyıdaki evin anahtarıydı. Komşusu neden sakladığını anlatmadı; Selin de sormadı.",
            "Mektubu masanın üzerine bıraktı. Sanki sokak susmuş gibi geldi ona. Bu kez kapının önünde uzun süre beklemedi; anahtarı cebine koydu.",
            "Akşamın son ışığı masadaki defteri aydınlatıyordu. Anahtarı cebinden çıkarıp defterin yanına koydu, sonra yeniden aldı. Komşusu konuşmadan kalkıp gitti."]},
        {"id":"b4", "title":"04 / Köprü", "kind":"prose", "paragraphs":[
            "Selin dükkânı kilitledi. Anahtarı cebindeydi. Köprüye vardığında ardına bakmadı; kapalı dükkânı artık göremiyordu. İlk tahtanın üstüne bastı.",
            "Karşı kıyıya geçtiğinde köprüden bir tahta koptu. Geri dönmeyeceğini söylemedi. Anahtarı avucunda tuttu ve evin kapısına yürüdü."]},
        {"id":"b5", "title":"05 / Ev · taslak", "kind":"draft", "evaluated":False,"paragraphs":["Evde ne bulacağını henüz bilmiyorum. Belki defterin karşılığı burada açılacak. Bu bölüm henüz taslak; olay ve zaman kesinleşmedi."]},
        {"id":"not", "title":"Yazar notu", "kind":"note", "evaluated":False,"paragraphs":["Yorum: Anahtar ve mektup ilişkisi üzerinde düşünülecek. Bu bir bölüm değil, çalışma notudur."]},
        {"id":"b6", "title":"06 / Devam · planlanan, yazılmadı", "kind":"missing"}
    ]}
    m = analyzer.analyze(manifest,Path("."))
    def ev(ch,p,quote):return {"chapter":ch,"paragraph":p,"quote":quote}
    e1=ev("b1",2,"Köprü yıkılmadan karşıya geç.")
    e2=ev("b2",1,"Dükkânı bırakamazdı.")
    e3=ev("b3",1,"Selin'e bir anahtar uzattı.")
    e4=ev("b4",2,"Karşı kıyıya geçtiğinde köprüden bir tahta koptu.")
    def stage(sid,status,ass,ch,note,e=[]):return {"id":sid,"status":status,"assessment":ass,"chapters":ch,"note":note,"evidence":e}
    c=[stage(1,"green","present",["b1"],"Mektup olağan düzeni bozan somut çağrıdır.",[e1]),stage(2,"yellow","revision",["b2"],"Direnç var; dükkânı bırakamama gerekçesi soyut kalıyor.",[e2]),stage(3,"green","implicit",["b3"],"Anahtar veren komşu yardımcı işlevi görüyor; doğaüstü olması gerekmiyor.",[e3]),stage(4,"green","present",["b4"],"Karşı kıyıya geçişin geri dönüşü zorlaştıran bedeli var.",[e4]),stage(5,"gray","draft",["b5"],"Yalnız taslak bulunuyor; kanonik işlev kararı verilmiyor."),stage(6,"red","not_written",["b6"],"Bu örnekte planlanan devam yazılmadı. Bir kurgu hatası hükmü değildir.")]
    v=[stage(1,"green","present",["b1"],"Dükkân rutini olağan dünyayı kuruyor.",[ev("b1",1,"Selin her sabah aynı saatte dükkânın kepengini kaldırırdı.")]),stage(2,"green","present",["b1"],"Mektup çağrıyı taşıyor.",[e1]),stage(3,"yellow","revision",["b2"],"Ret açık; kaybetme korkusu daha somut bağlanabilir.",[e2]),stage(4,"green","present",["b3"],"Komşunun anahtarı kararın aracını veriyor.",[e3]),stage(5,"green","present",["b4"],"Eşik geçildi; geri dönüş güçleşti.",[e4]),stage(6,"gray","draft",["b5"],"Taslak henüz değerlendirilmiyor."),stage(7,"red","not_written",["b6"],"Planlanan devam henüz yazılmadı; sonuç bölümü değerlendirilmedi.")]
    def module(mid,summary,findings=[],state="complete",**extra):return dict(id=mid,state=state,summary=summary,findings=findings,**extra)
    def find(label,text,e=[]):return {"label":label,"text":text,"evidence":e}
    modules=[
      module("editor","Bu kısa görsel örnekte çağrı, yardım ve geçiş birbirine bağlanıyor. Ana belirsizlik direnç gerekçesinde.",[find("Çalışan","Kırılan köprü eşiğin bedelini olayla gösteriyor.",[e4])]),
      module("gelistirme","Dört kısa parça bir karar çizgisi oluşturuyor. Bekleyişteki tekrarların tempo işlevi tartışmaya açık.",[find("Tercih meselesi","Dükkânın Selin için neyi riske attığı mevcut metinde soyut kalıyor.",[e2])]),
      module("satir","Tekrar taramasındaki mektup ve bekleyiş cümleleri işlev bakımından ayrılmalı.",[find("Tercih meselesi","Mektubu bırakma hareketinin her dönüşü yeni bir iç karar taşımıyor.",[ev("b2",2,"Mektubu masanın üzerine bıraktı.")])]),
      module("imla","Görsel provada tek yazım adayı gösteriliyor; kapsamlı TDK doğrulaması yapılmadı.",[find("Bilgi","“Herşey” → “Her şey”: ayrı yazım adayı; gerçek raporda ilgili TDK kaynağı doğrulanır.",[ev("b2",2,"Herşey yerli yerindeydi;")])],"limited"),
      module("sureklilik","Örnek metindeki anahtar komşudan Selin'e geçiyor, defterin yanına konup yeniden alınıyor. Köprüye cebinde taşınıyor.",[find("Çalışan","Anahtarın sahneler arasındaki yeri izlenebiliyor.",[ev("b3",3,"Anahtarı cebinden çıkarıp defterin yanına koydu, sonra yeniden aldı.")])]),
      module("okur","Mektubun tek cümlesinde meraklandım. İkinci parçadaki bekleyişte hızım düştü. Köprü kırıldığında kararın ciddiyetini hissettim.",[find("Okur tepkisi","Anahtarın hangi kapıyı açacağını merak ediyorum.",[e3])]),
      module("yayinevi","Simülasyon: bu çok kısa örnek bir açılış çizgisi sunuyor. Eser bütünü ve yayımlanabilirliği hakkında karar vermeye yetmez.",[],"limited"),
      module("yapi","Campbell 4 ve Vogler 5, son kanonik olay için desteklenen konumlar. Taslakta sonraki aşamaları tamamlanmış saymıyoruz.",[find("Çalışan","Karşıya geçişin ardından kopan tahta, geri dönüş güçlüğünü somutlaştırıyor.",[e4])]),
      module("iskele","Yalnız teknik farkı göstermek için kısa bir yer tutucu; romanın yeni metni değildir.",sample="[Bekleme hareketi] → [mevcut metindeki gerçek kayıp] → [karakterin seçimi].",technique="Bekleyişi yeni olay eklemeden gerekçe ve seçime bağlayan işlev şeması."),
      module("olgu","Bu görsel provada dış kaynak isteyen tarih, coğrafya veya atıf doğrulaması yapılmadı. Kurgu içi nesne takibi süreklilik kartında.",[],"not_needed"),
      module("tolstoy","Mercek: iç hâlin sahne içinde değişmesi ve seçimin bedeli. Kırılan köprü bu kısa metinde kararın dış karşılığını veriyor.",[find("Çalışan","Karar açıklama yerine bedelle görünür oluyor.",[e4])]),
      module("ahmet-hasim","Mercek: günün saati, ışık ve cümle sesi. Deftere vuran son ışık, ayrılma ânına duygusal zaman katıyor.",[find("Çalışan","Işık bir eşyanın üzerinde toplanıyor; sahneye yeni süs eklemek gerekmiyor.",[ev("b3",3,"Akşamın son ışığı masadaki defteri aydınlatıyordu.")])]),
      module("sabahattin-ali","Mercek: kişinin kendine gösterdiği gerekçeyle davranışı arasındaki açıklık. Dükkânı bahane etmesi mevcut metinde görünür.",[find("Tercih meselesi","Son müşteriyi hatırlamaması, dükkân gerekçesini kendisinin de sınadığını düşündürüyor.",[ev("b2",3,"son müşterinin ne zaman geldiğini hatırlayamıyordu.")])])
    ]
    a={"schema_version":1,"mode":"kurul","metrics_sha256":m["metrics_sha256"],"generated_at":"2026-10-19","coverage_note":"Görsel prova: dört kısa, yapay örnek parça okundu. Beşinci parça taslak, bir yazar notu ve yazılmamış devam ayrı gösterildi. Kullanıcının romanı okunmadı.","reading_mode":"same_session","current":{"chapter":"b4","campbell":[4],"vogler":[5],"summary":"Son kanonik olay karşı kıyıya geçiştir. Campbell 4 ve Vogler 5; taslak konumu değiştirmez.","evidence":[e4]},"maps":{"campbell":c,"vogler":v},"chapter_reviews":[{"chapter":ch,"status":st,"note":note,"evidence":[e]} for ch,st,note,e in [("b1","green","Çağrı somut bir haberle geliyor.",e1),("b2","yellow","Direnç gerekçesi üzerine tercih kararı var.",e2),("b3","green","Yardım ve araç aynı sahnede kuruluyor.",e3),("b4","green","Eşiğin bedeli metinde görünür.",e4)]],"opinions":{"editor":{"state":"complete","summary":"Çağrı, yardımcı ve eşik işliyor. Açılması gereken ana mesele bekleyişin gerekçesi.","evidence":[e2]},"danisman":{"state":"complete","summary":"Dört parça bir karar çizgisi kuruyor. Tekrarların her dönüşünde yeni bir davranış olup olmadığı tartışılabilir.","evidence":[]},"okur":{"state":"complete","summary":"Mektupta meraklandım; bekleyişte hızım düştü; köprü kırıldığında geri dönüşün zorlaştığını hissettim.","evidence":[]},"yayinevi":{"state":"limited","summary":"Simülasyon: açılış fikri görünür; bu kısa örnek eser bütünü veya kabul kararı için yeterli değil.","evidence":[]}},"verdict":"Görsel provada açılış çizgisi okunuyor. Ana karar, bekleyişin gerekçesi ve tekrarların işlevi üzerine; taslaklara hüküm verilmedi.","decisions":[find("Tercih meselesi","Bekleyişin nedenini metinde zaten bulunan dükkân bağıyla belirginleştirmek değerlendirilebilir.",[e2]),find("Tercih meselesi","Tekrarlanan mektup hareketinin motif mi, durağanlık mı olduğuna sahne işleviyle karar verilmeli.",[ev("b2",2,"Mektubu masanın üzerine bıraktı.")])],"disagreements":"Satır okuması tekrarın aşınmasına, Haşim merceği ritim değerine bakıyor. Her tekrar otomatik silinmemeli.","modules":modules}
    return manifest,m,a


if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--skill",type=Path,required=True);p.add_argument("--output",type=Path,required=True);args=p.parse_args()
    sys.path.insert(0,str(args.skill/"scripts"));import analyze
    args.output.mkdir(parents=True,exist_ok=True)
    for name,data in zip(("manifest","metrics","analysis"),fixture(analyze)):
        (args.output/(name+".json")).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(str(args.output.resolve()))
