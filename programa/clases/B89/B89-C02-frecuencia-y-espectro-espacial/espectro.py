#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C02. Frecuencia y espectro espacial: ancho de banda ocupado, plan de canales, Doppler y limite de Shannon.
La banda de 50 MHz y todos los parametros del enlace son SINTETICOS/ILUSTRATIVOS (no es una asignacion de la UIT)."""
import math, sys

C = 299_792_458.0  # m/s (NIST CODATA 2022)

def calcular():
    R = {}
    rb, tasa_cod, bits_sim, alfa = 2.0e6, 0.5, 2, 0.35  # bit/s, tasa del codigo, QPSK, roll-off
    R["rs"] = rb / (tasa_cod * bits_sim)          # simbolos/s
    R["bw"] = R["rs"] * (1 + alfa)                # Hz ocupados (filtro coseno alzado)
    guarda = 0.3e6
    R["sep"] = R["bw"] + guarda
    banda = 50e6
    R["n"] = int(banda // R["sep"])
    R["usado"] = R["n"] * R["sep"]
    R["eta"] = rb / R["bw"]                       # bit/s/Hz del enlace
    v = 7.5e3                                     # m/s, velocidad radial maxima ilustrativa de una LEO
    R["dop"] = {"UHF 401 MHz": 401e6 * v / C, "S 2.2 GHz": 2.2e9 * v / C, "X 8.4 GHz": 8.4e9 * v / C}
    R["dop_en_canales"] = R["dop"]["X 8.4 GHz"] / R["sep"]
    snr = 10 ** (10 / 10)
    R["shannon"] = R["bw"] * math.log2(1 + snr)   # bit/s con SNR = 10 dB
    R["ebn0_min_db"] = 10 * math.log10((2 ** R["eta"] - 1) / R["eta"])
    R["ebn0_inf_db"] = 10 * math.log10(math.log(2))   # limite cuando la eficiencia -> 0
    # verificacion independiente: el limite de Shannon despejado reproduce SNR
    R["chk_snr"] = abs((2 ** (R["shannon"] / R["bw"]) - 1) - snr) / snr
    R["chk_banda"] = R["usado"] <= banda
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("ILUSTRATIVO: Rb = 2 Mbit/s, codigo 1/2, QPSK, roll-off 0.35, guarda 0.3 MHz, banda 50 MHz")
    print(f"  Rs = {R['rs']/1e6:.3f} Msimb/s ; ancho ocupado = {R['bw']/1e6:.3f} MHz ; separacion = {R['sep']/1e6:.3f} MHz")
    print(f"  canales = {R['n']} ; espectro usado = {R['usado']/1e6:.2f} MHz ; eficiencia = {R['eta']:.3f} bit/s/Hz")
    for k, v in R["dop"].items():
        print(f"  Doppler maximo a 7.5 km/s en {k:12s} = {v/1e3:8.3f} kHz")
    print(f"  Doppler X = {R['dop_en_canales']:.3f} separaciones de canal")
    print(f"Shannon con SNR = 10 dB: C = {R['shannon']/1e6:.3f} Mbit/s")
    print(f"Eb/N0 minimo (Shannon) a esta eficiencia = {R['ebn0_min_db']:.3f} dB ; limite absoluto = {R['ebn0_inf_db']:.3f} dB")
    assert R["chk_snr"] < 1e-12 and R["chk_banda"]
    assert abs(R["ebn0_inf_db"] + 1.5917) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
