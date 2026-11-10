#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C16: captura blanda 1D con resorte y amortiguador, y conservacion del momento.

Datos SINTETICOS (no proceden de ningun sistema de acoplamiento real; los estandares de acoplamiento NO se consultaron):
masa del perseguidor 7000 kg, masa del objetivo 15000 kg, velocidad de cierre 0.10 m/s, rigidez del mecanismo de captura 2.0e5 N/m,
amortiguamiento 1.2e5 N s/m, desalineacion lateral 0.05 m, brazo de contacto 1.2 m.
Modelo: dos masas libres unidas por un resorte-amortiguador lineal que se activa al contacto; RK4 con paso 1 ms durante 20 s.
Magnitudes: masa reducida mu = m1 m2/(m1+m2); fuerza maxima sin amortiguacion F = v sqrt(k mu); energia disipada = 1/2 mu v^2.
Verificaciones: momento total conservado (< 1e-9 relativa), velocidad final comun = m1 v/(m1+m2), energia disipada frente a 1/2 mu v^2.
Tolerancias: 1e-6 relativa en la energia (la oscilacion residual decae con el amortiguamiento).
"""
from __future__ import annotations
import math, os, platform, sys

M1, M2, V0 = 7000.0, 15000.0, 0.10
K, C = 2.0e5, 1.2e5
DESALINEO, BRAZO = 0.05, 1.2


def simular(k=K, c=C, v0=V0, dt=1e-3, t_fin=20.0):
    x1, x2, v1, v2 = 0.0, 0.0, v0, 0.0     # x1 perseguidor (acercandose), x2 objetivo en reposo; compresion = x1 - x2
    fmax = 0.0
    n = int(t_fin / dt)
    def acc(x1, x2, v1, v2):
        comp = x1 - x2
        f = k * comp + c * (v1 - v2)
        if comp < 0:
            f = 0.0
        return -f / M1, f / M2, f
    for _ in range(n):
        # RK4 sobre (x1,x2,v1,v2)
        def d(s):
            a1, a2, f = acc(*s)
            return (s[2], s[3], a1, a2), f
        s = (x1, x2, v1, v2)
        k1, f1 = d(s)
        k2, _ = d(tuple(a + 0.5 * dt * b for a, b in zip(s, k1)))
        k3, _ = d(tuple(a + 0.5 * dt * b for a, b in zip(s, k2)))
        k4, _ = d(tuple(a + dt * b for a, b in zip(s, k3)))
        s = tuple(a + dt / 6 * (b + 2 * cc + 2 * dd + e) for a, b, cc, dd, e in zip(s, k1, k2, k3, k4))
        x1, x2, v1, v2 = s
        fmax = max(fmax, f1)
    return x1, x2, v1, v2, fmax


def calcular():
    mu = M1 * M2 / (M1 + M2)
    x1, x2, v1, v2, fmax = simular()
    p0 = M1 * V0
    p1 = M1 * v1 + M2 * v2
    ec0 = 0.5 * M1 * V0 ** 2
    ec1 = 0.5 * M1 * v1 ** 2 + 0.5 * M2 * v2 ** 2
    v_com = M1 * V0 / (M1 + M2)
    comp_max = V0 * math.sqrt(mu / K)
    zeta = C / (2 * math.sqrt(K * mu))
    torque = fmax * DESALINEO
    return dict(mu=mu, v1=v1, v2=v2, v_com=v_com, dp=abs(p1 - p0) / p0, e_dis=ec0 - ec1, e_teo=0.5 * mu * V0 ** 2,
                fmax=fmax, f_teo=V0 * math.sqrt(K * mu), zeta=zeta, comp_max=comp_max, torque=torque,
                ang=math.degrees(math.atan2(DESALINEO, BRAZO)))


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar) ; datos SINTETICOS")
    print(f"Masa reducida = {r['mu']:.2f} kg ; amortiguamiento relativo zeta = {r['zeta']:.3f}")
    print(f"Velocidad final: perseguidor = {r['v1']:.6f} m/s ; objetivo = {r['v2']:.6f} m/s ; comun teorica = {r['v_com']:.6f} m/s")
    print(f"Error de momento = {r['dp']:.2e}")
    print(f"Energia disipada = {r['e_dis']:.4f} J ; 1/2 mu v^2 = {r['e_teo']:.4f} J")
    print(f"Fuerza maxima simulada = {r['fmax']:.1f} N ; v sqrt(k mu) (sin amortiguar) = {r['f_teo']:.1f} N ; compresion sin amortiguar = {r['comp_max'] * 1000:.1f} mm")
    print(f"Momento de vuelco por desalineacion de {DESALINEO * 100:.0f} cm con la fuerza maxima = {r['torque']:.1f} N m ; angulo = {r['ang']:.2f} grados")
    assert r['dp'] < 1e-9
    assert abs(r['e_dis'] - r['e_teo']) / r['e_teo'] < 1e-6
    assert abs(r['v1'] - r['v_com']) < 1e-6 and abs(r['v2'] - r['v_com']) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
