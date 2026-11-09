#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C11: mezclador de conmutacion ideal, perdida de conversion, armonicos del oscilador local, tabla de espurios y ruido de la cadena mezclador mas FI.

Datos: ninguna constante fisica. Las frecuencias estan en unidades de 10 MHz (RF = 142, es decir 1420 MHz; OL = 132; FI = 10), la amplitud de RF de 1, la perdida de conversion de 7 dB y las temperaturas
de 1163 K (mezclador) y 100 K (FI) son ILUSTRATIVAS; no describen ningun mezclador real.
Modelo: mezclador de conmutacion que multiplica la RF por una onda cuadrada del oscilador local (fundamental 4/pi), sintetizada con sus armonicos impares hasta el 9. Transformada discreta de N = 4096
muestras (bins enteros, sin fuga). Perdida de conversion ideal: la componente de FI tiene amplitud (2/pi) de la de RF, es decir 20 log10(pi/2) = 3,922 dB. Cada armonico m del OL da un espurio en |f_RF - m f_OL| con
amplitud relativa 1/m. Tabla de productos |m f_RF +- n f_OL| hasta orden 5. Ruido: T_cadena = T_mezclador + L_c T_FI con L_c la perdida en veces.
Supuestos: conmutacion instantanea, sin perdidas ohmicas, sin aislamiento finito, sin saturacion de la FI. Validez: ilustra el principio; no modela diodos, mezcladores SIS ni HEB.
Tolerancia: componente de FI medida frente a 2/pi a 1e-9; espurios 1/m frente a lo medido a 1e-9; la tabla de productos incluye la FI y la imagen.
"""
from __future__ import annotations
import math, platform

N = 4096
F_RF, F_OL = 142, 132


def amp_bin(sig, b):
    n = len(sig)
    re = sum(v * math.cos(2 * math.pi * b * i / n) for i, v in enumerate(sig))
    im = sum(v * math.sin(2 * math.pi * b * i / n) for i, v in enumerate(sig))
    return 2 * math.hypot(re, im) / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    def ol(i):
        return sum((4 / math.pi) / m * math.sin(2 * math.pi * m * F_OL * i / N) for m in (1, 3, 5, 7, 9))
    rf = [math.cos(2 * math.pi * F_RF * i / N) for i in range(N)]
    s = [rf[i] * ol(i) for i in range(N)]
    a_if = amp_bin(s, F_RF - F_OL)
    print(f"RF = {F_RF} ; OL = {F_OL} ; FI = |RF - OL| = {F_RF - F_OL} (unidades de 10 MHz)")
    print(f"Amplitud de la FI = {a_if:.9f} ; 2/pi = {2 / math.pi:.9f} ; perdida de conversion = {-20 * math.log10(a_if):.4f} dB ; 20 log10(pi/2) = {20 * math.log10(math.pi / 2):.4f} dB")
    assert abs(a_if - 2 / math.pi) < 1e-9
    print(f"{'armonico m':>10} {'frecuencia |RF - m OL|':>23} {'amplitud':>10} {'relativa a la FI':>17} {'1/m':>8}")
    for m in (1, 3, 5, 7, 9):
        f = abs(F_RF - m * F_OL)
        a = amp_bin(s, f)
        rel = a / a_if
        print(f"{m:10d} {f:23d} {a:10.6f} {rel:17.6f} {1 / m:8.4f}")
        assert abs(rel - 1 / m) < 1e-9
    # imagen
    f_im = F_OL - (F_RF - F_OL)
    a_im = amp_bin(s, F_RF - F_OL)
    print(f"Una senal en la imagen f = 2 OL - RF = {f_im} tambien cae en la FI = {abs(f_im - F_OL)}")
    # RF-OL feed-through en mezclador no balanceado
    s_unip = [rf[i] * (0.5 + 0.5 * (ol(i) > 0 and 1 or -1)) for i in range(N)]
    print(f"Mezclador no balanceado (OL de 0 a 1): fuga de RF en la salida = {amp_bin(s_unip, F_RF):.4f} ; FI = {amp_bin(s_unip, F_RF - F_OL):.4f}")
    # tabla de productos hasta orden 5
    prods = {}
    for m in range(0, 6):
        for n in range(0, 6):
            if m + n > 5 or (m == 0 and n == 0):
                continue
            for sg in (1, -1):
                f = abs(m * F_RF + sg * n * F_OL)
                prods.setdefault(f, []).append(f"{m}RF{'+' if sg > 0 else '-'}{n}OL")
    cerca = {f: v for f, v in prods.items() if 5 <= f <= 15}
    print("Productos de orden <= 5 con frecuencia entre 5 y 15 (banda de FI de 5 a 15 unidades):")
    for f in sorted(cerca):
        print(f"  {f:4d}: {', '.join(cerca[f])}")
    assert 10 in cerca and "1RF-1OL" in cerca[10]
    # ruido
    lc = 10 ** (7 / 10)
    t = 1163.0 + lc * 100.0
    print(f"Perdida de conversion de 7 dB = {lc:.4f} veces ; aporte de la FI referido a la entrada = L_c T_FI = {lc * 100:.1f} K ; T_mezclador + L_c T_FI = {t:.1f} K")
    t2 = 1163.0 + 10 ** (3.922 / 10) * 100
    print(f"Con la perdida ideal de 3,922 dB y el mismo T_mezclador: {t2:.1f} K")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
