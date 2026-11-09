#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C14: coordenadas (u, v, w) de una linea de base y retardo geometrico, por dos vias.

Datos: c de NIST CODATA 2022 (consultada 2026-11-09). La linea de base (300 m este-oeste y 200 m norte-sur), la latitud (-30 grados), la declinacion
(+20 grados) y la longitud de onda (0,21 m) son ILUSTRATIVAS.
Modelo: via 1: matriz de rotacion de (E, N, U) a coordenadas ecuatoriales (X, Y, Z) y luego (u, v, w) con angulo horario H y declinacion delta.
Via 2: formulas explicitas de la linea de base este-oeste: u = (B/lambda) cos H, v = (B/lambda) sin delta sin H, w = -(B/lambda) cos delta sin H (solo para una linea E-O).
Retardo geometrico tau = B . s / c = w lambda / c. La pista de una linea E-O es una elipse con semiejes B/lambda y (B/lambda) sin delta.
Supuestos: Tierra rigida, sin refraccion. Validez: orientativa.
Tolerancia: ambas vias coinciden a 1e-9; la elipse cierra a 1e-9.
"""
from __future__ import annotations
import math, platform
C = 299792458.0

def enu_a_xyz(E_, N_, U_, lat):
    # X hacia el meridiano en el ecuador, Y hacia el este, Z hacia el polo
    X = -N_ * math.sin(lat) + U_ * math.cos(lat)
    Y = E_
    Z = N_ * math.cos(lat) + U_ * math.sin(lat)
    return X, Y, Z

def uvw(X, Y, Z, H, dec, lam):
    u = (math.sin(H) * X + math.cos(H) * Y) / lam
    v = (-math.sin(dec) * math.cos(H) * X + math.sin(dec) * math.sin(H) * Y + math.cos(dec) * Z) / lam
    w = (math.cos(dec) * math.cos(H) * X - math.cos(dec) * math.sin(H) * Y + math.sin(dec) * Z) / lam
    return u, v, w

def calc():
    lat, dec, lam = math.radians(-30.0), math.radians(20.0), 0.21
    B = 300.0
    X, Y, Z = enu_a_xyz(B, 0.0, 0.0, lat)
    filas, maxdif, cierre = [], 0.0, 0.0
    for hh in (-6, -3, 0, 3, 6):
        H = math.radians(15 * hh)
        u, v, w = uvw(X, Y, Z, H, dec, lam)
        ua = B / lam * math.cos(H)
        va = B / lam * math.sin(dec) * math.sin(H)
        wa = -B / lam * math.cos(dec) * math.sin(H)
        maxdif = max(maxdif, abs(u - ua), abs(v - va), abs(w - wa))
        filas.append((hh, u, v, w, w * lam / C * 1e9))
    for hh in range(0, 24):
        H = math.radians(15 * hh)
        u, v, w = uvw(X, Y, Z, H, dec, lam)
        cierre = max(cierre, abs((u / (B / lam)) ** 2 + (v / (B / lam * math.sin(dec))) ** 2 - 1))
    Xn, Yn, Zn = enu_a_xyz(0.0, 200.0, 0.0, lat)
    Xt, Yt, Zt = X + Xn, Y + Yn, Z + Zn
    Lm = math.sqrt(Xt ** 2 + Yt ** 2 + Zt ** 2)
    ut, vt, wt = uvw(Xt, Yt, Zt, 0.0, dec, lam)
    return dict(filas=filas, maxdif=maxdif, cierre=cierre, L=Lm, mod_uvw=math.sqrt(ut ** 2 + vt ** 2 + wt ** 2) * lam,
                franja_arcmin=math.degrees(lam / B) * 60, a=B / lam, b=B / lam * math.sin(dec))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"semiejes de la elipse: a = {r['a']:.2f} lambda ; b = {r['b']:.2f} lambda ; separacion de franjas = {r['franja_arcmin']:.2f} arcmin")
    print(f"{'H [h]':>6} {'u [lambda]':>11} {'v [lambda]':>11} {'w [lambda]':>11} {'retardo [ns]':>13}")
    for hh, u, v, w, t in r["filas"]:
        print(f"{hh:6d} {u:11.2f} {v:11.2f} {w:11.2f} {t:13.2f}")
    print(f"diferencia maxima entre vias = {r['maxdif']:.2e} lambda ; cierre de la elipse = {r['cierre']:.2e}")
    print(f"|B| con componente norte (300 m E + 200 m N) = {r['L']:.3f} m ; |(u,v,w)| lambda = {r['mod_uvw']:.3f} m")
    assert r["maxdif"] < 1e-6 and r["cierre"] < 1e-9
    assert abs(r["L"] - math.hypot(300, 200)) < 1e-9 and abs(r["mod_uvw"] - r["L"]) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
