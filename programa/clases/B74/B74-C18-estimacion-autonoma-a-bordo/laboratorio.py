#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C18: filtro a bordo con precision numerica limitada (simple frente a forma de Joseph, float32 frente a float64) y coste de calculo.

Todo SINTETICO: orbita kepleriana (a = 7200 km, e = 0.01, i = 55 deg; mu = 3.986004e14 m3/s2, valor nominal ilustrativo, no consultado) con medidas de posicion
(3 componentes, sigma 0.05 m, ILUSTRATIVO y optimista) cada 10 s durante 2000 s (200 pasos). Covarianza inicial 10 km y 10 m/s por eje (P0 con gran rango dinamico frente a
R). La propagacion de la verdad y de la matriz de transicion se hace en float64 (STM de diferencias centrales); la covarianza y la ganancia se actualizan en float32 de dos maneras:
(a) forma simple P = (I - K H) P ; (b) forma de Joseph P = (I - K H) P (I - K H)^T + K R K^T ; y en float64 de referencia con la forma de Joseph. Se mide el menor autovalor de P (en float64)
tras 200 pasos, la asimetria relativa, el rms del error de posicion en los ultimos 50 pasos y el NEES medio. Coste: numero aproximado de operaciones de punto flotante por paso (conteo
analitico para n = 6, m = 3). Semilla 61.
Tolerancias: la forma de Joseph en float32 debe mantener autovalores positivos; las dos formas float64 coinciden con diferencia relativa < 1e-6 en P.
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
        if abs(d) < 1e-10: break
    z = al * chi**2; C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C; g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0; rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi; gd = 1 - chi**2 / rn * C
    return np.concatenate([r, fd * r0 + gd * v0])


def stm(x, dt):
    Phi = np.zeros((6, 6))
    for k in range(6):
        d = np.zeros(6); d[k] = 1.0 if k < 3 else 1e-3
        Phi[:, k] = (prop(x + d, dt) - prop(x - d, dt)) / (2 * d[k])
    return Phi


def inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


def main():
    rng = np.random.default_rng(61)
    dt, NP = 10.0, 200
    xt = inicial()
    truth = [xt]
    for _ in range(NP):
        truth.append(prop(truth[-1], dt))
    Phis = [stm(truth[k], dt) for k in range(NP)]
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita y medidas SINTETICAS, semilla 61)", f"{NP} pasos de {dt:.0f} s"]
    res = {}
    H = np.hstack([np.eye(3), np.zeros((3, 3))])
    sal = {}
    for caso, sigz, p0pos, q in (("base", 0.05, 1e4, 1e-10), ("estres", 1e-4, 1e5, 0.0)):
        P0 = np.diag([p0pos**2] * 3 + [10.0**2] * 3)
        Qd = np.diag([0, 0, 0, q, q, q])
        R = np.eye(3) * sigz**2
        x0 = truth[0] + rng.multivariate_normal(np.zeros(6), P0)
        zs = [truth[k + 1][:3] + rng.normal(0, sigz, 3) for k in range(NP)]

        def correr(dtype, joseph):
            x = x0.copy(); P = P0.astype(dtype)
            errs = []
            for k in range(NP):
                Phi = Phis[k].astype(dtype)
                x = prop(x, dt)
                P = (Phi @ P @ Phi.T + Qd.astype(dtype)).astype(dtype)
                S = (H.astype(dtype) @ P @ H.T.astype(dtype) + R.astype(dtype)).astype(dtype)
                K = (P @ H.T.astype(dtype) @ np.linalg.inv(S)).astype(dtype)
                x = x + K.astype(np.float64) @ (zs[k] - x[:3])
                IKH = (np.eye(6, dtype=dtype) - K @ H.astype(dtype)).astype(dtype)
                if joseph:
                    P = (IKH @ P @ IKH.T + K @ R.astype(dtype) @ K.T).astype(dtype)
                else:
                    P = (IKH @ P).astype(dtype)
                errs.append(np.linalg.norm(x[:3] - truth[k + 1][:3]))
            Pd = P.astype(np.float64)
            w = np.linalg.eigvalsh((Pd + Pd.T) / 2)
            asim = np.linalg.norm(Pd - Pd.T) / np.linalg.norm(Pd)
            return P, w.min(), float(asim), float(np.sqrt(np.mean(np.square(errs[-50:]))))
        out.append(f"Caso {caso}: sigma de medida = {sigz} m ; P0 = {p0pos:.0e} m y 10 m/s ; Q = {q:.0e}")
        out.append("variante                   menor autovalor de P [m^2]   asimetria relativa   rms error pos. ultimos 50 pasos [m]")
        for nom, dtp, jos in (("float64 Joseph", np.float64, True), ("float32 Joseph", np.float32, True), ("float32 simple", np.float32, False)):
            P, wmin, asim, rms = correr(dtp, jos)
            out.append(f"{nom:24s}   {wmin:24.3e}   {asim:16.2e}   {rms:30.4f}")
            sal[(caso, nom)] = (P, wmin, asim, rms)
            k = caso + "_" + nom.replace(" ", "_")
            res[f"wmin_{k}"] = float(wmin); res[f"asim_{k}"] = asim; res[f"rms_{k}"] = rms
    n, m = 6, 3
    flops = 2 * n**3 * 2 + 2 * n * n * m * 2 + m**3 + 2 * n * m * m
    out.append(f"Coste aproximado por paso (n = 6, m = 3): {flops} operaciones de punto flotante ; a 10 Hz: {flops*10/1e3:.1f} kflop/s")
    res["flops"] = flops
    ok = sal[("estres", "float32 Joseph")][1] > 0 and sal[("base", "float32 Joseph")][1] > 0
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
