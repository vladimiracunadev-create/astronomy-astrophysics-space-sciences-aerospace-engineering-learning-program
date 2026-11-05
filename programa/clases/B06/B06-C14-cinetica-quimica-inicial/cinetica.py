#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C14: cinética de primer orden y ecuación de Arrhenius.

Datos: la reacción A -> productos con k = 0,010 1/s, E_a = 50 kJ/mol y el factor
preexponencial 1e9 1/s son SINTÉTICOS (ilustrativos), no corresponden a una
sustancia real. R = 8,314 462 618 J/(mol K) (CODATA 2022). La edad del universo
usada solo como escala (13,8 mil millones de años) sale de B01-C01 de este programa.
Modelo: dA/dt = -k A (primer orden), solución A = A0 exp(-k t); k = A_f exp(-Ea/(R T)).
Supuestos: temperatura constante, un solo paso elemental, sin reacción inversa.
Dominio de validez: ilustración del modelo; no predice una reacción real.
Tolerancias: integración RK4 frente a la solución analítica dentro de 1e-9 relativo
con paso k*dt = 0,01.
"""

from __future__ import annotations

import math
import sys

R = 8.314462618
K1 = 0.010                 # 1/s (sintético)
EA, AF = 50_000.0, 1e9     # J/mol, 1/s (sintéticos)
EDAD_UNIVERSO_S = 13.8e9 * 365.25 * 86_400


def concentracion(a0: float, k: float, t: float) -> float:
    return a0 * math.exp(-k * t)


def vida_media(k: float) -> float:
    return math.log(2) / k


def arrhenius(T: float, ea: float = EA, a: float = AF) -> float:
    return a * math.exp(-ea / (R * T))


def rk4(a0: float, k: float, t_fin: float, pasos: int) -> float:
    h, y = t_fin / pasos, a0
    f = lambda v: -k * v
    for _ in range(pasos):
        k1 = f(y); k2 = f(y + h * k1 / 2); k3 = f(y + h * k2 / 2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def euler(a0: float, k: float, t_fin: float, pasos: int) -> float:
    h, y = t_fin / pasos, a0
    for _ in range(pasos):
        y += h * (-k * y)
    return y


def pruebas() -> None:
    # la concentración cae a la mitad en una vida media y a 1/8 en tres
    assert abs(concentracion(1.0, K1, vida_media(K1)) - 0.5) < 1e-12
    assert abs(concentracion(1.0, K1, 3 * vida_media(K1)) - 0.125) < 1e-12
    # RK4 frente a la solución analítica
    t = 5 * vida_media(K1)
    ref = concentracion(1.0, K1, t)
    assert abs(rk4(1.0, K1, t, int(K1 * t / 0.01)) - ref) / ref < 1e-9
    # Arrhenius: a Ea = 0 la velocidad no depende de T
    assert abs(arrhenius(300.0, 0.0) - arrhenius(10.0, 0.0)) < 1e-9
    # k crece con T
    assert arrhenius(310.0) > arrhenius(300.0)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    th = vida_media(K1)
    print(f"k = {K1} 1/s ; vida media = {th:.2f} s ; fracción restante a 100 s = {concentracion(1, K1, 100):.4f} ; "
          f"tiempo hasta 1 % = {math.log(100) / K1:.1f} s")
    t5 = 5 * th
    print(f"A los 5 t_1/2: analítica {concentracion(1, K1, t5):.6f} ; RK4 {rk4(1, K1, t5, int(K1 * t5 / 0.01)):.6f}")
    print(f"Euler con 10 pasos hasta t = 1/k: {euler(1, K1, 1 / K1, 10):.4f} frente a {math.exp(-1):.4f} "
          f"(error {100 * (euler(1, K1, 1 / K1, 10) / math.exp(-1) - 1):.1f} %)")
    for T in (300.0, 310.0, 214.0, 10.0):
        k = arrhenius(T)
        print(f"T = {T:5.0f} K : k = {k:.3e} 1/s ; vida media = {vida_media(k):.3e} s")
    print(f"k(310)/k(300) con Ea = 50 kJ/mol: {arrhenius(310.0) / arrhenius(300.0):.2f} ; "
          f"con Ea = 100 kJ/mol: {arrhenius(310.0, 100_000.0) / arrhenius(300.0, 100_000.0):.2f}")
    print(f"Vida media a 10 K / edad del universo = {vida_media(arrhenius(10.0)) / EDAD_UNIVERSO_S:.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
