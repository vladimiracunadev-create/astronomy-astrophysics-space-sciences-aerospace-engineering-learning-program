#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C17: revisar una definición de contenedor y simular el caché de capas.

AVISO: este laboratorio NO construye ni ejecuta ningún contenedor (no se usó
Docker). Trabaja sobre TEXTO: revisa un Dockerfile de ejemplo con reglas de
reproducibilidad y simula, con un encadenado de hashes SHA-256, cómo el caché
de capas decide qué se reconstruye.
Datos: SINTÉTICOS. Un Dockerfile de ejemplo (dos versiones: una descuidada y
otra revisada) y dos archivos ficticios (uv.lock y analisis.py).
Modelo del caché: la huella de una capa = SHA-256(huella de la capa anterior +
texto de la instrucción + huella de los archivos que la instrucción copia).
Si la huella no cambia, la capa se reutiliza; si cambia, se reconstruye esa
capa y todas las siguientes.
Supuestos: es una simulación de la idea, no del algoritmo real de Docker.
Validez: demostración; las reglas de revisión son convenciones de esta clase.
Tolerancia: conteos exactos de capas reutilizadas y reconstruidas.
"""
from __future__ import annotations
import hashlib, platform, re, sys

DESCUIDADO = """FROM python:latest
COPY . /app
RUN pip install numpy scipy
CMD python /app/analisis.py
"""

REVISADO = """FROM python:3.12.9-slim
WORKDIR /app
COPY uv.lock pyproject.toml ./
RUN pip install uv==0.13.7 && uv sync --locked
COPY analisis.py ./
USER 1000
CMD ["uv", "run", "python", "analisis.py"]
"""


def revisar(texto):
    """Devuelve la lista de hallazgos (vacía si pasa todas las reglas)."""
    h = []
    lineas = [l.strip() for l in texto.splitlines() if l.strip() and not l.startswith("#")]
    froms = [l for l in lineas if l.upper().startswith("FROM ")]
    if not froms:
        h.append("falta FROM")
    else:
        imagen = froms[0].split()[1]
        if ":" not in imagen or imagen.endswith(":latest"):
            h.append("imagen base sin versión fija (latest o sin etiqueta)")
    if not any(l.upper().startswith("USER ") for l in lineas):
        h.append("se ejecuta como root (falta USER)")
    if not any(l.upper().startswith("WORKDIR ") for l in lineas):
        h.append("falta WORKDIR")
    if any(re.match(r"RUN pip install [^&]*$", l) and "==" not in l for l in lineas):
        h.append("pip install sin versiones fijadas")
    primera_copy = next((i for i, l in enumerate(lineas) if l.upper().startswith("COPY ")), None)
    if primera_copy is not None and re.match(r"COPY \. ", lineas[primera_copy]):
        h.append("COPY . antes de instalar dependencias: cualquier cambio invalida el caché de todo")
    if not any("lock" in l for l in lineas):
        h.append("no usa un archivo de bloqueo")
    return h


def huellas(texto, archivos):
    """Huella encadenada por instrucción. archivos: dict nombre -> contenido (bytes)."""
    prev, out = "", []
    for l in [l.strip() for l in texto.splitlines() if l.strip()]:
        contenido = b""
        if l.upper().startswith("COPY "):
            for nombre in archivos:
                if nombre in l or " . " in l + " ":
                    contenido += archivos[nombre]
        prev = hashlib.sha256((prev + l).encode() + contenido).hexdigest()
        out.append(prev)
    return out


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  (no se construyó ningún contenedor)")
    h1, h2 = revisar(DESCUIDADO), revisar(REVISADO)
    print(f"Dockerfile descuidado: {len(h1)} hallazgos")
    for x in h1:
        print("  -", x)
    print(f"Dockerfile revisado: {len(h2)} hallazgos")
    prueba(len(h1) >= 5, "el descuidado debe tener varios hallazgos")
    prueba(h2 == [], "el revisado debe pasar")

    base = {"uv.lock": b"lock v1", "pyproject.toml": b"proyecto v1", "analisis.py": b"print('v1')"}
    a = huellas(REVISADO, base)
    # 1) sin cambios: todo se reutiliza
    prueba(huellas(REVISADO, base) == a, "determinista")
    # 2) cambia solo el script de análisis: se reconstruyen las capas desde su COPY
    b = huellas(REVISADO, {**base, "analisis.py": b"print('v2')"})
    reutil = sum(1 for x, y in zip(a, b) if x == y)
    print(f"cambia analisis.py: {reutil} de {len(a)} capas reutilizadas, {len(a)-reutil} reconstruidas")
    prueba(reutil == 4 and len(a) == 7, "con el orden revisado solo se reconstruyen las 3 últimas")
    # 3) cambia el archivo de bloqueo: se reconstruyen casi todas
    c = huellas(REVISADO, {**base, "uv.lock": b"lock v2"})
    reutil_c = sum(1 for x, y in zip(a, c) if x == y)
    print(f"cambia uv.lock: {reutil_c} de {len(a)} capas reutilizadas, {len(a)-reutil_c} reconstruidas")
    prueba(reutil_c == 2, "cambiar el bloqueo invalida desde su COPY")
    # 4) en el Dockerfile descuidado, cambiar el script reconstruye casi todo
    d1 = huellas(DESCUIDADO, base)
    d2 = huellas(DESCUIDADO, {**base, "analisis.py": b"print('v2')"})
    reutil_d = sum(1 for x, y in zip(d1, d2) if x == y)
    print(f"descuidado, cambia analisis.py: {reutil_d} de {len(d1)} capas reutilizadas")
    prueba(reutil_d == 1, "COPY . invalida todo salvo FROM")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
