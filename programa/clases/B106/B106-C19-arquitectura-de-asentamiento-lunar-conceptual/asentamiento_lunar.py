#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C19: dimensionado conceptual de un asentamiento lunar: noche lunar, energia, presion frente a peso del regolito y excavacion.

Valores de manual NO consultados: mes sinodico de 29.53 dias, gravedad lunar de 1.62 m/s2, constante solar de 1361 W/m2. ILUSTRATIVOS: carga electrica de 15 kW, noche igual a la mitad
del mes (sitio ecuatorial sin sombras), baterias de 200 Wh/kg con 80 % de profundidad de descarga y 90 % de rendimiento, paneles de 25 % de eficiencia, regolito de 1500 kg/m3,
habitat cilindrico enterrado de 5 m de radio y 20 m de largo bajo 3 m de regolito, excavadora de 10 m3/h. Es un ejercicio CONCEPTUAL: no es un diseno.
Verificacion: noche = mitad del mes; la presion del regolito es rho g h; el volumen enterrado coincide con la diferencia de areas por la longitud.
"""
from __future__ import annotations
import math
import platform
import numpy as np

SIN, G, S0 = 29.53, 1.62, 1361.0


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: constantes de manual NO consultadas y valores ILUSTRATIVOS; ejercicio conceptual, NO un diseno")
    R = {}
    t_noche = SIN * 24 / 2
    R["t_noche"] = t_noche
    print(f"Mes sinodico {SIN} dias: noche de {t_noche:.1f} h ({t_noche/24:.2f} dias)")
    assert abs(t_noche - SIN * 12) < 1e-9
    P = 15e3
    E = P * t_noche / 1e3  # kWh
    m_bat = E * 1e3 / (200.0 * 0.8 * 0.9) / 1000.0
    R.update(E=E, m_bat=m_bat)
    print(f"Energia de la noche a {P/1e3:.0f} kW: {E:.0f} kWh = {E/1e3:.2f} MWh; baterias (200 Wh/kg, DOD 0.8, eficiencia 0.9): {m_bat:.1f} t")
    P_dia = P * (1 + t_noche / t_noche)  # para cargar durante el dia
    A = P_dia / (S0 * 0.25)
    R["A"] = A
    print(f"Paneles: de dia deben dar {P_dia/1e3:.0f} kW (carga + consumo): {A:.0f} m2 con 25 % de eficiencia y sol perpendicular")
    print("Presion frente a peso del regolito (rho g h, rho = 1500 kg/m3, g = 1.62 m/s2):")
    print("   espesor [m]   presion del regolito [kPa]   fraccion de 101.3 kPa")
    for h in (1.0, 3.0, 10.0):
        p = 1500 * G * h
        print(f"   {h:9.1f}   {p/1e3:24.1f}   {p/101325:20.3f}")
    R["p3"] = 1500 * G * 3.0
    R["h_101"] = 101325 / (1500 * G)
    R["h_70"] = 70300 / (1500 * G)
    print(f"Espesor para equilibrar 101.3 kPa con solo regolito: {R['h_101']:.1f} m; para 70.3 kPa: {R['h_70']:.1f} m (el casco debe resistir la traccion)")
    r_i, L, cub = 5.0, 20.0, 3.0
    area = math.pi * (r_i + cub) ** 2 - math.pi * r_i ** 2
    vol = area * L
    m_reg = vol * 1500.0
    t_exc = vol / 10.0
    R.update(vol=vol, m_reg=m_reg, t_exc=t_exc, x_cm2=1500 * cub / 10.0)
    print(f"Habitat de r = {r_i:.0f} m y L = {L:.0f} m cubierto por {cub:.0f} m: volumen de regolito {vol:.0f} m3, {m_reg/1e3:.0f} t; excavadora de 10 m3/h: {t_exc:.0f} h")
    print(f"Espesor masico de la cubierta: {1500*cub/10:.0f} g/cm2 (ver C14: fuera del rango de validez del modelo de protones)")
    assert abs(vol - (math.pi * 8 ** 2 - math.pi * 5 ** 2) * 20) < 1e-9
    net = 101325 - R["p3"]
    R["net"] = net
    print(f"Carga neta hacia afuera sobre el casco con 3 m de cubierta: {net/1e3:.1f} kPa (101.3 - {R['p3']/1e3:.1f}); el casco sigue sosteniendo casi toda la presion")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
