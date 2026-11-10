#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca comun de los laboratorios del bloque B82 (problema de Lambert).

Unidades: el codigo trabaja en unidades canonicas (mu = 1); longitud en UA y tiempo en TU = sqrt(AU^3/GM_sol).
Constantes consultadas el 2026-11-10 (JPL SSD, astro_par): GM_sol = 1.32712440041279419e20 m3/s2 (DE440);
1 UA = 149597870.7 km (valor adoptado, ver CLASE). Sistema de referencia: inercial heliocentrico de EJEMPLO (plano z = 0).
Modelo: dos cuerpos, sin perturbaciones. Todo dato de los laboratorios es SINTETICO.
Contiene: propagador kepleriano (variables universales), solucionador de Lambert x-lambda (Lancaster-Blanchard / Izzo 2014),
solucionador de variables universales (z, Stumpff) y utilidades. Cada clase importa lo que necesita.
"""
from __future__ import annotations
import math
import numpy as np

GM_SOL = 1.32712440041279419e20          # m3/s2 (JPL SSD, DE440)
UA_M = 149597870700.0                     # m
TU_S = math.sqrt(UA_M ** 3 / GM_SOL)      # s por unidad de tiempo canonica
TU_DIA = TU_S / 86400.0                   # dias por TU
VU_KMS = UA_M / TU_S / 1000.0             # km/s por unidad de velocidad canonica


def stumpff(z):
    if abs(z) < 1e-8:
        return 0.5 - z / 24.0, 1.0 / 6.0 - z / 120.0
    if z > 0:
        s = math.sqrt(z)
        return (1 - math.cos(s)) / z, (s - math.sin(s)) / s ** 3
    s = math.sqrt(-z)
    return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s ** 3


def propagar(r0, v0, dt, mu=1.0):
    """Propagador kepleriano por variables universales (Newton con salvaguarda). Devuelve r, v."""
    r0 = np.asarray(r0, float); v0 = np.asarray(v0, float)
    nr0 = np.linalg.norm(r0); vr0 = np.dot(r0, v0) / nr0
    alpha = 2.0 / nr0 - np.dot(v0, v0) / mu
    sm = math.sqrt(mu)
    def fun(chi):
        z = alpha * chi * chi
        c, s = stumpff(z)
        f = nr0 * vr0 / sm * chi ** 2 * c + (1 - alpha * nr0) * chi ** 3 * s + nr0 * chi - sm * dt
        df = nr0 * vr0 / sm * chi * (1 - z * s) + (1 - alpha * nr0) * chi ** 2 * c + nr0
        return f, df

    sgn = 1.0 if dt >= 0 else -1.0
    dt = abs(dt)
    lo, hi = 0.0, max(1e-3, sm * dt / nr0)       # f(chi) es creciente en chi: se acota la raiz
    while fun(sgn * hi)[0] * sgn < 0:
        lo, hi = hi, hi * 2.0
    chi = 0.5 * (lo + hi)
    for _ in range(300):
        f, df = fun(sgn * chi)
        f *= sgn
        if f < 0: lo = chi
        else: hi = chi
        cn = chi - f / df
        if not (lo < cn < hi):
            cn = 0.5 * (lo + hi)
        if abs(cn - chi) < 1e-15 * max(1.0, chi):
            chi = cn
            break
        chi = cn
    chi *= sgn
    dt = sgn * dt
    z = alpha * chi * chi
    c, s = stumpff(z)
    fl = 1 - chi ** 2 / nr0 * c
    g = dt - chi ** 3 / sm * s
    r = fl * r0 + g * v0
    nr = np.linalg.norm(r)
    fd = sm / (nr * nr0) * (z * s - 1) * chi
    gd = 1 - chi ** 2 / nr * c
    return r, fd * r0 + gd * v0


def residuo(r1, v1, r2, tof, mu=1.0):
    """Distancia (UA canonicas) entre r2 y la posicion propagada desde (r1, v1) durante tof."""
    r, _ = propagar(r1, v1, tof, mu)
    return float(np.linalg.norm(r - np.asarray(r2)))


def energia(r, v, mu=1.0):
    return 0.5 * float(np.dot(v, v)) - mu / float(np.linalg.norm(r))


# ---------------------------------------------------------------- Lancaster-Blanchard / Izzo
def y_de_x(x, lam):
    return math.sqrt(1.0 - lam * lam * (1.0 - x * x))


def tof_x(x, lam, M=0):
    """Tiempo de vuelo adimensional T(x) (forma de Lancaster-Blanchard)."""
    if abs(x - 1.0) < 1e-14:
        return 2.0 / 3.0 * (1.0 - lam ** 3)
    y = y_de_x(x, lam)
    if x < 1.0:
        psi = math.acos(x * y + lam * (1.0 - x * x))
    else:
        psi = math.asinh((y - x * lam) * math.sqrt(x * x - 1.0))
    return ((psi + M * math.pi) / math.sqrt(abs(1.0 - x * x)) - x + lam * y) / (1.0 - x * x)


def tof_lagrange(x, lam, M=0):
    """Segunda forma (Lagrange, con a = 1/(1-x^2)) para comprobar tof_x lejos de x = 1."""
    a = 1.0 / (1.0 - x * x)
    if a > 0:
        al = 2.0 * math.acos(x); be = 2.0 * math.asin(math.sqrt(lam * lam / a))
        if lam < 0: be = -be
        return a * math.sqrt(a) * ((al - math.sin(al)) - (be - math.sin(be)) + 2 * math.pi * M) / 2.0
    al = 2.0 * math.acosh(x); be = 2.0 * math.asinh(math.sqrt(-lam * lam / a))
    if lam < 0: be = -be
    return -a * math.sqrt(-a) * ((be - math.sinh(be)) - (al - math.sinh(al))) / 2.0


def derivadas_x(x, T, lam):
    y = y_de_x(x, lam)
    l2 = lam * lam; l3 = l2 * lam; l5 = l3 * l2
    d1 = (3.0 * T * x - 2.0 + 2.0 * l3 * x / y) / (1.0 - x * x)
    d2 = (3.0 * T + 5.0 * x * d1 + 2.0 * (1.0 - l2) * l3 / y ** 3) / (1.0 - x * x)
    d3 = (7.0 * x * d2 + 8.0 * d1 - 6.0 * (1.0 - l2) * l5 * x / y ** 5) / (1.0 - x * x)
    return d1, d2, d3


def x_tmin(lam, M, tol=1e-13):
    """x donde T(x) es minimo para M >= 1 (Halley sobre T'(x) = 0)."""
    if M == 0:
        return math.inf
    x = 0.1 if lam > 0 else -0.1
    x = 0.0
    for _ in range(60):
        T = tof_x(x, lam, M)
        d1, d2, d3 = derivadas_x(x, T, lam)
        xn = x - 2.0 * d1 * d2 / (2.0 * d2 * d2 - d1 * d3)
        if abs(xn - x) < tol:
            x = xn; break
        x = xn
    return x


def x_inicial(T, lam, M, rama="derecha"):
    if M == 0:
        T0 = math.acos(lam) + lam * math.sqrt(1 - lam * lam)
        T1 = 2.0 / 3.0 * (1 - lam ** 3)
        if T >= T0:
            return (T0 / T) ** (2.0 / 3.0) - 1.0
        if T < T1:
            return 2.5 * T1 * (T1 - T) / (T * (1 - lam ** 5)) + 1.0
        return (T0 / T) ** (math.log(T1 / T0) / math.log(2.0)) - 1.0
    if rama == "izquierda":
        t = ((M * math.pi + math.pi) / (8.0 * T)) ** (2.0 / 3.0)
    else:
        t = (8.0 * T / (M * math.pi)) ** (2.0 / 3.0)
        return (t - 1.0) / (t + 1.0)
    return (t - 1.0) / (t + 1.0)


def resolver_x(T, lam, M=0, rama="derecha", metodo="householder", tol=1e-12, maxit=50, x0=None, traza=None):
    """Raiz de T(x) = T. Devuelve (x, iteraciones) o (None, 0) si no hay solucion (T < Tmin)."""
    if M > 0:
        xm = x_tmin(lam, M)
        if T < tof_x(xm, lam, M):
            return None, 0
    x = x_inicial(T, lam, M, rama) if x0 is None else x0
    it = 0
    while it < maxit:
        Tx = tof_x(x, lam, M)
        d = Tx - T
        if traza is not None:
            traza.append(abs(d))
        d1, d2, d3 = derivadas_x(x, Tx, lam)
        if metodo == "newton":
            xn = x - d / d1
        elif metodo == "halley":
            xn = x - 2.0 * d * d1 / (2.0 * d1 * d1 - d * d2)
        else:
            xn = x - d * (d1 * d1 - d * d2 / 2.0) / (d1 * (d1 * d1 - d * d2) + d3 * d * d / 6.0)
        it += 1
        if abs(xn - x) < tol:
            x = xn
            break
        x = xn
    return x, it


def geometria(r1, r2, prograda=True, normal=None):
    """Devuelve c, s, lam (con signo), n (normal del plano), t1, t2 (tangentes en el sentido del movimiento)."""
    r1 = np.asarray(r1, float); r2 = np.asarray(r2, float)
    nr1, nr2 = np.linalg.norm(r1), np.linalg.norm(r2)
    c = float(np.linalg.norm(r2 - r1)); s = 0.5 * (nr1 + nr2 + c)
    lam = math.sqrt(max(0.0, 1.0 - c / s))
    ref = np.array([0.0, 0.0, 1.0]) if normal is None else np.asarray(normal, float)
    h = np.cross(r1, r2)
    nh = np.linalg.norm(h)
    if nh < 1e-12 * nr1 * nr2:                 # 0 o 180 deg: el plano no esta definido, se usa ref
        h = ref.copy(); nh = np.linalg.norm(h)
    h = h / nh
    n = h if (np.dot(h, ref) > 0) == bool(prograda) else -h
    if np.dot(n, h) < 0:
        lam = -lam                              # el giro es de mas de 180 deg alrededor de n
    t1 = np.cross(n, r1 / nr1); t2 = np.cross(n, r2 / nr2)
    t1 /= np.linalg.norm(t1); t2 /= np.linalg.norm(t2)
    return c, s, lam, n, t1, t2


def lambert_izzo(r1, r2, tof, mu=1.0, M=0, prograda=True, rama="derecha", metodo="householder",
                 tol=1e-12, maxit=50, normal=None, traza=None):
    """Lambert por la variable x de Lancaster-Blanchard con iteracion (Izzo 2014). Devuelve v1, v2, x, iteraciones."""
    r1 = np.asarray(r1, float); r2 = np.asarray(r2, float)
    c, s, lam, n, t1, t2 = geometria(r1, r2, prograda, normal)
    nr1, nr2 = np.linalg.norm(r1), np.linalg.norm(r2)
    T = math.sqrt(2.0 * mu / s ** 3) * tof
    x, it = resolver_x(T, lam, M, rama, metodo, tol, maxit, traza=traza)
    if x is None:
        return None
    y = y_de_x(x, lam)
    gam = math.sqrt(mu * s / 2.0)
    rho = (nr1 - nr2) / c
    sig = math.sqrt(max(0.0, 1.0 - rho * rho))
    ir1, ir2 = r1 / nr1, r2 / nr2
    vr1 = gam * ((lam * y - x) - rho * (lam * y + x)) / nr1
    vr2 = -gam * ((lam * y - x) + rho * (lam * y + x)) / nr2
    vt1 = gam * sig * (y + lam * x) / nr1
    vt2 = gam * sig * (y + lam * x) / nr2
    return vr1 * ir1 + vt1 * t1, vr2 * ir2 + vt2 * t2, x, it


# ---------------------------------------------------------------- variables universales (z, Stumpff)
def lambert_universal(r1, r2, tof, mu=1.0, prograda=True, tol=1e-12, maxit=200, metodo="biseccion", traza=None):
    """Lambert por variables universales (z, Stumpff), M = 0. Devuelve v1, v2, z, iteraciones."""
    r1 = np.asarray(r1, float); r2 = np.asarray(r2, float)
    nr1, nr2 = np.linalg.norm(r1), np.linalg.norm(r2)
    cosd = float(np.dot(r1, r2) / (nr1 * nr2))
    cz = np.cross(r1, r2)[2]
    dth = math.acos(max(-1.0, min(1.0, cosd)))
    if (prograda and cz < 0) or ((not prograda) and cz >= 0):
        dth = 2 * math.pi - dth
    A = math.sin(dth) * math.sqrt(nr1 * nr2 / (1.0 - cosd))
    sm = math.sqrt(mu)

    def yz(z):
        c, s = stumpff(z)
        return nr1 + nr2 + A * (z * s - 1.0) / math.sqrt(c)

    def F(z):
        c, s = stumpff(z); y = yz(z)
        return (y / c) ** 1.5 * s + A * math.sqrt(y) - sm * tof

    def dF(z):
        c, s = stumpff(z); y = yz(z)
        if abs(z) < 1e-6:
            return math.sqrt(2) / 40 * y ** 1.5 + A / 8 * (math.sqrt(y) + A * math.sqrt(1 / (2 * y)))
        return (y / c) ** 1.5 * (1 / (2 * z) * (c - 1.5 * s / c) + 0.75 * s * s / c) + \
            A / 8 * (3 * s / c * math.sqrt(y) + A * math.sqrt(c / y))

    it = 0
    lo, hi = -4 * math.pi ** 2 + 1e-6, 4 * math.pi ** 2 - 1e-6
    if yz(lo) <= 0:             # F(z) solo esta definida donde y(z) > 0; y(z) crece con z: se halla la frontera por biseccion
        zl, zh = lo, hi
        for _ in range(60):
            zm = 0.5 * (zl + zh)
            if yz(zm) <= 0: zl = zm
            else: zh = zm
        lo = zh
    z = 0.5 * (lo + hi) if metodo == "biseccion" else 0.0
    if metodo != "biseccion" and z < lo:
        z = lo + 0.01
    for it in range(1, maxit + 1):
        if metodo == "biseccion":
            z = 0.5 * (lo + hi)
        f = F(z)
        if traza is not None:
            traza.append(abs(f))
        if f < 0:
            lo = z
        else:
            hi = z
        if metodo == "biseccion":
            if hi - lo < tol:
                break
        else:                    # Newton con salvaguarda: si sale del intervalo, biseca
            zn = z - f / dF(z)
            if not (lo < zn < hi):
                zn = 0.5 * (lo + hi)
            if abs(zn - z) < tol:
                z = zn
                break
            z = zn
    y = yz(z)
    f = 1 - y / nr1; g = A * math.sqrt(y / mu); gd = 1 - y / nr2
    v1 = (r2 - f * r1) / g
    v2 = (gd * r2 - r1) / g
    return v1, v2, z, it


def planetas_ejemplo(theta_deg, ra=1.0, rb=1.524):
    """Dos posiciones SINTETICAS en orbitas circulares coplanares (ra, rb en UA), angulo theta entre ellas."""
    th = math.radians(theta_deg)
    return np.array([ra, 0.0, 0.0]), np.array([rb * math.cos(th), rb * math.sin(th), 0.0])
