#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C13: navegacion optica por triangulacion de lineas de vision a cuerpos de posicion conocida.

Todo SINTETICO: nave en r = (0, 0, 0) del marco de referencia local; tres cuerpos de referencia ('balizas') SINTETICOS a distancias de
1.0e8, 1.5e8 y 2.0e8 km. Cada imagen da la direccion unitaria a una baliza con incertidumbre angular sigma (ILUSTRATIVA,
0.0003 grados = 1.1 arcsec). Estimador: el punto que minimiza la suma de distancias perpendiculares ponderadas a las lineas de vision (minimos
cuadrados lineales): A = sum (I - u u^T)/(rho^2 sigma^2) con la covarianza P = A^-1. Se compara con 3000 realizaciones de Monte Carlo (semilla 43)
con una geometria amplia (balizas separadas 90 grados o mas) y una estrecha (balizas dentro de 15 grados). Tolerancia: la sigma empirica de cada componente de la
posicion dentro del 8 % de la prevista por P.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

SIG = math.radians(0.0003)  # rad


def unit(az, el):
    az, el = math.radians(az), math.radians(el)
    return np.array([math.cos(el) * math.cos(az), math.cos(el) * math.sin(az), math.sin(el)])


def solve(pos_b, dirs, rho_est):
    A = np.zeros((3, 3)); b = np.zeros(3)
    for p, u, rho in zip(pos_b, dirs, rho_est):
        M = (np.eye(3) - np.outer(u, u)) / (rho * SIG) ** 2
        A += M; b += M @ (p - rho * u)  # el punto de la linea mas cercano a x tiene la forma p - s u
    return np.linalg.solve(A, b), np.linalg.inv(A)


def caso(rng, nombre, angs, rhos, n=3000):
    pos_b = [rho * unit(a, e) for (a, e), rho in zip(angs, rhos)]
    est = []
    for _ in range(n):
        dirs = []
        for p in pos_b:
            u = p / np.linalg.norm(p)
            # perturbacion transversal aleatoria de sigma por eje transversal
            t1 = np.cross(u, [0, 0, 1.0]); t1 /= np.linalg.norm(t1); t2 = np.cross(u, t1)
            d = u + SIG * (rng.normal() * t1 + rng.normal() * t2)
            dirs.append(d / np.linalg.norm(d))
        x, _ = solve(pos_b, dirs, [np.linalg.norm(p) for p in pos_b])
        est.append(x)
    est = np.array(est)
    _, P = solve(pos_b, [p / np.linalg.norm(p) for p in pos_b], [np.linalg.norm(p) for p in pos_b])
    se = est.std(axis=0, ddof=1)
    sp = np.sqrt(np.diag(P))
    return se, sp, P


def main():
    rng = np.random.default_rng(43)
    rhos = [1.0e11, 1.5e11, 2.0e11]  # m
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (geometria y direcciones SINTETICAS, semilla 43)",
           f"sigma angular por imagen = {math.degrees(SIG):.4f} deg = {SIG*206264.806:.3f} arcsec ; distancias a las balizas = 1.0, 1.5 y 2.0e8 km"]
    res = {}
    casos = {"amplia": [(0, 0), (90, 0), (210, 30)], "estrecha": [(0, 0), (10, 2), (15, -2)]}
    ok = True
    out.append("geometria   sigma prevista (x,y,z) [km]        sigma empirica (x,y,z) [km]      sigma 3D prevista [km]")
    for nom, angs in casos.items():
        se, sp, P = caso(rng, nom, angs, rhos)
        out.append(f"{nom:9s}   {sp[0]/1e3:8.1f} {sp[1]/1e3:8.1f} {sp[2]/1e3:8.1f}     {se[0]/1e3:8.1f} {se[1]/1e3:8.1f} {se[2]/1e3:8.1f}     {math.sqrt(np.trace(P))/1e3:9.1f}")
        res[f"p3_{nom}"] = math.sqrt(np.trace(P)) / 1e3
        res[f"pmax_{nom}"] = float(sp.max() / 1e3)
        res[f"e_{nom}"] = float(math.sqrt((se**2).sum()) / 1e3)
        ok &= bool(np.all(np.abs(se / sp - 1) < 0.08))
    out.append(f"Cociente 3D estrecha/amplia = {res['p3_estrecha']/res['p3_amplia']:.2f}")
    res["cociente"] = res["p3_estrecha"] / res["p3_amplia"]
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
