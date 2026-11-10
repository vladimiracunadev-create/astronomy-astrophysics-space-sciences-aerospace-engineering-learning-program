#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C23. Relacion C/N0, Eb/N0 y tasa de error de bit: conversiones, tasa maxima para una BER objetivo y verificacion por Monte Carlo.
Valores de C/N0 y tasas SINTETICOS; canal AWGN con BPSK (semilla 89)."""
import math, random, sys

def q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))

def ber_bpsk_db(ebn0_db):
    return q(math.sqrt(2 * 10 ** (ebn0_db / 10)))

def req_db(ber, f=ber_bpsk_db):
    lo, hi = -10.0, 30.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > ber:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def ebn0_desde_cn0(cn0_dbhz, rb):
    return cn0_dbhz - 10 * math.log10(rb)

def esn0_desde_ebn0(ebn0_db, bits_simbolo, tasa_codigo):
    return ebn0_db + 10 * math.log10(bits_simbolo * tasa_codigo)

def rb_max(cn0_dbhz, req, margen=0.0):
    return 10 ** ((cn0_dbhz - req - margen) / 10)

def mc_bpsk(ebn0_db, n, rng):
    g = 10 ** (ebn0_db / 10)
    sigma = math.sqrt(1 / (2 * g))
    err = 0
    for _ in range(n):
        b = rng.getrandbits(1)
        y = (1 if b else -1) + rng.gauss(0, sigma)
        err += (y > 0) != bool(b)
    return err / n

def calcular():
    R = {}
    R["req_1e3"], R["req_1e5"], R["req_1e7"] = req_db(1e-3), req_db(1e-5), req_db(1e-7)
    R["tabla"] = {}
    for cn0 in (40.0, 50.0, 60.0):
        R["tabla"][cn0] = {rb: ebn0_desde_cn0(cn0, rb) for rb in (1e3, 1e4, 1e5)}
    R["rbmax"] = {cn0: (rb_max(cn0, R["req_1e5"]), rb_max(cn0, R["req_1e5"], 3.0)) for cn0 in (40.0, 50.0, 60.0)}
    R["doble"] = ebn0_desde_cn0(50.0, 1e4) - ebn0_desde_cn0(50.0, 2e4)
    R["esn0"] = esn0_desde_ebn0(R["req_1e5"], 2, 0.5)
    R["esn0_bpsk"] = esn0_desde_ebn0(R["req_1e5"], 1, 1.0)
    # verificacion por Monte Carlo en una cadena C/N0 -> Eb/N0 -> BER
    rng = random.Random(89)
    cn0, rb = 47.0, 10e3
    ebn0 = ebn0_desde_cn0(cn0, rb)
    n = 500_000
    R["mc"] = (ebn0, mc_bpsk(ebn0, n, rng), ber_bpsk_db(ebn0), n)
    R["z"] = abs(R["mc"][1] - R["mc"][2]) / math.sqrt(R["mc"][2] * (1 - R["mc"][2]) / n)
    # BER frente a rb para C/N0 = 50
    R["ber_vs_rb"] = {rb: ber_bpsk_db(ebn0_desde_cn0(50.0, rb)) for rb in (1e4, 2e4, 5e4, 1e5)}
    # comprobacion de consistencia: la tasa maxima reproduce la BER objetivo
    R["chk"] = abs(ber_bpsk_db(ebn0_desde_cn0(50.0, R["rbmax"][50.0][0])) - 1e-5) / 1e-5
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"Eb/N0 requerido por BPSK: BER 1e-3 = {R['req_1e3']:.3f} dB ; 1e-5 = {R['req_1e5']:.3f} dB ; 1e-7 = {R['req_1e7']:.3f} dB")
    print("Eb/N0 [dB] = C/N0 [dB-Hz] - 10 log10(Rb):")
    print(f"{'C/N0':>6s}{'Rb=1 kbit/s':>14s}{'10 kbit/s':>12s}{'100 kbit/s':>13s}")
    for cn0, v in R["tabla"].items():
        print(f"{cn0:6.0f}" + "".join(f"{x:14.2f}" if i == 0 else f"{x:12.2f}" if i == 1 else f"{x:13.2f}" for i, x in enumerate(v.values())))
    print("Tasa maxima para BER 1e-5 (sin margen / con 3 dB de margen):")
    for cn0, (a, b) in R["rbmax"].items():
        print(f"  C/N0 = {cn0:.0f} dB-Hz: {a/1e3:9.2f} / {b/1e3:9.2f} kbit/s")
    print(f"Duplicar la tasa cuesta {R['doble']:.3f} dB ; Es/N0 para QPSK con codigo 1/2 a Eb/N0 requerido = {R['esn0']:.3f} dB (BPSK sin codigo: {R['esn0_bpsk']:.3f} dB)")
    e, mc, teo, n = R["mc"]
    print(f"Monte Carlo (C/N0 = 47 dB-Hz, Rb = 10 kbit/s -> Eb/N0 = {e:.2f} dB, {n} bits): BER = {mc:.4e} ; teoria = {teo:.4e} ; z = {R['z']:.2f}")
    print("BER frente a la tasa a C/N0 = 50 dB-Hz:", ", ".join(f"{rb/1e3:.0f} kbit/s: {v:.2e}" for rb, v in R["ber_vs_rb"].items()))
    assert R["z"] < 4 and R["chk"] < 1e-6 and abs(R["doble"] - 3.0103) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
