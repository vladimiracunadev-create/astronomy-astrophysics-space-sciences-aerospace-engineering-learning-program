#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C06: fisica basica de un ecografo portatil, guiado remoto y valor predictivo de una prueba de diagnostico.

Todo es calculo con parametros ILUSTRATIVOS (sin semilla: determinista). No describe ningun equipo real ni da criterio clinico.
Relaciones estandar de ultrasonido (no consultadas en una fuente concreta; las verifica el laboratorio): tiempo de ida y vuelta
t = 2 d / c con c = 1540 m/s (velocidad del sonido en tejido blando, valor de ensenanza); longitud de onda lambda = c / f; resolucion
axial ~ N lambda / 2 con N = 2 ciclos por pulso; atenuacion de ida y vuelta 2 alfa f d con alfa = 0,5 dB/(cm MHz) (valor de ensenanza);
profundidad maxima = rango dinamico / (2 alfa f) con 60 dB; frecuencia de repeticion maxima PRF = c / (2 d); cuadros por segundo =
PRF / lineas. Valor predictivo (teorema de Bayes): VPP = S p / (S p + (1 - E)(1 - p)); VPN = E (1 - p) / (E (1 - p) + (1 - S) p), con S la
sensibilidad, E la especificidad y p la prevalencia. Contexto consultado (2026-11-10): Kirkpatrick et al. (NTRS), segun el cual la
ecografia es la unica modalidad de imagen a bordo de la ISS y que las restricciones de masa, potencia, volumen, comunicaciones y
formacion limitan la capacidad medica. Retardo unidireccional de 4 a 24 min (Goddard, NASA). Unidades: Hz, m, cm, dB, s, bit/s. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

C = 1540.0  # m/s
ALFA = 0.5  # dB/(cm MHz), ida (ilustrativo)
RD = 60.0  # dB, rango dinamico (ilustrativo)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("PARAMETROS ILUSTRATIVOS: calculo determinista; no describe un equipo real ni da criterio clinico")
    t10 = 2 * 0.10 / C
    print(f"Control: tiempo de ida y vuelta a 10 cm = {t10 * 1e6:.1f} us (esperado 129.9 us)")
    assert abs(t10 * 1e6 - 129.87) < 0.01
    print("Frecuencia, longitud de onda, resolucion axial, profundidad maxima y velocidad de cuadros (128 lineas):")
    print("  f [MHz]   lambda [mm]   res. axial [mm]   prof. max. [cm]   PRF max a prof. max. [Hz]   cuadros/s")
    prev = 1e9
    for f in (2.0, 3.5, 5.0, 7.5, 10.0, 15.0):
        lam = C / (f * 1e6) * 1e3
        res = 2 * lam / 2
        dmax = RD / (2 * ALFA * f)
        prf = C / (2 * dmax / 100)
        fps = prf / 128
        assert dmax < prev
        prev = dmax
        print(f"   {f:5.1f}      {lam:6.3f}         {res:6.3f}            {dmax:6.1f}             {prf:8.0f}                {fps:6.1f}")
    print("Compromiso: subir f mejora la resolucion axial pero reduce la profundidad (la atenuacion crece con f).")
    print("Perdida de ida y vuelta [dB] a distintas profundidades con f = 3.5 MHz y f = 7.5 MHz:")
    for d in (2, 5, 10, 15):
        print(f"   {d:2d} cm: {2 * ALFA * 3.5 * d:5.1f} dB (3.5 MHz) ; {2 * ALFA * 7.5 * d:5.1f} dB (7.5 MHz)")
    print("Guiado remoto: ancho de banda de una imagen en vivo 640 x 480 px, 8 bit, 15 cuadros/s, compresion 20:1 (ilustrativa):")
    bruto = 640 * 480 * 8 * 15
    print(f"  bruto = {bruto / 1e6:.1f} Mbit/s; comprimido = {bruto / 20 / 1e6:.2f} Mbit/s")
    print("Retardo de ida y vuelta para el guiado (4 a 24 min unidireccional) frente a la tolerancia de una guia en tiempo real (~2 s, ilustrativa):")
    for d in (0.01, 4, 12, 24):
        rtt = 2 * d * 60
        print(f"   unidireccional {d:5.2f} min: ida y vuelta = {rtt:7.1f} s -> guia en tiempo real {'posible' if rtt <= 2 else 'IMPOSIBLE: almacenar y reenviar'}")
    print("Valor predictivo de una prueba de diagnostico ILUSTRATIVA (S = 0.90, E = 0.85) segun la prevalencia:")
    print("  prevalencia   VPP     VPN     razon de verosimilitud +")
    S, E = 0.90, 0.85
    prev_vpp = -1
    for p in (0.01, 0.05, 0.10, 0.30, 0.50):
        vpp = S * p / (S * p + (1 - E) * (1 - p))
        vpn = E * (1 - p) / (E * (1 - p) + (1 - S) * p)
        assert vpp > prev_vpp
        prev_vpp = vpp
        print(f"     {p:5.2f}     {vpp:5.3f}   {vpn:5.3f}          {S / (1 - E):5.2f}")
    p = 0.10
    n = 1000
    tp, fn, fp, tn = S * p * n, (1 - S) * p * n, (1 - E) * (1 - p) * n, E * (1 - p) * n
    print(f"Tabla de 1000 exploraciones con p = 0.10: VP = {tp:.0f}, FN = {fn:.0f}, FP = {fp:.0f}, VN = {tn:.0f}; VPP = {tp / (tp + fp):.3f}")
    assert abs(tp + fn + fp + tn - n) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
