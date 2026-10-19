#!/usr/bin/env python3
"""Validate evidence, then create a self-contained dashboard and vector PDF locally."""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import html
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
COLORS = {"green": "#2B8064", "yellow": "#EDBB4A", "red": "#C65D56", "gray": "#ADB4B1"}
STATUS = {"green": "Çalışıyor", "yellow": "Gözden geçir", "red": "Eksik", "gray": "Değerlendirilmedi"}
ASSESS = {"present": "Metinde var", "implicit": "Örtük işlev", "different": "Bilinçli farklı kuruluş", "revision": "Revizyon gerekli", "missing": "İşlev eksik", "not_written": "Henüz yazılmadı", "draft": "Taslak / not", "unassessed": "Değerlendirilmedi"}
KINDS = {"prose": "Anlatı", "draft": "Taslak", "note": "Not / yorum", "raw": "Ham metin", "missing": "Henüz yazılmadı"}
STATES = {"complete": "İncelendi", "limited": "Sınırlı inceleme", "not_run": "Çalıştırılmadı", "not_needed": "Gerekmedi"}
MODULES = {"editor": "Editör", "gelistirme": "Geliştirme / danışman", "satir": "Satır editörlüğü", "imla": "İmla", "sureklilik": "Süreklilik", "okur": "Okur", "yayinevi": "Yayınevi okuru", "yapi": "Yapı haritası", "iskele": "Örnek / iskele", "olgu": "Olgu denetimi", "tolstoy": "Tolstoy merceği", "ahmet-hasim": "Ahmet Haşim merceği", "sabahattin-ali": "Sabahattin Ali merceği"}
ROLES = {"editor": "Editör", "danisman": "Danışman", "okur": "Okur", "yayinevi": "Yayınevi · simülasyon"}
LABELS = {"Kesin sorun", "Tercih meselesi", "Ben olsam değiştirirdim", "Çalışan", "Okur tepkisi", "Bilgi"}


def compact(value):
    return " ".join(value.split())


