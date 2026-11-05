#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C15: a qué ritmo hay que mover una montura para seguir una estrella.

Datos PUBLICADOS: rotación sidérea de la Tierra 23,9345 h (NASA Earth Fact Sheet, act. 15-nov-2024; consultada 2026-11-05).
Modelo (SIMULADO): el cielo gira con velocidad angular Omega = 360 grados / 23,9345 h alrededor del polo celeste.
Montura ecuatorial: velocidad de seguimiento = Omega cos(dec) en ascensión recta, 0 en declinación.
Montura altacimutal: dA/dt y dh/dt dependen de la posición; fórmulas analíticas
dh/dt = +Omega cos(lat) sen(A) y dA/dt = Omega (sen(lat) - cos(lat) tan(h) cos(A)) (variables en grados y segundos de arco).
Error de alineación polar eps: la deriva máxima en declinación es Omega*eps.
Dominio: estrella (sin movimiento propio), sin refracción; error de alineación pequeño. Tolerancias: 0,1 % en derivadas.
Prueba independiente: derivadas por diferencias finitas de astrolib_b08.altaz (ya validada contra astropy) y simulación por rotación
de vectores del polo desalineado (fórmula de Rodrigues), comparadas con las fórmulas analíticas.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, altaz, pruebas_biblioteca  # noqa: E402

DIA_SIDEREO_H = 23.9345
OMEGA_ARCSEC_S = 360.0 * 3600.0 / (DIA_SIDEREO_H * 3600.0)        # arcsec por segundo de tiempo


def tasa_ecuatorial(dec: float) -> float:
    return OMEGA_ARCSEC_S * math.cos(dec * D2R)


def tasas_altacimutales(alt: float, az: float, lat: float) -> tuple[float, float]:
    """(dh/dt, dA/dt) en arcsec/s para altura y acimut (desde el norte hacia el este) dados."""
    h, a, f = alt * D2R, az * D2R, lat * D2R
    dh = OMEGA_ARCSEC_S * math.cos(f) * math.sin(a)
    da = OMEGA_ARCSEC_S * (math.sin(f) - math.cos(f) * math.tan(h) * math.cos(a))
    return dh, da


def tasas_numericas(ra: float, dec: float, lat: float, lst: float, dt_s: float = 1.0) -> tuple[float, float]:
    omega_deg = OMEGA_ARCSEC_S / 3600.0
    h0, a0 = altaz(ra, dec, lat, lst - omega_deg * dt_s / 2.0)
    h1, a1 = altaz(ra, dec, lat, lst + omega_deg * dt_s / 2.0)
    da = (a1 - a0 + 180.0) % 360.0 - 180.0
    return (h1 - h0) * 3600.0 / dt_s, da * 3600.0 / dt_s


def deriva_dec_max(eps_deg: float) -> float:
    return OMEGA_ARCSEC_S * eps_deg * D2R


def deriva_dec_simulada(eps_deg: float, dt_s: float = 60.0) -> float:
    """Rota una estrella del ecuador celeste alrededor de un eje desalineado eps (hacia el norte) y mide el máximo cambio de Dec por segundo."""
    eps = eps_deg * D2R
    k = (math.sin(eps), 0.0, math.cos(eps))                       # eje de la montura
    mejor = 0.0
    for fase in range(0, 360, 5):
        th = fase * D2R
        v = (math.cos(th), math.sin(th), 0.0)                     # estrella del ecuador celeste

        def rot(v, ang):
            c, s = math.cos(ang), math.sin(ang)
            kv = (k[1] * v[2] - k[2] * v[1], k[2] * v[0] - k[0] * v[2], k[0] * v[1] - k[1] * v[0])
            kd = sum(a * b for a, b in zip(k, v))
            return tuple(v[i] * c + kv[i] * s + k[i] * kd * (1 - c) for i in range(3))

        w = rot(v, OMEGA_ARCSEC_S / 3600.0 * D2R * dt_s)
        d0, d1 = math.asin(v[2]), math.asin(w[2])
        mejor = max(mejor, abs(d1 - d0) / D2R * 3600.0 / dt_s)
    return mejor


def pruebas() -> None:
    pruebas_biblioteca()
    assert abs(OMEGA_ARCSEC_S - 15.0411) < 0.001, OMEGA_ARCSEC_S
    for ra, dec, lst in [(30.0, 17.0, 50.0), (200.0, -63.0, 190.0), (45.0, -20.0, 10.0)]:
        h, a = altaz(ra, dec, -30.0, lst)
        dh, da = tasas_altacimutales(h, a, -30.0)
        nh, na = tasas_numericas(ra, dec, -30.0, lst)
        assert abs(dh - nh) < 0.002 * OMEGA_ARCSEC_S and abs(da - na) < 0.002 * OMEGA_ARCSEC_S + 0.01 * abs(na), (ra, dec, dh, nh, da, na)
    assert abs(deriva_dec_max(1.0) - deriva_dec_simulada(1.0)) / deriva_dec_max(1.0) < 0.01


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Omega = {OMEGA_ARCSEC_S:.4f} arcsec/s = {OMEGA_ARCSEC_S * 60:.1f} arcsec/min = {OMEGA_ARCSEC_S * 3600 / 3600:.3f} grados/h (SIMULADO)")
    for dec in (0, -30, -60, -85):
        print(f"Ecuatorial: dec {dec:+3d}: {tasa_ecuatorial(dec):6.2f} arcsec/s")
    print("Altacimutal en lat -30 (la Luna del 5-nov-2025 a las 04:00 UT: alt 42,3, az 359,7) y otras posiciones:")
    for alt, az in [(42.3, 359.7), (20.0, 90.0), (60.0, 180.0), (85.0, 100.0)]:
        dh, da = tasas_altacimutales(alt, az, -30.0)
        print(f"  alt {alt:4.1f} az {az:5.1f}: dh/dt = {dh:+6.2f} arcsec/s | dA/dt = {da:+7.2f} arcsec/s")
    for eps in (0.1, 0.5, 1.0):
        print(f"Alineacion polar con error {eps} grados: deriva maxima en dec {deriva_dec_max(eps):.2f} arcsec/s = {deriva_dec_max(eps) * 60:.1f} arcsec/min")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
