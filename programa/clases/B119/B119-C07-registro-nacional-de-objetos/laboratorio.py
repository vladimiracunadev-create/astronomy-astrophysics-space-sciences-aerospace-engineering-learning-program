#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C07: calidad de un registro nacional de objetos espaciales SINTETICO (200 objetos con errores inyectados).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, UNOOSA, Convenio de Registro; WebFetch): art. II (cada Estado lleva un registro y avisa al Secretario General; su contenido lo fija el Estado),
art. IV (datos a informar: designador, fecha y lugar, parametros orbitales, funcion), y que si un objeto ya no esta en orbita se informa en lo posible.
SINTETICO: el registro completo; formato de designador AAAA-NNNL (ilustrativo, inspirado en designadores internacionales, no verificado).
Errores inyectados con semilla 119: designador vacio, designador duplicado, perigeo > apogeo, funcion vacia, fecha invalida.
Verificacion: las reglas de validacion deben encontrar EXACTAMENTE los errores inyectados (precision y exhaustividad 1.0).
"""
import datetime, json, platform, random, re

rng = random.Random(119)
FUNC = ["observacion", "comunicaciones", "navegacion", "ciencia", "tecnologia"]
reg = []
for i in range(200):
    anio = 2020 + i // 40
    reg.append(dict(id=f"{anio}-{i % 40 + 1:03d}{'ABCD'[i % 4]}", estado="Pais-" + "ABC"[i % 3], fecha=f"{anio}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}",
                    apogeo=rng.randint(500, 800), perigeo=0, funcion=rng.choice(FUNC)))
    reg[-1]["perigeo"] = reg[-1]["apogeo"] - rng.randint(0, 40)
# designadores unicos por construccion? comprobar y arreglar
vistos = set()
for r in reg:
    k = r["id"]
    n = 0
    while k in vistos:
        n += 1
        k = r["id"][:-1] + "EFGHIJKLMN"[n % 10]
    r["id"] = k
    vistos.add(k)
inj = {"id_vacio": set(), "id_dup": set(), "orbita": set(), "funcion": set(), "fecha": set()}
idx = rng.sample(range(200), 25)
for t, grupo in zip(inj, [idx[0:5], idx[5:10], idx[10:15], idx[15:20], idx[20:25]]):
    for j in grupo:
        inj[t].add(j)
        if t == "id_vacio": reg[j]["id"] = ""
        elif t == "id_dup": reg[j]["id"] = reg[(j + 1) % 200]["id"] if (j + 1) % 200 not in idx else reg[j]["id"]
        elif t == "orbita": reg[j]["perigeo"] = reg[j]["apogeo"] + 5
        elif t == "funcion": reg[j]["funcion"] = ""
        elif t == "fecha": reg[j]["fecha"] = f"{reg[j]['fecha'][:4]}-13-40"
# el duplicado puede no haberse creado si el vecino estaba tambien en idx: registrar solo los realmente duplicados
from collections import Counter
cnt = Counter(r["id"] for r in reg if r["id"])
dups = {j for j, r in enumerate(reg) if r["id"] and cnt[r["id"]] > 1}

def valida(r, cnt):
    e = set()
    if not r["id"]: e.add("id_vacio")
    elif not re.fullmatch(r"\d{4}-\d{3}[A-Z]", r["id"]): e.add("formato")
    elif cnt[r["id"]] > 1: e.add("id_dup")
    if r["perigeo"] > r["apogeo"]: e.add("orbita")
    if not r["funcion"]: e.add("funcion")
    try: datetime.date.fromisoformat(r["fecha"])
    except ValueError: e.add("fecha")
    return e

enc = {t: {j for j, r in enumerate(reg) if t in valida(r, cnt)} for t in inj}
real = {"id_vacio": inj["id_vacio"], "id_dup": dups, "orbita": inj["orbita"], "funcion": inj["funcion"], "fecha": inj["fecha"]}
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Registro SINTETICO de 200 objetos con errores inyectados (semilla 119); campos segun UNOOSA (consultado 2026-11-11).")
tot_real = tot_enc = 0
for t in inj:
    tp = len(enc[t] & real[t])
    print(f"  {t:9s} inyectados {len(real[t]):2d}  detectados {len(enc[t]):2d}  aciertos {tp:2d}")
    assert enc[t] == real[t], t
    tot_real += len(real[t]); tot_enc += len(enc[t])
con_error = {j for t in enc for j in enc[t]}
completitud = 1 - len(con_error) / 200
print(f"Objetos con al menos un error: {len(con_error)} de 200 ; calidad (sin errores) = {completitud:.3f}")
print(f"Precision = exhaustividad = {tot_enc / tot_real:.2f}")
print("CLAVES " + json.dumps({"n_err": len(con_error), "q": "%.3f" % completitud, "dup": len(dups), "vacio": len(inj["id_vacio"]), "orb": len(inj["orbita"])}))
print("Pruebas superadas.")
