#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C12: argumento del periapsis, su mal condicionamiento cuando e -> 0 y el argumento de latitud.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 (IAU 2015 B3).
DATOS SINTETICOS (semilla 12): orbita con a = 8000 km, i = 40 grados, RAAN = 70 grados, omega = 130 grados, nu = 50 grados (ilustrativos),
excentricidades e = 0.3, 0.03, 3e-3, 3e-4, 3e-5, 3e-6. Ruido de medida SINTETICO: sigma_r = 1 m (por componente) y sigma_v = 1e-3 m/s (por componente),
gaussiano, 400 repeticiones por excentricidad. Sistema: marco inercial geocentrico idealizado, SI. Dos cuerpos.
Modelo: e_vec = ((v^2 - mu/r) r - (r.v) v)/mu ; n = z x h ; omega = acos(n.e_vec/(|n||e_vec|)) con signo de e_z ; u = omega + nu = argumento de latitud = angulo de r desde el nodo.
Segunda via: el argumento de latitud se calcula tambien directamente como angulo entre n y r (sin pasar por e_vec) y debe coincidir con omega + nu.
Tolerancias: sin ruido omega se recupera dentro de 1e-6 rad (el redondeo de la maquina se amplifica por 1/e: ~1e-8 rad para e = 3e-6); la dispersion de omega crece ~1/e (cociente entre excentricidades vecinas entre 5 y 20 para e >= 3e-5); la de u no depende de e (cociente < 2).
Valor citado sin consulta: inclinacion critica acos(1/sqrt(5)) = 63.4349 grados (resultado de la teoria de J2, que se deduce en B72; no consultado).
"""
from __future__ import annotations
import math, platform, random

MU = 3.986004e14


def rot313(raan, inc, w):
    cO, sO, ci, si, cw, sw = math.cos(raan), math.sin(raan), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    return [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
            [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
            [sw * si, cw * si, ci]]


def mv(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def estado(a, e, inc, raan, w, nu):
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    m = rot313(raan, inc, w)
    f = math.sqrt(MU / p)
    return mv(m, (r * math.cos(nu), r * math.sin(nu), 0.0)), mv(m, (-f * math.sin(nu), f * (e + math.cos(nu)), 0.0))


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norma(a):
    return math.sqrt(dot(a, a))


def angulo_con_signo(n, x, ref_z):
    c = max(-1.0, min(1.0, dot(n, x) / (norma(n) * norma(x))))
    ang = math.acos(c)
    return ang if ref_z >= 0 else 2 * math.pi - ang


def omega_y_u(r, v):
    rn, v2 = norma(r), dot(v, v)
    ev = tuple(((v2 - MU / rn) * r[k] - dot(r, v) * v[k]) / MU for k in range(3))
    h = cruz(r, v)
    n = (-h[1], h[0], 0.0)
    w = angulo_con_signo(n, ev, ev[2])
    u = angulo_con_signo(n, r, r[2])
    return w, u, norma(ev)


def dang(a, b):
    d = abs(a - b) % (2 * math.pi)
    return min(d, 2 * math.pi - d)


def calcular():
    R = {}
    rnd = random.Random(12)
    a = 8000e3
    inc, raan, w0, nu0 = (math.radians(x) for x in (40.0, 70.0, 130.0, 50.0))
    es = [0.3, 0.03, 3e-3, 3e-4, 3e-5, 3e-6]
    sd_w, sd_u, err0 = [], [], 0.0
    for e in es:
        r0, v0 = estado(a, e, inc, raan, w0, nu0)
        w, u, en = omega_y_u(r0, v0)
        err0 = max(err0, dang(w, w0), dang(u, w0 + nu0))
        dw, du = [], []
        for _ in range(400):
            r = tuple(x + rnd.gauss(0, 1.0) for x in r0)
            v = tuple(x + rnd.gauss(0, 1e-3) for x in v0)
            w, u, _ = omega_y_u(r, v)
            dw.append(dang(w, w0))
            du.append(dang(u, w0 + nu0))
        sd_w.append(math.sqrt(sum(x * x for x in dw) / len(dw)))
        sd_u.append(math.sqrt(sum(x * x for x in du) / len(du)))
    R.update(es=es, sd_w=sd_w, sd_u=sd_u, err0=err0)
    R["sd_w_deg"] = [math.degrees(x) for x in sd_w]
    R["sd_u_deg"] = [math.degrees(x) for x in sd_u]
    R["razones_w"] = [sd_w[i + 1] / sd_w[i] for i in range(1, 5)]
    R["razon_u"] = max(sd_u[1:]) / min(sd_u[1:])
    R["prod_e_sd"] = [es[i] * sd_w[i] for i in range(len(es))]
    R["i_crit"] = math.degrees(math.acos(1 / math.sqrt(5)))
    R["i_crit_dif_ret"] = 180.0 - R["i_crit"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("Orbita SINTETICA a = 8000 km, i = 40, RAAN = 70, omega = 130, nu = 50 grados; ruido sigma_r = 1 m, sigma_v = 1e-3 m/s (400 repeticiones, semilla 12)")
    print(f"Sin ruido: error maximo de omega y de u = {R['err0']:.1e} rad")
    print("      e        sigma(omega) [grados]   sigma(u) [grados]   e*sigma(omega) [rad]")
    for e, sw, su, p in zip(R["es"], R["sd_w_deg"], R["sd_u_deg"], R["prod_e_sd"]):
        print(f"  {e:8.0e}     {sw:14.5f}      {su:14.6f}      {p:12.3e}")
    print("  cocientes sigma(omega) entre excentricidades vecinas (e/10): " + " ".join(f"{x:.2f}" for x in R["razones_w"]))
    print(f"  cociente max/min de sigma(u) para e <= 0.03: {R['razon_u']:.2f}")
    print(f"Inclinacion critica acos(1/sqrt(5)) = {R['i_crit']:.4f} grados (y {R['i_crit_dif_ret']:.4f} retrograda); valor citado sin consultar")
    assert R["err0"] < 1e-6
    assert all(5 < x < 20 for x in R["razones_w"])
    assert R["razon_u"] < 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
