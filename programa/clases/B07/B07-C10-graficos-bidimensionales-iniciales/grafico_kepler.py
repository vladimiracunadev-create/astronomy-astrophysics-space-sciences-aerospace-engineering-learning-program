#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C10: gráfico bidimensional período-semieje con ejes logarítmicos.

Datos PUBLICADOS: planetas_nssdc.csv (clase B07-C08): semieje mayor (1e6 km) y período
sidéreo (d) del NASA NSSDC, consultados el 2026-11-05.
Modelo: si T ∝ a^p, en escala log-log los puntos caen sobre una recta de pendiente p.
Ajuste: recta por mínimos cuadrados sobre log10(a) y log10(T) (np.polyfit grado 1).
Supuestos: sin incertidumbres en los datos; pendiente esperada p = 1,5 (Kepler).
Dominio de validez: planetas del sistema solar. Tolerancia: |pendiente − 1,5| < 0,01.
Requiere: numpy 2.4.4 y matplotlib 3.10.8 (Python 3.12.9); backend sin pantalla (Agg).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # sin ventana: solo guarda archivos
import matplotlib.pyplot as plt
import numpy as np

AQUI = Path(__file__).resolve().parent
CSV = AQUI.parent / "B07-C08-lectura-de-archivos-csv" / "planetas_nssdc.csv"
SALIDA = AQUI / "kepler_loglog.png"


def leer(ruta: Path):
    """Devuelve (nombres, semieje en 1e6 km, período en d) como arreglos."""
    with ruta.open(encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
    return ([f["nombre"] for f in filas],
            np.array([float(f["semieje_1e6km"]) for f in filas]),
            np.array([float(f["periodo_sidereo_d"]) for f in filas]))


def ajustar_pendiente(a, t):
    """Devuelve (pendiente, ordenada) del ajuste lineal de log10(t) frente a log10(a)."""
    pendiente, ordenada = np.polyfit(np.log10(a), np.log10(t), 1)
    return float(pendiente), float(ordenada)


def dibujar(nombres, a, t, pendiente, ordenada, ruta: Path) -> None:
    """Dibuja dos paneles (lineal y log-log) y guarda la figura en `ruta`."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    ax1.plot(a, t, "o")
    ax1.set_xlabel("Semieje mayor (10⁶ km)")
    ax1.set_ylabel("Período sidéreo (d)")
    ax1.set_title("Escala lineal")
    ax2.loglog(a, t, "o", label="datos NASA NSSDC (publicados)")
    xs = np.array([a.min(), a.max()])
    ax2.loglog(xs, 10 ** ordenada * xs ** pendiente, "-", label=f"ajuste: pendiente {pendiente:.3f}")
    for n, x, y in zip(nombres, a, t):
        ax2.annotate(n, (x, y), textcoords="offset points", xytext=(5, -10), fontsize=8)
    ax2.set_xlabel("Semieje mayor (10⁶ km), escala log")
    ax2.set_ylabel("Período sidéreo (d), escala log")
    ax2.set_title("Escala log-log")
    ax2.legend(loc="upper left")
    fig.suptitle("Período frente a semieje mayor de los ocho planetas")
    fig.savefig(ruta, dpi=110)
    plt.close(fig)


def pruebas() -> None:
    nombres, a, t = leer(CSV)
    assert len(nombres) == 8 and a.shape == t.shape == (8,)
    pendiente, ordenada = ajustar_pendiente(a, t)
    assert abs(pendiente - 1.5) < 0.01, pendiente                       # tolerancia declarada
    p_exacta, _ = ajustar_pendiente(np.array([1.0, 10.0, 100.0]), np.array([1.0, 10 ** 1.5, 10 ** 3.0]))
    assert abs(p_exacta - 1.5) < 1e-12                                  # caso analítico exacto
    dibujar(nombres, a, t, pendiente, ordenada, SALIDA)
    assert SALIDA.exists() and SALIDA.stat().st_size > 10_000           # se generó el archivo


def main() -> int:
    pruebas()
    nombres, a, t = leer(CSV)
    pendiente, ordenada = ajustar_pendiente(a, t)
    print(f"python {sys.version.split()[0]} | numpy {np.__version__} | matplotlib {matplotlib.__version__} | pruebas OK")
    print(f"Pendiente del ajuste log-log: {pendiente:.4f} (esperada 1.5)")
    print(f"Ordenada log10(T) en log10(a)=0: {ordenada:.4f}")
    print(f"Figura guardada: {SALIDA.name} ({SALIDA.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
