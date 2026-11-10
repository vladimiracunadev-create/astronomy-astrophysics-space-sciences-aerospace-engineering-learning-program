#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C02: rueda rigida sobre suelo suelto (Bekker + Mohr-Coulomb), Tierra, Marte y Luna.

Datos consultados (2026-11-10): gravedad media de Marte 3.73 m/s2 y de la Luna 1.62 m/s2 (fichas NASA/NSSDC);
Tierra: g_n = 9.80665 m/s2 (NIST, CODATA 2022). ILUSTRATIVOS (sinteticos, no de un suelo real): masa del rover 1000 kg
sobre 6 ruedas (carga por rueda W = M g / 6), radio R = 0.25 m, ancho b = 0.20 m; suelo con k = 8.0e5 Pa/m^n, n = 0.8,
cohesion c = 1000 Pa, angulo de friccion 30 deg, modulo de cizalladura K = 0.01 m.
Modelo: p = k z^n (presion-hundimiento); z(theta) = R (cos theta - cos theta0); W = b R int p cos theta dtheta (carga normal en la
parte delantera del arco); tau = (c + sigma tan phi)(1 - exp(-j/K)), j = R[(theta0 - theta) - (1 - s)(sin theta0 - sin theta)];
empuje H = b R int tau cos theta dtheta; resistencia por compactacion Rc = b k z0^(n+1)/(n+1); tiro de barra DP = H - Rc.
Sistema: marco de la rueda, x en el sentido de avance, esfuerzos en Pa, fuerzas en N. Supuestos: suelo homogeneo, sin
bulldozing ni resistencia por flexion de la rueda, esfuerzo normal radial, rueda rigida.
Tolerancias: cuadratura N = 400 frente a N = 4000 < 1e-6 relativa; carga recuperada de z0 < 1e-9 relativa;
H(s) creciente y acotado por H_max.
"""
from __future__ import annotations
import math, platform

M, NR = 1000.0, 6
R, B = 0.25, 0.20
K_B, N_B, C, PHI, KS = 8.0e5, 0.8, 1000.0, math.radians(30.0), 0.01
GRAV = {"Tierra": 9.80665, "Marte": 3.73, "Luna": 1.62}


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def theta0(z0):
    return math.acos(1.0 - z0 / R)


def sigma(theta, th0):
    z = R * (math.cos(theta) - math.cos(th0))
    return K_B * max(z, 0.0) ** N_B


def carga(z0, n=400):
    th0 = theta0(z0)
    return B * R * simpson(lambda t: sigma(t, th0) * math.cos(t), 0.0, th0, n)


def hundimiento(w, n=400):
    lo, hi = 1e-6, 0.5 * R
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if carga(mid, n) < w:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def empuje(z0, s, n=400, saturado=False):
    th0 = theta0(z0)

    def f(t):
        sg = sigma(t, th0)
        if saturado:
            tau = C + sg * math.tan(PHI)
        else:
            j = R * ((th0 - t) - (1.0 - s) * (math.sin(th0) - math.sin(t)))
            tau = (C + sg * math.tan(PHI)) * (1.0 - math.exp(-max(j, 0.0) / KS))
        return tau * math.cos(t)

    return B * R * simpson(f, 0.0, th0, n)


def compactacion(z0):
    return B * K_B * z0 ** (N_B + 1) / (N_B + 1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Suelo y rover ILUSTRATIVOS: k = {K_B:.1e} Pa/m^n, n = {N_B}, c = {C:.0f} Pa, phi = 30 deg, K = {KS} m; R = {R} m, b = {B} m")
    print(" cuerpo   W [N]   z0 [mm]  theta0 [deg]  Rc [N]  H(s=0.2) [N]  DP(0.2)/W")
    res = {}
    for nom, g in GRAV.items():
        w = M * g / NR
        z0 = hundimiento(w)
        rc = compactacion(z0)
        h = empuje(z0, 0.2)
        res[nom] = (w, z0, rc, h)
        print(f"{nom:7s} {w:7.1f} {z0 * 1000:8.3f} {math.degrees(theta0(z0)):11.3f} {rc:8.3f} {h:12.3f} {(h - rc) / w:10.4f}")
    # curva de traccion de barra para Marte
    w, z0, rc, _ = res["Marte"]
    hmax = empuje(z0, 1.0, saturado=True)
    print(f"Curva de traccion de barra en Marte (W = {w:.1f} N, z0 = {z0 * 1000:.3f} mm, H_max = {hmax:.2f} N):")
    print("  s      H [N]    DP [N]   DP/W")
    prev = -1.0
    mono = True
    for s in (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 0.99):
        h = empuje(z0, s)
        mono = mono and h >= prev
        prev = h
        print(f"{s:5.2f} {h:9.3f} {h - rc:9.3f} {(h - rc) / w:7.4f}")
    assert mono and prev <= hmax
    # verificaciones
    rel_q = max(abs(empuje(res[n][1], 0.2, 400) - empuje(res[n][1], 0.2, 4000)) / res[n][3] for n in res)
    rel_w = max(abs(carga(res[n][1]) - res[n][0]) / res[n][0] for n in res)
    print(f"Cuadratura N=400 frente a N=4000: diferencia relativa maxima de H = {rel_q:.2e}")
    print(f"Carga recuperada desde z0 frente a W: error relativo maximo = {rel_w:.2e}")
    # control: hundimiento aumenta con la carga
    zs = [hundimiento(w_) for w_ in (500.0, 1000.0, 2000.0)]
    print(f"z0 para W = 500, 1000, 2000 N: {zs[0] * 1000:.3f}, {zs[1] * 1000:.3f}, {zs[2] * 1000:.3f} mm")
    assert zs[0] < zs[1] < zs[2]
    assert rel_q < 1e-6 and rel_w < 1e-9
    assert res["Luna"][1] < res["Marte"][1] < res["Tierra"][1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
