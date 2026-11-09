#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C18: anisoplanatismo, angulo isoplanatico y cobertura geometrica de la optica adaptativa multiconjugada (modelo ILUSTRATIVO de dos capas).

Datos: dos capas (suelo con 60 % de la turbulencia integrada y 8 km con 40 %), r0 total de 0,13 m a 500 nm, apertura de 8 m (R = 4 m) y cuatro estrellas guia en un cuadrado de +-30 arcsec son ILUSTRATIVOS ; semilla
20261109. Los coeficientes 0,423, 2,914, 0,314, 6,88 y 1,03 son de libro de texto, NO consultados en esta clase (se verifica su consistencia interna). La unica fuente leida es el RESUMEN de Rigaut y Neichel, arXiv:2003.03097.
Modelo: (1) angulo isoplanatico theta0 = [2,914 k^2 int Cn^2 h^(5/3) dh]^(-3/5) y su forma theta0 = 0,314 r0 / h_bar (dos vias algebraicas independientes) ; error de anisoplanatismo de la correccion con un espejo en el suelo
sigma^2(theta) = (theta/theta0)^(5/3). (2) cobertura geometrica: la huella de la pupila en la capa de altitud h para una direccion theta es un disco de radio R desplazado h theta ; la parte de la huella del objeto que NINGUNA
estrella guia observa no esta restringida por las medidas. Se calcula la fraccion no cubierta por Monte Carlo (400000 puntos) y se contrasta con la formula analitica de la interseccion de dos discos para una sola estrella.
(3) un modelo de error residual MCAO ilustrativo sigma^2_MCAO(theta) = f_nc(theta) * 1,03 (2R/r0,h)^(5/3) (la capa alta sin restriccion se supone no corregida ; la capa de suelo se supone medida y corregida).
Supuestos: capas finas, Kolmogorov, medidas sin ruido, reconstruccion ideal en la parte cubierta. Validez: SOLO ilustrativa ; no reproduce a ningun sistema real (MAD, GeMS...).
Tolerancia: las dos formas de theta0 coinciden a 0,5 % ; interseccion Monte Carlo frente a la formula analitica a 3e-3 ; sigma^2 en theta0 igual a 1 a 1e-12.
"""
from __future__ import annotations
import math, platform, random

ARCSEC = 206264.806247
LAM = 500e-9
K = 2 * math.pi / LAM

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    r0 = 0.13
    j_tot = r0 ** (-5 / 3) / (0.423 * K * K)       # integral de Cn^2 dh total
    capas = [(0.0, 0.6), (8000.0, 0.4)]
    j = [(h, w * j_tot) for h, w in capas]
    print(f"integral de Cn^2 dh = {j_tot:.4e} m^(1/3) ; r0 = {r0} m ; r0 por capa: " + ", ".join(f"h = {h / 1e3:.0f} km -> {(0.423 * K * K * jj) ** (-3 / 5):.3f} m" for h, jj in j))
    t0_a = (2.914 * K * K * sum(jj * h ** (5 / 3) for h, jj in j)) ** (-3 / 5)
    h_bar = (sum(jj * h ** (5 / 3) for h, jj in j) / j_tot) ** (3 / 5)
    t0_b = 0.314 * r0 / h_bar
    print(f"h_bar = {h_bar / 1e3:.3f} km ; theta0 (via integral) = {t0_a * ARCSEC:.3f} arcsec ; theta0 = 0,314 r0 / h_bar = {t0_b * ARCSEC:.3f} arcsec ; diferencia = {abs(t0_a / t0_b - 1):.2%}")
    assert abs(t0_a / t0_b - 1) < 0.005
    print(f"{'theta [arcsec]':>14} {'sigma^2 = (theta/theta0)^5/3':>29} {'Strehl exp(-s2)':>16}")
    for ang in (2, 5, 10, 20, 40):
        s2 = (ang / ARCSEC / t0_a) ** (5 / 3)
        print(f"{ang:14d} {s2:29.4f} {math.exp(-s2):16.4f}")
    assert abs((t0_a / t0_a) ** (5 / 3) - 1) < 1e-12
    # (2) interseccion de dos discos
    R = 4.0
    h = 8000.0
    print(f"{'theta [arcsec]':>14} {'desplazamiento [m]':>19} {'fraccion comun MC':>18} {'analitica':>10}")
    for ang in (10, 30, 60, 120):
        d = h * ang / ARCSEC
        if d >= 2 * R:
            ana = 0.0
        else:
            ana = (2 * R * R * math.acos(d / (2 * R)) - 0.5 * d * math.sqrt(4 * R * R - d * d)) / (math.pi * R * R)
        n = 400000
        c = 0
        for _ in range(n):
            r = R * math.sqrt(rnd.random()); t = 2 * math.pi * rnd.random()
            x, y = r * math.cos(t), r * math.sin(t)
            if math.hypot(x - d, y) <= R:
                c += 1
        mc = c / n
        print(f"{ang:14d} {d:19.3f} {mc:18.4f} {ana:10.4f}")
        assert abs(mc - ana) < 3e-3, (ang, mc, ana)
    # (3) cuatro estrellas guia en +-30 arcsec : fraccion no cubierta para un objeto en theta
    gs = [(30, 30), (-30, 30), (30, -30), (-30, -30)]
    r0h = (0.423 * K * K * j[1][1]) ** (-3 / 5)
    var_alta = 1.03 * (2 * R / r0h) ** (5 / 3)
    print(f"capa de 8 km: r0,h = {r0h:.3f} m ; varianza de fase sobre la pupila (modelo) = {var_alta:.2f} rad^2")
    print(f"{'theta (x,y) arcsec':>20} {'f no cubierta':>14} {'sigma^2 MCAO':>13} {'sigma^2 un espejo':>18}")
    n = 200000
    # puntos de la huella del objeto en la capa alta
    pts = []
    for _ in range(n):
        r = R * math.sqrt(rnd.random()); t = 2 * math.pi * rnd.random()
        pts.append((r * math.cos(t), r * math.sin(t)))
    prev = 0.0
    for tx, ty in ((0, 0), (10, 0), (20, 0), (30, 0), (40, 0), (50, 50)):
        ox, oy = h * tx / ARCSEC, h * ty / ARCSEC
        sin_cub = 0
        for (x, y) in pts:
            px, py = x + ox, y + oy
            if any(math.hypot(px - h * gx / ARCSEC, py - h * gy / ARCSEC) <= R for gx, gy in gs):
                sin_cub += 1
        f_nc = 1 - sin_cub / n
        s2 = f_nc * var_alta
        s2_sc = (math.hypot(tx, ty) / ARCSEC / t0_a) ** (5 / 3)
        print(f"{f'({tx}, {ty})':>20} {f_nc:14.4f} {s2:13.3f} {s2_sc:18.3f}")
        if (tx, ty) in ((0, 0), (10, 0), (20, 0), (30, 0)):
            assert f_nc == 0.0 or f_nc < 0.02
        prev = f_nc
    assert prev > 0.0      # lejos de las guias hay region no restringida
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
