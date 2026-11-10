#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C07: atenuacion por lluvia en un trayecto oblicuo (UIT-R P.838-3 y P.618-14) y ruido de cielo.

Datos consultados (2026-11-10):
  - UIT-R P.838-3 (2005): ecuaciones (1)-(5) y constantes de las Tablas 1-4 (k_H, k_V, alpha_H, alpha_V). NO consultada la Tabla 5 (valores por frecuencia).
  - UIT-R P.618-14 (2023): pasos 2-10 del procedimiento de atenuacion por lluvia (reduccion horizontal r, ajuste vertical v, escalado a otros porcentajes).
  - NASA/JPL DSN 810-005 modulo 101 rev. D (2011): ganancia X rx 74.55 dBi (DSS-14) y temperatura operacional T_op = 16.69 K en zenit (CD = 25 %).
SINTETICO / ILUSTRATIVO (no consultado): R_0.01 = 42 mm/h; altura de lluvia h_R = 3.5 km (la Rec. P.839 no se consulto); altura de la estacion h_s = 0.1 km;
  latitud 33.4 grados; temperatura media fisica de la atmosfera T_m = 275 K (ilustrativa); elevacion 30 grados; polarizacion circular (tau = 45 grados).
Segunda via / comprobaciones: (a) tau = 0 y theta = 0 reproducen k_H y tau = 90 reproduce k_V; (b) A(p = 0.01 %) del escalado = A_0.01; (c) A decrece al aumentar p;
  (d) Rec. P.618: si h_R - h_s <= 0 la atenuacion es nula; (e) T_sky = T_m (1 - 10^(-A/10)) crece con A y satura en T_m.
