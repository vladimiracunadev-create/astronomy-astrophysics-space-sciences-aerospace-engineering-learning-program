#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C21: una etiqueta XML que describe un archivo binario (estilo PDS4, simplificado).

AVISO: la etiqueta de este laboratorio es una SIMPLIFICACIÓN DIDÁCTICA con
nombres inventados; NO es una etiqueta PDS4 válida y no se validó contra
ningún esquema PDS4. Ilustra solo la idea: un archivo de datos binario va
acompañado de un archivo XML que dice cómo leerlo (dimensiones, tipo, orden
de bytes, unidades, valor especial de dato ausente).
Datos: SINTÉTICOS. Una imagen de 24 filas x 32 columnas (float32, big-endian)
con una mancha gaussiana (amplitud 500 DN, centro fila 10, columna 20, sigma 3)
sobre un fondo de 50 DN, 12 píxeles marcados como ausentes con el valor especial
-1.0e32 (convención sintética). Semilla 20261105 para el ruido (sigma 2 DN).
Modelo: lectura guiada por la etiqueta: dtype = '>f4', forma (filas, columnas);
los píxeles con el valor especial se convierten a NaN.
Supuestos: orden C (la columna varía más rápido); sin cabecera binaria.
Validez: demostración; los productos de misión reales tienen estructura más rica.
Tolerancia: lectura idéntica a lo escrito (np.array_equal con NaN en la misma
posición); tamaño de archivo exactamente filas*columnas*4 bytes.
"""
from __future__ import annotations
import os, platform, sys, tempfile
import xml.etree.ElementTree as ET
import numpy as np

ETIQUETA = """<?xml version="1.0" encoding="UTF-8"?>
<producto_sintetico>
  <identificacion>
    <id_logico>urn:ejemplo:sintetico:imagen_demo</id_logico>
    <version>1.0</version>
  </identificacion>
  <archivo>
    <nombre>imagen.dat</nombre>
    <bytes>{bytes}</bytes>
  </archivo>
  <arreglo_2d>
    <ejes>
      <eje nombre="fila" elementos="{filas}" secuencia="1"/>
      <eje nombre="columna" elementos="{cols}" secuencia="2"/>
    </ejes>
    <tipo_dato>IEEE754MSBSingle</tipo_dato>
    <unidad>DN</unidad>
    <valor_especial_ausente>-1.0e32</valor_especial_ausente>
  </arreglo_2d>
</producto_sintetico>
"""
TIPOS = {"IEEE754MSBSingle": ">f4", "IEEE754LSBSingle": "<f4", "IEEE754MSBDouble": ">f8"}


def leer_producto(ruta_etiqueta, carpeta):
    raiz = ET.parse(ruta_etiqueta).getroot()
    nombre = raiz.findtext("archivo/nombre")
    declarados = int(raiz.findtext("archivo/bytes"))
    ejes = sorted(raiz.findall("arreglo_2d/ejes/eje"), key=lambda e: int(e.get("secuencia")))
    forma = tuple(int(e.get("elementos")) for e in ejes)
    tipo = TIPOS[raiz.findtext("arreglo_2d/tipo_dato")]
    ausente = float(raiz.findtext("arreglo_2d/valor_especial_ausente"))
    unidad = raiz.findtext("arreglo_2d/unidad")
    ruta = os.path.join(carpeta, nombre)
    real = os.path.getsize(ruta)
    esperado = int(np.prod(forma)) * np.dtype(tipo).itemsize
    if not (real == declarados == esperado):
        raise ValueError(f"tamaño inconsistente: archivo {real}, etiqueta {declarados}, esperado por forma y tipo {esperado}")
    datos = np.fromfile(ruta, dtype=tipo).reshape(forma).astype(np.float64)
    datos[datos == np.float64(np.float32(ausente))] = np.nan
    return datos, unidad, forma


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  (etiqueta simplificada, NO PDS4 válida)")
    rng = np.random.default_rng(20261105)
    filas, cols = 24, 32
    y, x = np.mgrid[0:filas, 0:cols]
    img = 50.0 + 500.0 * np.exp(-((y - 10) ** 2 + (x - 20) ** 2) / (2 * 3.0**2)) + rng.normal(0, 2.0, (filas, cols))
    img = img.astype(np.float32)
    ausentes = np.zeros(img.shape, bool)
    ausentes[0, :12] = True
    img_disco = img.copy()
    img_disco[ausentes] = np.float32(-1.0e32)

    with tempfile.TemporaryDirectory() as td:
        img_disco.astype(">f4").tofile(os.path.join(td, "imagen.dat"))
        tam = os.path.getsize(os.path.join(td, "imagen.dat"))
        with open(os.path.join(td, "imagen.xml"), "w", encoding="utf-8") as f:
            f.write(ETIQUETA.format(bytes=tam, filas=filas, cols=cols))
        print(f"archivo de datos: {tam} bytes = {filas} x {cols} x 4")
        prueba(tam == filas * cols * 4, "tamaño de archivo")
        datos, unidad, forma = leer_producto(os.path.join(td, "imagen.xml"), td)
        print(f"leído con la etiqueta: forma = {forma}, unidad = {unidad}, NaN = {int(np.isnan(datos).sum())}")
        esperado = img.astype(np.float64)
        esperado[ausentes] = np.nan
        prueba(np.array_equal(datos, esperado, equal_nan=True), "lectura idéntica a lo escrito")
        prueba(int(np.isnan(datos).sum()) == 12, "12 píxeles ausentes")
        cy, cx = np.unravel_index(np.nanargmax(datos), datos.shape)
        print(f"máximo en (fila, columna) = ({cy}, {cx}); valor = {np.nanmax(datos):.1f} DN")
        prueba((cy, cx) == (10, 20), "posición de la mancha")
        # lectura con la etiqueta equivocada (orden de bytes) -> basura detectable
        mal = np.fromfile(os.path.join(td, "imagen.dat"), dtype="<f4").reshape(forma)
        print(f"leído con el orden de bytes equivocado (little-endian): máximo = {np.nanmax(np.where(np.isfinite(mal), mal, np.nan)):.3g} (absurdo)")
        prueba(not np.allclose(np.nan_to_num(mal), np.nan_to_num(esperado), rtol=1e-3), "el orden equivocado no debe coincidir")
        # tamaño inconsistente: se trunca el archivo
        with open(os.path.join(td, "imagen.dat"), "r+b") as f:
            f.truncate(tam - 4)
        try:
            leer_producto(os.path.join(td, "imagen.xml"), td)
            prueba(False, "debía detectar el archivo truncado")
        except ValueError as e:
            print(f"archivo truncado detectado: {e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
