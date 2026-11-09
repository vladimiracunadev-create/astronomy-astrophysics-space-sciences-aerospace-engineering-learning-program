#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C07: residuos de una calibracion, chi cuadrado reducido, residuos normalizados y localizacion de problemas.

Datos: ninguna constante fisica. Cielo de dos fuentes puntuales (1,0 y 0,4 Jy), 10 antenas, ganancias y ruido SINTETICOS e ILUSTRATIVOS (semilla 20261109).
Modelo: tras resolver las ganancias, r_ij = V_ij - g_i conj(g_j) M_ij; z = r/sigma por componente real e imaginaria; chi2_red = suma(z^2) / dof con dof = 2 N_bases - (2 N - 1).
Segunda via: la media y la desviacion esperadas del chi2_red (1 y sqrt(2/dof)) frente a un Monte Carlo; la cola gaussiana P(|z|>4) = erfc(4/sqrt 2) frente a la frecuencia observada.
Supuestos: ruido gaussiano de sigma conocida; ganancias de un parametro complejo por antena. Validez: ilustrativa.
Tolerancia: media de chi2_red dentro de 3 errores estandar de 1; dispersion dentro de 15 % de lo esperado; el modelo incompleto y el valor atipico se detectan.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def stefcal(n, V, M, iters=80):
    g = [1 + 0j] * n
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
    return g

def resid(n, V, M, sig):
    g = stefcal(n, V, M)
    z = {}
    for (i, j) in V:
        r = V[(i, j)] - g[i] * g[j].conjugate() * M[(i, j)]
        z[(i, j)] = (r.real / sig, r.imag / sig)
    return z

def compute():
    rng = random.Random(20261109)
    n = 10
    x = [(rng.uniform(0, 2000), rng.uniform(0, 2000)) for _ in range(n)]
    base = [(i, j) for i in range(n) for j in range(i + 1, n)]
    def vis_of(srcs):
        return {(i, j): sum(s * cmath.exp(-2j * math.pi * ((x[j][0] - x[i][0]) * l + (x[j][1] - x[i][1]) * m)) for s, l, m in srcs) for (i, j) in base}
    sky = [(1.0, 0.0, 0.0), (0.4, 6.0e-4, 3.0e-4)]
    Mt = vis_of(sky)
    gt = [rng.lognormvariate(0, 0.1) * cmath.exp(1j * rng.gauss(0, 0.7)) for _ in range(n)]
    sig = 0.03
    dof = 2 * len(base) - (2 * n - 1)
    def data(extra=None):
        d = {b: gt[b[0]] * gt[b[1]].conjugate() * Mt[b] + complex(rng.gauss(0, sig), rng.gauss(0, sig)) for b in base}
        if extra:
            d[extra[0]] += extra[1]
        return d
    def chi2(z):
        return sum(a * a + b * b for a, b in z.values()) / dof
    vals = [chi2(resid(n, data(), Mt, sig)) for _ in range(300)]
    mu = sum(vals) / len(vals)
    sd = math.sqrt(sum((v - mu) ** 2 for v in vals) / (len(vals) - 1))
    R = dict(n=n, nbase=len(base), dof=dof, sig=sig, chi_mu=mu, chi_sd=sd, chi_sd_pred=math.sqrt(2 / dof))
    # modelo incompleto
    Mi = vis_of([sky[0]])
    R["chi_inc"] = chi2(resid(n, data(), Mi, sig))
    # valor atipico de 10 sigma en la base (2,7)
    z = resid(n, data(((2, 7), complex(10 * sig, 0))), Mt, sig)
    R["chi_out"] = chi2(z)
    mx = max(z, key=lambda b: max(abs(z[b][0]), abs(z[b][1])))
    R["out_base"] = mx; R["out_z"] = max(abs(z[mx][0]), abs(z[mx][1]))
    # cola gaussiana
    cnt = tot = 0
    for _ in range(300):
        for a, b in resid(n, data(), Mt, sig).values():
            tot += 2
            cnt += (abs(a) > 3) + (abs(b) > 3)
    R["s"] = math.sqrt(dof / (2 * len(base))); R["tail_obs"] = cnt / tot; R["tail_naive"] = math.erfc(3 / math.sqrt(2)); R["tail_th"] = math.erfc(3 / (R["s"] * math.sqrt(2)))
    # curtosis exceso
    zs = []
    for _ in range(100):
        for a, b in resid(n, data(), Mt, sig).values():
            zs += [a, b]
    m = sum(zs) / len(zs); v = sum((q - m) ** 2 for q in zs) / len(zs)
    R["skew"] = sum((q - m) ** 3 for q in zs) / len(zs) / v ** 1.5
    R["kurt"] = sum((q - m) ** 4 for q in zs) / len(zs) / v ** 2 - 3
    R["z_sd"] = math.sqrt(v)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"antenas = {R['n']} ; bases = {R['nbase']} ; grados de libertad = {R['dof']} ; sigma = {R['sig']} Jy")
    print(f"chi2 reducido (300 ensayos): media = {R['chi_mu']:.4f} ; desviacion = {R['chi_sd']:.4f} ; esperada sqrt(2/dof) = {R['chi_sd_pred']:.4f}")
    assert abs(R["chi_mu"] - 1) < 3 * R["chi_sd_pred"] / math.sqrt(300) and abs(R["chi_sd"] / R["chi_sd_pred"] - 1) < 0.15
    print(f"modelo incompleto (solo la fuente de 1,0 Jy): chi2 reducido = {R['chi_inc']:.2f}")
    assert R["chi_inc"] > 3
    print(f"valor atipico de 10 sigma en la base (2, 7): chi2 reducido = {R['chi_out']:.3f} ; mayor |z| = {R['out_z']:.2f} en la base {R['out_base']}")
    assert R["out_base"] == (2, 7) and R["out_z"] > 5
    print(f"cola |z| > 3: observada = {R['tail_obs']:.5f} ; gaussiana ingenua = {R["tail_naive"]:.5f} ; gaussiana con sigma reducida {R["s"]:.4f} = {R["tail_th"]:.5f}")
    assert abs(R["tail_obs"] / R["tail_th"] - 1) < 0.2
    print(f"desviacion de z = {R['z_sd']:.4f} ; asimetria = {R['skew']:+.4f} ; curtosis en exceso = {R['kurt']:+.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
