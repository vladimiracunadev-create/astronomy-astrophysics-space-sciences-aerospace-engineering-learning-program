#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C24: medidas retardadas y fuera de secuencia (OOSM) en un filtro de Kalman lineal.

Todo SINTETICO: movimiento en una dimension con aceleracion aleatoria q = 0.05 (m/s2)^2, medida de posicion cada 1 s con sigma 5 m (ILUSTRATIVOS), 30 pasos,
2000 realizaciones (semilla 79). Las medidas de los pasos 21 a 25 llegan RETRASADAS: se reciben tras procesar la del paso 30 (retardo de 5 a 9 pasos).
Cuatro tratamientos: (a) DESCARTAR las medidas tardias; (b) INGENUO: usarlas como si fueran del instante actual (error de modelo); (c) RETRODICCION aproximada sin correlacion cruzada (se espera una covarianza inconsistente: es el fallo que se quiere mostrar)
(estado retropropagado x_m = F^-l x_k, con covarianza F^-l (P + Q_l) F^-l^T y SIN correlacion cruzada entre el error actual y el ruido de proceso del intervalo; la correccion K nu calculada en el instante m se traslada al instante actual con F^l y se resta F^l K S K^T F^l^T de la covarianza); (d) REPROCESAR desde el paso 20 con todas las medidas en orden (optimo para un modelo lineal; es la referencia).
Metricas en el paso 30: rms del error de posicion y NEES medio (esperado 2). Tolerancias: (d) tiene el rms mas bajo; (b) es peor que (a); el NEES de (d) esta entre 1.8 y 2.2 (promedio de 2000 casos).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

DT, SIG, Q = 1.0, 5.0, 0.05
F = np.array([[1, DT], [0, 1.0]]); G = np.array([[DT**2 / 2], [DT]]); QD = Q * (G @ G.T); H = np.array([[1.0, 0.0]]); R = SIG**2


def paso(x, P):
    return F @ x, F @ P @ F.T + QD


def upd(x, P, z):
    S = (H @ P @ H.T)[0, 0] + R
    K = (P @ H.T)[:, 0] / S
    x = x + K * (z - x[0])
    P = (np.eye(2) - np.outer(K, H[0])) @ P
    return x, P


def Fl(l):
    return np.linalg.matrix_power(F, l)


def Ql(l):
    Qs = np.zeros((2, 2))
    for j in range(l):
        Fj = np.linalg.matrix_power(F, j)
        Qs += Fj @ QD @ Fj.T
    return Qs


def main():
    rng = np.random.default_rng(79)
    n = 30
    tarde = range(21, 26)
    NR = 2000
    errs = {k: [] for k in "abcd"}
    nopd = {k: 0 for k in "abcd"}
    nees = {k: [] for k in "abcd"}
    x0 = np.array([0.0, 8.0]); P0 = np.diag([100.0**2, 20.0**2])
    for _ in range(NR):
        x = np.array([0.0, 10.0]); tru = [x.copy()]
        for k in range(1, n + 1):
            a = rng.normal(0, math.sqrt(Q))
            x = F @ x + G[:, 0] * a
            tru.append(x.copy())
        z = {k: tru[k][0] + rng.normal(0, SIG) for k in range(1, n + 1)}
        # estado normal hasta el paso 20 (todas las medidas llegan)
        xe, Pe = x0.copy(), P0.copy()
        hist = {}
        for k in range(1, 21):
            xe, Pe = paso(xe, Pe); xe, Pe = upd(xe, Pe, z[k])
        x20, P20 = xe.copy(), Pe.copy()
        # pasos 21-25 sin sus medidas, 26-30 con ellas
        xe, Pe = x20.copy(), P20.copy()
        for k in range(21, 31):
            xe, Pe = paso(xe, Pe)
            if k not in tarde:
                xe, Pe = upd(xe, Pe, z[k])
        x30, P30 = xe.copy(), Pe.copy()
        res = {}
        res["a"] = (x30, P30)
        # (b) ingenuo
        xb, Pb = x30.copy(), P30.copy()
        for k in tarde:
            xb, Pb = upd(xb, Pb, z[k])
        res["b"] = (xb, Pb)
        # (c) retrodiccion aproximada
        xc, Pc = x30.copy(), P30.copy()
        for k in tarde:
            l = 30 - k
            Fi = np.linalg.inv(Fl(l))
            xm = Fi @ xc
            Pm = Fi @ (Pc + Ql(l)) @ Fi.T
            Sm = (H @ Pm @ H.T)[0, 0] + R
            Km = (Pm @ H.T)[:, 0] / Sm
            nu = z[k] - xm[0]
            xc = xc + Fl(l) @ (Km * nu)
            Pc = Pc - Fl(l) @ np.outer(Km, Km) @ Fl(l).T * Sm
        res["c"] = (xc, Pc)
        # (d) reprocesar
        xd, Pd = x20.copy(), P20.copy()
        for k in range(21, 31):
            xd, Pd = paso(xd, Pd); xd, Pd = upd(xd, Pd, z[k])
        res["d"] = (xd, Pd)
        for kk, (xx, PP) in res.items():
            e = xx - tru[30]
            errs[kk].append(e[0]); nees[kk].append(float(e @ np.linalg.solve(PP, e)))
            nopd[kk] += int(np.min(np.linalg.eigvalsh((PP + PP.T) / 2)) <= 0)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (datos SINTETICOS, semilla 79)",
           f"{NR} realizaciones; medidas de los pasos 21-25 llegan tras el paso 30 (retardo de 5 a 9 pasos)"]
    out.append("tratamiento                           rms error de posicion [m]   NEES medio (esperado 2)   covarianza no definida positiva")
    nom = {"a": "(a) descartar", "b": "(b) ingenuo (como actual)", "c": "(c) retrodiccion aproximada", "d": "(d) reprocesar en orden"}
    res = {}
    for k in "abcd":
        rms = float(np.sqrt(np.mean(np.square(errs[k])))); ne = float(np.mean(nees[k]))
        out.append(f"{nom[k]:36s} {rms:20.3f}   {ne:18.3f}   {nopd[k]/NR*100:18.1f} %")
        res[f"rms_{k}"] = rms; res[f"nees_{k}"] = ne; res[f"nopd_{k}"] = nopd[k] / NR * 100
    ok = res["rms_d"] <= min(res["rms_a"], res["rms_b"], res["rms_c"]) and res["rms_b"] > res["rms_a"] and 1.8 < res["nees_d"] < 2.2
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
