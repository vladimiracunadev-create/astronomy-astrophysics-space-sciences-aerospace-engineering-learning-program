#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C09: momento angular en una órbita y torque sobre un rotor.

Datos: GM = 3,9860e14 m³/s² y R = 6 378 137 m (NASA NSSDC, Earth Fact Sheet); condiciones
iniciales de la órbita elíptica y datos del rotor SINTÉTICOS. Modelo: gravedad puntual
central (fuerza central: el torque respecto del centro es cero), 2D, velocity-Verlet.
Supuestos: sin atmósfera ni achatamiento. Dominio de validez: pocas órbitas.
Tolerancias: el momento angular específico L = x vy - y vx varía menos de 1e-9
(relativo); el apoapsis integrado coincide con el analítico en 1e-3.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
R0 = 6_378_137.0 + 400_000.0

def acc(x: float, y: float) -> tuple[float, float]:
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3

def integrar(factor: float, n: int = 20_000):
    """Órbita con v0 = factor * v_circular en el periapsis (x = R0, y = 0)."""
    vc = math.sqrt(GM / R0)
    x, y, vx, vy = R0, 0.0, 0.0, factor * vc
    eps = 0.5 * vy * vy - GM / R0
    a_sm = -GM / (2 * eps)
    T = 2 * math.pi * math.sqrt(a_sm**3 / GM)
    dt = T / n
    ax, ay = acc(x, y)
    L0 = x * vy - y * vx
    rmax, dL = R0, 0.0
    for _ in range(n):
        vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
        x += vx * dt; y += vy * dt
        ax, ay = acc(x, y)
        vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
        rmax = max(rmax, math.hypot(x, y))
        dL = max(dL, abs((x * vy - y * vx) - L0) / L0)
    return L0, eps, T, rmax, dL

def apoapsis_analitico(L: float, eps: float) -> float:
    d = math.sqrt(GM**2 + 2 * eps * L**2)
    r1, r2 = (-GM + d) / (2 * eps), (-GM - d) / (2 * eps)
    return max(r1, r2)

def main() -> int:
    L0, eps, T, rmax, dL = integrar(1.10)
    ra = apoapsis_analitico(L0, eps)
    assert dL < 1e-9, dL
    assert abs(rmax - ra) / ra < 1e-3, (rmax, ra)
    # velocidad areolar constante: dA/dt = L/2 (segunda ley de Kepler) = área elipse / T
    a_sm = (R0 + ra) / 2
    e = (ra - R0) / (ra + R0)
    area = math.pi * a_sm * a_sm * math.sqrt(1 - e * e)
    assert abs(area / T - L0 / 2) / (L0 / 2) < 1e-6
    vp = 1.10 * math.sqrt(GM / R0)
    va = L0 / ra
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Orbita elíptica (v0 = 1,10 v_c): periapsis = {R0/1e3:.1f} km, apoapsis = {ra/1e3:.1f} km (integrado {rmax/1e3:.1f} km), e = {e:.4f}")
    print(f"Momento angular específico L = {L0:.6e} m²/s (variación máxima {dL:.1e}); velocidad areolar L/2 = {L0/2:.6e} m²/s")
    print(f"v_periapsis = {vp:.1f} m/s, v_apoapsis = {va:.1f} m/s; semieje mayor = {a_sm/1e3:.1f} km; T = {T:.1f} s = {T/60:.2f} min")
    # Satélite circular (1000 kg): momento angular
    m = 1000.0
    vc = math.sqrt(GM / R0)
    print(f"Satélite circular: L = m r v = {m*R0*vc:.4e} kg·m²/s")
    # Rotor sintético: I = 200 kg m², torque 0,05 N m durante 600 s
    I, tau, t = 200.0, 0.05, 600.0
    w = tau * t / I
    assert abs(I * w - tau * t) < 1e-12
    print(f"Rotor sintético: tau = {tau} N·m, I = {I:.0f} kg·m², t = {t:.0f} s -> w = {w:.3f} rad/s ({w*60/(2*math.pi):.2f} rpm)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
