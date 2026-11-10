#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C17: movimiento en el plano orbital, sistema perifocal (PQW) y rotacion al marco inercial (3-1-3).

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 (IAU 2015 B3). DATOS SINTETICOS (semilla 17): 500 estados con a en [7000, 30000] km,
e en [0, 0.8], i en [0, 180] grados, RAAN, omega, nu en [0, 360); y una orbita de ejemplo a = 12000 km, e = 0.4, i = 63.4, RAAN = 20, omega = 250 grados.
Sistema: marco inercial geocentrico idealizado (ECI), SI. Dos cuerpos.
Modelo: en el sistema perifocal, r = r (cos nu P + sin nu Q), v = sqrt(mu/p) (-sin nu P + (e + cos nu) Q); la matriz de rotacion es R3(-RAAN) R1(-i) R3(-omega).
Segunda via: (1) la matriz debe ser ortogonal con determinante +1; (2) h = r x v debe ser paralelo a W = z-inercial rotado y |h| = sqrt(mu p);
(3) la energia v^2/2 - mu/r debe valer -mu/(2a); (4) la componente radial y transversal de v debe ser mu e sin nu/h y h/r; (5) un paso de RK4 de 1 s desde el estado
en el marco inercial debe coincidir con la velocidad de la formula (derivada numerica de la posicion), residuo < 1e-3 m.
Tolerancias: ortogonalidad < 1e-12; h paralelo a W: 1e-12; energia y |h| 1e-9 relativas; derivada numerica de la posicion frente a v dentro de 1e-6 relativa.
"""
from __future__ import annotations
import math, platform, random

MU = 3.986004e14


def rot(raan, inc, w):
    cO, sO, ci, si, cw, sw = math.cos(raan), math.sin(raan), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    return [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
            [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
            [sw * si, cw * si, ci]]


def mv(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def norma(a):
    return math.sqrt(sum(x * x for x in a))


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def perifocal(a, e, nu):
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    f = math.sqrt(MU / p)
    return (r * math.cos(nu), r * math.sin(nu), 0.0), (-f * math.sin(nu), f * (e + math.cos(nu)), 0.0), p, r


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def calcular():
    R = {}
    rnd = random.Random(17)
    o_max = dh = de = dhm = dvr = dvt = 0.0
    det_dev = 0.0
    for _ in range(500):
        a = rnd.uniform(7000e3, 30000e3)
        e = rnd.uniform(0.0, 0.8)
        inc, raan, w, nu = (math.radians(rnd.uniform(lo, hi)) for lo, hi in ((0, 180), (0, 360), (0, 360), (0, 360)))
        rp_, vp_, p, rr = perifocal(a, e, nu)
        m = rot(raan, inc, w)
        # ortogonalidad: M M^T = I
        for i in range(3):
            for j in range(3):
                s = sum(m[i][k] * m[j][k] for k in range(3))
                o_max = max(o_max, abs(s - (1.0 if i == j else 0.0)))
        det_dev = max(det_dev, abs(det3(m) - 1.0))
        r, v = mv(m, rp_), mv(m, vp_)
        h = cruz(r, v)
        W = mv(m, (0.0, 0.0, 1.0))
        hh = norma(h)
        dh = max(dh, norma(tuple(h[k] / hh - W[k] for k in range(3))))
        dhm = max(dhm, abs(hh - math.sqrt(MU * p)) / hh)
        eps = 0.5 * dot(v, v) - MU / norma(r)
        de = max(de, abs(eps + MU / (2 * a)) / (MU / (2 * a)))
        # componentes radial y transversal
        vr = dot(r, v) / norma(r)
        vt = hh / norma(r)
        vr_teo = MU * e * math.sin(nu) / hh
        dvr = max(dvr, abs(vr - vr_teo) / math.sqrt(MU / p))
        vt_calc = math.sqrt(max(0.0, dot(v, v) - vr * vr))
        dvt = max(dvt, abs(vt_calc - vt) / math.sqrt(MU / p))
    R.update(ortog=o_max, det_dev=det_dev, h_par_W=dh, h_mod=dhm, energia=de, vr_dev=dvr, vt_dev=dvt)
    # derivada numerica de la posicion kepleriana: se propaga con anomalia excentrica
    a, e = 12000e3, 0.4
    inc, raan, w = (math.radians(x) for x in (63.4, 20.0, 250.0))
    nu0 = math.radians(75.0)
    rp_, vp_, p, rr = perifocal(a, e, nu0)
    m = rot(raan, inc, w)
    r0, v0 = mv(m, rp_), mv(m, vp_)
    R["r0_km"] = norma(r0) / 1e3
    R["v0"] = norma(v0)
    R["h_vec"] = cruz(r0, v0)
    hn = norma(R["h_vec"])
    R["i_h"] = math.degrees(math.acos(R["h_vec"][2] / hn))
    # RK4 de 1 s desde (r0, v0), comparar r(1) y v(1) con la formula en nu(1)
    def f(s):
        d3 = norma(s[:3]) ** 3
        return (s[3], s[4], s[5], -MU * s[0] / d3, -MU * s[1] / d3, -MU * s[2] / d3)
    s = r0 + v0
    dt = 1.0
    nsub = 100
    for _ in range(nsub):
        h_ = dt / nsub
        k1 = f(s); k2 = f(tuple(s[i] + 0.5 * h_ * k1[i] for i in range(6)))
        k3 = f(tuple(s[i] + 0.5 * h_ * k2[i] for i in range(6))); k4 = f(tuple(s[i] + h_ * k3[i] for i in range(6)))
        s = tuple(s[i] + h_ / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(6))
    # formula: avanzar nu por dt con nu' = h/r^2 (primer orden insuficiente): se usa Kepler
    n_mov = math.sqrt(MU / a ** 3)
    E0 = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu0 / 2), math.sqrt(1 + e) * math.cos(nu0 / 2))
    M0 = E0 - e * math.sin(E0)
    M1 = M0 + n_mov * dt
    E = M1
    for _ in range(50):
        E -= (E - e * math.sin(E) - M1) / (1 - e * math.cos(E))
    nu1 = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    rp1, vp1, _, _ = perifocal(a, e, nu1)
    r1, v1 = mv(m, rp1), mv(m, vp1)
    R["dr_1s"] = norma(tuple(s[k] - r1[k] for k in range(3)))
    R["dv_1s"] = norma(tuple(s[3 + k] - v1[k] for k in range(3)))
    # derivada numerica de r: (r1 - r0)/dt frente a (v0 + v1)/2
    R["dif_deriv"] = norma(tuple((r1[k] - r0[k]) / dt - 0.5 * (v0[k] + v1[k]) for k in range(3))) / norma(v0)
    R["nu1_deg"] = math.degrees(nu1)
    R["dnu_deg"] = math.degrees(nu1 - nu0)
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("500 estados SINTETICOS (semilla 17), a en [7000, 30000] km, e en [0, 0.8], i en [0, 180] grados:")
    print(f"  ortogonalidad de la matriz 3-1-3: max |M M^T - I| = {R['ortog']:.1e} ; |det - 1| = {R['det_dev']:.1e}")
    print(f"  h/|h| frente a W (z perifocal rotado): {R['h_par_W']:.1e} ; |h| frente a sqrt(mu p): {R['h_mod']:.1e}")
    print(f"  energia frente a -mu/(2a): {R['energia']:.1e} ; v_radial = mu e sin nu/h: {R['vr_dev']:.1e} ; v_transversal = h/r: {R['vt_dev']:.1e} (normalizados por sqrt(mu/p))")
    print("Orbita de ejemplo SINTETICA a = 12000 km, e = 0.4, i = 63.4, RAAN = 20, omega = 250 grados, nu = 75 grados:")
    print(f"  |r| = {R['r0_km']:.3f} km ; |v| = {R['v0']:.3f} m/s ; inclinacion de h = {R['i_h']:.4f} grados")
    print(f"  tras 1 s: RK4 inercial frente a la formula en nu = {R['nu1_deg']:.5f} grados (avance {R['dnu_deg']:.5f}): |dr| = {R['dr_1s']:.2e} m ; |dv| = {R['dv_1s']:.2e} m/s")
    print(f"  (r1 - r0)/dt frente a la velocidad media: diferencia relativa {R['dif_deriv']:.1e}")
    assert R["ortog"] < 1e-12 and R["det_dev"] < 1e-12 and R["h_par_W"] < 1e-12
    assert R["h_mod"] < 1e-9 and R["energia"] < 1e-9 and R["vr_dev"] < 1e-9 and R["vt_dev"] < 1e-9
    assert R["dr_1s"] < 1e-3 and R["dif_deriv"] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
