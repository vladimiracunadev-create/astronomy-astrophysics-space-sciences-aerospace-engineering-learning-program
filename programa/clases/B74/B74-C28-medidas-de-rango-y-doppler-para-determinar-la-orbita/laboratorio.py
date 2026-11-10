#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C28: informacion de alcance y de velocidad de alcance (Doppler) para determinar una orbita.

Todo SINTETICO: misma orbita kepleriana (a = 7200 km, e = 0.01, i = 55 deg; mu = 3.986004e14 m3/s2, valor nominal ilustrativo, no consultado) y las mismas estaciones fijas en el marco inercial
que en las clases C07 y C09 (simplificacion). Observaciones cada 60 s durante 20 min (21 instantes) con sigma de alcance 10 m y de velocidad de alcance 0.01 m/s (ILUSTRATIVOS).
Se compara la covarianza formal P = (J^T W J)^-1 del estado inicial (J por diferencias centrales del propagador) para cuatro configuraciones: ambos observables con 1 estacion, alcance solo con 2 estaciones, Doppler solo
con 2 estaciones y ambos con 2 estaciones. Se reportan sigma de posicion (radial, transversal, normal en el instante inicial), sigma de velocidad, el numero de condicion y el rango numerico de la matriz de
informacion normalizada (si el rango es menor que 6 el estado no es observable con esa configuracion y no se da covarianza). Segunda via: 200 realizaciones de ruido con ajuste de Gauss-Newton para la configuracion 'ambos, 2 estaciones' (semilla 101): la dispersion empirica debe coincidir con la formal dentro del 20 %.
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


def inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


EST = np.array([[6.371e6, 0, 0], [0, 4.5e6, 4.5e6]])
T = np.arange(0, 1201.0, 60.0)
SR, SD = 10.0, 0.01


def estados(x0):
    return [prop(x0, t) if t > 0 else x0 for t in T]


def obs(x0, est, usa_r, usa_d):
    y = []
    for x in estados(x0):
        for s in est:
            d = x[:3] - s; rho = np.linalg.norm(d)
            if usa_r: y.append(rho)
            if usa_d: y.append(np.dot(d, x[3:]) / rho)
    return np.array(y)


def sigmas(est, usa_r, usa_d):
    sig = np.tile(([SR] if usa_r else []) + ([SD] if usa_d else []), len(T) * len(est))
    return sig


def jac(x0, est, usa_r, usa_d):
    n = len(obs(x0, est, usa_r, usa_d))
    J = np.zeros((n, 6))
    for k in range(6):
        dx = np.zeros(6); dx[k] = 1.0 if k < 3 else 1e-3
        J[:, k] = (obs(x0 + dx, est, usa_r, usa_d) - obs(x0 - dx, est, usa_r, usa_d)) / (2 * dx[k])
    return J


def rtn(x0):
    r = x0[:3] / np.linalg.norm(x0[:3]); n = np.cross(x0[:3], x0[3:]); n /= np.linalg.norm(n); t = np.cross(n, r)
    return np.vstack([r, t, n])


def main():
    x0 = inicial()
    Q3 = rtn(x0)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita y estaciones SINTETICAS)",
           "configuracion                sigma pos R,T,N [m]            sigma vel R,T,N [m/s]              cond(info)"]
    res = {}
    cfg = (("a1", "alcance+Doppler, 1 est.", EST[:1], True, True), ("r2", "alcance, 2 estaciones", EST, True, False),
           ("d2", "Doppler, 2 estaciones", EST, False, True), ("b2", "alcance+Doppler, 2 est.", EST, True, True))
    for k, nom, est, ur, ud in cfg:
        J = jac(x0, est, ur, ud)
        W = np.diag(1 / sigmas(est, ur, ud) ** 2)
        A = J.T @ W @ J
        # normalizar por escalas para el numero de condicion
        D = np.diag(1 / np.sqrt(np.diag(A)))
        cond = np.linalg.cond(D @ A @ D)
        ev = np.linalg.eigvalsh(D @ A @ D)
        rango = int(np.sum(ev > 1e-9 * ev.max()))
        res[f"{k}_rango"] = rango
        res[f"{k}_c"] = float(cond)
        if rango < 6:
            out.append(f"{nom:26s} no observable: rango {rango} de 6 (numero de condicion {cond:.1e})")
            continue
        P = np.linalg.inv(A)
        sp = np.sqrt(np.diag(Q3 @ P[:3, :3] @ Q3.T)); sv = np.sqrt(np.diag(Q3 @ P[3:, 3:] @ Q3.T))
        out.append(f"{nom:26s} {sp[0]:9.1f} {sp[1]:9.1f} {sp[2]:9.1f}    {sv[0]:8.4f} {sv[1]:8.4f} {sv[2]:8.4f}   {cond:12.2e}")
        res[f"{k}_pR"] = float(sp[0]); res[f"{k}_pT"] = float(sp[1]); res[f"{k}_pN"] = float(sp[2])
        res[f"{k}_vR"] = float(sv[0]); res[f"{k}_vT"] = float(sv[1]); res[f"{k}_vN"] = float(sv[2])
    # segunda via con ruido
    rng = np.random.default_rng(101)
    est = EST
    J0 = jac(x0, est, True, True)
    W = np.diag(1 / sigmas(est, True, True) ** 2)
    Pf = np.linalg.inv(J0.T @ W @ J0)
    errs = []
    sg = sigmas(est, True, True)
    y0 = obs(x0, est, True, True)
    for _ in range(200):
        y = y0 + rng.normal(0, sg)
        x = x0 + np.array([30.0, -30, 20, 0.03, -0.03, 0.02])
        for _ in range(3):
            Jx = jac(x, est, True, True)
            x = x + np.linalg.solve(Jx.T @ W @ Jx, Jx.T @ W @ (y - obs(x, est, True, True)))
        errs.append(x - x0)
    emp = np.array(errs).std(axis=0, ddof=1)
    raz = emp / np.sqrt(np.diag(Pf))
    out.append("Cociente sigma empirica / formal (alcance+Doppler, 2 est., 200 realizaciones): " + " ".join(f"{v:.2f}" for v in raz))
    res.update(rmin=float(raz.min()), rmax=float(raz.max()))
    ok = np.all((raz > 0.8) & (raz < 1.2))
    ok &= res["b2_rango"] == 6 and res["a1_rango"] < 6
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
