# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T05 (Saturno, Cassini-Huygens).

Secciones: 1 por qué hacen falta asistencias · 2 efecto de un sobrevuelo planetario · 3 inserción en órbita de Saturno ·
4 sonda en Titán · 5 energía y enlace · 6 fin de la misión · 7 fiabilidad y costo.

UNIDADES: km, s, kg, W, km/s, m/s; costos en miles de millones de USD (GUSD).
SISTEMA DE REFERENCIA: heliocéntrico (transferencias) y planetocéntrico (sobrevuelos, inserción, descenso).
MODELO: cónicas de dos cuerpos, sobrevuelo instantáneo (esfera de influencia nula), atmósfera exponencial.
TOLERANCIA: ±10 % en sobrevuelos e inserción; ±30 % en el descenso por paracaídas. No sirve para vuelo.
DATOS: constantes NASA/JPL redondeadas; cifras de la misión de referencia pública redondeadas (⚠ verificar).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

R_SATURNO = 60268.0
A_SATURNO = 9.5388 * UA


def necesidad() -> dict:
    h = hohmann(UA, A_SATURNO)
    c3_directo = h["v_inf_salida"] ** 2
    return {"v_inf": h["v_inf_salida"], "c3": c3_directo, "anios": h["t_vuelo_s"] / (365.25 * 86400),
            "v_llegada": h["v_inf_llegada"]}


def sobrevuelo(v_inf: float, mu: float, rp: float) -> dict:
    """Giro máximo de la velocidad relativa en un sobrevuelo con periapsis rp y su cambio de velocidad heliocéntrica."""
    s = 1 / (1 + rp * v_inf**2 / mu)
    delta = 2 * math.asin(s)
    return {"giro_grados": math.degrees(delta), "dv": 2 * v_inf * s}


def insercion(v_inf: float = 5.5, rp: float = 78000.0, periodo_dias: float = 116.0) -> dict:
    t = periodo_dias * 86400
    a = (MU_SATURNO * (t / (2 * math.pi)) ** 2) ** (1 / 3)
    ra = 2 * a - rp
    v_h = math.sqrt(v_inf**2 + 2 * MU_SATURNO / rp)
    v_e = vis_viva(MU_SATURNO, rp, a)
    return {"dv": v_h - v_e, "ra": ra, "a": a, "v_h": v_h}


def titan(masa: float = 318.0, rho: float = 5.4, g: float = 1.352, cd: float = 1.5, d_paracaidas: float = 3.0) -> dict:
    area = math.pi * (d_paracaidas / 2) ** 2
    v_term = math.sqrt(2 * masa * g / (rho * cd * area))
    h_escala = 20.0  # km
    return {"v_terminal": v_term, "h_escala": h_escala}


def energia() -> dict:
    p0 = 885.0
    return {"p": lambda a: rtg(p0, a, degradacion_anual=0.008),
            "luz_min": (luz_min(8.2 * UA), luz_min(10.1 * UA))}


def fin() -> dict:
    v_esc = math.sqrt(2 * MU_SATURNO / R_SATURNO)
    return {"v_escape": v_esc, "v_circ": circular(MU_SATURNO, R_SATURNO)}


def fiabilidad() -> float:
    ev = {"lanzamiento": 0.98, "cuatro sobrevuelos": 0.99, "inserción en Saturno": 0.97, "liberación de Huygens": 0.98,
          "descenso en Titán": 0.95}
    return serie(list(ev.values()))


def main() -> None:
    print("TALLER T05 - Saturno (Cassini-Huygens): laboratorio de diseño preliminar\n")
    n = necesidad()
    print("1. POR QUÉ HACEN FALTA ASISTENCIAS: transferencia de Hohmann Tierra-Saturno (9,54 UA)")
    print(f"   v∞ necesaria al salir : {n['v_inf']:.2f} km/s  -> C3 = {n['c3']:.0f} km²/s²")
    print(f"   tiempo de vuelo       : {n['anios']:.1f} años")
    print("   el cohete lanzó la nave con un C3 de ≈ 16 km²/s² (⚠): faltaba mucha energía; la aportaron Venus, la Tierra y Júpiter")
    print("\n2. SOBREVUELOS (giro máximo de la velocidad y cambio de velocidad respecto al Sol)")
    for nombre, v_inf, mu, rp in (("Tierra 1999 (a 1.166 km de altura)", 16.9, MU_TIERRA, R_TIERRA + 1166),
                                  ("Júpiter 2000 (a ≈ 9,7 millones de km)", 5.7, MU_JUPITER, 9.7e6),
                                  ("Venus 1999 (a ≈ 600 km)", 11.0, MU_VENUS, 6052 + 600)):
        s = sobrevuelo(v_inf, mu, rp)
        print(f"   {nombre:<42}: giro {s['giro_grados']:5.1f}°  -> Δv de dirección ≈ {s['dv']:.2f} km/s")
    i = insercion()
    print("\n3. INSERCIÓN EN ÓRBITA DE SATURNO (periapsis 78.000 km, v∞ = 5,5 km/s, órbita de 116 días)")
    print(f"   velocidad en el periapsis antes de frenar: {i['v_h']:.2f} km/s")
    print(f"   delta-v del freno                         : {i['dv'] * 1000:.0f} m/s  (la real fue ≈ 626 m/s)")
    print(f"   apoapsis de la órbita obtenida            : {i['ra'] / 1e6:.1f} millones de km")
    print(f"   combustible para 626 m/s en una nave de ≈ 4.600 kg (Isp 320 s): {masa_propelente(0.626, 320, 4600):.0f} kg")
    tt = titan()
    print("\n4. HUYGENS EN TITÁN (318 kg, paracaídas pequeño de 3 m)")
    print(f"   velocidad terminal cerca del suelo: {tt['v_terminal']:.1f} m/s  (el contacto real fue de unos 4-5 m/s)")
    print("   atmósfera de ≈ 1,5 bar y gravedad de 1,35 m/s²: se frena con paracaídas durante ≈ 2,5 h")
    e = energia()
    print("\n5. ENERGÍA Y ENLACE")
    for a in (0, 7, 13, 20):
        print(f"   año {a:>2}: {e['p'](a):6.0f} W (3 generadores)")
    print(f"   retardo de luz a Saturno: de {e['luz_min'][0]:.0f} a {e['luz_min'][1]:.0f} min en un sentido")
    f = fin()
    print("\n6. FIN DE LA MISIÓN: ENTRADA EN SATURNO")
    print(f"   velocidad de escape en la cima de las nubes: {f['v_escape']:.1f} km/s; circular: {f['v_circ']:.1f} km/s")
    print(f"\n7. FIABILIDAD EN SERIE (valores ilustrativos): {fiabilidad():.3f}")
    print("   COSTO de referencia: ≈ 3,9 GUSD incluyendo operaciones y contribuciones europeas e italiana (⚠ verificar)")


if __name__ == "__main__":
    main()
