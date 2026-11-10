#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C15: retraso de una maniobra de correccion fallida, delta-v de recuperacion y ventana admisible.

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y UA = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Arco heliocentrico SINTETICO (ILUSTRATIVO) plano: r0 = 1 UA, v0 = (3, 31) km/s (el de B81-C02, arco no asociado a una mision), llegada a T = 250 d.
Error de inyeccion SINTETICO: dispersion de posicion (500 km, -300 km) y de velocidad (0,5; 0,3) m/s al inicio del arco, propagada de forma lineal con la matriz de transicion.
Una correccion en el instante t anula el error de posicion en T: dv(t) = -Phi_rv(T,t)^-1 [Phi_rr(T,t) dr(t) + Phi_rv(T,t) dv_err(t)] (dos componentes en el plano).
Phi se obtiene por las ecuaciones variacionales (B81-C01). Presupuesto de recuperacion ILUSTRATIVO: 3 m/s.
Ventana: ultimo instante tal que |dv(t)| <= presupuesto. Si la maniobra planeada en t = 10 d falla, se reintenta en t > 10 d.
Segunda via: se aplica dv(t) al estado perturbado propagado de forma no lineal y se mide el error de posicion a T.
Tolerancias: residual no lineal en T menor que 1 % del error sin corregir; dv(t) monotono creciente tras 50 d.
"""
from __future__ import annotations
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp

GM = 132712440041.279419
AU = 149597870.7
DIA = 86400.0


def rhs(t, y):
    r = y[:2]
    rn = np.linalg.norm(r)
    G = GM * (3.0 * np.outer(r, r) / rn**5 - np.eye(2) / rn**3)
    A = np.zeros((4, 4)); A[:2, 2:] = np.eye(2); A[2:, :2] = G
    return np.concatenate([y[2:4], -GM * r / rn**3, (A @ y[4:].reshape(4, 4)).ravel()])


def rhs_s(t, y):
    r = y[:2]
    return np.concatenate([y[2:], -GM * r / np.linalg.norm(r)**3])


def tramo(x0, t0, t1):
    s = solve_ivp(rhs, (t0, t1), np.concatenate([x0, np.eye(4).ravel()]), method="DOP853", rtol=1e-12, atol=1e-9)
    y = s.y[:, -1]
    return y[:4], y[4:].reshape(4, 4)


def estado(x0, t0, t1):
    return solve_ivp(rhs_s, (t0, t1), x0, method="DOP853", rtol=1e-12, atol=1e-9).y[:, -1]


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    x0 = np.array([AU, 0.0, 3.0, 31.0])
    T = 250 * DIA
    err0 = np.array([500.0, -300.0, 5e-4, 3e-4])
    xT, PhiT0 = tramo(x0, 0.0, T)
    print(f"Arco SINTETICO de {T/DIA:.0f} d ; error de inyeccion ILUSTRATIVO: 500 km, -300 km, 0,5 m/s, 0,3 m/s ; error de posicion final sin corregir = {np.linalg.norm((PhiT0@err0)[:2]):.1f} km")
    presupuesto = 3.0
    print("  t [d]   tiempo restante [d]   |dv| necesario [m/s]   residuo no lineal [km]")
    ts = [5, 10, 20, 40, 80, 120, 160, 200, 230, 245]
    dvs = {}
    resid = []
    for td in ts:
        t = td * DIA
        xt, P1 = tramo(x0, 0.0, t)
        _, P2 = tramo(xt, t, T)
        d_t = P1 @ err0   # dispersion en t (lineal)
        # con el modelo lineal: el error en T es P2 d_t; la correccion cambia la velocidad en t
        dv = -np.linalg.solve(P2[:2, 2:], P2[:2, :] @ d_t)
        dvs[td] = np.linalg.norm(dv)
        # no lineal: estado real = nominal + d_t, con dv aplicado en t
        xr = xt + d_t
        xr = xr + np.array([0.0, 0.0, dv[0], dv[1]])
        res = np.linalg.norm(estado(xr, t, T)[:2] - xT[:2])
        resid.append(res)
        print(f"{td:7d} {250-td:14d}          {dvs[td]*1e3:14.4f}          {res:10.4f}")
    # ventana
    fino = []
    for td in range(5, 249, 4):
        t = td * DIA
        xt, P1 = tramo(x0, 0.0, t)
        _, P2 = tramo(xt, t, T)
        d_t = P1 @ err0
        dv = -np.linalg.solve(P2[:2, 2:], P2[:2, :] @ d_t)
        fino.append((td, np.linalg.norm(dv) * 1e3))
    ult = max([td for td, d in fino if d <= presupuesto] or [0])
    print(f"Presupuesto de recuperacion ILUSTRATIVO = {presupuesto:.1f} m/s -> ultimo reintento admisible (malla de 4 d): t = {ult} d")
    print(f"Cociente |dv|(245 d)/|dv|(10 d) = {dvs[245]/dvs[10]:.1f} (la palanca Phi_rv se debilita al acercarse la llegada)")
    assert all(dvs[a] < dvs[b] for a, b in ((80, 120), (120, 160), (160, 200), (200, 230), (230, 245)))
    ref = np.linalg.norm((PhiT0 @ err0)[:2])
    assert all(r < 0.01 * ref for r in resid)
    print(f"Prueba: todos los residuos no lineales son menores que 1 % de {ref:.1f} km")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
