#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C10: elongación máxima, períodos sinódicos y qué planetas se ven.

Datos PUBLICADOS: distancias al Sol (UA) y períodos orbitales (años terrestres) de la NASA, «Planetary Fact Sheet -
Ratio to Earth Values», act. 18-mar-2025, consultada 2026-11-05 (solo 3 cifras significativas); período sidéreo de la
Tierra 365,256 d (NASA Earth Fact Sheet). Modelo (SIMULADO): órbitas circulares y coplanares. Dominio: orden de magnitud
de los intervalos; las excentricidades reales cambian los resultados unos %. Tolerancias: 1 % en períodos sinódicos de
Venus y Júpiter, 3 % en Marte; 0,01 grados en la elongación máxima numérica.
Referencia independiente: fechas de conjunciones y oposiciones calculadas con astropy 8.0.2 (get_body, efeméride
integrada en erfa) el 2026-11-05 y copiadas aquí; y elongaciones del 2025-11-05 (mismo origen).
"""
from __future__ import annotations

import math
import sys

D2R = math.pi / 180.0
A_UA = {"Mercurio": 0.387, "Venus": 0.723, "Marte": 1.52, "Jupiter": 5.20, "Saturno": 9.57}   # NASA ratio table
P_AÑOS = {"Mercurio": 0.241, "Venus": 0.615, "Marte": 1.88, "Jupiter": 11.9, "Saturno": 29.4}  # años terrestres
AÑO_D = 365.256   # NASA Earth Fact Sheet

# Intervalos de la referencia astropy (días): Venus entre conjunciones inferiores consecutivas (2024-06-04 -> 2027-08-11, 2 ciclos),
# Marte entre oposiciones 2025-01-16 y 2027-02-19, Júpiter entre oposiciones 2024-12-08, 2026-01-10, 2027-02-11, 2028-03-12 (promedio)
REF_SINODICO_D = {"Venus": 581.5, "Marte": 764.75, "Jupiter": 396.92}
# 2025-11-05 00:00 UT, referencia astropy: (elongación grados, lado)
REF_ELONGACION = {"Mercurio": (22.72, "este"), "Venus": (15.32, "oeste"), "Marte": (17.51, "este"),
                  "Jupiter": (107.75, "oeste"), "Saturno": (132.75, "este")}
# lat -30,0 lon -70,7; altura en el crepúsculo astronómico vespertino (2025-11-06 00:35 UT) y matutino (08:15 UT), astropy
REF_ALTURAS = {"Mercurio": (2.8, -26.3), "Venus": (-33.0, -10.9), "Marte": (-2.6, -26.4), "Jupiter": (-46.4, 35.9), "Saturno": (61.6, -8.3)}


def elongacion_maxima_analitica(a_ua: float) -> float:
    return math.asin(a_ua) / D2R                       # planeta interior: sen(eps) = a / 1 UA


def elongacion_maxima_numerica(a_ua: float) -> float:
    """Barre la posición del planeta en su órbita circular y busca la mayor separación Sol-planeta visto desde la Tierra."""
    mejor = 0.0
    for k in range(0, 36000):
        th = k * 0.01 * D2R                            # ángulo Sol-centro: planeta en (a cos th, a sen th); Tierra en (1,0)
        px, py = a_ua * math.cos(th), a_ua * math.sin(th)
        vx, vy = px - 1.0, py                          # vector Tierra->planeta; Sol en (0,0): vector Tierra->Sol = (-1, 0)
        cos_e = (vx * -1.0 + vy * 0.0) / math.hypot(vx, vy)
        mejor = max(mejor, math.acos(max(-1.0, min(1.0, cos_e))) / D2R)
    return mejor


def sinodico_dias(p_años: float) -> float:
    return AÑO_D / abs(1.0 - 1.0 / p_años)          # 1/S = |1/P_Tierra - 1/P_planeta| con P_Tierra = 1 año


def pruebas() -> None:
    for nombre in ("Mercurio", "Venus"):
        assert abs(elongacion_maxima_analitica(A_UA[nombre]) - elongacion_maxima_numerica(A_UA[nombre])) < 0.01, nombre
    tol = {"Venus": 0.01, "Jupiter": 0.01, "Marte": 0.03}
    for nombre, ref in REF_SINODICO_D.items():
        s = sinodico_dias(P_AÑOS[nombre])
        assert abs(s - ref) / ref < tol[nombre], (nombre, s, ref)
    # un planeta exterior en oposición está a 180 grados y uno interior nunca supera el máximo
    assert REF_ELONGACION["Venus"][0] < elongacion_maxima_analitica(A_UA["Venus"])


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for n in ("Mercurio", "Venus"):
        print(f"{n}: elongacion maxima (orbita circular) {elongacion_maxima_analitica(A_UA[n]):.1f} grados")
    print("Periodo sinodico (modelo circular, NASA 3 cifras) vs referencia astropy")
    for n in A_UA:
        ref = REF_SINODICO_D.get(n)
        print(f"  {n}: {sinodico_dias(P_AÑOS[n]):6.1f} d" + (f" | astropy {ref} d" if ref else ""))
    print("2025-11-05 00 UT (astropy, SIMULADO): planeta | elongacion | lado | altura al crepusculo astronomico vespertino / matutino (lat -30)")
    for n, (e, lado) in REF_ELONGACION.items():
        print(f"  {n:9s} {e:6.2f} {lado:5s} | {REF_ALTURAS[n][0]:6.1f} / {REF_ALTURAS[n][1]:6.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
