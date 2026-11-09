#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C02: fase de cierre y amplitud de cierre de un conjunto de 6 estaciones.

Datos: ninguna constante fisica. El cielo (una fuente de 1,0 Jy en el centro y otra de 0,5 Jy desplazada), las posiciones de las estaciones y las ganancias son
SINTETICOS e ILUSTRATIVOS (semilla 20261109).
Modelo: V_ij = g_i conj(g_j) M_ij + ruido. Fase de cierre del triangulo (i,j,k) = arg(V_ij V_jk V_ki); amplitud de cierre del cuadrangulo (i,j,k,l) = |V_ij||V_kl| / (|V_ik||V_jl|).
Segunda via: la fase de cierre del modelo (sin ganancias) frente a la de los datos corrompidos; el ruido de la fase de cierre contra la formula sqrt(suma de 1/SNR^2) y un Monte Carlo.
Supuestos: ganancias complejas por estacion (no por base), ruido gaussiano independiente por base. Validez: ilustrativa.
Tolerancia: invariancia de cierres a 1e-9 sin ruido; el ruido Monte Carlo coincide con la formula dentro de 5 %.
"""
from __future__ import annotations
import cmath, math, platform, random, sys
from itertools import combinations

def compute():
    rng = random.Random(20261109)
    n = 6
    pos = [(rng.uniform(0, 3000), rng.uniform(0, 3000)) for _ in range(n)]   # en longitudes de onda
    src = [(1.0, 0.0, 0.0), (0.5, 4.0e-4, 2.0e-4)]                          # (flujo, l, m)
    def model(i, j):
        u, v = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
        return sum(s * cmath.exp(-2j * math.pi * (u * l + v * m)) for s, l, m in src)
    g = [rng.lognormvariate(0, 0.2) * cmath.exp(1j * rng.gauss(0, 1.0)) for _ in range(n)]
    def vis(i, j, sig=0.0, r=rng):
        v = g[i] * g[j].conjugate() * model(i, j)
        return v + complex(r.gauss(0, sig), r.gauss(0, sig)) if sig else v
    tri = list(combinations(range(n), 3))
    quad = [(i, j, k, l) for (i, j, k, l) in combinations(range(n), 4)]
    def vm(i, j):
        return model(i, j) if i < j else model(j, i).conjugate()
    def vd(i, j, sig=0.0, r=rng):
        return vis(i, j, sig, r) if i < j else vis(j, i, sig, r).conjugate()
    cp_d = [cmath.phase(vd(i, j) * vd(j, k) * vd(k, i)) for i, j, k in tri]
    cp_m = [cmath.phase(vm(i, j) * vm(j, k) * vm(k, i)) for i, j, k in tri]
    dcp = max(abs(cmath.phase(cmath.exp(1j * (a - b)))) for a, b in zip(cp_d, cp_m))
    def ca(f, i, j, k, l):
        return abs(f(i, j)) * abs(f(k, l)) / (abs(f(i, k)) * abs(f(j, l)))
    dca = max(abs(ca(vd, *q) / ca(vm, *q) - 1) for q in quad)
    R = dict(n=n, ntri=len(tri), nquad=len(quad), nind_cp=(n - 1) * (n - 2) // 2, nind_ca=n * (n - 3) // 2, dcp=dcp, dca=dca)
    # ganancia de fase tipica
    R["gphase_rms"] = math.degrees(math.sqrt(sum(cmath.phase(x) ** 2 for x in g) / n))
    # ruido de la fase de cierre
    sig = 0.15
    t0 = tri[0]
    i, j, k = t0
    amps = [abs(vm(i, j)), abs(vm(j, k)), abs(vm(k, i))]
    pred = math.sqrt(sum((sig / (a * abs(g[x]) * abs(g[y]))) ** 2 for a, (x, y) in zip(amps, [(i, j), (j, k), (k, i)])))
    vals = []
    r2 = random.Random(20261109)
    for _ in range(20000):
        vals.append(cmath.phase(vd(i, j, sig, r2) * vd(j, k, sig, r2) * vd(k, i, sig, r2)) - cp_m[0])
    vals = [math.atan2(math.sin(v), math.cos(v)) for v in vals]
    mu = sum(vals) / len(vals)
    sd = math.sqrt(sum((v - mu) ** 2 for v in vals) / (len(vals) - 1))
    R.update(sig=sig, pred_cp=math.degrees(pred), mc_cp=math.degrees(sd), tri0=t0, amps=amps)
    R["cp_model_deg"] = [math.degrees(x) for x in cp_m[:4]]
    R["cp_data_deg"] = [math.degrees(x) for x in cp_d[:4]]
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"estaciones = {R['n']} ; triangulos = {R['ntri']} (independientes {R['nind_cp']}) ; cuadrangulos = {R['nquad']} (amplitudes independientes {R['nind_ca']})")
    print(f"rms de la fase de ganancia por estacion = {R['gphase_rms']:.1f} grados")
    for a, b in zip(R["cp_model_deg"], R["cp_data_deg"]):
        print(f"  fase de cierre: modelo {a:+9.4f} grados ; datos con ganancias {b:+9.4f} grados")
    print(f"max |cierre de fase datos - modelo| = {R['dcp']:.2e} rad ; max |cierre de amplitud datos/modelo - 1| = {R['dca']:.2e}")
    assert R["dcp"] < 1e-9 and R["dca"] < 1e-9
    print(f"ruido de la fase de cierre (triangulo {R['tri0']}): formula = {R['pred_cp']:.3f} grados ; Monte Carlo = {R['mc_cp']:.3f} grados")
    assert abs(R["mc_cp"] / R["pred_cp"] - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
