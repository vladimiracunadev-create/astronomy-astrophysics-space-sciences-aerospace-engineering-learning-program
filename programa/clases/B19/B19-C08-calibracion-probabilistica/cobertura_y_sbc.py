#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C08: cobertura, calibracion basada en simulacion (SBC) y fiabilidad.

Datos: SIMULADOS (semilla fija); no hay datos observados.
Modelo generador "de verdad": theta ~ N(m_v, 1); y | theta ~ N(theta, s_v^2).
Modelo del analista: prior theta ~ N(0, 1); verosimilitud con desviacion s_a.
Posterior del analista (exacta): precision 1 + 1/s_a^2; media (y/s_a^2)/precision.
Escenarios:
  1 BIEN        : m_v = 0, s_v = 1, s_a = 1   (analista = verdad)
  2 PRIOR MAL   : m_v = 2, s_v = 1, s_a = 1   (el prior del analista no cubre la realidad)
  3 RUIDO MAL   : m_v = 0, s_v = 1, s_a = 0.5 (analista subestima el ruido)
Se repite R = 20 000 veces: se sortea theta, y; se calcula el intervalo central
al 90 % y la cobertura; en SBC se sortean L = 99 valores de la posterior y se
cuenta el rango de theta entre ellos (0..99, en 10 casillas).
Teoria: con modelo correcto la cobertura nominal es exacta y los rangos son
uniformes (Talts et al. 2018). Error estandar MC de la cobertura ~ 0.0021.
Fiabilidad: p ~ U(0.02, 0.98); resultado ~ Bernoulli(p) (calibrado) o pronostico
sobreconfiado p' = expit(2 logit(p)) para el mismo resultado.
Supuestos: normalidad; independencia entre repeticiones.
Validez: ilustra el diagnostico, no valida un software concreto.
Tolerancia: cobertura del escenario 1 = 0.90 +- 0.01 y de los escenarios 2 y 3 a 0.01 de su valor exacto; chi-cuadrado de rangos (9 g.l.)
< 27.88 (percentil 99.9 %) en el escenario 1 y > 27.88 en 2 y 3.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

Z90 = 1.6448536269514722        # cuantil 0.95 de N(0,1) (valor de referencia conocido)


def escenario(mv, sv, sa, rng, R=20_000, L=99):
    theta = rng.normal(mv, 1.0, size=R)
    y = rng.normal(theta, sv)
    prec = 1.0 + 1.0 / sa ** 2
    m = (y / sa ** 2) / prec
    sd = 1.0 / math.sqrt(prec)
    cobertura = float((np.abs(theta - m) <= Z90 * sd).mean())
    draws = rng.normal(m[:, None], sd, size=(R, L))
    rank = (draws < theta[:, None]).sum(axis=1)                   # 0..L
    hist = np.bincount((rank * 10) // (L + 1), minlength=10)
    esperado = R / 10.0
    chi2 = float(((hist - esperado) ** 2 / esperado).sum())
    return cobertura, hist, chi2


def expit(x):
    return 1.0 / (1.0 + np.exp(-x))


def fiabilidad(rng, N=200_000):
    p = rng.uniform(0.02, 0.98, size=N)
    ocurre = rng.uniform(size=N) < p
    p_sobre = expit(2.0 * np.log(p / (1 - p)))
    filas = []
    for nom, f in (("calibrado", p), ("sobreconfiado", p_sobre)):
        b = np.minimum((f * 10).astype(int), 9)
        filas.append((nom, [(float(f[b == k].mean()), float(ocurre[b == k].mean())) for k in range(10)]))
    return filas


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    rng = np.random.default_rng(2026)
    res = {}
    for nom, (mv, sv, sa) in (("1 BIEN", (0.0, 1.0, 1.0)), ("2 PRIOR MAL", (2.0, 1.0, 1.0)),
                              ("3 RUIDO MAL", (0.0, 1.0, 0.5))):
        res[nom] = escenario(mv, sv, sa, rng)
    assert abs(res["1 BIEN"][0] - 0.90) < 0.01, res["1 BIEN"][0]
    assert res["1 BIEN"][2] < 27.88 and res["2 PRIOR MAL"][2] > 27.88 and res["3 RUIDO MAL"][2] > 27.88
    # coberturas exactas (calculo propio): theta - m ~ N(mu_e, s_e^2) y cobertura = P(|theta-m| <= Z90 sd_post)
    phi = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
    c2 = phi((Z90 * math.sqrt(0.5) - 1.0) / math.sqrt(0.5)) - phi((-Z90 * math.sqrt(0.5) - 1.0) / math.sqrt(0.5))
    c3 = 2 * phi(Z90 / math.sqrt(5) / math.sqrt(0.68)) - 1
    assert abs(res["2 PRIOR MAL"][0] - c2) < 0.01 and abs(res["3 RUIDO MAL"][0] - c3) < 0.01, (c2, c3)
    print(f"Pruebas: OK (coberturas exactas: escenario 2 = {c2:.4f}, escenario 3 = {c3:.4f})\n")
    print(f"{'escenario':<14}{'cobertura 90 %':>16}{'chi2 rangos':>13}   casillas SBC (10 de 99 rangos)")
    for nom, (cob, hist, chi2) in res.items():
        print(f"{nom:<14}{cob:16.4f}{chi2:13.1f}   {' '.join(f'{h:5d}' for h in hist)}")
    print("\nDiagrama de fiabilidad (casilla: pronostico medio -> frecuencia observada)")
    for nom, filas in fiabilidad(np.random.default_rng(9)):
        print(f"  {nom}: " + "  ".join(f"{a:.2f}->{b:.2f}" for a, b in filas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
