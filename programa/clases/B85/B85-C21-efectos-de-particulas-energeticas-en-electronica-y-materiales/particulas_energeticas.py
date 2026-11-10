# SPDX-License-Identifier: Apache-2.0
"""B85-C21: efectos de partículas energéticas en electrónica: tasa de eventos únicos y probabilidad de upset.

Consultado: nada (ver fuentes de la clase). ILUSTRATIVO y SINTÉTICO: sección eficaz de Weibull, espectro de LET integral Φ(>L) = Φ1 L^-2,
número de bits, duración de la misión.
Segunda vía: integral numérica (Simpson logarítmico) frente a Monte Carlo con semilla fija (muestreo Pareto del LET).
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

SIG_SAT, L0, W, S_W = 1.0e-7, 1.5, 20.0, 1.5       # cm2/bit, MeV cm2/mg, -, -
PHI1 = 1.0e-6                                       # cm-2 s-1 con LET > 1 MeV cm2/mg (ilustrativo)
L_MIN, L_MAX = 1.0, 100.0
BITS = 8 * 1024 * 1024 * 8                          # 64 Mbit
SEMILLA = 20261110


def sigma(l, sat=SIG_SAT, l0=L0):
    if l <= l0:
        return 0.0
    return sat * (1.0 - math.exp(-(((l - l0) / W) ** S_W)))


def tasa_bit(sat=SIG_SAT, l0=L0, phi1=PHI1):
    """Integral de sigma(L) * dPhi/dL, con dPhi/dL = 2 Phi1 L^-3, entre L_MIN y L_MAX (Simpson en ln L)."""
    n = 40000
    a, b = math.log(L_MIN), math.log(L_MAX)
    h = (b - a) / n
    s = 0.0
    for i in range(n + 1):
        l = math.exp(a + i * h)
        f = sigma(l, sat, l0) * 2 * phi1 * l ** -3 * l
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * f
    return s * h / 3


def tasa_mc(n=400000):
    rng = random.Random(SEMILLA)
    suma = 0.0
    for _ in range(n):
        l = L_MIN * (1.0 - rng.random()) ** (-0.5)    # Pareto: P(>L) = (L/L_MIN)^-2
        if l <= L_MAX:
            suma += sigma(l)
    return PHI1 * suma / n


def calcular():
    r = {}
    r["tasa_bit"] = tasa_bit()
    r["tasa_mc"] = tasa_mc()
    r["sat_max"] = SIG_SAT * PHI1
    r["tasa_disp_s"] = r["tasa_bit"] * BITS
    r["por_dia"] = r["tasa_disp_s"] * 86400
    r["por_anio"] = r["tasa_disp_s"] * YEAR
    r["p_1_anio"] = 1 - math.exp(-r["por_anio"])
    r["p_5_anios"] = 1 - math.exp(-5 * r["por_anio"])
    r["tasa_umbral_alto"] = tasa_bit(l0=10.0)
    r["cociente_umbral"] = r["tasa_umbral_alto"] / r["tasa_bit"]
    r["tasa_sat_mitad"] = tasa_bit(sat=0.5 * SIG_SAT)
    r["mtbf_dias"] = 1.0 / r["por_dia"] if r["por_dia"] > 0 else float("inf")
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Weibull ILUSTRATIVA: sigma_sat = {SIG_SAT:.0e} cm2/bit, L0 = {L0} MeV cm2/mg, W = {W}, s = {S_W} ; espectro Phi(>L) = {PHI1:.0e} L^-2 cm-2 s-1")
    print(f"Memoria de {BITS/1e6:.0f} Mbit")
    print(f"Tasa por bit: Simpson = {r['tasa_bit']:.4e} s-1 ; Monte Carlo (4e5 muestras, semilla {SEMILLA}) = {r['tasa_mc']:.4e} s-1 ; cota sigma_sat*Phi1 = {r['sat_max']:.1e}")
    print(f"Por dispositivo: {r['tasa_disp_s']:.4e} s-1 = {r['por_dia']:.4f} por dia = {r['por_anio']:.2f} por anio ; MTBF = {r['mtbf_dias']:.1f} dias")
    print(f"Probabilidad de al menos un upset: 1 anio {r['p_1_anio']*100:.2f} % ; 5 anios {r['p_5_anios']*100:.4f} %")
    print(f"Con umbral L0 = 10 la tasa cae a {r['cociente_umbral']*100:.1f} % ; con sigma_sat a la mitad, {r['tasa_sat_mitad']/r['tasa_bit']*100:.1f} %")
    comprobar(abs(r["tasa_mc"] - r["tasa_bit"]) / r["tasa_bit"] < 0.03, "Monte Carlo frente a integral")
    comprobar(r["tasa_bit"] < r["sat_max"], "cota")
    fin()


if __name__ == "__main__":
    main()
