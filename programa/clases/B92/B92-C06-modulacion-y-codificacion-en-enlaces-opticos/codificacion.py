#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C06: tasa de informacion de un enlace PPM con los parametros del CCSDS 142.0-B-1.

Datos consultados (2026-11-10), CCSDS 142.0-B-1 (agosto de 2019): tasas de codigo r en {1/3, 1/2, 2/3} con bloques de
informacion k = 5006, 7526, 10046 bits (k + CRC-32 + 2 bits de terminacion = 5040, 7560, 10080 bits; tabla 3-1);
orden PPM M en {4, 8, 16, 32, 64, 128, 256} (3.8.5); M/4 ranuras de guarda tras cada simbolo (3.13); marcador de
sincronizacion de palabra (CSM) de W = 16 simbolos PPM para M >= 8 y 24 para M = 4 (3.10.2.1); la palabra codigo tiene 15120
simbolos binarios de codigo (el texto de 3.8.5 indica que 15120 es multiplo de m = log2 M). CCSDS 141.0-B-1 (agosto de 2019):
ranuras de 0.125 a 512 ns (3.9) y el ejemplo de 1 ns, 16-PPM y 4 ranuras de guarda con tasa de repeticion de pulsos de
28.57 a 200 MHz (3.10).
ILUSTRATIVOS (sinteticos, no medidos): ranura de 1 ns, fotones detectados por simbolo 0.5..4 para la capacidad.
Modelo: simbolos por palabra = 15120/m + W; ranuras por palabra = (15120/m + W) * 1.25 M; tasa = k / (ranuras * T).
No se cuentan el ASM, los encabezados ni los marcos de transferencia: es la tasa de bloque de informacion, no la tasa de usuario.
Capacidad del canal PPM sin fondo (canal de borrado): C = (1 - exp(-ns)) log2 M bits por simbolo.
Segunda via: construccion explicita de las ranuras (mapeo bits -> posicion de pulso + guardas) con random.Random(92).
Tolerancia: conteo de ranuras exacto; PRR 1e-12 relativa.
"""
from __future__ import annotations
import math, platform, random

K = {"1/3": (5006, 5040), "1/2": (7526, 7560), "2/3": (10046, 10080)}
N_COD = 15120
T = 1e-9


def csm(m):
    return 24 if m == 4 else 16


def ranuras_formula(m):
    mm = int(math.log2(m))
    return (N_COD // mm + csm(m)) * (m + m // 4)


def ranuras_explicitas(m, rng):
    mm = int(math.log2(m))
    assert N_COD % mm == 0
    bits = [rng.randint(0, 1) for _ in range(N_COD)]
    simbolos = [int("".join(map(str, bits[i:i + mm])), 2) for i in range(0, N_COD, mm)]
    simbolos += [rng.randrange(m) for _ in range(csm(m))]  # el CSM ocupa W simbolos PPM
    ranuras = []
    pulsos = 0
    for s in simbolos:
        v = [0] * (m + m // 4)
        v[s] = 1
        pulsos += 1
        ranuras.extend(v)
    return len(ranuras), pulsos, len(simbolos)


def tasa(k, m):
    return k / (ranuras_formula(m) * T)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(92)
    print("Comprobacion de la estructura de la palabra (formula frente a construccion explicita de ranuras):")
    print("   M  m  simbolos/palabra  ranuras formula  ranuras construidas  pulsos")
    for m in (4, 8, 16, 32, 64, 128, 256):
        nr, npul, nsim = ranuras_explicitas(m, rng)
        assert nr == ranuras_formula(m) and npul == nsim
        print(f"{m:4d} {int(math.log2(m)):2d} {nsim:16d} {ranuras_formula(m):16d} {nr:20d} {npul:7d}")
    print(f"Bloques: k/k^ = {', '.join(f'{r}: {k}/{kh}' for r, (k, kh) in K.items())} ; control: k^ / r = 15120")
    for r, (k, kh) in K.items():
        num, den = map(int, r.split("/"))
        assert kh * den / num == N_COD and kh == k + 34
    print("Tasa de informacion del bloque [Mbps], ranura de 1 ns:")
    print("   M   r=1/3     r=1/2     r=2/3   bits por ranura (r=1/2)  P_pico/P_media")
    for m in (4, 16, 64, 256):
        fila = [tasa(K[r][0], m) / 1e6 for r in ("1/3", "1/2", "2/3")]
        print(f"{m:4d} {fila[0]:8.3f} {fila[1]:9.3f} {fila[2]:9.3f} {K['1/2'][0] / ranuras_formula(m):17.5f} {1.25 * m:18.1f}")
    # PRR de ejemplo del CCSDS 141
    t_min, t_max = 5e-9, 35e-9
    prr_hi, prr_lo = 1 / t_min / 1e6, 1 / t_max / 1e6
    print(f"PRR del ejemplo CCSDS (1 ns, 16-PPM, 4 guardas): {prr_lo:.2f} a {prr_hi:.0f} MHz (publicado: 28.57 a 200 MHz)")
    assert abs(prr_lo - 28.57) < 0.01 and abs(prr_hi - 200.0) < 1e-12
    print("Capacidad del canal PPM sin fondo (borrado), M = 16:")
    print("  ns detectados  bits/simbolo  bits por foton detectado")
    prev = None
    for ns in (0.5, 1.0, 2.0, 4.0):
        c = (1 - math.exp(-ns)) * 4.0
        print(f"  {ns:12.1f}  {c:12.4f}  {c / ns:12.4f}")
        if prev is not None:
            assert c / ns < prev
        prev = c / ns
    print(f"  limite ns -> 0: {math.log2(16):.4f} bits por foton = log2 M")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
