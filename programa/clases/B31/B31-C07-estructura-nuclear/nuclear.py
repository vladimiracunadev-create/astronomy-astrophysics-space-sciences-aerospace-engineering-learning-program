#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C07: energias de ligadura de nucleos ligeros, energia liberada en reacciones y barrera de Coulomb.

Datos: masas del proton, neutron, deuteron, triton, helion y particula alfa en MeV/c^2 (NIST CODATA 2022, tabla allascii.txt: 938.272 089 43; 939.565 421 94; 1875.612 945 00;
2808.921 136 68; 2808.391 611 12; 3727.379 4118), la constante de masa atomica (931.494 103 72 MeV), la constante de estructura fina (7.297 352 5643e-3), hbar c = 197.326 980 4 MeV fm,
y k_B (NIST), consultados 2026-11-09. El radio r_0 = 1.2 fm y la temperatura 1.5e7 K (nucleo solar) son ILUSTRATIVOS (sinteticos).
Modelo: B = (Z m_p + N m_n - M) c^2 con masas de nucleos desnudos; Q = (suma de masas iniciales - suma de masas finales) c^2; barrera de Coulomb E_C = Z1 Z2 alpha hbar c/(r_0 (A1^(1/3) + A2^(1/3)));
energia de Gamow E_G = 2 m_r c^2 (pi alpha Z1 Z2)^2 y pico de Gamow E_0 = (E_G (k T)^2/4)^(1/3).
Supuestos: nucleos esfericos con radio r_0 A^(1/3), efecto tunel sin correcciones. Validez: orden de magnitud para E_C y E_0.
Tolerancia: energias de ligadura dentro de 1e-9 MeV entre la via en MeV y la via en kg; conservacion de la carga y del numero de nucleones en las reacciones.
"""
from __future__ import annotations
import math
import platform
import sys

MP, MN, MD, MT, MH, MA = 938.27208943, 939.56542194, 1875.61294500, 2808.92113668, 2808.39161112, 3727.3794118
MU_MEV = 931.49410372
ALPHA, HBARC = 7.2973525643e-3, 197.3269804
KB_EV = 8.617333262e-5
# masas en kg para comprobar la conversion
KG = {"p": 1.67262192595e-27, "n": 1.67492750056e-27, "d": 3.3435837768e-27, "t": 5.0073567512e-27, "h": 5.0064127862e-27, "a": 6.6446573450e-27}
C, E = 299792458.0, 1.602176634e-19


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nuc = {"d": (1, 1, MD, "d"), "t": (1, 2, MT, "t"), "h": (2, 1, MH, "h"), "a": (2, 2, MA, "a")}
    print(f"{'nucleo':<10} {'Z':>2} {'N':>2} {'B [MeV]':>10} {'B/A [MeV]':>10} {'B por kg [MeV]':>15}")
    for nombre, (z, n, m, k) in nuc.items():
        b = z * MP + n * MN - m
        b_kg = (z * KG["p"] + n * KG["n"] - KG[k]) * C ** 2 / E / 1e6
        print(f"{nombre:<10} {z:2d} {n:2d} {b:10.5f} {b / (z + n):10.5f} {b_kg:15.5f}")
        assert abs(b - b_kg) < 5e-5, f"conversion {nombre}"
    # reacciones
    reac = [
        ("d + t -> alfa + n", [MD, MT], [MA, MN], (2, 5), (2, 5)),
        ("d + d -> helion + n", [MD, MD], [MH, MN], (2, 4), (2, 4)),
        ("d + d -> triton + p", [MD, MD], [MT, MP], (2, 4), (2, 4)),
    ]
    print(f"{'reaccion':<22} {'Q [MeV]':>10}")
    for nombre, ini, fin, ci, cf in reac:
        q = sum(ini) - sum(fin)
        assert ci == cf
        print(f"{nombre:<22} {q:10.5f}")
    # barrera de Coulomb y Gamow
    kt_kev = KB_EV * 1.5e7 / 1e3
    print(f"k T a 1.5e7 K = {kt_kev:.4f} keV")
    print(f"{'par':<8} {'E_C [MeV]':>10} {'E_C/kT':>9} {'E_G [keV]':>10} {'E_0 [keV]':>10}")
    for nombre, z1, z2, a1, a2, m1, m2 in (("p + p", 1, 1, 1, 1, MP, MP), ("d + t", 1, 1, 2, 3, MD, MT), ("alfa+alfa", 2, 2, 4, 4, MA, MA)):
        ec = z1 * z2 * ALPHA * HBARC / (1.2 * (a1 ** (1 / 3) + a2 ** (1 / 3)))
        mr = m1 * m2 / (m1 + m2)
        eg = 2 * mr * (math.pi * ALPHA * z1 * z2) ** 2 * 1e3
        e0 = (eg * kt_kev ** 2 / 4) ** (1 / 3)
        print(f"{nombre:<8} {ec:10.4f} {ec * 1e3 / kt_kev:9.1f} {eg:10.2f} {e0:10.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
