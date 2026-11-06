#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C18: un flujo de datos con verificación, caché y procedencia.

AVISO: no hay acceso a ningún archivo ni servicio remoto. El "archivo remoto"
es un catálogo SINTÉTICO de 5000 estrellas ficticias generado en el script
(semilla 20261105) y guardado en un directorio temporal que hace de servidor.
Flujo: adquirir -> verificar huella -> leer -> filtrar (consulta) -> resumir ->
registrar procedencia (JSON con huellas de entrada y salida, parámetros y
versiones). La consulta se escribe también en ADQL (texto) pero NO se envía.
Modelo del catálogo: paralaje p ~ 0.5 + Exp(2) mas; magnitud ~ N(14, 2).
Supuestos: los datos no cambian durante el flujo; sin red.
Validez: demostración de estructura del flujo, no de una consulta real.
Tolerancia: la consulta debe devolver EXACTAMENTE las filas que cumplen el
criterio contado por un método independiente; dos ejecuciones con los mismos
parámetros deben dar la misma huella de salida; un parámetro distinto, otra.
"""
from __future__ import annotations
import hashlib, io, json, os, platform, sys, tempfile
import numpy as np
import pandas as pd


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def generar_servidor(carpeta):
    rng = np.random.default_rng(20261105)
    n = 5000
    df = pd.DataFrame({
        "id": np.arange(n),
        "paralaje_mas": 0.5 + rng.exponential(2.0, n),
        "mag": rng.normal(14.0, 2.0, n),
    })
    ruta = os.path.join(carpeta, "catalogo.csv")
    df.to_csv(ruta, index=False, float_format="%.9g")
    with open(ruta, "rb") as f:
        return ruta, sha256_bytes(f.read())


def consulta_adql(p_min, mag_max):
    return (f"SELECT id, paralaje_mas, mag FROM catalogo "
            f"WHERE paralaje_mas > {p_min} AND mag < {mag_max}")


class Flujo:
    def __init__(self, cache):
        self.cache = cache
        self.llamadas_descarga = 0

    def adquirir(self, ruta_servidor, huella_esperada):
        copia = os.path.join(self.cache, "catalogo.csv")
        if os.path.exists(copia):
            with open(copia, "rb") as f:
                if sha256_bytes(f.read()) == huella_esperada:
                    return copia                       # caché válida: no se vuelve a descargar
        self.llamadas_descarga += 1
        with open(ruta_servidor, "rb") as f:
            datos = f.read()
        if sha256_bytes(datos) != huella_esperada:
            raise ValueError("la huella del archivo no coincide con la publicada")
        with open(copia, "wb") as f:
            f.write(datos)
        return copia

    def ejecutar(self, ruta_servidor, huella, p_min, mag_max):
        ruta = self.adquirir(ruta_servidor, huella)
        df = pd.read_csv(ruta)
        sel = df[(df["paralaje_mas"] > p_min) & (df["mag"] < mag_max)]
        resumen = {"n_filas": int(len(sel)),
                   "distancia_mediana_pc": round(float(np.median(1000.0 / sel["paralaje_mas"])), 6) if len(sel) else None}
        salida = json.dumps(resumen, sort_keys=True).encode()
        procedencia = {
            "entrada": {"archivo": "catalogo.csv", "sha256": huella},
            "parametros": {"p_min_mas": p_min, "mag_max": mag_max},
            "consulta_adql_equivalente": consulta_adql(p_min, mag_max),
            "versiones": {"python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__},
            "salida": {"resumen": resumen, "sha256": sha256_bytes(salida)},
        }
        return resumen, procedencia


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  pandas {pd.__version__}  (sin red)")
    with tempfile.TemporaryDirectory() as srv, tempfile.TemporaryDirectory() as cache:
        ruta_srv, huella = generar_servidor(srv)
        print(f"catálogo sintético: sha256 = {huella[:16]}...")
        fl = Flujo(cache)
        r1, p1 = fl.ejecutar(ruta_srv, huella, 2.0, 15.0)
        r2, p2 = fl.ejecutar(ruta_srv, huella, 2.0, 15.0)
        print(f"consulta (p > 2 mas, mag < 15): {r1}")
        print(f"descargas realizadas en 2 ejecuciones: {fl.llamadas_descarga} (la segunda usa la caché)")
        prueba(fl.llamadas_descarga == 1, "una sola descarga")
        prueba(p1["salida"]["sha256"] == p2["salida"]["sha256"], "misma huella de salida")
        # conteo independiente
        df = pd.read_csv(os.path.join(cache, "catalogo.csv"))
        n_indep = int(np.count_nonzero((df["paralaje_mas"].to_numpy() > 2.0) & (df["mag"].to_numpy() < 15.0)))
        prueba(n_indep == r1["n_filas"], "conteo independiente")
        print(f"conteo independiente = {n_indep} (coincide)")
        # parámetro distinto, otra huella
        r3, p3 = fl.ejecutar(ruta_srv, huella, 3.0, 15.0)
        print(f"consulta (p > 3 mas, mag < 15): {r3}; huella de salida distinta: {p3['salida']['sha256'] != p1['salida']['sha256']}")
        prueba(p3["salida"]["sha256"] != p1["salida"]["sha256"], "otro parámetro, otra huella")
        prueba(r3["n_filas"] < r1["n_filas"], "filtro más estricto, menos filas")
        # archivo corrupto en el servidor
        with open(ruta_srv, "ab") as f:
            f.write(b"\n")
        os.remove(os.path.join(cache, "catalogo.csv"))
        try:
            Flujo(cache).adquirir(ruta_srv, huella)
            prueba(False, "debía rechazar el archivo modificado")
        except ValueError as e:
            print(f"archivo alterado en origen rechazado: {e}")
        print("procedencia (JSON, claves):", sorted(p1.keys()))
        print("consulta ADQL equivalente (no enviada):", p1["consulta_adql_equivalente"])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
