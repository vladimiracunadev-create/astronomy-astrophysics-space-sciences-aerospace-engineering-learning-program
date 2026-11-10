#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C02: disparo simple y multiple para un problema de contorno de dos cuerpos.

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y UA = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Problema SINTETICO: de r0 = (1 UA, 0) alcanzar un punto objetivo r_f tras un tiempo T. El objetivo se genera propagando una velocidad
"verdadera" v_true = (3, 31) km/s, de modo que la solucion exacta existe y se conoce. Plano heliocentrico inercial; km, km/s, s.
Incognitas: v0 (disparo simple) o v0 mas los estados intermedios (disparo multiple, m tramos). Semilla de los nodos del disparo multiple: estados de la trayectoria verdadera con 3 % de error gaussiano (semilla 1), un conocimiento previo SINTETICO; el disparo simple parte solo de v0 = (0, v_c). El numero de condicion se informa con posiciones en UA y velocidades en v_c.
Metodo: Newton con el Jacobiano calculado con la matriz de transicion (ecuaciones variacionales de B81-C01); estado plano de 4 componentes.
Integrador: DOP853 con rtol = 1e-12, atol = 1e-9. Guess inicial: v0 = (0, v_c).
Tolerancias: |defecto| < 1e-6 km; error de v0 frente a v_true < 1e-9 km/s.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp

GM = 132712440041.279419
AU = 149597870.7
DIA = 86400.0
vc0 = math.sqrt(GM / AU)


def rhs(t, y):
    r = y[:2]
    rn = np.linalg.norm(r)
    a = -GM * r / rn**3
    G = GM * (3.0 * np.outer(r, r) / rn**5 - np.eye(2) / rn**3)
    A = np.zeros((4, 4))
    A[:2, 2:] = np.eye(2)
    A[2:, :2] = G
    return np.concatenate([y[2:4], a, (A @ y[4:].reshape(4, 4)).ravel()])


class Colapso(Exception):
    """La trayectoria candidata se acerca al Sol (< 0,05 UA): el candidato se descarta."""


def prop(x0, T):
    y0 = np.concatenate([x0, np.eye(4).ravel()])
    ev = lambda t, y: math.hypot(y[0], y[1]) - 0.05 * AU
    ev.terminal = True
    s = solve_ivp(rhs, (0.0, T), y0, method="DOP853", rtol=1e-12, atol=1e-9, events=ev)
    if s.status == 1:
        raise Colapso()
    y = s.y[:, -1]
    return y[:4], y[4:].reshape(4, 4)


def simple(x0, rf, T, v_init, it_max=40):
    v = np.array(v_init, float)
    hist = []
    P = np.eye(4)
    for k in range(it_max):
        try:
            xf, P = prop(np.concatenate([x0, v]), T)
        except Colapso:
            break
        F = xf[:2] - rf
        hist.append(np.linalg.norm(F))
        if hist[-1] < 1e-6:
            return v, k, hist, np.linalg.cond(P[:2, 2:] * (np.array([1/AU, 1/AU])[:, None]) * np.array([vc0, vc0])[None, :]), True
        try:
            dv = np.linalg.solve(P[:2, 2:], -F)
        except np.linalg.LinAlgError:
            break
        v = v + dv
        if np.linalg.norm(v) > 200.0:
            break
    return v, len(hist), hist, np.linalg.cond(P[:2, 2:] * (np.array([1/AU, 1/AU])[:, None]) * np.array([vc0, vc0])[None, :]), False


def escalado(J, n_nodos):
    """Cond del Jacobiano con posiciones en UA y velocidades en v_c (evita mezclar km con km/s)."""
    vc = math.sqrt(GM / AU)
    filas = np.concatenate([np.tile([1 / AU, 1 / AU, 1 / vc, 1 / vc], n_nodos), [1 / AU, 1 / AU]])
    cols = np.concatenate([[vc, vc], np.tile([AU, AU, vc, vc], n_nodos)])
    return np.linalg.cond(filas[:, None] * J * cols[None, :])


