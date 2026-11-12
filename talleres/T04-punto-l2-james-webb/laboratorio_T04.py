# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T04 (punto L2, telescopio espacial James Webb).

Secciones: 1 geometría del punto L2 · 2 óptica y resolución · 3 por qué hay que enfriar · 4 escudo solar ·
5 fiabilidad de los despliegues · 6 combustible de mantenimiento orbital · 7 datos · 8 costo.

UNIDADES: km, s, kg, K, W/m^2, µm, segundos de arco (″); costos en miles de millones de USD (GUSD).
SISTEMA DE REFERENCIA: Sol-Tierra giratorio para L2; telescopio en su propio sistema para la óptica.
MODELO: tres cuerpos restringido circular (aproximación de la esfera de Hill), difracción en apertura circular,
cuerpo negro, láminas planas paralelas ideales. TOLERANCIA: ±5 %, salvo el escudo solar (solo orden de magnitud).
DATOS: constantes NASA/JPL redondeadas; cifras de la misión de referencia pública redondeadas (⚠ verificar).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

M_TIERRA_SOL = 3.003e-6   # razón de masas Tierra/Sol
WIEN = 2897.77            # µm·K


def geometria_l2() -> dict:
    r = UA * (M_TIERRA_SOL / 3) ** (1 / 3)
    omega = 2 * math.pi / (365.25 * 86400)
    return {"r_km": r, "luz_s": r / C_LUZ, "v_kms": omega * (UA + r), "ratio_v": (UA + r) / UA}


def optica() -> dict:
    d_jwst, d_hst = 6.5, 2.4
    lam = 2.0e-6
    theta = 1.22 * lam / d_jwst
    area_j = 25.4
    area_h = math.pi * (d_hst / 2) ** 2 * 0.9
    return {"theta_arcsec": math.degrees(theta) * 3600, "area_ratio": area_j / area_h,
            "theta_hst_arcsec": math.degrees(1.22 * 0.55e-6 / d_hst) * 3600}


def pico_de_wien() -> dict:
    return {t: WIEN / t for t in (300.0, 100.0, 40.0)}


def escudo(n: int = 5, t_caliente: float = 383.0) -> list[float]:
    """Temperatura tras cada lámina en el modelo ideal de láminas paralelas (cada una irradia por ambas caras)."""
    res = [t_caliente]
    for _ in range(n):
        res.append(res[-1] * 0.5 ** 0.25)
    return res


def despliegues(p_punto: float, n: int = 344) -> float:
    return p_punto ** n


def exigido(objetivo: float = 0.90, n: int = 344) -> float:
    return objetivo ** (1 / n)


def combustible(dv_ms_anio: float, anios: float, masa: float = 6200.0, isp: float = 220.0) -> float:
    return masa_propelente(dv_ms_anio * anios / 1000, isp, masa)


def datos(gb_dia: float = 28.0, mbps: float = 25.9) -> float:
    return gb_dia * 8e9 / (mbps * 1e6) / 3600


def costo() -> dict:
    return {"inicial": 1.0, "final": 10.0, "por_m2": 10.0 / 25.4}


def main() -> None:
    print("TALLER T04 - Punto L2 (telescopio James Webb): laboratorio de diseño preliminar\n")
    g = geometria_l2()
    print("1. PUNTO L2 SOL-TIERRA")
    print(f"   distancia a la Tierra   : {g['r_km']:,.0f} km  (≈ 1,5 millones)".replace(",", "."))
    print(f"   retardo de luz          : {g['luz_s']:.1f} s en un sentido")
    print(f"   velocidad alrededor del Sol: {g['v_kms']:.2f} km/s (misma velocidad angular que la Tierra)")
    o = optica()
    print("\n2. ÓPTICA (espejo de 6,5 m, 25,4 m² de área colectora)")
    print(f"   límite de difracción a 2 µm : {o['theta_arcsec']:.3f} ″   (Hubble a 0,55 µm: {o['theta_hst_arcsec']:.3f} ″)")
    print(f"   área colectora frente a Hubble: x{o['area_ratio']:.1f}")
    print("\n3. POR QUÉ HAY QUE ENFRIARLO: longitud de onda donde un cuerpo emite más (ley de Wien)")
    for t, lam in pico_de_wien().items():
        print(f"   a {t:>5.0f} K : {lam:5.1f} µm")
    print("   a 300 K el telescopio brillaría justo en el infrarrojo medio que quiere observar; a ≈ 40 K deja de molestar")
    print("\n4. ESCUDO SOLAR: modelo ideal de láminas paralelas, cara caliente a 383 K")
    for i, t in enumerate(escudo()):
        print(f"   tras {i} láminas: {t:6.1f} K")
    print("   el diseño real llega a ≈ 40 K usando láminas inclinadas y separadas que evacúan el calor hacia los lados")
    print("\n5. FIABILIDAD DE LOS DESPLIEGUES (344 puntos únicos de fallo)")
    for p in (0.999, 0.9995, 0.9999, 0.99999):
        print(f"   {p * 100:7.3f} % por punto -> {despliegues(p) * 100:5.1f} % de éxito global")
    print(f"   para llegar a 90 % global hace falta {exigido() * 100:.4f} % por punto")
    print("\n6. COMBUSTIBLE DE MANTENIMIENTO (hidrazina, Isp 220 s, nave de 6.200 kg)")
    for dv in (2.0, 3.0, 4.0):
        print(f"   {dv:.0f} m/s por año durante 20 años: {combustible(dv, 20):6.1f} kg")
    print(f"\n7. DATOS: 28 GB al día a 25,9 Mbit/s = {datos():.1f} horas de enlace por día")
    c = costo()
    print("\n8. COSTO (referencias públicas aproximadas: estimación inicial ≈ 1 GUSD, total ≈ 10 GUSD)")
    print(f"   crecimiento x{c['final'] / c['inicial']:.0f}; ≈ {c['por_m2']:.2f} GUSD por m² de apertura")


if __name__ == "__main__":
    main()
