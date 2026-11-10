#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C08: filtrado recursivo de estados (Bayes gaussiano, minimos cuadrados recursivos y Kalman lineal).

Todo SINTETICO: movimiento en una dimension, posicion p(t) = p0 + v0 t + (ruido de aceleracion q). Medida de posicion cada 1 s durante
60 s con sigma 5 m (ILUSTRATIVO). Estado x = (p, v). Pruebas:
 1) Minimos cuadrados recursivos con previa difusa (P0 = 1e12 I) frente al ajuste por lotes: diferencia < 1e-6 m.
 2) Filtro de Kalman con q = 0 y previa difusa reproduce el ajuste por lotes en el ultimo instante (Bayes recursivo = lotes).
 3) Con ruido de proceso q > 0 el filtro sigue una trayectoria con aceleracion aleatoria; se reporta el rms y la ganancia estacionaria.
 4) Una previa informativa correcta reduce la covarianza inicial; una previa incorrecta sobreconfiada produce sesgo.
Semilla 23. Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, platform, sys
import numpy as np


def kalman(y, dt, R, q, x0, P0):
    F = np.array([[1, dt], [0, 1.0]])
    Q = q * np.array([[dt**4 / 4, dt**3 / 2], [dt**3 / 2, dt**2]])
    H = np.array([[1.0, 0.0]])
    x, P = x0.copy(), P0.copy()
    xs, Ps, Ks = [], [], []
    for yk in y:
        x = F @ x
        P = F @ P @ F.T + Q
        S = H @ P @ H.T + R
        K = P @ H.T / S
        x = x + (K * (yk - H @ x)).ravel()
        P = (np.eye(2) - K @ H) @ P
        xs.append(x.copy()); Ps.append(P.copy()); Ks.append(K.ravel().copy())
    return np.array(xs), np.array(Ps), np.array(Ks)


def main():
    rng = np.random.default_rng(23)
    n, dt, sig = 60, 1.0, 5.0
    t = np.arange(1, n + 1) * dt
    p0, v0 = 100.0, 12.0
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (datos SINTETICOS, semilla 23)"]
    res = {}
    # 1) lotes frente a recursivo (q = 0)
    y = p0 + v0 * t + rng.normal(0, sig, n)
    A = np.column_stack([np.ones(n), t])
    xb = np.linalg.lstsq(A, y, rcond=None)[0]
    Pb = np.linalg.inv(A.T @ A) * sig**2
    # RLS: estado = (p0, v0) constantes
    x = np.zeros(2); P = np.eye(2) * 1e12
    for k in range(n):
        a = A[k]
        K = P @ a / (a @ P @ a + sig**2)
        x = x + K * (y[k] - a @ x)
        P = P - np.outer(K, a @ P)
    d_rls = float(np.max(np.abs(x - xb)))
    out.append(f"Lotes: p0 = {xb[0]:.4f} m, v0 = {xb[1]:.5f} m/s ; sigma = {np.sqrt(Pb[0,0]):.3f} m, {np.sqrt(Pb[1,1]):.5f} m/s")
    out.append(f"RLS vs lotes: diferencia maxima = {d_rls:.2e}")
    res.update(p0b=float(xb[0]), v0b=float(xb[1]), sp0=float(np.sqrt(Pb[0, 0])), sv0=float(np.sqrt(Pb[1, 1])), d_rls=d_rls)
    # 2) Kalman q = 0 sobre (p, v) en el instante final
    xs, Ps, Ks = kalman(y, dt, sig**2, 0.0, np.zeros(2), np.eye(2) * 1e12)
    p_lotes = xb[0] + xb[1] * t[-1]
    d_kf = abs(xs[-1, 0] - p_lotes)
    out.append(f"Kalman (q = 0) vs lotes en t = 60 s: |dp| = {d_kf:.2e} m ; sigma_p final = {np.sqrt(Ps[-1,0,0]):.3f} m")
    res.update(d_kf=float(d_kf), spf=float(np.sqrt(Ps[-1, 0, 0])))
    # 3) proceso con aceleracion aleatoria
    q = 0.05  # (m/s2)^2 ILUSTRATIVO
    p, v = 0.0, 10.0
    tru, med = [], []
    for k in range(n):
        a = rng.normal(0, np.sqrt(q))
        p += v * dt + 0.5 * a * dt**2
        v += a * dt
        tru.append([p, v]); med.append(p + rng.normal(0, sig))
    tru = np.array(tru)
    xs, Ps, Ks = kalman(med, dt, sig**2, q, np.array([0.0, 0.0]), np.diag([100.0**2, 20.0**2]))
    e = xs - tru
    rms_f = np.sqrt(np.mean(e[10:, 0] ** 2)); rms_m = np.sqrt(np.mean((np.array(med)[10:] - tru[10:, 0]) ** 2))
    out.append(f"Seguimiento con q = {q} (m/s2)^2: rms posicion del filtro = {rms_f:.3f} m frente a {rms_m:.3f} m de la medida cruda")
    out.append(f"Ganancia estacionaria K = ({Ks[-1,0]:.4f}, {Ks[-1,1]:.4f}) ; sigma_p estacionaria = {np.sqrt(Ps[-1,0,0]):.3f} m")
    res.update(rms_f=float(rms_f), rms_m=float(rms_m), k1=float(Ks[-1, 0]), k2=float(Ks[-1, 1]), spss=float(np.sqrt(Ps[-1, 0, 0])))
    # 4) previas
    xs_c, Ps_c, _ = kalman(y, dt, sig**2, 0.0, np.array([100.0, 12.0]), np.diag([10.0**2, 1.0**2]))
    xs_m, Ps_m, _ = kalman(y, dt, sig**2, 0.0, np.array([200.0, 5.0]), np.diag([1.0**2, 0.01**2]))
    err_c = abs(xs_c[-1, 0] - (p0 + v0 * t[-1])); err_m = abs(xs_m[-1, 0] - (p0 + v0 * t[-1]))
    out.append(f"Previa informativa correcta: error final {err_c:.3f} m, sigma {np.sqrt(Ps_c[-1,0,0]):.3f} m")
    out.append(f"Previa sobreconfiada y equivocada: error final {err_m:.3f} m, sigma {np.sqrt(Ps_m[-1,0,0]):.3f} m (no refleja el error)")
    res.update(err_c=float(err_c), err_m=float(err_m), sc=float(np.sqrt(Ps_c[-1, 0, 0])), sm=float(np.sqrt(Ps_m[-1, 0, 0])))
    ok = d_rls < 1e-6 and d_kf < 1e-3 and rms_f < rms_m
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