def multiple(x0, rf, T, v_init, m, semilla, it_max=60):
    """m tramos de igual duracion. Incognitas: v0 (2) y estados de los nodos 1..m-1 (4 cada uno)."""
    tau = T / m
    X = np.concatenate([np.array(v_init, float)] + [np.array(z, float) for z in semilla])
    n = 2 + 4 * (m - 1)
    for k in range(it_max):
        starts = [np.concatenate([x0, X[:2]])] + [X[2 + 4 * i:6 + 4 * i] for i in range(m - 1)]
        F = np.zeros(n)
        J = np.zeros((n, n))
        ends, Ps = [], []
        try:
            for s in starts:
                e, P = prop(s, tau)
                ends.append(e)
                Ps.append(P)
        except Colapso:
            return X[:2], k, float("inf"), False
        for i in range(m - 1):  # continuidad: fin del tramo i - inicio del tramo i+1
            F[4 * i:4 * i + 4] = ends[i] - starts[i + 1]
            if i == 0:
                J[0:4, 0:2] = Ps[0][:, 2:]
            else:
                J[4 * i:4 * i + 4, 2 + 4 * (i - 1):2 + 4 * i] = Ps[i]
            J[4 * i:4 * i + 4, 2 + 4 * i:6 + 4 * i] = -np.eye(4)
        F[4 * (m - 1):] = ends[-1][:2] - rf
        if m == 1:
            J[:, :] = Ps[0][:2, 2:]
        else:
            J[4 * (m - 1):, 2 + 4 * (m - 2):2 + 4 * (m - 1)] = Ps[-1][:2, :]
        nf = np.linalg.norm(F)
        if nf < 1e-6:
            return X[:2], k, escalado(J, m - 1), True
        X = X + np.linalg.solve(J, -F)
    return X[:2], it_max, escalado(J, m - 1), False


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    x0 = np.array([AU, 0.0])
    v_true = np.array([3.0, 31.0])
    vc = np.sqrt(GM / AU)
    v_guess = np.array([0.0, vc])
    print(f"Problema SINTETICO: v_true = {v_true.tolist()} km/s ; guess = (0, {vc:.4f}) km/s")
    print(" T [d]  metodo            iter  cond(J)      error v0 [km/s]  convergio")
    resultados = {}
    for Td in (120, 250, 500):
        T = Td * DIA
        xf, _ = prop(np.concatenate([x0, v_true]), T)
        rf = xf[:2]
        v, it, hist, cnd, ok = simple(x0, rf, T, v_guess)
        e = np.linalg.norm(v - v_true) if ok else float("nan")
        print(f"{Td:6d}  disparo simple   {it:5d}  {cnd:9.2e}   {e:14.3e}   {'si' if ok else 'no'}")
        resultados[(Td, "simple")] = (ok, e, it)
        for m in (4, 8):
            # semilla de los nodos: estados de la trayectoria verdadera con un 3 % de error (conocimiento previo SINTETICO)
            rng = np.random.default_rng(1)
            semilla, x = [], np.concatenate([x0, v_true])
            for i in range(m - 1):
                x, _ = prop(x, T / m)
                semilla.append(x * (1 + 0.03 * rng.standard_normal(4)))
            vm, itm, cj, okm = multiple(x0, rf, T, v_guess, m, semilla)
            em = np.linalg.norm(vm - v_true) if okm else float("nan")
            print(f"{Td:6d}  multiple m={m}     {itm:5d}  {cj:9.2e}   {em:14.3e}   {'si' if okm else 'no'}")
            resultados[(Td, m)] = (okm, em, itm)
    ok1, e1, _ = resultados[(120, "simple")]
    assert ok1 and e1 < 1e-9
    for Td in (120, 250, 500):
        for m in (4, 8):
            assert resultados[(Td, m)][0] and resultados[(Td, m)][1] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
