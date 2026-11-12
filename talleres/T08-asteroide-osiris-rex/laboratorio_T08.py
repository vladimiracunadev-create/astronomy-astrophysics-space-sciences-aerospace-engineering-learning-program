# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T08 (asteroide Bennu, OSIRIS-REx).

Secciones: 1 un cuerpo diminuto · 2 por qué ir a un asteroide cuesta más de lo que parece · 3 órbitas cercanas ·
4 toma de muestra y retardo · 5 regreso y reentrada · 6 masa de propelente · 7 fiabilidad y costo.

UNIDADES: km, m, s, kg, g, m/s, km/s; costos en miles de millones de USD (GUSD).
SISTEMA DE REFERENCIA: heliocéntrico (traslado); asteroidocéntrico (órbitas cercanas y muestreo); geocéntrico (regreso).
MODELO: cuerpo esférico con GM constante (Bennu es casi esférico, con forma de peonza); órbitas circulares.
TOLERANCIA: ±20 % cerca del cuerpo (la gravedad no es uniforme); ±10 % en la geometría heliocéntrica.
DATOS: constantes de referencia pública redondeadas (⚠ verificar): GM ≈ 4,9 m³/s², radio medio ≈ 245 m.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

GM_B = 4.892        # m^3/s^2
R_B = 245.0         # m


def cuerpo() -> dict:
    return {"g": GM_B / R_B**2, "v_esc": math.sqrt(2 * GM_B / R_B), "v_circ_1km": math.sqrt(GM_B / 1000.0),
            "t_1km_h": 2 * math.pi * math.sqrt(1000.0**3 / GM_B) / 3600}


def periodo_orbita(r_m: float) -> float:
    return 2 * math.pi * math.sqrt(r_m**3 / GM_B) / 3600


def plano() -> dict:
    a = 1.126 * UA
    h = hohmann(UA, a)
    incl = math.radians(6.03)
    cambio = 2 * circular(MU_SOL, UA) * math.sin(incl / 2)
    return {"v_inf_hohmann": h["v_inf_salida"], "cambio_plano": cambio, "c3_real": 28.0}


def muestreo() -> dict:
    luz_min_tag = 18.5
    contacto_s = 5.0
    return {"luz_s": luz_min_tag * 60, "contacto_s": contacto_s, "razon": luz_min_tag * 60 / contacto_s}


def regreso(v_entrada: float = 12.4, alt_km: float = 125.0) -> dict:
    r = R_TIERRA + alt_km
    v_esc = math.sqrt(2 * MU_TIERRA / r)
    v_inf = math.sqrt(v_entrada**2 - v_esc**2)
    return {"v_esc": v_esc, "v_inf": v_inf, "km_h": v_entrada * 3600, "e_mj_kg": v_entrada**2 / 2}


def propelente(m_seca: float = 880.0, m_prop: float = 1230.0, isp: float = 230.0) -> dict:
    return {"dv_kms": cohete_dv(isp, m_seca + m_prop, m_seca), "razon": (m_seca + m_prop) / m_seca}


def fiabilidad() -> float:
    ev = {"lanzamiento": 0.98, "asistencia por la Tierra": 0.99, "aproximación y captura de forma": 0.97,
          "órbitas a ≈ 1 km": 0.97, "toma de muestra (contacto de ≈ 5 s)": 0.90, "salida y crucero de 2,4 años": 0.97,
          "reentrada a 12,4 km/s": 0.98, "paracaídas y recuperación": 0.98}
    return serie(list(ev.values()))


def main() -> None:
    print("TALLER T08 - Asteroide Bennu (OSIRIS-REx): laboratorio de diseño preliminar\n")
    c = cuerpo()
    print("1. UN CUERPO DIMINUTO (GM = 4,892 m³/s², radio 245 m)")
    print(f"   gravedad en la superficie : {c['g'] * 1e5:.1f} cienmilésimas de m/s² (≈ {c['g'] / 9.80665 * 1e6:.1f} millonésimas de la terrestre)")
    print(f"   velocidad de escape       : {c['v_esc'] * 100:.0f} cm/s")
    print(f"   órbita a 1 km             : {c['v_circ_1km'] * 100:.1f} cm/s, período {c['t_1km_h']:.0f} h")
    p = plano()
    print("\n2. POR QUÉ IR A BENNU CUESTA MÁS DE LO QUE PARECE")
    print(f"   transferencia ideal (órbitas circulares y coplanares): v∞ = {p['v_inf_hohmann']:.2f} km/s")
    print(f"   pero su órbita está inclinada 6°: cambiar de plano a 29,8 km/s cuesta ≈ {p['cambio_plano']:.2f} km/s")
    print(f"   el lanzamiento real usó un C3 ≈ {p['c3_real']:.0f} km²/s² (⚠): la inclinación manda sobre la distancia")
    print("\n3. ÓRBITAS CERCANAS (período en horas)")
    for r in (700, 1000, 1750, 3000):
        print(f"   a {r:>4} m del centro: {periodo_orbita(r):6.1f} h")
    m = muestreo()
    print("\n4. TOMA DE MUESTRA (TAG)")
    print(f"   retardo de luz a Bennu durante el muestreo: {m['luz_s'] / 60:.1f} min en un sentido")
    print(f"   el contacto dura ≈ {m['contacto_s']:.0f} s: el retardo es {m['razon']:.0f} veces mayor -> secuencia autónoma")
    print("   muestra obtenida ≈ 121,6 g frente a un requisito de 60 g: ×2,0 (⚠ verificar)")
    r = regreso()
    print("\n5. REGRESO A LA TIERRA")
    print(f"   velocidad de entrada ≈ 12,4 km/s (≈ {r['km_h']:,.0f} km/h); escape local {r['v_esc']:.2f} km/s -> v∞ de llegada ≈ {r['v_inf']:.1f} km/s".replace(",", "."))
    print(f"   energía específica de la entrada: {r['e_mj_kg']:.0f} MJ/kg (la de T02 era ≈ 61 MJ/kg)")
    q = propelente()
    print("\n6. PROPELENTE (≈ 1.230 kg sobre una nave seca de ≈ 880 kg, Isp 230 s; ⚠ cifras redondeadas)")
    print(f"   delta-v ideal disponible: {q['dv_kms']:.2f} km/s (razón de masas {q['razon']:.2f})")
    print(f"\n7. FIABILIDAD EN SERIE (ilustrativa): {fiabilidad():.3f}; la toma de muestra pesa más que todo lo demás")
    print("   COSTO de referencia: ≈ 1,16 GUSD (⚠ verificar; sin contar parte del lanzamiento)")


if __name__ == "__main__":
    main()
