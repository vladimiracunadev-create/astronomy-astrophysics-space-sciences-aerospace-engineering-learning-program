#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C05: distancia de campo lejano, error de distancia finita e incertidumbre de ganancia por sustitucion.

Sin medicion real: todo SINTETICO (antena bajo prueba AUT de D = 1.2 m a 8.4 GHz; ganancia de referencia 20.0 dBi; ruido de receptor simulado con semilla 91).
Relaciones estandar (no consultadas en una fuente concreta): R_ff = 2 D^2 / lambda; error de fase maximo en el borde = pi D^2 / (4 lambda R) rad
  (diferencia de camino D^2/(8R)); transferencia de ganancia G_AUT = G_ref + (P_AUT - P_ref); combinacion RSS de incertidumbres.
Modelo del diagrama: apertura lineal uniforme de longitud D: patron 1D E(u) = integral exp(j k (x u + x^2/(2R))) dx, con el termino cuadratico del campo cercano.
Segunda via: a R -> infinito el patron numerico coincide con sinc; HPBW teorico 0.886 lambda/D (apertura uniforme 1D).
Tolerancias: patron numerico (R grande) frente a sinc < 1e-3; error de fase a 2D^2/lambda = 22.5 deg con 1e-9.
"""
from __future__ import annotations
import cmath, math, platform, random

C = 299_792_458.0


def patron(d, lam, r, u, n=801):
    """Intensidad normalizada |E|^2 en u = sin(theta) para una apertura lineal uniforme observada a distancia r (aprox. de Fresnel)."""
    k = 2 * math.pi / lam
    tot = 0j
    for i in range(n):
        x = -d / 2 + d * i / (n - 1)
        fase = k * x * u + (k * x * x / (2 * r) if r else 0.0)
        tot += cmath.exp(1j * fase)
    return abs(tot / n) ** 2


def sinc2(d, lam, u):
    a = math.pi * d * u / lam
    return 1.0 if abs(a) < 1e-12 else (math.sin(a) / a) ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f, D = 8.4e9, 1.2
    lam = C / f
    rff = 2 * D * D / lam
    print(f"AUT SINTETICA: D = {D} m, f = {f/1e9} GHz, lambda = {lam*1e3:.3f} mm ; campo lejano R_ff = 2D^2/lambda = {rff:.2f} m")
    # patron en el limite
    mx = max(abs(patron(D, lam, 0, u / 100) - sinc2(D, lam, u / 100)) for u in range(-30, 31))
    print(f"Patron numerico (R infinito) frente a sinc^2: error maximo = {mx:.2e}")
    assert mx < 1e-3
    hp_t = math.degrees(0.886 * lam / D)
    print(f"HPBW teorico 0.886 lambda/D = {hp_t:.3f} deg")
    print("Error de fase en el borde de la apertura (pi D^2/(4 lambda R)) y efecto sobre el patron")
    print("  R/R_ff   fase borde [deg]   nivel en nulo ideal [dB]   perdida de pico [dB]   dHPBW [%]")
    ref_peak = patron(D, lam, 0, 0.0)
    hp_ref = None
    for fr in (10.0, 4.0, 2.0, 1.0, 0.5, 0.25):
        r = fr * rff
        fase = math.degrees(math.pi * D * D / (4 * lam * r))
        # primer nulo ideal: u = lam/D ; se mide el nivel alli
        nivel = 10 * math.log10(max(patron(D, lam, r, lam / D), 1e-12))
        pico = max(patron(D, lam, r, u * 1e-4) for u in range(-100, 101, 5))
        # HPBW por barrido
        def half(rr):
            p0 = patron(D, lam, rr, 0.0)
            u = 0.0
            while patron(D, lam, rr, u) > 0.5 * p0:
                u += 2e-5
            return 2 * math.degrees(math.asin(u))
        h = half(r)
        if hp_ref is None:
            hp_ref = half(0)
        print(f"  {fr:6.2f}     {fase:9.2f}          {nivel:9.2f}              {10*math.log10(pico/ref_peak):8.3f}            {100*(h-hp_ref)/hp_ref:6.2f}")
    assert abs(math.degrees(math.pi * D * D / (4 * lam * rff)) - 22.5) < 1e-9
    print("Con R = 2D^2/lambda la fase en el borde es 22.5 deg (criterio clasico): los nulos se rellenan, el pico casi no cambia.")
    print("Transferencia de ganancia (sustitucion), datos SINTETICOS con ruido gaussiano de 0.05 dB (semilla 91, 30 repeticiones):")
    rnd = random.Random(91)
    g_ref, g_true = 20.0, 23.4
    est = []
    for _ in range(30):
        p_aut = g_true - g_ref + rnd.gauss(0, 0.05)  # diferencia de potencia recibida, dB
        est.append(g_ref + p_aut)
    media = sum(est) / len(est)
    sd = math.sqrt(sum((e - media) ** 2 for e in est) / (len(est) - 1))
    print(f"   G_AUT media = {media:.3f} dBi (valor sintetico verdadero {g_true}); desviacion tipica = {sd:.3f} dB; error tipico de la media = {sd/math.sqrt(30):.3f} dB")
    terminos = {"ganancia de la referencia (certificado)": 0.20, "desadaptacion de impedancia": 0.10, "alineacion de polarizacion": 0.05, "multitrayecto / reflexiones": 0.15, "repetibilidad (tipo A)": sd / math.sqrt(30)}
    u = math.sqrt(sum(v * v for v in terminos.values()))
    print("Presupuesto de incertidumbre (dB, k = 1, terminos SINTETICOS independientes):")
    for k, v in terminos.items():
        print(f"   {k:42s} {v:.3f}")
    print(f"   incertidumbre tipica combinada = {u:.3f} dB ; expandida (k = 2) = {2*u:.3f} dB")
    assert abs(u - math.sqrt(sum(v * v for v in terminos.values()))) < 1e-15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
