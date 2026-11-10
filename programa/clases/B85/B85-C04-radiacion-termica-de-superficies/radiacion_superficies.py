# SPDX-License-Identifier: Apache-2.0
"""B85-C04: radiación térmica: Planck, Wien, fracciones de banda e intercambio entre superficies.

Consultado: SIGMA (NIST CODATA 2022). Constantes h, k_B, c exactas del SI (no consultadas aquí; se contrastan con SIGMA).
ILUSTRATIVO: temperaturas, emisividades y geometrías.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *


def planck(lam, T):
    """Exitancia espectral M_lambda [W m^-3] de un cuerpo negro."""
    x = H_P * C_L / (lam * K_B * T)
    if x > 700:
        return 0.0
    return 2 * math.pi * H_P * C_L ** 2 / lam ** 5 / math.expm1(x)


def integrar(T, l_min, l_max, n=20000):
    """Integral de M_lambda entre l_min y l_max con regla de Simpson en escala logaritmica."""
    a, b = math.log(l_min), math.log(l_max)
    h = (b - a) / n
    s = 0.0
    for i in range(n + 1):
        u = a + i * h
        lam = math.exp(u)
        f = planck(lam, T) * lam
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * f
    return s * h / 3


def sigma_desde_constantes():
    return 2 * math.pi ** 5 * K_B ** 4 / (15 * H_P ** 3 * C_L ** 2)


def constante_wien():
    """Raiz de x = 5 (1 - e^-x) y b = h c / (k x)."""
    x = biseccion(lambda x: x - 5 * (1 - math.exp(-x)), 4.0, 6.0)
    return H_P * C_L / (K_B * x)


def maximo_numerico(T):
    a, b = 0.1e-6, 100e-6
    gr = (math.sqrt(5) - 1) / 2
    c1, d1 = b - gr * (b - a), a + gr * (b - a)
    for _ in range(200):
        if planck(c1, T) > planck(d1, T):
            b = d1
        else:
            a = c1
        c1, d1 = b - gr * (b - a), a + gr * (b - a)
    return 0.5 * (a + b)


def fraccion(T, l1, l2):
    return integrar(T, l1, l2) / (SIGMA * T ** 4)


def placas_paralelas(t1, t2, e1, e2):
    return SIGMA * (t1 ** 4 - t2 ** 4) / (1 / e1 + 1 / e2 - 1)


def esferas_concentricas(t1, t2, e1, e2, r1, r2):
    return SIGMA * (t1 ** 4 - t2 ** 4) / (1 / e1 + (r1 / r2) ** 2 * (1 / e2 - 1))


def calcular():
    r = {}
    r["sigma_calc"] = sigma_desde_constantes()
    r["b_wien"] = constante_wien()
    r["lam_max_300"] = maximo_numerico(300.0)
    r["lam_max_5772"] = maximo_numerico(5772.0)
    r["int_300"] = integrar(300.0, 0.05e-6, 2000e-6)
    r["sig_300"] = SIGMA * 300.0 ** 4
    r["f_sol_vis"] = fraccion(5772.0, 0.4e-6, 0.7e-6)
    r["f_sol_25"] = fraccion(5772.0, 0.05e-6, 2.5e-6)
    r["f_300_mayor_4"] = fraccion(300.0, 4e-6, 2000e-6)
    r["q_placas"] = placas_paralelas(300.0, 200.0, 0.8, 0.8)
    r["q_placas_e1"] = placas_paralelas(300.0, 200.0, 0.05, 0.05)
    r["q_esferas"] = esferas_concentricas(300.0, 200.0, 0.8, 0.8, 0.3, 0.5)
    r["q_esferas_lim"] = esferas_concentricas(300.0, 200.0, 0.8, 0.8, 0.3, 1e6)
    r["q_negro_sin_cavidad"] = SIGMA * (300.0 ** 4 - 200.0 ** 4)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"sigma desde h, k, c = {r['sigma_calc']:.9e} ; sigma (NIST) = {SIGMA:.9e} ; dif. relativa = {abs(r['sigma_calc']-SIGMA)/SIGMA:.2e}")
    print(f"b de Wien = {r['b_wien']*1e3:.6f} mm K ; lambda_max(300 K) = {r['lam_max_300']*1e6:.3f} um (b/T = {r['b_wien']/300*1e6:.3f}) ; lambda_max(5772 K) = {r['lam_max_5772']*1e6:.4f} um")
    print(f"Integral de Planck a 300 K = {r['int_300']:.4f} W/m2 ; sigma T^4 = {r['sig_300']:.4f} W/m2")
    print(f"Fraccion de un cuerpo negro de 5772 K (ILUSTRATIVO como Sol): visible 0.4-0.7 um = {r['f_sol_vis']:.4f} ; < 2.5 um = {r['f_sol_25']:.4f}")
    print(f"Fraccion de un cuerpo negro de 300 K con lambda > 4 um = {r['f_300_mayor_4']:.5f}")
    print(f"Placas paralelas 300 K / 200 K: eps = 0.8 -> {r['q_placas']:.2f} W/m2 ; eps = 0.05 -> {r['q_placas_e1']:.3f} W/m2 ; negras -> {r['q_negro_sin_cavidad']:.2f} W/m2")
    print(f"Esferas concentricas (r1 = 0.3, r2 = 0.5, eps = 0.8): {r['q_esferas']:.2f} W/m2 (por area interior) ; limite r2 -> infinito: {r['q_esferas_lim']:.2f} W/m2 = eps sigma (T1^4 - T2^4)")
    comprobar(abs(r["sigma_calc"] - SIGMA) / SIGMA < 1e-8, "sigma")
    comprobar(abs(r["lam_max_300"] - r["b_wien"] / 300.0) / r["lam_max_300"] < 1e-6, "Wien")
    comprobar(abs(r["int_300"] - r["sig_300"]) / r["sig_300"] < 1e-4, "integral de Planck")
    comprobar(abs(r["q_esferas_lim"] - 0.8 * r["q_negro_sin_cavidad"]) < 1e-3, "limite de esferas")
    fin()


if __name__ == "__main__":
    main()
