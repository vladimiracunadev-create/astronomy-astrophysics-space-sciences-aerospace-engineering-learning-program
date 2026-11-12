# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T10 (defensa planetaria, DART).

Secciones: 1 el sistema Didymos-Dimorphos · 2 el impacto: cantidad de movimiento · 3 efecto en el período orbital ·
4 navegación terminal y tiempos · 5 cuánta anticipación hace falta · 6 fiabilidad y costo.

UNIDADES: m, km, s, kg, m/s, mm/s, min, h; costos en millones de USD (MUSD).
SISTEMA DE REFERENCIA: Dimorphos en órbita circular alrededor de Didymos (selenocéntrico análogo); impacto en el plano orbital.
MODELO: órbita circular, impacto frontal tangencial (retrógrado), factor de aumento de cantidad de movimiento β.
TOLERANCIA: ±20 % en masas y β (incertidumbres reales mayores); no sirve para planificar una defensa real.
DATOS: cifras públicas redondeadas (⚠ verificar): masa de Dimorphos ≈ 4,3·10⁹ kg, órbita de ≈ 1,2 km, período ≈ 11,9 h.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

G = 6.674e-11
M_DIM = 4.3e9       # kg
M_DID = 5.3e11      # kg
A_ORB = 1190.0      # m, semieje de la órbita de Dimorphos
T_ORB = 11.92 * 3600
M_NAVE = 580.0      # kg al impacto
V_IMP = 6.1e3       # m/s


def sistema() -> dict:
    gm = G * (M_DID + M_DIM)
    t = 2 * math.pi * math.sqrt(A_ORB**3 / gm)
    return {"v_orb": 2 * math.pi * A_ORB / T_ORB, "periodo_h": t / 3600, "v_escape_dim": math.sqrt(2 * G * M_DIM / 80.0)}


def impacto(beta: float) -> float:
    """Cambio de velocidad de Dimorphos en m/s (impacto tangencial, retrógrado)."""
    return beta * M_NAVE * V_IMP / M_DIM


def cambio_periodo(dv: float) -> dict:
    s = sistema()
    v = s["v_orb"]
    frac = 3 * dv / v
    return {"frac": frac, "min": frac * T_ORB / 60}


def navegacion() -> dict:
    d_km = 11e6
    t_ultimas = 4 * 3600
    return {"luz_s": d_km * 1e3 / (C_LUZ * 1e3), "v_ms": V_IMP, "dist_ultima_hora_km": V_IMP * 3600 / 1000,
            "t_ultimos_4m": 4 * 60, "dist_4min_km": V_IMP * 240 / 1000, "dist_2min_km": V_IMP * 120 / 1000,
            "dist_20s_km": V_IMP * 20 / 1000}


def anticipacion(masa_objeto: float, dv_necesario_ms: float) -> dict:
    """Impulso requerido para desviar un objeto: a mayor anticipación, menor dv (cambio de posición ≈ dv · tiempo · factor)."""
    fac = 3.0    # desplazamiento a lo largo de la órbita ≈ 3 · dv · t (resonancias y deriva)
    r_tierra_km = R_TIERRA
    res = []
    for anios in (1, 5, 10, 20):
        dv = r_tierra_km * 1000 / (fac * anios * 365.25 * 86400)
        res.append((anios, dv * 1000))   # mm/s
    return {"filas": res}


def fiabilidad() -> float:
    ev = {"lanzamiento": 0.98, "crucero de 10 meses": 0.98, "detección de los dos objetos": 0.97,
          "separación del microsatélite de observación": 0.98, "navegación autónoma terminal": 0.93,
          "impacto en un blanco de 160 m": 0.90}
    return serie(list(ev.values()))


def main() -> None:
    print("TALLER T10 - Defensa planetaria (DART): laboratorio de diseño preliminar\n")
    s = sistema()
    print("1. EL SISTEMA DIDYMOS-DIMORPHOS (blanco de 160 m en órbita de 1.190 m alrededor de un cuerpo de 780 m)")
    print(f"   velocidad orbital de Dimorphos : {s['v_orb'] * 100:.1f} cm/s")
    print(f"   período calculado con las masas: {s['periodo_h']:.2f} h (el medido era ≈ 11,9 h)")
    print("\n2. EL IMPACTO (580 kg a 6,1 km/s)")
    p = M_NAVE * V_IMP
    print(f"   cantidad de movimiento de la nave: {p / 1e6:.2f} · 10⁶ kg·m/s")
    for beta in (1.0, 2.0, 3.6, 5.0):
        dv = impacto(beta)
        print(f"   β = {beta:3.1f}: Dimorphos cambia su velocidad en {dv * 1000:5.2f} mm/s")
    print("   β es el factor de aumento de la cantidad de movimiento: los restos expulsados empujan más que la nave sola (la medición dio β ≈ 3,6; ⚠)")
    print("\n3. EFECTO EN EL PERÍODO ORBITAL (cambio fraccional ≈ 3 Δv / v)")
    for beta in (1.0, 2.0, 3.6, 5.0):
        c = cambio_periodo(impacto(beta))
        print(f"   β = {beta:3.1f}: el período se acorta en {c['min']:5.1f} min ({c['frac'] * 100:.1f} %)")
    print("   el cambio observado fue de ≈ 33 min (⚠); el modelo con β ≈ 3,6 da el orden de magnitud")
    n = navegacion()
    print("\n4. NAVEGACIÓN TERMINAL")
    print(f"   la nave va a {n['v_ms'] / 1000:.1f} km/s: en la última hora recorre {n['dist_ultima_hora_km']:.0f} km")
    print(f"   en los últimos 4 min: {n['dist_4min_km']:.0f} km; en los últimos 2 min: {n['dist_2min_km']:.0f} km; en los últimos 20 s: {n['dist_20s_km']:.0f} km")
    print(f"   retardo de luz a 11 millones de km: {n['luz_s']:.0f} s -> la guía debe ser autónoma")
    print("\n5. CUÁNTA ANTICIPACIÓN HACE FALTA (desplazar un objeto un radio terrestre)")
    for anios, dv in anticipacion(1e10, 0)["filas"]:
        print(f"   con {anios:>2} años de antelación basta un cambio de velocidad de ≈ {dv:.1f} mm/s")
    print("   lección: detectar pronto vale más que empujar fuerte")
    print(f"\n6. FIABILIDAD EN SERIE (ilustrativa): {fiabilidad():.3f}; COSTO de referencia ≈ 325 MUSD sin el lanzamiento (⚠ verificar)")


if __name__ == "__main__":
    main()
