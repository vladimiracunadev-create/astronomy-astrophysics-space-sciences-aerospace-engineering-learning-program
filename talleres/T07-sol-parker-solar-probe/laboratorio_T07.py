# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T07 (Sol, Parker Solar Probe).

Secciones: 1 por qué no se puede ir directo · 2 la órbita final · 3 flujo de calor y temperatura ·
4 paneles solares casi de canto · 5 velocidad, tiempo y enlace · 6 autonomía · 7 costo.

UNIDADES: km, s, m, W/m², K, km/s; UA y radios solares (R☉); costos en miles de millones de USD (GUSD).
SISTEMA DE REFERENCIA: heliocéntrico (órbitas); cuerpo de la nave (térmica).
MODELO: cónicas de dos cuerpos; equilibrio radiativo de placa plana (una o dos caras); sin conducción.
TOLERANCIA: ±10 % en órbitas; ±15 % en temperaturas (propiedades ópticas supuestas). No sirve para vuelo.
DATOS: constantes NASA/JPL redondeadas; cifras de la misión de referencia pública redondeadas (⚠ verificar).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

RP_FINAL = 9.86 * R_SOL      # km, perihelio mínimo (desde el centro del Sol)
RP_PRIMERO = 35.7 * R_SOL


def ir_directo() -> dict:
    a = (UA + RP_FINAL) / 2
    v_afelio = vis_viva(MU_SOL, UA, a)
    dv = circular(MU_SOL, UA) - v_afelio
    return {"dv": dv, "c3": dv**2, "c3_real": 154.0}


def orbita_final(periodo_d: float = 88.0) -> dict:
    t = periodo_d * 86400
    a = (MU_SOL * (t / (2 * math.pi)) ** 2) ** (1 / 3)
    ra = 2 * a - RP_FINAL
    return {"a": a, "ra": ra, "ra_ua": ra / UA, "e": (ra - RP_FINAL) / (ra + RP_FINAL),
            "v_perihelio": vis_viva(MU_SOL, RP_FINAL, a), "v_afelio": vis_viva(MU_SOL, ra, a)}


def termica() -> dict:
    s = S_1UA * (UA / RP_FINAL) ** 2
    return {"flujo": s, "veces": s / S_1UA, "T_ideal": temperatura_equilibrio(s, 1.0, 1.0, 1.0),
            "T_blanca": temperatura_equilibrio(s, 0.7, 1.0, 1.0), "S_primero": S_1UA * (UA / RP_PRIMERO) ** 2}


def paneles(flujo: float, t_max_k: float = 423.0, alfa: float = 0.9, eps: float = 0.9) -> dict:
    cos_t = 2 * eps * SIGMA * t_max_k**4 / (alfa * flujo)
    return {"cos": cos_t, "angulo": math.degrees(math.acos(min(1.0, cos_t)))}


def velocidades() -> dict:
    o = orbita_final()
    return {"v_p": o["v_perihelio"], "t_diametro_s": 2 * R_SOL / o["v_perihelio"], "km_s": o["v_perihelio"],
            "km_h": o["v_perihelio"] * 3600}


def autonomia() -> dict:
    luz_s = UA / C_LUZ
    return {"luz_min": luz_s / 60, "ida_vuelta_min": 2 * luz_s / 60}


def fiabilidad() -> float:
    ev = {"lanzamiento con C3 récord": 0.98, "siete asistencias de Venus": 0.97, "protección térmica": 0.99,
          "autoprotección por apuntado": 0.98, "paneles plegables": 0.98}
    return serie(list(ev.values()))


def main() -> None:
    print("TALLER T07 - Sol (Parker Solar Probe): laboratorio de diseño preliminar\n")
    d = ir_directo()
    print("1. POR QUÉ NO SE PUEDE IR DIRECTO AL SOL (perihelio de 9,86 R☉ desde una órbita terrestre)")
    print(f"   hay que perder {d['dv']:.1f} km/s de velocidad orbital -> C3 ≈ {d['c3']:.0f} km²/s²")
    print(f"   el cohete dio ≈ {d['c3_real']:.0f} km²/s² (récord): no basta; por eso Venus frena a la nave en 7 pasos")
    o = orbita_final()
    print("\n2. LA ÓRBITA FINAL (período de 88 días)")
    print(f"   semieje mayor : {o['a'] / UA:.3f} UA; excentricidad {o['e']:.3f}")
    print(f"   afelio        : {o['ra_ua']:.2f} UA (la órbita de Venus es 0,72 UA)")
    print(f"   velocidad en el perihelio: {o['v_perihelio']:.0f} km/s (≈ {o['v_perihelio'] * 3600:,.0f} km/h)".replace(",", "."))
    print(f"   velocidad en el afelio   : {o['v_afelio']:.1f} km/s")
    t = termica()
    print("\n3. CALOR EN EL PERIHELIO MÍNIMO")
    print(f"   flujo solar: {t['flujo'] / 1000:.0f} kW/m² = {t['veces']:.0f} veces el de la Tierra")
    print(f"   en el primer perihelio (35,7 R☉): {t['S_primero'] / 1000:.0f} kW/m²")
    print(f"   temperatura de equilibrio de una placa que mira al Sol, absorbente ideal : {t['T_ideal']:.0f} K ({t['T_ideal'] - 273.15:.0f} °C)")
    print(f"   con un recubrimiento que absorbe menos de lo que emite (α/ε = 0,7)       : {t['T_blanca']:.0f} K ({t['T_blanca'] - 273.15:.0f} °C)")
    print("   el escudo real llega a ≈ 1.650 K (≈ 1.400 °C) en la cara solar mientras la nave detrás queda cerca de 300 K")
    p = paneles(t["flujo"])
    print("\n4. PANELES SOLARES CASI DE CANTO (para no pasar de 150 °C)")
    print(f"   coseno del ángulo de incidencia necesario: {p['cos']:.4f} -> {p['angulo']:.1f}° respecto a la normal")
    v = velocidades()
    print("\n5. VELOCIDAD Y ENLACE")
    print(f"   en el perihelio la nave recorre una distancia igual al diámetro del Sol en {v['t_diametro_s'] / 3600:.1f} h")
    a = autonomia()
    print(f"   la luz tarda {a['luz_min']:.1f} min en llegar a la Tierra: {a['ida_vuelta_min']:.1f} min ida y vuelta")
    print(f"\n6. AUTONOMÍA: si la nave se desapunta, no hay tiempo de pedir ayuda; fiabilidad en serie ilustrativa: {fiabilidad():.3f}")
    print("\n7. COSTO de referencia: ≈ 1,5 GUSD sin contar el lanzador (⚠ verificar)")


if __name__ == "__main__":
    main()
