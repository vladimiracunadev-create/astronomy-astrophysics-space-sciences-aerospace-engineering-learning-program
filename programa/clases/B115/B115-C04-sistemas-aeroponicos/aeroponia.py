#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C04: aeroponia: gotas, humedad de la raiz y ciclo de niebla/secado en una camara SINTETICA.

Todo es sintetico o ilustrativo: boquilla (0.05 L/min), zona radicular (0.05 m2 de superficie de raiz), espesor maximo
de pelicula de agua en la raiz (50 um), coeficiente de transferencia de masa (0.004 m/s), eficiencia de deposito (30 %).
Relaciones estandar NO consultadas (las verifica el laboratorio): presion de saturacion de Magnus, ley de Stokes,
ley d2 de evaporacion de una gota, impactacion tipo sigmoide en funcion del numero de Stokes (forma ilustrativa).
Unidades SI salvo donde se indica (um, s, L, mL, %). Sistema: camara a 22 C y 101.3 kPa; gravedad terrestre o cero.
Metodo: (1) fisica de la gota: tiempo de relajacion, numero de Stokes, sedimentacion en 1 g y 0 g, vida por evaporacion;
(2) tiempo de secado de la pelicula de la raiz segun la humedad relativa; (3) simulacion segundo a segundo de un dia
completo del ciclo niebla/secado frente al calculo analitico de la fraccion de tiempo con la raiz seca.
Verificacion: la fraccion seca simulada coincide con la analitica (tolerancia 0.5 puntos porcentuales).
"""
from __future__ import annotations
import math
import platform
import numpy as np

T_C, P_KPA, RV = 22.0, 101.3, 461.5          # C, kPa, J/(kg K) constante del vapor de agua
RHO_W, MU_AIRE, DV = 1000.0, 1.8e-5, 2.5e-5  # kg/m3, Pa s, m2/s
HM, DELTA_MAX = 0.004, 50e-6                 # m/s (sintetico), m (sintetico)
Q_BOQ, T_ON_DEF, A_RAIZ, ETA_DEP = 0.05 / 1000 / 60, 5.0, 0.05, 0.30   # m3/s, s, m2, -
D_RAIZ, V_CHORRO, G = 0.5e-3, 2.0, 9.81      # m, m/s (sinteticos), m/s2


def rho_vapor_sat(t_c):
    es = 0.6108 * math.exp(17.27 * t_c / (t_c + 237.3)) * 1000.0   # Pa (Magnus)
    return es / (RV * (t_c + 273.15))


def deficit(rh):
    return rho_vapor_sat(T_C) * (1.0 - rh)                         # kg/m3


def t_secado(rh, delta=DELTA_MAX):
    return RHO_W * delta / (HM * deficit(rh))                      # s


def gota(d_um, rh):
    d = d_um * 1e-6
    tau = RHO_W * d * d / (18 * MU_AIRE)
    st = tau * V_CHORRO / D_RAIZ
    imp = (st / (st + 0.5)) ** 2
    vs = tau * G
    parada = V_CHORRO * tau
    vida = RHO_W * d * d / (8 * DV * deficit(rh))
    return tau, st, imp, vs, parada, vida


def fraccion_seca_analitica(t_on, t_off, rh, delta):
    periodo = t_on + t_off
    return max(0.0, (periodo - t_secado(rh, delta)) / periodo)


def simular(t_on, t_off, rh, delta_pulso, dt=1.0):
    periodo = t_on + t_off
    delta, seca, pasos = 0.0, 0, 0
    e = HM * deficit(rh) / RHO_W                                    # m/s de adelgazamiento
    for k in range(int(86400 / dt)):
        t = (k * dt) % periodo
        if t < dt:                                                  # inicio de cada pulso de niebla
            delta = min(DELTA_MAX, delta + delta_pulso)
        delta = max(0.0, delta - e * dt)
        pasos += 1
        if delta <= 0.0:
            seca += 1
    return seca / pasos


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: camara 22 C, boquilla 0.05 L/min, raiz 0.05 m2, pelicula maxima 50 um")
    print(f"Densidad de vapor saturado a {T_C:.0f} C = {rho_vapor_sat(T_C)*1000:.2f} g/m3")
    print("Gotas (chorro de 2 m/s, raiz de 0.5 mm; vida por evaporacion con HR 90 % y 60 %)")
    print("   d[um]  tau[ms]  Stokes  impacto  v_sed 1g[mm/s]  parada[mm]  vida90[s]  vida60[s]")
    for d in (5, 10, 20, 50):
        tau, st, imp, vs, par, v90 = gota(d, 0.9)
        v60 = gota(d, 0.6)[5]
        print(f"   {d:5d}  {tau*1000:7.3f}  {st:6.2f}  {imp:7.2f}  {vs*1000:14.2f}  {par*1000:10.2f}  {v90:9.3f}  {v60:9.3f}")
    assert gota(50, 0.9)[3] > 0.07 and gota(5, 0.9)[1] < gota(50, 0.9)[1]
    print("En 0 g la velocidad de sedimentacion es 0 para todas las gotas: la niebla solo se mueve con el aire.")

    print("Tiempo de secado de una pelicula de 50 um en la raiz segun la humedad relativa")
    for rh in (0.60, 0.75, 0.90, 0.95):
        print(f"   HR {rh*100:3.0f} %: deficit = {deficit(rh)*1000:5.2f} g/m3; flujo = {HM*deficit(rh)*3600*1000:6.1f} g/m2/h; "
              f"secado = {t_secado(rh)/60:6.1f} min")

    delta_pulso = ETA_DEP * Q_BOQ * T_ON_DEF / A_RAIZ   # m3 / m2 = m
    print(f"Pulso de {T_ON_DEF:.0f} s: agua depositada = {ETA_DEP*Q_BOQ*T_ON_DEF*1e6:.2f} mL -> {delta_pulso*1e6:.1f} um de pelicula "
          f"(limitado a {DELTA_MAX*1e6:.0f} um)")
    print("Ciclo niebla/secado: fraccion del dia con la raiz seca (simulada / analitica) y consumo de la boquilla")
    print("   HR   t_off[s]   seca sim[%]  seca analitica[%]   pulsos/dia   agua bombeada[L/dia]   depositada[L/dia]")
    err_max = 0.0
    for rh in (0.90, 0.60):
        for t_off in (60, 300, 900, 1800, 3600):
            sim = simular(T_ON_DEF, t_off, rh, delta_pulso)
            ana = fraccion_seca_analitica(T_ON_DEF, t_off, rh, min(DELTA_MAX, delta_pulso))
            err_max = max(err_max, abs(sim - ana))
            n = 86400 / (T_ON_DEF + t_off)
            bomb = n * Q_BOQ * T_ON_DEF * 1000
            print(f"   {rh*100:3.0f}   {t_off:7d}   {sim*100:10.1f}   {ana*100:16.1f}   {n:10.0f}   {bomb:20.2f}   {bomb*ETA_DEP:15.2f}")
    print(f"Error maximo de la fraccion seca simulada frente a la analitica = {err_max*100:.2f} puntos porcentuales")
    assert err_max < 0.005
    print("Regla de diseno ilustrativa: raiz seca <= 10 % del tiempo")
    for rh in (0.90, 0.60):
        mejor = max(t for t in range(30, 7200, 30) if fraccion_seca_analitica(T_ON_DEF, t, rh, min(DELTA_MAX, delta_pulso)) <= 0.10)
        print(f"   HR {rh*100:.0f} %: t_off maximo = {mejor} s ({mejor/60:.1f} min)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
