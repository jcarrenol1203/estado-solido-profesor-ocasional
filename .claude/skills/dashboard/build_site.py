#!/usr/bin/env python3
"""Genera el sitio del dashboard de Parcial_2 (todo el contenido dentro del artifact).

  python3 build_site.py <salida_dir>

Crea <salida_dir>/dash_juan.html, dash_isa.html y copia los .md/imagenes (rutas relativas).
Luego se publica cada HTML con la herramienta Artifact usando `files` = lista de _files.txt.
"""
import sys, os, re, json, glob, shutil
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = os.path.join(ROOT, "Parcial_2")
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
SECT = [("teoria", "Teoría", "teoria", "teoria/"), ("practica", "Práctica", "practica", ""),
        ("viejos", "Exámenes viejos", "examenes_resueltos", "")]
files = []
tabs = []
for k, label, d, base in SECT:
    fl = []
    for f in sorted(glob.glob(f"{BASE}/{d}/*.md")):
        rel = f"{d}/{os.path.basename(f)}"; os.makedirs(os.path.join(out, d), exist_ok=True)
        shutil.copy(f, os.path.join(out, rel)); files.append(rel); fl.append(dict(path=rel, base=base))
    tabs.append(dict(k=k, label=label, files=fl))
os.makedirs(os.path.join(out, "teoria/img"), exist_ok=True)
for im in sorted(glob.glob(f"{BASE}/teoria/img/*.jpg")):
    shutil.copy(im, os.path.join(out, "teoria/img", os.path.basename(im))); files.append("teoria/img/" + os.path.basename(im))
# examen: parte 1 opción múltiple, parte 2 problemas con literales
exam = []
txt = open(f"{BASE}/examen/examen_opcion_multiple.md").read()
for m in re.finditer(r"^\*\*(EX\.M\.\d+) \(([\d.]+)\) — (.*?)\.\*\* \((.*?)\) (.*?)\n+((?:- [a-e]\. .*\n?)+)", txt, re.M):
    qid, pts, title, sub, stem, ops = m.groups()
    opts = [o[3:].strip() for o in ops.strip().split("\n")]
    exam.append(dict(id=qid, part="M", type="mc", pts=float(pts), title=title, intro=stem.strip(), opts=opts,
                     lits=[dict(id=qid, lab="", text="", pts=float(pts))]))
n_lit = sum(len(q["lits"]) for q in exam)
print("examen:", len(exam), "preguntas,", n_lit, "literales")
tabs.insert(2, dict(k="examen", label="Examen", files=[]))
tabs.append(dict(k="pendientes", label="Pendientes", files=[]))

def pend(person):
    md = open(f"{BASE}/progreso/{person}.md").read()
    m = re.search(r"<!-- PENDIENTES:START -->(.*?)<!-- PENDIENTES:END -->", md, re.S)
    rows = []
    for l in (m.group(1) if m else "").split("\n"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 6 and c[0].isdigit(): rows.append(dict(n=c[0], fecha=c[1], sub=c[2], tipo=c[3], desc=c[4], est=c[5]))
    return rows

tpl = open(os.path.join(os.path.dirname(__file__), "site_template.html")).read()
for person in ("juan", "isa"):
    cfg = dict(person=person, tabs=tabs)
    h = tpl.replace("@@NAME@@", person.capitalize()).replace("@@CFG@@", json.dumps(cfg, ensure_ascii=False)).replace("@@EXAM@@", json.dumps(exam, ensure_ascii=False)).replace("@@PEND@@", json.dumps(pend(person), ensure_ascii=False))
    open(os.path.join(out, f"dash_{person}.html"), "w").write(h)
open(os.path.join(out, "_files.txt"), "w").write("\n".join(files))
json.dump(exam, open(os.path.join(out, "_exam.json"), "w"), ensure_ascii=False, indent=1)
print(len(files), "archivos de apoyo")
