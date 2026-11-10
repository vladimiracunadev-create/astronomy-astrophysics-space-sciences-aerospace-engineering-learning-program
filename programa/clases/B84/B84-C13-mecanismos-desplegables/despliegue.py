#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C13: despliegue de un panel con resorte de torsion, friccion y tope, y margen de par.

DATOS ILUSTRATIVOS (no consultados): inercia del panel respecto de la bisagra I = 0,05 kg m2; resorte de torsion T_s(theta) = T0 - k theta con
T0 = 0,40 N m y k = 0,20 N m/rad; friccion seca T_f = 0,02 N m; amortiguamiento viscoso c = 0,01 N m s/rad; recorrido 0 a 90 grados (pi/2 rad); parte del reposo.
Requisito de margen ILUSTRATIVO: par disponible / par resistente >= 2,0 en todo el recorrido (el valor de los estandares de mecanismos, por ejemplo
ECSS-E-ST-33-01, NO se consulto).
Ecuacion: I theta'' = T_s(theta) - T_f - c theta'. Integracion RK4 con dt = 1e-4 s.
Segunda via: balance de energia. El trabajo del resorte int T_s d(theta) debe igualar la energia cinetica final + el trabajo de friccion seca
+ el trabajo del amortiguador (int c omega d(theta)). Tolerancia del balance < 1e-6 relativa.
Unidades: N m, rad, s, kg m2.
"""
from __future__ import annotations
import math, platform

I, T0, K, TF, CV = 0.05, 0.40, 0.20, 0.02, 0.01
TH_F = math.pi / 2


def deriv(th, w, t0=T0, tf=TF):
    return w, (t0 - K * th - tf - CV * w) / I


def simular(dt=1e-4, t0=T0, tf=TF):
    th, w, t = 0.0, 0.0, 0.0
    Wv = 0.0   # trabajo viscoso acumulado (int c w dth)
    tra = []
    while th < TH_F:
        k1 = deriv(th, w, t0, tf)
        k2 = deriv(th + 0.5 * dt * k1[0], w + 0.5 * dt * k1[1], t0, tf)
        k3 = deriv(th + 0.5 * dt * k2[0], w + 0.5 * dt * k2[1], t0, tf)
        k4 = deriv(th + dt * k3[0], w + dt * k3[1], t0, tf)
        th_n = th + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        w_n = w + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if th_n >= TH_F:
            f = (TH_F - th) / (th_n - th)
            w_c = w + f * (w_n - w)
            Wv += CV * 0.5 * (w + w_c) * (TH_F - th)
            t += f * dt
            th, w = TH_F, w_c
            break
        Wv += CV * 0.5 * (w + w_n) * (th_n - th)
        th, w, t = th_n, w_n, t + dt
        tra.append((t, th, w))
    return t, w, Wv, tra


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Panel ILUSTRATIVO: I = 0,05 kg m2, T0 = 0,40 N m, k = 0,20 N m/rad, T_f = 0,02 N m, c = 0,01 N m s/rad")
    t, wf, Wv, tra = simular()
    print(f"Tiempo de despliegue = {t:.4f} s ; velocidad angular al llegar al tope = {wf:.4f} rad/s ({math.degrees(wf):.1f} grados/s)")
    ek = 0.5 * I * wf ** 2
    ws = T0 * TH_F - 0.5 * K * TH_F ** 2
    wf_fric = TF * TH_F
    print(f"Energia: trabajo del resorte = {ws:.6f} J ; friccion seca = {wf_fric:.6f} J ; viscosa = {Wv:.6f} J ; cinetica final = {ek:.6f} J")
    bal = abs(ws - wf_fric - Wv - ek) / ws
    print(f"Residuo del balance de energia = {bal:.2e} (relativo)")
    # Margen de par: par disponible (resorte) frente a resistente (friccion + viscoso) en cada instante
    margen_min = min((T0 - K * th) / (TF + CV * w) for (_, th, w) in tra)
    th_min = min(tra, key=lambda x: (T0 - K * x[1]) / (TF + CV * x[2]))
    print(f"Margen de par minimo = {margen_min:.3f} a theta = {math.degrees(th_min[1]):.1f} grados (requisito ilustrativo >= 2,0 -> {'cumple' if margen_min >= 2 else 'NO cumple'})")
    print(f"Par del resorte en el tope = {T0 - K * TH_F:.4f} N m (par de mantenimiento restante frente a la friccion {TF:.2f} N m: razon {(T0 - K * TH_F) / TF:.2f})")
    # Sensibilidad: friccion x3 y precarga -20 %
    print("Sensibilidad (tiempo, velocidad al tope, margen minimo):")
    for nom, (t0, tf) in (("base", (T0, TF)), ("friccion x3", (T0, 3 * TF)), ("precarga -20 %", (0.8 * T0, TF))):
        tt, ww, _, tr = simular(t0=t0, tf=tf)
        mm = min((t0 - K * th) / (tf + CV * w) for (_, th, w) in tr)
        print(f"  {nom:15s} t = {tt:.4f} s  w = {ww:.4f} rad/s  margen = {mm:.3f}")
    # Precarga T0 necesaria para cumplir la razon de par ilustrativa de 2,0 (biseccion)
    lo, hi = T0, 1.5
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        _, _, _, tr = simular(dt=1e-3, t0=mid)
        mm = min((mid - K * th) / (TF + CV * w) for (_, th, w) in tr)
        if mm < 2.0:
            lo = mid
        else:
            hi = mid
    t0n = 0.5 * (lo + hi)
    tt, ww, _, _ = simular(t0=t0n)
    print(f"Precarga T0 que da una razon de par de 2,0: {t0n:.4f} N m (tiempo {tt:.4f} s, velocidad al tope {ww:.3f} rad/s, energia cinetica {0.5 * I * ww ** 2:.4f} J)")
    assert bal < 1e-6
    assert margen_min > 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
