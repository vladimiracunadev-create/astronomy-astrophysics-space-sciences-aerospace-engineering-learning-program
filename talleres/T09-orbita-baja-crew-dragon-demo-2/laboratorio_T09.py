# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T09 (órbita baja tripulada, Crew Dragon Demo-2).

Secciones: 1 la órbita de la estación · 2 alcanzar la estación (fase) · 3 abortos · 4 reentrada y retorno ·
5 soporte vital · 6 riesgo de pérdida de la tripulación · 7 costo por asiento.

UNIDADES: km, s, min, h, kg, N, g (aceleración), km/s; costos en millones de USD (MUSD).
SISTEMA DE REFERENCIA: geocéntrico inercial; fechas en UTC.
MODELO: órbitas circulares y coplanares, Tierra esférica, impulsos instantáneos. TOLERANCIA: ±5 % salvo abortos (±30 %).
DATOS: constantes NASA/JPL redondeadas; cifras de la misión de referencia pública redondeadas (⚠ verificar).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

R_ISS = R_TIERRA + 420.0
R_INI = R_TIERRA + 200.0
LAT_KSC = math.radians(28.5)
INCL = math.radians(51.6)


def estacion() -> dict:
    v = circular(MU_TIERRA, R_ISS)
    per = periodo(MU_TIERRA, R_ISS) / 60
    az = math.degrees(math.asin(math.cos(INCL) / math.cos(LAT_KSC)))
    bono = 0.4651 * math.cos(LAT_KSC) * math.sin(math.radians(az))
    return {"v": v, "periodo_min": per, "azimut": az, "bono_rotacion": bono, "v_util": v - bono}


def fase() -> dict:
    a = (R_INI + R_ISS) / 2
    t_transf = math.pi * math.sqrt(a**3 / MU_TIERRA)
    n_iss = 2 * math.pi / periodo(MU_TIERRA, R_ISS)
    angulo = math.degrees(math.pi - n_iss * t_transf)
    t_ini = periodo(MU_TIERRA, R_INI) / 60
    t_iss = periodo(MU_TIERRA, R_ISS) / 60
    ganancia = 360 * (t_iss - t_ini) / t_iss
    dv1 = vis_viva(MU_TIERRA, R_INI, a) - circular(MU_TIERRA, R_INI)
    dv2 = circular(MU_TIERRA, R_ISS) - vis_viva(MU_TIERRA, R_ISS, a)
    return {"angulo_inicial": angulo, "t_transf_min": t_transf / 60, "t_ini": t_ini, "t_iss": t_iss,
            "ganancia_por_vuelta": ganancia, "dv1": dv1, "dv2": dv2}


def aborto(empuje_total_n: float = 8 * 71000.0) -> list[tuple[float, float]]:
    return [(m, empuje_total_n / m / G0) for m in (9000.0, 10500.0, 12000.0)]


def retorno() -> dict:
    r_per = R_TIERRA + 50.0
    a = (R_ISS + r_per) / 2
    dv = circular(MU_TIERRA, R_ISS) - vis_viva(MU_TIERRA, R_ISS, a)
    v_entrada = circular(MU_TIERRA, R_TIERRA + 122.0)
    return {"dv_desorbita": dv, "v_entrada": v_entrada, "e_mj_kg": v_entrada**2 / 2}


def soporte(personas: int = 2, dias: int = 4, margen: float = 0.3) -> dict:
    o2, co2, agua = 0.84, 1.0, 2.5   # kg por persona y día (valores típicos, ⚠)
    f = personas * dias * (1 + margen)
    return {"o2": o2 * f, "agua": agua * f, "co2": co2 * f}


def riesgo() -> dict:
    p_req = 1 - 1 / 270
    p_shuttle = 1 - 2 / 135
    p_obj = 1 - 1 / 1000
    return {"req": p_req, "shuttle": p_shuttle, "obj": p_obj,
            "diez_req": p_req**10, "diez_shuttle": p_shuttle**10, "diez_obj": p_obj**10}


