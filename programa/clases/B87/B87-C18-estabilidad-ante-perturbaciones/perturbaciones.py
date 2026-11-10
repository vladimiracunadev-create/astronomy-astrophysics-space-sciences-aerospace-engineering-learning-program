#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C18: pares perturbadores (gradiente de gravedad, resistencia, presion de radiacion solar, dipolo residual) de un microsatelite
SINTETICO a 500 km, y error en regimen permanente de un lazo PD de un eje; funcion de Lyapunov. Valores ADOPTADOS de ejemplo (no consultados):
densidad atmosferica 5e-13 kg/m3 a 500 km, presion solar 4.56e-6 N/m2, Cd = 2.2, area 0.06 m2, brazo 0.01 m, reflectividad 0.5,
dipolo residual 0.01 A m^2. I = diag(0.35, 0.40, 0.30) kg m^2."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

ARC = D2R / 3600.0


def pares():
    a = RE + 500e3
    I = np.diag(inertia_example())
    gg = 1.5 * MU_E / a ** 3 * (I.max() - I.min())               # maximo (sin 2 theta = 1)
    v = math.sqrt(MU_E / a)
    aero = 0.5 * 5e-13 * v ** 2 * 2.2 * 0.06 * 0.01
    srp = 4.56e-6 * 0.06 * (1 + 0.5) * 0.01
    Bmax = 2 * B0_T * (RE / a) ** 3
    mag = 0.01 * Bmax
    return dict(gg=gg, aero=aero, srp=srp, mag=mag, v=v, n=math.sqrt(MU_E / a ** 3))


def lazo(tau_d, wn=0.2, zeta=0.8, T=200.0, dt=0.01):
    Iz = 0.30
    kp, kd = Iz * wn ** 2, 2 * zeta * wn * Iz
    th, w = 0.0, 0.0
    Vs = []
    for k in range(int(T / dt)):
        u = -kp * th - kd * w
        w += (u + tau_d) / Iz * dt
        th += w * dt
        Vs.append(0.5 * Iz * w ** 2 + 0.5 * kp * (th - tau_d / kp) ** 2)
    Vs = np.array(Vs)
    return th, kp, float(np.max(np.diff(Vs))), float(Vs[0])


def calcular():
    p = pares()
    tot = p['gg'] + p['aero'] + p['srp'] + p['mag']
    rss = math.sqrt(p['gg'] ** 2 + p['aero'] ** 2 + p['srp'] ** 2 + p['mag'] ** 2)
    th, kp, dVmax, V0 = lazo(tot)
    return dict(p=p, suma=tot, rss=rss, th_ss=th / ARC, th_teo=tot / kp / ARC, kp=kp, dVmax=dVmax, V0=V0)


def main():
    banner("B87-C18 perturbaciones y estabilidad | microsatelite SINTETICO a 500 km; coeficientes de ejemplo (no consultados)")
    d = calcular(); p = d['p']
    print(f"gradiente de gravedad (max) = {p['gg']*1e9:.1f} nN m ; resistencia = {p['aero']*1e9:.1f} nN m ; presion solar = {p['srp']*1e9:.2f} nN m ; dipolo residual = {p['mag']*1e9:.1f} nN m")
    print(f"suma (peor caso) = {d['suma']*1e9:.1f} nN m ; raiz de la suma de cuadrados = {d['rss']*1e9:.1f} nN m")
    print(f"lazo PD wn = 0.2 rad/s: Kp = {d['kp']:.4f} N m/rad ; error permanente simulado = {d['th_ss']:.2f} arcsec ; teorico tau/Kp = {d['th_teo']:.2f} arcsec")
    print(f"V = 1/2 I w^2 + 1/2 Kp (th - th_ss)^2: V0 = {d['V0']:.3e} ; mayor incremento por paso = {d['dVmax']:.2e} (<= ~0)")
    assert abs(d['th_ss'] - d['th_teo']) / d['th_teo'] < 0.01 and d['dVmax'] < 1e-12
    assert p['mag'] > p['gg'] > p['aero'] > p['srp']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
