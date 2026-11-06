#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C19: divergencia, rotacional, flujo y circulación.

Datos (PUBLICADOS): (GM)_Tierra nominal = 3.986004e14 m3/s2 y R_eE nominal =
6.3781e6 m (IAU 2015 B3, arXiv:1510.07674); omega = 7.292115e-5 rad/s y
a_E = 6378137 m (IERS Conventions 2010, TN36, tabla 1.2, GRS80).
Modelos: campo gravitatorio g(r) = -GM r / |r|^3 (masa puntual, r != 0) y campo
de velocidades de rotación rígida v = omega x r.
Resultados teóricos a comprobar (DLMF 1.6(iii)-(v), ecs. 1.6.20-1.6.22, 1.6.42,
1.6.57-1.6.58): div g = 0 y rot g = 0 fuera del origen; flujo de g a través de
una esfera que encierra la masa = -4 pi GM; flujo = 0 si no la encierra;
integral de línea de g independiente de la trayectoria = Phi(A) - Phi(B);
rot v = 2 omega; circulación de v en el ecuador = 2 pi a^2 omega (Stokes).
Supuestos: masa puntual; rotación rígida. Validez: r != 0.
Tolerancias: derivadas por cociente central 1e-6 relativa a |g|/r; cuadraturas
(Simpson) 1e-7 relativa.
"""
from __future__ import annotations
import math, platform, sys

GM, R = 3.986004e14, 6.3781e6
OMEGA, A_E = 7.292115e-5, 6378137.0


def g(p):
    x, y, z = p
    r3 = (x * x + y * y + z * z) ** 1.5
    return (-GM * x / r3, -GM * y / r3, -GM * z / r3)


def v_rot(p):
    x, y, z = p
    return (-OMEGA * y, OMEGA * x, 0.0)


def div(F, p, h):
    s = 0.0
    for i in range(3):
        a = list(p); b = list(p)
        a[i] += h; b[i] -= h
        s += (F(a)[i] - F(b)[i]) / (2 * h)
    return s


def rot(F, p, h):
    def d(comp, var):
        a = list(p); b = list(p)
        a[var] += h; b[var] -= h
        return (F(a)[comp] - F(b)[comp]) / (2 * h)
    return (d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1))


def simpson(f, a, b, n=200):
    h = (b - a) / n
    s = f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    return s * h / 3


def flujo_esfera(F, centro, radio, n=200):
    """Flujo saliente de F a través de una esfera (coordenadas esféricas)."""
    def integrando(th, ph):
        nx, ny, nz = math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)
        p = (centro[0] + radio * nx, centro[1] + radio * ny, centro[2] + radio * nz)
        f = F(p)
        return (f[0] * nx + f[1] * ny + f[2] * nz) * radio**2 * math.sin(th)
    return simpson(lambda ph: simpson(lambda th: integrando(th, ph), 0, math.pi, n), 0, 2 * math.pi, n)


def integral_linea(F, camino, t0, t1, n=2000):
    """int F . dr a lo largo de camino(t) por Simpson, con derivada numérica."""
    def f(t):
        h = 1e-6 * (t1 - t0)
        p0, p1 = camino(t - h), camino(t + h)
        dr = [(p1[i] - p0[i]) / (2 * h) for i in range(3)]
        Fv = F(camino(t))
        return sum(Fv[i] * dr[i] for i in range(3))
    return simpson(f, t0, t1, n)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # divergencia y rotacional de g
    print("Punto (en R)          |g| [m/s2]    div g [s-2]     |rot g| [s-2]")
    for p in ((1.0, 0.0, 0.0), (2.0, 1.0, -1.0), (0.3, -2.0, 1.5)):
        P = tuple(c * R for c in p)
        gm = math.sqrt(sum(c * c for c in g(P)))
        h = 1e-4 * R
        d = div(g, P, h)
        rv = rot(g, P, h)
        escala = gm / math.sqrt(sum(c * c for c in P))
        prueba(abs(d) < 1e-6 * escala and max(abs(c) for c in rv) < 1e-6 * escala, "div g = 0 y rot g = 0")
        print(f"{str(p):20s}  {gm:10.5f}  {d:12.3e}  {math.sqrt(sum(c*c for c in rv)):12.3e}")
    # flujo (ley de Gauss para la gravedad)
    print("\nFlujo de g a través de esferas (m3/s2):  -4 pi GM =", f"{-4*math.pi*GM:.6e}")
    for r_esf in (1.0, 2.0, 10.0):
        f = flujo_esfera(g, (0, 0, 0), r_esf * R)
        prueba(abs(f / (-4 * math.pi * GM) - 1) < 1e-7, "flujo = -4 pi GM")
        print(f"  esfera de radio {r_esf:4.1f} R centrada en la masa: {f:.6e}")
    f_fuera = flujo_esfera(g, (3 * R, 0, 0), 0.5 * R)
    prueba(abs(f_fuera) < 1e-7 * 4 * math.pi * GM, "flujo nulo si no encierra la masa")
    print(f"  esfera de radio 0.5 R centrada en (3R, 0, 0), sin la masa: {f_fuera:.3e}")
    # integral de línea y potencial
    A, B = (R, 0.0, 0.0), (2 * R, 0.0, 0.0)
    recto = lambda t: (R * (1 + t), 0.0, 0.0)
    arco = lambda t: (R * (1 + math.sin(math.pi * t / 2)) , R * 0.8 * math.sin(math.pi * t), 0.0)
    w1 = integral_linea(g, recto, 0.0, 1.0)
    w2 = integral_linea(g, arco, 0.0, 1.0)
    esperado = GM / (2 * R) * (-1)         # = Phi(A) - Phi(B) = -GM/R + GM/(2R)
    prueba(abs(w1 / esperado - 1) < 1e-6 and abs(w2 / esperado - 1) < 1e-6, "independencia de la trayectoria")
    print(f"\nIntegral de línea de g de R a 2R: recto {w1:.6e}; arco {w2:.6e}; Phi(A)-Phi(B) = {esperado:.6e} J/kg")
    # rotación rígida y Stokes
    P0 = (0.4 * R, 0.2 * R, 0.1 * R)
    rv = rot(v_rot, P0, 1.0)
    dv = div(v_rot, P0, 1.0)
    prueba(abs(rv[2] - 2 * OMEGA) < 1e-12 and abs(dv) < 1e-15, "rot v = 2 omega, div v = 0")
    print(f"\nv = omega x r: rot v = (0, 0, {rv[2]:.6e}) rad/s = 2 omega = {2*OMEGA:.6e};  div v = {dv:.1e}")
    circ = integral_linea(v_rot, lambda t: (A_E * math.cos(t), A_E * math.sin(t), 0.0), 0.0, 2 * math.pi)
    stokes = 2 * OMEGA * math.pi * A_E**2
    prueba(abs(circ / stokes - 1) < 1e-7, "Stokes")
    print(f"Circulación en el ecuador: {circ:.6e} m2/s;  rot . area = 2 omega pi a^2 = {stokes:.6e} m2/s")
    print(f"Velocidad del ecuador = omega a_E = {OMEGA*A_E:.3f} m/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
