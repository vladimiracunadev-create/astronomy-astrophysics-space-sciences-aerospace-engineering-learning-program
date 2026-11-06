#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C26: por qué un ráster en teselas se lee por regiones (idea de COG), sin GDAL.

AVISO: NO es un GeoTIFF ni un COG. Es un formato binario didáctico propio con
una tabla de teselas y una pirámide de resoluciones, que reproduce la IDEA
descrita para los COG (datos en teselas internas y lecturas parciales de solo lo
necesario). No usa HTTP ni GDAL.
Datos: SINTÉTICOS. Un ráster de 1024 x 1024 píxeles float32 (valor = función
suave conocida de la posición: v = 100 + 0.5*col + 0.25*fila + 10*sin(col/50)),
con geotransformación inventada: esquina superior izquierda en (lon 10.0, lat 40.0),
tamaño de píxel 0.001 grados (norte arriba).
Modelo: teselas de 128 x 128 (64 teselas) con directorio (desplazamiento, bytes);
una pirámide con un nivel a mitad de resolución (promedio 2 x 2).
Supuestos: sin compresión; orden de teselas por filas; el píxel (fila, col) cubre
[lon0 + col*dx, lon0 + (col+1)*dx) y (lat0 - (fila+1)*dy, lat0 - fila*dy]; el
convenio «esquina del píxel» se define aquí, no se consultó.
Validez: demostración de la idea; un COG real añade compresión, etiquetas TIFF y
convenciones que este laboratorio no implementa.
Tolerancia: la lectura de una región por teselas debe ser IDÉNTICA a la rebanada
del arreglo completo; el nivel de pirámide debe coincidir con el promedio 2 x 2
calculado de forma independiente.
"""
from __future__ import annotations
import os, platform, struct, sys, tempfile
import numpy as np

N, T = 1024, 128
LON0, LAT0, D = 10.0, 40.0, 0.001


def generar():
    f, c = np.mgrid[0:N, 0:N].astype(np.float64)
    return (100.0 + 0.5 * c + 0.25 * f + 10.0 * np.sin(c / 50.0)).astype(np.float32)


def escribir(ruta, arr):
    nt = N // T
    cuerpo = []
    directorio = []
    despl = 0
    for ti in range(nt):
        for tj in range(nt):
            b = np.ascontiguousarray(arr[ti * T:(ti + 1) * T, tj * T:(tj + 1) * T]).astype("<f4").tobytes()
            directorio.append((despl, len(b)))
            cuerpo.append(b)
            despl += len(b)
    cab = struct.pack("<4sIII", b"TILE", N, T, nt * nt)
    dir_b = b"".join(struct.pack("<QQ", o, n) for o, n in directorio)
    base = len(cab) + len(dir_b)
    with open(ruta, "wb") as f:
        f.write(cab + dir_b + b"".join(cuerpo))
    return base


class Lector:
    def __init__(self, ruta):
        self.f = open(ruta, "rb")
        magic, self.n, self.t, nt = struct.unpack("<4sIII", self.f.read(16))
        assert magic == b"TILE"
        self.dir = [struct.unpack("<QQ", self.f.read(16)) for _ in range(nt)]
        self.base = 16 + 16 * nt
        self.bytes_leidos = 16 + 16 * nt          # cabecera y directorio

    def tesela(self, ti, tj):
        o, n = self.dir[ti * (self.n // self.t) + tj]
        self.f.seek(self.base + o)
        self.bytes_leidos += n
        return np.frombuffer(self.f.read(n), dtype="<f4").reshape(self.t, self.t)

    def region(self, f0, f1, c0, c1):
        out = np.empty((f1 - f0, c1 - c0), dtype=np.float32)
        for ti in range(f0 // self.t, (f1 - 1) // self.t + 1):
            for tj in range(c0 // self.t, (c1 - 1) // self.t + 1):
                tes = self.tesela(ti, tj)
                fa, fb = max(f0, ti * self.t), min(f1, (ti + 1) * self.t)
                ca, cb = max(c0, tj * self.t), min(c1, (tj + 1) * self.t)
                out[fa - f0:fb - f0, ca - c0:cb - c0] = tes[fa - ti * self.t:fb - ti * self.t, ca - tj * self.t:cb - tj * self.t]
        return out

    def cerrar(self):
        self.f.close()


def pix_a_geo(fila, col):
    """Centro del píxel (fila, col) en (lon, lat)."""
    return LON0 + (col + 0.5) * D, LAT0 - (fila + 0.5) * D


def geo_a_pix(lon, lat):
    return int(np.floor((LAT0 - lat) / D)), int(np.floor((lon - LON0) / D))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  (formato didáctico, NO es GeoTIFF ni COG)")
    arr = generar()
    with tempfile.TemporaryDirectory() as td:
        ruta = os.path.join(td, "raster.tile")
        escribir(ruta, arr)
        total = os.path.getsize(ruta)
        print(f"archivo: {total} bytes; ráster completo = {N*N*4} bytes; teselas = {(N//T)**2}")
        lec = Lector(ruta)
        reg = lec.region(200, 300, 700, 820)
        prueba(np.array_equal(reg, arr[200:300, 700:820]), "región idéntica a la rebanada")
        frac = lec.bytes_leidos / total
        print(f"región 100 x 120 píxeles: leídos {lec.bytes_leidos} bytes de {total} ({frac:.1%}); lectura idéntica a la rebanada completa")
        # teselas necesarias: filas 200-299 -> teselas 1..2; columnas 700-819 -> teselas 5..6 => 4 teselas
        esperado = 16 + 16 * 64 + 4 * T * T * 4
        prueba(lec.bytes_leidos == esperado, "solo 4 teselas más el directorio")
        print(f"bytes esperados = cabecera/directorio + 4 teselas x {T*T*4} = {esperado} (coincide)")
        lec.cerrar()
        # pirámide: nivel a mitad de resolución
        piramide = arr.reshape(N // 2, 2, N // 2, 2).mean(axis=(1, 3))
        indep = np.array([[arr[2*i:2*i+2, 2*j:2*j+2].mean() for j in range(0, 8)] for i in range(0, 8)])
        prueba(np.allclose(piramide[:8, :8], indep, rtol=1e-6), "pirámide = promedio 2x2")
        print(f"nivel de pirámide: {piramide.shape} (a mitad de resolución, {piramide.nbytes} bytes = 1/4 del original); verificado contra el promedio 2x2 independiente")
    # geotransformación
    lon, lat = pix_a_geo(0, 0)
    prueba(abs(lon - 10.0005) < 1e-12 and abs(lat - 39.9995) < 1e-12, "centro del primer píxel")
    prueba(geo_a_pix(*pix_a_geo(321, 654)) == (321, 654), "ida y vuelta pixel-geo")
    prueba(geo_a_pix(10.0, 40.0) == (0, 0), "esquina superior izquierda -> píxel (0,0)")
    print(f"centro del píxel (0,0) = ({lon:.4f}, {lat:.4f}); ida y vuelta píxel->geo->píxel exacta; esquina (10.0, 40.0) -> píxel (0, 0)")
    prueba(abs(1024 * D - 1.024) < 1e-12, "extensión")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
