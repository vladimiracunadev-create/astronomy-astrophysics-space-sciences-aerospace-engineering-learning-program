#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C12: encuentro parabolico entre dos galaxias con un disco de particulas de prueba.

Datos: ninguno observado. Todo SIMULADO en unidades G = 1: dos galaxias puntuales de masa 1 cada
una; el disco de la galaxia 1 son 120 particulas de prueba (sin masa) en cinco anillos circulares de
radio 0,2 a 0,6 (en unidades del pericentro, r_p = 1), orbita prograda. Los numeros de particulas y radios
son una eleccion de esta clase.
Modelo: problema restringido de tres cuerpos generalizado: las dos masas puntuales siguen una orbita
parabolica de dos cuerpos (masa total 2, r_p = 1); las particulas de prueba sienten ambas masas y no se
atraen entre si ni devuelven fuerza. Integrador leapfrog (kick-drift-kick), paso 0,002.
Supuestos: galaxias como masas puntuales (sin halo extenso ni friccion dinamica), disco plano coplanar
con la orbita, sin gas.
Validez: cualitativa; muestra colas y capturas, no reproduce una fusion real.
Tolerancias: 1e-3 (tiempo de Barker), 1e-6 (energia de la orbita), 1e-4 (anillos sin perturbador).
"""
from __future__ import annotations
import math
import platform
import sys

DT = 0.002


def accel(p, masas, pos):
    ax = ay = 0.0
    for m, (x, y) in zip(masas, pos):
        dx, dy = x - p[0], y - p[1]
        r3 = (dx * dx + dy * dy) ** 1.5
        ax += m * dx / r3
        ay += m * dy / r3
    return ax, ay


def barker_tiempo(r, rp=1.0, mtot=2.0):
    """Tiempo desde el pericentro hasta distancia r en una parabola: Barker."""
    p = 2 * rp
    nu = math.acos(p / r - 1)
    t2 = math.tan(nu / 2)
    return math.sqrt(p ** 3 / mtot) / 2 * (t2 + t2 ** 3 / 3)


def condiciones_iniciales(r0=10.0, rp=1.0, mtot=2.0):
    p = 2 * rp
    nu = -math.acos(p / r0 - 1)
    vr = math.sqrt(mtot / p) * math.sin(nu)
    vt = math.sqrt(mtot / p) * (1 + math.cos(nu))
    x, y = r0 * math.cos(nu), r0 * math.sin(nu)
    vx = vr * math.cos(nu) - vt * math.sin(nu)
    vy = vr * math.sin(nu) + vt * math.cos(nu)
    return (x, y), (vx, vy)


def paso_dos_cuerpos(rel, vrel, dt):
    """Un paso leapfrog de la orbita relativa, masa total 2."""
    ax, ay = accel(rel, [2.0], [(0.0, 0.0)])
    vrel = (vrel[0] + 0.5 * dt * ax, vrel[1] + 0.5 * dt * ay)
    rel = (rel[0] + dt * vrel[0], rel[1] + dt * vrel[1])
    ax, ay = accel(rel, [2.0], [(0.0, 0.0)])
    vrel = (vrel[0] + 0.5 * dt * ax, vrel[1] + 0.5 * dt * ay)
    return rel, vrel


def tiempo_hasta_r(r_obj, dt=1e-3):
    rel, vrel = (1.0, 0.0), (0.0, math.sqrt(2 * 2.0 / 1.0))  # pericentro: v = sqrt(2 mtot/rp)
    t = 0.0
    e0 = 0.5 * (vrel[0] ** 2 + vrel[1] ** 2) - 2.0 / math.hypot(*rel)
    while math.hypot(*rel) < r_obj:
        rel, vrel = paso_dos_cuerpos(rel, vrel, dt)
        t += dt
    e1 = 0.5 * (vrel[0] ** 2 + vrel[1] ** 2) - 2.0 / math.hypot(*rel)
    return t, e0, e1


def simula(con_perturbador=True, t_final=40.0):
    rel, vrel = condiciones_iniciales()
    m2 = 1.0 if con_perturbador else 0.0
    # galaxia 1 en -rel/2, galaxia 2 en +rel/2 (masas iguales)
    parts = []
    radios = (0.2, 0.3, 0.4, 0.5, 0.6)
    cuentas = (12, 18, 24, 30, 36)
    r1 = (-rel[0] / 2, -rel[1] / 2)
    v1 = (-vrel[0] / 2, -vrel[1] / 2)
    for R, nn in zip(radios, cuentas):
        for k in range(nn):
            ang = 2 * math.pi * k / nn
            vc = math.sqrt(1.0 / R)
            parts.append([r1[0] + R * math.cos(ang), r1[1] + R * math.sin(ang),
                          v1[0] - vc * math.sin(ang), v1[1] + vc * math.cos(ang), R])
    g1 = [r1[0], r1[1], v1[0], v1[1]]
    g2 = [rel[0] / 2, rel[1] / 2, vrel[0] / 2, vrel[1] / 2]
    dt = DT
    n = int(round(t_final / dt))
    def acc_g(a, b, m_b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        r3 = (dx * dx + dy * dy) ** 1.5
        return m_b * dx / r3, m_b * dy / r3
    for _ in range(n):
        if m2:
            a1 = acc_g(g1, g2, 1.0); a2 = acc_g(g2, g1, 1.0)
            g1[2] += 0.5 * dt * a1[0]; g1[3] += 0.5 * dt * a1[1]
            g2[2] += 0.5 * dt * a2[0]; g2[3] += 0.5 * dt * a2[1]
        else:
            g2[2] = g2[3] = 0.0
        for p in parts:
            ax, ay = accel(p, [1.0, m2], [(g1[0], g1[1]), (g2[0], g2[1])]) if m2 else accel(p, [1.0], [(g1[0], g1[1])])
            p[2] += 0.5 * dt * ax; p[3] += 0.5 * dt * ay
        g1[0] += dt * g1[2]; g1[1] += dt * g1[3]
        if m2:
            g2[0] += dt * g2[2]; g2[1] += dt * g2[3]
        for p in parts:
            p[0] += dt * p[2]; p[1] += dt * p[3]
        if m2:
            a1 = acc_g(g1, g2, 1.0); a2 = acc_g(g2, g1, 1.0)
            g1[2] += 0.5 * dt * a1[0]; g1[3] += 0.5 * dt * a1[1]
            g2[2] += 0.5 * dt * a2[0]; g2[3] += 0.5 * dt * a2[1]
        for p in parts:
            ax, ay = accel(p, [1.0, m2], [(g1[0], g1[1]), (g2[0], g2[1])]) if m2 else accel(p, [1.0], [(g1[0], g1[1])])
            p[2] += 0.5 * dt * ax; p[3] += 0.5 * dt * ay
    return parts, g1, g2


def clasifica(parts, g1, g2):
    lig1 = lig2 = libres = 0
    colas = 0
    for p in parts:
        e1 = 0.5 * ((p[2] - g1[2]) ** 2 + (p[3] - g1[3]) ** 2) - 1.0 / math.hypot(p[0] - g1[0], p[1] - g1[1])
        e2 = 0.5 * ((p[2] - g2[2]) ** 2 + (p[3] - g2[3]) ** 2) - 1.0 / math.hypot(p[0] - g2[0], p[1] - g2[1])
        if e1 < 0 and e1 <= e2:
            lig1 += 1
            if math.hypot(p[0] - g1[0], p[1] - g1[1]) > 2 * p[4]:
                colas += 1
        elif e2 < 0:
            lig2 += 1
        else:
            libres += 1
    return lig1, lig2, libres, colas


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: Barker frente a leapfrog y conservacion de la energia de la parabola
    t_num, e0, e1 = tiempo_hasta_r(10.0)
    t_bar = barker_tiempo(10.0)
    assert abs(t_num / t_bar - 1) < 1e-3, "tiempo de Barker"
    assert abs(e0) < 1e-12 and abs(e1) < 1e-6, "energia de la parabola"
    # Prueba 2: sin perturbador los anillos conservan su radio
    parts, g1, g2 = simula(con_perturbador=False, t_final=10.0)
    for p in parts:
        r = math.hypot(p[0] - g1[0], p[1] - g1[1])
        assert abs(r / p[4] - 1) < 1e-4, "anillo no conserva el radio"
    print(f"Barker: t(pericentro -> r = 10) = {t_bar:.4f} ; leapfrog = {t_num:.4f} ; energia final = {e1:.2e}")
    parts, g1, g2 = simula(True, 40.0)
    l1, l2, lb, colas = clasifica(parts, g1, g2)
    n = len(parts)
    print(f"t = 40 desde r = 10, con pericentro en t = 12 (parabolica, r_p = 1, masas iguales, N = {n}):")
    print(f"  ligadas a la galaxia 1: {l1} ({100 * l1 / n:.0f} %), de ellas extendidas (> 2 x radio inicial): {colas}")
    print(f"  capturadas por la galaxia 2: {l2} ({100 * l2 / n:.0f} %) ; no ligadas a ninguna: {lb} ({100 * lb / n:.0f} %)")
    print(f"  separacion final de las galaxias = {math.hypot(g1[0] - g2[0], g1[1] - g2[1]):.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
