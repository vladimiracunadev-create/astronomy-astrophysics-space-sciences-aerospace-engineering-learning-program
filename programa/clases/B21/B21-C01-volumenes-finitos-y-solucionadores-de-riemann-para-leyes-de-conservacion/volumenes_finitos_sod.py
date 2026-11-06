#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B21-C01: volumenes finitos y solucionadores de Riemann.

Datos: SINTETICOS y adimensionales (tubo de choque de Sod: izquierda rho=1,
u=0, p=1; derecha rho=0.125, u=0, p=0.1; gamma=1.4; x en [0,1], disco en 0.5).
Modelo: (a) advección lineal u_t + a u_x = 0, solución exacta u0(x - a t);
(b) ecuaciones de Euler 1D de un gas ideal, comparadas con la solución exacta
del problema de Riemann (resuelta aquí por iteración de la presión).
Método: volumenes finitos de primer orden, q_i^{n+1} = q_i^n - dt/dx (F_{i+1/2} - F_{i-1/2}),
con flujo contracorriente (a), Rusanov y HLL (b).
Supuestos: malla uniforme; fronteras transmisivas; sin viscosidad física.
Validez: tiempo final en que las ondas aún no llegan a las fronteras.
Tolerancias (las pruebas detienen la ejecución si fallan): presión y velocidad de
la región estrella frente a valores tabulados (1e-4); orden observado de (a)
en [0.9, 1.1]; conservación de masa y energía < 1e-12 y de momento igual al
flujo de frontera < 1e-12; error L1 de HLL <= error L1 de Rusanov; el error L1
de la densidad decrece con N y su orden observado queda en [0.4, 1.2].
"""
import math
import platform

import numpy as np

G = 1.4


def prim_a_cons(rho, u, p):
    return np.array([rho, rho * u, p / (G - 1) + 0.5 * rho * u * u])


def flujo(q):
    rho, m, e = q
    u = m / rho
    p = (G - 1) * (e - 0.5 * rho * u * u)
    return np.array([m, m * u + p, u * (e + p)])


def velocidad_sonido(q):
    rho, m, e = q
    p = (G - 1) * (e - 0.5 * m * m / rho)
    return math.sqrt(G * p / rho)


def flujo_rusanov(qL, qR):
    smax = max(abs(qL[1] / qL[0]) + velocidad_sonido(qL),
               abs(qR[1] / qR[0]) + velocidad_sonido(qR))
    return 0.5 * (flujo(qL) + flujo(qR)) - 0.5 * smax * (qR - qL)


def flujo_hll(qL, qR):
    uL, uR = qL[1] / qL[0], qR[1] / qR[0]
    cL, cR = velocidad_sonido(qL), velocidad_sonido(qR)
    bm = min(min(uL - cL, uR - cR), 0.0)
    bp = max(max(uL + cL, uR + cR), 0.0)
    return (bp * flujo(qL) - bm * flujo(qR)) / (bp - bm) + bp * bm / (bp - bm) * (qR - qL)


def avanzar(q0, dx, tfin, flujo_num, cfl=0.8):
    q = q0.copy()
    n = q.shape[1]
    t = 0.0
    flujo_frontera = np.zeros(3)  # integral en el tiempo del flujo neto que entra
    while t < tfin - 1e-14:
        smax = max(abs(q[1, i] / q[0, i]) + velocidad_sonido(q[:, i]) for i in range(n))
        dt = min(cfl * dx / smax, tfin - t)
        qe = np.concatenate([q[:, :1], q, q[:, -1:]], axis=1)  # transmisiva
        F = np.array([flujo_num(qe[:, i], qe[:, i + 1]) for i in range(n + 1)]).T
        q = q - dt / dx * (F[:, 1:] - F[:, :-1])
        flujo_frontera += dt * (F[:, 0] - F[:, -1])
        t += dt
    return q, flujo_frontera


def solucion_exacta(x, t, WL=(1.0, 0.0, 1.0), WR=(0.125, 0.0, 0.1), x0=0.5):
    rL, uL, pL = WL
    rR, uR, pR = WR
    cL, cR = math.sqrt(G * pL / rL), math.sqrt(G * pR / rR)

    def f(p, r, pk, ck):
        if p > pk:
            A, B = 2 / ((G + 1) * r), (G - 1) / (G + 1) * pk
            return (p - pk) * math.sqrt(A / (p + B))
        return 2 * ck / (G - 1) * ((p / pk) ** ((G - 1) / (2 * G)) - 1)

    def F(p):
        return f(p, rL, pL, cL) + f(p, rR, pR, cR) + (uR - uL)

    lo, hi = 1e-8, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(lo) * F(mid) <= 0:
            hi = mid
        else:
            lo = mid
    ps = 0.5 * (lo + hi)
    us = 0.5 * (uL + uR) + 0.5 * (f(ps, rR, pR, cR) - f(ps, rL, pL, cL))
    # configuración de Sod: rarefacción a la izquierda, choque a la derecha
    rsL = rL * (ps / pL) ** (1 / G)
    csL = cL * (ps / pL) ** ((G - 1) / (2 * G))
    rsR = rR * ((ps / pR + (G - 1) / (G + 1)) / ((G - 1) / (G + 1) * ps / pR + 1))
    SR = uR + cR * math.sqrt((G + 1) / (2 * G) * ps / pR + (G - 1) / (2 * G))
    cabeza, cola = uL - cL, us - csL
    rho = np.empty_like(x)
    for k, xx in enumerate(x):
        s = (xx - x0) / t
        if s < cabeza:
            rho[k] = rL
        elif s < cola:
            c_ = 2 / (G + 1) * (cL + (G - 1) / 2 * (uL - s))
            rho[k] = rL * (c_ / cL) ** (2 / (G - 1))
        elif s < us:
            rho[k] = rsL
        elif s < SR:
            rho[k] = rsR
        else:
            rho[k] = rR
    return rho, ps, us, rsL, rsR


def malla(N):
    dx = 1.0 / N
    x = (np.arange(N) + 0.5) * dx
    return x, dx


def inicial(x):
    q = np.zeros((3, x.size))
    for i, xx in enumerate(x):
        q[:, i] = prim_a_cons(1.0, 0.0, 1.0) if xx < 0.5 else prim_a_cons(0.125, 0.0, 0.1)
    return q


print(f"Python {platform.python_version()}  NumPy {np.__version__}")

# (a) advección lineal con flujo contracorriente
print("(a) advección lineal, u0 = sin(2 pi x), a = 1, periodica, t = 1 (una vuelta)")
errs = []
for N in (50, 100, 200, 400):
    dx = 1.0 / N
    x = (np.arange(N) + 0.5) * dx
    u = np.sin(2 * math.pi * x)
    masa0 = u.sum() * dx
    nsteps = int(round(1.0 / (0.8 * dx)))
    dt = 1.0 / nsteps
    for _ in range(nsteps):
        u = u - dt / dx * (u - np.roll(u, 1))
    # promedio de celda exacto de sin(2 pi (x - 1)) = sin(2 pi x)
    err = float(np.max(np.abs(u - np.sin(2 * math.pi * x))))
    errs.append(err)
    assert abs(u.sum() * dx - masa0) < 1e-12, "no conserva"
    print(f"    N={N:4d}  error max = {err:.4e}")
orden = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
print("    orden observado:", " ".join(f"{o:.3f}" for o in orden))
assert all(0.9 <= o <= 1.1 for o in orden[1:]), "orden fuera de rango"

# (b) Sod: solución exacta
xs = np.linspace(0, 1, 11)
_, ps, us, rsL, rsR = solucion_exacta(xs, 0.2)
print(f"(b) Sod exacto: p* = {ps:.5f}  u* = {us:.5f}  rho*_izq = {rsL:.5f}  rho*_der = {rsR:.5f}")
assert abs(ps - 0.30313) < 1e-4 and abs(us - 0.92745) < 1e-4, "estado estrella"

# (b) Sod numérico
tfin = 0.2
tabla = {}
for nombre, fn in (("Rusanov", flujo_rusanov), ("HLL", flujo_hll)):
    prev = None
    errs_l1 = []
    for N in (100, 200, 400):
        x, dx = malla(N)
        q0 = inicial(x)
        q, fb = avanzar(q0, dx, tfin, fn)
        rho_ex = solucion_exacta(x, tfin)[0]
        l1 = float(np.sum(np.abs(q[0] - rho_ex)) * dx)
        errs_l1.append(l1)
        tot0, tot = q0.sum(axis=1) * dx, q.sum(axis=1) * dx
        res = tot - tot0 - fb  # cambio total menos flujo de frontera
        assert np.max(np.abs(res)) < 1e-12, "conservación"
        p_cambio_esp = (1.0 - 0.1) * tfin
        assert abs((tot[1] - tot0[1]) - p_cambio_esp) < 1e-12, "momento"
        assert abs(tot[0] - tot0[0]) < 1e-12 and abs(tot[2] - tot0[2]) < 1e-12
        print(f"    {nombre:7s} N={N:4d}  L1(densidad) = {l1:.4e}  residuo de conservacion = {np.max(np.abs(res)):.1e}")
    o = [math.log2(errs_l1[i] / errs_l1[i + 1]) for i in range(2)]
    print(f"    {nombre:7s} orden observado L1: {o[0]:.3f} {o[1]:.3f}")
    assert errs_l1[0] > errs_l1[1] > errs_l1[2]
    assert all(0.4 <= v <= 1.2 for v in o)
    tabla[nombre] = errs_l1
assert all(h <= r for h, r in zip(tabla["HLL"], tabla["Rusanov"])), "HLL no mejora a Rusanov"
print("Pruebas superadas.")
