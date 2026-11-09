#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C02: geometria instrumental (Newton, Cassegrain clasico y Ritchey-Chretien) por trazado exacto de rayos meridionales.

Datos: ILUSTRATIVOS (D = 200 mm, primario f/5 de 1000 mm, separacion 700 mm, aumento del secundario m = 4, angulo de campo 0,1 grados). Sin datos de instrumentos reales.
Modelo: superficies conicas z = zv + (R - sqrt(R^2 - (1+K) y^2))/(1+K); interseccion por Newton, reflexion vectorial. El Cassegrain clasico usa K1 = -1 y K2 = -((m+1)/(m-1))^2;
el Ritchey-Chretien se obtiene resolviendo K1 y K2 numericamente (Newton 2x2) para anular la aberracion esferica y el coma tangencial.
Verificacion independiente: coma tangencial del paraboloide con la formula 3 theta/(16 N^2) (aberracion de tercer orden) y K2 clasico frente a la forma cerrada del hiperboloide.
Supuestos: trazado meridional 2D, sin obstruccion, monocromatico. Validez: campos pequenos.
Tolerancia: dispersion del foco axial del clasico < 1e-6 mm; coma del paraboloide frente a la formula, 2 %.
"""
from __future__ import annotations
import math, platform

D = 200.0; F1 = 1000.0; SEP = 700.0; M = 4.0; THETA = math.radians(0.1)

def sag(y, R, K):
    q = 1 + K
    if abs(q) < 1e-12:
        return y * y / (2 * R)
    # forma estable: y^2 / (R + sqrt(R^2 - q y^2))
    return y * y / (R + math.sqrt(R * R - q * y * y))

def dsag(y, R, K):
    return y / math.sqrt(R * R - (1 + K) * y * y)

def hit(p, d, zv, R, K):
    t = 0.0
    for _ in range(60):
        y = p[0] + t * d[0]; z = p[1] + t * d[1]
        f = z - (zv + sag(y, R, K))
        df = d[1] - dsag(y, R, K) * d[0]
        dt = f / df
        t -= dt
        if abs(dt) < 1e-13:
            break
    return (p[0] + t * d[0], p[1] + t * d[1])

def reflect(d, y, R, K):
    n = (-dsag(y, R, K), 1.0); nn = math.hypot(*n); n = (n[0] / nn, n[1] / nn)
    k = d[0] * n[0] + d[1] * n[1]
    return (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])

def secondary_R():
    s1 = F1 - SEP; s2 = M * s1
    return 2 * s1 * s2 / (s2 - s1), SEP - s2

def trace(h, theta, K1, K2, newton=False):
    """Rayo con altura h en el primario y angulo de campo theta. Devuelve (y en el plano focal, z del cruce con el eje)."""
    d0 = (math.sin(theta), -math.cos(theta))
    p0 = (h - 3000 * d0[0] / (-d0[1]) * (-1) if False else h, 3000.0)
    p0 = (h - d0[0] / d0[1] * (3000.0), 3000.0)
    p1 = hit(p0, d0, 0.0, 2 * F1, K1)
    d1 = reflect(d0, p1[0], 2 * F1, K1)
    if newton:
        return p1, d1
    R2, zf = secondary_R()
    p2 = hit(p1, d1, SEP, R2, K2)
    d2 = reflect(d1, p2[0], R2, K2)
    t = (zf - p2[1]) / d2[1]
    yf = p2[0] + t * d2[0]
    zax = p2[1] - p2[0] * d2[1] / d2[0] if abs(d2[0]) > 0 else 0.0
    return yf, zax

def sa_coma(K1, K2, h=100.0):
    zs = [trace(hh, 0.0, K1, K2)[1] for hh in (h,)]
    sa = zs[0] - secondary_R()[1]
    up = trace(h, THETA, K1, K2)[0]; dn = trace(-h, THETA, K1, K2)[0]; ch = trace(0.0, THETA, K1, K2)[0]
    return sa, (up + dn) / 2 - ch

def solve_rc():
    K1, K2 = -1.0, -((M + 1) / (M - 1)) ** 2
    for _ in range(30):
        f0 = sa_coma(K1, K2); e = 1e-6
        fa = sa_coma(K1 + e, K2); fb = sa_coma(K1, K2 + e)
        a11 = (fa[0] - f0[0]) / e; a12 = (fb[0] - f0[0]) / e
        a21 = (fa[1] - f0[1]) / e; a22 = (fb[1] - f0[1]) / e
        det = a11 * a22 - a12 * a21
        d1 = (a22 * f0[0] - a12 * f0[1]) / det; d2 = (-a21 * f0[0] + a11 * f0[1]) / det
        K1 -= d1; K2 -= d2
        if abs(d1) + abs(d2) < 1e-12:
            break
    return K1, K2

def calc():
    r = {}
    R2, zf = secondary_R()
    s1 = F1 - SEP; s2 = M * s1
    r["R2_mm"] = R2; r["foco_final_z_mm"] = zf; r["f_efectiva_mm"] = F1 * M; r["N_efectiva"] = F1 * M / D
    K2c = -((M + 1) / (M - 1)) ** 2
    a = (s1 + s2) / 2 - s1; c = (s1 + s2) / 2
    r["K2_clasico"] = K2c; r["K2_hiperbola"] = -(c / a) ** 2
    zs = [trace(h, 0.0, -1.0, K2c)[1] for h in (20.0, 40.0, 60.0, 80.0, 100.0)]
    r["dispersion_foco_clasico_mm"] = max(zs) - min(zs)
    zs_esf = [trace(h, 0.0, -1.0, 0.0)[1] for h in (20.0, 100.0)]
    r["esferica_sec_esferico_mm"] = zs_esf[1] - zs_esf[0]
    # coma
    ch = trace(0.0, THETA, -1.0, K2c)[0]
    sa, cm = sa_coma(-1.0, K2c)
    r["coma_clasico_um"] = cm * 1e3
    K1, K2 = solve_rc()
    r["K1_RC"] = K1; r["K2_RC"] = K2
    sa2, cm2 = sa_coma(K1, K2)
    r["sa_RC_mm"] = sa2; r["coma_RC_um"] = cm2 * 1e3
    # Newton (parabola)
    def newton_y(h, th):
        p, d = trace(h, th, -1.0, 0.0, newton=True)
        t = (F1 - p[1]) / d[1]
        return p[0] + t * d[0]
    up = newton_y(100, THETA); dn = newton_y(-100, THETA); c0 = newton_y(0, THETA)
    r["coma_newton_um"] = ((up + dn) / 2 - c0) * 1e3
    r["coma_formula_um"] = 3 * THETA / (16 * (F1 / D) ** 2) * F1 * 1e3
    r["tubo_newton_mm"] = F1; r["tubo_cassegrain_mm"] = SEP
    r["obstruccion_sec_mm"] = D * (F1 - SEP) / F1 * (1 + 0.0)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.6g}")
    assert abs(r["K2_clasico"] - r["K2_hiperbola"]) < 1e-9
    assert r["dispersion_foco_clasico_mm"] < 1e-6
    assert abs(r["sa_RC_mm"]) < 1e-7 and abs(r["coma_RC_um"]) < 1e-4
    assert abs(r["coma_newton_um"] - r["coma_formula_um"]) / r["coma_formula_um"] < 0.02
    assert abs(r["coma_RC_um"]) < abs(r["coma_clasico_um"]) * 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
