#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C13: montura altacimutal: velocidades de acimut y altura, rotacion de campo y zona ciega del cenit.

Datos: ILUSTRATIVOS (latitud -30,0 grados, estrella de declinacion -10 grados, velocidad maxima de acimut de la montura 1 grado/s). Velocidad angular de la Tierra omega = 2 pi/86164,0905 s (dia sideral calculado en C12 con el ano tropico de 365,2422 dias).
Modelo: vector unitario de la estrella en el horizonte (Este, Norte, Cenit): s = (-cos d sin H, sin d cos f - cos d cos H sin f, sin d sin f + cos d cos H cos f), alt = asin(s_cenit), az = atan2(s_este, s_norte).
Velocidades: derivacion por diferencias finitas centrales (dt = 1 s) frente a la derivada vectorial ds/dt = -omega p x s con p = (0, cos f, sin f); rotacion de campo (angulo paralactico q) frente a -omega cos f cos(az)/cos(alt) (el signo depende de la convencion de q usada aqui: q = atan2(sin H, tan f cos d - sin d cos H)).
Zona ciega: radio cenital minimo eps = omega cos f / v_max (aproximacion de trayectoria recta), contrastado con la busqueda numerica de la velocidad de acimut maxima en un transito a distancia cenital dada.
Supuestos: refraccion y flexion ignoradas, montura ideal. Validez: eps pequeno.
Tolerancia: diferencias finitas frente a derivada vectorial, 1e-6 relativo; zona ciega, 2 %.
"""
from __future__ import annotations
import math, platform

OM = 2 * math.pi / 86164.0905
PHI = math.radians(-30.0); DEC = math.radians(-10.0)

def vec(H, dec=DEC, phi=PHI):
    return (-math.cos(dec) * math.sin(H), math.sin(dec) * math.cos(phi) - math.cos(dec) * math.cos(H) * math.sin(phi),
            math.sin(dec) * math.sin(phi) + math.cos(dec) * math.cos(H) * math.cos(phi))

def altaz(H, dec=DEC, phi=PHI):
    s = vec(H, dec, phi)
    return math.asin(s[2]), math.atan2(s[0], s[1])

def parallactic(H, dec=DEC, phi=PHI):
    return math.atan2(math.sin(H), math.tan(phi) * math.cos(dec) - math.sin(dec) * math.cos(H))

def unwrap(d):
    while d > math.pi: d -= 2 * math.pi
    while d < -math.pi: d += 2 * math.pi
    return d

def fd(f, H, dt=1.0):
    a = f(H + OM * dt); b = f(H - OM * dt)
    return unwrap(a - b) / (2 * dt)

def tasa_vectorial(H, dec=DEC, phi=PHI):
    s = vec(H, dec, phi); p = (0.0, math.cos(phi), math.sin(phi))
    # el cielo gira hacia el oeste: ds/dt = -omega * p x s
    cx = (p[1] * s[2] - p[2] * s[1], p[2] * s[0] - p[0] * s[2], p[0] * s[1] - p[1] * s[0])
    ds = (-OM * cx[0], -OM * cx[1], -OM * cx[2])
    h = math.asin(s[2]); cosh = math.cos(h)
    dh = ds[2] / cosh
    # d(az)/dt = (s_n ds_e - s_e ds_n)/(s_e^2 + s_n^2)
    dA = (s[1] * ds[0] - s[0] * ds[1]) / (s[0] ** 2 + s[1] ** 2)
    return dh, dA

def calc():
    r = {}
    filas = []
    for Hh in (-4.0, -2.0, -0.5, 0.5, 2.0, 4.0):
        H = Hh * math.pi / 12
        h, A = altaz(H)
        dh, dA = tasa_vectorial(H)
        dh_f = fd(lambda x: altaz(x)[0], H); dA_f = fd(lambda x: altaz(x)[1], H)
        dq_f = fd(parallactic, H)
        dq_a = -OM * math.cos(PHI) * math.cos(A) / math.cos(h)
        filas.append((Hh, math.degrees(h), math.degrees(A) % 360, math.degrees(dA) * 3600, math.degrees(dh) * 3600, dh_f / dh - 1 if dh else 0, dA_f / dA - 1, math.degrees(dq_a) * 3600, dq_f / dq_a - 1))
    r["filas"] = filas
    vmax = math.radians(1.0)
    r["eps_formula_deg"] = math.degrees(OM * math.cos(PHI) / vmax)
    # busqueda numerica: declinacion tal que la distancia cenital minima sea eps, maximo de |dA/dt| en el transito
    eps = OM * math.cos(PHI) / vmax
    dec_e = PHI + eps  # distancia cenital minima al pasar por el meridiano
    mx = 0.0
    for k in range(-20000, 20001):
        H = k * 2e-5
        dA = tasa_vectorial(H, dec_e)[1]
        mx = max(mx, abs(dA))
    r["vel_az_max_deg_s"] = math.degrees(mx)
    r["vel_az_transito_cenit_1arcmin"] = None
    mx2 = 0.0
    dec2 = PHI + math.radians(1.0 / 60)
    for k in range(-20000, 20001):
        mx2 = max(mx2, abs(tasa_vectorial(k * 2e-5, dec2)[1]))
    r["vel_az_max_1arcmin_deg_s"] = math.degrees(mx2)
    r["vel_az_formula_1arcmin_deg_s"] = math.degrees(OM * math.cos(PHI) / math.radians(1.0 / 60))
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("H (h) | alt (deg) | az (deg) | dAz/dt (\"/s) | dAlt/dt (\"/s) | dif rel alt | dif rel az | dq/dt (\"/s) | dif rel q")
    for f in r["filas"]:
        print(f"{f[0]:+.1f} | {f[1]:.3f} | {f[2]:.3f} | {f[3]:.3f} | {f[4]:.3f} | {f[5]:.1e} | {f[6]:.1e} | {f[7]:.3f} | {f[8]:.1e}")
    for k in ("eps_formula_deg", "vel_az_max_deg_s", "vel_az_max_1arcmin_deg_s", "vel_az_formula_1arcmin_deg_s"):
        print(f"{k} = {r[k]:.6g}")
    for f in r["filas"]:
        assert abs(f[5]) < 1e-6 and abs(f[6]) < 1e-6 and abs(f[8]) < 1e-6
    assert abs(r["vel_az_max_deg_s"] - 1.0) < 0.02
    assert abs(r["vel_az_max_1arcmin_deg_s"] / r["vel_az_formula_1arcmin_deg_s"] - 1) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
