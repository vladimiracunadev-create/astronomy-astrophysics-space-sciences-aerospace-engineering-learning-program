#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C02: fotometria participativa con datos SINTETICOS.

Todo SINTETICO: estrella variable VS-S (m = 10.00 + 0.50 sin(2 pi t/37.0)), estrella de comparacion de magnitud
catalogo 10.50 (valor ILUSTRATIVO, no es de ningun catalogo), 8 voluntarios con ruido y sesgo inventados.
Relaciones: m = -2.5 log10(F) + cte; magnitud diferencial m_v = m_c - 2.5 log10(F_v/F_c);
error fotonico sigma_m = 1.0857 sqrt(1/F_v + 1/F_c) (flujos en electrones, solo ruido de Poisson, sin cielo ni lectura).
Segunda via del error: Monte Carlo (semilla 129, 20000 repeticiones, ruido de Poisson aproximado por gaussiana).
Combinacion: media ponderada w = 1/sigma^2 con varianza 1/sum(w); el sesgo comun NO se reduce con mas voluntarios.
Periodo: barrido de periodos de prueba con ajuste lineal por minimos cuadrados de [1, sin, cos] (resolucion 0.05 d).
Tolerancias: sigma analitico vs MC dentro del 3 %; varianza de la media ponderada vs MC dentro del 5 %.
Unidades: dias (t), magnitudes (mag), electrones (flujos).
"""
from __future__ import annotations
import math, platform, random, statistics

M0, AMP, PER = 10.00, 0.50, 37.0
M_COMP = 10.50
# (nombre, sigma [mag], sesgo [mag]) -- SINTETICOS
VOL = [("V1", 0.02, +0.00), ("V2", 0.03, -0.04), ("V3", 0.05, +0.06), ("V4", 0.05, -0.02),
       ("V5", 0.08, +0.03), ("V6", 0.10, -0.05), ("V7", 0.12, +0.05), ("V8", 0.15, +0.00)]


def verdadera(t):
    return M0 + AMP * math.sin(2 * math.pi * t / PER)


def sigma_fotonico(fv, fc):
    return 1.0857 * math.sqrt(1.0 / fv + 1.0 / fc)


def mc_fotometria(fv, fc, n, rng):
    ms = []
    for _ in range(n):
        v = fv + rng.gauss(0, math.sqrt(fv))
        c = fc + rng.gauss(0, math.sqrt(fc))
        ms.append(M_COMP - 2.5 * math.log10(v / c))
    return statistics.pstdev(ms)


def ajuste_sinusoide(ts, ms, p):
    # normales de [1, sin, cos] resueltas a mano (3x3)
    w = 2 * math.pi / p
    X = [(1.0, math.sin(w * t), math.cos(w * t)) for t in ts]
    A = [[sum(x[i] * x[j] for x in X) for j in range(3)] for i in range(3)]
    b = [sum(x[i] * y for x, y in zip(X, ms)) for i in range(3)]
    n = 3
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[piv] = A[piv], A[i]
        b[i], b[piv] = b[piv], b[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
            b[r] -= f * b[i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    res = sum((y - sum(c * v for c, v in zip(x, xi))) ** 2 for xi, y in zip(X, ms))
    return res, x


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    print("DATOS SINTETICOS: variable VS-S (m0 = 10.00, A = 0.50 mag, P = 37.0 d); comparacion 10.50 (ilustrativo)")
    # 1) error fotonico
    print("1) Error fotonico de la magnitud diferencial (analitico frente a Monte Carlo)")
    print("   F_v [e-]   F_c [e-]   sigma anal [mag]   sigma MC [mag]   dif [%]")
    for fv, fc in ((2.0e3, 4.0e3), (2.0e4, 4.0e4), (2.0e5, 4.0e5)):
        sa = sigma_fotonico(fv, fc)
        sm = mc_fotometria(fv, fc, 20000, rng)
        d = abs(sa - sm) / sa * 100
        print(f"   {fv:8.0f}  {fc:9.0f}   {sa:14.5f}   {sm:14.5f}   {d:6.2f}")
        assert d < 3.0, "el error fotonico no coincide con el Monte Carlo"
    # 2) combinacion de voluntarios
    print("2) Combinacion de 8 voluntarios: 60 noches, cada uno observa con probabilidad 0.5")
    obs = []  # (noche, voluntario, magnitud)
    for noche in range(60):
        t = noche * 1.0
        for nom, s, b in VOL:
            if rng.random() < 0.5:
                obs.append((t, nom, verdadera(t) + b + rng.gauss(0, s)))
    sig = {nom: s for nom, s, _ in VOL}
    sesgo = {nom: b for nom, _, b in VOL}
    por_noche = {}
    for t, nom, m in obs:
        por_noche.setdefault(t, []).append((nom, m))

    def rms(f):
        e = []
        for t, lst in por_noche.items():
            e.append(f(lst) - verdadera(t))
        return math.sqrt(sum(x * x for x in e) / len(e))

    def pond(lst, corr=None):
        w = [1 / sig[n] ** 2 for n, _ in lst]
        v = [m - (corr[n] if corr else 0.0) for n, m in lst]
        return sum(a * b for a, b in zip(w, v)) / sum(w)

    simple = rms(lambda l: sum(m for _, m in l) / len(l))
    med = rms(lambda l: statistics.median(m for _, m in l))
    ponde = rms(pond)
    print(f"   noches con datos = {len(por_noche)}, observaciones = {len(obs)}")
    print(f"   RMS media simple = {simple:.4f} mag; mediana = {med:.4f} mag; media ponderada = {ponde:.4f} mag")
    # sesgo estimado respecto del conjunto (solo es identificable el sesgo relativo)
    res = {n: [] for n in sig}
    for t, lst in por_noche.items():
        if len(lst) >= 3:
            mm = statistics.median(m for _, m in lst)
            for n, m in lst:
                res[n].append(m - mm)
    est = {n: statistics.median(v) for n, v in res.items() if v}
    c0 = statistics.mean(est.values())
    est = {n: v - c0 for n, v in est.items()}
    ponde_c = rms(lambda l: pond(l, est))
    print(f"   sesgo relativo estimado [mag]: " + ", ".join(f"{n}:{est[n]:+.3f}" for n in sorted(est)))
    print(f"   RMS ponderada con sesgo relativo corregido = {ponde_c:.4f} mag")
    assert ponde <= simple, "la ponderacion debe mejorar a la media simple"
    # 3) varianza de la media ponderada: analitica y Monte Carlo (sin sesgo)
    nombres = [n for n, _, _ in VOL]
    var_a = 1 / sum(1 / sig[n] ** 2 for n in nombres)
    vals = []
    for _ in range(20000):
        w = [1 / sig[n] ** 2 for n in nombres]
        x = [rng.gauss(0, sig[n]) for n in nombres]
        vals.append(sum(a * b for a, b in zip(w, x)) / sum(w))
    var_m = statistics.pvariance(vals)
    d = abs(var_a - var_m) / var_a * 100
    print(f"3) Varianza de la media ponderada de los 8 (sin sesgo): analitica = {var_a:.3e} mag2; MC = {var_m:.3e} mag2; dif = {d:.2f} %")
    assert d < 5.0
    # sesgo medio ponderado = piso del error con muchos voluntarios
    wb = sum(sesgo[n] / sig[n] ** 2 for n in nombres) / sum(1 / sig[n] ** 2 for n in nombres)
    print(f"   Sesgo medio ponderado (piso del error aunque N crezca) = {wb:+.4f} mag")
    # 4) periodo
    ts = [t for t, _, _ in obs]
    ms = [m for _, _, m in obs]
    mejor = None
    p = 20.0
    while p <= 60.0001:
        r, x = ajuste_sinusoide(ts, ms, p)
        if mejor is None or r < mejor[0]:
            mejor = (r, p, x)
        p += 0.05
    amp = math.hypot(mejor[2][1], mejor[2][2])
    print(f"4) Periodo recuperado por minimos cuadrados = {mejor[1]:.2f} d (sintetico 37.0 d); amplitud = {amp:.3f} mag (0.500)")
    assert abs(mejor[1] - PER) < 0.5 and abs(amp - AMP) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
