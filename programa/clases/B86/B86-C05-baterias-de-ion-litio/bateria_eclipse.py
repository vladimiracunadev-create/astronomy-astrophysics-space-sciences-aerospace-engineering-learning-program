#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C05: dimensionamiento de una bateria de ion-litio SINTETICA para el eclipse de una orbita baja.

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC); energia especifica de celdas Li-ion
comerciales de 150 a 270 Wh/kg y de paquetes de 91 a 250 Wh/kg a 3.6 V medios (tabla del estado del arte de la NASA, solo como rango).
ILUSTRATIVOS (sinteticos, no medidos): celda de 3.0 Ah, 3.6 V nominales, resistencia interna 0.05 ohm, OCV lineal de 3.3 a 4.1 V
con el estado de carga, 8 celdas en serie, paquete de 120 Wh/kg, eficiencia de descarga 0.95, perdida de capacidad al fin de vida 20 %,
carga en eclipse 64.8 W (resultado de B86-C01), vida de 5 anos, vida en ciclos N = 3000 (0.8/DoD)^1.6 (ley ilustrativa).
Modelo: la energia del eclipse sale de la bateria a potencia constante; DoD requerida para N ciclos resuelta en forma cerrada y por biseccion.
Segunda via: simulacion de la descarga (cuenta de Coulomb con OCV y resistencia) para comparar el DoD real con el planificado.
Tolerancia: DoD cerrada frente a biseccion < 1e-12; DoD simulado menor que el planificado (la tension nominal de 3.6 V es conservadora a SOC alto) y a menos de 15 % relativo.
"""
from __future__ import annotations
import math, platform

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
TE = math.asin(RE / A) / math.pi * T
PE, ETA_D, FADE, ANOS = 64.8, 0.95, 0.20, 5.0
NS, CAP_AH, VNOM, RINT, WHKG = 8, 3.0, 3.6, 0.05, 120.0


def ciclos(dod):
    return 3000.0 * (0.8 / dod) ** 1.6


def dod_cerrada(n):
    return 0.8 * (3000.0 / n) ** (1.0 / 1.6)


def dod_biseccion(n):
    lo, hi = 0.01, 0.8
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if ciclos(m) > n:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def ocv(s):
    return 3.3 + 0.8 * s


def simular(np_):
    """Descarga a potencia constante en el eclipse desde SOC = 1; devuelve (DoD, V minima, I maxima)."""
    p_term = PE / ETA_D
    cap = np_ * CAP_AH
    s, dt, t = 1.0, 1.0, 0.0
    vmin, imax = 1e9, 0.0
    while t < TE - 1e-9:
        h = min(dt, TE - t)
        e = NS * ocv(s)
        r = NS * RINT / np_
        # p = (e - r i) i  ->  r i^2 - e i + p = 0 (raiz menor)
        i = (e - math.sqrt(e * e - 4.0 * r * p_term)) / (2.0 * r)
        v = e - r * i
        vmin, imax = min(vmin, v), max(imax, i)
        s -= i * h / (3600.0 * cap)
        t += h
    return 1.0 - s, vmin, imax


def resultados():
    ciclos_orb = 365.25 * 86400.0 / T
    n = ciclos_orb * ANOS
    d1, d2 = dod_cerrada(n), dod_biseccion(n)
    e_sale = PE * TE / 3600.0                       # Wh que pide la carga en el eclipse
    e_celdas = e_sale / ETA_D                       # Wh que salen de las celdas
    e_nom = e_celdas / (d1 * (1.0 - FADE))          # Wh nominales para cumplir DoD al fin de vida
    ah = e_nom / (NS * VNOM)
    np_ = math.ceil(ah / CAP_AH)
    e_inst = NS * np_ * CAP_AH * VNOM
    dod_plan = e_celdas / e_inst
    dod_sim, vmin, imax = simular(np_)
    return dict(T=T, Te=TE, ciclos_orb=ciclos_orb, N=n, DoD_c=d1, DoD_b=d2, dDoD=abs(d1 - d2), E_sale=e_sale, E_celdas=e_celdas,
                E_nom=e_nom, Ah=ah, Np=np_, Ncel=NS * np_, E_inst=e_inst, masa=e_inst / WHKG, DoD_plan=dod_plan,
                DoD_sim=dod_sim, err_sim=abs(dod_sim - dod_plan) / dod_plan, Vmin=vmin, Imax=imax,
                DoD_c_pct=d1 * 100.0, DoD_plan_pct=dod_plan * 100.0, DoD_sim_pct=dod_sim * 100.0,
                N_a_dod50=ciclos(0.5), err_sim_pct=abs(dod_sim - dod_plan) / dod_plan * 100.0, N40=ciclos(0.4), ej4=161.0 / 28.8,
                E_cel90=e_sale / 0.90, E_nom30=e_celdas / (d1 * 0.7), N100=ciclos(1.0), ratio=e_inst / e_sale, N_a_dod30=ciclos(0.3), E_eol=e_inst * (1.0 - FADE))


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA h = {H:.0f} km: T = {T:.1f} s ; eclipse = {TE:.1f} s ; ciclos por ano = {r['ciclos_orb']:.0f}")
    print(f"Ciclos en {ANOS:.0f} anos = {r['N']:.0f} ; DoD maxima segun la ley ilustrativa = {r['DoD_c']*100:.2f} % (biseccion {r['DoD_b']*100:.2f} %; dif {r['dDoD']:.1e})")
    print(f"Energia pedida por la carga en el eclipse = {r['E_sale']:.2f} Wh ; desde las celdas = {r['E_celdas']:.2f} Wh")
    print(f"Energia nominal necesaria (DoD fin de vida con {FADE*100:.0f} % de perdida) = {r['E_nom']:.1f} Wh ; capacidad = {r['Ah']:.2f} Ah a {NS*VNOM:.1f} V")
    print(f"Paquete: {NS}S{r['Np']}P = {r['Ncel']} celdas de {CAP_AH} Ah ; energia instalada = {r['E_inst']:.1f} Wh ; masa = {r['masa']:.3f} kg a {WHKG:.0f} Wh/kg")
    print(f"DoD planificado = {r['DoD_plan']*100:.2f} % ; DoD simulado (Coulomb con OCV y R) = {r['DoD_sim']*100:.2f} % ; diferencia relativa = {r['err_sim']*100:.2f} %")
    print(f"Tension minima del paquete = {r['Vmin']:.2f} V ; corriente maxima = {r['Imax']:.2f} A")
    print(f"Referencia de la ley: {r['N_a_dod30']:.0f} ciclos a DoD 30 % ; {r['N_a_dod50']:.0f} ciclos a DoD 50 %")
    assert r["dDoD"] < 1e-12
    assert r["DoD_sim"] < r["DoD_plan"] and r["err_sim"] < 0.15
    assert r["DoD_plan"] / (1.0 - FADE) <= r["DoD_c"] + 1e-12   # DoD al fin de vida no supera el limite
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
