# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T06 (cometa 67P, Rosetta y Philae).

Secciones: 1 un cuerpo de gravedad casi nula · 2 energía solar a distancias distintas · 3 aterrizaje y rebote ·
4 órbitas cercanas · 5 enlace · 6 hibernación y fiabilidad · 7 costo.

UNIDADES: km, m, s, kg, W, m/s; UA para distancias al Sol; costos en miles de millones de euros (GEUR).
SISTEMA DE REFERENCIA: cometocéntrico (cuerpo fijo, sin rotación en el modelo) y heliocéntrico para el flujo solar.
MODELO: cuerpo esférico y homogéneo con GM constante; flujo solar ∝ 1/d²; rebote con coeficiente de restitución.
TOLERANCIA: ±20 % (el cometa es muy irregular y su gravedad cambia de un lugar a otro). No sirve para vuelo.
DATOS: constantes de referencia pública redondeadas (⚠ verificar): radio medio ≈ 1,7 km, GM ≈ 666 m³/s².
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

GM = 666.0          # m^3/s^2 (⚠)
R_MEDIO = 1700.0    # m (radio medio equivalente)


def cuerpo() -> dict:
    g = GM / R_MEDIO**2
    return {"g": g, "v_escape": math.sqrt(2 * GM / R_MEDIO), "v_circ": math.sqrt(GM / R_MEDIO),
            "peso_kg_100": 100 * g, "periodo_h": 2 * math.pi * R_MEDIO / math.sqrt(GM / R_MEDIO) / 3600,
            "g_tierra_rel": g / 9.80665}


def solar() -> list[tuple[str, float, float]]:
    pts = [("Tierra (1 UA)", 1.0), ("Marte (1,5 UA)", 1.5), ("Cinturón (3 UA)", 3.0), ("Hibernación (5,3 UA)", 5.3), ("Perihelio del cometa (1,24 UA)", 1.24)]
    return [(n, d, flujo_solar(d)) for n, d in pts]


def panel(area_m2: float, eficiencia: float, d_ua: float) -> float:
    return area_m2 * eficiencia * flujo_solar(d_ua)


def rebote(v0: float = 1.0, e: float = 0.3, g: float = GM / R_MEDIO**2) -> dict:
    """Altura y tiempo del primer rebote vertical con coeficiente de restitución e."""
    v1 = e * v0
    return {"v1": v1, "altura_m": v1**2 / (2 * g), "t_s": 2 * v1 / g, "v_esc": math.sqrt(2 * GM / R_MEDIO)}


def orbita(r_km: float) -> dict:
    r = r_km * 1000
    v = math.sqrt(GM / r)
    return {"v_ms": v, "periodo_dias": 2 * math.pi * r / v / 86400, "v_cm_s": v * 100}


def enlace(dist_ua: float = 3.0) -> dict:
    return {"luz_min": luz_min(dist_ua * UA)}


def hibernacion() -> dict:
    dias = 957
    return {"dias": dias, "anios": dias / 365.25}


def fiabilidad() -> float:
    ev = {"ensamble y lanzamiento": 0.99, "cuatro asistencias planetarias": 0.98, "dos pasos por asteroides": 0.995,
          "hibernación de 2,6 años": 0.97, "encendido tras la hibernación": 0.97, "inserción en torno al cometa": 0.97,
          "separación y descenso de la sonda": 0.85}
    return serie(list(ev.values()))


def main() -> None:
    print("TALLER T06 - Cometa 67P (Rosetta y Philae): laboratorio de diseño preliminar\n")
    c = cuerpo()
    print("1. UN CUERPO DE GRAVEDAD CASI NULA (modelo esférico, GM = 666 m³/s², radio 1,7 km)")
    print(f"   gravedad en la superficie : {c['g'] * 1000:.2f} mm/s²  (= {c['g_tierra_rel'] * 1e5:.1f} cienmilésimas de la terrestre)")
    print(f"   velocidad de escape       : {c['v_escape']:.2f} m/s  (¡caminando rápido se escaparía!)")
    print(f"   velocidad orbital rasante : {c['v_circ']:.2f} m/s, período {c['periodo_h']:.1f} h")
    print(f"   un cuerpo de 100 kg 'pesa' : {c['peso_kg_100'] * 1000:.0f} mN (el peso de {c['peso_kg_100'] / 9.80665 * 1000:.0f} g en la Tierra)")
    print("\n2. ENERGÍA SOLAR A DISTINTAS DISTANCIAS (flujo en W/m² y potencia de 64 m² de paneles al 18 %)")
    for n, d, f in solar():
        print(f"   {n:<34}: {f:7.1f} W/m² -> {panel(64, 0.18, d):6.0f} W")
    print("   a 5,3 UA los paneles casi no alcanzan: por eso la sonda hibernó")
    r = rebote()
    print("\n3. ATERRIZAJE Y REBOTE (llegada a 1 m/s, coeficiente de restitución 0,3)")
    print(f"   velocidad tras el primer rebote: {r['v1']:.2f} m/s (el escape es {r['v_esc']:.2f} m/s)")
    print(f"   altura del primer rebote       : {r['altura_m']:.0f} m; tiempo en el aire: {r['t_s'] / 3600:.1f} h")
    print("   con esa gravedad un rebote dura horas: Philae rebotó ≈ 2 horas y luego otra vez (⚠ verifica los tiempos)")
    print("\n4. ÓRBITAS CERCANAS ALREDEDOR DEL COMETA")
    for km in (10, 20, 30):
        o = orbita(km)
        print(f"   a {km:>2} km de altura: {o['v_cm_s']:5.1f} cm/s, período {o['periodo_dias']:5.1f} días")
    e = enlace()
    print(f"\n5. ENLACE: a 3 UA la luz tarda {e['luz_min']:.0f} min en un sentido (a 5,3 UA, ≈ 44 min)")
    h = hibernacion()
    print(f"\n6. HIBERNACIÓN: {h['dias']} días ({h['anios']:.1f} años); fiabilidad de la cadena (ilustrativa): {fiabilidad():.3f}")
    print("\n7. COSTO de referencia: ≈ 1,4 GEUR para el conjunto de la misión de la ESA (⚠ verificar)")


if __name__ == "__main__":
    main()
