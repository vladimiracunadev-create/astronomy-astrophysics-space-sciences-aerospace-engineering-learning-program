#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C15: doblete acromatico, espectro secundario y triplete apocromatico (lentes delgadas en contacto).

Datos: coeficientes de Sellmeier de tres vidrios tipo crown (B1 1,03961212; B2 0,231792344; B3 1,01046945; C1 0,00600069867; C2 0,0200179144; C3 103,560653),
flint (1,34533359; 0,209073176; 0,937357162; 0,00997743871; 0,0470450767; 111,886764) y fluorita (0,5675888; 0,4710914; 3,8484723; 0,00252643; 0,01007833; 1200,556),
con C en micras^2, escritos de MEMORIA por el autor: NO se consultaron en esta sesion y son ILUSTRATIVOS (no un catalogo de fabricante). Focal total 1000 mm y D = 100 mm.
Modelo: potencia de cada elemento fino P_i(lambda) = k_i (n_i(lambda) - 1), donde k_i (1/R1 - 1/R2) es el factor de forma. Doblete: se imponen potencias iguales en F (486,1 nm) y C
(656,3 nm) y la potencia total en d (587,6 nm); triplete: potencias iguales en 450, 550 y 650 nm. Segunda via: el doblete frente a la formula de libro
P1 = P V1/(V1 - V2). Se mide el desenfoque en el rango 400-800 nm.
Supuestos: lentes delgadas en contacto, rayos paraxiales. Validez: ilustrativa; no incluye esfericromatismo.
Tolerancia: P1 por resolucion frente a la formula de libro 2 %; focal en F y C iguales a 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, sys

VID = {
    "crown": ((1.03961212, 0.231792344, 1.01046945), (0.00600069867, 0.0200179144, 103.560653)),
    "flint": ((1.34533359, 0.209073176, 0.937357162), (0.00997743871, 0.0470450767, 111.886764)),
    "fluorita": ((0.5675888, 0.4710914, 3.8484723), (0.00252643, 0.01007833, 1200.556)),
}


def n_de(v, lam):
    B, C = VID[v]
    l2 = (lam / 1000.0) ** 2
    return math.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(B, C)))


def resolver(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]
                M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]


def potencia(vs, ks, lam):
    return sum(k * (n_de(v, lam) - 1) for v, k in zip(vs, ks))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    F0 = 1000.0
    P = 1 / F0
    Vv = {}
    for v in VID:
        Vv[v] = (n_de(v, 587.6) - 1) / (n_de(v, 486.1) - n_de(v, 656.3))
        print(f"{v:>9}: nd = {n_de(v,587.6):.5f}  V = {Vv[v]:.2f}")
    # singlete
    k0 = P / (n_de("crown", 587.6) - 1)
    # doblete
    vs = ("crown", "flint")
    A = [[n_de(v, 486.1) - 1 for v in vs], [n_de(v, 656.3) - 1 for v in vs]]
    ks = resolver(A, [P, P])
    P1d = ks[0] * (n_de("crown", 587.6) - 1)
    P1f = P * Vv["crown"] / (Vv["crown"] - Vv["flint"])
    print(f"doblete crown+flint: P1(d) = {P1d*1e3:.4f} dioptrias por resolucion ; formula de libro = {P1f*1e3:.4f} ; diferencia {abs(P1d-P1f)/P1f*100:.2f} %")
    print(f"  focales de los elementos en d: f1 = {1/P1d:.1f} mm ; f2 = {1/(ks[1]*(n_de('flint',587.6)-1)):.1f} mm")
    assert abs(P1d - P1f) / P1f < 0.02
    # espectro secundario
    print(f"{'lambda [nm]':>12} {'singlete f-1000 [mm]':>22} {'doblete [mm]':>14} {'triplete [mm]':>15}")
    vs3 = ("crown", "flint", "fluorita")
    A3 = [[n_de(v, lam) - 1 for v in vs3] for lam in (450.0, 550.0, 650.0)]
    k3 = resolver(A3, [P, P, P])
    rng = {}
    for lam in (400.0, 435.8, 486.1, 550.0, 587.6, 656.3, 700.0, 800.0):
        f_s = 1 / (k0 * (n_de("crown", lam) - 1))
        f_d = 1 / potencia(vs, ks, lam)
        f_t = 1 / potencia(vs3, k3, lam)
        rng[lam] = (f_s - F0, f_d - F0, f_t - F0)
        print(f"{lam:12.1f} {f_s-F0:22.3f} {f_d-F0:14.3f} {f_t-F0:15.3f}")
    assert abs(1 / potencia(vs, ks, 486.1) - 1 / potencia(vs, ks, 656.3)) < 1e-6
    assert abs(1 / potencia(vs3, k3, 450.0) - F0) < 1e-6
    print(f"factores de forma del triplete (k1, k2, k3) = ({k3[0]*1e3:.4f}, {k3[1]*1e3:.4f}, {k3[2]*1e3:.4f}) /1000 mm")
    Fn = F0 / 100.0   # N = 10
    prof = 4 * 550e-6 * 10 ** 2
    print(f"profundidad de enfoque (4 lambda N^2 con N = 10) = {prof:.3f} mm")
    for i, nom in enumerate(("singlete", "doblete", "triplete")):
        ext = max(abs(rng[l][i]) for l in (486.1, 550.0, 587.6, 656.3))
        ext2 = max(abs(rng[l][i]) for l in rng)
        print(f"  {nom:>8}: desenfoque maximo 486-656 nm = {ext:.3f} mm ({ext/prof:.2f} profundidades) ; 400-800 nm = {ext2:.3f} mm")
    assert max(abs(rng[l][1]) for l in (486.1, 550.0, 587.6, 656.3)) < 0.1 * max(abs(rng[l][0]) for l in (486.1, 656.3))
    assert max(abs(rng[l][2]) for l in (450.0 if 450.0 in rng else 486.1, 550.0, 656.3)) < max(abs(rng[l][1]) for l in (486.1, 550.0, 656.3))
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
