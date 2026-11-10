#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C14: acumulacion de momento en las ruedas por un par perturbador secular + ciclico y descarga con magnetopares
(ley m = -K (B x h)/|B|^2, limitada a m_max). Se supone apuntamiento perfecto (cuerpo fijo respecto del inercial de EJEMPLO),
por lo que dh/dt = tau_ext + tau_mag. Campo dipolar SINTETICO, orbita de 500 km y 51.6 deg; par perturbador de ejemplo
(2, -1, 4) uN m + 20 uN m ciclico a la frecuencia orbital en el eje y; capacidad de la rueda 0.05 N m s; m_max = 0.2 A m^2. Todo SINTETICO."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

HCAP = 0.05
MMAX = 0.2
TAU_SEC = np.array([2e-6, -1e-6, 4e-6])
TAU_CIC = np.array([0.0, 20e-6, 0.0])


def simular(K, T_orb=12, dt=2.0):
    r0, nm = orbit_state(0.0)
    P = 2 * math.pi / nm
    n = int(T_orb * P / dt)
    h = np.zeros(3)
    hmax = 0.0; t_sat = None; hs = []; sat_m = 0
    for k in range(n):
        t = k * dt
        B = dipole_B_inertial(orbit_state(t)[0])
        td = TAU_SEC + TAU_CIC * math.sin(nm * t)
        if K > 0:
            m = -K * np.cross(B, h) / (B @ B)
            if np.linalg.norm(m) > MMAX:
                m = m / np.linalg.norm(m) * MMAX; sat_m += 1
            tm = np.cross(m, B)
        else:
            tm = np.zeros(3)
        h = h + (td + tm) * dt
        hn = np.linalg.norm(h)
        hmax = max(hmax, hn)
        if t_sat is None and hn > HCAP:
            t_sat = t
        if k % int(P / dt) == 0:
            hs.append(hn)
    return dict(P=P, hmax=hmax, t_sat=t_sat, hfin=float(np.linalg.norm(h)), hs=hs, frac_m=sat_m / n)


def calcular():
    P = 2 * math.pi / orbit_state(0.0)[1]
    sin_d = simular(0.0)
    con_d = simular(1.0 / 600.0)
    t_teo = HCAP / np.linalg.norm(TAU_SEC)
    return dict(sin=sin_d, con=con_d, t_teo=t_teo, tauN=float(np.linalg.norm(TAU_SEC)), h_cic=float(TAU_CIC[1] / (2 * math.pi / P)), P=P)


def main():
    banner("B87-C14 saturacion y descarga | SINTETICO: par secular (2,-1,4) uN m + 20 uN m ciclico; rueda 0.05 N m s; m_max 0.2 A m^2; 12 orbitas")
    d = calcular(); s = d['sin']; c = d['con']
    print(f"periodo orbital = {d['P']/60:.2f} min ; |par secular| = {d['tauN']*1e6:.3f} uN m")
    print(f"tiempo teorico a saturacion con el par secular = {d['t_teo']/3600:.2f} h ({d['t_teo']/d['P']:.1f} orbitas)")
    print(f"sin descarga: momento maximo en 12 orbitas = {s['hmax']:.4f} N m s ; supera 0.05 a t = {s['t_sat']/3600:.2f} h")
    print(f"con descarga (K = 1/600 1/s): momento maximo = {c['hmax']:.5f} N m s ; final = {c['hfin']:.5f} N m s ; dipolo saturado el {c['frac_m']*100:.1f} % del tiempo")
    print("momento al inicio de cada orbita con descarga [N m s]: " + " ".join(f"{x:.4f}" for x in c['hs']))
    print(f"amplitud ciclica del momento = tau_c / n = {d['h_cic']:.4f} N m s")
    assert s['t_sat'] is not None and abs(s['t_sat'] - d['t_teo']) / d['t_teo'] < 0.3
    assert c['hmax'] < 0.5 * s['hmax'] and c['hmax'] < HCAP
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
