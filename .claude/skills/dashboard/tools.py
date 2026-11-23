#!/usr/bin/env python3
"""Herramientas del skill /dashboard (Parcial_2).

  python3 tools.py sync <persona>   -> actualiza las tablas de checklists en Parcial_2/progreso/<persona>.md
                                       a partir de los .md de teoria/, practica/, examen/, examenes_resueltos/
                                       (conserva el estado ya guardado de cada ítem)
  python3 tools.py html <persona> <salida.html>  -> genera el HTML del tablero
"""
import re, sys, glob, os, html as H
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = os.path.join(ROOT, "Parcial_2")
REPO = "https://github.com/jcarrenol1203/estado-solido-profesor-ocasional/blob/main/Parcial_2/"
SECS = [("teoria", "Teoría", "teoria", ["pendiente", "en progreso", "hecho"]),
        ("practica", "Práctica", "practica", ["pendiente", "en progreso", "hecho"]),
        ("examen", "Examen", "examen", ["pendiente", "entregado", "calificado"]),
        ("viejos", "Exámenes viejos", "examenes_resueltos", ["pendiente", "en progreso", "hecho"])]
VN = {"V.P2501": "P-2025-01 (Parcial)", "V.P252S": "P-2025-2S (Parcial)", "V.T25II": "T-2025-II (Taller)", "V.TSS20": "T-SS2020 (Taller)", "V.P261S": "P-2026-1S (solo #11)"}
STATES = "pendiente|en progreso|hecho|entregado|calificado"
ITEM = re.compile(r"^- \[ \] (\S+) (.*)$", re.M)

def items(sec):
    _, _, d, _ = next(s for s in SECS if s[0] == sec)
    out = []
    for f in sorted(glob.glob(f"{BASE}/{d}/*.md")):
        for i, t in ITEM.findall(open(f).read()):
            out.append(dict(id=i, text=t.strip(), file=f"{d}/{os.path.basename(f)}"))
    return out

def group(sec, it):
    p = it["id"].split(".")
    if sec in ("teoria", "practica"): return ".".join(p[1:3]) if len(p) >= 4 else p[1]
    if sec == "examen": return "Teoría" if p[1] == "T" else "Ejercicios"
    return p[0] + "." + p[1]

def pts(text):
    m = re.search(r"— ([\d.]+)\s*$", text); return float(m.group(1)) if m else None

def read_state(md):
    st = {}
    for l in md.split("\n"):
        m = re.match(rf"^\| (\S+) \| .* \| ({STATES}) \| ([^|]*) \|$", l)
        if m: st[m.group(1)] = (m.group(2), m.group(3).strip())
    return st

def sync(persona):
    p = f"{BASE}/progreso/{persona}.md"; md = open(p).read(); st = read_state(md)
    blk = ["<!-- CHECKLISTS:START -->", "## Seguimiento de checklists", "",
           "Generado por `.claude/skills/dashboard/tools.py sync`; cambia solo las columnas Estado y Nota (el texto sale de los `.md` de contenido).",
           "Estados: teoría/práctica/viejos `pendiente | en progreso | hecho`; examen `pendiente | entregado | calificado` (Nota = `obtenido/máximo`).", ""]
    for key, name, d, _ in SECS:
        its = items(key); blk += [f"### {name} ({len(its)} ítems)", "", "| ID | Ítem | Estado | Nota |", "|---|---|---|---|"]
        for it in its:
            s, n = st.get(it["id"], ("pendiente", "—"))
            blk.append(f"| {it['id']} | {it['text'].replace('|', '/')} | {s} | {n or '—'} |")
        blk.append("")
    blk.append("<!-- CHECKLISTS:END -->")
    new = "\n".join(blk)
    if "<!-- CHECKLISTS:START -->" in md:
        md = re.sub(r"<!-- CHECKLISTS:START -->.*<!-- CHECKLISTS:END -->", lambda m: new, md, flags=re.S)
    else:
        md = md.replace("## Parciales y talleres", new + "\n\n## Parciales y talleres", 1)
    open(p, "w").write(md); print("sync", persona, {k: len(items(k)) for k, *_ in SECS})

def subtemas(md):
    out = []
    for l in md.split("\n"):
        m = re.match(r"^\| ((?:metal|gas1d|interac|drude|cal|fermi3d|extra|vib|trans|term|falla)\.\d) \| (.*?) \| \S+ \| (no visto|en progreso|dominado|fuera de alcance) \| (.*?) \|$", l)
        if m: out.append(m.groups())
    return out

