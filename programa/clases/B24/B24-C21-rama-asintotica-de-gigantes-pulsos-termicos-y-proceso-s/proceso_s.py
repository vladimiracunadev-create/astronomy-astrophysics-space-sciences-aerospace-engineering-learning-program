#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C21: capturas lentas de neutrones (proceso s) y dragados en la fase AGB.

Datos: ninguno observado. Secciones eficaces relativas, flujo de neutrones, masas de dragado y
abundancias son valores SINTETICOS (ilustrativos), no de ningun isotopo ni modelo concreto.
Modelo: (1) cadena de capturas con la misma seccion eficaz: dN_i/dtau = N_(i-1) - N_i, con
tau = exposicion de neutrones integrada; solucion exacta de Poisson N_i = tau^i exp(-tau)/i!.
(2) flujo estacionario con secciones distintas: dN_i/dt = s_(i-1) N_(i-1) - s_i N_i con N_0 fijo; en
el estado estacionario s_i N_i = s_0 N_0 (el producto seccion x abundancia es constante).
(3) dragados: cada pulso lleva dM de material de la capa intermedia (fraccion de masa de C, O
fijas) a la envoltura; el carbono y el oxigeno totales se conservan; C/O por numero.
Supuestos: sin decaimientos beta ni ramificaciones; masa de la envoltura solo crece por el dragado
(sin perdida de masa). Validez: ilustrativa.
Tolerancia: 1e-8 entre RK4 y Poisson; 1e-4 en s_i N_i constante; 1e-12 en la conservacion de masa.
"""
from __future__ import annotations
import math
import platform
import sys


def rk4(f, y, dt, n):
    for _ in range(n):
        k1 = f(y)
        k2 = f([a + dt / 2 * b for a, b in zip(y, k1)])
        k3 = f([a + dt / 2 * b for a, b in zip(y, k2)])
        k4 = f([a + dt * b for a, b in zip(y, k3)])
        y = [a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(y, k1, k2, k3, k4)]
    return y


def poisson(i, tau):
    return tau ** i * math.exp(-tau) / math.factorial(i)


def cadena_igual(tau, n_esp=12, pasos=2000):
    def f(y):
        return [-y[0]] + [y[i - 1] - y[i] for i in range(1, len(y))]
    y0 = [1.0] + [0.0] * (n_esp - 1)
    return rk4(f, y0, tau / pasos, pasos)


def flujo_estacionario(sig, t_final=4000.0, dt=0.01):
    n = len(sig)

    def f(y):
        d = [0.0]                              # N_0 fijo
        for i in range(1, n):
            d.append(sig[i - 1] * y[i - 1] - sig[i] * y[i])
        return d
    y = [1.0] + [0.0] * (n - 1)
    return rk4(f, y, dt, int(t_final / dt))


def dragados(n_pulsos, dm=0.002, m_env=0.5, c0=0.003, o0=0.009, xc_dr=0.05, xo_dr=0.005):
    c, o, m = c0 * m_env, o0 * m_env, m_env
    hist = []
    for k in range(1, n_pulsos + 1):
        c += dm * xc_dr
        o += dm * xo_dr
        m += dm
        hist.append((k, (c / 12.0) / (o / 16.0), c / m))
    return c, o, m, hist


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    tau = 2.0
    y = cadena_igual(tau)
    err = max(abs(y[i] - (math.exp(-tau) if i == 0 else poisson(i, tau))) for i in range(len(y)))
    assert err < 1e-8, "RK4 no reproduce Poisson"
    imax = max(range(len(y)), key=lambda i: y[i])
    print(f"cadena igual (tau = {tau}): error maximo frente a Poisson = {err:.1e} ; maximo en N_{imax} = {y[imax]:.4f}")
    sig = [1.0, 0.5, 2.0, 0.1, 1.5, 0.8]
    ys = flujo_estacionario(sig)
    prods = [s * v for s, v in zip(sig, ys)]
    assert max(abs(p / prods[0] - 1) for p in prods) < 1e-4, "s_i N_i no constante"
    print("flujo estacionario: " + "  ".join(f"s{i}N{i}={p:.5f}" for i, p in enumerate(prods)))
    print("abundancias N_i = " + " ".join(f"{v:.3f}" for v in ys) + " (mayor abundancia donde la seccion es menor)")
    c, o, m, hist = dragados(40)
    c_ini, o_ini = 0.003 * 0.5, 0.009 * 0.5
    assert abs(c - (c_ini + 40 * 0.002 * 0.05)) < 1e-12 and abs(m - (0.5 + 40 * 0.002)) < 1e-12, "conservacion de masa"
    primer = next((k for k, r, _ in hist if r > 1.0), None)
    print(f"C/O inicial = {(c_ini / 12) / (o_ini / 16):.3f} ; tras 40 pulsos C/O = {hist[-1][1]:.3f} ; primer pulso con C/O > 1: {primer}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
