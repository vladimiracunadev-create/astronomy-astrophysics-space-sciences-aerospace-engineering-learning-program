#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C23: priorizacion y deslastre de cargas electricas frente a la potencia disponible (satelite SINTETICO).

Datos consultados (2026-11-10): ninguno numerico (la logica de cargas prioritarias se estudia con datos sinteticos).
ILUSTRATIVOS (sinteticos): diez cargas con potencia y prioridad (1 = mas alta); las cargas de prioridad 1 y la recepcion de radio son criticas (no se pueden deslastrar);
dos modelos de valor: lexicografico (valor = 2^(9 - prioridad), la prioridad mas alta domina a todas las demas juntas) y aditivo (valor = 9 - prioridad);
potencias disponibles de 150, 100, 70, 60 y 30 W; perfil temporal sintetico con ruido (semilla 20261110) para probar la histeresis de reposicion (10 % de margen).
Estrategias: (a) deslastre estricto: se retira la carga de menor prioridad hasta que la suma cabe; (b) relleno: se recorre de mayor a menor prioridad anadiendo lo que cabe;
(c) optimo: busqueda exhaustiva (fuerza bruta) del subconjunto de mayor valor que contiene las cargas criticas y cabe en la potencia disponible.
Segunda via: la fuerza bruta (c) es la referencia; se comprueba que (a) y (b) nunca superan su valor y que con valores lexicograficos (b) es optimo.
Tolerancia: ninguna heuristica supera al optimo (diferencia exacta, enteros); (b) coincide con (c) en valor lexicografico en todas las potencias.
"""
from __future__ import annotations
import itertools, platform, random

CARGAS = [  # nombre, P [W], prioridad, critica
    ("Ordenador de a bordo", 12.0, 1, True),
    ("Control de actitud", 20.0, 1, True),
    ("Termica de supervivencia", 10.0, 1, True),
    ("Radio recepcion", 4.0, 2, True),
    ("Radio transmision", 14.0, 3, False),
    ("Almacenamiento de datos", 6.0, 4, False),
    ("Calefactor opcional", 8.0, 5, False),
    ("Carga util A", 30.0, 6, False),
    ("Carga util B", 15.0, 7, False),
    ("Experimento", 12.0, 8, False),
]
N = len(CARGAS)
DISPONIBLES = [150.0, 100.0, 70.0, 60.0, 30.0]


def valor(i, modelo):
    pr = CARGAS[i][2]
    return 2 ** (9 - pr) if modelo == "lex" else 9 - pr


def potencia(conj):
    return sum(CARGAS[i][1] for i in conj)


def estricto(pav):
    conj = set(range(N))
    for i in sorted(range(N), key=lambda k: (-CARGAS[k][2], -CARGAS[k][1])):
        if potencia(conj) <= pav:
            break
        if not CARGAS[i][3]:
            conj.discard(i)
    return conj


def relleno(pav):
    conj = {i for i in range(N) if CARGAS[i][3]}
    for i in sorted(range(N), key=lambda k: (CARGAS[k][2], CARGAS[k][1])):
        if i not in conj and potencia(conj) + CARGAS[i][1] <= pav:
            conj.add(i)
    return conj


def optimo(pav, modelo):
    crit = {i for i in range(N) if CARGAS[i][3]}
    libres = [i for i in range(N) if i not in crit]
    mejor, mv = set(crit), -1          # si ni las criticas caben se devuelve solo el conjunto critico (emergencia)
    for r in range(len(libres) + 1):
        for c in itertools.combinations(libres, r):
            s = crit | set(c)
            if potencia(s) <= pav:
                v = sum(valor(i, modelo) for i in s)
                if v > mv:
                    mejor, mv = s, v
    return mejor


def vsum(conj, modelo):
    return sum(valor(i, modelo) for i in conj)


def histeresis(perfil, margen=0.10, usar=True):
    activo = set(range(N))
    trans = 0
    for pav in perfil:
        if potencia(activo) > pav:
            nuevo = estricto(pav)
        elif usar and any(i not in activo for i in range(N)) and potencia(set(range(N))) * (1.0 + 0.0) <= pav * (1.0 - margen):
            nuevo = set(range(N))
        elif not usar:
            nuevo = relleno(pav) if potencia(set(range(N))) > pav else set(range(N))
        else:
            nuevo = activo
        if nuevo != activo:
            trans += 1
        activo = nuevo
    return trans


def resultados():
    r = dict(P_total=potencia(range(N)), P_crit=potencia({i for i in range(N) if CARGAS[i][3]}))
    filas = []
    for pav in DISPONIBLES:
        e, f = estricto(pav), relleno(pav)
        ol, oa = optimo(pav, "lex"), optimo(pav, "adit")
        fila = dict(pav=pav,
                    e_P=potencia(e), f_P=potencia(f), ol_P=potencia(ol), oa_P=potencia(oa),
                    e_lex=vsum(e, "lex"), f_lex=vsum(f, "lex"), ol_lex=vsum(ol, "lex"),
                    e_adit=vsum(e, "adit"), f_adit=vsum(f, "adit"), oa_adit=vsum(oa, "adit"),
                    e_n=len(e), f_n=len(f), ol_n=len(ol), oa_n=len(oa),
                    f_shed=sorted(CARGAS[i][0] for i in range(N) if i not in f),
                    e_shed=sorted(CARGAS[i][0] for i in range(N) if i not in e))
        filas.append(fila)
    r["filas"] = filas
    r["fila_70"] = [f for f in filas if f["pav"] == 70.0][0]
    # perfil temporal sintetico: dias 1-3 con luz (140 W) y eclipse (60-75 W) con ruido
    rng = random.Random(20261110)
    perfil = []
    for k in range(400):
        base = 140.0 if (k % 8) < 5 else 62.0
        perfil.append(base + rng.uniform(-9.0, 9.0))
    r["trans_con"], r["trans_sin"] = histeresis(perfil, 0.10, True), histeresis(perfil, 0.10, False)
    r["n_perfil"] = len(perfil)
    for k, f in enumerate(filas):
        for a in ("e_n", "e_P", "e_lex", "f_n", "f_P", "f_lex", "f_adit", "ol_n", "ol_lex", "oa_n", "oa_P", "oa_adit"):
            r[f"{a.split('_')[0]}{k}_{a.split('_')[1]}"] = f[a]
    f70 = r["fila_70"]
    r["e_n70"], r["e_P70"], r["f_n70"], r["f_P70"] = f70["e_n"], f70["e_P"], f70["f_n"], f70["f_P"]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Cargas SINTETICAS: {N} (total {r['P_total']:.0f} W ; criticas {r['P_crit']:.0f} W). Fuerza bruta sobre {2 ** (N - 4)} subconjuntos de las 6 cargas no criticas")
    print(" P_disp [W]  estricto: n / P / valor lex / valor adit   relleno: n / P / lex / adit   optimo lex: n / P / lex   optimo adit: n / P / adit")
    for f in r["filas"]:
        print(f" {f['pav']:9.0f}   {f['e_n']:2d} {f['e_P']:5.0f} {f['e_lex']:5d} {f['e_adit']:3d}          {f['f_n']:2d} {f['f_P']:5.0f} {f['f_lex']:5d} {f['f_adit']:3d}       {f['ol_n']:2d} {f['ol_P']:5.0f} {f['ol_lex']:5d}          {f['oa_n']:2d} {f['oa_P']:5.0f} {f['oa_adit']:3d}")
    print("Cargas deslastradas con 70 W: estricto =", ", ".join(r["fila_70"]["e_shed"]) or "ninguna")
    print("                              relleno  =", ", ".join(r["fila_70"]["f_shed"]) or "ninguna")
    print(f"Perfil de {r['n_perfil']} pasos con ruido: transiciones con histeresis de reposicion = {r['trans_con']} ; sin histeresis (relleno en cada paso) = {r['trans_sin']}")
    for f in r["filas"]:
        assert f["f_lex"] == f["ol_lex"], "con valor lexicografico el relleno es optimo"
        assert f["e_lex"] <= f["ol_lex"] and f["f_adit"] <= f["oa_adit"] and f["e_adit"] <= f["oa_adit"]
        assert f["e_P"] <= max(f["pav"], r["P_crit"]) and f["f_P"] <= max(f["pav"], r["P_crit"])
    assert any(f["f_adit"] < f["oa_adit"] for f in r["filas"]), "debe existir un caso donde el relleno no es optimo con valores aditivos"
    assert r["trans_con"] <= r["trans_sin"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
