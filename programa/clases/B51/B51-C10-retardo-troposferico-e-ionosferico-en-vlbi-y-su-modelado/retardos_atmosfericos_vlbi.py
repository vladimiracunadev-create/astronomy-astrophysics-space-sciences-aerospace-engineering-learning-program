#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C10: retardo troposferico (funcion de mapeo y retardo cenital humedo) e ionosferico (combinacion libre de ionosfera) en VLBI.

Datos: constantes de NIST CODATA 2022 (e, m_e, epsilon_0, c; consultadas el 2026-11-09) para la constante del retardo dispersivo K ~ 40,3 m^3/s^2. El radio terrestre (6371 km), las alturas
de capa, la refractividad (N0 = 280 unidades, escala de 8 km), el retardo cenital humedo (0,10 m), el TEC (30 TECU), las bandas S/X (2,3 y 8,4 GHz) y los ruidos son
SINTETICOS e ILUSTRATIVOS (semilla 20261109); no son un modelo troposferico operativo ni sus coeficientes.
Modelo: (a) funcion de mapeo de capa esferica m = 1/sqrt(1 - (R cos e / (R + H))^2) frente a 1/sin e y frente a la integral numerica del camino recto en una atmosfera exponencial;
(b) ajuste por minimos cuadrados del retardo cenital humedo con observaciones a varias elevaciones; (c) tau_libre = (nu1^2 tau1 - nu2^2 tau2) / (nu1^2 - nu2^2).
Segunda via: la integral numerica contra la formula de capa; el ruido de la combinacion libre frente a su amplificacion analitica sqrt(nu1^4 + nu2^4)/(nu1^2 - nu2^2) y un Monte Carlo.
Supuestos: camino recto (sin curvatura del rayo, valido por encima de unos 10 grados), simetria esferica, ruido gaussiano. Validez: ilustrativa.
Tolerancia: integral cenital a 1e-6 del valor analitico N0 H0; mapeo numerico y de capa dentro de 1 % a 20 grados; combinacion libre exacta a 1e-12 sin ruido.
"""
from __future__ import annotations
import math, platform, random, sys

E = 1.602176634e-19; ME = 9.1093837139e-31; EPS0 = 8.8541878188e-12; C = 299792458.0
RT = 6371e3

def delay_numeric(elev_deg, n0=280e-6, h0=8000.0, smax=400e3, steps=40000):
    e = math.radians(elev_deg)
    ds = smax / steps
    tot = 0.0
    for k in range(steps + 1):
        s = k * ds
        h = math.sqrt(RT * RT + 2 * RT * s * math.sin(e) + s * s) - RT
        w = 1 if k in (0, steps) else (4 if k % 2 else 2)
        tot += w * n0 * math.exp(-h / h0)
    return tot * ds / 3

def shell(elev_deg, H):
    e = math.radians(elev_deg)
    return 1 / math.sqrt(1 - (RT * math.cos(e) / (RT + H)) ** 2)

def solve_ls(els, d, sig_rng):
    ms = [1 / math.sin(math.radians(e)) for e in els]
    return sum(m * x for m, x in zip(ms, d)) / sum(m * m for m in ms)

def compute():
    rng = random.Random(20261109)
    K = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME)
    R = dict(K=K)
    zen = delay_numeric(90.0, steps=4000)
    R["zen_num"] = zen; R["zen_an"] = 280e-6 * 8000.0
    R["rows"] = []
    for e in (90, 30, 20, 10, 5):
        mn = delay_numeric(float(e)) / zen
        R["rows"].append((e, 1 / math.sin(math.radians(e)), shell(e, 8000.0), mn))
    R["rows"] = [tuple(r) for r in R["rows"]]
    # ajuste del retardo cenital humedo
    zwd = 0.10; sig = 0.005
    els = [90, 60, 45, 30, 20, 15, 10]
    ms = [shell(e, 8000.0) for e in els]
    est = []
    for _ in range(3000):
        d = [zwd * m + rng.gauss(0, sig) for m in ms]
        est.append(sum(m * x for m, x in zip(ms, d)) / sum(m * m for m in ms))
    mu = sum(est) / len(est)
    R.update(zwd=zwd, sig=sig, zwd_mu=mu, zwd_sd=math.sqrt(sum((v - mu) ** 2 for v in est) / (len(est) - 1)), zwd_pred=sig / math.sqrt(sum(m * m for m in ms)))
    # ionosfera S/X
    tec = 30e16
    n1, n2 = 2.3e9, 8.4e9
    t1 = K * tec / (C * n1 ** 2); t2 = K * tec / (C * n2 ** 2)
    tau_geo = 12.345678e-9
    a1, a2 = tau_geo + t1, tau_geo + t2
    libre = (n1 ** 2 * a1 - n2 ** 2 * a2) / (n1 ** 2 - n2 ** 2)
    R.update(t1=t1, t2=t2, libre_err=libre - tau_geo, tec_s=30.0)
    sg = 0.02e-9
    ls = []
    for _ in range(4000):
        b1 = a1 + rng.gauss(0, sg); b2 = a2 + rng.gauss(0, sg)
        ls.append((n1 ** 2 * b1 - n2 ** 2 * b2) / (n1 ** 2 - n2 ** 2) - tau_geo)
    mu2 = sum(ls) / len(ls)
    R.update(sg=sg, lib_sd=math.sqrt(sum((v - mu2) ** 2 for v in ls) / (len(ls) - 1)), amp=math.sqrt(n1 ** 4 + n2 ** 4) / (n2 ** 2 - n1 ** 2))
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"K = {R['K']:.4f} m^3/s^2 ; integral cenital numerica = {R['zen_num']:.6f} m ; analitica N0 H0 = {R['zen_an']:.6f} m")
    assert abs(R["zen_num"] - R["zen_an"]) < 1e-6 * R["zen_an"] + 1e-5
    print("elev [gr]   1/sin e   capa H=8 km   integral numerica")
    for e, a, b, c in R["rows"]:
        print(f"{e:9d} {a:9.4f} {b:13.4f} {c:19.4f}")
    r20 = [r for r in R["rows"] if r[0] == 20][0]
    assert abs(r20[2] / r20[3] - 1) < 0.01
    print(f"retardo cenital humedo {R['zwd']} m, ruido {R['sig']} m: media = {R['zwd_mu']:.5f} m ; desviacion MC = {R['zwd_sd']:.5f} m ; formula = {R['zwd_pred']:.5f} m")
    assert abs(R["zwd_sd"] / R["zwd_pred"] - 1) < 0.05
    print(f"retardo ionosferico (30 TECU): S (2,3 GHz) = {R['t1'] * 1e9:.4f} ns ; X (8,4 GHz) = {R['t2'] * 1e9:.4f} ns")
    print(f"combinacion libre de ionosfera sin ruido: error = {R['libre_err']:.2e} s")
    assert abs(R["libre_err"]) < 1e-12 * 1e-3 + 1e-18
    print(f"con ruido {R['sg'] * 1e9:.2f} ns por banda: desviacion MC = {R['lib_sd'] * 1e9:.4f} ns ; amplificacion analitica = {R['amp']:.4f} (-> {R['amp'] * R['sg'] * 1e9:.4f} ns)")
    assert abs(R["lib_sd"] / (R["amp"] * R["sg"]) - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
