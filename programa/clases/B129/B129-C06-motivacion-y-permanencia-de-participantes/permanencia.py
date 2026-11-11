#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C06: permanencia de participantes SINTETICOS (Kaplan-Meier) y concentracion de contribuciones.

Todo SINTETICO e ILUSTRATIVO: cohorte de 500 voluntarios inventados; tiempo hasta el abandono exponencial con riesgo h0 = 0.08 por semana
(mediana ln2/h = 8.66 semanas); censura administrativa a las 26 semanas. Escenario B: riesgo multiplicado por 0.80, un efecto SUPUESTO de
un incentivo (NO medido en ninguna fuente); escenario C: riesgo igual a h0 (incentivo sin efecto).
Estimador de Kaplan-Meier implementado a mano; segunda via: S(t) = exp(-h t) con h estimado como eventos / tiempo total en riesgo (maxima
verosimilitud exponencial). Comparacion de dos cohortes con la razon de riesgos y su IC aproximado: log(RR) +/- 1.96 sqrt(1/d1 + 1/d2).
Contribuciones por voluntario: lognormal(mu=1.0, sigma=1.5) (forma ILUSTRATIVA); Gini por dos formulas (suma de diferencias y ordenada).
Las 12 categorias de motivacion de Raddick et al. (2009) se citan como lista; NO se simula ninguna motivacion.
Tolerancias: |KM - exp| <= 0.05 en semanas 4, 8, 13, 26; los dos Gini coinciden a 1e-9. Semilla 129. Unidades: semanas.
"""
from __future__ import annotations
import math, platform, random

H0 = 0.08
CENSURA = 26.0
N = 500
MOTIV = ["Contribute", "Learning", "Discovery", "Community", "Teaching", "Beauty", "Fun", "Vastness", "Helping", "Zoo", "Astronomy", "Science"]


def cohorte(rng, h, n=N):
    datos = []
    for _ in range(n):
        t = rng.expovariate(h)
        datos.append((min(t, CENSURA), t <= CENSURA))
    return datos


def kaplan_meier(datos):
    datos = sorted(datos)
    riesgo = len(datos)
    s = 1.0
    curva = []
    i = 0
    while i < len(datos):
        t = datos[i][0]
        d = c = 0
        while i < len(datos) and datos[i][0] == t:
            d += datos[i][1]
            c += not datos[i][1]
            i += 1
        if d:
            s *= 1 - d / riesgo
        curva.append((t, s))
        riesgo -= d + c
    return curva


def s_en(curva, t):
    s = 1.0
    for ti, si in curva:
        if ti <= t:
            s = si
        else:
            break
    return s


def h_mle(datos):
    return sum(e for _, e in datos) / sum(t for t, _ in datos)


def gini_a(x):
    n = len(x)
    m = sum(x) / n
    return sum(abs(a - b) for a in x for b in x) / (2 * n * n * m)


def gini_b(x):
    y = sorted(x)
    n = len(y)
    return (2 * sum((i + 1) * v for i, v in enumerate(y)) / (n * sum(y))) - (n + 1) / n


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    print(f"DATOS SINTETICOS: {N} voluntarios; riesgo h0 = {H0}/semana (mediana {math.log(2) / H0:.2f} sem); censura a {CENSURA:.0f} sem")
    A = cohorte(rng, H0)
    curva = kaplan_meier(A)
    hA = h_mle(A)
    print(f"1) Cohorte A: abandonos = {sum(e for _, e in A)}, censurados = {sum(not e for _, e in A)}; h estimado = {hA:.4f} /sem")
    print("   semana   KM      exp(-h_mle t)   exp(-h0 t)  |KM-exp|")
    peor = 0.0
    for t in (4, 8, 13, 26):
        km = s_en(curva, t)
        ex = math.exp(-hA * t)
        peor = max(peor, abs(km - ex))
        print(f"   {t:5d}   {km:.3f}   {ex:.3f}          {math.exp(-H0 * t):.3f}       {abs(km - ex):.3f}")
    assert peor <= 0.05
    # mediana KM
    mediana = next((t for t, s in curva if s <= 0.5), float("nan"))
    print(f"   mediana de permanencia (KM) = {mediana:.2f} sem; teorica {math.log(2) / H0:.2f} sem")
    # 2) comparacion de dos escenarios
    print("2) Comparacion con un incentivo SUPUESTO (riesgo x 0.80) y con un incentivo sin efecto (riesgo x 1.00)")
    print("   escenario        eventos   tiempo[sem]   h_mle    RR vs A    IC95 %")
    dA, tA = sum(e for _, e in A), sum(t for t, _ in A)
    print(f"   A (control)      {dA:7d}   {tA:11.1f}   {hA:.4f}")
    for nombre, f in (("B (x0.80)", 0.80), ("C (x1.00)", 1.00)):
        X = cohorte(rng, H0 * f)
        dX, tX = sum(e for _, e in X), sum(t for t, _ in X)
        hX = dX / tX
        rr = hX / hA
        se = math.sqrt(1 / dX + 1 / dA)
        lo, hi = rr * math.exp(-1.96 * se), rr * math.exp(1.96 * se)
        print(f"   {nombre:15s}  {dX:7d}   {tX:11.1f}   {hX:.4f}   {rr:7.3f}   [{lo:.3f}, {hi:.3f}]")
    # tamano necesario para detectar RR = 0.8 (aprox.): d tal que 1.96*sqrt(2/d)*... ancho < 0.22
    d_nec = math.ceil(2 * (1.96 / math.log(1 / 0.8)) ** 2)
    print(f"   Eventos por cohorte para que el IC95 % de log(RR) excluya 0 si el RR fuera 0.80: aprox. {d_nec} (potencia ~50 %)")
    # 3) concentracion de contribuciones
    cont = [rng.lognormvariate(1.0, 1.5) for _ in range(N)]
    ga, gb = gini_a(cont), gini_b(cont)
    orden = sorted(cont, reverse=True)
    top10 = sum(orden[: N // 10]) / sum(cont)
    top1 = sum(orden[: N // 100]) / sum(cont)
    print(f"3) Concentracion (lognormal ilustrativa): Gini = {ga:.4f} (suma de diferencias) = {gb:.4f} (ordenada); top 10 % aporta {top10 * 100:.1f} %, top 1 % aporta {top1 * 100:.1f} %")
    assert abs(ga - gb) < 1e-9
    teorico = math.erf(1.5 / 2)
    print(f"   Gini teorico lognormal = erf(sigma/2) = {teorico:.4f}")
    assert abs(ga - teorico) < 0.05
    print("4) Categorias de motivacion de Raddick et al. (2009), solo como lista: " + ", ".join(MOTIV))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
