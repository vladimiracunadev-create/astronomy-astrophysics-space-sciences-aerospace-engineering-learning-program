#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C04: espacio de trabajo por Monte Carlo, limites articulares, autocolision con capsulas y evasion de limites por espacio nulo.

Unidades: m, rad. Datos SINTETICOS (brazo de B101-C01; limites +-170 grados y capsulas de 0.08 m de radio, de ejemplo). Semilla 104.
Comprobacion independiente de la distancia entre segmentos: busqueda por malla densa.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: brazo de B101-C01, limites +-170 grados, capsulas de radio 0.08 m")
rng = np.random.default_rng(104)
N = 20000
P = np.array([fk(rng.uniform(-LIM_NOM, LIM_NOM, 7))[:3, 3] for _ in range(N)])
r = np.linalg.norm(P, axis=1)
print(f"Espacio de trabajo (Monte Carlo, {N} configuraciones uniformes en los limites):")
print(f"  |p| minimo = {r.min():.3f} m ; maximo = {r.max():.3f} m (alcance geometrico 1.9 m)")
comprobar(r.max() <= 1.9 + 1e-9, "no se puede superar 1.9 m")
# celdas de 0.1 m visitadas
celdas = {tuple(c) for c in np.floor(P / 0.1).astype(int)}
print(f"  celdas de 0.1 m visitadas = {len(celdas)} ; z de -1.9 a {P[:, 2].max():.2f} m")
for Lg in (170, 120, 90, 60):
    Pg = np.array([fk(rng.uniform(-np.radians(Lg), np.radians(Lg), 7))[:3, 3] for _ in range(N)])
    rg = np.linalg.norm(Pg, axis=1)
    cg = {tuple(c) for c in np.floor(Pg / 0.1).astype(int)}
    print(f"  limites +-{Lg:3d} grados: |p| maximo = {rg.max():.3f} m ; celdas de 0.1 m = {len(cg)}")


def dist_segmentos(p1, q1, p2, q2):
    """Distancia minima entre los segmentos p1q1 y p2q2 (formulacion de puntos mas cercanos acotada)."""
    d1, d2, rr = q1 - p1, q2 - p2, p1 - p2
    a, e, f = d1 @ d1, d2 @ d2, d2 @ rr
    if a <= 1e-12 and e <= 1e-12:
        return float(np.linalg.norm(rr))
    if a <= 1e-12:
        s, t = 0.0, np.clip(f / e, 0, 1)
    else:
        c = d1 @ rr
        if e <= 1e-12:
            t, s = 0.0, np.clip(-c / a, 0, 1)
        else:
            b = d1 @ d2
            den = a * e - b * b
            s = np.clip((b * f - c * e) / den, 0, 1) if den > 1e-12 else 0.0
            t = (b * s + f) / e
            if t < 0:
                t, s = 0.0, np.clip(-c / a, 0, 1)
            elif t > 1:
                t, s = 1.0, np.clip((b - c) / a, 0, 1)
    return float(np.linalg.norm((p1 + d1 * s) - (p2 + d2 * t)))


def dist_malla(p1, q1, p2, q2, n=400):
    s = np.linspace(0, 1, n)[:, None]
    A = p1 + s * (q1 - p1)
    B = p2 + s * (q2 - p2)
    return float(np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(-1).min()))


dmax = 0.0
for _ in range(300):
    p1, q1, p2, q2 = (rng.uniform(-1, 1, 3) for _ in range(4))
    dmax = max(dmax, abs(dist_segmentos(p1, q1, p2, q2) - dist_malla(p1, q1, p2, q2)))
print(f"Distancia entre segmentos: formula frente a malla de 400x400 (300 pares): diferencia max = {dmax:.2e} m")
comprobar(dmax < 5e-3, "distancia entre segmentos")

RAD = 0.08


def segmentos(q):
    O = [T[:3, 3] for T in cadena(q)]
    return {"base": (O[0], O[1]), "brazo": (O[2], O[3]), "antebrazo": (O[4], O[5]), "mano": (O[6], O[7])}


PARES = (("base", "antebrazo"), ("base", "mano"), ("brazo", "mano"))


def autocolision(q):
    S = segmentos(q)
    return min((dist_segmentos(*S[a], *S[b]) - 2 * RAD, (a, b)) for a, b in PARES)


col = 0
peor = (9.0, None)
for _ in range(5000):
    q = rng.uniform(-LIM_NOM, LIM_NOM, 7)
    m, par = autocolision(q)
    if m < 0:
        col += 1
    if m < peor[0]:
        peor = (m, par)
print(f"Autocolision (5000 configuraciones): {col} con holgura < 0 ({100 * col / 5000:.1f} %) ; holgura minima = {peor[0] * 1000:.1f} mm en {peor[1]}")
qe = np.zeros(7)
print(f"Brazo estirado q = 0: holgura minima = {autocolision(qe)[0] * 1000:.1f} mm")
comprobar(autocolision(qe)[0] > 0, "el brazo estirado no se autocolisiona")
qp = np.radians([0, 0, 0, 170, 0, -60, 0])
mq, pq = autocolision(qp)
print(f"Codo plegado a 170 grados: holgura minima = {mq * 1000:.1f} mm ({pq[0]}-{pq[1]})")
comprobar(col > 0, "debe existir alguna autocolision")

# evitacion del limite: gradiente de centrado en el espacio nulo (Liegeois), sin cambiar la pose
q0 = np.radians([160, -100, 20, 100, -150, 60, 30])
T_obj = fk(q0)
q = q0.copy()
w = lambda x: float(np.sum((x / LIM_NOM) ** 2))
for _ in range(3000):
    J = jacobiano(q)
    N_ = np.eye(7) - np.linalg.pinv(J) @ J
    g = -2 * q / LIM_NOM**2
    q = q + 5e-4 * (N_ @ g)
    q = q + J.T @ np.linalg.solve(J @ J.T + 1e-8 * np.eye(6), error_pose(T_obj, fk(q)))
print(f"Evitacion de limites: costo de centrado {w(q0):.3f} -> {w(q):.3f} ; error de pose = {np.linalg.norm(error_pose(T_obj, fk(q))):.2e}")
print(f"  mayor |q_i|/limite: {np.max(np.abs(q0)) / LIM_NOM:.3f} -> {np.max(np.abs(q)) / LIM_NOM:.3f}")
comprobar(w(q) < w(q0) and np.linalg.norm(error_pose(T_obj, fk(q))) < 1e-6, "el espacio nulo aleja de los limites sin mover el extremo")
fin()
