#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C16: polarimetro de placa de media onda rotante, demodulacion y sesgo de la polarizacion.

Datos: nada medido. El estado de entrada (q, u) y la polarizacion instrumental (0,005; -0,002) son SINTETICOS e ILUSTRATIVOS; los conteos llevan ruido de fotones (gaussiano) con semilla 20261109.
El sesgo de la polarizacion se describe en la literatura (Plaszczynski et al., arXiv:1312.0437; Montier et al., arXiv:1406.6536): solo se leyeron los extractos de una busqueda web del 2026-11-09; nada
de esas cifras se usa aqui. Las formulas de Rayleigh y Rice son resultados estadisticos estandar que se verifican por integracion numerica.
Modelo: placa de media onda a theta_k = k 22,5 grados (k = 0..7) y analizador fijo: I_k = (I + Q cos 4 theta_k + U sin 4 theta_k)/2; Q = (4/K) sum I_k cos 4 theta_k, U analogo.
Supuestos: placa ideal, ruido de fotones, polarizacion instrumental aditiva y conocida. Validez: sin cromatismo ni errores de angulo.
Tolerancia: el ruido de q y u por Monte Carlo coincide con sqrt(2/N) a 3 %; el sesgo medio de P con P verdadero nulo coincide con sigma sqrt(pi/2) a 3 %; el valor de Rice por integracion a 3 %.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
K = 8
TH = [math.radians(22.5 * k) for k in range(K)]


def modelo(Itot, q, u):
    return [0.5 * Itot * (1 + q * math.cos(4 * t) + u * math.sin(4 * t)) / 1.0 * (1.0 / 1.0) / 1.0 for t in TH]


def demod(ik):
    I = 2.0 / K * sum(ik)
    Q = 4.0 / K * sum(i * math.cos(4 * t) for i, t in zip(ik, TH))
    U = 4.0 / K * sum(i * math.sin(4 * t) for i, t in zip(ik, TH))
    return I, Q / I, U / I


def i0(x):
    s, t, k = 1.0, 1.0, 1
    while t > 1e-17 * s:
        t *= (x / (2 * k)) ** 2
        s += t
        k += 1
    return s


def rice_media(nu, sigma=1.0):
    """Media de P con pdf de Rice, por integracion numerica."""
    n = 6000
    pmax = nu + 10 * sigma
    h = pmax / n
    num = 0.0
    den = 0.0
    for i in range(n + 1):
        p = i * h
        pdf = (p / sigma ** 2) * math.exp(-(p * p + nu * nu) / (2 * sigma ** 2) + 0) * i0(p * nu / sigma ** 2) if p * nu / sigma ** 2 < 600 else 0.0
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        num += w * p * pdf
        den += w * pdf
    return num / den


def calcular():
    rnd = random.Random(SEMILLA)
    r = {}
    q0, u0 = 0.03, -0.01
    Ntot = 4.0e6                       # conteos totales sobre los 8 angulos
    sigma_pred = math.sqrt(2.0 / Ntot)
    r["sigma_pred"] = sigma_pred
    r["q0"], r["u0"] = q0, u0
    ik0 = [Ntot / K * (1 + q0 * math.cos(4 * t) + u0 * math.sin(4 * t)) for t in TH]
    qs, us = [], []
    inst = (0.005, -0.002)
    for _ in range(4000):
        ik = [rnd.gauss(m, math.sqrt(m)) for m in ik0]
        I, q, u = demod(ik)
        qs.append(q + inst[0])
        us.append(u + inst[1])
    mq = sum(qs) / len(qs)
    mu = sum(us) / len(us)
    r["mq"], r["mu"] = mq, mu
    r["sq"] = math.sqrt(sum((a - mq) ** 2 for a in qs) / (len(qs) - 1))
    r["su"] = math.sqrt(sum((a - mu) ** 2 for a in us) / (len(us) - 1))
    r["q_corr"], r["u_corr"] = mq - inst[0], mu - inst[1]
    r["P_ver"] = math.hypot(q0, u0)
    r["chi_ver"] = 0.5 * math.degrees(math.atan2(u0, q0))
    r["chi_med"] = 0.5 * math.degrees(math.atan2(r["u_corr"], r["q_corr"]))
    # sesgo con P verdadero 0, 1, 2, 3, 5 sigma
    sig = 0.002
    filas = []
    for nu_sig in (0.0, 1.0, 2.0, 3.0, 5.0):
        ps = []
        for _ in range(20000):
            a = rnd.gauss(nu_sig * sig, sig)
            b = rnd.gauss(0.0, sig)
            ps.append(math.hypot(a, b))
        m = sum(ps) / len(ps)
        deb = [math.sqrt(max(p * p - sig * sig, 0.0)) for p in ps]
        md = sum(deb) / len(deb)
        filas.append((nu_sig, m / sig, rice_media(nu_sig), md / sig))
    r["sesgo"] = filas
    r["rayleigh"] = math.sqrt(math.pi / 2)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"ruido previsto por componente = sqrt(2/N) = {r['sigma_pred']*100:.4f} % (N = 4e6) ; Monte Carlo: sigma_q = {r['sq']*100:.4f} %, sigma_u = {r['su']*100:.4f} %")
    print(f"q medido {r['mq']:+.5f}, u medido {r['mu']:+.5f} (con polarizacion instrumental +0.005, -0.002) ; corregidos: q = {r['q_corr']:+.5f}, u = {r['u_corr']:+.5f} ; verdaderos {r['q0']:+.5f}, {r['u0']:+.5f}")
    print(f"P verdadero = {r['P_ver']*100:.4f} % ; angulo verdadero = {r['chi_ver']:.3f} grados ; angulo recuperado = {r['chi_med']:.3f} grados")
    print(f"{'P/sigma':>8} {'media P/sigma MC':>17} {'Rice (integral)':>16} {'P sin sesgo/sigma':>19}")
    for nu, m, ri, md in r["sesgo"]:
        print(f"{nu:8.1f} {m:17.4f} {ri:16.4f} {md:19.4f}")
    print(f"Rayleigh: sqrt(pi/2) = {r['rayleigh']:.4f}")
    assert abs(r["sq"] / r["sigma_pred"] - 1) < 0.03 and abs(r["su"] / r["sigma_pred"] - 1) < 0.03
    assert abs(r["q_corr"] - r["q0"]) < 4 * r["sq"] / math.sqrt(4000) and abs(r["u_corr"] - r["u0"]) < 4 * r["su"] / math.sqrt(4000)
    nu, m, ri, md = r["sesgo"][0]
    assert abs(m / r["rayleigh"] - 1) < 0.03 and abs(ri / r["rayleigh"] - 1) < 1e-3
    for nu, m, ri, md in r["sesgo"]:
        assert abs(m / ri - 1) < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
