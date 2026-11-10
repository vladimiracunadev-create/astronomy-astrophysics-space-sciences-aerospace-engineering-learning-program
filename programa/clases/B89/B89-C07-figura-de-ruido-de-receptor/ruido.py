#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C07. Figura de ruido de receptor: formula de Friis en cascada, temperatura de sistema y G/T.
Etapas y temperatura de antena SINTETICAS; T0 = 290 K es la referencia convencional de la figura de ruido (no consultada). k: NIST (consultada)."""
import math, sys

K = 1.380649e-23
T0 = 290.0

def db(x):
    return 10 * math.log10(x)

def lin(x_db):
    return 10 ** (x_db / 10)

def t_de_nf(nf_db):
    return T0 * (lin(nf_db) - 1)

def cascada(etapas):
    """etapas: lista de (ganancia dB, NF dB). Devuelve (T_equivalente K, G total lineal) por Friis de temperaturas."""
    t, g = 0.0, 1.0
    for ganancia_db, nf_db in etapas:
        t += t_de_nf(nf_db) / g
        g *= lin(ganancia_db)
    return t, g

def cascada_nf(etapas):
    """Segunda via: formula de Friis en factores de ruido F = F1 + (F2-1)/G1 + ..."""
    f, g = 0.0, 1.0
    for i, (ganancia_db, nf_db) in enumerate(etapas):
        f = lin(nf_db) if i == 0 else f + (lin(nf_db) - 1) / g
        g *= lin(ganancia_db)
    return db(f)

def calcular():
    cable = (-1.0, 1.0)      # perdida pasiva: ganancia -1 dB, NF = 1 dB
    lna = (30.0, 0.6)
    rx = (40.0, 8.0)
    R = {}
    ordenes = {"LNA primero": [lna, cable, rx], "cable primero": [cable, lna, rx], "sin LNA": [cable, rx]}
    R["T"] = {k: cascada(v)[0] for k, v in ordenes.items()}
    R["NF"] = {k: db(1 + v / T0) for k, v in R["T"].items()}
    R["NF_friis"] = {k: cascada_nf(v) for k, v in ordenes.items()}
    R["chk"] = max(abs(R["NF"][k] - R["NF_friis"][k]) for k in ordenes)
    t_ant = 25.0   # K (cielo + antena), SINTETICO
    gr = 68.0
    R["tsis"] = {k: t_ant + v for k, v in R["T"].items()}
    R["gt"] = {k: gr - db(R["tsis"][k]) for k in ordenes}
    R["n0_dbw"] = {k: db(K * R["tsis"][k]) for k in ordenes}
    R["gt_dif"] = R["gt"]["LNA primero"] - R["gt"]["sin LNA"]
    R["t_lna_solo"] = t_de_nf(0.6)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: LNA 30 dB / 0.6 dB, cable 1 dB, receptor 40 dB / 8 dB ; T_antena = 25 K ; Gr = 68 dBi ; T0 = 290 K")
    print(f"{'orden':14s}{'T_rx [K]':>10s}{'NF [dB]':>10s}{'NF Friis':>10s}{'T_sis [K]':>11s}{'G/T [dB/K]':>12s}{'N0 [dBW/Hz]':>13s}")
    for k in R["T"]:
        print(f"{k:14s}{R['T'][k]:10.2f}{R['NF'][k]:10.3f}{R['NF_friis'][k]:10.3f}{R['tsis'][k]:11.2f}{R['gt'][k]:12.2f}{R['n0_dbw'][k]:13.2f}")
    print(f"T del LNA solo (NF 0.6 dB) = {R['t_lna_solo']:.2f} K ; mejora de G/T con LNA primero frente a sin LNA = {R['gt_dif']:.2f} dB")
    assert R["chk"] < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
