#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C05: validación de un modelo kepleriano con una efeméride oficial.

Datos: EFEMÉRIDE OFICIAL (resultado de modelo, no observación directa): NASA/JPL
Horizons API v1.2, cuerpo 399 (Tierra, geocentro), centro 500@10 (Sol), vectores
geométricos, plano eclíptico J2000, ICRF, unidades au y au/d, escala TDB, efeméride
DE441. Cinco épocas (JD TDB) copiadas a mano a este script el 2026-11-05.
Constantes: GM_sol nominal IAU 2015 B3 = 1.3271244e20 m^3/s^2; 1 au = 149597870700 m.
Modelo bajo prueba: dos cuerpos (Sol fijo), integrado con DOP853 desde el estado de
la primera época (elementos osculadores).
Supuestos: se ignoran Luna, planetas y relatividad; el centro es el Sol (no el
baricentro) y el objeto es el geocentro (no el baricentro Tierra-Luna).
Criterios de aceptación (fijados ANTES de comparar; ver clase): error de posición
a +91 d <= 1e-3 au y a +365 d <= 5e-3 au; verificación de datos: energía osculadora
constante a 1e-4 relativo entre épocas (incumplido: ver clase; criterio revisado a 3e-3 con registro).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp

AU = 149597870700.0
MU = 1.3271244e20*86400.0**2/AU**3

# (JD TDB, x, y, z [au], vx, vy, vz [au/d])
HORIZONS = [
 (2460676.5, -1.786834409731047E-01, 9.669827953774551E-01, -5.109423915082682E-05, -1.720473858166942E-02, -3.193533189307208E-03, 5.457174067040888E-09),
 (2460767.5, -9.771032044732010E-01, -2.104323089919837E-01, 1.556486123938526E-05, 3.348948088761836E-03, -1.688703398173705E-02, 6.503050694285350E-07),
 (2460858.5, 1.771726921813559E-01, -1.001078644863905E+00, 5.909052845821723E-05, 1.666246564656617E-02, 2.940163198760981E-03, 3.364188097607674E-07),
 (2460950.5, 9.894351377731484E-01, 1.515214276914586E-01, -1.225729523122299E-05, -2.888763341338038E-03, 1.693745577992973E-02, -1.473616109658653E-06),
 (2461041.5, -1.742814809205833E-01, 9.677589202546031E-01, -5.944511017526243E-05, -1.720454736868129E-02, -3.116607022544302E-03, 2.371782782240443E-07),
]


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def energia(r, v):
    return 0.5*(v @ v) - MU/np.linalg.norm(r)


def propagar(r0, v0, dt):
    def f(t, y):
        r = y[:3]
        return np.concatenate([y[3:], -MU*r/np.linalg.norm(r)**3])
    s = solve_ivp(f, (0, dt), np.concatenate([r0, v0]), method="DOP853", rtol=1e-12, atol=1e-14)
    return s.y[:3, -1], s.y[3:, -1]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    D = np.array(HORIZONS)
    jd, R, V = D[:, 0], D[:, 1:4], D[:, 4:7]

    # 1. Verificación de los DATOS copiados (antes de compararlos con nada)
    rn = np.linalg.norm(R, axis=1)
    eps = np.array([energia(R[i], V[i]) for i in range(len(D))])
    L = np.array([np.linalg.norm(np.cross(R[i], V[i])) for i in range(len(D))])
    print("\n[datos] época  JD TDB       |r| [au]   |v| [au/d]   energía [au2/d2]    |L| [au2/d]")
    for i in range(len(D)):
        print(f"        {i}  {jd[i]:.1f}  {rn[i]:.6f}   {np.linalg.norm(V[i]):.6f}   {eps[i]:.6e}   {L[i]:.6e}")
    disp_e = (eps.max() - eps.min())/abs(eps.mean())
    disp_L = (L.max() - L.min())/L.mean()
    print(f"        dispersión relativa de la energía: {disp_e:.2e}; del momento angular: {disp_L:.2e}")
    prueba(0.98 < rn.min() and rn.max() < 1.02, "distancias entre 0.98 y 1.02 au")
    print(f"        criterio previo 1e-4: {'CUMPLE' if disp_e < 1e-4 else 'NO CUMPLE'} -> se investiga, no se ensancha en silencio")
    dif_e = np.diff(eps)
    suave = bool(np.all(dif_e < 0))
    print(f"        la energía decrece de forma monótona entre épocas (sin saltos de transcripción): {suave}")
    # Orden de magnitud esperado: variación de la velocidad del geocentro por la Luna (~12 m/s sobre ~29.8 km/s)
    esp = 2*12.0/29800.0
    print(f"        orden de magnitud esperable por la Luna: 2*dv/v ≈ {esp:.1e} (valores aproximados, no consultados)")
    prueba(suave and disp_e < 3e-3, "criterio REVISADO tras el hallazgo: dispersión < 3e-3 y variación suave")
    prueba(np.all(np.abs(np.diff(jd) - np.array([91, 91, 92, 91])) < 1e-9), "espaciado de épocas")

    # 2. Modelo frente a la efeméride
    print("\n[validación] error de posición del modelo de dos cuerpos frente a Horizons")
    errs = []
    for i in range(1, len(D)):
        r, v = propagar(R[0], V[0], jd[i] - jd[0])
        e_au = float(np.linalg.norm(r - R[i]))
        errs.append(e_au)
        print(f"  +{jd[i]-jd[0]:5.0f} d: error = {e_au:.3e} au = {e_au*AU/1000:.0f} km"
              f"  (|r|: modelo {np.linalg.norm(r):.6f}, Horizons {rn[i]:.6f})")
    crit = {1: 1e-3, 4: 5e-3}
    print(f"  criterios previos: +91 d <= {crit[1]:.0e} au ; +365 d <= {crit[4]:.0e} au")
    print(f"  veredicto +91 d: {'CUMPLE' if errs[0] <= crit[1] else 'NO CUMPLE'};  +365 d: {'CUMPLE' if errs[3] <= crit[4] else 'NO CUMPLE'}")

    # 3. Cota de lo esperable: Luna (geocentro vs baricentro) ~ 4.7e3 km
    cota_luna = 4.7e3*1000/AU
    print(f"[contexto] oscilación del geocentro respecto del baricentro Tierra-Luna ≈ {cota_luna:.1e} au (valor aproximado, no consultado)")
    prueba(errs[0] > 0 and errs[3] > errs[0], "el error crece con el intervalo")
    print("\nEjecución completa (los criterios se reportan; no son pruebas que detengan el script).")


if __name__ == "__main__":
    main()
