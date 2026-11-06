#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C06: escribir y leer un FITS con encabezado y escala física.

Datos: SINTÉTICOS. Imagen de 64x48 píxeles con una fuente gaussiana (amplitud
1000 e-, sigma 3 px, centro en x=40, y=20, 0-indexado) sobre un cielo de
100 e- y ruido gaussiano de 5 e- (semilla fija 20261105). No es una
observación real.
Modelo: los datos se guardan como enteros de 16 bits con BZERO y BSCALE
(física = BZERO + BSCALE * almacenado; estándar FITS 4.0, Eq. 3, sec. 4.4.2.5);
la WCS es lineal (CRPIX, CRVAL, CDELT) con proyección TAN.
Supuestos: campo pequeño (decenas de arcsec), sin distorsión.
Validez: demostración de la estructura del formato.
Tolerancia: la cuantización con BSCALE=0.1 introduce error <= 0.05 e- (más 1e-4 por la lectura reescalada en float32); el
tamaño del archivo es múltiplo de 2880 bytes; el píxel de referencia se
mapea a CRVAL a 1e-9 deg.
"""
from __future__ import annotations
import os, platform, sys, tempfile
import numpy as np
import astropy
from astropy.io import fits
from astropy.wcs import WCS


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  astropy {astropy.__version__}")
    rng = np.random.default_rng(20261105)
    y, x = np.mgrid[0:48, 0:64]
    fisico = 100.0 + 1000.0 * np.exp(-((x - 40) ** 2 + (y - 20) ** 2) / (2 * 3.0**2)) + rng.normal(0, 5.0, x.shape)

    bscale, bzero = 0.1, 0.0
    almacenado = np.round((fisico - bzero) / bscale).astype(">i2")
    hdu = fits.PrimaryHDU(almacenado)
    hdu.header["BSCALE"] = (bscale, "physical = BZERO + BSCALE * stored")
    hdu.header["BZERO"] = (bzero, "offset")
    hdu.header["BUNIT"] = ("electron", "unidad fisica")
    hdu.header["OBJECT"] = ("SYNTHETIC", "datos sinteticos")
    hdu.header["EXPTIME"] = (30.0, "[s] tiempo de exposicion")
    hdu.header["DATE-OBS"] = ("2026-11-05T00:00:00", "inicio, UTC, ficticio")
    hdu.header["CTYPE1"], hdu.header["CTYPE2"] = "RA---TAN", "DEC--TAN"
    hdu.header["CRPIX1"], hdu.header["CRPIX2"] = 33.0, 25.0
    hdu.header["CRVAL1"], hdu.header["CRVAL2"] = 150.0, 2.0
    hdu.header["CDELT1"], hdu.header["CDELT2"] = -1.0 / 3600, 1.0 / 3600
    hdu.header["CUNIT1"], hdu.header["CUNIT2"] = "deg", "deg"
    hdu.header["HISTORY"] = "generado por fits_y_encabezados.py (sintetico)"

    with tempfile.TemporaryDirectory() as td:
        ruta = os.path.join(td, "demo.fits")
        hdu.writeto(ruta)
        tam = os.path.getsize(ruta)
        print(f"tamaño del archivo = {tam} bytes = {tam/2880:.0f} bloques de 2880")
        prueba(tam % 2880 == 0, "tamaño múltiplo de 2880")
        with open(ruta, "rb") as f:
            raw = f.read()
        prueba(raw[:9] == b"SIMPLE  =", "primera tarjeta SIMPLE")
        cab = raw[:2880]
        tarjetas = [cab[i:i + 80] for i in range(0, 2880, 80)]
        prueba(len(tarjetas) == 36 and all(len(t) == 80 for t in tarjetas), "36 tarjetas de 80")
        n_end = [i for i, t in enumerate(tarjetas) if t[:8] == b"END     "]
        prueba(len(n_end) == 1, "una tarjeta END")
        print(f"bloque de encabezado: 36 tarjetas; END en la tarjeta {n_end[0] + 1}")
        print("primeras 3 tarjetas:", [t.decode().rstrip() for t in tarjetas[:3]])
        # el bloque de datos empieza tras el último bloque de encabezado
        n_bloques_cab = 1
        with fits.open(ruta) as h:
            h.info()
            hd = h[0].header
            print(f"BITPIX={hd['BITPIX']} NAXIS={hd['NAXIS']} NAXIS1={hd['NAXIS1']} NAXIS2={hd['NAXIS2']}")
            prueba(hd["BITPIX"] == 16 and hd["NAXIS1"] == 64 and hd["NAXIS2"] == 48, "estructura")
            datos = h[0].data
            prueba(datos.shape == (48, 64), "forma (fila, columna)")
            ini = 2880 * n_bloques_cab
            crudo = np.frombuffer(raw[ini:ini + 64 * 48 * 2], dtype=">i2").reshape(48, 64)
            rec = bzero + bscale * crudo
            prueba(np.allclose(datos, rec, atol=1e-6), "BZERO + BSCALE*almacenado")
            err = np.abs(datos - fisico).max()
            print(f"error máximo de cuantización = {err:.6f} e- (cota 0.05 más 1e-4 por la lectura en float32)")
            prueba(err <= 0.05 + 1e-4, "cuantización")
            w = WCS(hd)
            ra0, dec0 = w.wcs_pix2world(32.0, 24.0, 0)
            prueba(abs(ra0 - 150.0) < 1e-9 and abs(dec0 - 2.0) < 1e-9, "CRPIX -> CRVAL")
            ra1, dec1 = w.wcs_pix2world(32.0, 25.0, 0)
            paso = (dec1 - dec0) * 3600
            print(f"WCS: píxel de referencia -> ({ra0:.6f}, {dec0:.6f}) deg; un píxel en y = {paso:.4f} arcsec")
            prueba(abs(paso - 1.0) < 1e-3, "escala 1 arcsec/px")
            cy, cx = np.unravel_index(np.argmax(datos), datos.shape)
            print(f"máximo en (x, y) = ({cx}, {cy}) 0-indexado; valor = {datos.max():.1f} e-")
            prueba((cx, cy) == (40, 20), "posición de la fuente")
            hd2 = hd.copy()
            hd2["OBJECT"] = "OTRO"
            prueba(hd["OBJECT"] == "SYNTHETIC", "copia de encabezado")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
