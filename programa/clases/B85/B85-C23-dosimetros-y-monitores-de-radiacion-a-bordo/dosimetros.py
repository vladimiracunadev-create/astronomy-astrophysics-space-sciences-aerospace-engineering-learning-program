# SPDX-License-Identifier: Apache-2.0
"""B85-C23: dosímetro de a bordo: calibración, límite de detección y corrección por tiempo muerto.

Todo SINTÉTICO (semilla fija): respuesta de un RadFET ΔV = a D^b con ruido, contador con tiempo muerto.
Consultado: nada. Segunda vía: ajuste log-log por mínimos cuadrados cerrado frente a búsqueda directa del exponente.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

A_V, B_V = 0.012, 0.85          # V / Gy^b (sintético)
RUIDO = 0.002                   # V (sintético)
SEMILLA = 20261110
TAU_MUERTO = 5e-6               # s (sintético)


def datos():
    rng = random.Random(SEMILLA)
    dosis = [0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    dv = [A_V * d ** B_V + rng.gauss(0.0, RUIDO) for d in dosis]
    return dosis, dv


def ajuste_loglog(dosis, dv):
    x = [math.log(d) for d in dosis]
    y = [math.log(v) for v in dv]
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    b = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / sum((xi - mx) ** 2 for xi in x)
    a = math.exp(my - b * mx)
    return a, b


def ajuste_directo(dosis, dv):
    """Busqueda en b y a por minimos cuadrados lineales en a para cada b (sin linealizar con logaritmos)."""
    mejor = None
    for k in range(0, 2001):
        b = 0.5 + k * 0.0005
        g = [d ** b for d in dosis]
        a = sum(gi * vi for gi, vi in zip(g, dv)) / sum(gi * gi for gi in g)
        sse = sum((vi - a * gi) ** 2 for gi, vi in zip(g, dv))
        if mejor is None or sse < mejor[0]:
            mejor = (sse, a, b)
    return mejor[1], mejor[2]


def corregir_muerto(m, tau=TAU_MUERTO):
    return m / (1.0 - m * tau)


def calcular():
    r = {}
    d, v = datos()
    r["d"], r["v"] = d, v
    r["a1"], r["b1"] = ajuste_loglog(d, v)
    r["a2"], r["b2"] = ajuste_directo(d, v)
    r["limite_det"] = (3 * RUIDO / r["a2"]) ** (1.0 / r["b2"])
    r["sens_1Gy"] = r["a2"] * r["b2"]
    r["dosis_de_dv"] = lambda dv: (dv / r["a2"]) ** (1.0 / r["b2"])
    r["d_para_20mV"] = (0.020 / r["a2"]) ** (1.0 / r["b2"])
    r["res_rms"] = math.sqrt(sum((vi - r["a2"] * di ** r["b2"]) ** 2 for di, vi in zip(d, v)) / len(d))
    # contador con tiempo muerto
    verdaderas = [1e3, 1e4, 5e4, 1e5]
    r["muerto"] = []
    for n in verdaderas:
        m = n / (1 + n * TAU_MUERTO)          # paralizable aproximado a no paralizable
        r["muerto"].append((n, m, corregir_muerto(m)))
    # estadistica de Poisson: incertidumbre relativa de contar N cuentas
    r["poisson"] = [(n, 1 / math.sqrt(n)) for n in (100, 1000, 10000)]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Respuesta SINTETICA: dV = {A_V} D^{B_V} V (D en Gy), ruido gaussiano {RUIDO*1e3:.0f} mV, semilla {SEMILLA}")
    print("D [Gy]    dV [V]")
    for d, v in zip(r["d"], r["v"]):
        print(f"{d:7.1f}   {v:.4f}")
    print(f"Ajuste log-log: a = {r['a1']:.5f}, b = {r['b1']:.4f} ; ajuste directo: a = {r['a2']:.5f}, b = {r['b2']:.4f} (verdaderos {A_V}, {B_V})")
    print(f"RMS del residuo = {r['res_rms']*1e3:.2f} mV ; limite de deteccion (3 sigma) = {r['limite_det']:.3f} Gy ; D para 20 mV = {r['d_para_20mV']:.3f} Gy")
    print(f"Tiempo muerto {TAU_MUERTO*1e6:.0f} us: " + "; ".join(f"verdadera {n:.0f}/s -> medida {m:.1f}/s -> corregida {c:.1f}/s" for n, m, c in r["muerto"]))
    print("Incertidumbre de Poisson: " + "; ".join(f"N = {n}: {u*100:.1f} %" for n, u in r["poisson"]))
    comprobar(abs(r["b2"] - B_V) < 0.05, "exponente")
    comprobar(abs(r["a2"] - A_V) / A_V < 0.10, "coeficiente")
    comprobar(all(abs(c - n) / n < 1e-9 for n, m, c in r["muerto"]), "correccion de tiempo muerto")
    fin()


if __name__ == "__main__":
    main()
