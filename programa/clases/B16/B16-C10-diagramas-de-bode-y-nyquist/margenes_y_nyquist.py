#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C10: respuesta en frecuencia, márgenes y criterio de Nyquist.

Datos: SINTÉTICOS (parámetros normalizados). L(s) = K / (s (s + 1)(s + 2)).
Modelo: L(j w); módulo en dB = 20 log10 |L|, fase en grados.
Referencias independientes:
  - frecuencia de cruce de fase: w_pc = sqrt(2) rad/s, con |L(j w_pc)| = K/6,
    luego el margen de ganancia es 6/K (coincide con K_crit = 6 de C08);
  - criterio de Nyquist: Z = N + P con P = 0 (L no tiene polos en el
    semiplano derecho), N = vueltas horarias de 1 + L(s) en torno a 0, contadas
    numéricamente sobre el contorno de Nyquist con indentación en el origen;
    Z debe coincidir con el número de raíces inestables de Routh/np.roots.
Supuestos: LTI, sin retardo. Tolerancia: 1e-9 en los cruces; conteo exacto.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
from scipy.optimize import brentq


def L(s, K):
    return K / (s * (s + 1) * (s + 2))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def fase_deg(w, K):
    return np.degrees(np.unwrap(np.angle(L(1j * np.asarray(w, float), K))))


def margenes(K):
    gc = lambda w: abs(L(1j * w, K)) - 1.0
    wgc = brentq(gc, 1e-3, 100.0)
    ph = np.degrees(np.angle(L(1j * wgc, K)))
    pm = 180.0 + ph if ph <= 0 else ph - 180.0
    wpc = brentq(lambda w: np.imag(L(1j * w, K)), 0.5, 5.0)     # parte imaginaria nula
    gm = 1.0 / abs(L(1j * wpc, K))
    return wgc, pm, wpc, gm


def vueltas_zeros(K, eps=1e-3, R=1e3, n=40001):
    """Z = ceros de 1+L en el semiplano derecho = -(vueltas antihorarias de 1+L)."""
    t1 = np.linspace(-R, -eps, n); s1 = 1j * t1                       # eje imaginario negativo
    f2 = np.linspace(-np.pi / 2, np.pi / 2, n); s2 = eps * np.exp(1j * f2)   # indentación por la derecha
    t3 = np.linspace(eps, R, n); s3 = 1j * t3
    f4 = np.linspace(np.pi / 2, -np.pi / 2, n); s4 = R * np.exp(1j * f4)     # arco grande, horario
    s = np.concatenate([s1, s2, s3, s4])
    F = 1.0 + L(s, K)
    d = np.unwrap(np.angle(F))
    giro = (d[-1] - d[0]) / (2 * np.pi)
    return int(round(-giro))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    print("  K    w_gc    MF (grados)   w_pc     MG       MG (dB)   Z (Nyquist)   raíces inestables")
    for K in (0.5, 1.0, 2.0, 4.0, 5.5):
        wgc, pm, wpc, gm = margenes(K)
        Z = vueltas_zeros(K)
        inest = int(np.sum(np.roots([1, 3, 2, K]).real > 0))
        print(f"{K:5.1f}  {wgc:6.4f}  {pm:9.2f}    {wpc:6.4f}  {gm:7.4f}  {20*math.log10(gm):8.2f}   {Z:6d}        {inest:6d}")
        prueba(abs(wpc - math.sqrt(2)) < 1e-9, "w_pc")
        prueba(abs(gm - 6.0 / K) < 1e-9, "MG = 6/K")
        prueba(Z == inest == 0, "estable")
    for K in (6.5, 8.0, 20.0):
        Z = vueltas_zeros(K)
        inest = int(np.sum(np.roots([1, 3, 2, K]).real > 0))
        gm = margenes(K)[3]
        print(f"{K:5.1f}  (inestable)       MG = {gm:6.4f} < 1   Z (Nyquist) = {Z}   raíces inestables = {inest}")
        prueba(Z == inest == 2 and gm < 1, "inestable")
    # fase en la frecuencia de cruce de fase, para K = 2
    fase = fase_deg(np.linspace(1e-3, math.sqrt(2), 20001), 2.0)[-1]
    print(f"fase de L (continua desde w -> 0) en w = sqrt(2): {fase:.6f} grados")
    prueba(abs(fase + 180.0) < 1e-6, "fase -180")
    # margen de retardo: el retardo adicional que consume el margen de fase
    wgc, pm, _, _ = margenes(1.0)
    print(f"K = 1: margen de retardo ≈ MF/(180/pi)/w_gc = {math.radians(pm)/wgc:.3f} s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
