#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C19: cabecera FITS minima escrita a mano y leida por dos vias.

Datos: ninguna constante fisica. Los valores de las palabras clave (EXPTIME, GAIN, DATE-OBS, OBJECT, INSTRUME) son ILUSTRATIVOS (sinteticos); el objeto y la camara no existen.
Consulta: la pagina de NASA/HEASARC https://fits.gsfc.nasa.gov/fits_standard.html (2026-11-09) indica que la version vigente es la 4.0 (13 de agosto de 2018); el documento del estandar
NO se leyo. Las reglas de formato usadas aqui (tarjetas de 80 caracteres, bloques de 2880 bytes, enteros en big-endian, BZERO/BSCALE) son conocimiento general que este laboratorio comprueba
sobre su propio archivo, no una cita del estandar.
Modelo: HDU primaria con SIMPLE, BITPIX=16, NAXIS=2, NAXIS1, NAXIS2, BZERO=32768, BSCALE=1 (enteros sin signo de 16 bits), tarjetas informativas y END; datos big-endian rellenos a 2880.
Lectura por dos vias: (a) analisis de tarjetas con struct; (b) modulo array con byteswap. Valor fisico = BZERO + BSCALE x valor almacenado.
Supuestos: una sola HDU, sin extensiones ni compresion. Validez: ilustrativa; no sustituye a una biblioteca FITS.
Tolerancia: igualdad exacta de los datos recuperados; tamano de archivo multiplo de 2880.
"""
from __future__ import annotations
import array, math, os, platform, random, struct, sys, tempfile

def tarjeta(clave, valor=None, comentario=""):
    if valor is None:
        s = clave.ljust(8)
    else:
        v = ("'" + str(valor).ljust(8) + "'") if isinstance(valor, str) else (("T" if valor else "F") if isinstance(valor, bool) else repr(valor))
        s = clave.ljust(8) + "= " + v.rjust(20) + (" / " + comentario if comentario else "")
    assert len(s) <= 80
    return s.ljust(80)

def escribir(ruta, datos, nx, ny):
    cards = [tarjeta("SIMPLE", True, "conforme al formato FITS"), tarjeta("BITPIX", 16), tarjeta("NAXIS", 2), tarjeta("NAXIS1", nx), tarjeta("NAXIS2", ny),
             tarjeta("BZERO", 32768, "entero sin signo de 16 bits"), tarjeta("BSCALE", 1),
             tarjeta("OBJECT", "SINTETICO", "ilustrativo"), tarjeta("INSTRUME", "CAMARA-X", "ilustrativo"), tarjeta("EXPTIME", 30.0, "[s] exposicion"),
             tarjeta("GAIN", 1.5, "[e-/ADU] ilustrativo"), tarjeta("DATE-OBS", "2026-11-09T00:00:00", "ficticio"), tarjeta("END")]
    h = "".join(cards).encode("ascii")
    h += b" " * (-len(h) % 2880)
    raw = b"".join(struct.pack(">h", v - 32768) for v in datos)
    raw += b"\0" * (-len(raw) % 2880)
    with open(ruta, "wb") as f:
        f.write(h + raw)
    return len(h), len(raw)

def leer_a(ruta):
    b = open(ruta, "rb").read()
    cards, pos = {}, 0
    while True:
        c = b[pos:pos + 80].decode("ascii"); pos += 80
        k = c[:8].strip()
        if k == "END":
            break
        if c[8:10] == "= ":
            cards[k] = c[10:].split(" / ")[0].strip().strip("'").strip()
    hdr = pos + (-pos % 2880)
    nx, ny = int(cards["NAXIS1"]), int(cards["NAXIS2"])
    bz = int(cards["BZERO"]); bs = int(cards["BSCALE"])
    vals = struct.unpack(">" + "h" * (nx * ny), b[hdr:hdr + 2 * nx * ny])
    return cards, [bz + bs * v for v in vals], hdr, len(b)

def leer_b(ruta, hdr, n):
    a = array.array("h")
    with open(ruta, "rb") as f:
        f.seek(hdr)
        a.frombytes(f.read(2 * n))
    if sys.byteorder == "little":
        a.byteswap()
    return [32768 + v for v in a]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    nx, ny = 40, 30
    datos = [min(65535, max(0, round(rng.gauss(1000, 30)))) for _ in range(nx * ny)]
    datos[0], datos[-1] = 0, 65535        # extremos del rango sin signo
    ruta = os.path.join(tempfile.mkdtemp(prefix="fits_b44_"), "prueba.fits")
    lh, ld = escribir(ruta, datos, nx, ny)
    tam = os.path.getsize(ruta)
    print(f"cabecera {lh} bytes, datos {ld} bytes, archivo {tam} bytes ({tam//2880} bloques de 2880)")
    assert tam % 2880 == 0 and tam == lh + ld
    assert ld == math.ceil(2 * nx * ny / 2880) * 2880
    cards, va, hdr, n = leer_a(ruta)
    vb = leer_b(ruta, hdr, nx * ny)
    print(f"tarjetas leidas: {len(cards)} ; NAXIS1={cards['NAXIS1']} NAXIS2={cards['NAXIS2']} BITPIX={cards['BITPIX']} EXPTIME={cards['EXPTIME']}")
    print(f"via A (struct) == datos: {va == datos} ; via B (array) == datos: {vb == datos}")
    assert va == datos and vb == datos and hdr == lh
    print(f"valor almacenado del primer pixel: {datos[0]-32768} -> fisico {datos[0]} ; ultimo: {datos[-1]-32768} -> fisico {datos[-1]}")
    assert datos[0] - 32768 == -32768 and datos[-1] - 32768 == 32767
    os.remove(ruta)
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
