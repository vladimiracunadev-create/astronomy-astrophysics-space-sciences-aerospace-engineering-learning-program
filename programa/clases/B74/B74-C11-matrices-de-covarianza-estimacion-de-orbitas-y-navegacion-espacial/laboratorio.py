#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C11: interpretacion de una matriz de covarianza de posicion.

Todo SINTETICO: covarianza de posicion de un satelite sintetico en el marco RTN (radial, transversal, normal): sigma_R = 50 m,
sigma_T = 500 m, sigma_N = 100 m, correlacion R-T = -0.9 (ILUSTRATIVOS). Estado sintetico: r = (7000, 0, 0) km, v = (0, 7.5, 0.5) km/s en
un marco inercial. Operaciones: rotacion RTN -> inercial (P_I = Q P Q^T), autovalores (semiejes), traza, determinante, elipsoide de
confianza (el contenido del elipsoide k^2 de una gaussiana de 3 gl es F(k^2) = erf(sqrt(k^2/2)) - sqrt(2 k^2/pi) exp(-k^2/2)),
correlaciones, varianza condicional y comprobacion por Monte Carlo (200 000 muestras, semilla 37).
Tolerancias: autovalores, traza y determinante invariantes a la rotacion (1e-9 relativa); fraccion Monte Carlo dentro del elipsoide al 95 %
entre 0.948 y 0.952.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np


def F3(x):
    return math.erf(math.sqrt(x / 2)) - math.sqrt(2 * x / math.pi) * math.exp(-x / 2)


def k2_para(p):
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if F3(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    rng = np.random.default_rng(37)
    sR, sT, sN, rho = 50.0, 500.0, 100.0, -0.9
    P = np.array([[sR**2, rho * sR * sT, 0], [rho * sR * sT, sT**2, 0], [0, 0, sN**2]])
    r = np.array([7000e3, 0, 0]); v = np.array([0, 7.5e3, 0.5e3])
    R_ = r / np.linalg.norm(r); N_ = np.cross(r, v); N_ /= np.linalg.norm(N_); T_ = np.cross(N_, R_)
    Q = np.column_stack([R_, T_, N_])  # columnas: ejes RTN expresados en el marco inercial
    PI = Q @ P @ Q.T
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (covarianza SINTETICA, semilla 37)"]
    res = {}
    w, V = np.linalg.eigh(P)
    wI, VI = np.linalg.eigh(PI)
    inv_ok = np.allclose(w, wI, rtol=1e-9) and abs(np.trace(P) - np.trace(PI)) < 1e-6 * np.trace(P) and abs(np.linalg.det(P) / np.linalg.det(PI) - 1) < 1e-9
    out.append("P en RTN [m^2]:")
    for f in P: out.append("  " + " ".join(f"{x:12.1f}" for x in f))
    out.append("P en el marco inercial [m^2]:")
    for f in PI: out.append("  " + " ".join(f"{x:12.1f}" for x in f))
    out.append(f"Autovalores: {w[0]:.2f} {w[1]:.2f} {w[2]:.2f} ; semiejes 1-sigma = {math.sqrt(w[0]):.2f} {math.sqrt(w[1]):.2f} {math.sqrt(w[2]):.2f} m")
    out.append(f"Traza RTN = {np.trace(P):.1f} ; traza inercial = {np.trace(PI):.1f} ; det RTN = {np.linalg.det(P):.4e} ; det inercial = {np.linalg.det(PI):.4e}")
    res.update(l1=float(w[0]), l2=float(w[1]), l3=float(w[2]), s1=math.sqrt(w[0]), s2=math.sqrt(w[1]), s3=math.sqrt(w[2]), tr=float(np.trace(P)))
    # correlaciones
    d = np.sqrt(np.diag(PI)); C = PI / np.outer(d, d)
    out.append("Correlaciones en el marco inercial (x-y, x-z, y-z): " + " ".join(f"{C[i,j]:+.3f}" for i, j in ((0, 1), (0, 2), (1, 2))))
    out.append(f"sigma inercial por eje = {d[0]:.1f} {d[1]:.1f} {d[2]:.1f} m (los ejes no coinciden con los del elipsoide)")
    res.update(dx=float(d[0]), dy=float(d[1]), dz=float(d[2]), cxy=float(C[0, 1]))
    # condicional
    cond = sT**2 * (1 - rho**2)
    out.append(f"sigma_T marginal = {sT:.1f} m ; sigma_T condicionada a conocer R = {math.sqrt(cond):.2f} m")
    res.update(sTc=math.sqrt(cond))
    # elipsoides
    k95 = k2_para(0.95); k68 = k2_para(0.6827)
    out.append(f"k^2 para contenido 95 % (3 gl) = {k95:.4f} ; k^2 para 68.27 % = {k68:.4f} ; 1-sigma 1D contiene solo el 19.87 % en 3D (F(1) = {F3(1.0):.4f})")
    res.update(k95=k95, k68=k68, f1=F3(1.0))
    X = rng.multivariate_normal(np.zeros(3), P, 200000)
    m2 = np.einsum("ij,jk,ik->i", X, np.linalg.inv(P), X)
    frac = float(np.mean(m2 < k95))
    out.append(f"Fraccion Monte Carlo dentro del elipsoide k^2 = {k95:.3f}: {frac:.4f} (esperado 0.9500)")
    sx = np.sqrt(w[2]) * np.sqrt(k95)
    out.append(f"Semieje mayor del elipsoide al 95 % = {sx:.1f} m (sigma mayor {math.sqrt(w[2]):.1f} m x {math.sqrt(k95):.3f})")
    res.update(frac=frac, sx95=float(sx))
    ok = inv_ok and 0.948 < frac < 0.952
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
