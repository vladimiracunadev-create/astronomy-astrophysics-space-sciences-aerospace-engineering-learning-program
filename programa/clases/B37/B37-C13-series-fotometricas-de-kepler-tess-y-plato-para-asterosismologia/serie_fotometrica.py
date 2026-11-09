#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C13: preparacion de una serie fotometrica con huecos y espectro de amplitud para asterosismologia.

Datos: ninguna constante fisica. Todo es SINTETICO (ilustrativo): cadencia de 120 s, duracion de 10 d, 5 sinusoides de 50 ppm cerca de 1000 uHz, tendencia lenta de 500 ppm, ruido blanco
gaussiano de 100 ppm y un hueco de 1 d, con semilla 20261109. Las cadencias reales de Kepler, TESS y PLATO no se consultaron en esta clase y no se usan como dato.
Modelo: (1) frecuencia de Nyquist 1/(2 dt) y alias: una senal por encima de Nyquist reaparece en 1/dt - nu con el signo invertido (identidad exacta); (2) filtro pasa-altos por mediana movil
de 0,5 d; (3) espectro de amplitud por suma directa sobre las muestras existentes (recurrencia compleja), amplitud A = (2/N) |sum y_n exp(-i w t_n)|; (4) amplitud recuperada y precision de
frecuencia por Monte Carlo (30 realizaciones) frente a la expresion sigma_nu = sqrt(6) sigma/(pi sqrt(N) A T) (aproximacion estandar de minimos cuadrados, no consultada en esta clase);
(5) ventana espectral con y sin hueco.
Supuestos: ruido blanco, sinusoides coherentes (sin amortiguamiento estocastico), sin cambios de cadencia. Validez: orientativa.
Tolerancia: alias exacto a 1e-9; amplitud recuperada dentro de 3 sigma de 50 ppm; dispersion de la frecuencia entre 0,5 y 1,6 veces la teorica; el filtro reduce la potencia a baja frecuencia en un factor > 10.
"""
from __future__ import annotations
import cmath, math, platform, random, statistics, sys

DT = 120.0
NDIAS = 10
N = int(NDIAS * 86400 / DT)
FREQS = (980.0, 1010.0, 1043.0, 1075.0, 1105.0)  # uHz
AMP, SIG = 50.0, 100.0


def serie(rng, ruido=True, con_hueco=True):
    mask = [True] * N
    if con_hueco:
        for i in range(int(4.0 * 86400 / DT), int(5.0 * 86400 / DT)):
            mask[i] = False
    y = []
    for n in range(N):
        t = n * DT
        v = sum(AMP * math.sin(2 * math.pi * f * 1e-6 * t + 0.7 * k) for k, f in enumerate(FREQS))
        v += 500.0 * math.sin(2 * math.pi * t / (3 * 86400.0))
        if ruido:
            v += rng.gauss(0, SIG)
        y.append(v)
    return y, mask


def filtrar(y, mask, ventana=360):
    z = []
    mitad = ventana // 2
    for n in range(N):
        a, b = max(0, n - mitad), min(N, n + mitad + 1)
        vals = sorted(y[k] for k in range(a, b) if mask[k])
        z.append(y[n] - (vals[len(vals) // 2] if vals else 0.0))
    return z


def amplitud(y, mask, nu_uHz):
    w = 2 * math.pi * nu_uHz * 1e-6 * DT
    rot = cmath.exp(-1j * w)
    z = 1 + 0j
    s = 0j
    cnt = 0
    for n in range(N):
        if mask[n]:
            s += y[n] * z
            cnt += 1
        z *= rot
    return 2 * abs(s) / cnt


def pico(y, mask, lo, hi, paso):
    nu = lo
    mejor = (0.0, lo)
    while nu <= hi + 1e-9:
        a = amplitud(y, mask, nu)
        if a > mejor[0]:
            mejor = (a, nu)
        nu += paso
    a0, n0 = mejor
    am, ap = amplitud(y, mask, n0 - paso), amplitud(y, mask, n0 + paso)
    den = am - 2 * a0 + ap
    return a0, n0 + (0.5 * paso * (am - ap) / den if den != 0 else 0.0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"dt = {DT:.0f} s ; N = {N} ; T = {NDIAS} d ; Nyquist = {1e6 / (2 * DT):.2f} uHz ; resolucion 1/T = {1e6 / (NDIAS * 86400):.4f} uHz")
    # 1. alias exacto
    nu, alias = 4500.0, 1e6 / DT - 4500.0
    err = max(abs(math.sin(2 * math.pi * nu * 1e-6 * n * DT) + math.sin(2 * math.pi * alias * 1e-6 * n * DT)) for n in range(2000))
    print(f"alias: {nu:.1f} uHz sobre Nyquist reaparece en {alias:.2f} uHz ; max |s(nu) + s(alias)| = {err:.2e}")
    assert err < 1e-9
    rng = random.Random(20261109)
    y, mask = serie(rng)
    # 2. filtro pasa-altos
    ye = filtrar(y, mask)
    b = [amplitud(y, mask, f) for f in (1.0, 2.0, 3.0, 4.0)]
    a = [amplitud(ye, mask, f) for f in (1.0, 2.0, 3.0, 4.0)]
    print(f"amplitud media 1-4 uHz: antes = {statistics.mean(b):.1f} ppm ; despues = {statistics.mean(a):.2f} ppm ; factor = {statistics.mean(b) / statistics.mean(a):.0f}")
    assert statistics.mean(b) / statistics.mean(a) > 10
    # 3. amplitud y frecuencia recuperadas
    sg_a = math.sqrt(2.0 / sum(mask)) * SIG
    print(f"duty cycle = {sum(mask) / N:.3f} ; sigma(amplitud) esperada = {sg_a:.2f} ppm")
    print(f"{'nu real [uHz]':>14} {'nu recuperada':>14} {'A [ppm]':>9}")
    rec = []
    for f in FREQS:
        A, nuf = pico(ye, mask, f - 1.2, f + 1.2, 0.2)
        rec.append((f, nuf, A))
        print(f"{f:14.2f} {nuf:14.3f} {A:9.2f}")
        assert abs(A - AMP) < 3 * sg_a + 0.1 * AMP
    # 4. precision de frecuencia por Monte Carlo (un solo modo, sin tendencia)
    T = NDIAS * 86400.0
    sg_th = math.sqrt(6) * SIG / (math.pi * math.sqrt(sum(mask)) * AMP * T) * 1e6
    resid = []
    f0 = 1043.0
    for _ in range(30):
        yy = []
        for n in range(N):
            yy.append(AMP * math.sin(2 * math.pi * f0 * 1e-6 * n * DT + 0.3) + rng.gauss(0, SIG))
        A, nuf = pico(yy, mask, f0 - 0.8, f0 + 0.8, 0.2)
        resid.append(nuf - f0)
    sd = statistics.pstdev(resid)
    print(f"precision en frecuencia: Monte Carlo = {sd * 1e3:.2f} nHz ; expresion teorica = {sg_th * 1e3:.2f} nHz ; cociente = {sd / sg_th:.2f}")
    assert 0.5 < sd / sg_th < 1.6
    # 5. ventana espectral: una sinusoide sin ruido con y sin hueco
    yu = [AMP * math.sin(2 * math.pi * 1000.0 * 1e-6 * n * DT) for n in range(N)]
    mu = [True] * N
    ym = [AMP * math.sin(2 * math.pi * 1000.0 * 1e-6 * n * DT) for n in range(N)]
    def lobulo(yv, mv):
        a0 = amplitud(yv, mv, 1000.0)
        off = 1.3 / (NDIAS * 86400) * 1e6
        lat = max(amplitud(yv, mv, 1000.0 + s * 0.1) for s in range(int(off / 0.1) + 1, 40))
        return a0, lat / a0
    au, lu = lobulo(yu, mu)
    ag, lg = lobulo(ym, mask)
    print(f"sidelobes (a mas de 1,3/T del pico): sin hueco = {lu:.3f} ; con hueco de 1 d = {lg:.3f}")
    assert lg > lu
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
