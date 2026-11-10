#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C07: rastreador estelar SINTETICO: estrellas (direcciones aleatorias, NO un catalogo real) proyectadas en un sensor
de 1024x1024 px con campo de 15 deg (eje optico = +z del cuerpo), centroide con ruido gaussiano de 0.1 px, actitud por SVD (Wahba).
Se mide el error transversal (apuntamiento) y el de balanceo (giro alrededor del eje optico). Semilla 20260517."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

NPIX = 1024
FOV = 15.0 * D2R                      # campo total (diametro)
F_PX = (NPIX / 2) / math.tan(FOV / 2)  # focal en pixeles (pinhole; el campo se mide a lo largo del lado)
SIG_PX = 0.1
IFOV_ARCSEC = math.atan(1 / F_PX) * R2D * 3600


def estrellas_en_campo(n, rng):
    """n direcciones sinteticas dentro de un cono de semiangulo FOV/2 alrededor de +z (cuerpo)."""
    out = []
    while len(out) < n:
        x, y = rng.uniform(-1, 1, 2) * math.tan(FOV / 2) * 0.7
        out.append(unit([x, y, 1.0]))
    return np.array(out)


def proyectar(bvec, rng):
    xy = bvec[:, :2] / bvec[:, 2:3] * F_PX + SIG_PX * rng.standard_normal((len(bvec), 2))
    return np.array([unit([x / F_PX, y / F_PX, 1.0]) for x, y in xy])


def trial(n, rng):
    A_true = A_of_q(random_q(rng))
    b_true = estrellas_en_campo(n, rng)             # en el cuerpo
    r = (A_true.T @ b_true.T).T                       # en el inercial (catalogo)
    b_meas = proyectar(b_true, rng)
    A_est = wahba_svd(b_meas, r)
    dA = A_est @ A_true.T                             # error: rotacion pequena en ejes del cuerpo
    phi = np.array([dA[1, 2] - dA[2, 1], dA[2, 0] - dA[0, 2], dA[0, 1] - dA[1, 0]]) / 2
    return phi


def calcular(n_trials=1500):
    rng = np.random.default_rng(20260517)
    tabla = []
    for n in (3, 5, 10, 20, 40):
        P = np.array([trial(n, rng) for _ in range(n_trials)])
        cross = math.sqrt(np.mean(P[:, 0] ** 2 + P[:, 1] ** 2) / 2) * R2D * 3600   # por eje transversal
        roll = math.sqrt(np.mean(P[:, 2] ** 2)) * R2D * 3600
        # teoria: sigma_a / sqrt(n) ; balanceo sigma_a/(sqrt(n) rho_rms)
        sa = math.atan(SIG_PX / F_PX)
        rho_rms = math.sqrt(2 * (math.tan(FOV / 2) * 0.7) ** 2 / 3)  # radio rms de puntos uniformes en un cuadrado de lado 2a: sqrt(2/3) a
        tabla.append((n, cross, math.degrees(sa / math.sqrt(n)) * 3600, roll, math.degrees(sa / (math.sqrt(n) * rho_rms)) * 3600))
    return dict(tabla=tabla, ifov=IFOV_ARCSEC, f_px=F_PX, sig_arcsec=math.degrees(math.atan(SIG_PX / F_PX)) * 3600)


def main():
    banner("B87-C07 rastreador estelar | estrellas SINTETICAS, sensor 1024x1024 px, campo 15 deg, ruido de centroide 0.1 px (semilla 20260517)")
    d = calcular()
    print(f"focal = {d['f_px']:.1f} px ; IFOV = {d['ifov']:.2f} arcsec/px ; ruido de centroide = {d['sig_arcsec']:.2f} arcsec por eje")
    print("N estrellas | transversal sim [arcsec] | teoria | balanceo sim [arcsec] | teoria")
    for n, c, ct, r, rt in d['tabla']:
        print(f"{n:11d} | {c:24.2f} | {ct:6.2f} | {r:21.2f} | {rt:6.2f}")
    for n, c, ct, r, rt in d['tabla']:
        if n >= 10:   # la teoria asintotica vale con muchas estrellas
            assert abs(c - ct) / ct < 0.10 and abs(r - rt) / rt < 0.10, (n, c, ct, r, rt)
        else:         # con pocas estrellas la teoria subestima el error
            assert 1.0 < c / ct < 1.5 and 1.0 < r / rt < 1.6, (n, c, ct, r, rt)
        assert r > 5 * c
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
