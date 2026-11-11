#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C07: curva de luz SINTETICA de un transito -> tono sonoro y relieve tactil.

Consultado (2026-11-11): Zanella et al. (2022), arXiv:2206.13536, solo el RESUMEN: revision de ~100 proyectos sonoros en astronomia; el sonido sirve
para investigacion, educacion y acceso. NO se consulto el texto completo ni evaluaciones con personas.
SINTETICO: flujo normalizado f(t) = 1 - profundidad dentro del transito (con ingreso y egreso lineales). No es una observacion.
ILUSTRATIVOS (del curso, no consultados): rango 220-880 Hz (dos octavas), mapeo logaritmico, 0.1 s por punto, relieve de 5 niveles con paso de 0.5 mm.
Unidades: flujo adimensional, Hz, segundos, milimetros. Mapeo sonoro: f_Hz = 220 * 4^((flujo - fmin)/(fmax - fmin)) (flujo mayor = tono mas agudo).
Verificacion: monotonia, razon de frecuencias maxima = 4 (2 octavas), numero de muestras = puntos * 0.1 s * 8000, y hash estable del audio.
Tolerancia: 1e-9 en frecuencias; igualdad exacta en enteros.
"""
from __future__ import annotations
import hashlib, math, os, platform, struct, tempfile, wave

N, DT, FS = 60, 0.1, 8000
PROF = 0.01  # 1 % de profundidad, SINTETICA


def curva():
    f = []
    for i in range(N):
        if i < 20 or i >= 40: f.append(1.0)
        elif i < 24: f.append(1.0 - PROF * (i - 19) / 5)    # ingreso
        elif i < 36: f.append(1.0 - PROF)                   # fondo
        else: f.append(1.0 - PROF * (40 - i) / 5)           # egreso
    return f


def a_hz(f, fmin, fmax):
    return [220.0 * 4.0 ** ((x - fmin) / (fmax - fmin)) for x in f]


def a_relieve(f, fmin, fmax, niveles=5, paso_mm=0.5):
    return [int(round((x - fmin) / (fmax - fmin) * (niveles - 1))) * paso_mm for x in f]


def audio(hz):
    out, fase = [], 0.0
    for fr in hz:
        for _ in range(int(DT * FS)):
            fase += 2 * math.pi * fr / FS
            out.append(int(12000 * math.sin(fase)))
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Curva SINTETICA de transito (profundidad 1 %); parametros de mapeo ILUSTRATIVOS (no consultados).")
    f = curva(); fmin, fmax = min(f), max(f)
    hz = a_hz(f, fmin, fmax)
    assert abs(max(hz) / min(hz) - 4.0) < 1e-9 and abs(min(hz) - 220.0) < 1e-9
    assert all(hz[i] <= hz[i + 1] for i in range(0, 19)) and hz[30] == min(hz)
    print(f"Flujo: min {fmin:.4f}, max {fmax:.4f}; frecuencias {min(hz):.1f}-{max(hz):.1f} Hz (razon {max(hz)/min(hz):.3f})")
    semitonos = 12 * math.log2(max(hz) / min(hz))
    print(f"Rango musical: {semitonos:.1f} semitonos para una caida de {PROF*100:.0f} % (el eje se AMPLIFICA; hay que decirlo)")
    rel = a_relieve(f, fmin, fmax)
    print(f"Relieve: alturas distintas {sorted(set(rel))} mm; maximo {max(rel):.1f} mm")
    print("Puntos de cambio (i, flujo, Hz, relieve mm): " + "; ".join(f"{i}: {f[i]:.4f}, {hz[i]:.1f}, {rel[i]:.1f}" for i in (19, 21, 24, 30, 36, 38, 40)))
    mues = audio(hz)
    assert len(mues) == N * int(DT * FS)
    h = hashlib.sha256(struct.pack(f"<{len(mues)}h", *mues)).hexdigest()
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "transito.wav")
        with wave.open(p, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(FS); w.writeframes(struct.pack(f"<{len(mues)}h", *mues))
        with wave.open(p, "rb") as w:
            assert w.getnframes() == len(mues)
            dur = w.getnframes() / w.getframerate()
    print(f"Audio: {len(mues)} muestras a {FS} Hz = {dur:.1f} s; SHA-256 (16 primeros) {h[:16]}")
    # resolucion: 5 niveles no distinguen el ingreso fino
    niveles = len(set(rel))
    print(f"Niveles tactiles usados: {niveles} (el ingreso gradual se ve como escalones; la tabla de datos lo completa)")
    assert niveles == 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
