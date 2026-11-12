# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T02 (Luna, Artemis I).

Secciones: 1 geometría Tierra-Luna · 2 inyección translunar · 3 sobrevuelo lunar · 4 reentrada ·
5 lanzador (empuje/peso y costo por kg) · 6 retardo y enlace · 7 fiabilidad de la secuencia.

UNIDADES: km, s, kg, N, km/s; costos en millones de USD (MUSD).
SISTEMA DE REFERENCIA: geocéntrico inercial para la inyección y la reentrada; selenocéntrico para el sobrevuelo.
MODELO: cónicas de dos cuerpos, Luna en órbita circular. TOLERANCIA: ±5 % (diseño preliminar, no de vuelo).
DATOS: constantes NASA/JPL redondeadas; cifras de la misión redondeadas y de referencia pública.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

A_LUNA = 384400.0  # km, distancia media Tierra-Luna


def geometria() -> dict:
    v_luna = circular(MU_TIERRA, A_LUNA)
    return {"v_luna": v_luna, "periodo_d": periodo(MU_TIERRA, A_LUNA) / 86400, "luz_s": A_LUNA / C_LUZ}


def inyeccion(alt_km: float = 200.0) -> dict:
    r0 = R_TIERRA + alt_km
    at = (r0 + A_LUNA) / 2
    vp = vis_viva(MU_TIERRA, r0, at)
    return {"dv": vp - circular(MU_TIERRA, r0), "v_perigeo": vp, "t_ida_d": periodo(MU_TIERRA, at) / 2 / 86400,
            "v_llegada": vis_viva(MU_TIERRA, A_LUNA, at)}


def sobrevuelo(alt_km: float = 130.0) -> dict:
    r = R_LUNA + alt_km
    return {"v_escape": math.sqrt(2 * MU_LUNA / r), "v_circular": circular(MU_LUNA, r)}


def reentrada(alt_km: float = 122.0) -> dict:
    r = R_TIERRA + alt_km
    v_lunar = math.sqrt(2 * MU_TIERRA / r)   # retorno desde la Luna: v_inf ≈ 0 respecto a la Tierra
    v_leo = circular(MU_TIERRA, r)
    return {"v_lunar": v_lunar, "v_leo": v_leo, "e_lunar": v_lunar**2 / 2, "e_leo": v_leo**2 / 2,
            "razon_e": (v_lunar / v_leo) ** 2, "razon_flujo": (v_lunar / v_leo) ** 3}


def lanzador() -> dict:
    empuje, masa = 39.1e6, 2.6e6   # N y kg al despegue (SLS Block 1, ⚠ redondeado)
    tli_kg = 27000.0                # kg hacia la Luna (referencia pública)
    costo = 4100.0                  # MUSD por lanzamiento (referencia de la oficina de auditoría de la NASA, ⚠)
    return {"emp_peso": empuje / (masa * G0), "usd_por_kg": costo * 1e6 / tli_kg}


def enlace() -> dict:
    return {"luz_s": A_LUNA / C_LUZ, "ida_vuelta_s": 2 * A_LUNA / C_LUZ, "max_km": 432210.0, "luz_max_s": 432210.0 / C_LUZ}


def secuencia() -> dict:
    eventos = {"ascenso y puesta en órbita": 0.985, "inyección translunar": 0.995, "sobrevuelo lunar y DRO": 0.990,
               "salida de la DRO y retorno": 0.990, "separación del módulo de servicio": 0.995,
               "reentrada con rebote": 0.990, "paracaídas y amerizaje": 0.995}
    return {"eventos": eventos, "p": serie(list(eventos.values()))}


def main() -> None:
    print("TALLER T02 - Luna (Artemis I): laboratorio de diseño preliminar\n")
    g = geometria()
    print("1. GEOMETRÍA TIERRA-LUNA (órbita circular de 384.400 km)")
    print(f"   velocidad orbital de la Luna : {g['v_luna']:.3f} km/s")
    print(f"   período                      : {g['periodo_d']:.2f} días  (mes sidéreo; las ventanas se repiten cada mes)")
    print(f"   retardo de luz               : {g['luz_s']:.2f} s en un sentido")
    i = inyeccion()
    print("\n2. INYECCIÓN TRANSLUNAR desde una órbita baja de 200 km")
    print(f"   delta-v                      : {i['dv']:.3f} km/s")
    print(f"   velocidad en el perigeo      : {i['v_perigeo']:.3f} km/s")
    print(f"   tiempo de ida (media órbita) : {i['t_ida_d']:.2f} días  (la misión real tardó ≈ 5 días)")
    print(f"   velocidad al llegar a la Luna: {i['v_llegada']:.3f} km/s respecto a la Tierra")
    s = sobrevuelo()
    print("\n3. SOBREVUELO LUNAR a 130 km de altura")
    print(f"   velocidad de escape local    : {s['v_escape']:.3f} km/s")
    print(f"   velocidad circular local     : {s['v_circular']:.3f} km/s")
    r = reentrada()
    print("\n4. REENTRADA (interfaz a 122 km)")
    print(f"   desde la Luna                : {r['v_lunar']:.2f} km/s  (≈ {r['v_lunar'] * 3600:,.0f} km/h)".replace(",", "."))
    print(f"   desde órbita baja            : {r['v_leo']:.2f} km/s")
    print(f"   energía específica           : {r['e_lunar']:.1f} MJ/kg frente a {r['e_leo']:.1f} MJ/kg (x{r['razon_e']:.1f})")
    print(f"   el flujo de calor crece ≈ con v^3: x{r['razon_flujo']:.1f} respecto a una reentrada desde órbita baja")
    l = lanzador()
    print("\n5. LANZADOR (SLS Block 1, cifras redondeadas)")
    print(f"   empuje / peso al despegue    : {l['emp_peso']:.2f}")
    print(f"   costo por kg hacia la Luna   : {l['usd_por_kg']:,.0f} USD/kg  (4100 MUSD / 27 t)".replace(",", "."))
    e = enlace()
    print("\n6. ENLACE")
    print(f"   retardo ida y vuelta a la Luna     : {e['ida_vuelta_s']:.2f} s")
    print(f"   a la distancia máxima ({e['max_km']:,.0f} km): {e['luz_max_s']:.2f} s en un sentido".replace(",", "."))
    q = secuencia()
    print("\n7. FIABILIDAD DE LA SECUENCIA (valores ilustrativos)")
    for k, v in q["eventos"].items():
        print(f"   {k:<38}: {v:.3f}")
    print(f"   probabilidad de éxito en serie: {q['p']:.4f}  ({(1 - q['p']) * 100:.1f} % de riesgo)")


if __name__ == "__main__":
    main()
