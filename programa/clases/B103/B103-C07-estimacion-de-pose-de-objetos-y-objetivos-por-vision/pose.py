#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C07: pose de un objeto plano conocido (PnP plano) con datos SINTETICOS.

Todo es sintetico (semilla 103): camara ILUSTRATIVA sin distorsion (fx = fy = 800 px, cx = 640, cy = 480; ver B103-C01),
objeto = marcador plano con 9 puntos en una rejilla 3 x 3 de paso 0.05 m (0.10 m de lado) en su plano z = 0, ruido gaussiano de
deteccion sigma = 0.5 px. Convencion: p_camara = R p_objeto + t, z hacia delante; unidades px, m, grados.
Metodo: homografia por DLT -> pose inicial por descomposicion (columnas r1, r2, t, con ortonormalizacion por SVD) -> refinamiento
de Levenberg-Marquardt (jacobiano numerico) sobre el error de reproyeccion. Verificacion: sin ruido el error es < 1e-6; el
error relativo de profundidad (mediana) se contrasta con 0.6745 sigma_Z/Z, sigma_Z/Z ~ sigma_px Z / (f rho sqrt(N)), rho = radio
cuadratico medio de los puntos. Se cuenta la fraccion de 'vuelcos' (error de rotacion > 30 grados), por la ambiguedad conocida
de la pose de un objeto plano con poca perspectiva: el refinamiento solo parte de una solucion.
Tolerancias: cociente mediana/teorico entre 0.6 y 1.8 a 2 m con inclinacion de 20 grados; el error de rotacion con inclinacion de 5 grados es
mayor que con 45 grados. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

K = np.array([[800.0, 0, 640.0], [0, 800.0, 480.0], [0, 0, 1.0]])
G = np.array([[x, y] for y in (-0.05, 0.0, 0.05) for x in (-0.05, 0.0, 0.05)])
SIG = 0.5
RHO = np.sqrt(np.mean(np.sum(G ** 2, axis=1)))


def rodrigues(v):
    th = np.linalg.norm(v)
    if th < 1e-12:
        return np.eye(3)
    k = v / th
    km = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + np.sin(th) * km + (1 - np.cos(th)) * km @ km


def vec(r):
    th = np.arccos(np.clip((np.trace(r) - 1) / 2, -1, 1))
    if th < 1e-9:
        return np.zeros(3)
    return np.array([r[2, 1] - r[1, 2], r[0, 2] - r[2, 0], r[1, 0] - r[0, 1]]) / (2 * np.sin(th)) * th


def angulo(r):
    w = np.array([r[2, 1] - r[1, 2], r[0, 2] - r[2, 0], r[1, 0] - r[0, 1]]) / 2
    return np.degrees(np.arctan2(np.linalg.norm(w), (np.trace(r) - 1) / 2))


def proyectar(r, t):
    p = np.c_[G, np.zeros(len(G))] @ r.T + t
    return np.stack([K[0, 0] * p[:, 0] / p[:, 2] + K[0, 2], K[1, 1] * p[:, 1] / p[:, 2] + K[1, 2]], axis=1)


def homografia(a, b):
    f = []
    for (x, y), (u, v) in zip(a, b):
        f.append([x, y, 1, 0, 0, 0, -u * x, -u * y, -u])
        f.append([0, 0, 0, x, y, 1, -v * x, -v * y, -v])
    h = np.linalg.svd(np.array(f))[2][-1].reshape(3, 3)
    return h / h[2, 2]


def pose_inicial(obs):
    ki = np.linalg.inv(K)
    h = homografia(G, obs)
    lam = 1.0 / np.linalg.norm(ki @ h[:, 0])
    r1, r2, t = lam * ki @ h[:, 0], lam * ki @ h[:, 1], lam * ki @ h[:, 2]
    if t[2] < 0:
        r1, r2, t = -r1, -r2, -t
    u, _, vt = np.linalg.svd(np.stack([r1, r2, np.cross(r1, r2)], axis=1))
    return u @ vt, t


