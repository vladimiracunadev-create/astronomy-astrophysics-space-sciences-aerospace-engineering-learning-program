#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C07: ajuste por minimos cuadrados ponderados (Gauss-Newton) de una orbita sintetica.

Todo SINTETICO: orbita kepleriana de dos cuerpos (a = 7200 km, e = 0.01, i = 55 deg) observada durante 20 minutos cada 60 s desde
dos estaciones FIJAS en el marco inercial (simplificacion; sin rotacion terrestre ni visibilidad) con alcance (sigma 10 m) y velocidad
de alcance (sigma 0.01 m/s) -- niveles ILUSTRATIVOS. mu = 3.986004e14 m3/s2 (valor nominal ilustrativo, no consultado).
Modelo: x(t) = propagador kepleriano de variables universales; jacobiano por diferencias centrales (paso 1 m y 1e-3 m/s).
Estimador: x = x0 + (H^T W H)^-1 H^T W r, iterado; covarianza formal P = (H^T W H)^-1.
Segunda via: 100 realizaciones de ruido (semilla 19); la covarianza empirica de los errores debe coincidir con P (cociente de
desviaciones estandar entre 0.85 y 1.15 en cada componente). Tolerancia de convergencia: |dx| < 1e-6 relativa.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

MU = 3.986004e14


def stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def prop(x0, dt):
    r0, v0 = x0[:3], x0[3:]
    r0n = np.linalg.norm(r0); vr0 = np.dot(r0, v0) / r0n
    al = 2 / r0n - np.dot(v0, v0) / MU
    chi = math.sqrt(MU) * abs(al) * dt
    for _ in range(100):
        z = al * chi**2; C, S = stumpff(z)
        F = r0n * vr0 / math.sqrt(MU) * chi**2 * C + (1 - al * r0n) * chi**3 * S + r0n * chi - math.sqrt(MU) * dt
        dF = r0n * vr0 / math.sqrt(MU) * chi * (1 - z * S) + (1 - al * r0n) * chi**2 * C + r0n
        d = F / dF; chi -= d
        if abs(d) < 1e-9: break
    z = al * chi**2; C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C; g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0; rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi; gd = 1 - chi**2 / rn * C
    return np.concatenate([r, fd * r0 + gd * v0])


def estado_inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


EST = np.array([[6.371e6, 0, 0], [0, 4.5e6, 4.5e6]])  # m, SINTETICAS
T = np.arange(0, 1201.0, 60.0)
SIG = np.array([10.0, 0.01])


def h_todo(x0):
    y = []
    for t in T:
        x = prop(x0, t) if t > 0 else x0
        for s in EST:
            d = x[:3] - s; rho = np.linalg.norm(d)
            y += [rho, np.dot(d, x[3:]) / rho]
    return np.array(y)


def jac(x0):
    J = np.zeros((len(T) * len(EST) * 2, 6))
    for k in range(6):
        dx = np.zeros(6); dx[k] = 1.0 if k < 3 else 1e-3
        J[:, k] = (h_todo(x0 + dx) - h_todo(x0 - dx)) / (2 * dx[k])
    return J


def ajusta(y, x_ini, W, it=10):
    x = x_ini.copy(); hist = []
    for _ in range(it):
        r = y - h_todo(x)
        J = jac(x)
        N = J.T @ W @ J
        dx = np.linalg.solve(N, J.T @ W @ r)
        x = x + dx
        hist.append((float(r @ W @ r), float(np.linalg.norm(dx[:3])), float(np.linalg.norm(dx[3:]))))
        if np.linalg.norm(dx[:3]) < 1e-4 and np.linalg.norm(dx[3:]) < 1e-7:
            break
    return x, hist, np.linalg.inv(J.T @ W @ J)


def main():
    rng = np.random.default_rng(19)
    x_true = estado_inicial()
    nobs = len(T) * len(EST) * 2
    sig = np.tile(SIG, len(T) * len(EST))
    W = np.diag(1 / sig**2)
    y_clean = h_todo(x_true)
    y = y_clean + rng.normal(0, sig)
    x0 = x_true + np.array([5000.0, -4000, 3000, 5, -4, 3])
    x_hat, hist, P = ajusta(y, x0, W)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita y observaciones SINTETICAS, semilla 19)",
           f"Observaciones: {nobs} (alcance y velocidad de alcance, 2 estaciones, {len(T)} instantes); incognitas: 6",
           f"Error inicial: {np.linalg.norm(x0[:3]-x_true[:3]):.1f} m, {np.linalg.norm(x0[3:]-x_true[3:]):.2f} m/s",
           "iter   chi2        |dr| [m]    |dv| [m/s]"]
    for i, (c, dr, dv) in enumerate(hist, 1):
        out.append(f"{i:3d}  {c:10.2f}  {dr:11.4f}  {dv:11.6f}")
    err = x_hat - x_true
    sP = np.sqrt(np.diag(P))
    r_fin = y - h_todo(x_hat)
    chi2 = float(r_fin @ W @ r_fin)
    out.append(f"Error final: posicion {np.linalg.norm(err[:3]):.3f} m, velocidad {np.linalg.norm(err[3:]):.5f} m/s")
    out.append(f"sigma formal (x,y,z) [m] = {sP[0]:.3f} {sP[1]:.3f} {sP[2]:.3f} ; (vx,vy,vz) [m/s] = {sP[3]:.5f} {sP[4]:.5f} {sP[5]:.5f}")
    out.append(f"chi2 final = {chi2:.2f} para {nobs-6} grados de libertad (cociente {chi2/(nobs-6):.3f})")
    # Monte Carlo
    errs = []
    for _ in range(100):
        yy = y_clean + rng.normal(0, sig)
        xx, _, _ = ajusta(yy, x_true + np.array([200.0, -150, 100, 0.2, -0.2, 0.1]), W, it=3)
        errs.append(xx - x_true)
    errs = np.array(errs)
    emp = errs.std(axis=0, ddof=1)
    raz = emp / sP
    out.append("Cociente sigma empirica / sigma formal (100 realizaciones): " + " ".join(f"{v:.3f}" for v in raz))
    ok = np.all((raz > 0.85) & (raz < 1.15)) and hist[-1][1] < 1e-3
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res = dict(nobs=nobs, iters=len(hist), err_pos=float(np.linalg.norm(err[:3])), err_vel=float(np.linalg.norm(err[3:])),
               sx=float(sP[0]), sy=float(sP[1]), sz=float(sP[2]), svx=float(sP[3]), svy=float(sP[4]), svz=float(sP[5]),
               chi2=chi2, chi2n=chi2 / (nobs - 6), rmin=float(raz.min()), rmax=float(raz.max()), dof=nobs - 6,
               e0p=float(np.linalg.norm(x0[:3] - x_true[:3])), e0v=float(np.linalg.norm(x0[3:] - x_true[3:])))
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
