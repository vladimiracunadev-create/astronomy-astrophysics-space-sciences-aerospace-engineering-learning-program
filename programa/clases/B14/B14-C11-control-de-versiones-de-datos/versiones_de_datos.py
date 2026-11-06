#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C11: versiones de datos por contenido (sumas de verificación).

Datos: SINTÉTICOS. Un arreglo de 1000 flujos relativos (adimensionales) de
una fuente ficticia, media 1.0 y desviación 0.01, semilla fija 20261105.
Una "versión 2" cambia exactamente un valor de la versión 1.
Modelo: almacén direccionado por contenido: cada archivo se guarda bajo el
SHA-256 de sus bytes; un manifiesto JSON asigna nombres lógicos a hashes; una
"versión" es un manifiesto. Es el mismo principio que usan Git y DVC (DVC usa
MD5 según su documentación; aquí se usa SHA-256).
Supuestos: sin red ni remoto; un solo equipo; sin protección frente a un
atacante que manipule también el manifiesto.
Validez: demostración del principio; no sustituye a Git ni a DVC.
Tolerancia: el vector de prueba del NIST ("abc") debe coincidir exactamente;
la corrupción de un solo bit debe ser detectada siempre.
"""
from __future__ import annotations
import hashlib, json, os, platform, sys, tempfile
import numpy as np

SHA256_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


class Almacen:
    def __init__(self, raiz):
        self.raiz = raiz
        os.makedirs(os.path.join(raiz, "objetos"), exist_ok=True)

    def poner(self, datos: bytes) -> str:
        h = sha256(datos)
        ruta = os.path.join(self.raiz, "objetos", h)
        if not os.path.exists(ruta):          # el mismo contenido se guarda una sola vez
            with open(ruta, "wb") as f:
                f.write(datos)
        return h

    def leer(self, h: str) -> bytes:
        with open(os.path.join(self.raiz, "objetos", h), "rb") as f:
            datos = f.read()
        if sha256(datos) != h:
            raise ValueError(f"objeto corrupto: {h[:12]}...")
        return datos

    def n_objetos(self) -> int:
        return len(os.listdir(os.path.join(self.raiz, "objetos")))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def bits_distintos(h1: str, h2: str) -> int:
    return bin(int(h1, 16) ^ int(h2, 16)).count("1")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    # 1) vector de prueba del NIST
    prueba(sha256(b"abc") == SHA256_ABC, "vector de prueba SHA-256 de 'abc'")
    print(f"SHA-256('abc') = {sha256(b'abc')}  (coincide con el ejemplo del NIST)")

    rng = np.random.default_rng(20261105)
    v1 = rng.normal(1.0, 0.01, 1000)
    v2 = v1.copy()
    v2[500] += 1e-9                         # un solo valor, un cambio mínimo
    b1, b2 = v1.tobytes(), v2.tobytes()

    with tempfile.TemporaryDirectory() as td:
        al = Almacen(td)
        h1, h1b, h2 = al.poner(b1), al.poner(b1), al.poner(b2)
        print(f"v1 = {h1[:16]}...  v1 repetido = {h1b[:16]}...  v2 = {h2[:16]}...")
        prueba(h1 == h1b, "mismo contenido, mismo hash")
        prueba(h1 != h2, "un cambio mínimo cambia el hash")
        prueba(al.n_objetos() == 2, "el contenido repetido se guarda una sola vez")
        print(f"objetos en el almacén tras 3 inserciones: {al.n_objetos()} (contenido repetido deduplicado)")
        print(f"bits distintos entre los hashes de v1 y v2 (de 256): {bits_distintos(h1, h2)}")

        # 2) manifiestos como versiones
        man1 = {"flujo.npy": h1}
        man2 = {"flujo.npy": h2}
        json_man = json.dumps({"v1": man1, "v2": man2}, sort_keys=True)
        dev = json.loads(json_man)
        prueba(np.array_equal(np.frombuffer(al.leer(dev["v1"]["flujo.npy"])), v1), "recupera v1 exacta")
        prueba(np.array_equal(np.frombuffer(al.leer(dev["v2"]["flujo.npy"])), v2), "recupera v2 exacta")
        diferencias = np.flatnonzero(np.frombuffer(al.leer(h1)) != np.frombuffer(al.leer(h2)))
        print(f"posiciones que cambian entre v1 y v2: {diferencias.tolist()}")
        prueba(diferencias.tolist() == [500], "solo cambia la posición 500")

        # 3) corrupción de un solo bit: debe detectarse siempre
        ruta = os.path.join(td, "objetos", h1)
        with open(ruta, "rb") as f:
            corrupto = bytearray(f.read())
        corrupto[1234] ^= 0x01
        with open(ruta, "wb") as f:
            f.write(corrupto)
        try:
            al.leer(h1)
            prueba(False, "debía detectar la corrupción")
        except ValueError as e:
            print(f"corrupción de 1 bit detectada: {e}")

        # 4) avalancha: bits distintos al cambiar 1 bit del mensaje
        base = b1
        distintos = []
        for k in range(20):
            m = bytearray(base)
            m[k * 7] ^= 0x01
            distintos.append(bits_distintos(sha256(base), sha256(bytes(m))))
        print(f"avalancha: bits distintos en 20 cambios de 1 bit: mín {min(distintos)}, media {np.mean(distintos):.1f}, máx {max(distintos)} (de 256)")
        prueba(min(distintos) > 80 and max(distintos) < 176, "avalancha cercana a 128")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
