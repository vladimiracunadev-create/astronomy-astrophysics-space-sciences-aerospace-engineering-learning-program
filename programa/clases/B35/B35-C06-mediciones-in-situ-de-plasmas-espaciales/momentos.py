#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C06: momentos de una distribucion reducida desde cuentas con ruido de Poisson, truncamiento de la ventana de energia y potencial de la nave.

Datos: k_B y m_p (NIST CODATA 2022, tabla allascii.txt, consultados 2026-11-09). Los parametros del viento (densidad 5 cm^-3, velocidad 400 km/s, T = 1e5 K), la ventana de medida, la tasa de
cuentas y el potencial de la nave son ILUSTRATIVOS (sinteticos); no representan ningun instrumento ni mision reales.
Modelo: distribucion reducida 1D de protones F(v) = n N(v; V, sigma^2) con sigma^2 = kT/m, medida en bins de velocidad (ancho dv). Las cuentas de cada bin son Poisson con media
proporcional a F dv (semilla 20261109, 300 realizaciones). Momentos: n = sum(c)/g, V = sum(c v)/sum(c), T = m sum(c (v-V)^2)/(k sum(c)).
Casos: (1) ventana amplia (error estadistico comparado con sigma_V = sigma/sqrt(N)); (2) ventana truncada que corta la cola; (3) corrimiento de la escala de velocidad por un potencial de la nave.
Supuestos: sin ruido de fondo, respuesta ideal, bins independientes. Validez: ilustrativa.
Tolerancia: sesgo medio de V consistente con 0 dentro de 3 errores estandar; desviacion de V entre realizaciones igual a sigma/sqrt(N) con error < 15 %; sesgo de T con ventana truncada
frente a la integral analitica de la gaussiana truncada con error < 5 % del sesgo; sesgo de T en la ventana amplia consistente con 0 dentro de 3 errores estandar.
"""
from __future__ import annotations
import math, platform, random, sys

K_B = 1.380649e-23
M_P = 1.67262192595e-27

def poisson(rng, lam):
    if lam < 50:
        L = math.exp(-lam); k = 0; p = 1.0
        while True:
            p *= rng.random()
            if p <= L:
                return k
            k += 1
    return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))

def momentos(cuentas, v, m=M_P):
    N = sum(cuentas)
    V = sum(c * x for c, x in zip(cuentas, v)) / N
    var = sum(c * (x - V) ** 2 for c, x in zip(cuentas, v)) / N
    return N, V, m * var / K_B

def medir(rng, centro, sigma, V0, N_total, vmin, vmax, dv, corrimiento=0.0):
    """Cuentas esperadas en bins [vmin, vmax]; la escala medida esta corrida 'corrimiento' respecto de la verdadera."""
    nb = int(round((vmax - vmin) / dv))
    v = [vmin + (i + 0.5) * dv for i in range(nb)]
    cu = []
    for x in v:
        xv = x + corrimiento  # velocidad verdadera que cae en ese bin
        f = math.exp(-0.5 * ((xv - V0) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))
        cu.append(poisson(rng, N_total * f * dv))
    return v, cu

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    T = 1e5
    sigma = math.sqrt(K_B * T / M_P)
    V0 = 400e3
    dv = sigma / 5
    print(f"sigma_termica = {sigma/1e3:.3f} km/s ; dv = {dv/1e3:.3f} km/s ; V0 = {V0/1e3:.0f} km/s")
    rng = random.Random(20261109)
    Ntot, R = 20000, 300
    # (1) ventana amplia
    Vs, Ts, Ns = [], [], []
    for _ in range(R):
        v, c = medir(rng, V0, sigma, V0, Ntot, V0 - 6 * sigma, V0 + 6 * sigma, dv)
        N, V, Tm = momentos(c, v)
        Vs.append(V); Ts.append(Tm); Ns.append(N)
    mV = sum(Vs) / R; sdV = math.sqrt(sum((x - mV) ** 2 for x in Vs) / (R - 1))
    mT = sum(Ts) / R; sdT = math.sqrt(sum((x - mT) ** 2 for x in Ts) / (R - 1))
    sigV_an = sigma / math.sqrt(Ntot)
    sigT_an = T * math.sqrt(2.0 / Ntot)
    print(f"(1) ventana +-6 sigma: V medio - V0 = {(mV-V0):.1f} m/s (error estandar {sdV/math.sqrt(R):.1f}) ; desv(V) = {sdV:.1f} m/s (sigma/sqrt(N) = {sigV_an:.1f}) ; T medio = {mT:.0f} K ; desv(T) = {sdT:.0f} K (T sqrt(2/N) = {sigT_an:.0f})")
    assert abs(mV - V0) < 3 * sdV / math.sqrt(R)
    assert abs(sdV / sigV_an - 1) < 0.15 and abs(sdT / sigT_an - 1) < 0.15
    # el muestreo del integrando en el centro del bin (suma de Riemann) no sesga T: el sesgo debe ser compatible con 0
    print(f"    sesgo de T = {mT - T:.1f} K (error estandar {sdT/math.sqrt(R):.1f} K)")
    assert abs(mT - T) < 3 * sdT / math.sqrt(R)
    # (2) ventana truncada: solo se mide de V0 - 1 sigma a V0 + 3 sigma (corta la cola de baja velocidad)
    a, b = -1.0, 3.0
    # momentos analiticos de la gaussiana truncada
    phi = lambda z: math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)
    Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
    Zn = Phi(b) - Phi(a)
    mu_t = (phi(a) - phi(b)) / Zn
    var_t = 1 + (a * phi(a) - b * phi(b)) / Zn - mu_t ** 2
    T_t_an = T * var_t
    Ts2, Vs2 = [], []
    for _ in range(R):
        v, c = medir(rng, V0, sigma, V0, Ntot, V0 + a * sigma, V0 + b * sigma, dv)
        N, V, Tm = momentos(c, v)
        Ts2.append(Tm); Vs2.append(V)
    mT2 = sum(Ts2) / R; mV2 = sum(Vs2) / R
    print(f"(2) ventana [-1, +3] sigma: T medio = {mT2:.0f} K (analitico del truncamiento {T_t_an:.0f} K, razon {mT2/T:.3f}) ; V medio - V0 = {(mV2-V0)/1e3:.3f} km/s (analitico {mu_t*sigma/1e3:.3f})")
    assert abs((mT2 - T) / (T_t_an - T) - 1) < 0.05 and abs((mV2 - V0) - mu_t * sigma) < 0.05 * sigma
    # (3) corrimiento de escala por potencial de la nave: v_medida = v_verdadera - dv_phi ; para protones con phi = +10 V
    phi_nave = 10.0
    v_phi = math.sqrt(2 * 1.602176634e-19 * phi_nave / M_P)
    Vcorr = (V0 ** 2 - v_phi ** 2)
    print(f"(3) potencial de la nave de +10 V: la energia por carga medida difiere en 10 eV ; sobre 400 km/s (E = {0.5*M_P*V0**2/1.602176634e-19:.0f} eV) la velocidad aparente cambia en {(math.sqrt(V0**2 + v_phi**2)-V0)/1e3:.3f} km/s")
    ea = 0.5 * M_P * V0 ** 2 / 1.602176634e-19
    va = math.sqrt(2 * (ea + phi_nave) * 1.602176634e-19 / M_P)
    assert abs(va - math.sqrt(V0 ** 2 + v_phi ** 2)) < 1e-6 * V0
    assert 0.0 < va - V0 < 0.05 * sigma + 1e3
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
