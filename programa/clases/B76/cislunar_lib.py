#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca comun de los laboratorios del bloque B76 (solo biblioteca estandar).

Constantes CONSULTADAS el 2026-11-10:
  GM_TIERRA = 398600.435507 km3/s2 y GM_LUNA = 4902.800118 km3/s2 (JPL SSD, parametros astronomicos, DE440);
  radio medio lunar 1737.4 km (JPL SSD, parametros fisicos de satelites; IAU 2015);
  semieje mayor de la Luna 384400 km, periodo sideral 27.3217 d, sinodico 29.53 d (NASA/NSSDC, ficha de la Luna);
  radio ecuatorial terrestre 6378.137 km y radio medio 6371.000 km (NASA/NSSDC, ficha de la Tierra).
Modelo: problema restringido de tres cuerpos circular y plano (CR3BP) en unidades adimensionales
(distancia = a_Luna, tiempo = 1/n, con n = sqrt((GM_T+GM_L)/a^3)); ejes sinodicos, origen en el baricentro,
Tierra en (-mu, 0, 0), Luna en (1-mu, 0, 0). El CR3BP NO es una efemeride: no incluye Sol ni excentricidad lunar.
"""
from __future__ import annotations
import math

GM_T = 398600.435507      # km3/s2
GM_L = 4902.800118        # km3/s2
R_L = 1737.4              # km
A_L = 384400.0            # km
P_SID = 27.3217           # d
P_SIN = 29.53             # d
R_T_EQ = 6378.137         # km
R_T_MED = 6371.000        # km
MU = GM_L / (GM_T + GM_L)
N_L = math.sqrt((GM_T + GM_L) / A_L ** 3)   # rad/s
T_U = 1.0 / N_L                              # s por unidad de tiempo adimensional
DIA = 86400.0


def rhs(s, mu=MU):
    """CR3BP espacial: s = (x, y, z, vx, vy, vz)."""
    x, y, z, vx, vy, vz = s
    r1 = math.sqrt((x + mu) ** 2 + y * y + z * z)
    r2 = math.sqrt((x - 1 + mu) ** 2 + y * y + z * z)
    a1 = (1 - mu) / r1 ** 3
    a2 = mu / r2 ** 3
    ax = 2 * vy + x - a1 * (x + mu) - a2 * (x - 1 + mu)
    ay = -2 * vx + y - a1 * y - a2 * y
    az = -a1 * z - a2 * z
    return (vx, vy, vz, ax, ay, az)


def rk4(f, s, h):
    k1 = f(s)
    k2 = f(tuple(a + 0.5 * h * b for a, b in zip(s, k1)))
    k3 = f(tuple(a + 0.5 * h * b for a, b in zip(s, k2)))
    k4 = f(tuple(a + h * b for a, b in zip(s, k3)))
    return tuple(a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4))


def propagar(s, t, h=1e-3, f=rhs):
    """Integra con RK4 de paso fijo h (adimensional) hasta t; devuelve el estado final."""
    n = max(1, int(math.ceil(abs(t) / h)))
    hh = t / n
    for _ in range(n):
        s = rk4(f, s, hh)
    return s


def jacobi(s, mu=MU):
    x, y, z, vx, vy, vz = s
    r1 = math.sqrt((x + mu) ** 2 + y * y + z * z)
    r2 = math.sqrt((x - 1 + mu) ** 2 + y * y + z * z)
    return x * x + y * y + 2 * (1 - mu) / r1 + 2 * mu / r2 - (vx * vx + vy * vy + vz * vz)


def omega2(x, mu=MU):
    """2*Omega sobre el eje x (y = z = 0)."""
    return x * x + 2 * (1 - mu) / abs(x + mu) + 2 * mu / abs(x - 1 + mu)


def colineales(mu=MU):
    """Posiciones x de L1, L2, L3 por biseccion de dOmega/dx = 0."""
    def g(x):
        return x - (1 - mu) * (x + mu) / abs(x + mu) ** 3 - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3

    def biseccion(a, b):
        fa = g(a)
        for _ in range(200):
            m = 0.5 * (a + b)
            fm = g(m)
            if (fm > 0) == (fa > 0):
                a, fa = m, fm
            else:
                b = m
        return 0.5 * (a + b)

    eps = 1e-9
    l1 = biseccion(1 - mu - 0.5 + eps, 1 - mu - eps)
    l2 = biseccion(1 - mu + eps, 1 - mu + 0.5)
    l3 = biseccion(-1.5, -mu - 0.5)
    return l1, l2, l3


def km(x):
    return x * A_L


def dias(t):
    return t * T_U / DIA


# ---- algebra lineal pequena (listas) ----
def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def solve(a, b):
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (m[i][n] - sum(m[i][c] * x[c] for c in range(i + 1, n))) / m[i][i]
    return x


_C = [0, 1/5, 3/10, 4/5, 8/9, 1, 1]
_A = [[], [1/5], [3/40, 9/40], [44/45, -56/15, 32/9],
      [19372/6561, -25360/2187, 64448/6561, -212/729],
      [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
      [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84]]
_B5 = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
_B4 = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]


def dp_paso(f, s, h):
    """Un paso de Dormand-Prince 5(4): devuelve (estado, error estimado maximo)."""
    k = []
    for i in range(7):
        si = tuple(s[m] + h * sum(_A[i][j] * k[j][m] for j in range(i)) for m in range(len(s))) if i else s
        k.append(f(si))
    y5 = tuple(s[m] + h * sum(_B5[j] * k[j][m] for j in range(7)) for m in range(len(s)))
    y4 = tuple(s[m] + h * sum(_B4[j] * k[j][m] for j in range(7)) for m in range(len(s)))
    return y5, max(abs(a - b) for a, b in zip(y5, y4))


def propagar_ad(s, T, tol=1e-12, f=rhs, h0=1e-3, paso_max=0.01):
    """Integracion adaptativa Dormand-Prince hasta T (T > 0)."""
    t, h = 0.0, h0
    while t < T:
        h = min(h, T - t, paso_max)
        y, e = dp_paso(f, s, h)
        if e <= tol:
            s, t = y, t + h
        h *= min(4.0, max(0.2, 0.9 * (tol / max(e, 1e-300)) ** 0.2))
    return s


def cruce_y0(s, h=None, tmax=20.0, tol=1e-12):
    """Siguiente cruce de y = 0 (distinto del inicial). Devuelve (t, estado). Integracion adaptativa + biseccion."""
    t, hh = 0.0, 1e-3
    y_prev = s[1]
    while t < tmax:
        hh = min(hh, 0.01)
        y, e = dp_paso(rhs, s, hh)
        if e > tol:
            hh *= max(0.2, 0.9 * (tol / e) ** 0.2)
            continue
        if t > 0 and y[1] * y_prev < 0 or (t == 0 and y[1] * y_prev < 0 and abs(s[1]) > 1e-9):
            a, b = 0.0, hh
            for _ in range(60):
                m = 0.5 * (a + b)
                sm, _e = dp_paso(rhs, s, m)
                if sm[1] * y_prev < 0:
                    b = m
                else:
                    a = m
            tc = 0.5 * (a + b)
            return t + tc, dp_paso(rhs, s, tc)[0]
        s, t = y, t + hh
        if abs(s[1]) > 1e-9:
            y_prev = s[1]
        hh *= min(4.0, max(0.2, 0.9 * (tol / max(e, 1e-300)) ** 0.2))
    raise RuntimeError("sin cruce")


# ---- dinamica relativa HCW (x radial, y a lo largo de la trayectoria, z normal al plano) ----
MU_T = GM_T  # km3/s2 (Tierra)


def hcw(n, t, s0):
    """Solucion cerrada de Hill-Clohessy-Wiltshire. s0 = (x,y,z,vx,vy,vz) [m, m/s]; n [rad/s]; t [s]."""
    x0, y0, z0, u0, v0, w0 = s0
    c, s = math.cos(n * t), math.sin(n * t)
    x = (4 - 3 * c) * x0 + s / n * u0 + 2 * (1 - c) / n * v0
    y = 6 * (s - n * t) * x0 + y0 - 2 * (1 - c) / n * u0 + (4 * s - 3 * n * t) / n * v0
    z = z0 * c + w0 / n * s
    u = 3 * n * s * x0 + c * u0 + 2 * s * v0
    v = 6 * n * (c - 1) * x0 - 2 * s * u0 + (4 * c - 3) * v0
    w = -n * z0 * s + w0 * c
    return (x, y, z, u, v, w)


def hcw_blocks(n, t):
    """Bloques 3x3 (Phi_rr, Phi_rv, Phi_vr, Phi_vv) de la matriz de transicion de HCW."""
    c, s = math.cos(n * t), math.sin(n * t)
    rr = [[4 - 3 * c, 0, 0], [6 * (s - n * t), 1, 0], [0, 0, c]]
    rv = [[s / n, 2 * (1 - c) / n, 0], [-2 * (1 - c) / n, (4 * s - 3 * n * t) / n, 0], [0, 0, s / n]]
    vr = [[3 * n * s, 0, 0], [6 * n * (c - 1), 0, 0], [0, 0, -n * s]]
    vv = [[c, 2 * s, 0], [-2 * s, 4 * c - 3, 0], [0, 0, c]]
    return rr, rv, vr, vv


def kepler_rhs(s, mu=GM_T * 1e9):
    """Dos cuerpos inercial, SI (m, m/s); s = (x,y,z,vx,vy,vz)."""
    x, y, z, vx, vy, vz = s
    r3 = (x * x + y * y + z * z) ** 1.5
    return (vx, vy, vz, -mu * x / r3, -mu * y / r3, -mu * z / r3)


def propagar_dt(f, s, t, dt):
    n = max(1, int(math.ceil(t / dt)))
    h = t / n
    for _ in range(n):
        s = rk4(f, s, h)
    return s


def inv3(m):
    a, b, c = m[0]; d, e, f = m[1]; g, h, i = m[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return [[(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
            [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
            [(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det]]


def mv3(m, v):
    return [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]


def dos_impulsos(n, T, r0, v0, rf, vf):
    """Guiado de dos impulsos HCW: lleva (r0,v0) a (rf) en el tiempo T y termina con velocidad relativa vf.
    Devuelve (dv1, dv2) como listas [m/s]."""
    rr, rv, vr, vv = hcw_blocks(n, T)
    v0p = mv3(inv3(rv), [rf[i] - mv3(rr, r0)[i] for i in range(3)])
    dv1 = [v0p[i] - v0[i] for i in range(3)]
    vfin = [mv3(vr, r0)[i] + mv3(vv, v0p)[i] for i in range(3)]
    dv2 = [vf[i] - vfin[i] for i in range(3)]
    return dv1, dv2


def lvlh_a_inercial(rel, r0, n):
    """Referencia circular en (r0,0,0) con v=(0,n r0,0) [m, m/s]; rel LVLH -> (ref, cuerpo) inerciales en t = 0."""
    x, y, z, u, v, w = rel
    ref = (r0, 0.0, 0.0, 0.0, n * r0, 0.0)
    cue = (r0 + x, y, z, u - n * y, n * r0 + v + n * x, w)
    return ref, cue


def inercial_a_lvlh(ref, cue, n):
    th = math.atan2(ref[1], ref[0])
    c, s = math.cos(th), math.sin(th)
    dx, dy, dz = cue[0] - ref[0], cue[1] - ref[1], cue[2] - ref[2]
    x = c * dx + s * dy
    y = -s * dx + c * dy
    dvx, dvy, dvz = cue[3] - ref[3], cue[4] - ref[4], cue[5] - ref[5]
    return (x, y, dz, c * dvx + s * dvy + n * y, -s * dvx + c * dvy - n * x, dvz)
