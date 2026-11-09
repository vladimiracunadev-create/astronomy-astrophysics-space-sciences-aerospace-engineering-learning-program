#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C14: calibracion de banda en la reduccion de sintesis: solucion con un calibrador, aplicacion al blanco y sustraccion del continuo.

Datos: ninguna constante fisica. Banda de 128 canales con respuesta estructurada, calibrador de 5,0 Jy, blanco con continuo de 0,50 Jy y una linea de 5 mJy en 5 canales,
ruido por muestra de 0,05 Jy, 20 muestras (integraciones) por solucion de banda y ruido del blanco de 2,5 mJy por canal (400 muestras promediadas): todo SINTETICO e ILUSTRATIVO (semilla 20261109).
Modelo: B_c = |V_cal,c| / S_cal promediado en el tiempo; V_obj,c / B_c; ajuste polinomico de orden p al continuo con los canales sin linea y sustraccion.
Segunda via: el ruido que la solucion de banda inyecta en el blanco, S_obj sigma rms(1/B) / (S_cal sqrt(n)), con rms(1/B) sobre los canales, frente a un Monte Carlo; y la comparacion con ajustar solo un polinomio sin calibrar la banda.
Supuestos: la respuesta de banda es la misma para calibrador y blanco, constante en el tiempo y real positiva (amplitud); ruido gaussiano. Validez: ilustrativa.
Tolerancia: ruido inyectado Monte Carlo dentro de 5 % de la formula; el flujo de la linea recuperado dentro de 2 sigma; sin calibrar la banda el residuo es mucho mayor.
"""
from __future__ import annotations
import math, platform, random, sys

def polyfit(xs, ys, p):
    n = p + 1
    ata = [[sum(x ** (i + j) for x in xs) for j in range(n)] for i in range(n)]
    atb = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(n)]
    m = [r[:] + [atb[i]] for i, r in enumerate(ata)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(m[r][i])); m[i], m[piv] = m[piv], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    co = [0.0] * n
    for i in range(n - 1, -1, -1):
        co[i] = (m[i][n] - sum(m[i][j] * co[j] for j in range(i + 1, n))) / m[i][i]
    return co

def polyval(co, x):
    return sum(c * x ** i for i, c in enumerate(co))

def compute():
    rng = random.Random(20261109)
    N = 128
    xs = [-1 + 2 * (k + 0.5) / N for k in range(N)]
    Btrue = [1.0 - 0.45 * x * x + 0.06 * math.sin(14 * x) for x in xs]
    s_cal, s_obj, sig, n = 5.0, 0.50, 0.05, 20
    line = {c: 0.005 for c in range(60, 65)}
    inline = set(line)
    free = [k for k in range(N) if k not in inline and abs(k - 62) > 4]
    def visobj(r):
        return [Btrue[c] * (s_obj + line.get(c, 0.0)) + r.gauss(0, sig / 20) for c in range(N)]
    def run(order, calibrate, r):
        if calibrate:
            Bh = [sum(Btrue[c] * s_cal + r.gauss(0, sig) for _ in range(n)) / n / s_cal for c in range(N)]
        else:
            Bh = [1.0] * N
        sp = [v / b for v, b in zip(visobj(r), Bh)]
        co = polyfit([xs[c] for c in free], [sp[c] for c in free], order)
        res = [sp[c] - polyval(co, xs[c]) for c in range(N)]
        return res
    R = dict(N=N, s_cal=s_cal, s_obj=s_obj, sig=sig, n=n, free=len(free))
    R["pred_noise"] = s_obj * sig / (s_cal * math.sqrt(n)) * math.sqrt(sum(1 / b ** 2 for b in Btrue) / N)
    # ruido inyectado: aislar la contribucion de la solucion de banda (blanco sin ruido propio)
    tot = []
    for _ in range(300):
        Bh = [sum(Btrue[c] * s_cal + rng.gauss(0, sig) for _ in range(n)) / n / s_cal for c in range(N)]
        sp = [Btrue[c] * s_obj / Bh[c] for c in range(N)]
        tot += [(sp[c] - s_obj) for c in range(N)]
    mu = sum(tot) / len(tot)
    R["inj_sd"] = math.sqrt(sum((v - mu) ** 2 for v in tot) / (len(tot) - 1))
    # residuo con y sin calibrar la banda, por orden
    R["rows"] = []
    for p in (0, 1, 2, 3, 5):
        a = []; b = []; la = []
        for _ in range(100):
            res = run(p, True, rng)
            a += [res[c] for c in free]
            la.append(sum(res[c] for c in line) / len(line))
            res2 = run(p, False, rng)
            b += [res2[c] for c in free]
        sa = math.sqrt(sum(v * v for v in a) / len(a)); sb = math.sqrt(sum(v * v for v in b) / len(b))
        mla = sum(la) / len(la); sdl = math.sqrt(sum((v - mla) ** 2 for v in la) / (len(la) - 1))
        R["rows"].append((p, sa, sb, mla, sdl))
    R["noise_obj"] = sig / 20
    R["line_sigma_pred"] = math.sqrt(((sig / 20) ** 2 + R["pred_noise"] ** 2) / len(line))
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"canales = {R['N']} ; canales libres de linea = {R['free']} ; calibrador {R['s_cal']} Jy ; continuo del blanco {R['s_obj']} Jy ; ruido {R['sig']} Jy ; {R['n']} muestras por solucion")
    print(f"ruido inyectado por la solucion de banda en el blanco: formula S_obj sigma rms(1/B)/(S_cal sqrt n) = {R['pred_noise'] * 1000:.3f} mJy ; Monte Carlo = {R['inj_sd'] * 1000:.3f} mJy")
    assert abs(R["inj_sd"] / R["pred_noise"] - 1) < 0.05
    print("orden  rms residuo con banda calibrada [mJy]  rms residuo sin calibrar [mJy]  flujo medio de la linea [mJy]  dispersion [mJy]")
    for p, sa, sb, ml, sdl in R["rows"]:
        print(f"{p:5d} {sa * 1000:30.3f} {sb * 1000:30.3f} {ml * 1000:26.3f} {sdl * 1000:19.3f}")
    r = {row[0]: row for row in R["rows"]}
    assert r[0][2] > 20 * r[0][1] and r[5][2] > 3 * r[5][1]
    assert abs(r[3][3] - 0.005) < 2 * R["line_sigma_pred"]
    print(f"sigma esperada del flujo medio de la linea (5 canales) = {R['line_sigma_pred'] * 1000:.3f} mJy")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
