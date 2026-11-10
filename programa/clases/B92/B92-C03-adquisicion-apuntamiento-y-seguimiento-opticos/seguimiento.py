#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C03: tiempo de adquisicion por barrido y jitter residual de un lazo de seguimiento.

Datos consultados (2026-11-10): c = 299792458 m/s (NIST, CODATA 2022). Como contexto, el experimento LCRD adquiere
con una baliza de cuatro haces de mas de 200 urad y un detector de cuadrantes ("coarse track"), y pasa a "fine track"
con un haz de unos 20 urad (Israel et al., SPIE 2024, NTRS 20230018608). No entran en el calculo.
ILUSTRATIVOS (sinteticos, no medidos): incertidumbre de +-500 urad, distancia 45 000 km, divergencia de la baliza
50..400 urad, tiempo de reposo = tiempo de ida y vuelta + 10 ms; perturbacion S_d(f) = A/f^2 entre 1 y 1000 Hz con
A = 100 urad^2 Hz; ruido del sensor 0.05 urad/sqrt(Hz); divergencia del haz fino 12.355 urad.
Modelo: barrido en rejilla cuadrada con paso rho sqrt(2) (circulos de radio rho que cubren la rejilla);
N = ceil(2 u / (rho sqrt 2))^2; T = N (t_ida_vuelta + 10 ms). Lazo de primer orden con ancho de banda fc:
sensibilidad |S|^2 = f^2/(f^2+fc^2); varianza residual = (A/fc)[atan(f2/fc) - atan(f1/fc)]; ruido: N0^2 pi fc / 2.
Segunda via: cobertura por Monte Carlo (random.Random(92), 20000 puntos) e integracion numerica de Simpson en escala logaritmica.
Tolerancia: integral numerica frente a analitica 1e-8 relativa; cobertura exacta 1.0 con la rejilla N y menor que 1 con una rejilla 2 filas mas pequena.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
U = 500e-6
R = 45000e3
A = 100.0       # urad^2 Hz
N0 = 0.05       # urad/sqrt(Hz)
F1, F2 = 1.0, 1000.0
TH = 12.355     # urad


def n_barrido(u, rho, k=1.0):
    return math.ceil(2.0 * u / (k * rho * math.sqrt(2.0))) ** 2


def cobertura_mc(u, rho, m, n=20000):
    """Fraccion de puntos aleatorios del cuadrado [-u,u]^2 a distancia <= rho del centro de su celda (rejilla m x m)."""
    rng = random.Random(92)
    s = 2.0 * u / m
    cubierto = 0
    for _ in range(n):
        x, y = rng.uniform(-u, u), rng.uniform(-u, u)
        i = min(m - 1, int((x + u) / s)); j = min(m - 1, int((y + u) / s))
        if math.hypot(x - (-u + (i + 0.5) * s), y - (-u + (j + 0.5) * s)) <= rho:
            cubierto += 1
    return cubierto / n


def var_dist(fc):
    return (A / fc) * (math.atan(F2 / fc) - math.atan(F1 / fc))


def var_dist_num(fc, n=4000):
    a, b = math.log(F1), math.log(F2)
    h = (b - a) / n
    f = lambda x: (A / math.exp(x) ** 2) * (math.exp(x) ** 2 / (math.exp(x) ** 2 + fc ** 2)) * math.exp(x)
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def var_ruido(fc):
    return N0 ** 2 * math.pi * fc / 2.0


def total(fc):
    return var_dist(fc) + var_ruido(fc)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    tviaje = 2.0 * R / C
    print(f"Tiempo de ida y vuelta a 45000 km (ILUSTRATIVO) = {tviaje * 1e3:.2f} ms ; reposo por posicion = {(tviaje + 0.010) * 1e3:.2f} ms")
    print("Barrido de +-500 urad con baliza de divergencia rho (circulos de radio rho):")
    for rho in (50e-6, 100e-6, 200e-6, 400e-6):
        n = n_barrido(U, rho)
        print(f"  rho = {rho * 1e6:5.0f} urad  N = {n:4d}  T = {n * (tviaje + 0.010):8.2f} s")
    m_ok = int(math.sqrt(n_barrido(U, 100e-6)))
    cob_ok = cobertura_mc(U, 100e-6, m_ok)
    cob_mal = cobertura_mc(U, 100e-6, m_ok - 2)
    print(f"Cobertura Monte Carlo (rho = 100 urad): rejilla {m_ok}x{m_ok} = {cob_ok:.4f} ; rejilla {m_ok - 2}x{m_ok - 2} = {cob_mal:.4f}")
    print(f"Perturbacion en lazo abierto (sin control) entre 1 y 1000 Hz: sigma = {math.sqrt(A * (1 / F1 - 1 / F2)):.3f} urad")
    print("Lazo de primer orden: fc, sigma_perturbacion, sigma_ruido, sigma_total [urad] ; perdida media con theta = 12.355 urad")
    dmax = 0.0
    for fc in (10.0, 30.0, 100.0, 300.0, 900.0):
        vd = var_dist(fc)
        dmax = max(dmax, abs(vd - var_dist_num(fc)) / vd)
        vt = total(fc)
        perd = 1.0 / (1.0 + 4.0 * vt / TH ** 2)
        print(f"  fc = {fc:6.1f} Hz  {math.sqrt(vd):7.4f}  {math.sqrt(var_ruido(fc)):7.4f}  {math.sqrt(vt):7.4f}  perdida = {-10 * math.log10(perd):.4f} dB")
    lo, hi = 1.0, 900.0
    for _ in range(100):
        m1 = lo + (hi - lo) / 3.0; m2 = hi - (hi - lo) / 3.0
        if total(m1) < total(m2): hi = m2
        else: lo = m1
    fo = 0.5 * (lo + hi)
    malla = min((total(10 ** (k / 1000.0)), 10 ** (k / 1000.0)) for k in range(0, 2951))
    print(f"fc optimo (busqueda ternaria) = {fo:.2f} Hz ; sigma_total = {math.sqrt(total(fo)):.4f} urad ; malla fina: {malla[1]:.2f} Hz")
    print(f"Diferencia relativa maxima integral numerica frente a analitica = {dmax:.2e}")
    assert dmax < 1e-8
    assert cob_ok == 1.0 and cob_mal < 1.0
    assert abs(fo - malla[1]) / fo < 5e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
