#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C05: campo dipolar a lo largo de una orbita y modelo de magnetometro (sesgo, escala, ruido).
Campo SINTETICO: dipolo inclinado 11 deg, B0 = 31.2 uT ecuatorial (valor de ejemplo, NO el IGRF ni datos medidos).
Orbita circular de 500 km y 51.6 deg de inclinacion, sistema inercial de ejemplo. Semilla 20260515. Unidades: T (se imprime en uT/nT)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *


def orbita(n=720):
    r0, nm = orbit_state(0.0)
    T = 2 * math.pi / nm
    ts = np.linspace(0, T, n, endpoint=False)
    Bs = np.array([dipole_B_inertial(orbit_state(t)[0]) for t in ts])
    return ts, Bs, T


def calcular():
    ts, Bs, T = orbita()
    mag = np.linalg.norm(Bs, axis=1)
    # variacion de direccion: velocidad angular del vector campo en el sistema inercial
    dirs = Bs / mag[:, None]
    ang = np.array([math.acos(max(-1, min(1, dirs[i] @ dirs[(i + 1) % len(dirs)]))) for i in range(len(dirs))])
    rate_deg_s = ang / (ts[1] - ts[0]) * R2D
    # modelo de magnetometro: m = (1 + s) B + b + n
    rng = np.random.default_rng(20260515)
    sg_n = 100e-9
    nmed = 20000
    errs_ruido, errs_sesgo = [], []
    for i in rng.integers(0, len(ts), nmed):
        b = Bs[i]
        m = b + sg_n * rng.standard_normal(3)
        errs_ruido.append(math.acos(max(-1, min(1, unit(m) @ unit(b)))))
    sesgo = np.array([1000e-9, 0.0, 0.0])
    max_e = max(math.acos(max(-1, min(1, unit(b + sesgo) @ unit(b)))) for b in Bs) * R2D
    mean_e = np.mean([math.acos(max(-1, min(1, unit(b + sesgo) @ unit(b)))) for b in Bs]) * R2D
    return dict(Bmin=mag.min(), Bmax=mag.max(), Bmean=mag.mean(), T=T, rate_max=rate_deg_s.max(), rate_mean=rate_deg_s.mean(),
                e_ruido=math.sqrt(np.mean(np.square(errs_ruido))) * R2D, teo_ruido=(sg_n * math.sqrt(2) / mag.mean()) * R2D,
                max_sesgo=max_e, mean_sesgo=mean_e, sg_n=sg_n, B_eq=B0_T * (RE / (RE + 500e3)) ** 3,
                Bpolo=2 * B0_T * (RE / (RE + 500e3)) ** 3)


def main():
    banner("B87-C05 magnetometro y campo dipolar | dipolo SINTETICO inclinado 11 deg, B0 = 31.2 uT; orbita de 500 km, 51.6 deg")
    d = calcular()
    print(f"periodo orbital = {d['T']/60:.2f} min")
    print(f"|B| a lo largo de la orbita: min = {d['Bmin']*1e6:.3f} uT ; max = {d['Bmax']*1e6:.3f} uT ; media = {d['Bmean']*1e6:.3f} uT")
    print(f"dipolo en el radio orbital: ecuador = {d['B_eq']*1e6:.3f} uT ; polo = {d['Bpolo']*1e6:.3f} uT")
    print(f"giro de la direccion de B (inercial): media = {d['rate_mean']:.4f} deg/s ; maximo = {d['rate_max']:.4f} deg/s")
    print(f"ruido blanco de {d['sg_n']*1e9:.0f} nT por eje: error de direccion rms = {d['e_ruido']:.4f} deg (teoria sigma*sqrt(2)/|B| = {d['teo_ruido']:.4f})")
    print(f"sesgo de 1000 nT en x: error de direccion medio = {d['mean_sesgo']:.3f} deg ; maximo = {d['max_sesgo']:.3f} deg")
    assert d['Bmax'] < d['Bpolo'] * 1.001 and d['Bmin'] > d['B_eq'] * 0.5
    assert abs(d['e_ruido'] - d['teo_ruido']) / d['teo_ruido'] < 0.06
    assert d['max_sesgo'] > d['mean_sesgo'] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
