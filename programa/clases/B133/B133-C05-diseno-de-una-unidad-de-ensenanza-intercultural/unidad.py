#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B133-C05: verificar el plan de una unidad intercultural SINTETICA y dimensionar su medicion del orto solar.

Todo es SINTETICO: la escuela (latitud -38.0 deg), la comunidad ficticia de Alfa-Tul, el invitado portador del saber, las
sesiones y la incertidumbre de la brujula (sigma = 2 deg). Nada representa a una escuela ni a un pueblo reales.
Parte 1 (plan): 6 sesiones de 60 min; se comprueba (a) minutos por sesion <= 60 y total 360, (b) toda actividad de tipo
«saber» la lidera el portador y no el docente, (c) cada objetivo esta cubierto, (d) ningun componente (ciencia, saber,
dialogo) ocupa menos de 20 % del tiempo. Los umbrales son decisiones de esta clase; no provienen de una fuente.
Parte 2 (medicion): acimut del orto con la misma forma cerrada de B133-C01 (declinacion con longitud eclíptica uniforme,
valida cerca del equinoccio de marzo y de los solsticios). Se pide la separacion minima en dias entre dos mediciones para
que el cambio de acimut supere 2*sqrt(2)*sigma. Segunda via: derivada numerica frente a diferencia finita, y simulacion de
ruido con semilla fija (tasa de deteccion >= 0.95 con la separacion calculada, margen de 1.5 sigma).
Tolerancias: derivada analitica frente a diferencias finitas < 1e-4 deg/dia.
"""
from __future__ import annotations
import math, platform, random

RAD = math.pi / 180
PHI = -38.0          # SINTETICO
SIGMA = 2.0          # [deg] SINTETICO (brujula)
EPS = 23.44
H = -0.833

ACTIVIDADES = [  # (sesion, nombre, tipo, minutos, lidera, objetivo)
    (1, "Presentacion del territorio y de la comunidad", "saber", 30, "portador", "O2"),
    (1, "Acuerdo sobre protocolos del aula", "dialogo", 30, "portador", "O4"),
    (2, "Por que el sol sale por lugares distintos", "ciencia", 40, "docente", "O1"),
    (2, "Predecir el acimut del orto", "ciencia", 20, "docente", "O1"),
    (3, "Como la comunidad sigue el sol en su casa", "saber", 40, "portador", "O2"),
    (3, "Comparar el marcador con la medicion escolar", "dialogo", 20, "portador", "O2"),
    (4, "Medir el orto con brujula y registrar incertidumbre", "ciencia", 60, "docente", "O3"),
    (5, "Analizar datos con dos ojos: ciencia y saber", "dialogo", 40, "docente", "O1"),
    (5, "Cuidado de los relatos: que no se cuenta", "saber", 20, "portador", "O4"),
    (6, "Devolver los resultados a la comunidad", "dialogo", 40, "portador", "O4"),
    (6, "Cierre y evaluacion", "ciencia", 20, "docente", "O3"),
]
OBJETIVOS = {"O1": "explicar el cambio del orto", "O2": "describir el uso del cielo de la comunidad",
             "O3": "medir y expresar la incertidumbre", "O4": "respetar los protocolos del saber"}


def verificar(plan) -> list[str]:
    h = []
    por_sesion: dict[int, int] = {}
    for s, _n, _t, m, _l, _o in plan:
        por_sesion[s] = por_sesion.get(s, 0) + m
    for s, m in sorted(por_sesion.items()):
        if m > 60:
            h.append(f"sesion {s} dura {m} min (> 60)")
    total = sum(por_sesion.values())
    if total != 360:
        h.append(f"total {total} min (esperado 360)")
    for s, n, t, m, l, o in plan:
        if t == "saber" and l != "portador":
            h.append(f"actividad de saber sin portador: {n}")
    cubiertos = {o for *_, o in plan}
    for o in OBJETIVOS:
        if o not in cubiertos:
            h.append(f"objetivo {o} sin cubrir")
    for t in ("ciencia", "saber", "dialogo"):
        frac = sum(m for _s, _n, tt, m, _l, _o in plan if tt == t) / max(total, 1)
        if frac < 0.20:
            h.append(f"componente {t} con {frac:.2f} del tiempo (< 0.20)")
    return h


def decl(n: float) -> float:
    return math.degrees(math.asin(math.sin(EPS * RAD) * math.sin(2 * math.pi * (n - 80) / 365.25)))


def acimut(n: float) -> float:
    d, p, h = decl(n) * RAD, PHI * RAD, H * RAD
    c = (math.sin(d) - math.sin(p) * math.sin(h)) / (math.cos(p) * math.cos(h))
    return math.degrees(math.acos(max(-1, min(1, c))))


def dA_dn_analitica(n: float) -> float:
    """Derivada de A respecto del dia [deg/dia] por la regla de la cadena."""
    d = decl(n) * RAD
    p, h = PHI * RAD, H * RAD
    lam = 2 * math.pi * (n - 80) / 365.25
    dd = (math.sin(EPS * RAD) * math.cos(lam) * 2 * math.pi / 365.25) / math.cos(d)   # d(delta)/dn [rad/dia]
    c = (math.sin(d) - math.sin(p) * math.sin(h)) / (math.cos(p) * math.cos(h))
    dc = math.cos(d) * dd / (math.cos(p) * math.cos(h))
    return math.degrees(-dc / math.sqrt(1 - c * c))


def separacion_minima(n0: int, umbral: float) -> int | None:
    for dias in range(1, 200):
        if abs(acimut(n0 + dias) - acimut(n0)) >= umbral:
            return dias
    return None


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Escuela, comunidad y portador SINTETICOS (Alfa-Tul es ficticia).")
    h = verificar(ACTIVIDADES)
    tot = sum(a[3] for a in ACTIVIDADES)
    print(f"Plan: {len(ACTIVIDADES)} actividades, {tot} min, hallazgos = {len(h)}")
    for t in ("ciencia", "saber", "dialogo"):
        m = sum(a[3] for a in ACTIVIDADES if a[2] == t)
        print(f"   {t:8s} {m:4d} min  ({m / tot:.2f})")
    lid = sum(a[3] for a in ACTIVIDADES if a[4] == "portador")
    print(f"   tiempo liderado por el portador: {lid} min ({lid / tot:.2f})")
    assert h == []
    malo = [(s, n, t, m, ("docente" if t == "saber" else l), o) for s, n, t, m, l, o in ACTIVIDADES]
    hm = verificar(malo)
    print(f"Plan modificado (el docente lidera el saber): hallazgos = {len(hm)}")
    for x in hm:
        print(f"   {x}")
    assert len(hm) == 3
    # Parte 2
    Z = 1.645
    tau = Z * math.sqrt(2) * SIGMA            # criterio de decision (5 % de falsas alarmas)
    umbral = 2 * tau                          # cambio real para 95 % de potencia
    print(f"\nMedicion del orto con brujula (sigma = {SIGMA} deg): criterio de decision = {tau:.3f} deg; cambio real necesario = {umbral:.3f} deg")
    peor = 0.0
    for n in (80, 120, 172, 220, 260):
        an = dA_dn_analitica(n)
        fd = (acimut(n + 0.5) - acimut(n - 0.5))
        peor = max(peor, abs(an - fd))
    print(f"Derivada analitica frente a diferencia finita: diferencia maxima = {peor:.2e} deg/dia")
    assert peor < 1e-4
    print(" inicio    dia  dA/dn[deg/dia]  separacion minima [dias]")
    seps = {}
    for nombre, n0 in (("21-03", 80), ("21-06", 172), ("21-04", 111)):
        s = separacion_minima(n0, umbral)
        seps[n0] = s
        print(f" {nombre}  {n0:5d}   {dA_dn_analitica(n0):10.4f}      {s}")
    assert seps[80] < seps[111] < seps[172]
    rng = random.Random(20261111)
    n0, dias = 80, seps[80]
    real = abs(acimut(n0 + dias) - acimut(n0))
    N = 20000
    potencia = sum((acimut(n0) + rng.gauss(0, SIGMA)) - (acimut(n0 + dias) + rng.gauss(0, SIGMA)) >= tau for _ in range(N)) / N
    falsas = sum(rng.gauss(0, SIGMA) - rng.gauss(0, SIGMA) >= tau for _ in range(N)) / N
    print(f"Simulacion (semilla 20261111, {N} pares): con {dias} dias (cambio real {real:.3f} deg) potencia = {potencia:.3f}; falsas alarmas sin cambio = {falsas:.3f}")
    assert potencia >= 0.94 and abs(falsas - 0.05) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
