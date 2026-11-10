#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C04. Propagacion y perdidas de espacio libre: FSPL, retardo de luz y perdida atmosferica ilustrativa.
Distancias REDONDEADAS e ILUSTRATIVAS (no consultadas); atenuaciones atmosfericas SINTETICAS. c: NIST CODATA 2022."""
import math, sys

C = 299_792_458.0  # m/s
UA = 1.495978707e11  # m (valor redondeado, ILUSTRATIVO, no consultado)
DIST = {"LEO 500 km": 500e3, "GEO ~35 786 km": 35_786e3, "Luna ~384 400 km": 384_400e3,
        "Marte 0.5 UA": 0.5 * UA, "Marte 2.5 UA": 2.5 * UA, "Neptuno ~30 UA": 30 * UA}
FREC = {"UHF 401 MHz": 401e6, "S 2.2 GHz": 2.2e9, "X 8.4 GHz": 8.4e9, "Ka 32 GHz": 32e9}
ATM_DB = {"UHF 401 MHz": 0.05, "S 2.2 GHz": 0.1, "X 8.4 GHz": 0.3, "Ka 32 GHz": 1.5}  # cielo despejado, SINTETICO

def fspl_db(d, f):
    return 20 * math.log10(4 * math.pi * d * f / C)

def friis_inv_db(d, f):
    """Perdida como -10 log10 (Pr/Pt) con antenas isotropas: (lambda / 4 pi d)^2 (segunda via)."""
    lam = C / f
    return -10 * math.log10((lam / (4 * math.pi * d)) ** 2)

def calcular():
    R = {"fspl": {}, "t": {}}
    for kd, d in DIST.items():
        R["t"][kd] = d / C
        R["fspl"][kd] = {kf: fspl_db(d, f) for kf, f in FREC.items()}
    R["chk_friis"] = max(abs(fspl_db(d, f) - friis_inv_db(d, f)) for d in DIST.values() for f in FREC.values())
    R["doble_d"] = fspl_db(2e6, 8.4e9) - fspl_db(1e6, 8.4e9)
    R["decada_f"] = fspl_db(1e6, 84e9) - fspl_db(1e6, 8.4e9)
    R["x_vs_ka_marte"] = R["fspl"]["Marte 2.5 UA"]["Ka 32 GHz"] - R["fspl"]["Marte 2.5 UA"]["X 8.4 GHz"]
    R["atm"] = ATM_DB
    R["total_ka_luna"] = R["fspl"]["Luna ~384 400 km"]["Ka 32 GHz"] + ATM_DB["Ka 32 GHz"]
    R["ida_vuelta_neptuno"] = 2 * R["t"]["Neptuno ~30 UA"]
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("ILUSTRATIVO: distancias redondeadas; atenuacion atmosferica SINTETICA (cielo despejado)")
    cab = "".join(f"{k:>13s}" for k in FREC)
    print(f"{'distancia':18s}{'retardo[s]':>12s}{cab}   (FSPL en dB)")
    for kd in DIST:
        print(f"{kd:18s}{R['t'][kd]:12.4f}" + "".join(f"{R['fspl'][kd][kf]:13.2f}" for kf in FREC))
    print(f"Al duplicar la distancia: +{R['doble_d']:.3f} dB ; por decada de frecuencia: +{R['decada_f']:.3f} dB")
    print(f"Ka - X a 2.5 UA = {R['x_vs_ka_marte']:.3f} dB ; ida y vuelta a 30 UA = {R['ida_vuelta_neptuno']/3600:.3f} h")
    print(f"Luna, Ka: FSPL + atmosfera = {R['total_ka_luna']:.2f} dB")
    assert R["chk_friis"] < 1e-9
    assert abs(R["doble_d"] - 6.0206) < 1e-3 and abs(R["decada_f"] - 20.0) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
