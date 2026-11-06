#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C21: regresión dinámica con retardo y regresión espuria.

Datos: SINTÉTICOS, semilla fija. Un "impulsor" x_t (AR(1), phi = 0.8) y una
respuesta y_t = a y_{t-1} + b x_{t-2} + e_t con a = 0.5, b = 0.8, e ~ N(0, 0.5^2),
N = 3000 pasos de 3 h (la escala de tiempo del índice Kp, NOAA SWPC).
Referencias: (1) mínimos cuadrados ordinarios recupera (a, b) dentro de 3
errores estándar; (2) el criterio AIC elige el retardo correcto (2);
(3) prueba de causalidad en el sentido de Granger por razón de F (RSS restringida
frente a completa): p pequeño cuando x impulsa a y y no pequeño cuando x es
independiente; (4) regresión espuria: dos paseos aleatorios independientes dan
|t| > 2 en una fracción grande de casos; con diferencias, ~5 %.
Supuestos: modelo lineal, ruido blanco gaussiano, series estacionarias (salvo (4)).
Tolerancias: 3 sigma en (1); fracción > 0.5 en (4) sin diferenciar y < 0.10 diferenciando.
"""
import platform
import sys

import numpy as np
import scipy
from scipy import stats


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def mco(y, X):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    s2 = r @ r / (len(y) - X.shape[1])
    cov = s2 * np.linalg.inv(X.T @ X)
    return b, np.sqrt(np.diag(cov)), r @ r


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15021)
N, a_, b_ = 3000, 0.5, 0.8
x = np.zeros(N)
for t in range(1, N):
    x[t] = 0.8 * x[t - 1] + rng.standard_normal()
y = np.zeros(N)
e = 0.5 * rng.standard_normal(N)
for t in range(2, N):
    y[t] = a_ * y[t - 1] + b_ * x[t - 2] + e[t]

# (1) Estimación con el modelo correcto
t0 = 5
Y = y[t0:]
X = np.column_stack([y[t0 - 1:-1], x[t0 - 2:-2]])
b, se, rss = mco(Y, X)
print(f"(1) y_t = a y_(t-1) + b x_(t-2): a = {b[0]:.4f} ± {se[0]:.4f} (real {a_}); b = {b[1]:.4f} ± {se[1]:.4f} (real {b_})")
prueba(abs(b[0] - a_) < 3 * se[0] and abs(b[1] - b_) < 3 * se[1], "recupera los coeficientes")

# (2) Selección del retardo por AIC
print("(2) AIC al usar x_(t-L) (con y_(t-1)):")
aic = {}
for L in range(0, 6):
    Yl = y[t0:]
    Xl = np.column_stack([y[t0 - 1:-1], x[t0 - L:N - L]])
    bl, sel, rssl = mco(Yl, Xl)
    aic[L] = len(Yl) * np.log(rssl / len(Yl)) + 2 * 2
    print(f"    L = {L}: AIC = {aic[L]:.1f}; coeficiente de x = {bl[1]:+.3f}")
prueba(min(aic, key=aic.get) == 2, "AIC elige L = 2")


# (3) Causalidad de Granger (razón de F)
def granger(yv, xv, p=4):
    T = len(yv)
    Yg = yv[p:]
    Ly = np.column_stack([yv[p - k:T - k] for k in range(1, p + 1)])
    Lx = np.column_stack([xv[p - k:T - k] for k in range(1, p + 1)])
    _, _, r0 = mco(Yg, Ly)
    _, _, r1 = mco(Yg, np.column_stack([Ly, Lx]))
    F = ((r0 - r1) / p) / (r1 / (len(Yg) - 2 * p))
    return F, 1 - stats.f.cdf(F, p, len(Yg) - 2 * p)


F1, p1 = granger(y, x)
xi = np.zeros(N)
for t in range(1, N):
    xi[t] = 0.8 * xi[t - 1] + rng.standard_normal()
F2, p2 = granger(y, xi)
print(f"(3) Granger (4 retardos): x impulsa a y: F = {F1:.1f}, p = {p1:.2e}; x independiente: F = {F2:.2f}, p = {p2:.3f}")
prueba(p1 < 1e-10 and p2 > 0.01, "prueba de Granger")

# (4) Regresión espuria
M, n = 500, 200
fr_nivel = fr_dif = 0
for _ in range(M):
    u = np.cumsum(rng.standard_normal(n))
    v = np.cumsum(rng.standard_normal(n))
    bb, ss, _ = mco(v, np.column_stack([np.ones(n), u]))
    fr_nivel += abs(bb[1] / ss[1]) > 2
    du, dv = np.diff(u), np.diff(v)
    bb, ss, _ = mco(dv, np.column_stack([np.ones(n - 1), du]))
    fr_dif += abs(bb[1] / ss[1]) > 2
print(f"(4) dos paseos aleatorios independientes (n = {n}): |t| > 2 en {fr_nivel/M:.2f} de los casos con niveles; "
      f"en {fr_dif/M:.2f} con diferencias (esperado ≈ 0.05)")
prueba(fr_nivel / M > 0.5 and fr_dif / M < 0.10, "regresión espuria")
print("Pruebas superadas.")
