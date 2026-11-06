#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C01: características con sentido físico y unidades.

Datos: SINTÉTICOS (candidatos a tránsito generados aquí con semilla fija).
Constantes: G = 6,67430e-11 m^3 kg^-1 s^-2 (CODATA 2022, NIST); densidad media
del Sol 1408 kg/m^3 y radio 695 700 km (NASA NSSDC Sun Fact Sheet);
1 au = 149 597 870 700 m (exacto, B01-C08).
Modelo: tránsito central de un planeta pequeño en órbita circular:
  a/R* = (G rho P^2 / (3 pi))^(1/3),   T0 = P / (pi * a/R*).
Supuestos: órbita circular, parámetro de impacto 0, Rp << R*, masa del planeta
despreciable. Validez: planetas pequeños con P entre 1 y 400 d.
Tolerancia: 0,3 % frente a au/R_sol (limitada por la densidad con 4 cifras).
"""
import platform
import sys

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

G = 6.67430e-11
RHO_SOL = 1408.0
R_SOL = 6.957e8  # m (radio nominal del Sol; 695 700 km)
AU = 149_597_870_700.0
DIA = 86400.0


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def a_sobre_rstar(P_dias, rho):
    """a/R* (adimensional) a partir de P (d) y de la densidad estelar rho (kg/m^3)."""
    P = np.asarray(P_dias) * DIA
    return (G * rho * P**2 / (3.0 * np.pi)) ** (1.0 / 3.0)


def duracion_central_dias(P_dias, rho):
    """Duración T0 (d) de un tránsito central, Rp << R*."""
    return np.asarray(P_dias) / (np.pi * a_sobre_rstar(P_dias, rho))


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())

# --- Prueba 1: Tierra-Sol contra un valor independiente (au / R_sol) ---
ref = AU / R_SOL
calc = float(a_sobre_rstar(365.25, RHO_SOL))
print(f"a/R* Tierra-Sol: calculado {calc:.2f}; referencia au/R_sol {ref:.2f}; "
      f"diferencia {100*(calc-ref)/ref:+.3f} %")
prueba(abs(calc - ref) / ref < 0.003, "a/R* de la Tierra")

# --- Prueba 2: ida y vuelta (la característica se puede invertir) ---
rho_rec = (3 * np.pi / (G * (365.25 * DIA) ** 2)) * calc**3
prueba(abs(rho_rec - RHO_SOL) / RHO_SOL < 1e-12, "inversión de la densidad")
print(f"densidad recuperada: {rho_rec:.1f} kg/m^3")

# --- Conjunto sintético: planetas (duración compatible con rho) y falsos positivos ---
rng = np.random.default_rng(17)
n = 600
P = 10 ** rng.uniform(0, np.log10(300), 2 * n)          # d
rho = RHO_SOL * 10 ** rng.normal(0, 0.12, 2 * n)         # estrellas: ±~30 %
T0 = duracion_central_dias(P, rho)
y = np.r_[np.zeros(n), np.ones(n)].astype(int)           # 1 = falso positivo
T_obs = T0 * np.where(y == 1, 10 ** rng.normal(0, 0.35, 2 * n), 10 ** rng.normal(0, 0.03, 2 * n))
profundidad_pct = 10 ** rng.uniform(-2, 0, 2 * n)        # % (sin información de clase)
razon = T_obs / duracion_central_dias(P, RHO_SOL)        # adimensional, con rho nominal
print(f"razón T_obs/T0: planetas mediana {np.median(razon[y==0]):.3f}, "
      f"falsos positivos mediana {np.median(razon[y==1]):.3f}")

cv = StratifiedKFold(5, shuffle=True, random_state=0)
clf = lambda: KNeighborsClassifier(15)                   # noqa: E731


def acc(X, escalar):
    m = make_pipeline(StandardScaler(), clf()) if escalar else clf()
    return cross_val_score(m, X, y, cv=cv).mean()


X_d = np.c_[P, T_obs, profundidad_pct]                   # P (d), T (d), profundidad (%)
X_s = np.c_[P, T_obs * DIA, profundidad_pct]             # igual, pero T en segundos
a_d, a_s = acc(X_d, False), acc(X_s, False)
b_d, b_s = acc(X_d, True), acc(X_s, True)
print(f"k-NN sin escalar: días {a_d:.3f} | segundos {a_s:.3f}")
print(f"k-NN estandarizado: días {b_d:.3f} | segundos {b_s:.3f}")
prueba(abs(b_d - b_s) < 1e-12, "la estandarización debe borrar el cambio de unidad")
prueba(abs(a_d - a_s) > 0.01, "sin escalar, la unidad debería importar")

X_f = np.c_[np.log10(razon), np.log10(P)]                # característica física
c_f = acc(X_f, True)
print(f"k-NN con log10(razón de duración) y log10(P): {c_f:.3f}")
prueba(c_f > max(b_d, b_s), "la característica física debe superar a las crudas")
print("Pruebas superadas.")
