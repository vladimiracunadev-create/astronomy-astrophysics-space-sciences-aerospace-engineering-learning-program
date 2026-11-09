#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C03: ganancias complejas por antena con la ecuacion de medida V_ij = g_i conj(g_j) M_ij + ruido.

Datos: ninguna constante fisica. Modelo del cielo (1,0 Jy en el centro mas 0,4 Jy desplazado), posiciones, ganancias y ruido SINTETICOS e ILUSTRATIVOS (semilla 20261109).
Modelo: dos solucionadores independientes: (A) minimos cuadrados alternados complejos (tipo StefCal, con promediado de iteraciones) y (B) logaritmico-lineal, amplitud
por un lado y fase con antena de referencia por otro.
Supuestos: modelo del cielo conocido, una ganancia por antena, ruido gaussiano. La fase absoluta no es determinable: se fija la antena 0 como referencia (fase 0).
Validez: ilustrativa; no incluye terminos de polarizacion ni dependientes de direccion.
Tolerancia: recuperacion sin ruido 1e-9; con ruido, A y B coinciden con la verdad dentro de 2 veces el error predicho.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def solve(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x

def stefcal(n, V, M, iters=200):
    g = [1 + 0j] * n
    hist = []
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
        hist.append(sum(abs(a - b) for a, b in zip(g, new)))
        g = [(a + b) / 2 for a, b in zip(g, new)] if it % 2 == 0 else new
        if hist[-1] < 1e-13:
            break
    return g, it + 1

def loglin(n, V, M):
    base = list(V)
    ata = [[0.0] * n for _ in range(n)]; atb = [0.0] * n
    ph = [[0.0] * (n - 1) for _ in range(n - 1)]; pb = [0.0] * (n - 1)
    for (i, j) in base:
        z = V[(i, j)] / M[(i, j)]
        y = math.log(abs(z)); d = cmath.phase(z)
        atb[i] += y; atb[j] += y
        ata[i][i] += 1; ata[j][j] += 1; ata[i][j] += 1; ata[j][i] += 1
        # fase: phi_i - phi_j = d, con phi_0 = 0
        for a, s in ((i, 1), (j, -1)):
            if a > 0:
                pb[a - 1] += s * d
                for b, t in ((i, 1), (j, -1)):
                    if b > 0:
                        ph[a - 1][b - 1] += s * t
    amp = [math.exp(v) for v in solve(ata, atb)]
    phi = [0.0] + solve(ph, pb)
    return [a * cmath.exp(1j * p) for a, p in zip(amp, phi)]

def rms_err(gest, gtrue):
    # ambas referidas a la antena 0 como fase 0
    rot = gtrue[0] / abs(gtrue[0])
    gt = [x / rot for x in gtrue]
    ga = [x * (abs(gest[0]) / gest[0]) for x in gest]
    ea = math.sqrt(sum((abs(a) / abs(b) - 1) ** 2 for a, b in zip(ga, gt)) / len(gt))
    ep = math.sqrt(sum(cmath.phase(a / b) ** 2 for a, b in zip(ga, gt)) / len(gt))
    return ea, ep

def compute():
    rng = random.Random(20261109)
    n = 7
    pos = [(rng.uniform(0, 3000), rng.uniform(0, 3000)) for _ in range(n)]
    src = [(1.0, 0.0, 0.0), (0.4, 5.0e-4, -3.0e-4)]
    M = {}
    for i in range(n):
        for j in range(i + 1, n):
            u, v = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
            M[(i, j)] = sum(s * cmath.exp(-2j * math.pi * (u * l + v * m)) for s, l, m in src)
    g = [rng.lognormvariate(0, 0.15) * cmath.exp(1j * rng.gauss(0, 0.8)) for _ in range(n)]
    def make(sig, r):
        return {k: g[k[0]] * g[k[1]].conjugate() * M[k] + complex(r.gauss(0, sig), r.gauss(0, sig)) for k in M}
    R = dict(n=n, nbase=len(M))
    ga, it0 = stefcal(n, make(0.0, rng), M)
    R["a0"] = rms_err(ga, g); R["it0"] = it0
    gb = loglin(n, make(0.0, rng), M)
    R["b0"] = rms_err(gb, g)
    sig = 0.02
    mean_v = sum(abs(M[k]) * abs(g[k[0]]) * abs(g[k[1]]) for k in M) / len(M)
    R["sig"] = sig; R["pred"] = sig / (mean_v * math.sqrt(n - 1)); R["mean_v"] = mean_v
    ea = []; eb = []; pa = []; pbb = []
    for _ in range(200):
        d = make(sig, rng)
        x, _i = stefcal(n, d, M); y = loglin(n, d, M)
        ea.append(rms_err(x, g)); eb.append(rms_err(y, g))
    R["a_amp"] = math.sqrt(sum(e[0] ** 2 for e in ea) / len(ea)); R["a_ph"] = math.sqrt(sum(e[1] ** 2 for e in ea) / len(ea))
    R["b_amp"] = math.sqrt(sum(e[0] ** 2 for e in eb) / len(eb)); R["b_ph"] = math.sqrt(sum(e[1] ** 2 for e in eb) / len(eb))
    R["g_amp"] = [abs(x) for x in g]; R["g_ph"] = [math.degrees(cmath.phase(x / (g[0] / abs(g[0])))) for x in g]
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"antenas = {R['n']} ; bases = {R['nbase']} ; ganancias verdaderas (amp, fase respecto a la antena 0):")
    for k, (a, p) in enumerate(zip(R["g_amp"], R["g_ph"])):
        print(f"  antena {k}: |g| = {a:.4f} ; fase = {p:+8.3f} grados")
    print(f"sin ruido: A (alternados) error amp = {R['a0'][0]:.2e}, fase = {R['a0'][1]:.2e} rad en {R['it0']} iteraciones ; B (log-lineal) error amp = {R['b0'][0]:.2e}, fase = {R['b0'][1]:.2e} rad")
    assert R["a0"][0] < 1e-9 and R["a0"][1] < 1e-9 and R["b0"][0] < 1e-9 and R["b0"][1] < 1e-9
    print(f"con ruido {R['sig']} Jy (200 ensayos): error predicho ~ {R['pred']:.4f} (|V| medio {R['mean_v']:.3f})")
    print(f"  A: rms amp = {R['a_amp']:.4f}, rms fase = {R['a_ph']:.4f} rad ; B: rms amp = {R['b_amp']:.4f}, rms fase = {R['b_ph']:.4f} rad")
    for x in (R["a_amp"], R["a_ph"], R["b_amp"], R["b_ph"]):
        assert 0.5 * R["pred"] < x < 2 * R["pred"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
