"""B59-C05 · Desmezcla lineal de una mezcla mineral y rendimiento de agua extraíble.

Datos SINTÉTICOS (no medidos): cuatro miembros extremos con "espectros" de 12 bandas inventados y
un rendimiento de agua por miembro extremo inventado. No son minerales marcianos reales.
Modelo: mezcla lineal y = E a + ruido, con a >= 0 y suma(a) = 1. Se resuelve por mínimos cuadrados no
negativos (conjunto activo, implementación propia) y se contrasta con el solucionador NNLS de SciPy.
Rendimiento de agua de la mezcla = suma(a_i w_i) (masa de agua por masa de roca).
Unidades: reflectancia adimensional; abundancias como fracción másica (supuesto de mezcla íntima lineal, no
cierto para mezclas íntimas reales: ahí domina la mezcla no lineal).
Tolerancia: abundancias recuperadas a menos de 0,02 de las sembradas; coincidencia con SciPy a 1e-9.
"""
import math
import platform
import random

import numpy as np
import scipy
from scipy.optimize import nnls

SEMILLA = 20261109
NB = 12
NOMBRES = ["miembro A (sintetico)", "miembro B (sintetico)", "miembro C (sintetico)", "miembro D (sintetico)"]
W_AGUA = np.array([0.00, 0.08, 0.14, 0.05])     # kg agua / kg roca, SINTETICO
A_REAL = np.array([0.45, 0.30, 0.15, 0.10])
SIGMA = 0.003


def espectros():
    rng = random.Random(SEMILLA)
    cols = []
    for k in range(4):
        base = [0.25 + 0.15 * math.sin(0.6 * i + 1.3 * k) + 0.05 * k for i in range(NB)]
        cols.append([b + 0.02 * rng.random() for b in base])
    return np.array(cols).T


def nnls_conjunto_activo(E, y, it=200):
    """Lawson-Hanson simplificado, solo con numpy."""
    n = E.shape[1]
    P = []
    x = np.zeros(n)
    w = E.T @ (y - E @ x)
    for _ in range(it):
        resto = [j for j in range(n) if j not in P]
        if not resto or max(w[j] for j in resto) <= 1e-12:
            break
        P.append(max(resto, key=lambda j: w[j]))
        while True:
            z = np.zeros(n)
            z[P] = np.linalg.lstsq(E[:, P], y, rcond=None)[0]
            if all(z[j] > 0 for j in P):
                x = z
                break
            alpha = min(x[j] / (x[j] - z[j]) for j in P if z[j] <= 0)
            x = x + alpha * (z - x)
            P = [j for j in P if x[j] > 1e-14]
        w = E.T @ (y - E @ x)
    return x


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__}")
    E = espectros()
    rng = np.random.default_rng(SEMILLA)
    y = E @ A_REAL + rng.normal(0, SIGMA, NB)
    a_prop = nnls_conjunto_activo(E, y)
    a_sp, _ = nnls(E, y)
    print("miembro                  sembrado   recuperado")
    for n, s, r in zip(NOMBRES, A_REAL, a_prop):
        print(f"{n:24s} {s:8.3f}   {r:9.3f}")
    print(f"Suma de abundancias recuperadas = {a_prop.sum():.3f} (no se impone; sirve de control)")
    assert np.max(np.abs(a_prop - A_REAL)) < 0.02
    dif = np.max(np.abs(a_prop - a_sp))
    print(f"Maxima diferencia con scipy.optimize.nnls = {dif:.2e}")
    assert dif < 1e-9
    a_n = a_prop / a_prop.sum()
    w_real = float(A_REAL @ W_AGUA)
    w_est = float(a_n @ W_AGUA)
    print(f"Rendimiento de agua: sembrado = {100*w_real:.2f} % ; estimado = {100*w_est:.2f} % ; diferencia = {100*(w_est-w_real):+.3f} pp")
    # Incertidumbre por remuestreo del ruido (200 repeticiones)
    est = []
    for _ in range(200):
        yy = E @ A_REAL + rng.normal(0, SIGMA, NB)
        aa = nnls(E, yy)[0]
        est.append(float((aa / aa.sum()) @ W_AGUA))
    print(f"Dispersion del rendimiento por ruido (200 repeticiones): media = {100*np.mean(est):.2f} % ; desv. = {100*np.std(est):.3f} pp")
    # Mal condicionamiento: numero de condicion de E
    print(f"Numero de condicion de la matriz de miembros extremos = {np.linalg.cond(E):.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