def refinar(obs, r, t, it=40):
    p = np.concatenate([vec(r), t])
    res = lambda q: (proyectar(rodrigues(q[:3]), q[3:]) - obs).ravel()
    r0 = res(p)
    lam = 1e-3
    for _ in range(it):
        j = np.empty((len(r0), 6))
        for c in range(6):
            d = np.zeros(6)
            d[c] = 1e-7 * max(1.0, abs(p[c]))
            j[:, c] = (res(p + d) - r0) / d[c]
        a, g = j.T @ j, j.T @ r0
        mejor = False
        for _ in range(30):
            paso = np.linalg.solve(a + lam * np.diag(np.diag(a)), -g)
            r1 = res(p + paso)
            if r1 @ r1 < r0 @ r0:
                p, r0, lam, mejor = p + paso, r1, lam / 3, True
                break
            lam *= 4
        if not mejor or np.linalg.norm(paso) < 1e-10:
            break
    return rodrigues(p[:3]), p[3:]


def verdad(rng, z, incl):
    eje = np.array([np.cos(a := rng.uniform(0, 2 * np.pi)), np.sin(a), 0.0])
    r = rodrigues(eje * np.radians(incl)) @ rodrigues(np.array([0, 0, rng.uniform(-np.pi, np.pi)]))
    t = np.array([rng.uniform(-0.1, 0.1) * z / 2, rng.uniform(-0.1, 0.1) * z / 2, z])
    return r, t


def ensayo(rng, z, incl, sigma=SIG):
    r, t = verdad(rng, z, incl)
    obs = proyectar(r, t) + rng.normal(0, sigma, (len(G), 2))
    r0, t0 = pose_inicial(obs)
    re, te = refinar(obs, r0, t0)
    e = te - t
    return angulo(re @ r.T), np.abs(e[2]), np.hypot(e[0], e[1]), (re, te, r, t)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print(f"DATOS SINTETICOS (semilla 103): marcador 3x3 puntos, paso 0.05 m, camara ILUSTRATIVA f = 800 px, ruido {SIG} px")
    rng = np.random.default_rng(103)
    r, t = verdad(rng, 2.0, 20.0)
    obs = proyectar(r, t)
    r0, t0 = pose_inicial(obs)
    re, te = refinar(obs, r0, t0)
    sin_ruido = max(angulo(re @ r.T), np.linalg.norm(te - t))
    print(f"Sin ruido (Z = 2 m, inclinacion 20 grados): error de rotacion = {angulo(re @ r.T):.2e} grados, de traslacion = {np.linalg.norm(te - t):.2e} m")
    print(f"rho (radio cuadratico medio de los puntos) = {RHO*1000:.2f} mm")
    print("Monte Carlo (200 repeticiones, inclinacion 20 grados): error segun la distancia Z")
    print("  Z [m]   rotacion mediana [grados]   >30 grados [%]   lateral med. [mm]   profundidad med. [mm]   mediana dZ/Z [%]   0.6745 sigma teorico [%]   cociente")
    ratios = {}
    for z in (0.5, 1.0, 2.0, 4.0, 8.0):
        res = [ensayo(np.random.default_rng(7000 + s), z, 20.0) for s in range(200)]
        rot = np.median([x[0] for x in res])
        lat = np.median([x[2] for x in res]) * 1000
        pz = np.array([x[1] for x in res])
        vuelco = np.mean([x[0] > 30 for x in res]) * 100
        dz = np.median(pz) / z * 100
        teo = 0.6745 * SIG * z / (800.0 * RHO * np.sqrt(len(G))) * 100
        ratios[z] = dz / teo
        print(f"  {z:5.1f}   {rot:19.3f}   {vuelco:13.1f}   {lat:15.2f}   {np.median(pz)*1000:18.2f}   {dz:14.3f}   {teo:21.3f}   {dz/teo:8.2f}")
    print("Efecto de la inclinacion del marcador (Z = 2 m, 200 repeticiones): error de rotacion [grados]")
    inc = {}
    for ang in (5.0, 20.0, 45.0):
        res = [ensayo(np.random.default_rng(8000 + s), 2.0, ang) for s in range(200)]
        a = np.array([x[0] for x in res])
        inc[ang] = np.median(a)
        print(f"  inclinacion {ang:4.1f}: mediana {np.median(a):6.3f} ; percentil 95 {np.percentile(a, 95):6.3f} ; maximo {a.max():7.3f} ; vuelcos (> 30 grados) {np.mean(a > 30)*100:4.1f} %")
    assert sin_ruido < 1e-6
    assert 0.6 < ratios[2.0] < 1.8
    assert inc[5.0] > inc[45.0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
