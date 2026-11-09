#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C06: respuesta de un interferometro de Michelson y limite del ruido de disparo.

Datos: h, c (NIST CODATA 2022), consultados 2026-11-09. Contexto: Advanced LIGO es un Michelson con brazos de 4 km,
cavidades Fabry-Perot en los brazos y reciclaje de potencia y de senal (arXiv:1411.4547, resumen). La longitud de onda
(1064 nm), la potencia, la ganancia de cavidad y la frecuencia de la onda son ILUSTRATIVAS (sinteticas).
Modelo: potencia en el puerto oscuro P_oscuro = P0 sen^2(dphi/2) con dphi = 4 pi (L1 - L2)/lambda (Michelson). Una onda
con deformacion h cambia L1 - L2 en h L; con una cavidad de ganancia N (numero medio de viajes de ida y vuelta) el
cambio de fase se multiplica por N. Ruido de disparo: varianza de la fase 1/(2 N_foton) sobre un tiempo de integracion;
deformacion minima detectable h_min = lambda/(4 pi N L) sqrt(h c/(2 lambda eta P tau))... aqui se usa
dphi_min = 1/sqrt(N_fot) con N_fot = eta P tau lambda/(h c).
Se verifica por Monte Carlo (semilla fija) que la desviacion de la fase estimada de conteos Poisson coincide con 1/sqrt(N_fot).
Supuestos: Michelson ideal, sin ruido tecnico, contraste perfecto, onda en la banda plana. Validez: ilustrativa.
Tolerancia: 5 % entre la desviacion Monte Carlo y 1/sqrt(N_fot).
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

H, C = 6.62607015e-34, 299792458.0


def poisson(lam, rng):
    if lam > 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lam, L, p0, eta, tau, n_gan = 1064e-9, 4000.0, 100.0, 1.0, 1.0, 300.0
    e_fot = H * C / lam
    n_fot = eta * p0 * tau / e_fot
    print(f"energia de un foton = {e_fot:.4e} J ; fotones en {tau} s con {p0} W: {n_fot:.4e}")
    d_phi_min = 1 / math.sqrt(n_fot)
    h_min = d_phi_min * lam / (4 * math.pi * n_gan * L)
    print(f"fase minima por ruido de disparo = {d_phi_min:.4e} rad ; h_min = {h_min:.4e} (ganancia {n_gan:.0f}, L = {L:.0f} m)")
    # respuesta: fase por una onda de h dada
    for h in (1e-21, 1e-22):
        dl = h * L
        dphi = 4 * math.pi * n_gan * dl / lam
        print(f"h = {h:.0e}: dL = {dl:.3e} m ; dphi = {dphi:.3e} rad ; dphi/fase minima = {dphi / d_phi_min:.3e}")
    # escala con potencia y con ganancia
    h_min4 = (1 / math.sqrt(4 * n_fot)) * lam / (4 * math.pi * n_gan * L)
    print(f"h_min con 4x potencia: {h_min4:.4e} (cociente {h_min4 / h_min:.4f}, esperado 0.5)")
    assert abs(h_min4 / h_min - 0.5) < 1e-12
    # Monte Carlo: estimar la fase del puerto oscuro a partir de conteos Poisson (franja a media luz)
    rng = random.Random(20261109)
    n_prueba = 4.0e4        # fotones esperados en el puerto en el punto de trabajo
    phi0 = math.pi / 2      # punto de media intensidad
    dphi_true = 2.0e-3
    est = []
    for _ in range(2000):
        mu = n_prueba * math.sin((phi0 + dphi_true) / 2) ** 2 * 2     # normalizado: P(phi0)=n_prueba
        k = poisson(mu, rng)
        # inversion: sen^2(phi/2) = k/(2 n_prueba) -> phi
        s = min(max(k / (2 * n_prueba), 0.0), 1.0)
        est.append(2 * math.asin(math.sqrt(s)) - phi0)
    media, desv = statistics.mean(est), statistics.pstdev(est)
    # derivada de la potencia respecto de la fase en phi0: dP/dphi = n_prueba*... -> sigma_phi = sqrt(P)/(dP/dphi)
    p_dark = n_prueba * 2 * math.sin(phi0 / 2) ** 2
    dpdphi = n_prueba * 2 * math.sin(phi0 / 2) * math.cos(phi0 / 2)
    esp = math.sqrt(p_dark) / dpdphi
    print(f"Monte Carlo: fase inyectada {dphi_true:.1e} rad ; media estimada = {media:.4e} ; desviacion = {desv:.4e} ; esperada sqrt(P)/(dP/dphi) = {esp:.4e}")
    assert abs(desv / esp - 1) < 0.05, "ruido de disparo"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