def asiento() -> dict:
    return {"dragon": 55.0, "soyuz": 86.0, "boeing": 90.0}


def main() -> None:
    print("TALLER T09 - Órbita baja tripulada (Crew Dragon Demo-2): laboratorio de diseño preliminar\n")
    e = estacion()
    print("1. LA ÓRBITA DE LA ESTACIÓN (420 km, inclinación 51,6°)")
    print(f"   velocidad orbital    : {e['v']:.2f} km/s;  período {e['periodo_min']:.1f} min")
    print(f"   azimut de lanzamiento desde 28,5°N: {e['azimut']:.1f}° (hacia el noreste)")
    print(f"   bono de la rotación terrestre (componente hacia el este): {e['bono_rotacion'] * 1000:.0f} m/s -> velocidad que debe dar el cohete ≈ {e['v_util']:.2f} km/s (más pérdidas de ≈ 1,5-1,8 km/s)")
    f = fase()
    print("\n2. ALCANZAR LA ESTACIÓN (de 200 a 420 km)")
    print(f"   delta-v de las dos quemas: {f['dv1'] * 1000:.0f} + {f['dv2'] * 1000:.0f} m/s = {(f['dv1'] + f['dv2']) * 1000:.0f} m/s")
    print(f"   tiempo de la transferencia: {f['t_transf_min']:.0f} min; ángulo de fase inicial: {f['angulo_inicial']:.1f}° (la estación debe ir adelantada)")
    print(f"   períodos: {f['t_ini']:.1f} min a 200 km y {f['t_iss']:.1f} min a 420 km -> se gana {f['ganancia_por_vuelta']:.1f}° por vuelta")
    for ang in (180, 270):
        print(f"   para cerrar {ang}° hacen falta ≈ {ang / f['ganancia_por_vuelta']:.0f} vueltas ≈ {ang / f['ganancia_por_vuelta'] * f['t_ini'] / 60:.0f} h (la misión real tardó ≈ 19 h)")
    print("\n3. ABORTO EN EL ASCENSO: ocho motores de ≈ 71 kN (⚠)")
    for m, g in aborto():
        print(f"   cápsula de {m:>7,.0f} kg: empuje/peso ≈ {g:.1f} -> aceleración neta ≈ {g - 1:.1f} g".replace(",", "."))
    r = retorno()
    print("\n4. RETORNO")
    print(f"   quema de desorbitación (perigeo a 50 km): {r['dv_desorbita'] * 1000:.0f} m/s")
    print(f"   velocidad de entrada ≈ {r['v_entrada']:.2f} km/s; energía {r['e_mj_kg']:.0f} MJ/kg (la mitad que desde la Luna)")
    s = soporte()
    print("\n5. SOPORTE VITAL: 2 personas, 4 días de vuelo libre, 30 % de margen")
    print(f"   oxígeno {s['o2']:.1f} kg; agua {s['agua']:.1f} kg; CO2 a absorber {s['co2']:.1f} kg")
    q = riesgo()
    print("\n6. RIESGO DE PÉRDIDA DE LA TRIPULACIÓN (1 en 270 es un requisito; el transbordador tuvo 2 pérdidas en 135 vuelos)")
    print(f"   probabilidad de volver sano en un vuelo : requisito {q['req'] * 100:.2f} %, transbordador {q['shuttle'] * 100:.2f} %, objetivo 1/1000 {q['obj'] * 100:.2f} %")
    print(f"   en 10 vuelos                            : requisito {q['diez_req'] * 100:.1f} %, transbordador {q['diez_shuttle'] * 100:.1f} %, objetivo {q['diez_obj'] * 100:.1f} %")
    a = asiento()
    print("\n7. COSTO POR ASIENTO (referencias públicas aproximadas, ⚠): Dragon ≈ 55 MUSD; Soyuz ≈ 86 MUSD; Starliner ≈ 90 MUSD")


if __name__ == "__main__":
    main()
