#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C03. Bandas VHF, UHF, S, X y Ka: longitud de onda, apertura necesaria para una ganancia y ancho de haz.
Las frecuencias centrales son ILUSTRATIVAS (no se consulto IEEE 521 ni asignaciones de la UIT); eficiencia de apertura sintetica."""
import math, sys

C = 299_792_458.0  # m/s (NIST CODATA 2022)
BANDAS = {"VHF 145 MHz": 145e6, "UHF 401 MHz": 401e6, "S 2.2 GHz": 2.2e9, "X 8.4 GHz": 8.4e9, "Ka 32 GHz": 32e9}
ETA = 0.60  # eficiencia de apertura, SINTETICA

def diametro(g_dbi, f):
    lam = C / f
    g = 10 ** (g_dbi / 10)
    return lam / math.pi * math.sqrt(g / ETA)

def ganancia_dbi(d, f):
    lam = C / f
    return 10 * math.log10(ETA * (math.pi * d / lam) ** 2)

def haz_grados(d, f):
    return 70.0 * (C / f) / d   # aproximacion estandar 70 lambda/D (ILUSTRATIVA)

def calcular():
    R = {"lam": {}, "d30": {}, "g1m": {}, "haz1m": {}, "d_rel": {}}
    for k, f in BANDAS.items():
        R["lam"][k] = C / f
        R["d30"][k] = diametro(30.0, f)
        R["g1m"][k] = ganancia_dbi(1.0, f)
        R["haz1m"][k] = haz_grados(1.0, f)
    R["chk_ida_vuelta"] = max(abs(ganancia_dbi(diametro(30.0, f), f) - 30.0) for f in BANDAS.values())
    R["razon_x_uhf"] = R["d30"]["UHF 401 MHz"] / R["d30"]["X 8.4 GHz"]
    R["razon_f"] = 8.4e9 / 401e6
    R["dg_20log"] = 20 * math.log10(R["razon_f"])
    R["dg_obs"] = R["g1m"]["X 8.4 GHz"] - R["g1m"]["UHF 401 MHz"]
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("ILUSTRATIVO: frecuencias centrales; eficiencia de apertura 0.60 (sintetica)")
    print(f"{'banda':13s} {'lambda[cm]':>10s} {'D para 30 dBi [m]':>18s} {'G(1 m) [dBi]':>13s} {'haz(1 m) [deg]':>15s}")
    for k in R["lam"]:
        print(f"{k:13s} {R['lam'][k]*100:10.3f} {R['d30'][k]:18.3f} {R['g1m'][k]:13.2f} {R['haz1m'][k]:15.2f}")
    print(f"D(UHF)/D(X) para igual ganancia = {R['razon_x_uhf']:.3f} ; f_X/f_UHF = {R['razon_f']:.3f}")
    print(f"Ganancia extra de X sobre UHF con 1 m = {R['dg_obs']:.3f} dB ; 20 log10(f_X/f_UHF) = {R['dg_20log']:.3f} dB")
    assert R["chk_ida_vuelta"] < 1e-9
    assert abs(R["razon_x_uhf"] - R["razon_f"]) < 1e-9 and abs(R["dg_obs"] - R["dg_20log"]) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
