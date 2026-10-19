"""Regression checks for source scope, evidence and generated HTML behavior."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import sys

SKILL=Path(os.environ.get("YAZIHANE_DASHBOARD_ROOT",Path(__file__).resolve().parents[1]/"skills/dashboard"))
sys.path.insert(0,str(SKILL/"scripts"))
import analyze
import render
from dashboard_fixture import fixture


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.manifest,self.metrics,self.analysis=fixture(analyze)

    def rejected(self,change,pattern):
        a=copy.deepcopy(self.analysis);change(a)
        with self.assertRaisesRegex(ValueError,pattern):render.validate(self.metrics,a)

    def test_counting_and_turkish_case(self):
        self.assertEqual(analyze.words("IŞIK İZMİR Ankara'nın kırk-bir 42"),["ışık","izmir","ankara'nın","kırk-bir","42"])
        m=analyze.analyze({"chapters":[{"id":"a","kind":"prose","paragraphs":["Ali eve geldi. Ali eve geldi. Ali eve geldi."]},{"id":"d","kind":"draft","paragraphs":["Taslak iki kelime."]},{"id":"n","kind":"note","paragraphs":["Not burası."]},{"id":"x","kind":"missing"}]},Path("."))
        self.assertEqual(m["summary"]["all_words"],14)
        self.assertEqual(m["summary"]["repetition_words"],9)
        self.assertEqual(m["lexical"]["content_words"][0]["count"],3)
        self.assertEqual(m["chapters"][-1]["word_count"],None)

    def test_source_heading_and_sentence_heuristic(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"source.md";p.write_text("# Bölüm 1\nAli geldi.\n\n# Bölüm 2\nAyşe gitti.",encoding="utf8")
            extracted=analyze.extract(p)
            self.assertEqual([b["text"] for b in extracted["paragraphs"] if not b["heading"]],["Ali geldi.","Ayşe gitti."])
            self.assertEqual([b["number"] for b in extracted["paragraphs"] if not b["heading"]],[1,2])
        self.assertEqual(analyze.sentences('Dr. Ali 3.5 yazdı. “Gel.” Sonra gitti.'),['Dr. Ali 3.5 yazdı.','“Gel.”','Sonra gitti.'])

    def test_counts_are_fixture_ground_truth(self):
        self.assertEqual([c["word_count"] for c in self.metrics["chapters"]],[76,66,59,34,18,13,None])
        self.assertEqual(self.metrics["summary"]["repetition_words"],235)
        sentence=self.metrics["lexical"]["sentences"][0]
        self.assertEqual(sentence["count"],3)
        self.assertEqual(sentence["sentence"],"Sanki sokak susmuş gibi geldi ona.")

    def test_complete_workflow_and_source_text_not_embedded(self):
        data=render.validate(self.metrics,self.analysis)
        self.assertEqual(len(data["analysis"]["modules"]),13)
        self.assertEqual([len(data["analysis"]["maps"][m]) for m in ("campbell","vogler")],[17,12])
        self.assertNotIn("paragraphs",data["chapters"][0])
        self.assertEqual(data["analysis"]["current"]["campbell"],[4])
        self.assertEqual(data["analysis"]["maps"]["campbell"][-1]["status"],"gray")
        self.assertEqual(data["chapters"][4]["review"]["status"],"gray")

    def test_evidence_and_stale_metrics_rejected(self):
        self.rejected(lambda a:a.update(metrics_sha256="stale"),"different text")
        self.rejected(lambda a:a["current"]["evidence"][0].update(quote="Metinde bulunmayan cümle"),"Quote not found")
        self.rejected(lambda a:a["maps"]["campbell"][0].update(chapters=[]),"Draft/note/unread")

    def test_draft_not_current_or_green(self):
        self.rejected(lambda a:a["current"].update(chapter="b5",campbell=[5],evidence=[{"chapter":"b5","paragraph":1,"quote":"Evde ne bulacağını henüz bilmiyorum."}]),"evaluated prose")
        self.rejected(lambda a:a["chapter_reviews"].append({"chapter":"b5","status":"yellow","note":"x","evidence":[]}),"must be gray")
        self.rejected(lambda a:a["current"].update(campbell=[6]),"Current position must link")

    def test_full_board_and_decision_limits(self):
        self.rejected(lambda a:a["modules"].pop(),"all 13")
        self.rejected(lambda a:a["decisions"].extend([a["decisions"][0]]*2),"at most three")
        self.rejected(lambda a:a["maps"]["campbell"][0].update(status="red"),"contradict")

    def test_unread_comments_and_changed_metrics_rejected(self):
        ref={"chapter":"b5","paragraph":1,"quote":"Evde ne bulacağını henüz bilmiyorum."}
        self.rejected(lambda a:a["decisions"][0].update(evidence=[ref]),"outside the evaluated scope")
        self.rejected(lambda a:a["opinions"]["yayinevi"].update(evidence=[ref]),"outside the evaluated scope")
        self.rejected(lambda a:a["modules"][0]["findings"][0].update(evidence=[ref]),"outside the evaluated scope")
        self.rejected(lambda a:a["maps"]["campbell"][4].update(status="red",assessment="missing"),"missing-function judgment")
        self.rejected(lambda a:a["maps"]["campbell"][4].update(status="red",assessment="not_written"),"existing drafts stay gray")
        metrics=copy.deepcopy(self.metrics);metrics["summary"]["all_words"]+=1
        with self.assertRaisesRegex(ValueError,"Metrics content changed"):render.validate(metrics,self.analysis)

    def test_html_escaping_and_javascript(self):
        data=render.validate(self.metrics,self.analysis)
        data["project"]["title"]='</script><img src=x onerror=alert(1)>'
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/"report.html";render.write_html(data,p);s=p.read_text()
            self.assertNotIn(data["project"]["title"],s)
            self.assertEqual(s.count("</script>"),2)
            self.assertNotIn("Tahta masada annesinden kalan defter dururdu",s)
            scripts=re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>",s,re.S)
            js=Path(directory)/"report.js";js.write_text(scripts[-1])
            subprocess.run(["node","--check",str(js)],check=True,capture_output=True)
            # Exercise the actual interaction code with a small DOM adapter.
            harness=Path(directory)/"ui.cjs"
            harness.write_text('''const fs=require('fs'),vm=require('vm'),assert=require('assert');
class Element {constructor(tag){this.tag=tag;this.children=[];this.listeners={};this.style={};this.dataset={};this.value='';}append(...x){this.children.push(...x);}replaceChildren(...x){this.children=x;}setAttribute(k,v){this[k]=v;}addEventListener(k,v){this.listeners[k]=v;}scrollIntoView(){}}
const ids=new Map();const get=id=>{if(!ids.has(id))ids.set(id,new Element('div'));return ids.get(id);};
get('dashboard-data').textContent=fs.readFileSync(process.argv[2],'utf8');
const context={document:{getElementById:get,createElement:t=>new Element(t),createElementNS:(n,t)=>new Element(t),createTextNode:t=>({textContent:t}),querySelectorAll:()=>[]},window:{addEventListener(){},print(){}},Intl,console};
vm.createContext(context);vm.runInContext(fs.readFileSync(process.argv[3],'utf8'),context);
assert.equal(get('clock').children.filter(x=>x.tag==='g').length,29);
assert.equal(get('modules').children.length,13);
get('chapter').listeners.change({target:{value:'b4'}});
const groups=get('clock').children.filter(x=>x.tag==='g');assert.equal(groups.filter(x=>x.opacity==='1').length,2);
get('status').listeners.change({target:{value:'red'}});assert.equal(get('chapters').children.length,1);
get('chapter').listeners.change({target:{value:''}});
const redGroups=get('clock').children.filter(x=>x.tag==='g'&&x.opacity==='1');assert.equal(redGroups.length,2);
redGroups[0].listeners.click();assert(get('stage').children.length>3);
console.log('UI: 29 clock segments; chapter and status filters; 13 review cards; evidence detail passed.');
''')
            payload=Path(directory)/"data.json";payload.write_text(json.dumps(data,ensure_ascii=False))
            result=subprocess.run(["node",str(harness),str(payload),str(js)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn("passed",result.stdout)


if __name__=="__main__":unittest.main()
