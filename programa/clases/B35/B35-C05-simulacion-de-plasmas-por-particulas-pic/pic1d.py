#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C05: codigo PIC electrostatico 1D (salto de rana, ponderacion CIC, Poisson espectral) validado con dos casos analiticos.

Datos: ninguna constante fisica ni dato observado. Unidades normalizadas (frecuencia de plasma wp = 1, carga -1 y masa 1 por electron, densidad media 1, iones fijos y uniformes); todos los
parametros numericos (celdas, particulas, paso, amplitudes) son ILUSTRATIVOS (sinteticos). Semilla fija 20261109 (solo para la fase aleatoria de la perturbacion: el resto es un inicio ordenado).
Modelo: ecuacion de Poisson dE/dx = 1 - n(x) resuelta en Fourier; particulas avanzadas con v(t+dt/2) = v(t-dt/2) - E(x) dt, x(t+dt) = x + v dt; ponderacion lineal (cloud-in-cell) para depositar y para
interpolar el campo.
Casos de prueba: (A) oscilacion fria de plasma, frecuencia analitica wp = 1; (B) inestabilidad de dos haces frios simetricos (v0 = 1) con k v0 = sqrt(3/8) wp, tasa analitica gamma = wp/(2 sqrt 2)
(deducida en la clase B35-C03).
Supuestos: electrostatico, 1D, periodico; sin colisiones. Validez: ilustrativa, para ensenar el metodo (no es un codigo de investigacion).
Tolerancia: frecuencia de oscilacion con error < 2 %; deriva de energia < 1 % en (A); tasa de crecimiento con error < 12 % en (B); conservacion del momento total < 1e-9 en (A).
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def simular(L, nx, x, v, dt, pasos, modo_extra=None):
    Np = len(x); dx = L / nx; w = L / Np
    ks = [2 * math.pi * m / L for m in range(1, nx // 2)]
    tw = [[cmath.exp(-1j * 2 * math.pi * m * j / nx) for j in range(nx)] for m in range(1, nx // 2)]
    def campo(x):
        n = [0.0] * nx
        for xi in x:
            s = xi / dx
            j = int(s); f = s - j
            n[j % nx] += (1 - f)
            n[(j + 1) % nx] += f
        n = [c * w / dx for c in n]
        rho = [1.0 - c for c in n]
        E = [0.0] * nx
        Ek = []
        for idx, m in enumerate(range(1, nx // 2)):
            rk = sum(rho[j] * tw[idx][j] for j in range(nx)) / nx
            Ek.append(rk / (1j * ks[idx]))
        for j in range(nx):
            E[j] = 2 * sum((Ek[idx] * tw[idx][j].conjugate()).real for idx in range(len(ks)))
        return E, Ek
    def gather(E, x):
        out = []
        for xi in x:
            s = xi / dx; j = int(s); f = s - j
            out.append((1 - f) * E[j % nx] + f * E[(j + 1) % nx])
        return out
    E, Ek = campo(x)
    Ep = gather(E, x)
    v = [v[i] + 0.5 * dt * Ep[i] for i in range(Np)]  # v(-dt/2)
    hist = []
    for p in range(pasos + 1):
        E, Ek = campo(x)
        Ep = gather(E, x)
        ec = 0.5 * w * sum((v[i] - 0.5 * dt * Ep[i]) ** 2 for i in range(Np))  # v(t) aproximada
        ef = 0.5 * dx * sum(e * e for e in E)
        hist.append((p * dt, abs(Ek[0]) * 2, ec, ef, w * sum(v)))
        v = [v[i] - dt * Ep[i] for i in range(Np)]
        x = [(x[i] + dt * v[i]) % L for i in range(Np)]
    return hist

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    # (A) oscilacion fria
    L, nx, Np, dt = 2 * math.pi / 0.5, 32, 4000, 0.1
    k = 2 * math.pi / L
    x0 = [(i + 0.5) * L / Np for i in range(Np)]
    d = 0.01
    x = [(xi + d * math.sin(k * xi)) % L for xi in x0]
    v = [0.0] * Np
    h = simular(L, nx, x, v, dt, 100)
    # periodo por cruces por cero del modo 1 con signo: usamos el campo en el modulo y su minimo
    amp = [a[1] for a in h]
    # el modulo |E1| ~ |cos wt|: sus minimos ocurren en t = (n + 1/2) pi/w ; localizamos minimos locales
    mins = []
    for i in range(1, len(amp) - 1):
        if amp[i] <= amp[i - 1] and amp[i] < amp[i + 1]:
            # refinar con parabola
            y0, y1, y2 = amp[i - 1], amp[i], amp[i + 1]
            o = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
            mins.append((i + o) * dt)
    sep = [mins[i + 1] - mins[i] for i in range(len(mins) - 1)]
    omega = math.pi / (sum(sep) / len(sep))
    et = [a[2] + a[3] for a in h]
    deriva = (max(et) - min(et)) / (sum(et) / len(et))
    pmax = max(abs(a[4]) for a in h)
    print(f"(A) oscilacion fria: omega medida = {omega:.5f} wp ; deriva relativa de energia = {deriva:.2e} ; |momento total| maximo = {pmax:.1e}")
    print(f"    amplitud |E1| inicial = {amp[0]:.5f} (analitica d*1 = {d:.5f} en E = d)")
    assert abs(omega - 1) < 0.02 and deriva < 0.01 and pmax < 1e-9
    assert abs(amp[0] / d - 1) < 0.02
    # (B) dos haces
    k = math.sqrt(3 / 8)
    L = 2 * math.pi / k
    Np, dt = 6000, 0.1
    mitad = Np // 2
    xa = [(i + 0.25) * L / mitad for i in range(mitad)]
    xb = [(i + 0.75) * L / mitad for i in range(mitad)]
    fase = rng.uniform(0, 2 * math.pi)
    d = 1e-3
    x = [(xi + d * math.sin(k * xi + fase)) % L for xi in xa + xb]
    v = [1.0] * mitad + [-1.0] * mitad
    h = simular(L, 32, x, v, dt, 220)
    print(f"{'t [1/wp]':>9} {'|E1|':>12} {'E_campo':>12}")
    for a in h[::20]:
        print(f"{a[0]:9.1f} {a[1]:12.4e} {a[3]:12.4e}")
    # ajuste de ln|E1| en la ventana de crecimiento lineal: 1e-3*pico < |E1| < 0.1*pico_max... usar fraccion del maximo
    emax = max(a[1] for a in h)
    ven = [(a[0], math.log(a[1])) for a in h if a[0] > 6 and 0.003 * emax < a[1] < 0.2 * emax and a[0] < h[max(range(len(h)), key=lambda i: h[i][1])][0]]
    xs = [p[0] for p in ven]; ys = [p[1] for p in ven]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    gam = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    g_an = 1 / (2 * math.sqrt(2))
    print(f"(B) dos haces: ventana t = [{xs[0]:.1f}, {xs[-1]:.1f}] ({len(xs)} puntos) ; gamma medida = {gam:.4f} ; gamma analitica = {g_an:.4f} ; cociente = {gam/g_an:.3f}")
    assert len(xs) >= 20 and abs(gam / g_an - 1) < 0.12
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
