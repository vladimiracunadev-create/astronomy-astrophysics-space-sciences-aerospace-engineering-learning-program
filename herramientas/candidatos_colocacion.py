import json, os, re, sys, unicodedata
os.chdir(r"C:\dev\astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program")
rows = [json.loads(l) for l in open("catalogo/clases.jsonl", encoding="utf8")]


def tok(s):
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
    return {w[:6] for w in re.findall(r"[a-z]{4,}", s)} - {"sistem", "diseno", "analis", "modelo", "avanza", "profes", "aplica", "caso", "practi"}


ruta = sys.argv[1]
tronco = [(r["id"], r["titulo"], tok(r["titulo"])) for r in rows if r["tipo"] == "tronco_comun"]
for r in rows:
    if r.get("ruta_id") != ruta or r["numero_clase"] % 2 == 0:
        continue
    t = tok(r["titulo"])
    sc = sorted(((len(t & c[2]) / max(1, len(t | c[2])), c[0], c[1]) for c in tronco), reverse=True)[:3]
    cand = "; ".join(f"{i}:{ti[:34]}({s:.2f})" for s, i, ti in sc if s > 0.12)
    print(f"{r['id'][4:]}|{r['titulo'][:46]}|{cand}")
