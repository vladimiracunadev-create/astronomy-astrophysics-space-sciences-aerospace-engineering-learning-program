#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C04: factor de arreglo de un arreglo lineal uniforme, nulos, lobulos laterales, ponderacion, direccionamiento y errores de fase.

Datos: ninguna constante fisica. El numero de elementos (8), la separacion (0,5 lambda), los pesos (uniforme, Hann, Hamming), el angulo de direccionamiento (30 grados) y el error de fase de 10 grados
rms son ILUSTRATIVOS; elementos isotropicos e identicos. Simulacion con semilla 20261109.
Modelo: AF(u) = sum_n w_n exp(j k d n (u - u0)), con u = sin(theta) medido desde la normal. Para pesos uniformes, forma cerrada |AF|/N = |sin(N psi/2)/(N sin(psi/2))|, psi = k d (u - u0). Primer nulo en
u - u0 = lambda/(N d). Directividad en la direccion del haz: D = (sum w)^2 / sum w^2 para d = lambda/2 y elementos isotropicos (aproximacion exacta en la normal). Error de fase gaussiano e independiente:
potencia en el pico = exp(-s^2) + (1 - exp(-s^2))/N, con s en radianes.
Supuestos: sin acoplamiento mutuo, sin efecto del patron del elemento, ponderaciones fijas, banda estrecha. Validez: direccionamiento hasta unos 60 grados de la normal.
Tolerancia: suma directa de fasores frente a la forma cerrada a 1e-12; nulos en las posiciones teoricas a 1e-9; media simulada de la potencia con error de fase frente a la teoria a 1,5 % (4000 pruebas).
"""
from __future__ import annotations
import cmath, math, platform, random


def af(w, d_lam, u, u0=0.0):
    n = len(w)
    return sum(w[k] * cmath.exp(2j * math.pi * d_lam * k * (u - u0)) for k in range(n))


def af_cerrada(n, d_lam, u, u0=0.0):
    psi = 2 * math.pi * d_lam * (u - u0)
    s = math.sin(psi / 2)
    if abs(s) < 1e-14:
        return 1.0
    return abs(math.sin(n * psi / 2) / (n * s))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = 8
    d = 0.5
    unif = [1.0] * n
    hann = [0.5 - 0.5 * math.cos(2 * math.pi * (k + 1) / (n + 1)) for k in range(n)]
    hamm = [0.54 - 0.46 * math.cos(2 * math.pi * k / (n - 1)) for k in range(n)]
    pesos = {"uniforme": unif, "Hann": hann, "Hamming": hamm}
    # 1. fasores frente a forma cerrada
    maxdif = 0.0
    for i in range(0, 2001):
        u = -1 + 2 * i / 2000
        a = abs(af(unif, d, u)) / n
        b = af_cerrada(n, d, u)
        maxdif = max(maxdif, abs(a - b))
    print(f"Maxima diferencia entre suma de fasores y forma cerrada (N = {n}, d = 0,5 lambda, 2001 puntos): {maxdif:.2e}")
    assert maxdif < 1e-12
    # 2. nulos
    print("Nulos del arreglo uniforme: u_m = m lambda/(N d)")
    for m in (1, 2, 3):
        u = m / (n * d)
        th = math.degrees(math.asin(u))
        val = abs(af(unif, d, u))
        print(f"  m = {m}: u = {u:.5f} ; theta = {th:.3f} grados ; |AF| = {val:.2e}")
        assert val < 1e-9
    # 3. anchos y lobulos laterales por barrido fino
    print(f"{'pesos':>9} {'HPBW (grados)':>14} {'1er nulo (grados)':>18} {'lobulo lateral (dB)':>20} {'D (dBi)':>8} {'eficiencia':>11}")
    resumen = {}
    for nombre, w in pesos.items():
        pico = abs(af(w, d, 0.0))
        npts = 40001
        u = [i / (npts - 1) for i in range(npts)]
        v = [abs(af(w, d, x)) / pico for x in u]
        # ancho a media potencia
        i3 = next(i for i, y in enumerate(v) if y < 1 / math.sqrt(2))
        t3 = math.degrees(math.asin(u[i3]))
        hp = 2 * t3
        # primer minimo local y maximo lateral posterior
        imin = next(i for i in range(1, npts - 1) if v[i] <= v[i - 1] and v[i] < v[i + 1])
        lat = max(v[imin:])
        sl = 20 * math.log10(lat)
        sw2 = sum(x * x for x in w)
        dd = sum(w) ** 2 / sw2
        ef = dd / n
        resumen[nombre] = (hp, math.degrees(math.asin(u[imin])), sl, dd, ef)
        print(f"{nombre:>9} {hp:14.3f} {math.degrees(math.asin(u[imin])):18.3f} {sl:20.3f} {10 * math.log10(dd):8.3f} {ef:11.4f}")
    assert abs(resumen["uniforme"][2] - (-12.9)) < 0.3
    assert resumen["Hann"][2] < resumen["Hamming"][2] + 20 and resumen["Hann"][2] < resumen["uniforme"][2]
    assert abs(resumen["uniforme"][3] - n) < 1e-9
    # 4. direccionamiento
    th0 = 30.0
    u0 = math.sin(math.radians(th0))
    pico = max(abs(af(unif, d, x / 20000, u0)) for x in range(-20000, 20001))
    kmax = max(range(-20000, 20001), key=lambda x: abs(af(unif, d, x / 20000, u0)))
    thp = math.degrees(math.asin(kmax / 20000))
    # ensanchamiento por proyeccion 1/cos
    def hpbw(u0_):
        pk = abs(af(unif, d, u0_, u0_))
        xs = [u0_ + i * 1e-5 for i in range(0, 200000)]
        for x in xs:
            if abs(af(unif, d, x, u0_)) < pk / math.sqrt(2):
                break
        return x - u0_
    h0 = hpbw(0.0)
    h30 = hpbw(u0)
    print(f"Direccionamiento a {th0} grados: pico en {thp:.4f} grados ; ancho en u identico ({h30:.5f} = {h0:.5f}) ; ancho angular crece como 1/cos: {math.degrees(2 * h30 / math.cos(math.radians(th0))):.3f} grados")
    assert abs(thp - th0) < 0.01
    assert abs(h30 - h0) < 2e-5
    # 5. rejillas (lobulos de rejilla) para d = lambda
    grat = [x for x in (-1.0, 0.0, 1.0) if abs(af(unif, 1.0, x)) / n > 0.999999]
    media = [x for x in (-1.0, 0.0, 1.0) if abs(af(unif, 0.5, x)) / n > 0.999999]
    print(f"Maximos principales en u = -1, 0, 1: con d = 1 lambda en u = {grat} (lobulos de rejilla en +-1); con d = 0,5 lambda solo en u = {media}")
    assert grat == [-1.0, 0.0, 1.0] and media == [0.0]
    # 6. errores de fase
    rng = random.Random(20261109)
    s_deg = 10.0
    s = math.radians(s_deg)
    trials = 4000
    acc = 0.0
    for _ in range(trials):
        w = [cmath.exp(1j * rng.gauss(0, s)) for _ in range(n)]
        acc += abs(sum(w)) ** 2 / n ** 2
    sim = acc / trials
    teo = math.exp(-s * s) + (1 - math.exp(-s * s)) / n
    print(f"Error de fase {s_deg} grados rms en {n} elementos: potencia relativa en el pico simulada = {sim:.5f} ; teoria = {teo:.5f} ; perdida = {-10 * math.log10(sim):.4f} dB")
    assert abs(sim / teo - 1) < 0.015
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
