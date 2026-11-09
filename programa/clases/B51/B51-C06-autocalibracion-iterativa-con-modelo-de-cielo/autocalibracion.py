#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C06: autocalibracion iterativa (imagen -> modelo -> ganancias) en un cielo unidimensional.

Datos: ninguna constante fisica. Cielo de 3 fuentes puntuales (1,0; 0,4 y 0,2 Jy), 10 antenas en una linea (posiciones en longitudes de onda), ganancias y ruido SINTETICOS
e ILUSTRATIVOS (semilla 20261109).
Modelo: V_ij = g_i conj(g_j) M_ij + ruido; imagen sucia por transformada de Fourier discreta, CLEAN de Hogbom (ganancia 0,1) para el modelo, ganancias por minimos cuadrados
alternados; el modelo inicial es solo la fuente brillante (el caso de partida habitual).
Segunda via: el flujo y la posicion de las fuentes y el error de las ganancias frente a la verdad conocida del cielo sintetico; control con modelo completo (solo ganancias).
Supuestos: un solo cielo 1D, sin direccion dependiente, ganancias constantes. Validez: ilustrativa; un cielo real tiene estructura extensa.
Tolerancia: el error de fase de las ganancias baja a menos de un tercio del inicial; el flujo de la fuente debil recuperado dentro de 15 %.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def stefcal(n, V, M, g0=None, iters=60, fase=False):
    g = list(g0) if g0 else [1 + 0j] * n
    for it in range(iters):
        new = []
        for i in range(n):
            num = den = 0j
            for j in range(n):
                if i == j:
                    continue
                v = V[(i, j)] if i < j else V[(j, i)].conjugate()
                m = M[(i, j)] if i < j else M[(j, i)].conjugate()
                z = g[j].conjugate() * m
                num += v * z.conjugate(); den += abs(z) ** 2
            new.append(num / den)
        g = [(a + b) / 2 for a, b in zip(g, new)] if it % 2 == 0 else new
        if fase:
            g = [x / abs(x) for x in g]
    return g

def gain_err(g, gt):
    rot = gt[0] / abs(gt[0])
    ph = math.sqrt(sum(cmath.phase((a * abs(g[0]) / g[0]) / (b / rot)) ** 2 for a, b in zip(g, gt)) / len(g))
    am = math.sqrt(sum((abs(a) / abs(b) - 1) ** 2 for a, b in zip(g, gt)) / len(g))
    return math.degrees(ph), 100 * am

def compute():
    rng = random.Random(20261109)
    n = 14
    x = sorted(rng.uniform(0, 2000) for _ in range(n))
    base = [(i, j) for i in range(n) for j in range(i + 1, n)]
    u = {b: x[b[1]] - x[b[0]] for b in base}
    sky = [(1.0, 0.0), (0.4, 1.2e-3), (0.2, -2.0e-3)]
    def vis_of(srcs):
        return {b: sum(s * cmath.exp(-2j * math.pi * u[b] * l) for s, l in srcs) for b in base}
    Mtrue = vis_of(sky)
    gt = [rng.lognormvariate(0, 0.08) * cmath.exp(1j * rng.gauss(0, 0.6)) for _ in range(n)]
    sig = 0.01
    V = {b: gt[b[0]] * gt[b[1]].conjugate() * Mtrue[b] + complex(rng.gauss(0, sig), rng.gauss(0, sig)) for b in base}
    nl, dl = 801, 1e-5
    ls = [(k - nl // 2) * dl for k in range(nl)]
    # haz sucio
    beam = {}
    for d in range(-(nl - 1), nl):
        beam[d] = sum(math.cos(2 * math.pi * u[b] * d * dl) for b in base) / len(base)
    def dirty(Vc):
        return [sum((Vc[b] * cmath.exp(2j * math.pi * u[b] * l)).real for b in base) / len(base) for l in ls]
    def clean(img, ncomp=600, gain=0.2):
        res = list(img); comps = {}
        for _ in range(ncomp):
            k = max(range(nl // 2 - 270, nl // 2 + 271), key=lambda q: abs(res[q]))
            a = gain * res[k]
            comps[k] = comps.get(k, 0.0) + a
            for q in range(nl):
                res[q] -= a * beam[q - k]
        return comps
    def model_vis(comps):
        return {b: sum(c * cmath.exp(-2j * math.pi * u[b] * ls[k]) for k, c in comps.items()) for b in base}
    hist = []
    M = vis_of([(1.0, 0.0)])             # modelo inicial: solo la fuente brillante
    g = [1 + 0j] * n
    hist.append(("modelo inicial", gain_err(g, gt), 0.0, 0.0))
    for it in range(1, 16):
        g = stefcal(n, V, M, g, fase=(it <= 6))
        Vc = {b: V[b] / (g[b[0]] * g[b[1]].conjugate()) for b in base}
        comps = clean(dirty(Vc))
        M = model_vis(comps)
        def flux_near(l0):
            return sum(c for k, c in comps.items() if abs(ls[k] - l0) < 6e-4)
        hist.append((f"iter. {it} ({'fase' if it <= 6 else 'amp+fase'})", gain_err(g, gt), flux_near(1.2e-3), flux_near(-2.0e-3)))
    # control: modelo completo conocido
    gc = stefcal(n, V, Mtrue)
    R = dict(n=n, nbase=len(base), sig=sig, hist=hist, ctrl=gain_err(gc, gt), g0err=gain_err([1 + 0j] * n, gt))
    # sesgo: ganancias resueltas contra el modelo incompleto, sin actualizar el modelo
    gw = stefcal(n, V, vis_of([(1.0, 0.0)]), fase=True)
    R["wrong"] = gain_err(gw, gt)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"antenas = {R['n']} ; bases = {R['nbase']} ; ruido = {R['sig']} Jy ; cielo: 1,0 Jy en l=0 ; 0,4 Jy en l=1,2e-3 ; 0,2 Jy en l=-2,0e-3")
    print(f"{'paso':>20} {'fase rms [gr]':>14} {'amp rms [%]':>12} {'S(0,4) hallado':>15} {'S(0,2) hallado':>15}")
    for name, (p, a), f1, f2 in R["hist"]:
        print(f"{name:>20} {p:14.3f} {a:12.3f} {f1:15.3f} {f2:15.3f}")
    print(f"ganancias sin calibrar: fase rms = {R['g0err'][0]:.2f} grados ; modelo incompleto sin actualizar: fase rms = {R['wrong'][0]:.2f} grados, amp rms = {R['wrong'][1]:.2f} %")
    print(f"control con el modelo verdadero: fase rms = {R['ctrl'][0]:.3f} grados, amp rms = {R['ctrl'][1]:.3f} %")
    fin = R["hist"][-1]
    assert fin[1][0] < R["hist"][0][1][0] / 3
    assert abs(fin[3] / 0.2 - 1) < 0.15 and abs(fin[2] / 0.4 - 1) < 0.15
    assert fin[1][0] < 5.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
