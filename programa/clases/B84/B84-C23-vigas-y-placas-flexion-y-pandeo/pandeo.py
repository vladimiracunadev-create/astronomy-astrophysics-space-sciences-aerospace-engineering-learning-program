#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C23: flexion de vigas, pandeo de columnas (Euler) y de placas, y pandeo por autovalores de elementos finitos.

DATOS ILUSTRATIVOS (no consultados): viga/columna de aluminio E = 69 GPa, seccion rectangular b = 30 mm x h = 10 mm (I = b h^3/12 respecto del eje debil),
longitud L = 0,50 m; carga transversal en el extremo del voladizo P = 100 N; placa de aluminio a = 0,30 m x b = 0,20 m, t = 2,0 mm, nu = 0,33.
Formulas: voladizo con carga en el extremo: delta = P L^3/(3 E I); apoyo simple con carga al centro: delta = P L^3/(48 E I); Euler: P_cr = pi^2 E I/(K L)^2
con K = 1 (articulada-articulada), 0,5 (empotrada-empotrada), 0,7 (empotrada-articulada), 2 (voladizo);
placa simplemente apoyada en los 4 bordes cargada en compresion en un sentido: sigma_cr = k pi^2 E/(12 (1 - nu^2)) (t/b)^2 con k = 4 para a/b entero y k = (m b/a + a/(m b))^2 en general.
Segunda via (autovalores): pandeo articulada-articulada con n elementos de viga de Euler-Bernoulli: K phi = lambda Kg phi con la matriz geometrica de elemento
kg = P/(30 l) [[36, 3l, -36, 3l], [3l, 4 l^2, -3l, -l^2], [-36, -3l, 36, -3l], [3l, -l^2, -3l, 4 l^2]] y P = 1; lambda minimo = P_cr.
Tolerancias: P_cr FE frente a Euler < 0,5 % con 8 elementos.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import viga_ke, zeros, gen_eig, reducir

E = 69e9
B, H, L = 0.030, 0.010, 0.50
I = B * H ** 3 / 12


def kg_elemento(P, l):
    c = P / (30 * l)
    return [[c * v for v in f] for f in ((36, 3 * l, -36, 3 * l), (3 * l, 4 * l * l, -3 * l, -l * l), (-36, -3 * l, 36, -3 * l), (3 * l, -l * l, -3 * l, 4 * l * l))]


def pcr_fe(n):
    le = L / n
    N = 2 * (n + 1)
    K, G = zeros(N), zeros(N)
    ke, ge = viga_ke(E * I, le), kg_elemento(1.0, le)
    for e in range(n):
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4):
                K[g[i]][g[j]] += ke[i][j]
                G[g[i]][g[j]] += ge[i][j]
    libres = [i for i in range(N) if i not in (0, 2 * n)]  # w = 0 en los dos extremos
    lam, _ = gen_eig(reducir(K, libres), reducir(G, libres))
    return min(l for l in lam if l > 0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Seccion 30 x 10 mm: I = {I * 1e12:.1f} mm4 ; EI = {E * I:.3f} N m2 ; L = {L} m")
    P = 100.0
    print(f"Flecha con P = {P:.0f} N: voladizo = {P * L ** 3 / (3 * E * I) * 1e3:.3f} mm ; apoyo simple, carga central = {P * L ** 3 / (48 * E * I) * 1e3:.3f} mm")
    print("Carga critica de Euler segun las condiciones de borde:")
    base = math.pi ** 2 * E * I / L ** 2
    for nom, K in (("articulada-articulada", 1.0), ("empotrada-empotrada", 0.5), ("empotrada-articulada", 0.7), ("voladizo", 2.0)):
        print(f"  {nom:22s} K = {K:3.1f}  P_cr = {base / K ** 2:9.2f} N")
    print("Esbeltez: lambda = K L/r con r = h/sqrt(12) =", f"{L / (H / math.sqrt(12)):.1f} (articulada-articulada)")
    print("Pandeo por elementos finitos (articulada-articulada) frente a Euler:")
    for n in (2, 4, 8, 16):
        pf = pcr_fe(n)
        print(f"  n = {n:2d}  P_cr FE = {pf:9.3f} N  error = {(pf - base) / base * 100:8.4f} %")
    assert abs(pcr_fe(8) - base) / base < 0.005
    # placa
    a, b, t, nu = 0.30, 0.20, 2e-3, 0.33
    print("Placa de 0,30 x 0,20 x 0,002 m simplemente apoyada, compresion en la direccion de a:")
    best = None
    for m in range(1, 5):
        k = (m * b / a + a / (m * b)) ** 2
        sc = k * math.pi ** 2 * E / (12 * (1 - nu ** 2)) * (t / b) ** 2
        print(f"  m = {m} semiondas: k = {k:.3f}  sigma_cr = {sc / 1e6:.2f} MPa")
        best = sc if best is None else min(best, sc)
    print(f"Tension critica de la placa = {best / 1e6:.2f} MPa ; fuerza critica por ancho = {best * t / 1e3:.1f} kN/m")
    for tt in (1e-3, 2e-3, 3e-3):
        sc = 4 * math.pi ** 2 * E / (12 * (1 - nu ** 2)) * (tt / b) ** 2
        print(f"  espesor {tt * 1e3:.0f} mm (k = 4): sigma_cr = {sc / 1e6:.2f} MPa (escala con t^2)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
