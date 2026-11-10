#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C10. Sincronizacion de portadora: lazo de enganche de fase (PLL) digital de segundo orden que sigue una rampa de Doppler.
Senal y ruido SINTETICOS (semilla 89). Las formulas de ganancias del lazo y de jitter son relaciones estandar, no consultadas."""
import cmath, math, random, sys

def ganancias(bl_t, zeta):
    th = bl_t / (zeta + 1 / (4 * zeta))
    d = 1 + 2 * zeta * th + th * th
    return 4 * zeta * th / d, 4 * th * th / d

def simular(cn0_dbhz, bl, zeta, fs, dur, f0, fdot, semilla=89):
    rng = random.Random(semilla)
    cn0 = 10 ** (cn0_dbhz / 10)
    sigma = math.sqrt(fs / cn0 / 2)          # por componente; C = 1
    kp, ki = ganancias(bl / fs, zeta)
    n = int(dur * fs)
    fase_nco = 0.0
    integ = 2 * math.pi * f0 / fs   # frecuencia ya adquirida (la adquisicion queda fuera de alcance)
    err = []
    for i in range(n):
        t = i / fs
        fase_in = 2 * math.pi * (f0 * t + 0.5 * fdot * t * t)
        x = cmath.exp(1j * fase_in) + complex(rng.gauss(0, sigma), rng.gauss(0, sigma))
        e = cmath.phase(x * cmath.exp(-1j * fase_nco))
        real = (fase_in - fase_nco + math.pi) % (2 * math.pi) - math.pi   # error de fase verdadero
        integ += ki * e
        fase_nco += kp * e + integ
        # el lazo integra: la fase del NCO avanza con el termino proporcional + frecuencia acumulada
        err.append(real)
    return err

def calcular():
    fs, dur, bl, zeta = 100.0, 200.0, 5.0, 0.7071
    R = {"fs": fs, "bl": bl, "zeta": zeta}
    wn = 8 * zeta * bl / (4 * zeta ** 2 + 1)
    R["wn"] = wn
    fdot = 5.0
    R["err_rampa_teo"] = 2 * math.pi * fdot / wn ** 2
    R["casos"] = {}
    for cn0 in (30.0, 36.0):
        err = simular(cn0, bl, zeta, fs, dur, 50.0, fdot)
        tail = err[int(20 * fs):]
        m = sum(tail) / len(tail)
        sd = math.sqrt(sum((x - m) ** 2 for x in tail) / len(tail))
        snr_l = 10 ** (cn0 / 10) / bl
        R["casos"][cn0] = {"media": m, "sd": sd, "sd_teo": math.sqrt(1 / snr_l), "snr_l_db": 10 * math.log10(snr_l)}
    R["kp"], R["ki"] = ganancias(bl / fs, zeta)
    c = R["casos"][30.0]
    R["rel_sd"] = abs(c["sd"] - c["sd_teo"]) / c["sd_teo"]
    R["rel_rampa"] = abs(c["media"] - R["err_rampa_teo"]) / R["err_rampa_teo"]
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"SINTETICO: fs = {R['fs']:.0f} Hz, B_L = {R['bl']:.1f} Hz, zeta = {R['zeta']:.4f}, f0 = 50 Hz, rampa 5 Hz/s, 200 s")
    print(f"  wn = {R['wn']:.3f} rad/s ; Kp = {R['kp']:.6f} ; Ki = {R['ki']:.3e}")
    print(f"  error de fase teorico por la rampa = {R['err_rampa_teo']:.4f} rad")
    for cn0, c in R["casos"].items():
        print(f"  C/N0 = {cn0:.0f} dB-Hz: SNR_lazo = {c['snr_l_db']:.1f} dB ; error medio = {c['media']:.4f} rad ; "
              f"sigma medida = {c['sd']:.4f} rad ; sigma teorica = {c['sd_teo']:.4f} rad")
    print(f"  discrepancias a 30 dB-Hz: sigma {100*R['rel_sd']:.1f} % ; rampa {100*R['rel_rampa']:.1f} %")
    assert R["rel_sd"] < 0.25 and R["rel_rampa"] < 0.25
    assert R["casos"][36.0]["sd"] < R["casos"][30.0]["sd"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
