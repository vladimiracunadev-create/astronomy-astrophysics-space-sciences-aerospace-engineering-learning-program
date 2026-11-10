#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C01: modelo de observacion (alcance, azimut, elevacion) y su jacobiano.

Datos SINTETICOS (no observados): posicion de un satelite en un marco inercial simplificado y una estacion fija
en el mismo marco (sin rotacion terrestre). Unidades: m, rad, grados en la salida. Sistema de referencia: ENU local
de la estacion (Este, Norte, Cenit) obtenido del vector relativo inercial con una rotacion fija.
Modelo: y = h(r) = [rho, az, el]; jacobiano analitico frente a diferencias centrales (paso 1 m).
Version: Python 3.12.9, NumPy 2.4.4, semilla 7. Tolerancias: jacobiano analitico/numerico 1e-6 relativa;
residuos normalizados con media cercana a 0 (no se exige un valor).
"""
from __future__ import annotations
import json, platform, sys
import numpy as np

RE = 6378137.0  # m, radio ecuatorial usado solo para situar la estacion (valor ilustrativo del elipsoide WGS-84)
LAT, LON = np.radians(-33.0), np.radians(-70.0)  # estacion SINTETICA
EST = RE * np.array([np.cos(LAT) * np.cos(LON), np.cos(LAT) * np.sin(LON), np.sin(LAT)])
E = np.array([-np.sin(LON), np.cos(LON), 0.0])
N = np.array([-np.sin(LAT) * np.cos(LON), -np.sin(LAT) * np.sin(LON), np.cos(LAT)])
U = np.array([np.cos(LAT) * np.cos(LON), np.cos(LAT) * np.sin(LON), np.sin(LAT)])
R_ENU = np.vstack([E, N, U])


def h(r):
    """Observacion [rho (m), azimut (rad), elevacion (rad)] desde la estacion."""
    d = R_ENU @ (r - EST)
    rho = np.linalg.norm(d)
    return np.array([rho, np.arctan2(d[0], d[1]), np.arcsin(d[2] / rho)])


def jac_analitico(r):
    d = R_ENU @ (r - EST)
    rho = np.linalg.norm(d)
    rho_h = np.hypot(d[0], d[1])
    dh_dd = np.array([
        d / rho,
        [d[1] / rho_h**2, -d[0] / rho_h**2, 0.0],
        [-d[0] * d[2] / (rho**2 * rho_h), -d[1] * d[2] / (rho**2 * rho_h), rho_h / rho**2],
    ])
    return dh_dd @ R_ENU


def jac_numerico(r, paso=1.0):
    J = np.zeros((3, 3))
    for k in range(3):
        dr = np.zeros(3); dr[k] = paso
        J[:, k] = (h(r + dr) - h(r - dr)) / (2 * paso)
    return J


def main():
    rng = np.random.default_rng(7)
    # satelite SINTETICO a ~700 km de altitud, cerca del cenit de la estacion
    r_sat = EST + (RE * 0 + 700e3 + 300e3) * U + 450e3 * E + 200e3 * N
    y = h(r_sat)
    Ja, Jn = jac_analitico(r_sat), jac_numerico(r_sat)
    dif = float(np.max(np.abs(Ja - Jn) / (np.abs(Ja) + 1e-12)))
    sig = np.array([5.0, np.radians(0.01), np.radians(0.01)])  # m, rad, rad (ILUSTRATIVO)
    y_obs = y + rng.normal(0, sig)
    res = y_obs - y
    z = res / sig
    # error de posicion que corresponde a 0.01 grados a la distancia del satelite
    err_ang_m = y[0] * np.radians(0.01)
    # propagacion: covarianza de la medida a partir de una covarianza de posicion diagonal de (100 m)^2
    Pr = np.eye(3) * 100.0**2
    Py = Ja @ Pr @ Ja.T
    out = []
    out.append(f"Python {platform.python_version()}, NumPy {np.__version__} (datos SINTETICOS, semilla 7)")
    out.append(f"Estacion sintetica: lat {np.degrees(LAT):.1f} deg, lon {np.degrees(LON):.1f} deg; marco inercial simplificado")
    out.append(f"h(r): rho = {y[0]/1e3:.3f} km, az = {np.degrees(y[1]):.3f} deg, el = {np.degrees(y[2]):.3f} deg")
    out.append("Jacobiano analitico [filas rho, az, el; columnas x, y, z] (1/m, rad/m):")
    for fila in Ja:
        out.append("  " + " ".join(f"{v:+.4e}" for v in fila))
    out.append(f"Diferencia relativa maxima analitico/numerico = {dif:.2e}")
    out.append(f"Residuos normalizados z = {z[0]:+.3f} {z[1]:+.3f} {z[2]:+.3f}")
    out.append(f"0.01 deg a {y[0]/1e3:.1f} km equivalen a {err_ang_m:.1f} m transversales")
    out.append(f"Con sigma_r = 100 m por eje: sigma_rho = {np.sqrt(Py[0,0]):.2f} m, sigma_az = {np.degrees(np.sqrt(Py[1,1])):.5f} deg, sigma_el = {np.degrees(np.sqrt(Py[2,2])):.5f} deg")
    ok = dif < 1e-6
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res_d = dict(rho_km=y[0] / 1e3, az=float(np.degrees(y[1])), el=float(np.degrees(y[2])), dif=dif,
                 err_ang=float(err_ang_m), srho=float(np.sqrt(Py[0, 0])), saz=float(np.degrees(np.sqrt(Py[1, 1]))),
                 sel=float(np.degrees(np.sqrt(Py[2, 2]))), z0=float(z[0]), jr0=float(Ja[0, 0]), jr1=float(Ja[0, 1]), jr2=float(Ja[0, 2]))
    return out, res_d


if __name__ == "__main__":
    out, d = main()
    print(json.dumps(d) if "--json" in sys.argv else "\n".join(out))
