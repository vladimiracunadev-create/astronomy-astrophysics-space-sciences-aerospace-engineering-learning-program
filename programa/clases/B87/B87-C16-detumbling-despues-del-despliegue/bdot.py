#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C16: detumbling con la ley B-dot: m = -k dB/dt (limitado a 0.2 A m^2), par m x B. Satelite SINTETICO
I = diag(0.35, 0.40, 0.30) kg m^2, velocidad angular inicial (5, -4, 3) deg/s, campo dipolar SINTETICO a 500 km y 51.6 deg,
derivada del campo por diferencia finita de la medida en el cuerpo (ruido 50 nT, semilla 20260522), RK4 con paso de 0.5 s,
4 orbitas. El campo inercial se supone fijo en el sistema inercial de EJEMPLO."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

MMAX = 0.2


def simular(k=2e5, T_orb=4, dt=0.5, seed=20260522):
    rng = np.random.default_rng(seed)
    I = inertia_example()
    r0, nm = orbit_state(0.0)
    P = 2 * math.pi / nm
    q = qnormalize(np.array([0.1, 0.2, -0.3, 0.9])); w = np.array([5, -4, 3.0]) * D2R; h = np.zeros(3)
    Bprev = None
    n = int(T_orb * P / dt)
    wn_, Ts, Es = [], [], []
    t_cap = None; sat = 0; Tmono = 0
    T0 = 0.5 * w @ I @ w
    for i in range(n):
        t = i * dt
        Bi = dipole_B_inertial(orbit_state(t)[0])
        Bb = A_of_q(q) @ Bi
        Bm = Bb + 50e-9 * rng.standard_normal(3)
        if Bprev is None:
            m = np.zeros(3)
        else:
            m = -k * (Bm - Bprev) / dt
            if np.linalg.norm(m) > MMAX:
                m = m / np.linalg.norm(m) * MMAX; sat += 1
        Bprev = Bm
        tau = np.cross(m, Bb)
        q, w, h = step(q, w, h, np.zeros(3), tau, I, dt)
        wnorm = np.linalg.norm(w) * R2D
        if t_cap is None and wnorm < 0.5:
            t_cap = t
        if i % int(P / dt) == 0:
            wn_.append(wnorm)
        Es.append(0.5 * w @ I @ w)
    Es = np.array(Es)
    return dict(P=P, w0=float(np.linalg.norm([5, -4, 3])), wfin=float(np.linalg.norm(w) * R2D), wn_orb=wn_, t_cap=t_cap, T0=T0, Tfin=float(Es[-1]),
                sat=sat / n, nrate=nm * R2D, aumento_max=float(np.max(np.diff(Es)) / dt))


def calcular():
    return simular()


def main():
    banner("B87-C16 detumbling B-dot | SINTETICO: w0 = (5,-4,3) deg/s, k = 2e5, m_max = 0.2 A m^2, ruido de B 50 nT (semilla 20260522), 4 orbitas")
    d = calcular()
    print(f"periodo orbital = {d['P']/60:.2f} min ; velocidad orbital = {d['nrate']:.4f} deg/s")
    print(f"|w| inicial = {d['w0']:.3f} deg/s ; final = {d['wfin']:.4f} deg/s")
    print("|w| al inicio de cada orbita [deg/s]: " + " ".join(f"{x:.3f}" for x in d['wn_orb']))
    print(f"tiempo para |w| < 0.5 deg/s = {d['t_cap']/60:.1f} min ({d['t_cap']/d['P']:.2f} orbitas)")
    print(f"energia cinetica: inicial = {d['T0']*1e3:.4f} mJ ; final = {d['Tfin']*1e6:.3f} uJ ; dipolo saturado el {d['sat']*100:.1f} % del tiempo")
    print(f"mayor aumento instantaneo de energia = {d['aumento_max']:.2e} J/s (el ruido de la medida puede causar aumentos puntuales)")
    assert d['t_cap'] is not None and d['wfin'] < 0.5 and d['Tfin'] < 0.01 * d['T0']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