def validate(metrics, analysis):
    if metrics.get("schema_version") != 1 or analysis.get("schema_version") != 1:
        raise ValueError("Unsupported schema version.")
    actual_digest = hashlib.sha256(json.dumps({k:v for k,v in metrics.items() if k != "metrics_sha256"}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if actual_digest != metrics.get("metrics_sha256"):
        raise ValueError("Metrics content changed after measurement; recompute from source.")
    if analysis.get("metrics_sha256") != metrics.get("metrics_sha256"):
        raise ValueError("The review belongs to different text/metrics; recompute and review the new source.")
    if analysis.get("mode", "dashboard") not in {"dashboard", "kurul"}:
        raise ValueError("mode must be dashboard or kurul.")
    chapters = {c["id"]: c for c in metrics["chapters"]}
    if not analysis.get("coverage_note"):
        raise ValueError("A truthful coverage_note is required.")
    if analysis.get("reading_mode") not in {"same_session", "independent"}:
        raise ValueError("Disclose same_session or independent reading_mode.")

    def evidence(items, canonical=False, reviewed=False):
        if not isinstance(items, list):
            raise ValueError("Evidence must be a list.")
        for ref in items:
            chapter = chapters.get(ref.get("chapter"))
            if not chapter:
                raise ValueError("Unknown chapter in evidence.")
            paragraph = next((p for p in chapter["paragraphs"] if p["number"] == ref.get("paragraph")), None)
            quote = ref.get("quote", "")
            if not isinstance(quote, str) or not quote.strip() or not paragraph or compact(quote) not in compact(paragraph["text"]):
                raise ValueError(f"Quote not found at {ref.get('chapter')} ¶{ref.get('paragraph')}.")
            if canonical and (chapter["kind"] != "prose" or not chapter["evaluated"]):
                raise ValueError("A working/revision stage or current position needs evidence from evaluated prose.")
            if reviewed and not chapter["evaluated"]:
                raise ValueError("Editorial claims cannot use evidence from outside the evaluated scope.")

    def scan(item):
        if isinstance(item, dict):
            if "evidence" in item:
                evidence(item["evidence"])
            for key, value in item.items():
                if key != "evidence":
                    scan(value)
        elif isinstance(item, list):
            for value in item:
                scan(value)
    scan(analysis)
    frameworks = json.loads((ROOT / "assets/frameworks.json").read_text(encoding="utf-8"))
    maps = {}
    for model, definitions in frameworks.items():
        supplied = {}
        for stage in analysis.get("maps", {}).get(model, []):
            sid = stage.get("id")
            if sid not in range(1, len(definitions) + 1) or sid in supplied:
                raise ValueError(f"Duplicate or invalid {model} stage ID.")
            supplied[sid] = stage
        maps[model] = []
        for definition in definitions:
            stage = dict(definition, status="gray", assessment="unassessed", chapters=[], note="Bu aşama henüz değerlendirilmedi.", evidence=[])
            stage.update(supplied.get(definition["id"], {}))
            status, assessment = stage["status"], stage["assessment"]
            if status not in STATUS or assessment not in ASSESS:
                raise ValueError("Invalid status/assessment.")
            allowed = {"green": {"present", "implicit", "different"}, "yellow": {"revision"}, "red": {"missing", "not_written"}, "gray": {"draft", "unassessed"}}
            if assessment not in allowed[status]:
                raise ValueError("Status and assessment contradict each other.")
            if not stage["note"].strip():
                raise ValueError("Every stage needs an assessment note.")
            if any(cid not in chapters for cid in stage["chapters"]):
                raise ValueError("Unknown chapter in a stage.")
            if status in {"green", "yellow"}:
                if not stage["evidence"]:
                    raise ValueError("Green/yellow stages require source evidence.")
                evidence(stage["evidence"], canonical=True)
                if not stage["chapters"] or any(chapters[c]["kind"] != "prose" or not chapters[c]["evaluated"] for c in stage["chapters"]):
                    raise ValueError("Draft/note/unread chapters cannot support green/yellow stages.")
            if any(ref["chapter"] not in stage["chapters"] for ref in stage["evidence"]):
                raise ValueError("Stage evidence must be included in its chapter links.")
            if status == "red" and assessment == "missing":
                if not stage["chapters"] or any(chapters[c]["kind"] != "prose" or not chapters[c]["evaluated"] for c in stage["chapters"]):
                    raise ValueError("A missing-function judgment must refer to evaluated prose, not a draft or unread chapter.")
            if assessment == "not_written" and any(chapters[c]["kind"] != "missing" for c in stage["chapters"]):
                raise ValueError("Not-written stages may link only to explicitly missing chapters; existing drafts stay gray.")
            maps[model].append(stage)
    reviews = {}
    for review in analysis.get("chapter_reviews", []):
        cid = review.get("chapter")
        if cid not in chapters or cid in reviews or review.get("status") not in STATUS:
            raise ValueError("Invalid or duplicate chapter review.")
        chapter = chapters[cid]
        if (chapter["kind"] not in {"prose", "missing"} or not chapter["evaluated"]) and chapter["kind"] != "missing" and review["status"] != "gray":
            raise ValueError("Draft/note/raw/unread chapter reviews must be gray.")
        if chapter["kind"] == "missing" and review["status"] != "red":
            raise ValueError("An explicitly missing chapter must be red.")
        if review["status"] in {"green", "yellow"}:
            if not review.get("evidence"):
                raise ValueError("Green/yellow chapter reviews need evidence.")
            evidence(review["evidence"], canonical=True)
            if any(ref["chapter"] != cid for ref in review["evidence"]):
                raise ValueError("Chapter review evidence must refer to that chapter.")
        reviews[cid] = review
    output_chapters = []
    for chapter in metrics["chapters"]:
        default = {"chapter": chapter["id"], "status": "red" if chapter["kind"] == "missing" else "gray", "note": "Henüz yazılmadı." if chapter["kind"] == "missing" else "Editoryal değerlendirme yapılmadı.", "evidence": []}
        output_chapters.append(dict({k:v for k,v in chapter.items() if k not in {"paragraphs", "source", "source_sha256"}}, review=reviews.get(chapter["id"], default)))
    current = analysis.get("current", {})
    has_position = any(current.get(model) for model in frameworks)
    if has_position:
        if current.get("chapter") not in chapters or not current.get("evidence") or not current.get("summary"):
            raise ValueError("A current position requires chapter, explanation and evidence.")
        evidence(current["evidence"], canonical=True)
        if any(ref["chapter"] != current["chapter"] for ref in current["evidence"]):
            raise ValueError("Current evidence must refer to the current chapter.")
    for model in frameworks:
        ids = current.get(model, [])
        if not isinstance(ids, list) or len(ids) != len(set(ids)) or any(i not in range(1, len(frameworks[model])+1) for i in ids):
            raise ValueError("Invalid current stage IDs.")
        for sid in ids:
            stage = maps[model][sid - 1]
            if stage["status"] not in {"green", "yellow"} or current["chapter"] not in stage["chapters"]:
                raise ValueError("Current position must link to an evidenced stage in the current chapter.")
    if len(analysis.get("decisions", [])) > 3:
        raise ValueError("The joint decision may contain at most three main issues.")
    for decision in analysis.get("decisions", []):
        if decision.get("label") not in LABELS:
            raise ValueError("Invalid decision label.")
        evidence(decision.get("evidence",[]),reviewed=True)
    module_ids = set()
    for module in analysis.get("modules", []):
        mid = module.get("id")
        if mid not in MODULES or mid in module_ids or module.get("state") not in STATES or not module.get("summary"):
            raise ValueError("Invalid, duplicate or undocumented review module.")
        module_ids.add(mid)
        evidence(module.get("evidence",[]),reviewed=True)
        for finding in module.get("findings", []):
            if finding.get("label") not in LABELS or not finding.get("text"):
                raise ValueError("Invalid module finding.")
            evidence(finding.get("evidence",[]),reviewed=True)
        if module.get("sample") and mid != "iskele":
            raise ValueError("Only the iskele module may include sample prose.")
    if analysis.get("mode") == "kurul" and module_ids != set(MODULES):
        raise ValueError("Full kurul mode requires all 13 review cards, including the three selected master lenses.")
    opinions = {}
    for role in ROLES:
        item = analysis.get("opinions", {}).get(role, {"summary": "Bu bakış henüz çalıştırılmadı.", "state": "not_run", "evidence": []})
        if item.get("state") not in STATES or not item.get("summary"):
            raise ValueError("Each opinion needs summary and honest state.")
        evidence(item.get("evidence",[]),reviewed=True)
        opinions[role] = item
    return {"project": metrics.get("project", {}), "metrics_sha256": metrics["metrics_sha256"], "summary": metrics["summary"], "lexical": metrics["lexical"], "method": metrics["method"], "chapters": output_chapters, "analysis": dict(analysis, maps=maps, opinions=opinions), "labels": {"status": STATUS, "assessment": ASSESS, "kinds": KINDS, "states": STATES, "modules": MODULES, "roles": ROLES}, "colors": COLORS}


def write_html(data, path):
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    template = (ROOT / "assets/dashboard.html").read_text(encoding="utf-8")
    path.write_text(template.replace("__YAZIHANE_DATA__", payload), encoding="utf-8")


def create_pdf(data, path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A3, landscape
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Flowable, CondPageBreak

    pdfmetrics.registerFont(TTFont("Yazi", str(ROOT / "assets/DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("YaziBold", str(ROOT / "assets/DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFontFamily("Yazi", normal="Yazi", bold="YaziBold", italic="Yazi", boldItalic="YaziBold")
    needed = {ord(c) for c in json.dumps(data,ensure_ascii=False) if not c.isspace()}
    for name in ("Yazi","YaziBold"):
        unsupported = needed - set(pdfmetrics.getFont(name).face.charToGlyph)
        if unsupported:
            codes = ", ".join(f"U+{value:04X}" for value in sorted(unsupported)[:12])
            raise ValueError(f"PDF font lacks {codes}. Supply a compatible font asset before delivery; HTML can still be created.")
    styles = getSampleStyleSheet()
    for name in styles.byName:
        styles[name].fontName = "Yazi"
    styles.add(ParagraphStyle("BodyY", fontName="Yazi", fontSize=10, leading=14, textColor=colors.HexColor("#253E35"), spaceAfter=5))
    styles.add(ParagraphStyle("SmallY", parent=styles["BodyY"], fontSize=8, leading=11, textColor=colors.HexColor("#50655D")))
    styles.add(ParagraphStyle("H1Y", parent=styles["BodyY"], fontName="YaziBold", fontSize=29, leading=34, spaceAfter=10, keepWithNext=True))
    styles.add(ParagraphStyle("H2Y", parent=styles["BodyY"], fontName="YaziBold", fontSize=17, leading=22, spaceBefore=10, spaceAfter=9))
    styles.add(ParagraphStyle("H3Y", parent=styles["BodyY"], fontName="YaziBold", fontSize=12, leading=16, spaceBefore=5, spaceAfter=6, keepWithNext=True))
    styles.add(ParagraphStyle("KPIY", parent=styles["BodyY"], fontName="YaziBold", fontSize=23, leading=28))
    styles.add(ParagraphStyle("ClockY", parent=styles["BodyY"], fontName="YaziBold", alignment=TA_CENTER, fontSize=10, leading=14))

    def P(value, style="BodyY"):
        return Paragraph(html.escape(str(value)).replace("\n", "<br/>"), styles[style])

    chapters = {c["id"]: c for c in data["chapters"]}
    def refs(items):
        return " · ".join(dict.fromkeys(f'{chapters[r["chapter"]]["title"]} ¶{r["paragraph"]}' for r in items))

    def evidence(items):
        return [P(f'“{r["quote"]}” — {refs([r])}', "SmallY") for r in items]

    width, height = landscape(A3)
    available = width - 72
    green = colors.HexColor("#1C5145")
    gold = colors.HexColor("#D8B976")
    light = colors.HexColor("#EEF3EF")

    def table(rows, widths, header=True):
        t = Table(rows, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
        rules = [("VALIGN", (0,0),(-1,-1), "TOP"), ("LEFTPADDING",(0,0),(-1,-1),9), ("RIGHTPADDING",(0,0),(-1,-1),9), ("TOPPADDING",(0,0),(-1,-1),8), ("BOTTOMPADDING",(0,0),(-1,-1),8), ("LINEBELOW",(0,0),(-1,-1),0.35, colors.HexColor("#D9E0DA"))]
        if header:
            rules += [("BACKGROUND",(0,0),(-1,0),light)]
        t.setStyle(TableStyle(rules))
        return t

    class Clock(Flowable):
        def __init__(self):
            super().__init__()
            self.width = self.height = 415

        def draw(self):
            c = self.canv
            center = 207.5
            def point(radius, deg):
                a = math.radians(deg)
                return center + radius * math.cos(a), center + radius * math.sin(a)
            for model, outer, inner in (("campbell", 195, 143), ("vogler", 124, 84)):
                stages = data["analysis"]["maps"][model]
                n = len(stages)
                for stage in stages:
                    a = 90 - (stage["id"] - 1) * 360/n - 0.65
                    b = 90 - stage["id"] * 360/n + 0.65
                    p = c.beginPath()
                    p.moveTo(*point(outer, a))
                    for j in range(1, 21):
                        p.lineTo(*point(outer, a + (b-a)*j/20))
                    p.lineTo(*point(inner, b))
                    for j in range(1,21):
                        p.lineTo(*point(inner, b+(a-b)*j/20))
                    p.close()
                    c.setFillColor(colors.HexColor(COLORS[stage["status"]]))
                    c.setStrokeColor(colors.white)
                    c.drawPath(p, fill=1, stroke=1)
                    x,y = point((inner+outer)/2, (a+b)/2)
                    c.setFillColor(colors.white if stage["status"] in {"green", "red"} else colors.HexColor("#172F28"))
                    c.setFont("YaziBold", 10)
                    c.drawCentredString(x,y-3,str(stage["id"]))
                    if stage["id"] in data["analysis"].get("current", {}).get(model, []):
                        x,y = point(outer + 5, (a+b)/2)
                        c.setFillColor(colors.HexColor("#142C24"))
                        c.circle(x,y,4.5,fill=1,stroke=0)
            c.setFillColor(green)
            c.setFont("YaziBold",12)
            c.drawCentredString(center,center+14,"ŞU AN")
            c.setFont("Yazi",9)
            current = data["analysis"].get("current", {})
            for offset, model, label in ((-5,"campbell","Campbell"),(-23,"vogler","Vogler")):
                value = ", ".join(map(str,current.get(model,[]))) or "?"
                c.drawCentredString(center, center+offset, f"{label} {value}")

    class MiniBar(Flowable):
        def __init__(self, value, maximum, status):
            super().__init__()
            self.width, self.height = available*.08-20, 10
            self.value, self.maximum, self.status = value, maximum, status

        def draw(self):
            self.canv.setFillColor(light)
            self.canv.roundRect(0,1,self.width,5,2,fill=1,stroke=0)
            if self.value:
                self.canv.setFillColor(colors.HexColor(COLORS[self.status]))
                self.canv.roundRect(0,1,self.width*self.value/self.maximum,5,2,fill=1,stroke=0)

    def footer(c, doc):
        c.saveState()
        c.setStrokeColor(gold)
        c.line(36, 31, width-36, 31)
        c.setFont("Yazi",8)
        c.setFillColor(green)
        sample = "GÖRSEL PROVA · ÖRNEK VERİ | " if data["project"].get("demo") else ""
        c.drawString(36, 18, sample + "Yazıhane · AI değerlendirmesi · " + data["metrics_sha256"][:12])
        c.drawRightString(width-36,18,f"{doc.page}")
        c.restoreState()

    doc = SimpleDocTemplate(str(path), pagesize=(width,height), leftMargin=36,rightMargin=36,topMargin=34,bottomMargin=44, title="Yazıhane Dashboard — " + data["project"].get("title", "Metin"),author="Yazıhane")
    story = []
    if data["project"].get("demo"):
        story.append(P("GÖRSEL PROVA · ÖRNEK VERİ — Bu rapor kullanıcının romanına ait değildir.", "H3Y"))
    story += [P("Yazıhane / Dashboard", "H1Y"), P(data["project"].get("title", "Paylaşılan metin"), "H2Y"), P(data["analysis"]["coverage_note"])]
    s = data["summary"]
    kpis = [(s["all_words"], "kaynak kelimesi"), (s["evaluated_chapters"], "incelenen anlatı bölümü"), (s["draft_words"], "taslak kelimesi"), (s["repetition_words"], "tekrar taraması kelimesi")]
    cells = [[P(f"{n:,}".replace(",","."), "KPIY"),P(label,"SmallY")] for n,label in kpis]
    t = table([cells],[available/4]*4,False)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),light)]))
    story += [t, Spacer(1,12)]
    left = [Clock(), P("Dış halka Campbell · 17 / İç halka Vogler · 12", "ClockY"), P("Siyah nokta: metne dayalı konum. Halkaların açıları bire bir eşleşme değildir.","SmallY")]
    right = [P("Dört bakış", "H2Y")]
    for role, title in ROLES.items():
        item = data["analysis"]["opinions"][role]
        right += [P(title+" · "+STATES[item["state"]], "H3Y"),P(item["summary"])]
    right += [P("Mevcut konum", "H3Y"), P(data["analysis"].get("current",{}).get("summary","Kanıtlı konum belirlenmedi."))]
    story.append(table([[left,right]],[445,available-445],False))
    legend = []
    for status in STATUS:
        legend.append([P(STATUS[status],"H3Y"), P({"green":"İşlev çalışıyor", "yellow":"Kanıtlı revizyon", "red":"İşlev eksik / henüz yazılmadı", "gray":"Taslak, not, ham veya okunmamış"}[status],"SmallY")])
    t = table([legend],[available/4]*4,False)
    t.setStyle(TableStyle([("LINEABOVE",(i,0),(i,0),4,colors.HexColor(COLORS[k])) for i,k in enumerate(STATUS)]))
    story += [Spacer(1,12),t, PageBreak()]
    story += [P("Kurulun ortak kararı", "H1Y"),P(data["analysis"].get("verdict","Bu raporda ortak hüküm oluşturulmadı."))]
    for i,decision in enumerate(data["analysis"].get("decisions",[]),1):
        story += [P(f'{i:02d} / {decision["label"]}',"H3Y"), P(decision["text"])] + evidence(decision.get("evidence",[]))
    if data["analysis"].get("disagreements"):
        story += [P("Ayrışmalar", "H2Y"), P(data["analysis"]["disagreements"])]
    story += [P("Bölümlere göre kelime ve durum", "H2Y")]
    rows = [[P(t,"H3Y") for t in ("Bölüm / tür", "Kelime", "Durum / değerlendirme", "Şablon bağlantıları")]]
    max_chapter_words = max(1, *(ch["word_count"] or 0 for ch in data["chapters"]))
    for ch in data["chapters"]:
        links = []
        for model,label in (("campbell","C"),("vogler","V")):
            links += [label+str(stage["id"]) for stage in data["analysis"]["maps"][model] if ch["id"] in stage["chapters"]]
        count_cell = [P("—" if ch["word_count"] is None else ch["word_count"]),MiniBar(ch["word_count"],max_chapter_words,ch["review"]["status"])]
        rows.append([P(ch["title"]+" · "+KINDS[ch["kind"]]+(" · yapısı kapalı" if ch["locked"] else "")), count_cell, [P(STATUS[ch["review"]["status"]]),P(ch["review"]["note"],"SmallY")],P(", ".join(links) or "Eşleme yok")])
    story.append(table(rows,[available*.25,available*.08,available*.49,available*.18]))
    story += [P("Okuma kapsamı ve yöntem", "H2Y"), P("Ayrı görevlerle bağımsız AI okumaları." if data["analysis"]["reading_mode"]=="independent" else "Roller aynı oturumda sırayla uygulandı; birbirinden bağımsız insan okumaları değildir."), P(data["method"]["word_count"]), P(data["method"]["scope"]),PageBreak()]
    story += [P("Sözcük ve cümle izleri", "H1Y"),P(data["method"]["repetitions"]),P(data["method"]["patterns"]),P(f'Cümle sayısı: {s["sentence_count"]} · Ortalama kelime: {s["mean_sentence_words"] if s["mean_sentence_words"] is not None else "—"} · 35+ kelimeli cümle: {s["long_sentences_35"]}',"SmallY")]
    specs = [("İçerik sözcüğü tekrar adayları", "content_words", "word"), ("Sık kelimeler · işlev kelimeleri dahil", "all_frequent_words", "word"), ("3–6 sözcüklü tekrar adayları", "phrases", "phrase"), ("Aynı cümle tekrarları · noktalama duyarsız", "sentences", "sentence"), ("Tanımlı cümle kalıpları", "patterns", "pattern")]
    for title,key,field in specs:
        story += [CondPageBreak(125),P(title,"H2Y")]
        rows = [[P("Aday / kalıp","H3Y"),P("Sayı","H3Y"),P("Yerler","H3Y")]]
        for item in data["lexical"][key]:
            rows.append([P(item[field]),P(item["count"]),P(refs(item.get("refs",[])),"SmallY")])
        if len(rows)==1:
            rows.append([P("Tanımlı eşiği aşan aday yok."),P("—"),P("—")])
        story.append(table(rows,[available*.46,available*.07,available*.47]))
    story.append(PageBreak())
    story += [P("Bütün incelemeler", "H1Y"), P("Aşağıdaki mercekler AI yorumlarıdır. Tarihî yazarların gerçek sözleri veya bir yayınevinin resmî kararı değildir.")]
    for module in data["analysis"].get("modules",[]):
        story += [KeepTogether([P(MODULES[module["id"]]+" · "+STATES[module["state"]],"H2Y"),P(module["summary"])])]
        story += evidence(module.get("evidence",[]))
        for finding in module.get("findings",[]):
            story += [P(finding["label"]+" — "+finding["text"])] + evidence(finding.get("evidence",[]))
        if module.get("sample"):
            story += [P("[ÖRNEK / İSKELE — kanon değildir]", "H3Y"), P(module["sample"]), P(module.get("technique",""),"SmallY")]
    for role,title in ROLES.items():
        if data["analysis"]["opinions"][role].get("evidence"):
            story += [P(title+" · kaynaklar","H3Y")] + evidence(data["analysis"]["opinions"][role]["evidence"])
    current = data["analysis"].get("current",{})
    if current.get("evidence"):
        story += [P("Mevcut konum · kaynak", "H3Y")] + evidence(current["evidence"])
    story.append(PageBreak())
    story += [P("Yolculukların tam dökümü", "H1Y"),P("Renk bir değerlendirme durumudur; kuramın her roman için zorunlu olduğu anlamına gelmez. Henüz yazılmadı etiketi bir hata değildir.")]
    for model,title in (("campbell","Campbell · 17 aşama"),("vogler","Vogler · 12 aşama")):
        story += [CondPageBreak(145),P(title,"H2Y")]
        rows = [[P(t,"H3Y") for t in ("Aşama / işlev", "Durum", "Metindeki karşılığı / kanıt")]]
        for stage in data["analysis"]["maps"][model]:
            details = [P(stage["note"])] + evidence(stage["evidence"])
            if stage["chapters"]:
                details.append(P("Bölümler: "+", ".join(chapters[c]["title"] for c in stage["chapters"]),"SmallY"))
            rows.append([[P(f'{stage["id"]:02d} / {stage["name"]}',"H3Y"),P(stage["function"],"SmallY")], [P(STATUS[stage["status"]]),P(ASSESS[stage["assessment"]],"SmallY")], details])
        t=table(rows,[available*.29,available*.18,available*.53])
        for idx,stage in enumerate(data["analysis"]["maps"][model],1):
            t.setStyle(TableStyle([("LINEBEFORE",(0,idx),(0,idx),4,colors.HexColor(COLORS[stage["status"]]))]))
        story.append(t)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="Output base path without extension")
    parser.add_argument("--html-only", action="store_true", help="Explicit fallback if PDF dependencies are unavailable")
    args = parser.parse_args()
    try:
        data = validate(json.loads(args.metrics.read_text(encoding="utf-8")),json.loads(args.analysis.read_text(encoding="utf-8")))
        args.output.parent.mkdir(parents=True,exist_ok=True)
        html_path, pdf_path = args.output.with_suffix(".html"), args.output.with_suffix(".pdf")
        if html_path.resolve() in {args.metrics.resolve(),args.analysis.resolve()} or pdf_path.resolve() in {args.metrics.resolve(),args.analysis.resolve()}:
            raise ValueError("Output cannot overwrite an input file.")
        write_html(data,html_path)
        if not args.html_only:
            create_pdf(data,pdf_path)
        print(json.dumps({"html":str(html_path.resolve()),"pdf":None if args.html_only else str(pdf_path.resolve()),"metrics_sha256":data["metrics_sha256"]},ensure_ascii=False))
    except (ValueError, KeyError, OSError, TypeError, ImportError) as error:
        parser.exit(2,f"Dashboard render error: {error}\n")


if __name__ == "__main__":
    main()
