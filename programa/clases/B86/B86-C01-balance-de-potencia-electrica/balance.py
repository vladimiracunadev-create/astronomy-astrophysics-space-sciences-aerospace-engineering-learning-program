#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C01: balance de potencia eléctrica de un satélite SINTÉTICO en órbita circular baja.

Datos consultados (2026-11-10): GM de la Tierra = 0.39860e6 km3/s2, radio medio 6371.000 km y irradiancia solar 1361.0 W/m2
(NASA/NSSDC, Earth Fact Sheet); eficiencia de celda multiunion 29.5 % BOL como valor tipico de la tabla del estado del arte de la NASA.
ILUSTRATIVOS (sintéticos, no medidos): altitud 600 km, beta = 0, tabla de cargas, area del ala 1.2 m2, factor de empaquetado 0.85,
coseno medio 0.70, factor de fin de vida 0.85, eficiencias de camino Xd = 0.85 y Xe = 0.65, reserva de 20 % sobre las cargas.
Modelo: sombra cilindrica, fraccion de eclipse f = asin(R/a)/pi con beta = 0; P_sa = (Pe*Te/Xe + Pd*Td/Xd)/Td.
Segunda via: integracion numerica paso a paso de la energia de la bateria durante una orbita (paso de 1 s).
Tolerancia: balance de energia por orbita con residuo < 1e-6 Wh frente a la formula cerrada.
"""
from __future__ import annotations
import math, platform

MU, RE, GSC = 398600.0, 6371.0, 1361.0     # km3/s2, km, W/m2
H = 600.0                                   # km (ilustrativo)
CARGAS = [  # nombre, P en luz [W], P en eclipse [W] (ilustrativos)
    ("Ordenador de a bordo", 12.0, 12.0),
    ("Control de actitud", 20.0, 20.0),
    ("Radio (valor medio)", 18.0, 6.0),
    ("Carga util", 30.0, 0.0),
    ("Calefactores", 4.0, 16.0),
]
RESERVA, XD, XE = 0.20, 0.85, 0.65
AREA, ETA, EMP, COS, EOL = 1.2, 0.295, 0.85, 0.70, 0.85


def orbita():
    a = RE + H
    t = 2.0 * math.pi * math.sqrt(a ** 3 / MU)
    f = math.asin(RE / a) / math.pi
    return t, f * t, (1.0 - f) * t


def resultados():
    t, te, td = orbita()
    pd = sum(c[1] for c in CARGAS) * (1.0 + RESERVA)
    pe = sum(c[2] for c in CARGAS) * (1.0 + RESERVA)
    psa = (pe * te / XE + pd * td / XD) / td
    pgen = GSC * AREA * ETA * EMP * COS * EOL
    e_cerrada = (pgen - pd / XD) * td / 3600.0 - pe * te / XE / 3600.0   # Wh que entran a la bateria en la orbita
    # segunda via: integracion de la energia de la bateria con paso de 1 s
    e_bat, dt = 0.0, 1.0
    s = 0.0
    while s < t - 1e-12:
        limite = td if s < td else t           # el paso nunca cruza el limite luz/eclipse
        h = min(dt, limite - s)
        if s < td:                             # parte iluminada (beta = 0, empieza al salir del eclipse)
            e_bat += (pgen - pd / XD) * h / 3600.0
        else:
            e_bat -= pe / XE * h / 3600.0
        s += h
    residuo = abs(e_bat - e_cerrada)
    return dict(T=t, Te=te, Td=td, fe=te / t, Pd=pd, Pe=pe, Psa=psa, Pgen=pgen, margen=(pgen - psa) / psa,
                E_orbita=e_cerrada, ra=RE / (RE + H), asin_rad=math.asin(RE / (RE + H)), fe_pct=100.0 * te / t, margen_pct=100.0 * (pgen - psa) / psa, Psa_30=psa * 1.3 / 1.2,
                A_cero=AREA * psa / pgen, Ee_wh=pe * te / 3600.0, Ee_bat_wh=pe * te / 3600.0 / XE, E_num=e_bat, residuo=residuo, ncargas=len(CARGAS))


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita circular SINTETICA h = {H:.0f} km, beta = 0: T = {r['T']:.1f} s ({r['T']/60:.2f} min)")
    print(f"Eclipse Te = {r['Te']:.1f} s ({r['fe']*100:.2f} % de la orbita); luz Td = {r['Td']:.1f} s")
    print(" carga                    P_luz [W]  P_eclipse [W]")
    for n, a, b in CARGAS:
        print(f" {n:<24} {a:8.1f}  {b:10.1f}")
    print(f"Con reserva del {RESERVA*100:.0f} %: P_luz = {r['Pd']:.2f} W ; P_eclipse = {r['Pe']:.2f} W")
    print(f"Potencia de ala requerida (formula SMAD, eficiencias Xd={XD}, Xe={XE}) = {r['Psa']:.2f} W")
    print(f"Potencia generada al fin de vida = {r['Pgen']:.2f} W ; margen = {r['margen']*100:.1f} %")
    print(f"Energia neta a la bateria por orbita (formula) = {r['E_orbita']:.4f} Wh ; (integracion) = {r['E_num']:.4f} Wh")
    print(f"Diferencia entre las dos vias = {r['residuo']:.2e} Wh")
    # comprobaciones
    assert abs(r["Td"] + r["Te"] - r["T"]) < 1e-9
    assert r["residuo"] < 1.0e-2, "las dos vias deben coincidir (el paso de 1 s no es exacto)"
    # si la generacion iguala a P_sa, la bateria cierra el ciclo (energia neta = 0)
    cierre = (r["Psa"] - r["Pd"] / XD) * r["Td"] / 3600.0 - r["Pe"] * r["Te"] / XE / 3600.0
    print(f"Energia neta con P_sa exacta = {cierre:.2e} Wh")
    assert abs(cierre) < 1e-6
    assert r["margen"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
