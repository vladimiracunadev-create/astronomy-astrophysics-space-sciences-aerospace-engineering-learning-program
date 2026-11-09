#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C21: presupuesto de fotones de una estrella guia natural, magnitud limite y cobertura de cielo.

Datos: TODOS los numeros astrofotometricos son ILUSTRATIVOS y NO provienen de una fuente consultada: flujo de punto cero de 1,0e10 fotones/s/m^2 (banda ancha), eficiencia total de 0,30, subapertura de 0,20 m,
trama de 2 ms, mancha gaussiana de sigma 0,85 px (FWHM 2,0 px), ventana de 4 x 4 px, ruido de lectura de 3 e-, y una ley de cuentas de estrellas rho(<m) = 0,5 * 10^(0,3 (m - 15)) por minuto de arco cuadrado (no es un
catalogo ni una latitud galactica concreta). Semilla 20261109. Sin catalogos reales.
Modelo: fotones por subapertura y trama N = F0 10^(-0,4 m) d^2 T eta ; error del centroide sigma_c = sqrt((sigma^2 + 1/12)/N + sigma_r^2 sum(x-c)^2 / N^2) (clase C14) ; la magnitud limite es aquella en que
sigma_c = 0,2 FWHM. Cobertura: el numero de estrellas mas brillantes que m dentro de un disco de radio theta es Poisson con media rho(<m) pi theta^2, de modo que P(al menos una) = 1 - exp(-rho pi theta^2).
Vias independientes: Monte Carlo de la mancha (4000 repeticiones) frente a la formula en la magnitud limite ; Monte Carlo de campos Poisson (20000) frente a 1 - exp(-media).
Supuestos: estrella puntual, sin fondo de cielo, densidad uniforme (en la realidad depende de la latitud galactica). Validez: orden de magnitud pedagogico.
Tolerancia: sigma_c del Monte Carlo a 8 % de la formula ; cobertura Monte Carlo a 0,01 de la analitica.
"""
from __future__ import annotations
import math, platform, random

F0 = 1.0e10
ETA = 0.30
D_SUB = 0.20
T = 0.002
SIG = 0.85
SR = 3.0
SUMA = 4 * sum((k + 0.5 - 2) ** 2 for k in range(4))   # sum (x-c)^2 en 4 x 4 con c = 0
FWHM = 2.0

def fotones(m):
    return F0 * 10 ** (-0.4 * m) * D_SUB ** 2 * T * ETA

def sigma_c(n):
    return math.sqrt((SIG ** 2 + 1 / 12) / n + SR ** 2 * SUMA / n ** 2)

def poisson(rnd, lam):
    l = math.exp(-lam)
    k, p = 0, 1.0
    while True:
        p *= rnd.random()
        if p <= l:
            return k
        k += 1

def mc_centroide(rnd, n_ph, reps):
    """Devuelve (sigma con el flujo conocido, sigma con el denominador ruidoso)."""
    W = 4
    v_fijo, v_ruid = [], []
    for _ in range(reps):
        img = [[0.0] * W for _ in range(W)]
        dentro = 0
        for _ in range(int(n_ph)):
            x = rnd.gauss(0, SIG) + W / 2
            y = rnd.gauss(0, SIG) + W / 2
            i, j = int(math.floor(y)), int(math.floor(x))
            if 0 <= i < W and 0 <= j < W:
                img[i][j] += 1
                dentro += 1
        for i in range(W):
            for j in range(W):
                img[i][j] += rnd.gauss(0, SR)
        num = sum((j + 0.5 - W / 2) * img[i][j] for i in range(W) for j in range(W))
        v_fijo.append(num / dentro)
        v_ruid.append(num / sum(sum(r) for r in img))
    def sd(v):
        mu = sum(v) / len(v)
        return math.sqrt(sum((a - mu) ** 2 for a in v) / (len(v) - 1))
    return sd(v_fijo), sd(v_ruid)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    print(f"{'m':>5} {'fotones/subap./trama':>21} {'sigma_c [px]':>13} {'sigma_c/FWHM':>13}")
    for m in (8, 10, 11, 12, 13, 14):
        n = fotones(m)
        print(f"{m:5.1f} {n:21.1f} {sigma_c(n):13.4f} {sigma_c(n) / FWHM:13.4f}")
    # magnitud limite por biseccion
    lo, hi = 5.0, 20.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sigma_c(fotones(mid)) < 0.2 * FWHM:
            lo = mid
        else:
            hi = mid
    mlim = 0.5 * (lo + hi)
    nlim = fotones(mlim)
    print(f"magnitud limite (sigma_c = 0,2 FWHM = {0.2 * FWHM:.2f} px) = {mlim:.3f} ; fotones por subapertura y trama = {nlim:.1f}")
    assert abs(sigma_c(nlim) - 0.2 * FWHM) < 1e-9
    # Monte Carlo en el limite (mas fotones enteros, ruido de lectura incluido)
    mc, mc_r = mc_centroide(rnd, round(nlim), 4000)
    print(f"Monte Carlo en la magnitud limite (flujo conocido): sigma_c = {mc:.4f} px ; formula con N = {round(nlim)}: {sigma_c(round(nlim)):.4f} px")
    print(f"con el denominador ruidoso sum(I) (flujo desconocido) la dispersion sube a {mc_r:.3f} px: a pocos fotones el cociente tiene valores atipicos y la formula de primer orden no vale")
    assert abs(mc / sigma_c(round(nlim)) - 1) < 0.08
    assert mc_r > 3 * mc
    # cada magnitud mas debil reduce los fotones por 2,512
    assert abs(fotones(10) / fotones(11) - 10 ** 0.4) < 1e-9
    # cobertura de cielo
    rho = lambda m: 0.5 * 10 ** (0.3 * (m - 15))
    print(f"densidad acumulada en la magnitud limite: {rho(mlim):.4f} estrellas/arcmin^2")
    print(f"{'theta [arcsec]':>14} {'media':>8} {'P analitica':>12} {'P Monte Carlo':>14}")
    for th in (15, 30, 60):
        area = math.pi * (th / 60.0) ** 2
        media = rho(mlim) * area
        pa = 1 - math.exp(-media)
        nmc = 20000
        pm = sum(1 for _ in range(nmc) if poisson(rnd, media) >= 1) / nmc
        print(f"{th:14d} {media:8.4f} {pa:12.4f} {pm:14.4f}")
        assert abs(pm - pa) < 0.01, (th, pm, pa)
    # cobertura frente a la magnitud limite para theta = 30 arcsec
    print(f"{'m limite':>8} {'cobertura (theta=30 arcsec)':>28}")
    prev = -1.0
    for m in (10, 12, 14, 16, 18):
        c = 1 - math.exp(-rho(m) * math.pi * 0.5 ** 2)
        print(f"{m:8d} {c:28.4f}")
        assert c > prev
        prev = c
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
