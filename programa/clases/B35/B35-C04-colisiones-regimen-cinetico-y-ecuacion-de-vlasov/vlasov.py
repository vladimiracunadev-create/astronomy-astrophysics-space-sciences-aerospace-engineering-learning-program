#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C04: parametros de plasma no colisional y amortiguamiento de Landau por la ecuacion de Vlasov linealizada.

Datos: k_B, e, m_e, eps_0 (NIST CODATA 2022, tabla allascii.txt) y la unidad astronomica 149 597 870 700 m (valor recordado, NO consultado en esta clase). Las densidades y temperaturas de los tres plasmas
(viento solar a 1 au, ionosfera, descarga de laboratorio) son ILUSTRATIVAS (sinteticas); no son mediciones.
Modelo: (1) longitud de Debye, parametro de plasma y frecuencia de colision de Spitzer nu_ei = (4 sqrt(2 pi)/3) n e^4 lnL / ((4 pi eps0)^2 m^(1/2) (kT)^(3/2)) con lnL = ln(12 pi n lD^3),
camino libre medio v_t/nu y numero de Knudsen frente a una longitud L (formula estandar escrita aqui; NO se consulto una fuente); (2) ecuacion de Vlasov-Poisson linealizada para electrones,
d(df)/dt + i k v df = -v F0 E, i k E = -integral(df) dv, integrada con Runge-Kutta de cuarto orden sobre una malla de velocidad (unidades wp = 1, vt = 1);
(3) segunda via independiente: raiz de la relacion de dispersion 1 + (1 + zeta Z(zeta))/k^2 = 0 con Z por su serie entera, resuelta con el metodo de la secante complejo.
Supuestos: electrones con iones inmoviles, F0 maxwelliana, amplitud pequena. Validez: lineal; la malla en v (|v| < 8, 321 puntos) limita la prueba al tiempo de recurrencia 2 pi/(k dv).
Tolerancia: tasa de amortiguamiento y frecuencia de la simulacion frente a la raiz con error relativo < 3 %.
"""
from __future__ import annotations
import cmath, math, platform, sys

K_B = 1.380649e-23
E_Q = 1.602176634e-19
M_E = 9.1093837139e-31
EPS0 = 8.8541878188e-12
AU = 149597870700.0

def parametros(n, T, L):
    lD = math.sqrt(EPS0 * K_B * T / (n * E_Q ** 2))
    ND = (4 * math.pi / 3) * n * lD ** 3
    lnL = math.log(12 * math.pi * n * lD ** 3)
    nu = (4 * math.sqrt(2 * math.pi) / 3) * n * E_Q ** 4 * lnL / ((4 * math.pi * EPS0) ** 2 * math.sqrt(M_E) * (K_B * T) ** 1.5)
    vt = math.sqrt(K_B * T / M_E)
    lam = vt / nu
    return lD, ND, lnL, nu, lam, lam / L

def Z(z):
    s = 0j; t = 1.0 + 0j; n = 0
    while True:
        s += t
        n += 1
        t = t * (-2 * z * z) / (2 * n + 1)
        if abs(t) < 1e-18 and n > 5:
            break
    return 1j * math.sqrt(math.pi) * cmath.exp(-z * z) - 2 * z * s

def raiz_dispersion(k, w0):
    def eps(w):
        z = w / (math.sqrt(2) * k)
        return 1 + (1 + z * Z(z)) / (k * k)
    a, b = w0, w0 + 0.01 - 0.01j
    fa, fb = eps(a), eps(b)
    for _ in range(100):
        c = b - fb * (b - a) / (fb - fa)
        a, fa = b, fb
        b, fb = c, eps(c)
        if abs(b - a) < 1e-13:
            break
    return b

def vlasov_lineal(k, tf=22.0, dt=0.02, nv=321, vmax=8.0):
    dv = 2 * vmax / (nv - 1)
    v = [-vmax + i * dv for i in range(nv)]
    F0 = [math.exp(-x * x / 2) / math.sqrt(2 * math.pi) for x in v]
    alpha = 1e-3
    df = [complex(alpha * f) for f in F0]
    def campo(d):
        # integral trapezoidal (las colas son despreciables)
        return 1j / k * (sum(d) * dv)
    def deriv(d):
        E = campo(d)
        return [-1j * k * v[i] * d[i] - v[i] * F0[i] * E for i in range(nv)], E
    t = 0.0
    serie = [(0.0, abs(campo(df)))]
    for paso in range(int(round(tf / dt))):
        k1, _ = deriv(df)
        k2, _ = deriv([df[i] + 0.5 * dt * k1[i] for i in range(nv)])
        k3, _ = deriv([df[i] + 0.5 * dt * k2[i] for i in range(nv)])
        k4, _ = deriv([df[i] + dt * k3[i] for i in range(nv)])
        df = [df[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(nv)]
        t += dt
        serie.append((t, abs(campo(df))))
    return serie

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'plasma':>14} {'lambda_D [m]':>13} {'N_D':>10} {'lnL':>6} {'nu [1/s]':>11} {'camino [m]':>11} {'Kn=lambda/L':>12}")
    casos = (("viento solar", 5e6, 1e5, AU), ("ionosfera F", 1e12, 1e3, 1e5), ("descarga lab", 1e20, 23200.0, 0.1))
    res = {}
    for nombre, n, T, L in casos:
        lD, ND, lnL, nu, lam, Kn = parametros(n, T, L)
        res[nombre] = (lD, ND, lnL, nu, lam, Kn)
        print(f"{nombre:>14} {lD:13.4g} {ND:10.3g} {lnL:6.2f} {nu:11.4g} {lam:11.4g} {Kn:12.4g}")
    # coeficiente practico de la formula: nu = c * n[cm^-3] lnL T[eV]^-1.5
    n, T = 5e6, 1e5
    lD, ND, lnL, nu, lam, Kn = res["viento solar"]
    TeV = K_B * T / E_Q
    c = nu / (5.0 * lnL * TeV ** -1.5)
    print(f"coeficiente practico = {c:.3e} s^-1 (referencia recordada, no consultada: 2.9e-6)")
    assert abs(c / 2.9e-6 - 1) < 0.03
    assert res["viento solar"][5] > 0.1 and res["ionosfera F"][5] < 1e-2 and res["descarga lab"][5] < 1e-2
    assert all(r[1] > 100 for r in res.values())
    # Landau
    k = 0.5
    w = raiz_dispersion(k, 1.4 - 0.1j)
    print(f"relacion de dispersion (k lD = {k}): omega = {w.real:.5f} {w.imag:+.5f} i wp")
    serie = vlasov_lineal(k)
    picos = [(serie[i][0], serie[i][1]) for i in range(1, len(serie) - 1) if serie[i][1] > serie[i - 1][1] and serie[i][1] >= serie[i + 1][1] and serie[i][0] > 1.0]
    print(f"{'t_pico [1/wp]':>14} {'|E| pico':>12}")
    for tp, ap in picos:
        print(f"{tp:14.2f} {ap:12.4e}")
    # ajuste por minimos cuadrados de ln|E| frente a t
    xs = [p[0] for p in picos]; ys = [math.log(p[1]) for p in picos]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    gam = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    # frecuencia: el modulo tiene picos cada pi/omega
    dts = [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
    wr = math.pi / (sum(dts) / len(dts))
    print(f"simulacion: gamma = {gam:.5f} ; omega_r = {wr:.4f}  (raiz: {w.imag:.5f}; {w.real:.4f})")
    assert abs(gam / w.imag - 1) < 0.03 and abs(wr / w.real - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
