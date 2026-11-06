#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C05: tablas con unidades, valores enmascarados y cruce de catálogos.

Datos: SINTÉTICOS. Un catálogo A de 6 fuentes y un catálogo B de 5 fuentes,
construidos en el script; B reobserva 4 de las fuentes de A con un
desplazamiento de declinación definido de antemano (0.5 arcsec) y añade una
fuente nueva. Ninguna fila corresponde a una estrella real.
Modelo: distancia d[pc] = 1000 / paralaje[mas]; separación angular con
astropy.coordinates (SkyCoord); cruce por vecino más cercano con umbral de
2 arcsec.
Supuestos: posiciones en ICRS, sin movimiento propio, sin época.
Validez: demostración de estructura de tabla, no un cruce astrométrico real.
Tolerancia: 1e-9 en distancias; separaciones planeadas reproducidas a
1e-3 arcsec; ida y vuelta por ECSV exacta en unidades, máscara y metadatos.
"""
from __future__ import annotations
import io, platform, sys
import numpy as np
import astropy
import astropy.units as u
from astropy.table import QTable, MaskedColumn
from astropy.coordinates import SkyCoord


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  astropy {astropy.__version__}")
    ra = np.array([10.0, 10.5, 11.0, 150.0, 200.0, 359.9999]) * u.deg
    dec = np.array([-20.0, -20.1, 5.0, 60.0, -75.0, 0.0]) * u.deg
    par = MaskedColumn([100.0, 50.0, 12.5, 4.0, 0.0, 2.0], mask=[False, False, False, False, True, False],
                       unit=u.mas, name="paralaje")
    A = QTable([["A1", "A2", "A3", "A4", "A5", "A6"], ra, dec, par], names=("id", "ra", "dec", "paralaje"))
    A.meta["procedencia"] = "sintético, no es un catálogo real"

    d = (1000.0 / A["paralaje"].filled(np.nan).value) * u.pc
    A["distancia"] = d
    print("distancias [pc]:", np.round(A["distancia"].value, 3))
    prueba(abs(A["distancia"][0].value - 10.0) < 1e-9, "100 mas -> 10 pc")
    prueba(abs(A["distancia"][1].value - 20.0) < 1e-9, "50 mas -> 20 pc")
    prueba(np.isnan(A["distancia"][4].value), "paralaje enmascarada -> NaN")

    sel = [0, 1, 3, 5]
    dec_b = np.concatenate([dec[sel] + 0.5 * u.arcsec, [30.0] * u.deg])
    ra_b = np.concatenate([ra[sel], [40.0] * u.deg])
    B = QTable([["B1", "B2", "B3", "B4", "B5"], ra_b, dec_b], names=("id", "ra", "dec"))
    ca, cb = SkyCoord(A["ra"], A["dec"]), SkyCoord(B["ra"], B["dec"])
    idx, sep, _ = cb.match_to_catalog_sky(ca)
    for i in range(5):
        print(f"{B['id'][i]} -> {A['id'][idx[i]]}  sep = {sep[i].to(u.arcsec):.4f}")
    prueba(np.allclose(sep[:4].to_value(u.arcsec), 0.5, atol=1e-3), "separaciones planeadas 0.5 arcsec")
    ok = sep < 2 * u.arcsec
    prueba(list(ok) == [True, True, True, True, False], "umbral de 2 arcsec")
    prueba([A["id"][idx[i]] for i in range(4)] == ["A1", "A2", "A4", "A6"], "pares esperados")
    print(f"cruce con umbral 2 arcsec: {int(ok.sum())} pares, {int((~ok).sum())} fuente sin contraparte")

    s = SkyCoord(359.9999 * u.deg, 0 * u.deg).separation(SkyCoord(0.0001 * u.deg, 0 * u.deg))
    prueba(abs(s.to_value(u.arcsec) - 0.72) < 1e-6, "envoltura de ra")
    print(f"separación a través de ra=0: {s.to(u.arcsec):.4f} (esperado 0.7200 arcsec)")

    buf = io.StringIO()
    A.write(buf, format="ascii.ecsv")
    A2 = QTable.read(buf.getvalue(), format="ascii.ecsv")
    prueba(A2["paralaje"].unit == u.mas, "unidad tras ECSV")
    prueba(bool(A2["paralaje"].mask[4]) and not A2["paralaje"].mask[0], "máscara tras ECSV")
    prueba(np.allclose(A2["ra"].to_value(u.deg), A["ra"].to_value(u.deg), rtol=1e-12), "ra tras ECSV")
    prueba(A2.meta["procedencia"] == A.meta["procedencia"], "metadatos tras ECSV")
    print("ECSV: unidades, máscara y metadatos se conservan")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
