#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C30: nubes de puntos tridimensionales: filtro de suelo, plano por RANSAC y densidad.

Datos: SINTETICOS. Terreno de 100 x 100 m con pendiente 0.10 en x y 0.05 en y mas ruido de 0.05 m; 40 arboles (cilindros de radio 1.5 m y altura 12 m) y un edificio de
10 x 10 x 8 m; 20 000 puntos de suelo, 6 000 de vegetacion y 1 500 de tejado, semilla fija 57. No se usa ninguna nube de puntos de una mision.
Modelo: filtro de suelo: plano inicial por minimo en celdas de 5 m (queda bajo el suelo en laderas), refinado 3 veces con los puntos a menos de 1.2, 0.7 y 0.35 m ; RANSAC de un plano (3 puntos, umbral 0.15 m, 400 iteraciones)
sobre los puntos clasificados como suelo ; densidad = puntos / area.
Validez: terreno casi plano a la escala de la celda, sin puntos bajo la superficie. Tolerancia: recall del suelo > 0.90 y contaminacion del suelo (puntos no suelo) < 5 %;
pendiente recuperada por RANSAC dentro de 0.01 de la verdadera.
Requiere numpy.
"""
import math, platform
import numpy as np

L = 100.0
SX, SY = 0.10, 0.05


def nube(rng):
    xs = rng.uniform(0, L, 20000); ys = rng.uniform(0, L, 20000)
    suelo = np.column_stack([xs, ys, SX * xs + SY * ys + 0.05 * rng.standard_normal(xs.size)])
    pts, lab = [suelo], [np.ones(len(suelo), int)]
    cx, cy = rng.uniform(5, 95, 40), rng.uniform(5, 95, 40)
    for i in range(150):
        k = rng.integers(40)
        a, rr, h = rng.uniform(0, 2 * math.pi), 1.5 * math.sqrt(rng.uniform()), rng.uniform(0, 12)
        x, y = cx[k] + rr * math.cos(a), cy[k] + rr * math.sin(a)
        pts.append(np.array([[x, y, SX * x + SY * y + h]])); lab.append(np.array([0]))
    ve = []
    for _ in range(6000 - 150):
        k = rng.integers(40)
        a, rr, h = rng.uniform(0, 2 * math.pi), 1.5 * math.sqrt(rng.uniform()), rng.uniform(1.0, 12)
        x, y = cx[k] + rr * math.cos(a), cy[k] + rr * math.sin(a)
        ve.append([x, y, SX * x + SY * y + h])
    pts.append(np.array(ve)); lab.append(np.zeros(len(ve), int))
    tx, ty = rng.uniform(40, 50, 1500), rng.uniform(40, 50, 1500)
    pts.append(np.column_stack([tx, ty, SX * tx + SY * ty + 8.0 + 0.03 * rng.standard_normal(tx.size)])); lab.append(np.zeros(1500, int))
    return np.vstack(pts), np.concatenate(lab)


def filtro_suelo(P, celda=5.0, umbral=0.35):
    n = int(L / celda)
    ix = np.clip((P[:, 0] / celda).astype(int), 0, n - 1)
    iy = np.clip((P[:, 1] / celda).astype(int), 0, n - 1)
    zmin = np.full((n, n), np.inf)
    np.minimum.at(zmin, (ix, iy), P[:, 2])
    # plano local de minimos por minimos cuadrados sobre las celdas con datos
    cx, cy = np.meshgrid((np.arange(n) + 0.5) * celda, (np.arange(n) + 0.5) * celda, indexing="ij")
    ok = np.isfinite(zmin)
    A = np.column_stack([cx[ok], cy[ok], np.ones(ok.sum())])
    c = np.linalg.lstsq(A, zmin[ok], rcond=None)[0]
    z0 = c[0] * P[:, 0] + c[1] * P[:, 1] + c[2]
    # refinamiento: el minimo por celda queda por debajo del suelo en laderas; se reajusta el plano con los puntos cercanos
    for thr in (1.2, 0.7, umbral):
        sel = np.abs(P[:, 2] - z0) < thr
        A2 = np.column_stack([P[sel, 0], P[sel, 1], np.ones(sel.sum())])
        c = np.linalg.lstsq(A2, P[sel, 2], rcond=None)[0]
        z0 = c[0] * P[:, 0] + c[1] * P[:, 1] + c[2]
    return np.abs(P[:, 2] - z0) < umbral


def ransac(P, rng, it=400, umbral=0.15):
    mejor, cmax = None, -1
    for _ in range(it):
        i = rng.choice(len(P), 3, replace=False)
        v1, v2 = P[i[1]] - P[i[0]], P[i[2]] - P[i[0]]
        nrm = np.cross(v1, v2)
        if abs(nrm[2]) < 1e-9:
            continue
        a, b = -nrm[0] / nrm[2], -nrm[1] / nrm[2]
        c0 = P[i[0], 2] - a * P[i[0], 0] - b * P[i[0], 1]
        d = np.abs(P[:, 2] - (a * P[:, 0] + b * P[:, 1] + c0))
        k = int((d < umbral).sum())
        if k > cmax:
            cmax, mejor = k, (a, b, c0)
    return mejor, cmax


def calcular():
    rng = np.random.default_rng(57)
    P, lab = nube(rng)
    r = {"n": len(P), "dens": len(P) / L**2}
    pred = filtro_suelo(P)
    tp = int((pred & (lab == 1)).sum())
    r["recall"] = tp / int((lab == 1).sum())
    r["contaminacion"] = int((pred & (lab == 0)).sum()) / int(pred.sum())
    r["n_pred"] = int(pred.sum())
    (a, b, c0), k = ransac(P[pred], rng)
    r["pend_x"], r["pend_y"] = a, b
    r["err_pend"] = max(abs(a - SX), abs(b - SY))
    r["inliers"] = k / int(pred.sum())
    # sin filtro, RANSAC sobre toda la nube
    (a2, b2, _), _ = ransac(P, rng)
    r["err_pend_sin"] = max(abs(a2 - SX), abs(b2 - SY))
    r["dens_suelo"] = int(pred.sum()) / L**2
    r["espaciado"] = 1 / math.sqrt(r["dens_suelo"])
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Nube sintetica: {r['n']} puntos en 100 x 100 m ({r['dens']:.2f} puntos/m2)")
    print(f"Filtro de suelo: puntos clasificados como suelo = {r['n_pred']} ; recall del suelo = {r['recall']:.3f} ; contaminacion (no suelo en el suelo) = {r['contaminacion']*100:.2f} %")
    print(f"RANSAC sobre el suelo filtrado: pendiente x = {r['pend_x']:.4f} (0.1000) ; y = {r['pend_y']:.4f} (0.0500) ; error maximo = {r['err_pend']:.4f} ; fraccion de inliers = {r['inliers']:.3f}")
    print(f"RANSAC sobre toda la nube (sin filtrar): error maximo = {r['err_pend_sin']:.4f}")
    print(f"Densidad del suelo = {r['dens_suelo']:.2f} puntos/m2 -> espaciado medio = {r['espaciado']:.2f} m")
    assert r["recall"] > 0.90 and r["contaminacion"] < 0.05
    assert r["err_pend"] < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