def html(persona, outp):
    md = open(f"{BASE}/progreso/{persona}.md").read(); st = read_state(md)
    name = persona.capitalize(); data = {}
    for key, label, d, states in SECS:
        its = items(key); done = "calificado" if key == "examen" else "hecho"
        for it in its: it["state"], it["note"] = st.get(it["id"], ("pendiente", "—")); it["pts"] = pts(it["text"]); it["group"] = group(key, it)
        data[key] = (label, its, done)
    sub = {s[0]: s for s in subtemas(md)}
    inscope = [s for s in sub.values() if s[2] != "fuera de alcance"]
    dom = [s for s in inscope if s[2] == "dominado"]
    def pct(key):
        l, its, done = data[key]; return 100 * sum(1 for i in its if i["state"] == done) / max(1, len(its))
    def link(i): return REPO + i["file"]
    css = """
:root{--bg:#f5f7fb;--panel:#fff;--fg:#14213d;--mut:#5b6785;--line:#dbe1ee;--acc:#1f4fd8;--accbg:#e6edff;--ok:#1b7a3d;--okbg:#e2f4e8;--wip:#a15c00;--wipbg:#fff0d6;--off:#7a8399;--offbg:#eceff5}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1524;--panel:#171f33;--fg:#e8ecf7;--mut:#9aa6c4;--line:#2a3554;--acc:#7da2ff;--accbg:#1e2b52;--ok:#5fd187;--okbg:#17321f;--wip:#ffbe55;--wipbg:#3a2a0c;--off:#8e98b3;--offbg:#222b44;color-scheme:dark}}
:root[data-theme=dark]{--bg:#0f1524;--panel:#171f33;--fg:#e8ecf7;--mut:#9aa6c4;--line:#2a3554;--acc:#7da2ff;--accbg:#1e2b52;--ok:#5fd187;--okbg:#17321f;--wip:#ffbe55;--wipbg:#3a2a0c;--off:#8e98b3;--offbg:#222b44;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:Inter,system-ui,sans-serif;line-height:1.5;padding-block:20px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.w{max-width:980px;margin:0 auto}h1{font-family:'Space Grotesk',Inter,sans-serif;font-size:1.7rem;margin:0 0 4px;text-wrap:balance}h2{font-family:'Space Grotesk',Inter,sans-serif;font-size:1.1rem;margin:22px 0 8px}
.sub{color:var(--mut);margin:0 0 16px}.kp{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.k{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px;min-width:0}.k b{display:block;font-size:1.5rem;font-variant-numeric:tabular-nums}.k span{color:var(--mut);font-size:.85rem}
.bar{height:8px;background:var(--offbg);border-radius:4px;margin-top:8px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc);border-radius:4px}
.tabs{display:flex;flex-wrap:wrap;gap:6px;margin:20px 0 8px}.tabs button{font:inherit;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:7px 12px;cursor:pointer}
.tabs button[aria-selected=true]{background:var(--acc);color:var(--bg);border-color:var(--acc)}button:focus-visible,a:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.g{background:var(--panel);border:1px solid var(--line);border-radius:8px;margin:10px 0;overflow:hidden}.g h3{margin:0;padding:10px 12px;font-size:.95rem;display:flex;gap:8px;flex-wrap:wrap;align-items:center;border-bottom:1px solid var(--line)}
.row{display:grid;grid-template-columns:1fr auto;gap:8px;padding:8px 12px;border-top:1px solid var(--line);align-items:start}.row:first-of-type{border-top:0}.row>div{min-width:0;overflow-wrap:anywhere}
.id{font-size:.75rem;color:var(--mut);font-family:ui-monospace,monospace}.pill{font-size:.75rem;padding:2px 8px;border-radius:99px;white-space:nowrap;background:var(--offbg);color:var(--off)}
.pill.ok{background:var(--okbg);color:var(--ok)}.pill.wip{background:var(--wipbg);color:var(--wip)}.pill.acc{background:var(--accbg);color:var(--acc)}
a{color:var(--acc)}.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%}td,th{border-top:1px solid var(--line);padding:6px 10px;text-align:left;font-size:.9rem}
.na{opacity:.65}
"""
    def pill(s):
        c = {"hecho": "ok", "calificado": "ok", "dominado": "ok", "en progreso": "wip", "entregado": "wip"}.get(s, "")
        return f'<span class="pill {c}">{H.escape(s)}</span>'
    body = [f'<div class="w"><h1>Progreso P2 de {name}</h1><p class="sub">Alcance: diapositivas 1-70 de Metales 2021 (+ Pavlov). Fuente: progreso/{persona}.md</p>']
    body.append('<div class="kp">')
    body.append(f'<div class="k"><b>{len(dom)}/{len(inscope)}</b><span>subtemas dominados (en alcance)</span><div class="bar"><i style="width:{100*len(dom)/max(1,len(inscope)):.0f}%"></i></div></div>')
    for key, label, d, _ in SECS:
        l, its, done = data[key]; n = sum(1 for i in its if i["state"] == done)
        body.append(f'<div class="k"><b>{n}/{len(its)}</b><span>{label}</span><div class="bar"><i style="width:{pct(key):.0f}%"></i></div></div>')
    body.append('</div>')
    ex = data["examen"][1]; got = sum(float(re.match(r"([\d.]+)/", i["note"]).group(1)) for i in ex if i["state"] == "calificado" and re.match(r"([\d.]+)/", i["note"]))
    body.append(f'<p class="sub" style="margin-top:12px">Nota acumulada del examen propuesto: <b>{got:.1f}</b> de 10.0 (solo ítems calificados).</p>')
    body.append('<div class="tabs" role="tablist">' + "".join(f'<button role="tab" id="t-{k}" aria-selected="{"true" if n == 0 else "false"}" data-t="{k}">{l}</button>' for n, (k, l, *_ ) in enumerate(SECS)) + '<button role="tab" id="t-sub" aria-selected="false" data-t="sub">Subtemas y parciales</button></div>')
    for n, (key, label, d, _) in enumerate(SECS):
        l, its, done = data[key]; body.append(f'<section id="p-{key}"{"" if n == 0 else " hidden"}>')
        groups = {}
        for i in its: groups.setdefault(i["group"], []).append(i)
        for g, gi in groups.items():
            s = sub.get(g); title = f"{g} · {re.sub(r'[$]', '', s[1])}" if s else VN.get(g, g)
            nd = sum(1 for i in gi if i["state"] == done)
            off = ' na' if s and s[2] == "fuera de alcance" else ''
            body.append(f'<div class="g{off}"><h3>{H.escape(title)} <span class="pill acc">{nd}/{len(gi)}</span></h3>')
            for i in gi:
                t = H.escape(i["text"].replace("$", ""))
                nt = f' · {H.escape(i["note"])}' if i["note"] not in ("—", "") else ""
                body.append(f'<div class="row"><div><span class="id">{i["id"]}</span><br>{t} · <a href="{link(i)}" target="_blank" rel="noopener">abrir</a></div><div>{pill(i["state"])}<span class="id">{nt}</span></div></div>')
            body.append('</div>')
        body.append('</section>')
    body.append('<section id="p-sub" hidden><h2>Subtemas (alcance 1-70 y fuera del parcial)</h2><div class="scroll"><table><tr><th>ID</th><th>Subtema</th><th>Estado</th><th>Última evaluación</th></tr>')
    for s in sub.values():
        body.append(f'<tr class="{"na" if s[2]=="fuera de alcance" else ""}"><td>{s[0]}</td><td>{H.escape(re.sub(r"[$]", "", s[1]))}</td><td>{pill(s[2]) if s[2]!="fuera de alcance" else "<span class=pill>fuera del parcial (p. &gt;70)</span>"}</td><td>{H.escape(s[3])}</td></tr>')
    body.append('</table></div><h2>Parciales y talleres (banco de exámenes viejos)</h2><div class="scroll"><table><tr><th>ID</th><th>Tipo</th><th>Estado</th><th>Nota</th><th>Fecha</th></tr>')
    in_tab = False
    for l in md.split("\n"):
        m = re.match(r"^\| ((?:P|T)-\S+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", l)
        if m: body.append("<tr>" + "".join(f"<td>{H.escape(x)}</td>" for x in m.groups()) + "</tr>")
    body.append('</table></div></section>')
    body.append("""</div><script>
document.querySelectorAll('.tabs button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.tabs button').forEach(function(x){x.setAttribute('aria-selected',x===b?'true':'false')});document.querySelectorAll('section[id^=p-]').forEach(function(s){s.hidden=s.id!=='p-'+b.dataset.t})})});
</script>""")
    head = f'<title>Progreso P2 de {name}</title><meta name="claude:viewport-fit-sides" content="cover"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Space+Grotesk:wght@600&display=swap"><style>{css}</style>'
    open(outp, "w").write(head + "\n" + "\n".join(body)); print("html", outp, len("\n".join(body)))

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "sync": sync(a[1])
    elif a[0] == "html": html(a[1], a[2])
