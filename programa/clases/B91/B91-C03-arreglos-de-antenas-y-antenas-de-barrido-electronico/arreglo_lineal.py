#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C03: arreglo lineal uniforme con barrido electronico.

Sin datos publicados consultados: todo es CALCULO sobre un arreglo SINTETICO (N elementos, separacion d en longitudes de onda).
Modelo: factor de arreglo AF(theta) = sum_n exp(j n (k d (sin theta - sin theta0) )), con theta medido desde la normal (broadside);
elementos isotropos; la perdida de barrido 10 log cos(theta0) es un modelo ILUSTRATIVO de elemento con U ~ cos(theta), no se calcula por integracion.
Segunda via: forma cerrada |AF| = |sin(N psi/2) / sin(psi/2)|, psi = k d (sin theta - sin theta0); directividad de isotropos con d = lambda/2 igual a N.
Tolerancias: suma directa frente a forma cerrada < 1e-9; directividad numerica frente a N < 1e-3 relativa.
Cuantizacion de fase: desfasadores de b bits, error uniforme en [-pi/2^b, +pi/2^b] (aleatorio con semilla fija 91).
"""
from __future__ import annotations
import cmath, math, platform, random


def af_suma(n, d, th_deg, th0_deg):
    psi = 2 * math.pi * d * (math.sin(math.radians(th_deg)) - math.sin(math.radians(th0_deg)))
    return abs(sum(cmath.exp(1j * k * psi) for k in range(n)))


def af_cerrada(n, d, th_deg, th0_deg):
    psi = 2 * math.pi * d * (math.sin(math.radians(th_deg)) - math.sin(math.radians(th0_deg)))
    s = math.sin(psi / 2)
    return float(n) if abs(s) < 1e-12 else abs(math.sin(n * psi / 2) / s)


def directividad(n, d, th0_deg, pasos=20000):
    """D = 4 pi U_max / int U dOmega con U = |AF|^2 * elem(theta); haz en el plano (simetria azimutal NO supuesta: arreglo sobre eje x, 'theta' en el plano del arreglo,
    integracion sobre el cono alrededor del eje del arreglo: u = sin(theta) -> dOmega = 2 pi du)."""
    # integral sobre u = cos(angulo respecto del eje del arreglo) en [-1, 1]; AF depende solo de u: psi = k d (u - u0)
    u0 = math.sin(math.radians(th0_deg))
    def f(u):
        psi = 2 * math.pi * d * (u - u0)
        s = math.sin(psi / 2)
        af2 = float(n * n) if abs(s) < 1e-12 else (math.sin(n * psi / 2) / s) ** 2
        return af2
    h = 2.0 / pasos
    tot = f(-1) + f(1)
    for i in range(1, pasos):
        tot += (4 if i % 2 else 2) * f(-1 + i * h)
    integral = 2 * math.pi * tot * h / 3
    umax = max(f(u0), 1e-30)
    return 4 * math.pi * umax / integral


def hpbw(n, d, th0_deg):
    """Ancho de media potencia por biseccion sobre la forma cerrada."""
    pico = n * n
    def g(th):
        return af_cerrada(n, d, th, th0_deg) ** 2 / pico - 0.5
    paso = 0.002
    a = th0_deg
    while g(a + paso) > 0 and a < 89.9:
        a += paso
    b = th0_deg
    while g(b - paso) > 0 and b > -89.9:
        b -= paso
    return a - b


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, d = 16, 0.5
    mx = max(abs(af_suma(n, d, t, 20) - af_cerrada(n, d, t, 20)) for t in range(-89, 90))
    print(f"Arreglo SINTETICO N = {n}, d = {d} lambda. Suma directa frente a forma cerrada: error maximo = {mx:.2e}")
    assert mx < 1e-9
    dn = directividad(n, d, 0)
    print(f"Directividad broadside (isotropos): D = {dn:.4f}  (N = {n}); {10*math.log10(dn):.2f} dBi")
    assert abs(dn - n) / n < 1e-3
    print("Barrido: ancho de haz y perdida de barrido por proyeccion de la apertura (perdida = 10 log cos theta0, modelo ILUSTRATIVO de elemento con U ~ cos theta)")
    print(" theta0 [deg]  HPBW [deg]  HPBW*cos(th0) [deg]  D_isotropos  perdida_proyeccion [dB]")
    for th0 in (0, 20, 40, 60):
        hp = hpbw(n, d, th0)
        di = directividad(n, d, th0)
        print(f" {th0:8d}      {hp:8.3f}     {hp*math.cos(math.radians(th0)):10.3f}          {di:8.3f}     {10*math.log10(math.cos(math.radians(th0))):8.3f}")
    print("  HPBW*cos(theta0) casi constante: el haz se ensancha como 1/cos(theta0). La directividad de isotropos no cae, la del elemento real si (ver teoria).")
    print("Lobulos de rejilla: condicion d/lambda <= 1/(1 + |sin theta0|)")
    for dd in (0.5, 0.6, 0.8):
        for th0 in (0, 30, 60):
            lim = 1 / (1 + math.sin(math.radians(th0)))
            # busqueda numerica de un maximo secundario de nivel ~ pico fuera del lobulo principal
            pico_sec = max(af_cerrada(n, dd, t / 10, th0) for t in range(-899, 900) if abs(t / 10 - th0) > 12)
            hay = pico_sec > 0.9 * n
            print(f"   d = {dd:.1f} lambda, theta0 = {th0:2d} deg: limite {lim:.3f}; lobulo de rejilla {'SI' if hay else 'no'} (maximo fuera del haz = {pico_sec/n:.3f} del pico)")
            assert hay == (dd > lim + 1e-9) or abs(dd - lim) < 0.02
    print("Cuantizacion de fase (semilla 91, 400 repeticiones, theta0 = 30 deg):")
    rnd = random.Random(91)
    print("  bits   perdida de ganancia media [dB]   sinc^2 teorico [dB]")
    for bits in (2, 3, 4, 6):
        q = math.pi / 2 ** bits
        acc = 0.0
        for _ in range(400):
            tot = sum(cmath.exp(1j * rnd.uniform(-q, q)) for _ in range(n))
            acc += abs(tot) ** 2 / (n * n)
        teo = (math.sin(q) / q) ** 2
        print(f"  {bits:4d}        {10*math.log10(acc/400):8.4f}                   {10*math.log10(teo):8.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
