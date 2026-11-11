#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C08: oscilador circadiano arrastrado por luz (modelo DIDACTICO de fase, SINTETICO).

Ecuacion de Adler para la diferencia de fase theta entre el reloj interno y el ciclo de luz: d theta/dt = d_omega - K sin(theta), con
d_omega = 2 pi/tau - 2 pi/T (rad/h), tau = 24.2 h (periodo intrinseco, ILUSTRATIVO) y T el periodo del ciclo de luz; K (rad/h) la fuerza de arrastre.
Arrastre (bloqueo de fase) si |d_omega| <= K; si no, deriva con periodo de batido 2 pi/sqrt(d_omega^2 - K^2). K = 0.01 rad/h (ILUSTRATIVO).
Una estacion en orbita baja da ~15.5 amaneceres por dia (periodo orbital ~92.7 min, valor de orden de magnitud, no consultado aqui); se calcula aparte.
Integracion con Euler dt = 0.05 h durante 2000 h. Sin datos medidos. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

TAU, K = 24.2, 0.01


def d_omega(t_luz):
    return 2 * np.pi / TAU - 2 * np.pi / t_luz


def simular(t_luz, horas=2000.0, dt=0.05):
    th = 1.0
    n = int(horas / dt)
    for _ in range(n):
        th += dt * (d_omega(t_luz) - K * np.sin(th))
    # tras el transitorio: la diferencia de fase esta bloqueada si su variacion en la ultima hora es ~0
    th2 = th
    for _ in range(int(1.0 / dt)):
        th2 += dt * (d_omega(t_luz) - K * np.sin(th2))
    return abs(th2 - th) / 1.0


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: tau = 24.2 h y K = 0.01 rad/h; sin mediciones")
    lo = 2 * np.pi / (2 * np.pi / TAU + K)
    hi = 2 * np.pi / (2 * np.pi / TAU - K)
    print(f"Intervalo de arrastre analitico: T de {lo:.2f} h a {hi:.2f} h (|d_omega| <= K)")
    print("T de la luz [h]   |d_omega| [rad/h]   deriva final [rad/h]   resultado   periodo de batido analitico [h]")
    ok = {}
    for t_luz in (20.0, 22.0, 23.0, 24.0, 24.2, 25.0, 26.0, 28.0):
        dw = abs(d_omega(t_luz))
        deriva = simular(t_luz)
        bloq = deriva < 1e-3
        ok[t_luz] = bloq
        beat = "-" if dw <= K else f"{2 * np.pi / np.sqrt(dw ** 2 - K ** 2):7.1f}"
        print(f"  {t_luz:6.1f}          {dw:8.4f}            {deriva:9.5f}            {'arrastrado' if bloq else 'deriva    '}   {beat}")
    t_orb = 92.7 / 60
    dw_orb = abs(d_omega(t_orb))
    print(f"Ciclo orbital: {24 / t_orb:.2f} amaneceres/dia (T = {t_orb:.3f} h); |d_omega| = {dw_orb:.2f} rad/h >> K = {K}: no hay arrastre")
    print(f"Desfase de 6 h entre el reloj y la luz = {2 * np.pi * 6 / 24:.3f} rad = {np.degrees(2 * np.pi * 6 / 24):.0f} grados")
    # reajuste tras un salto de fase de 6 h con T = 24 h
    th, dt, t = 2 * np.pi * 6 / 24, 0.05, 0.0
    while abs(th) > 0.05 and t < 20000:
        th += dt * (d_omega(24.0) - K * np.sin(th)); t += dt
    print(f"Tras un salto de fase de 6 h con T = 24 h, el reloj se realinea (|theta| < 0.05 rad) en {t:.0f} h = {t / 24:.1f} dias")
    assert ok[24.0] and ok[24.2] and ok[25.0] and not ok[20.0] and not ok[26.0] and not ok[23.0]
    assert abs(lo - 23.30) < 0.05 and abs(hi - 25.17) < 0.05
    assert dw_orb > 10 * K
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
