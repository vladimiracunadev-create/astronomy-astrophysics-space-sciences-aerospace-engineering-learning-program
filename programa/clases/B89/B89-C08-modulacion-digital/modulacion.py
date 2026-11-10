#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C08. Modulacion digital: BER teorica de BPSK, QPSK, 8PSK y 16QAM y simulacion de Monte Carlo (semilla fija).
Canal AWGN SINTETICO; las aproximaciones de 8PSK y 16QAM son relaciones estandar, no consultadas."""
import math, random, sys

def q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))

def ber_bpsk(g):      # g = Eb/N0 lineal
    return q(math.sqrt(2 * g))

def ber_qpsk(g):      # con Gray, igual que BPSK por bit
    return q(math.sqrt(2 * g))

def ber_8psk(g):      # aproximacion con Gray: Pb ~ Ps/3
    return math.erfc(math.sqrt(3 * g) * math.sin(math.pi / 8)) / 3

def ber_16qam(g):     # aproximacion con Gray
    return (3 / 8) * math.erfc(math.sqrt(0.4 * g))

TEORIA = {"BPSK": ber_bpsk, "QPSK": ber_qpsk, "8PSK": ber_8psk, "16QAM": ber_16qam}
BITS = {"BPSK": 1, "QPSK": 2, "8PSK": 3, "16QAM": 4}

def req_db(f, ber):
    lo, hi = 0.0, 1000.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(mid) > ber:
            lo = mid
        else:
            hi = mid
    return 10 * math.log10(lo)

def sim_bpsk(g, n, rng):
    sigma = math.sqrt(1 / (2 * g))   # Eb = 1, N0/2 = sigma^2
    err = 0
    for _ in range(n):
        bit = rng.getrandbits(1)
        y = (1 if bit else -1) + rng.gauss(0, sigma)
        err += (y > 0) != bool(bit)
    return err / n

def sim_qpsk(g, n, rng):
    # Eb = 1, Es = 2: cada eje lleva un bit con amplitud 1
    sigma = math.sqrt(1 / (2 * g))
    err = 0
    for _ in range(n // 2):
        for _ in range(2):
            bit = rng.getrandbits(1)
            y = (1 if bit else -1) + rng.gauss(0, sigma)
            err += (y > 0) != bool(bit)
    return err / (2 * (n // 2))

GRAY = {-3: (0, 0), -1: (0, 1), 1: (1, 1), 3: (1, 0)}

def decidir(y):
    return -3 if y < -2 else (-1 if y < 0 else (1 if y < 2 else 3))

def sim_16qam(g, n_sim, rng):
    # Es = 10 d^2 con d = 1 -> Eb = Es/4 = 2.5 ; sigma^2 = N0/2 = Eb/(2 g)
    eb = 2.5
    sigma = math.sqrt(eb / (2 * g))
    niveles = (-3, -1, 1, 3)
    err = 0
    for _ in range(n_sim):
        for _ in range(2):   # dos ejes
            a = rng.choice(niveles)
            y = a + rng.gauss(0, sigma)
            r = decidir(y)
            err += sum(x != z for x, z in zip(GRAY[a], GRAY[r]))
    return err / (n_sim * 4)

def calcular():
    R = {"teo": {}, "req": {}}
    for nombre, f in TEORIA.items():
        R["teo"][nombre] = {eb: f(10 ** (eb / 10)) for eb in (4, 8, 10)}
        R["req"][nombre] = req_db(f, 1e-5)
    rng = random.Random(89)
    g4 = 10 ** (4 / 10)
    n = 200_000
    R["n"] = n
    R["sim_bpsk"] = sim_bpsk(g4, n, rng)
    R["sim_qpsk"] = sim_qpsk(g4, n, rng)
    g8 = 10 ** (8 / 10)
    R["n16"] = 100_000
    R["sim_16qam"] = sim_16qam(g8, R["n16"], rng)
    R["t_bpsk"], R["t_16qam"] = ber_bpsk(g4), ber_16qam(g8)
    # tolerancia binomial a 4 sigma
    def z(sim, teo, nb):
        return abs(sim - teo) / math.sqrt(teo * (1 - teo) / nb)
    R["z"] = {"bpsk": z(R["sim_bpsk"], R["t_bpsk"], n), "qpsk": z(R["sim_qpsk"], R["t_bpsk"], n),
              "16qam": z(R["sim_16qam"], R["t_16qam"], 4 * R["n16"])}
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print("AWGN sintetico. BER teorica:")
    print(f"{'modulacion':10s}{'bits/simb':>10s}{'Eb/N0=4':>12s}{'Eb/N0=8':>12s}{'Eb/N0=10':>12s}{'req. 1e-5 [dB]':>16s}")
    for k in TEORIA:
        t = R["teo"][k]
        print(f"{k:10s}{BITS[k]:10d}{t[4]:12.3e}{t[8]:12.3e}{t[10]:12.3e}{R['req'][k]:16.2f}")
    print(f"Monte Carlo a Eb/N0 = 4 dB ({R['n']} bits): BPSK = {R['sim_bpsk']:.4e} (teoria {R['t_bpsk']:.4e}, z = {R['z']['bpsk']:.2f})")
    print(f"                                           QPSK = {R['sim_qpsk']:.4e} (teoria {R['t_bpsk']:.4e}, z = {R['z']['qpsk']:.2f})")
    print(f"Monte Carlo a Eb/N0 = 8 dB ({4*R['n16']} bits): 16QAM = {R['sim_16qam']:.4e} (teoria aprox. {R['t_16qam']:.4e}, z = {R['z']['16qam']:.2f})")
    assert max(R["z"].values()) < 4.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
