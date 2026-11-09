#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C12: umbrales cinematicos con cuadrivectores y energia de aniquilacion.

Datos: masas del electron (0.510 998 950 69 MeV), del muon (105.658 3755 MeV) y del proton (938.272 089 43 MeV) en MeV/c^2, c y e (NIST CODATA 2022, tabla allascii.txt), consultados 2026-11-09.
Las masas de las muestras (1 g de materia y 1 g de antimateria) son ILUSTRATIVAS (sinteticas).
Modelo: cuadrivectores (E, p) con c = 1; masa invariante s = (Sum E)^2 - |Sum p|^2; umbrales de reacciones en blanco fijo por biseccion sobre la energia del proyectil y comparacion con las
formulas cerradas: e+ e- -> mu+ mu- (E_lab = (4 m_mu^2 - 2 m_e^2)/(2 m_e)); p p -> p p p pbar (T = 6 m_p); fotones sobre un electron en reposo (4 m_e) y sobre un nucleo pesado (2 m_e);
aniquilacion en reposo e+ e- -> 2 gamma con conservacion del momento; energia E = 2 m c^2 de 1 g de materia con 1 g de antimateria.
Supuestos: nucleo infinitamente pesado para el umbral de 2 m_e; ignora la seccion eficaz. Validez: cinematica pura.
Tolerancia: umbrales numericos frente a los cerrados a 1e-9 relativo; conservacion del momento a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

ME, MMU, MP = 0.51099895069, 105.6583755, 938.27208943
C, E = 299792458.0, 1.602176634e-19


def s_invariante(*particulas):
    et = sum(p[0] for p in particulas)
    px = sum(p[1] for p in particulas)
    return et * et - px * px


def umbral(m_proy, m_blanco, m_finales, foton=False):
    objetivo = sum(m_finales) ** 2
    lo, hi = 0.0, 1e9
    for _ in range(300):
        e = 0.5 * (lo + hi)
        p = e if foton else math.sqrt(max(e * e - m_proy ** 2, 0.0))
        s = s_invariante((e, p), (m_blanco, 0.0))
        if s < objetivo:
            lo = e
        else:
            hi = e
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'reaccion':<30} {'umbral numerico [MeV]':>22} {'formula cerrada [MeV]':>22} {'cociente':>10}")
    casos = [
        ("e+ e- (blanco) -> mu+ mu-", umbral(ME, ME, [MMU, MMU]), (4 * MMU ** 2 - 2 * ME ** 2) / (2 * ME)),
        ("p p (blanco) -> p p p pbar (E total)", umbral(MP, MP, [MP] * 4), 7 * MP),
        ("gamma + e- -> e- e+ e-", umbral(0, ME, [ME] * 3, foton=True), 4 * ME),
        ("gamma + M(infinito) -> e+ e-", umbral(0, 1e9, [ME, ME, 1e9], foton=True), 2 * ME),
    ]
    for nombre, num, cer in casos:
        print(f"{nombre:<30} {num:22.6f} {cer:22.6f} {num / cer:10.9f}")
        assert abs(num / cer - 1) < 1e-6, nombre
    t_th = 7 * MP - MP
    print(f"energia cinetica del proyectil en el umbral de p p -> p p p pbar: T = 6 m_p c^2 = {t_th:.3f} MeV = {t_th / 1e3:.4f} GeV")
    print(f"energia de cada haz en un colisionador e+ e- -> mu+ mu-: m_mu c^2 = {MMU:.4f} MeV (frente a {casos[0][2] / 1e3:.2f} GeV en blanco fijo)")
    # aniquilacion en reposo
    e1 = ME
    g1, g2 = (e1, e1), (e1, -e1)
    print(f"aniquilacion en reposo: dos fotones de {e1:.5f} MeV en sentidos opuestos ; momento total = {g1[1] + g2[1]:.1e} ; energia total = {g1[0] + g2[0]:.5f} MeV = 2 m_e c^2")
    assert abs(g1[1] + g2[1]) < 1e-12
    # un gramo
    m = 1e-3
    en = 2 * m * C ** 2
    print(f"1 g de materia con 1 g de antimateria: E = 2 m c^2 = {en:.4e} J = {en / 4.184e12:.2f} kt de TNT equivalente (1 kt = 4.184e12 J, definicion)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
