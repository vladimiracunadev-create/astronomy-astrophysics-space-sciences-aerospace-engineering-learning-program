#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C07: conservacion del flujo en MHD ideal, difusion resistiva y numero de enlace (helicidad).

Datos: ninguna constante fisica ni dato observado. Todo esta en unidades normalizadas y los perfiles (campo, flujo de compresion, resistividad, geometria de los anillos) son ILUSTRATIVOS (sinteticos).
Modelo: (1) ecuacion de induccion 1D con B = B(x) z y v = v(x) x: dB/dt + d(vB)/dx = 0, con v = -a x (compresion). Se integra con volumenes finitos contra el viento (primer orden) y se compara con la
solucion analitica por caracteristicas B(x,t) = exp(a t) B0(x exp(a t)); el flujo entre dos puntos materiales x_i(t) = x_i(0) exp(-a t) debe conservarse.
(2) Difusion resistiva dB/dt = eta d2B/dx2 (FTCS) frente a la solucion gaussiana exacta de anchura sigma^2 = sigma0^2 + 2 eta t.
(3) Numero de enlace de Gauss de dos circunferencias (enlazadas y no enlazadas) por integracion doble; la helicidad de dos tubos delgados de flujos F1 y F2 es K = 2 Lk F1 F2 (relacion teorica no consultada).
Supuestos: 1D para (1) y (2); curvas cerradas simples para (3). Validez: ilustrativa.
Tolerancia: error maximo relativo del campo < 2 %; deriva del flujo material < 5e-3 (difusion numerica del esquema de primer orden); difusion con error maximo < 1e-3 del pico; numero de enlace a 1e-4 de un entero.
"""
from __future__ import annotations
import math, platform, sys

def B0(x):
    return 1.0 + 0.8 * math.exp(-x * x / 2)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # (1) compresion
    a, tf = 0.2, 3.0
    xmin, xmax, N = -10.0, 10.0, 400
    dx = (xmax - xmin) / N
    xc = [xmin + (i + 0.5) * dx for i in range(N)]
    dt = 0.02
    B = [B0(x) for x in xc]
    pasos = int(round(tf / dt))
    t = 0.0
    for _ in range(pasos):
        # flujos en las caras con upwind; condicion de entrada analitica en los bordes
        Bf = [0.0] * (N + 1)
        for i in range(N + 1):
            xf = xmin + i * dx
            vf = -a * xf
            if i == 0:
                Bu = math.exp(a * t) * B0(xf * math.exp(a * t))
            elif i == N:
                Bu = math.exp(a * t) * B0(xf * math.exp(a * t))
            else:
                Bu = B[i - 1] if vf > 0 else B[i]
            Bf[i] = vf * Bu
        B = [B[i] - dt / dx * (Bf[i + 1] - Bf[i]) for i in range(N)]
        t += dt
    ex = [math.exp(a * t) * B0(x * math.exp(a * t)) for x in xc]
    err = max(abs(B[i] - ex[i]) / ex[i] for i in range(N))
    x1, x2 = -2.0, 3.0
    x1f, x2f = x1 * math.exp(-a * t), x2 * math.exp(-a * t)
    def flujo(xa, xb):
        return sum(B[i] * dx for i in range(N) if xa <= xc[i] < xb)
    # integral con medios bines para precisar: interpolamos con fraccion de celda
    def flujo_precisa(xa, xb):
        s = 0.0
        for i in range(N):
            lo, hi = xc[i] - dx / 2, xc[i] + dx / 2
            ov = max(0.0, min(hi, xb) - max(lo, xa))
            s += B[i] * ov
        return s
    F0 = sum(B0(x1 + (j + 0.5) * (x2 - x1) / 4000) for j in range(4000)) * (x2 - x1) / 4000
    Ft = flujo_precisa(x1f, x2f)
    print(f"(1) t = {t:.2f} ; error relativo maximo del campo = {err:.2e} ; flujo inicial = {F0:.5f} ; flujo entre los puntos materiales = {Ft:.5f} ; deriva = {abs(Ft/F0-1):.2e}")
    print(f"    intervalo material: [{x1:.1f}, {x2:.1f}] -> [{x1f:.4f}, {x2f:.4f}] ; B maximo = {max(B):.4f} (analitico {max(ex):.4f})")
    assert err < 0.02 and abs(Ft / F0 - 1) < 5e-3
    # (2) difusion
    eta, s0, tf2 = 1.0, 1.0, 2.0
    Nd, L = 400, 20.0
    dxd = L / Nd
    xd = [-L / 2 + (i + 0.5) * dxd for i in range(Nd)]
    Bd = [math.exp(-x * x / (2 * s0 * s0)) for x in xd]
    dtd = 0.2 * dxd * dxd / eta
    n = int(round(tf2 / dtd)); dtd = tf2 / n
    for _ in range(n):
        Bd = [Bd[i] + eta * dtd / dxd ** 2 * (Bd[(i + 1) % Nd] - 2 * Bd[i] + Bd[i - 1]) for i in range(Nd)]
    s2 = s0 * s0 + 2 * eta * tf2
    ed = [s0 / math.sqrt(s2) * math.exp(-x * x / (2 * s2)) for x in xd]
    errd = max(abs(Bd[i] - ed[i]) for i in range(Nd))
    area0 = sum(math.exp(-x * x / (2 * s0 * s0)) for x in xd) * dxd
    area1 = sum(Bd) * dxd
    print(f"(2) difusion: pico numerico = {max(Bd):.5f} ; analitico = {s0/math.sqrt(s2):.5f} ; error maximo = {errd:.2e} ; flujo total conservado: {area1/area0:.8f}")
    assert errd < 1e-3 and abs(area1 / area0 - 1) < 1e-9
    # (3) numero de enlace
    def gauss_lk(c2x, M=240):
        s = 0.0
        h = 2 * math.pi / M
        for i in range(M):
            th = i * h
            p1 = (math.cos(th), math.sin(th), 0.0)
            d1 = (-math.sin(th) * h, math.cos(th) * h, 0.0)
            for j in range(M):
                ph = j * h
                p2 = (c2x + math.cos(ph), 0.0, math.sin(ph))
                d2 = (-math.sin(ph) * h, 0.0, math.cos(ph) * h)
                r = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
                cx = (d1[1] * d2[2] - d1[2] * d2[1], d1[2] * d2[0] - d1[0] * d2[2], d1[0] * d2[1] - d1[1] * d2[0])
                den = (r[0] ** 2 + r[1] ** 2 + r[2] ** 2) ** 1.5
                s += (r[0] * cx[0] + r[1] * cx[1] + r[2] * cx[2]) / den
        return s / (4 * math.pi)
    lk_enl = gauss_lk(1.0)
    lk_no = gauss_lk(3.0)
    print(f"(3) numero de enlace de Gauss: anillos enlazados Lk = {lk_enl:.6f} ; anillos separados Lk = {lk_no:.6f}")
    F1 = F2 = 1.0
    print(f"    helicidad de dos tubos delgados K = 2 Lk F1 F2 = {2*abs(round(lk_enl))*F1*F2:.1f} (enlazados) y {2*abs(round(lk_no))*F1*F2:.1f} (separados), en unidades de F^2")
    assert abs(abs(lk_enl) - 1) < 1e-4 and abs(lk_no) < 1e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
