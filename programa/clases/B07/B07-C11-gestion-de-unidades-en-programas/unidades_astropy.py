#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C11: unidades dentro del programa con astropy.units.

Datos PUBLICADOS: planetas_nssdc.csv (clase B07-C08), del NASA NSSDC, consultado el
2026-11-05. Constantes: astropy.constants (G de CODATA 2022 y au según la tabla de la
documentación de Astropy 8.0.2, consultada el 2026-11-05).
Modelo: (1) densidad media ρ = M / (4/3 π R³) con R radio medio volumétrico;
(2) gravedad en la superficie g = G M / R² con R radio ecuatorial (esfera, sin rotación).
Supuestos: cuerpos esféricos y sin rotación en (2). Resultados = DERIVADOS.
Dominio de validez: la comparación de g con el dato publicado solo se exige para los
cuatro planetas rocosos (publicados con una cifra decimal): tolerancia 0,05 m/s².
Los gigantes se informan sin exigirlo (su «superficie» y su rotación son otro caso).
Requiere: astropy 8.0.2, numpy 2.4.4 (Python 3.12.9).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import astropy
import astropy.units as u
import numpy as np
from astropy.constants import G
from astropy.units import UnitConversionError

AQUI = Path(__file__).resolve().parent
CSV = AQUI.parent / "B07-C08-lectura-de-archivos-csv" / "planetas_nssdc.csv"
ROCOSOS = {"Mercurio", "Venus", "Tierra", "Marte"}


def leer_con_unidades(ruta: Path) -> list[dict]:
    """Lee el CSV de planetas y devuelve registros con Quantity (valor + unidad)."""
    with ruta.open(encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
    return [{
        "nombre": f["nombre"],
        "masa": float(f["masa_1e24kg"]) * 1e24 * u.kg,
        "radio_medio": float(f["radio_medio_km"]) * u.km,
        "radio_eq": float(f["radio_ecuatorial_km"]) * u.km,
        "semieje": float(f["semieje_1e6km"]) * 1e6 * u.km,
        "rho_pub": float(f["densidad_kg_m3"]) * u.kg / u.m ** 3,
        "g_pub": float(f["gravedad_m_s2"]) * u.m / u.s ** 2,
    } for f in filas]


def densidad(masa, radio):
    """Densidad media de una esfera, en kg/m³ (acepta cualquier unidad compatible)."""
    return (masa / (4.0 / 3.0 * np.pi * radio ** 3)).to(u.kg / u.m ** 3)


def gravedad_superficial(masa, radio):
    """Gravedad en la superficie de una esfera sin rotación, en m/s²."""
    return (G * masa / radio ** 2).to(u.m / u.s ** 2)


def pruebas() -> None:
    assert abs((1 * u.au).to_value(u.km) - 149597870.7) < 1e-3          # valor devuelto por astropy 8.0.2
    assert (2.5 * u.m).to_value(u.cm) == 250.0                           # conversión simple
    try:
        (1 * u.kg + 1 * u.m)                                             # suma incompatible
    except UnitConversionError:
        pass
    else:
        raise AssertionError("sumar kg y m debía fallar")
    assert (20.0 * u.cm / (1.0 * u.m)).decompose().value == 0.2          # adimensional
    planetas = leer_con_unidades(CSV)
    assert len(planetas) == 8
    for p in planetas:
        rho = densidad(p["masa"], p["radio_medio"])
        assert abs(rho / p["rho_pub"] - 1.0) < 0.002, p["nombre"]        # igual criterio que C09
        assert densidad(p["masa"], p["radio_medio"].to(u.m)).unit == u.kg / u.m ** 3
        if p["nombre"] in ROCOSOS:
            dg = abs((gravedad_superficial(p["masa"], p["radio_eq"]) - p["g_pub"]).to_value(u.m / u.s ** 2))
            assert dg < 0.05, (p["nombre"], dg)
    tierra = planetas[2]
    assert abs(tierra["semieje"].to_value(u.au) - 1.0) < 1e-5            # la Tierra está a ≈ 1 au


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | astropy {astropy.__version__} | numpy {np.__version__} | pruebas OK")
    print(f"G = {G.value:.4e} {G.unit}")
    print(f"{'planeta':<9}{'a (au)':>10}{'ρ calc (kg/m³)':>16}{'g calc (m/s²)':>15}{'g publ.':>9}")
    for p in leer_con_unidades(CSV):
        rho = densidad(p["masa"], p["radio_medio"])
        g = gravedad_superficial(p["masa"], p["radio_eq"])
        print(f"{p['nombre']:<9}{p['semieje'].to_value(u.au):>10.3f}{rho.value:>16.1f}"
              f"{g.value:>15.2f}{p['g_pub'].value:>9.1f}")
    try:
        (1 * u.kg + 1 * u.m)
    except UnitConversionError as error:
        print("Suma de kg y m ->", type(error).__name__ + ":", error)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
