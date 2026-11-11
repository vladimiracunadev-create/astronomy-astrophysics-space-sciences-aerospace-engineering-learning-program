#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C10: presupuesto de residuos humanos de una mision (masa, volumen y almacenamiento).

Consultado (OCHMO-TB-002, requisito V2 7102 citado en el resumen): promedio maximo de 2 eventos de 1.1 lb por persona y dia para heces y de 7 eventos de 1 L por persona
y dia para orina. ILUSTRATIVOS (no consultados): valores tipicos de 1.2 eventos/dia de 0.12 kg y de 5 eventos/dia de 0.3 L, contenido de agua de las heces de 75 %,
densidad de 1000 kg/m3, 10 % de masa de bolsas y envases. Monte Carlo con semilla 106 (Poisson) para el percentil 95.
Verificacion: 1 lb = 0.45359 kg; la masa maxima es 0.998 kg/dia por persona; el percentil 95 simulado queda por debajo del diseno maximo y sobre la media.
"""
from __future__ import annotations
import platform
import numpy as np

LB = 0.45359237


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: maximos de diseno consultados (OCHMO-TB-002); valores tipicos y Monte Carlo SINTETICOS (semilla 106)")
    R = {}
    f_max = 2 * 1.1 * LB
    u_max = 7 * 1.0
    R["f_max"], R["u_max"] = f_max, u_max
    print(f"Maximos consultados por persona y dia: heces {f_max:.3f} kg (2 x 1.1 lb); orina {u_max:.1f} L (7 x 1 L)")
    assert abs(f_max - 0.998) < 1e-3
    crew, dias = 4, 30
    f_t, u_t = 1.2 * 0.12, 5 * 0.3
    print(f"Mision de {crew} personas y {dias} dias:")
    print("   caso            heces [kg]   orina [L]   heces secas [kg]   volumen de heces [L]")
    filas = {}
    for nom, f, u in (("diseno maximo", f_max, u_max), ("tipico (ilustr.)", f_t, u_t)):
        F, U = f * crew * dias, u * crew * dias
        seca = F * (1 - 0.75)
        filas[nom] = (F, U, seca)
        print(f"   {nom:16s} {F:10.1f}   {U:9.0f}   {seca:14.1f}   {F:16.1f}")
    R["F_max"], R["U_max"], R["F_t"], R["U_t"], R["seca_max"] = filas["diseno maximo"][0], filas["diseno maximo"][1], filas["tipico (ilustr.)"][0], filas["tipico (ilustr.)"][1], filas["diseno maximo"][2]
    R["con_bolsas"] = filas["diseno maximo"][0] * 1.10
    print(f"Con 10 % de bolsas y envases, el diseno maximo de heces pesa {R['con_bolsas']:.1f} kg")
    rng = np.random.default_rng(106)
    N = 20000
    ev = rng.poisson(1.2 * crew * dias, N)
    masa = ev * 0.12
    p50, p95 = np.percentile(masa, [50, 95])
    R["p50"], R["p95"] = p50, p95
    print(f"Monte Carlo (Poisson, {N} misiones): masa de heces mediana {p50:.1f} kg, percentil 95 {p95:.1f} kg; diseno maximo {filas['diseno maximo'][0]:.1f} kg")
    assert p50 < p95 < filas["diseno maximo"][0]
    sob = filas["diseno maximo"][0] / p95
    R["sob"] = sob
    print(f"El diseno maximo es {sob:.1f} veces el percentil 95 simulado (margen de diseno)")
    # urina -> agua recuperable
    rec = 0.85
    R["agua_rec"] = filas["tipico (ilustr.)"][1] * rec
    print(f"Con 85 % de recuperacion (ilustrativo, ver C27), la orina tipica devuelve {R['agua_rec']:.0f} L y deja {filas['tipico (ilustr.)'][1]*(1-rec):.0f} L de salmuera")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
