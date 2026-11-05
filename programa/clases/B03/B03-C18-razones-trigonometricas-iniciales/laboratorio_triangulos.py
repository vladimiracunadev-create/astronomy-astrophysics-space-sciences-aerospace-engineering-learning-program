#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C18: razones trigonométricas, tamaño angular y paralaje.

Datos PUBLICADOS: radio medio de la Luna 1737,4 km y semieje 384 400 km; diámetro aparente de la Luna
en oposición 1896″ a 378 000 km (NASA Moon Fact Sheet, 11-ene-2024); radio solar 695 700 km (NASA Sun);
1 au = 149 597 870,7 km y 1″ = π/648 000 rad (SI). Modelo: tamaño angular θ = 2 atan(r/d) de una
esfera; paralaje p con tan p = b/d. Supuestos: esfera vista de frente, sin refracción. Validez:
cuerpos lejanos y ángulos pequeños. Tolerancias: 1e-12 en el triángulo 3-4-5; 0,1 % entre θ calculado
y el aparente publicado de la Luna; 1e-6 relativa entre tan y ángulo pequeño para 1″.
"""
from __future__ import annotations

import math
import platform

R_LUNA, A_LUNA, R_SOL, AU_KM = 1737.4, 384_400.0, 695_700.0, 149_597_870.7
D_OPOSICION, DIAM_APARENTE_ARCSEG = 378_000.0, 1896.0
ARCSEG_RAD = math.pi / 648_000


def tamano_angular_deg(r: float, d: float) -> float:
    return math.degrees(2 * math.atan(r / d))


def distancia_por_paralaje(base: float, p_rad: float) -> float:
    return base / math.tan(p_rad)


def pruebas() -> None:
    h = math.hypot(3, 4)
    assert h == 5.0 and abs(math.sin(math.atan2(3, 4)) - 3 / 5) < 1e-12 and abs(math.cos(math.atan2(3, 4)) - 4 / 5) < 1e-12
    assert abs(math.tan(math.radians(45)) - 1) < 1e-12
    assert abs(math.degrees(ARCSEG_RAD) * 3600 - 1) < 1e-12                          # 1″ = 1/3600°
    assert abs(math.tan(ARCSEG_RAD) - ARCSEG_RAD) / ARCSEG_RAD < 1e-6               # ángulo pequeño
    theta = tamano_angular_deg(R_LUNA, D_OPOSICION) * 3600
    assert abs(theta - DIAM_APARENTE_ARCSEG) / DIAM_APARENTE_ARCSEG < 0.001, theta   # frente a la NASA
    assert abs(distancia_por_paralaje(AU_KM, ARCSEG_RAD) / AU_KM - 648_000 / math.pi) < 1.0


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"Luna a 378 000 km: {tamano_angular_deg(R_LUNA, D_OPOSICION) * 3600:.0f} ″ (NASA: 1896 ″)")
    print(f"Luna a 384 400 km: {tamano_angular_deg(R_LUNA, A_LUNA):.4f} °")
    print(f"Sol a 1 au: {tamano_angular_deg(R_SOL, AU_KM):.4f} ° = {tamano_angular_deg(R_SOL, AU_KM) * 60:.2f} ′")
    d = distancia_por_paralaje(AU_KM, ARCSEG_RAD)
    print(f"Paralaje 1″ con base 1 au: d = {d / AU_KM:,.0f} au = {d * 1000:.4e} m")
    print(f"Paralaje 0,1″: d = {distancia_por_paralaje(AU_KM, 0.1 * ARCSEG_RAD) / AU_KM:,.0f} au")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
