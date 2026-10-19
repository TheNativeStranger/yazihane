#!/usr/bin/env python3
"""Local, deterministic manuscript measurements. No network or source edits."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import statistics
import unicodedata
import xml.etree.ElementTree as ET
from zipfile import ZipFile

WORD = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*", re.UNICODE)
STOP = set("ve veya ile de da ki bu şu o bir için gibi kadar daha çok az en ne mi mı mu mü ama fakat ancak ise hem her hiç bazı diye çünkü sonra önce yine artık bile ben sen biz siz onlar onun bunu şunu onu benim senin kendi başka var yok olan olarak oldu olmak olur değil dedi diye böyle şöyle sadece yalnız üzere içinde üzerine arasında doğru karşı göre bütün tüm aynı birkaç nasıl neden zaman şey şimdi kadar böyle şöyle beri rağmen".split())
KINDS = {"prose", "draft", "note", "raw", "missing"}
PATTERNS = {
    "sanki ... gibi": re.compile(r"\bsanki\b.*?\bgibi\b"),
    "hem ... hem ...": re.compile(r"\bhem\b.*?\bhem\b"),
    "ne ... ne ...": re.compile(r"\bne\b.*?\bne\b"),
    "öyle ... ki": re.compile(r"\böyle\b.*?\bki\b"),
    "bir yandan ... öte/diğer yandan": re.compile(r"\bbir yandan\b.*?\b(?:öte|diğer) yandan\b"),
}
ABBREVIATIONS = re.compile(r"\b(?:Dr|Prof|Doç|Sn|Hz|vb|vs|No|sf|s)\.", re.I)


def normalize(text):
    return unicodedata.normalize("NFC", text).translate(str.maketrans({"I": "ı", "İ": "i", "’": "'"})).casefold()


def words(text):
    return [normalize(m.group()) for m in WORD.finditer(text)]


def sentences(text):
    # Protect common abbreviations and decimal points; retain the source text.
    protected = ABBREVIATIONS.sub(lambda m: m.group().replace(".", "\uFFF0"), text)
    protected = re.sub(r"(?<=\d)\.(?=\d)", "\uFFF0", protected)
    parts = re.split(r"(?<=[.!?…])\s+|(?<=[.!?…][\"”’'])\s+", protected)
    return [p.replace("\uFFF0", ".").strip() for p in parts if words(p)]


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extract(path):
    path = Path(path)
    suffix = path.suffix.lower()
    blocks = []
    if suffix == ".docx":
        w = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        with ZipFile(path) as z:
            tree = ET.fromstring(z.read("word/document.xml"))
            style_names = {}
            if "word/styles.xml" in z.namelist():
                for s in ET.fromstring(z.read("word/styles.xml")).iter(w + "style"):
                    name = s.find(w + "name")
                    if name is not None:
                        style_names[s.get(w + "styleId")] = name.get(w + "val", "")
            body = tree.find(w + "body")
            for p in body.iter(w + "p"):
                text = "".join((e.text or "") if e.tag == w + "t" else "\t" if e.tag == w + "tab" else "\n" if e.tag == w + "br" else "" for e in p.iter()).strip()
                style = p.find(w + "pPr/" + w + "pStyle")
                sid = style.get(w + "val", "") if style is not None else ""
                name = normalize(style_names.get(sid, sid))
                if text:
                    blocks.append((text, name.startswith(("heading", "başlık", "title", "subtitle"))))
    elif suffix in {".txt", ".md"}:
        source_text = path.read_text(encoding="utf-8-sig")
        if suffix == ".md":
            source_text = re.sub(r"(?m)^(#{1,6}\s+[^\n]+)$", r"\n\n\1\n\n", source_text)
        for text in re.split(r"\n\s*\n", source_text):
            text = text.strip()
            if text:
                blocks.append((text, bool(re.match(r"^#{1,6}\s", text))))
    elif suffix == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(path)
        for page in reader.pages:
            text = page.extract_text() or ""
            if not text.strip():
                raise ValueError("PDF has an unreadable/empty page; use verified OCR or a text source before counting.")
            blocks.extend((p.strip(), False) for p in re.split(r"\n\s*\n", text) if p.strip())
    else:
        raise ValueError("Use DOCX, UTF-8 TXT/MD, or a readable text PDF; convert other formats first.")
    paragraphs, number = [], 0
    for block, (text, heading) in enumerate(blocks, 1):
        if not heading:
            number += 1
        paragraphs.append({"block": block, "number": None if heading else number, "heading": heading, "text": text})
    return {"source": str(path.resolve()), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "paragraphs": paragraphs,
            "note": "PDF paragraph boundaries are extracted text blocks, not guaranteed visual paragraphs." if suffix == ".pdf" else "Headings are excluded from paragraph numbering and word counts."}


def load_chapters(manifest, root):
    result, ids, sources = [], set(), {}
    for item in manifest.get("chapters", []):
        cid = str(item["id"])
        if not cid or cid in ids:
            raise ValueError("Chapter IDs must be non-empty and unique.")
        ids.add(cid)
        kind = item.get("kind", "raw")
        if kind not in KINDS:
            raise ValueError(f"Unknown chapter kind: {kind}")
        if kind == "missing":
            if item.get("source") or item.get("paragraphs"):
                raise ValueError("A missing chapter cannot also contain source text.")
            paragraphs, fingerprint = [], None
        elif "paragraphs" in item:
            paragraphs = [{"number": p.get("number", j), "text": p["text"]} if isinstance(p, dict) else {"number": j, "text": p} for j, p in enumerate(item["paragraphs"], 1)]
            fingerprint = hashlib.sha256(json.dumps(paragraphs, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        elif item.get("source"):
            path = (root / item["source"]).resolve()
            if path not in sources:
                sources[path] = extract(path)
            source = sources[path]
            start, end = item.get("start", 1), item.get("end", float("inf"))
            omit = set(item.get("omit", []))
            paragraphs = [{"number": p["number"], "text": p["text"]} for p in source["paragraphs"] if not p["heading"] and start <= p["number"] <= end and p["number"] not in omit]
            fingerprint = source["sha256"]
        else:
            raise ValueError(f"No source text for {cid}; mark it missing explicitly instead of inventing text.")
        numbers = [p["number"] for p in paragraphs]
        if any(not isinstance(n, int) or n < 1 for n in numbers) or len(numbers) != len(set(numbers)):
            raise ValueError(f"Invalid paragraph IDs in {cid}")
        if any(not isinstance(p["text"], str) for p in paragraphs):
            raise ValueError(f"Paragraph text must be a string in {cid}")
        if kind != "missing" and not any(p["text"].strip() for p in paragraphs):
            raise ValueError(f"Empty source range for {cid}")
        result.append({"id": cid, "title": item.get("title", cid), "kind": kind, "evaluated": bool(item.get("evaluated", kind == "prose")),
                       "locked": bool(item.get("locked", False)), "source": item.get("source", "paylaşılan metin"), "source_sha256": fingerprint, "paragraphs": paragraphs})
    if not result:
        raise ValueError("At least one chapter or explicit missing chapter is required.")
    return result


def analyze(manifest, root):
    chapters = load_chapters(manifest, root)
    include_drafts = bool(manifest.get("include_drafts_in_repetitions", False))
    excluded = STOP | {normalize(s) for s in manifest.get("ignore_words", [])}
    counts, word_refs, phrase_counts, phrase_refs = Counter(), defaultdict(list), Counter(), defaultdict(list)
    sentence_counts, sentence_refs, sentence_examples = Counter(), defaultdict(list), {}
    pattern_counts, pattern_refs = Counter(), defaultdict(list)
    lengths, selected_count = [], 0
    for chapter in chapters:
        chapter["word_count"] = None if chapter["kind"] == "missing" else sum(len(words(p["text"])) for p in chapter["paragraphs"])
        chapter["paragraph_count"] = len(chapter["paragraphs"])
        chapter["dialogue_paragraphs"] = sum(bool(re.match(r"^[\-—–“\"]", p["text"].lstrip())) for p in chapter["paragraphs"])
        selected = chapter["evaluated"] and (chapter["kind"] == "prose" or include_drafts and chapter["kind"] == "draft")
        chapter["in_repetition_scope"] = selected
        if not selected:
            continue
        for p in chapter["paragraphs"]:
            tokens = words(p["text"])
            selected_count += len(tokens)
            ref = {"chapter": chapter["id"], "paragraph": p["number"]}
            for token in tokens:
                counts[token] += 1
                if len(word_refs[token]) < 30:
                    word_refs[token].append(ref)
            for n in range(3, 7):
                for i in range(len(tokens) - n + 1):
                    key = tuple(tokens[i:i+n])
                    if all(w in excluded for w in key):
                        continue
                    phrase_counts[key] += 1
                    if len(phrase_refs[key]) < 30:
                        phrase_refs[key].append(dict(ref, token=i+1))
            for sentence in sentences(p["text"]):
                sw = words(sentence)
                lengths.append(len(sw))
                key = " ".join(sw)
                if len(sw) >= 6:
                    sentence_counts[key] += 1
                    sentence_examples.setdefault(key, sentence)
                    if len(sentence_refs[key]) < 30:
                        sentence_refs[key].append(ref)
                for label, regex in PATTERNS.items():
                    if regex.search(normalize(sentence)):
                        pattern_counts[label] += 1
                        if len(pattern_refs[label]) < 20:
                            pattern_refs[label].append(dict(ref, example=sentence))
    content_words = [{"word": w, "count": n, "per_1000": round(n * 1000 / selected_count, 2) if selected_count else 0, "refs": word_refs[w]} for w, n in counts.most_common() if len(w) >= 3 and w not in excluded and n >= 3][:30]
    candidates = sorted(((key, n) for key, n in phrase_counts.items() if n >= 3), key=lambda row: (-row[1] * len(row[0]), -len(row[0]), row[0]))[:400]
    phrases = []
    for key, n in candidates:
        nested = any(n == old["count"] and any(tuple(old["words"])[j:j+len(key)] == key for j in range(len(old["words"])-len(key)+1)) for old in phrases)
        if not nested:
            phrases.append({"phrase": " ".join(key), "words": list(key), "count": n, "refs": phrase_refs[key]})
        if len(phrases) == 25:
            break
    totals = {kind: sum(c["word_count"] or 0 for c in chapters if c["kind"] == kind) for kind in KINDS}
    result = {"schema_version": 1, "project": manifest.get("project", {}), "chapters": chapters,
            "measurement_config": {"ignore_words": sorted(excluded), "include_drafts": include_drafts},
            "summary": {"all_words": sum(totals.values()), "prose_words": totals["prose"], "draft_words": totals["draft"], "note_words": totals["note"] + totals["raw"],
                        "chapter_count": len(chapters), "evaluated_chapters": sum(c["evaluated"] and c["kind"] == "prose" for c in chapters), "repetition_words": selected_count,
                        "sentence_count": len(lengths), "mean_sentence_words": round(statistics.mean(lengths), 1) if lengths else None, "long_sentences_35": sum(n >= 35 for n in lengths)},
            "lexical": {"content_words": content_words, "all_frequent_words": [{"word":w,"count":n} for w,n in counts.most_common(20)], "phrases": phrases,
                        "sentences": [{"sentence": sentence_examples[s], "count": n, "refs": sentence_refs[s]} for s, n in sentence_counts.most_common() if n >= 2][:20],
                        "patterns": [{"pattern": p,"count":n,"refs":pattern_refs[p]} for p,n in pattern_counts.most_common()]},
            "method": {"word_count": "Unicode harf/sayı dizileri sayılır; iç kesme ve tire korunur. Başlıklar ve açıkça dışlanan paragraflar sayılmaz.",
                       "repetitions": "Türkçe I/İ dönüşümü; yüzey biçimi. Kök/ek çözümlemesi yapılmaz. İçerik sözcüğü >=3, 3-6 sözcüklü kalıp >=3, >=6 sözcüklü aynı cümle >=2 tekrar. Sayılar sorun kararı değildir.",
                       "scope": "Değerlendirilen düzyazı" + (" ve açıkça dahil edilen taslaklar" if include_drafts else "; taslak/not/ham metin hariç"),
                       "patterns": "Tanımlı bağlaç kalıpları cümle başına bir kez sayılır. Paragraf/cümle bölme otomatik bir yaklaşımdır; dil bilgisel analiz değildir."}}
    result["metrics_sha256"] = hashlib.sha256(json.dumps(result, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("extract", "analyze"):
        p = sub.add_parser(command)
        p.add_argument("input", type=Path)
        p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "extract":
            result = extract(args.input)
        else:
            result = analyze(json.loads(args.input.read_text(encoding="utf-8")), args.input.resolve().parent)
        dump(args.output, result)
        print(json.dumps({"output": str(args.output.resolve()), "metrics_sha256": result.get("metrics_sha256"), "summary": result.get("summary")}, ensure_ascii=False))
    except (ValueError, KeyError, OSError, ET.ParseError) as error:
        parser.exit(2, f"Dashboard measurement error: {error}\n")


if __name__ == "__main__":
    main()