Tolerancias: comprobaciones a 1e-12; limite de validez de P.838: 1 a 1000 GHz; de P.618: hasta 55 GHz y elevacion >= 5 grados (aqui 30).
"""
from __future__ import annotations
import math, platform

KH = dict(a=[-5.33980, -0.35351, -0.23789, -0.94158], b=[-0.10008, 1.26970, 0.86036, 0.64552], c=[1.13098, 0.45400, 0.15354, 0.16817], m=-0.18961, cc=0.71147)
KV = dict(a=[-3.80595, -3.44965, -0.39902, 0.50167], b=[0.56934, -0.22911, 0.73042, 1.07319], c=[0.81061, 0.51059, 0.11899, 0.27195], m=-0.16398, cc=0.63297)
AH = dict(a=[-0.14318, 0.29591, 0.32177, -5.37610, 16.1721], b=[1.82442, 0.77564, 0.63773, -0.96230, -3.29980], c=[-0.55187, 0.19822, 0.13164, 1.47828, 3.43990], m=0.67849, cc=-1.95537)
AV = dict(a=[-0.07771, 0.56727, -0.20238, -48.2991, 48.5833], b=[2.33840, 0.95545, 1.14520, 0.791669, 0.791459], c=[-0.76284, 0.54039, 0.26809, 0.116226, 0.116479], m=-0.053739, cc=0.83433)


def serie(t, f):
    lf = math.log10(f)
    return sum(a * math.exp(-(((lf - b) / c) ** 2)) for a, b, c in zip(t["a"], t["b"], t["c"])) + t["m"] * lf + t["cc"]


def coef(f, theta_deg, tau_deg):
    kh, kv = 10 ** serie(KH, f), 10 ** serie(KV, f)
    ah, av = serie(AH, f), serie(AV, f)
    c2 = math.cos(math.radians(theta_deg)) ** 2
    c2t = math.cos(2 * math.radians(tau_deg))
    k = (kh + kv + (kh - kv) * c2 * c2t) / 2
    a = (kh * ah + kv * av + (kh * ah - kv * av) * c2 * c2t) / (2 * k)
    return k, a, kh, kv, ah, av


def lluvia_p618(f, theta_deg, tau_deg, r001, hr, hs, lat_deg, p):
    if hr - hs <= 0 or r001 <= 0:
        return 0.0, 0.0, 0.0, 0.0
    th = math.radians(theta_deg)
    ls = (hr - hs) / math.sin(th)  # theta >= 5 grados
    lg = ls * math.cos(th)
    k, a, *_ = coef(f, theta_deg, tau_deg)
    gam = k * r001 ** a
    r = 1 / (1 + 0.78 * math.sqrt(lg * gam / f) - 0.38 * (1 - math.exp(-2 * lg)))
    zeta = math.degrees(math.atan((hr - hs) / (lg * r)))
    lr = lg * r / math.cos(th) if zeta > theta_deg else (hr - hs) / math.sin(th)
    chi = 36 - abs(lat_deg) if abs(lat_deg) < 36 else 0.0
    v = 1 / (1 + math.sqrt(math.sin(th)) * (31 * (1 - math.exp(-theta_deg / (1 + chi))) * math.sqrt(lr * gam) / f ** 2 - 0.45))
    le = lr * v
    a001 = gam * le
    if p >= 1.0 or abs(lat_deg) >= 36:
        beta = 0.0
    elif theta_deg >= 25:
        beta = -0.005 * (abs(lat_deg) - 36)
    else:
        beta = -0.005 * (abs(lat_deg) - 36) + 1.8 - 4.25 * math.sin(th)
    ap = a001 * (p / 0.01) ** (-(0.655 + 0.033 * math.log(p) - 0.045 * math.log(a001) - beta * (1 - p) * math.sin(th)))
    return gam, le, a001, ap


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # comprobacion (a)
    k0, a0, kh, kv, ah, av = coef(20.0, 0.0, 0.0)
    k90, a90, *_ = coef(20.0, 0.0, 90.0)
    assert abs(k0 - kh) < 1e-12 and abs(k90 - kv) < 1e-12 and abs(a0 - ah) < 1e-12 and abs(a90 - av) < 1e-12
    print("Comprobacion (a): tau = 0 -> k_H, alpha_H ; tau = 90 -> k_V, alpha_V (identidad de las ecuaciones 4 y 5).")
    print("Coeficientes calculados con las ecuaciones (2)-(3) y las Tablas 1-4 (el contraste con la Tabla 5 NO se hizo: no consultada)")
    print("  f [GHz]    k_H        k_V        alpha_H   alpha_V   k (circ, 30 grad)  alpha")
    for f in (2.2, 8.4, 20.0, 32.0, 40.0):
        k, a, kh, kv, ah, av = coef(f, 30.0, 45.0)
        print(f"  {f:6.1f}  {kh:10.6f} {kv:10.6f}  {ah:8.4f}  {av:8.4f}   {k:10.6f}      {a:7.4f}")
        assert 0.5 < ah < 1.8 and 0.5 < av < 1.8
    R, hr, hs, lat, th = 42.0, 3.5, 0.1, 33.4, 30.0
    print(f"Entradas SINTETICAS: R_0.01 = {R} mm/h, h_R = {hr} km, h_s = {hs} km, latitud {lat} grados, elevacion {th} grados, polarizacion circular")
    print("  f [GHz]  gamma_R [dB/km]  L_E [km]  A_0.01 [dB]  A_1% [dB]  A_0.1% [dB]  A_0.001% [dB]")
    filas = {}
    for f in (2.2, 8.4, 20.0, 32.0, 40.0):
        g, le, a001, _ = lluvia_p618(f, th, 45.0, R, hr, hs, lat, 0.01)
        ps = [lluvia_p618(f, th, 45.0, R, hr, hs, lat, p)[3] for p in (1.0, 0.1, 0.001)]
        filas[f] = (a001, ps)
        print(f"  {f:6.1f}   {g:10.4f}     {le:7.3f}   {a001:9.3f}   {ps[0]:8.3f}   {ps[1]:9.3f}    {ps[2]:10.3f}")
        # (b) y (c)
        assert abs(lluvia_p618(f, th, 45.0, R, hr, hs, lat, 0.01)[3] - a001) < 1e-12
        assert ps[0] < lluvia_p618(f, th, 45.0, R, hr, hs, lat, 0.01)[3] < ps[1] < ps[2] or ps[0] < ps[1] < ps[2]
    assert lluvia_p618(20.0, th, 45.0, R, 0.05, 0.1, lat, 0.01)[3] == 0.0
    print("Comprobaciones (b), (c) y (d) superadas.")
    print("Ruido de cielo por lluvia (T_m = 275 K ILUSTRATIVA) y efecto sobre G/T de la antena de 70 m en X (G = 74.55 dBi, T_op = 16.69 K, DSN, zenit 25 %)")
    print("  A [dB]   T_sky_lluvia [K]   T_sys [K]   G/T [dB/K]   perdida de G/T respecto de cielo claro [dB]  (la antena ve ademas la atenuacion A en la senal)")
    gt0 = 74.55 - 10 * math.log10(16.69)
    prev = -1.0
    for A in (0.0, 0.5, 1.0, 3.0, 6.0, 10.0):
        ts = 275.0 * (1 - 10 ** (-A / 10))
        assert ts > prev or A == 0.0
        prev = ts
        tsys = 16.69 + ts
        gt = 74.55 - 10 * math.log10(tsys)
        print(f"  {A:5.1f}     {ts:9.2f}        {tsys:8.2f}    {gt:8.2f}        {gt0-gt:8.2f}  (+ {A:.1f} dB en la senal -> {gt0-gt+A:.2f} dB de perdida de C/N0)")
    print(f"G/T con cielo claro = {gt0:.2f} dB/K (calculado de dos valores publicados; no es un valor publicado de G/T)")
    assert 275.0 * (1 - 10 ** (-60 / 10)) < 275.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
