#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C12: par magnetico tau = m x B: subactuacion instantanea y controlabilidad promedio en una orbita.
Campo dipolar SINTETICO (ver C05), orbita de 500 km y 51.6 deg; dipolo maximo de ejemplo 0.2 A m^2. Se supone el cuerpo
alineado con el sistema inercial de ejemplo (B en el cuerpo = B inercial). Todo SINTETICO."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

MMAX = 0.2   # A m^2


def calcular(n=720):
    r0, nm = orbit_state(0.0)
    T = 2 * math.pi / nm
    ts = np.linspace(0, T, n, endpoint=False)
    B = np.array([dipole_B_inertial(orbit_state(t)[0]) for t in ts])
    Bm = np.linalg.norm(B, axis=1)
    Bh = B / Bm[:, None]
    # 1) par maximo instantaneo = MMAX |B| (m perpendicular a B)
    tau_max = MMAX * Bm
    # 2) fraccion de un par deseado que se puede realizar: sin(angulo entre tau_d y B)
    fr = {}
    for nombre, td in (("x", [1, 0, 0]), ("y", [0, 1, 0]), ("z", [0, 0, 1])):
        td = np.array(td, float)
        f = np.sqrt(np.clip(1 - (Bh @ td) ** 2, 0, 1))
        fr[nombre] = (float(f.mean()), float(f.min()))
    # 3) verificacion de la ley m = (B x tau_d)/|B|^2 : el par m x B reproduce la parte perpendicular de tau_d
    td = unit([0.3, -0.5, 0.8]) * 2e-6
    err = 0.0
    for b in B[::10]:
        m = np.cross(b, td) / (b @ b)
        tau = np.cross(m, b)
        perp = td - (td @ b) / (b @ b) * b
        err = max(err, np.linalg.norm(tau - perp) / np.linalg.norm(td))
    # 4) controlabilidad promedio: matriz Pbar = mean(I - Bh Bh^T), eigenvalores (suman 2)
    Pbar = np.mean([np.eye(3) - np.outer(b, b) for b in Bh], axis=0)
    ev = np.linalg.eigvalsh(Pbar)
    # 5) saturacion del dipolo: par deseado de 4e-6 N m a lo largo de y
    td2 = np.array([0, 4e-6, 0.0])
    sat = 0
    for b in B:
        m = np.cross(b, td2) / (b @ b)
        if np.linalg.norm(m) > MMAX:
            sat += 1
    return dict(T=T, tmax_min=float(tau_max.min()), tmax_max=float(tau_max.max()), fr=fr, err=err, ev=ev, rank=int(np.linalg.matrix_rank(Pbar, tol=1e-9)),
                sat=sat / n, Bmin=float(Bm.min()), Bmax=float(Bm.max()))


def main():
    banner("B87-C12 magnetopares | campo dipolar SINTETICO, orbita de 500 km y 51.6 deg, dipolo maximo de ejemplo 0.2 A m^2")
    d = calcular()
    print(f"|B| = {d['Bmin']*1e6:.2f} a {d['Bmax']*1e6:.2f} uT -> par maximo instantaneo m|B| = {d['tmax_min']*1e6:.2f} a {d['tmax_max']*1e6:.2f} uN m")
    print("fraccion realizable de un par deseado fijo (sin angulo entre tau y B): media / minimo en la orbita")
    for k, (mu, mn) in d['fr'].items():
        print(f"  eje {k}: {mu:.3f} / {mn:.3f}")
    print(f"ley m = (B x tau_d)/|B|^2: error relativo del par frente a la parte perpendicular = {d['err']:.2e}")
    print(f"matriz de controlabilidad promedio P = mean(I - Bh Bh^T): autovalores = {np.round(d['ev'],4)} ; suma = {d['ev'].sum():.4f} ; rango = {d['rank']}")
    print(f"par deseado de 4 uN m en y: dipolo saturado (> 0.2 A m^2) en {d['sat']*100:.1f} % de la orbita")
    assert d['err'] < 1e-12 and abs(d['ev'].sum() - 2) < 1e-9 and d['rank'] == 3 and d['ev'].min() > 0.2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
