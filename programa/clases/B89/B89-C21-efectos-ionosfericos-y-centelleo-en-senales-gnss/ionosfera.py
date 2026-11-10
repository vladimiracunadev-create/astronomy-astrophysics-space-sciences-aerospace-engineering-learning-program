#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C21. Efectos ionosfericos y centelleo en senales GNSS: retardo de primer orden 40.3 TEC/f^2, factor de oblicuidad,
combinacion libre de ionosfera y desvanecimiento por centelleo (indice S4, distribucion de Nakagami-m). TEC, ruido y frecuencias ILUSTRATIVOS;
la constante 40.3 y las frecuencias usuales NO se consultaron (Navipedia no estuvo disponible). Semilla 89."""
import math, random, sys

C = 299_792_458.0
F1, F2 = 1575.42e6, 1227.60e6     # Hz, valores usuales ILUSTRATIVOS, no consultados
K40 = 40.3                         # m3/s2? (m Hz^2 / (el/m2)), relacion estandar, no consultada
TECU = 1e16                        # electrones/m2
RE, HI = 6371e3, 350e3             # m, ILUSTRATIVOS

def retardo(tec_tecu, f):
    return K40 * tec_tecu * TECU / f ** 2

def oblicuidad(elev_deg):
    e = math.radians(elev_deg)
    return 1.0 / math.sqrt(1 - (RE * math.cos(e) / (RE + HI)) ** 2)

def libre_iono(p1, p2):
    return (F1 ** 2 * p1 - F2 ** 2 * p2) / (F1 ** 2 - F2 ** 2)

def desvanecimiento(s4, n, rng):
    """Potencia relativa con distribucion gamma de forma m = 1/S4^2 y media 1 (Nakagami-m)."""
    m = 1.0 / s4 ** 2
    return [rng.gammavariate(m, 1.0 / m) for _ in range(n)]

def calcular():
    R = {}
    R["delay_zenit"] = {t: (retardo(t, F1), retardo(t, F2)) for t in (10, 50, 100)}
    R["obl"] = {e: oblicuidad(e) for e in (90, 45, 20, 10, 5)}
    R["delay_20"] = retardo(50, F1) * R["obl"][20]
    # combinacion libre de ionosfera
    rng = random.Random(89)
    rho = 22_000_000.0
    tec = 50.0
    sigma = 0.3
    errores_if, errores_l1 = [], []
    for _ in range(20000):
        p1 = rho + retardo(tec, F1) + rng.gauss(0, sigma)
        p2 = rho + retardo(tec, F2) + rng.gauss(0, sigma)
        errores_if.append(libre_iono(p1, p2) - rho)
        errores_l1.append(p1 - rho)
    media = lambda v: sum(v) / len(v)
    desv = lambda v: math.sqrt(sum((x - media(v)) ** 2 for x in v) / len(v))
    R["if_media"], R["if_sigma"] = media(errores_if), desv(errores_if)
    R["l1_media"], R["l1_sigma"] = media(errores_l1), desv(errores_l1)
    R["amp"] = math.sqrt(F1 ** 4 + F2 ** 4) / (F1 ** 2 - F2 ** 2)
    R["if_sigma_teo"] = sigma * R["amp"]
    R["f2_f1"] = retardo(1, F2) / retardo(1, F1)
    # centelleo
    R["scint"] = {}
    for s4 in (0.3, 0.6, 1.0):
        x = desvanecimiento(s4, 100_000, rng)
        m = media(x)
        var = sum((v - m) ** 2 for v in x) / len(x)
        bajo10 = sum(1 for v in x if v < 0.1) / len(x)
        R["scint"][s4] = (m, math.sqrt(var) / m, bajo10)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print("ILUSTRATIVO: L1 = 1575.42 MHz, L2 = 1227.60 MHz (valores usuales, no consultados); delta = 40.3 TEC / f^2")
    print(f"{'TEC [TECU]':>11s}{'retardo L1 [m]':>16s}{'retardo L2 [m]':>16s}")
    for t, (a, b) in R["delay_zenit"].items():
        print(f"{t:11d}{a:16.3f}{b:16.3f}")
    print(f"Retardo L2 / L1 = {R['f2_f1']:.4f} = (f1/f2)^2")
    print("Factor de oblicuidad (capa fina a 350 km):", ", ".join(f"{e} grados: {v:.3f}" for e, v in R["obl"].items()))
    print(f"Retardo L1 con 50 TECU a 20 grados de elevacion = {R['delay_20']:.3f} m")
    print("Combinacion libre de ionosfera con sigma = 0.3 m por frecuencia, TEC = 50 TECU (20000 ensayos):")
    print(f"  L1 sola: sesgo = {R['l1_media']:.3f} m ; sigma = {R['l1_sigma']:.3f} m")
    print(f"  L1/L2 libre: sesgo = {R['if_media']:+.4f} m ; sigma = {R['if_sigma']:.3f} m ; teoria = {R['amp']:.4f} x sigma = {R['if_sigma_teo']:.3f} m")
    print("Centelleo (Nakagami-m, m = 1/S4^2, 100000 muestras): S4 -> media, S4 medido, P(potencia < -10 dB)")
    for s4, (m, s, p) in R["scint"].items():
        print(f"  S4 = {s4:.1f}: media = {m:.4f} ; S4 medido = {s:.4f} ; P(< -10 dB) = {p:.4f}")
    assert abs(R["f2_f1"] - (F1 / F2) ** 2) < 1e-12
    assert abs(R["if_media"]) < 0.02 and abs(R["if_sigma"] - R["if_sigma_teo"]) / R["if_sigma_teo"] < 0.03
    for s4, (m, s, p) in R["scint"].items():
        assert abs(m - 1) < 0.02 and abs(s - s4) / s4 < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
