#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C09: compresion de 1 dB, punto de intercepcion de tercer orden, prueba de dos tonos, cascada y rango dinamico libre de espurios.

Datos: k = 1.380649e-23 J/K (NIST, CODATA 2022, consultada el 2026-11-09), usada para el suelo de ruido. Todo lo demas es ILUSTRATIVO: amplificador de 20 dB de ganancia con IIP3 = -10 dBm, impedancia de 50 ohm,
segunda etapa con IIP3 = +5 dBm y 10 dB de ganancia, cifra de ruido de 2 dB, ancho de banda de 1 MHz. No describe ningun receptor real.
Modelo: no linealidad polinomica sin memoria y = a1 x + a3 x^3 (a3 < 0). Compresion: A_1dB^2 = (4/3)(a1/|a3|)(1 - 10^(-1/20)); intercepcion A_IP3^2 = (4/3) a1/|a3|; por tanto IIP3 - P1dB = 9,64 dB. Dos tonos
x = A (cos w1 t + cos w2 t): el producto de intermodulacion 2 w1 - w2 tiene amplitud (3/4)|a3| A^3 y pendiente 3 dB por dB. Potencia en dBm: P = A^2/(2R). Cascada: 1/IIP3 = 1/IIP3_1 + G1/IIP3_2 (lineal).
Rango libre de espurios SFDR = (2/3)(IIP3 - suelo de ruido). El espectro se mide con la transformada discreta en bins enteros (ventana rectangular, periodos enteros: sin fuga).
Supuestos: solo termino de tercer orden; sin memoria; sin compresion de orden superior. Validez: potencias por debajo de unos 10 dB bajo el punto de compresion.
Tolerancia: la compresion simulada a la potencia analitica de P1dB da 1,000 dB a 0,01 dB (modelo exacto del polinomio); amplitud medida del producto de tercer orden frente a (3/4)|a3|A^3 a 1e-6 relativo; pendiente
3,00 a 0,01; IIP3 de la cascada simulada frente a la formula a 5 % (estimacion por extrapolacion a bajo nivel).
"""
from __future__ import annotations
import math, platform

R = 50.0
K = 1.380649e-23
NB = 4096


def dbm(a):
    return 10 * math.log10(a * a / (2 * R) * 1000)


def amp(p_dbm):
    return math.sqrt(2 * R * 10 ** (p_dbm / 10) / 1000)


def bin_amp(sig, b):
    n = len(sig)
    re = sum(v * math.cos(2 * math.pi * b * i / n) for i, v in enumerate(sig))
    im = sum(v * math.sin(2 * math.pi * b * i / n) for i, v in enumerate(sig))
    return 2 * math.hypot(re, im) / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a1 = 10.0
    iip3 = -10.0
    a_ip3 = amp(iip3)
    a3 = -(4.0 / 3.0) * a1 / a_ip3 ** 2
    print(f"a1 = {a1} (20 dB) ; IIP3 = {iip3} dBm -> A_IP3 = {a_ip3:.5f} V ; a3 = {a3:.2f} V^-2")
    a_1db = math.sqrt((4.0 / 3.0) * (a1 / abs(a3)) * (1 - 10 ** (-1 / 20)))
    p1db = dbm(a_1db)
    print(f"Compresion de 1 dB en la entrada: A = {a_1db:.5f} V ; P1dB = {p1db:.3f} dBm ; IIP3 - P1dB = {iip3 - p1db:.3f} dB")
    g1 = 20 * math.log10(abs(a1 + 0.75 * a3 * a_1db ** 2) / a1)
    print(f"Ganancia de pequena senal 20,000 dB ; ganancia a P1dB = {20 + g1:.4f} dB (compresion {g1:.4f} dB)")
    assert abs(g1 + 1) < 0.01

    t = [i for i in range(NB)]
    b1, b2 = 101, 109
    print(f"{'P por tono (dBm)':>17} {'fundamental (dBm)':>18} {'IM3 (dBm)':>10} {'IM3 teorico (dBm)':>18} {'dif relativa':>13}")
    filas = []
    for p in (-50.0, -40.0, -30.0, -20.0):
        A = amp(p)
        x = [A * (math.cos(2 * math.pi * b1 * i / NB) + math.cos(2 * math.pi * b2 * i / NB)) for i in t]
        y = [a1 * v + a3 * v ** 3 for v in x]
        f1 = bin_amp(y, b1)
        im = bin_amp(y, 2 * b1 - b2)
        im_t = 0.75 * abs(a3) * A ** 3
        dif = abs(im / im_t - 1)
        filas.append((p, dbm(f1), dbm(im)))
        print(f"{p:17.1f} {dbm(f1):18.3f} {dbm(im):10.3f} {dbm(im_t):18.3f} {dif:13.2e}")
        if p <= -30:
            assert dif < 1e-6 or p > -30
    pend = (filas[1][2] - filas[0][2]) / (filas[1][0] - filas[0][0])
    print(f"Pendiente del producto de tercer orden entre -50 y -40 dBm: {pend:.4f} dB/dB")
    assert abs(pend - 3) < 0.01
    # extrapolacion: IIP3 = P + (F - IM)/2 en entrada
    p, f1d, imd = filas[0]
    iip3_ext = p + (f1d - imd) / 2
    print(f"IIP3 por extrapolacion a bajo nivel = {iip3_ext:.3f} dBm (referido a la entrada; la ganancia de 20 dB se resta a la salida)")
    iip3_in = p + ((f1d - 20.0) - (imd - 20.0)) / 2
    assert abs(iip3_in - iip3) < 0.05

    # cascada
    g1_db, g2_db = 20.0, 10.0
    iip3_2 = 5.0
    lin = lambda d: 10 ** (d / 10)
    inv = 1 / lin(iip3) + lin(g1_db) / lin(iip3_2)
    iip3_c = -10 * math.log10(inv)
    print(f"Cascada: 1/IIP3 = 1/IIP3_1 + G1/IIP3_2 -> IIP3 = {iip3_c:.3f} dBm (primera etapa sola {iip3} dBm)")
    # simulacion de la cascada: segunda etapa con a1b = 10^(10/20), a3b por IIP3_2
    a1b = 10 ** (g2_db / 20)
    a3b = -(4.0 / 3.0) * a1b / amp(iip3_2) ** 2
    pt = -50.0
    A = amp(pt)
    x = [A * (math.cos(2 * math.pi * b1 * i / NB) + math.cos(2 * math.pi * b2 * i / NB)) for i in t]
    y1 = [a1 * v + a3 * v ** 3 for v in x]
    y2 = [a1b * v + a3b * v ** 3 for v in y1]
    f_o = bin_amp(y2, b1)
    i_o = bin_amp(y2, 2 * b1 - b2)
    iip3_sim = pt + (dbm(f_o) - dbm(i_o)) / 2
    print(f"IIP3 de la cascada simulada = {iip3_sim:.3f} dBm ; formula = {iip3_c:.3f} dBm ; dif = {abs(iip3_sim - iip3_c):.3f} dB")
    assert abs(10 ** (iip3_sim / 10) / 10 ** (iip3_c / 10) - 1) < 0.05

    # SFDR
    nf, bw = 2.0, 1e6
    suelo = 10 * math.log10(K * 290 * bw * 1000) + nf
    sfdr = 2.0 / 3.0 * (iip3 - suelo)
    print(f"Suelo de ruido de entrada = {suelo:.2f} dBm (kTB a 290 K, B = 1 MHz, NF = 2 dB) ; SFDR = (2/3)(IIP3 - suelo) = {sfdr:.2f} dB")
    pmax = suelo + sfdr
    print(f"Un tono de {pmax:.2f} dBm por canal produce IM3 igual al suelo de ruido")
    assert abs((3 * pmax - 2 * iip3) - suelo) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
