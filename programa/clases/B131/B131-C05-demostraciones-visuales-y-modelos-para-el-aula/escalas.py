#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C05: modelos a escala del Sistema Solar y fase lunar como geometria.

CONTENIDO EDUCATIVO. CONSULTADOS (2026-11-11): IAU 2015, Resolucion B3 (PDF leido con PyMuPDF): radio solar nominal 6.957e8 m, radio ecuatorial
nominal de la Tierra 6.3781e6 m, radio ecuatorial nominal de Jupiter 7.1492e7 m.
NO CONSULTADOS (valores estandar de memoria, tratados como ilustrativos): 1 UA = 1.495978707e11 m; semiejes (UA) Mercurio 0.387, Venus 0.723,
Tierra 1.000, Marte 1.524, Jupiter 5.203, Saturno 9.537, Urano 19.19, Neptuno 30.07; distancia Tierra-Luna 3.844e8 m; radio lunar 1.7374e6 m;
mes sinodico 29.530589 d.
Unidades: m, cm, mm, UA; angulos en grados. Tolerancias: fraccion iluminada analitica (1 + cos i)/2 frente a Monte Carlo de 400000 puntos en el disco (semilla 131) < 3e-3.
Seguridad: el modelo es una maqueta; no incluye ninguna observacion del Sol.
"""
from __future__ import annotations
import math, platform, random

R_SOL, R_TIERRA, R_JUP = 6.957e8, 6.3781e6, 7.1492e7
UA = 1.495978707e11
SEMIEJES = {"Mercurio": 0.387, "Venus": 0.723, "Tierra": 1.000, "Marte": 1.524, "Jupiter": 5.203, "Saturno": 9.537, "Urano": 19.19, "Neptuno": 30.07}
D_TL, R_LUNA = 3.844e8, 1.7374e6


def frac_iluminada(i_deg):
    return (1 + math.cos(math.radians(i_deg))) / 2


def frac_numerica(i_deg, n=400000, semilla=131):
    """Monte Carlo: puntos uniformes en el disco visible; cada uno es la normal de la esfera (x, y, z) y esta iluminado si n.s > 0,
    con s la direccion del Sol (z hacia la Tierra; i = angulo de fase)."""
    rng = random.Random(semilla)
    i = math.radians(i_deg)
    s = (math.sin(i), 0.0, math.cos(i))
    dentro = ilum = 0
    while dentro < n:
        x, y = rng.uniform(-1, 1), rng.uniform(-1, 1)
        r2 = x * x + y * y
        if r2 > 1:
            continue
        dentro += 1
        if x * s[0] + math.sqrt(1 - r2) * s[2] > 0:
            ilum += 1
    return ilum / dentro


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Radios IAU 2015 B3 CONSULTADOS; semiejes, UA, Luna y mes sinodico ESTANDAR NO CONSULTADOS (ilustrativos).")
    # 1) modelo con Sol de diametro D cm
    for d_sol_cm in (10.0, 100.0):
        k = d_sol_cm / 100 / (2 * R_SOL)  # m de modelo por m real
        print(f"\nModelo A (misma escala para tamano y distancia), Sol de {d_sol_cm:.0f} cm de diametro (1 : {1 / k:.3e})")
        print("  cuerpo      diametro      distancia al Sol")
        d_t = 2 * R_TIERRA * k
        d_j = 2 * R_JUP * k
        print(f"  Tierra      {d_t * 1000:8.3f} mm   {SEMIEJES['Tierra'] * UA * k:9.2f} m")
        print(f"  Jupiter     {d_j * 1000:8.3f} mm   {SEMIEJES['Jupiter'] * UA * k:9.2f} m")
        print(f"  Neptuno (distancia)             {SEMIEJES['Neptuno'] * UA * k:9.2f} m")
    # 2) caben en el aula? Neptuno a 8 m
    k_aula = 8.0 / (SEMIEJES["Neptuno"] * UA)
    print(f"\nModelo B (Neptuno a 8 m en el aula): Sol de {2 * R_SOL * k_aula * 1000:.2f} mm ; Tierra de {2 * R_TIERRA * k_aula * 1000:.4f} mm ; Tierra a {SEMIEJES['Tierra'] * UA * k_aula:.3f} m")
    print("  -> la Tierra es menor que un grano de polvo visible; no se puede mostrar a la vez distancia y tamano en un aula.")
    # 3) razon de tamanos y cuanto hay que agrandar para ver planetas
    razon = (SEMIEJES["Tierra"] * UA) / (2 * R_SOL)
    print(f"Distancia Tierra-Sol / diametro solar = {razon:.1f} ; angulo del Sol visto desde la Tierra = {math.degrees(2 * math.atan(R_SOL / (UA))):.3f} deg")
    # 4) Tierra-Luna: Tierra de 5 cm
    k_tl = 0.05 / (2 * R_TIERRA)
    print(f"\nModelo Tierra-Luna con Tierra de 5 cm: Luna de {2 * R_LUNA * k_tl * 100:.2f} cm a {D_TL * k_tl:.2f} m")
    # 5) fases: analitico frente a numerico
    print("\nFase lunar: fraccion iluminada k = (1 + cos i)/2, i = angulo de fase (Sol-Luna-Tierra)")
    print("  i[deg]  k analitica  k Monte Carlo  dia aprox. (i = 180 deg al dia 0)")
    err = 0.0
    for i in (0, 45, 90, 135, 180):
        ka, kn = frac_iluminada(i), frac_numerica(i)
        err = max(err, abs(ka - kn))
        dia = (180 - i) / 360 * 29.530589
        print(f"  {i:5d}   {ka:10.4f}   {kn:10.4f}   {dia:6.2f}")
    print(f"Error maximo analitica-Monte Carlo = {err:.2e}")
    assert err < 3e-3
    assert abs(frac_iluminada(0) - 1) < 1e-12 and abs(frac_iluminada(90) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
