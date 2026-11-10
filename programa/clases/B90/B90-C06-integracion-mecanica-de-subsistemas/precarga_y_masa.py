#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C06: precarga por par de apriete y propiedades de masa de un CubeSat 3U SINTETICO.

Precarga: F = T / (K d) (relacion de par; K es el coeficiente de par, dispersion SINTETICA 0.15-0.25).
Union: separacion cuando la carga externa por perno supera F_min / (1 - phi), phi = factor de carga de la union.
Masa: CG = sum m r / sum m; tensor de inercia por el teorema de ejes paralelos, contrastado con una discretizacion en puntos.
Sistema de referencia: origen en el centro geometrico, z a lo largo del eje largo. Unidades SI. Tolerancia de inercia: 1 %.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: perno M3, par 1.0 N m; CubeSat 3U de 0.1 x 0.1 x 0.34 m")
d, T = 0.003, 1.0
K0, Klo, Khi = 0.20, 0.15, 0.25
As = 5.03e-6                                   # area resistente de una rosca M3 [m2] (valor de tabla de roscas, no consultado)
F = lambda K: T / (K * d)
print(f"Precarga nominal = {F(K0):.0f} N ; con K = {Klo}-{Khi}: {F(Khi):.0f} a {F(Klo):.0f} N")
rng = np.random.default_rng(90)
Fm = F(rng.uniform(Klo, Khi, 200000))
print(f"Monte Carlo: min = {Fm.min():.0f} N ; max = {Fm.max():.0f} N ; media = {Fm.mean():.0f} N")
comprobar(abs(Fm.min() - F(Khi)) / F(Khi) < 1e-3 and abs(Fm.max() - F(Klo)) / F(Klo) < 1e-3, "el Monte Carlo debe llenar el rango analitico")
sig_max = F(Klo) / As / 1e6
Sy = 600.0                                      # MPa limite de fluencia SINTETICO
FS = 1.25
MS_y = Sy / (sig_max * FS) - 1
print(f"Tension de precarga maxima = {sig_max:.1f} MPa ; margen a fluencia (FS {FS}) = {MS_y:.2f}")
phi = 0.20
P_ext = 4.0 * 50 * 9.80665 / 4                  # 4 kg, 50 g de aceleracion de ejemplo, 4 pernos
FSs = 1.4
P_sep = F(Khi) / (1 - phi)
MS_sep = P_sep / (P_ext * FSs) - 1
print(f"Carga externa por perno = {P_ext:.0f} N ; separacion en {P_sep:.0f} N ; margen de separacion (FS {FSs}) = {MS_sep:.2f}")
comprobar(MS_y > 0 and MS_sep > 0, "los margenes del ejemplo deben ser positivos")

# Propiedades de masa: (nombre, masa kg, (dx, dy, dz) m, centro (x, y, z) m)
piezas = [
    ("Estructura", 0.60, (0.10, 0.10, 0.34), (0.000, 0.000, 0.000)),
    ("Bateria", 0.40, (0.09, 0.09, 0.03), (0.000, 0.000, -0.120)),
    ("EPS", 0.30, (0.09, 0.09, 0.02), (0.000, 0.000, -0.080)),
    ("OBC", 0.10, (0.09, 0.09, 0.015), (0.000, 0.000, -0.040)),
    ("COM", 0.15, (0.09, 0.09, 0.02), (0.000, 0.000, 0.010)),
    ("Carga util", 1.20, (0.09, 0.09, 0.10), (0.005, -0.003, 0.070)),
    ("ADCS", 0.50, (0.09, 0.09, 0.05), (0.000, 0.000, 0.130)),
]
M = sum(p[1] for p in piezas)
cg = sum(p[1] * np.array(p[3]) for p in piezas) / M
print(f"Masa total = {M:.2f} kg ; CG = ({cg[0] * 1000:.2f}, {cg[1] * 1000:.2f}, {cg[2] * 1000:.2f}) mm")
lim = np.array([0.02, 0.02, 0.07])               # +-2 cm, +-2 cm, +-7 cm (limites consultados en el CDS para 3U)
ok = np.abs(cg) <= lim
print("Limites 3U (CDS Rev. 14.1): +-20, +-20, +-70 mm ->", ["OK" if o else "FALLA" for o in ok])
comprobar(bool(ok.all()), "el CG de ejemplo debe estar dentro de los limites")

def inercia_analitica(piezas, cg):
    I = np.zeros((3, 3))
    for _, m, (a, b, c), ctr in piezas:
        Ic = np.diag([m * (b**2 + c**2) / 12, m * (a**2 + c**2) / 12, m * (a**2 + b**2) / 12])
        r = np.array(ctr) - cg
        I += Ic + m * (np.dot(r, r) * np.eye(3) - np.outer(r, r))
    return I

def inercia_puntos(piezas, cg, n=30):
    I = np.zeros((3, 3))
    for _, m, (a, b, c), ctr in piezas:
        u = (np.arange(n) + 0.5) / n - 0.5
        X, Y, Z = np.meshgrid(u * a, u * b, u * c, indexing="ij")
        P = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1) + np.array(ctr) - cg
        mp = m / len(P)
        r2 = (P**2).sum(axis=1)
        I += mp * (r2.sum() * np.eye(3) - P.T @ P)
    return I

Ia = inercia_analitica(piezas, cg)
Ip = inercia_puntos(piezas, cg)
print("Inercias analiticas [kg m2]: Ixx = %.5f ; Iyy = %.5f ; Izz = %.5f ; Ixy = %.6f ; Ixz = %.6f ; Iyz = %.6f" % (Ia[0, 0], Ia[1, 1], Ia[2, 2], -Ia[0, 1], -Ia[0, 2], -Ia[1, 2]))
dif = np.abs(np.diag(Ia) - np.diag(Ip)) / np.diag(Ia)
print("Diferencia con la discretizacion en puntos (diagonal): " + ", ".join(f"{x * 100:.3f} %" for x in dif))
comprobar(bool((dif < 0.01).all()), "la discretizacion debe coincidir a 1 %")
w = np.linalg.eigvalsh(Ia)
print(f"Momentos principales = {w[0]:.5f}, {w[1]:.5f}, {w[2]:.5f} kg m2 ; triangulo: {w[0] + w[1] >= w[2] - 1e-12}")
comprobar(bool((w > 0).all()) and w[0] + w[1] >= w[2] - 1e-12, "el tensor debe ser fisicamente valido")
fin()
