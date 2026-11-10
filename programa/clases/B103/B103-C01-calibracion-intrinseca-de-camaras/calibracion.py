#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C01: calibracion intrinseca plana (tipo Zhang) sobre datos SINTETICOS.

Todo es sintetico y generado con semilla 103: la camara (fx = fy = 800 px, cx = 640, cy = 480, imagen 1280 x 960,
k1 = -0.12, k2 = 0.05), el patron (tablero 9 x 6 esquinas, casilla de 25 mm) y las 12 vistas. Ruido gaussiano de 0.3 px.
Modelo: p = K * D(x/z, y/z), con distorsion radial D(x, y) = (x, y) (1 + k1 r2 + k2 r4). Unidades: px y m. Sistema: camara
con z hacia delante, patron en su plano z = 0.
Metodo: homografia por DLT en cada vista -> restricciones de Zhang sobre B = K^-T K^-1 -> K; luego k1, k2 por minimos
cuadrados lineales; 4 iteraciones alternando (quitar distorsion, recalibrar); y un refinamiento final de Levenberg-Marquardt
(jacobiano numerico) sobre K, k1, k2 y las poses que minimiza el error de reproyeccion. Numpy requerido.
Verificacion: error frente a los parametros verdaderos y RMS de reproyeccion; tolerancia 1 % en focal, 0.6 px de RMS.
"""
from __future__ import annotations
import platform
import numpy as np

W, H = 1280, 960
K_VERDAD = np.array([[800.0, 0.0, 640.0], [0.0, 800.0, 480.0], [0.0, 0.0, 1.0]])
DIST_VERDAD = (-0.12, 0.05)
SIGMA_PX = 0.3
NX, NY, LADO = 9, 6, 0.025


def patron():
    xs, ys = np.meshgrid(np.arange(NX) * LADO, np.arange(NY) * LADO)
    return np.stack([xs.ravel() - (NX - 1) * LADO / 2, ys.ravel() - (NY - 1) * LADO / 2], axis=1)


def rot(ax, ay, az):
    cx, sx, cy, sy, cz, sz = np.cos(ax), np.sin(ax), np.cos(ay), np.sin(ay), np.cos(az), np.sin(az)
    rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return rz @ ry @ rx


def proyectar(k, dist, r, t, pts2):
    p3 = np.c_[pts2, np.zeros(len(pts2))] @ r.T + t
    x, y = p3[:, 0] / p3[:, 2], p3[:, 1] / p3[:, 2]
    r2 = x * x + y * y
    f = 1 + dist[0] * r2 + dist[1] * r2 * r2
    return np.stack([k[0, 0] * x * f + k[0, 2], k[1, 1] * y * f + k[1, 2]], axis=1)


def homografia(a, b):
    filas = []
    for (x, y), (u, v) in zip(a, b):
        filas.append([x, y, 1, 0, 0, 0, -u * x, -u * y, -u])
        filas.append([0, 0, 0, x, y, 1, -v * x, -v * y, -v])
    h = np.linalg.svd(np.array(filas))[2][-1].reshape(3, 3)
    return h / h[2, 2]


def vij(h, i, j):
    return np.array([h[0, i] * h[0, j], h[0, i] * h[1, j] + h[1, i] * h[0, j], h[1, i] * h[1, j],
                     h[2, i] * h[0, j] + h[0, i] * h[2, j], h[2, i] * h[1, j] + h[1, i] * h[2, j], h[2, i] * h[2, j]])


def k_desde_homografias(hs):
    v = []
    for h in hs:
        v.append(vij(h, 0, 1))
        v.append(vij(h, 0, 0) - vij(h, 1, 1))
    b = np.linalg.svd(np.array(v))[2][-1]
    if b[0] < 0:
        b = -b
    b11, b12, b22, b13, b23, b33 = b
    cy = (b12 * b13 - b11 * b23) / (b11 * b22 - b12 ** 2)
    lam = b33 - (b13 ** 2 + cy * (b12 * b13 - b11 * b23)) / b11
    fx = np.sqrt(lam / b11)
    fy = np.sqrt(lam * b11 / (b11 * b22 - b12 ** 2))
    cx = -b13 * fx ** 2 / lam
    return np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1.0]])


def pose_desde_h(k, h):
    ki = np.linalg.inv(k)
    lam = 1.0 / np.linalg.norm(ki @ h[:, 0])
    r1, r2, t = lam * ki @ h[:, 0], lam * ki @ h[:, 1], lam * ki @ h[:, 2]
    r = np.stack([r1, r2, np.cross(r1, r2)], axis=1)
    u, _, vt = np.linalg.svd(r)
    return u @ vt, t


def quitar_distorsion(k, dist, px):
    x, y = (px[:, 0] - k[0, 2]) / k[0, 0], (px[:, 1] - k[1, 2]) / k[1, 1]
    xu, yu = x.copy(), y.copy()
    for _ in range(20):
        r2 = xu * xu + yu * yu
        f = 1 + dist[0] * r2 + dist[1] * r2 * r2
        xu, yu = x / f, y / f
    return np.stack([xu * k[0, 0] + k[0, 2], yu * k[1, 1] + k[1, 2]], axis=1)


def estimar_dist(k, vistas, poses):
    a, b = [], []
    for obs, (r, t) in zip(vistas, poses):
        p3 = np.c_[PAT, np.zeros(len(PAT))] @ r.T + t
        x, y = p3[:, 0] / p3[:, 2], p3[:, 1] / p3[:, 2]
        r2 = x * x + y * y
        ideal_u, ideal_v = k[0, 0] * x + k[0, 2], k[1, 1] * y + k[1, 2]
        a += list(np.c_[k[0, 0] * x * r2, k[0, 0] * x * r2 ** 2]) + list(np.c_[k[1, 1] * y * r2, k[1, 1] * y * r2 ** 2])
        b += list(obs[:, 0] - ideal_u) + list(obs[:, 1] - ideal_v)
    sol = np.linalg.lstsq(np.array(a), np.array(b), rcond=None)[0]
    return sol


def rms_reproyeccion(k, dist, vistas, poses):
    e = []
    for obs, (r, t) in zip(vistas, poses):
        e.append(np.sum((proyectar(k, dist, r, t, PAT) - obs) ** 2, axis=1))
    return float(np.sqrt(np.mean(np.concatenate(e))))


def generar(rng, n):
    vistas, poses = [], []
    while len(vistas) < n:
        r = rot(rng.uniform(-0.5, 0.5), rng.uniform(-0.5, 0.5), rng.uniform(-0.3, 0.3))
        t = np.array([rng.uniform(-0.05, 0.05), rng.uniform(-0.04, 0.04), rng.uniform(0.35, 0.7)])
        px = proyectar(K_VERDAD, DIST_VERDAD, r, t, PAT)
        if px[:, 0].min() > 20 and px[:, 0].max() < W - 20 and px[:, 1].min() > 20 and px[:, 1].max() < H - 20:
            vistas.append(px + rng.normal(0, SIGMA_PX, px.shape))
            poses.append((r, t))
    return vistas, poses


def calibrar(vistas, iteraciones=4):
    dist = np.zeros(2)
    k = None
    hist = []
    for _ in range(iteraciones):
        k_prev = np.array([[800.0, 0, 640.0], [0, 800.0, 480.0], [0, 0, 1.0]]) if k is None else k
        und = [quitar_distorsion(k_prev, dist, o) for o in vistas]
        hs = [homografia(PAT, u) for u in und]
        k = k_desde_homografias(hs)
        poses = [pose_desde_h(k, h) for h in hs]
        dist = estimar_dist(k, vistas, poses)
        hist.append((k[0, 0], k[1, 1], k[0, 2], k[1, 2], dist[0], dist[1], rms_reproyeccion(k, dist, vistas, poses)))
    k, dist, poses = refinar(k, dist, poses, vistas)
    hist.append((k[0, 0], k[1, 1], k[0, 2], k[1, 2], dist[0], dist[1], rms_reproyeccion(k, dist, vistas, poses)))
    return k, dist, poses, hist


def rodrigues(v):
    th = np.linalg.norm(v)
    if th < 1e-12:
        return np.eye(3)
    k = v / th
    km = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + np.sin(th) * km + (1 - np.cos(th)) * km @ km


def vec_rodrigues(r):
    th = np.arccos(np.clip((np.trace(r) - 1) / 2, -1, 1))
    if th < 1e-12:
        return np.zeros(3)
    w = np.array([r[2, 1] - r[1, 2], r[0, 2] - r[2, 0], r[1, 0] - r[0, 1]]) / (2 * np.sin(th))
    return w * th


def residuos(par, vistas):
    k = np.array([[par[0], 0, par[2]], [0, par[1], par[3]], [0, 0, 1.0]])
    dist = par[4:6]
    out = []
    for i, obs in enumerate(vistas):
        q = par[6 + 6 * i: 12 + 6 * i]
        out.append((proyectar(k, dist, rodrigues(q[:3]), q[3:], PAT) - obs).ravel())
    return np.concatenate(out)


def refinar(k, dist, poses, vistas, iteraciones=30):
    """Levenberg-Marquardt con jacobiano numerico sobre K, k1, k2 y las poses (minimiza el error de reproyeccion)."""
    par = np.concatenate([[k[0, 0], k[1, 1], k[0, 2], k[1, 2], dist[0], dist[1]]] +
                         [np.concatenate([vec_rodrigues(r), t]) for r, t in poses])
    lam = 1e-3
    r0 = residuos(par, vistas)
    for _ in range(iteraciones):
        j = np.empty((len(r0), len(par)))
        for c in range(len(par)):
            d = np.zeros(len(par))
            d[c] = 1e-6 * max(1.0, abs(par[c]))
            j[:, c] = (residuos(par + d, vistas) - r0) / d[c]
        a, g = j.T @ j, j.T @ r0
        while True:
            paso = np.linalg.solve(a + lam * np.diag(np.diag(a)), -g)
            r1 = residuos(par + paso, vistas)
            if r1 @ r1 < r0 @ r0:
                par, r0, lam = par + paso, r1, lam / 3
                break
            lam *= 4
            if lam > 1e8:
                break
        if lam > 1e8 or np.linalg.norm(paso) < 1e-9:
            break
    k = np.array([[par[0], 0, par[2]], [0, par[1], par[3]], [0, 0, 1.0]])
    poses = [(rodrigues(par[6 + 6 * i: 9 + 6 * i]), par[9 + 6 * i: 12 + 6 * i]) for i in range(len(vistas))]
    return k, par[4:6], poses


PAT = patron()


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    rng = np.random.default_rng(103)
    vistas, _ = generar(rng, 12)
    print(f"DATOS SINTETICOS (semilla 103): 12 vistas, tablero {NX}x{NY}, casilla {LADO*1000:.0f} mm, ruido {SIGMA_PX} px")
    print(f"Verdad: fx=fy=800.0 cx=640.0 cy=480.0 k1={DIST_VERDAD[0]} k2={DIST_VERDAD[1]}")
    k, dist, poses, hist = calibrar(vistas)
    print("iter(1-4 forma cerrada; 5 = refinamiento LM)     fx       fy       cx       cy       k1       k2     RMS[px]")
    for i, h in enumerate(hist, 1):
        print(f"{i:4d} {h[0]:8.2f} {h[1]:8.2f} {h[2]:8.2f} {h[3]:8.2f} {h[4]:8.4f} {h[5]:8.4f} {h[6]:9.4f}")
    print(f"Error relativo de fx = {abs(k[0,0]-800)/800*100:.3f} %; de fy = {abs(k[1,1]-800)/800*100:.3f} %")
    print(f"Error de punto principal = ({k[0,2]-640:.2f}, {k[1,2]-480:.2f}) px")
    # Sin modelar la distorsion (k = 0): error de reproyeccion
    hs0 = [homografia(PAT, o) for o in vistas]
    k0 = k_desde_homografias(hs0)
    p0 = [pose_desde_h(k0, h) for h in hs0]
    rms0 = rms_reproyeccion(k0, np.zeros(2), vistas, p0)
    print(f"Sin modelo de distorsion: fx = {k0[0,0]:.2f}, RMS = {rms0:.4f} px")
    # Monte Carlo de la focal frente al numero de vistas
    print("Monte Carlo (30 repeticiones): desviacion de fx segun el numero de vistas")
    for n in (3, 6, 12):
        fx = []
        for s in range(30):
            v, _ = generar(np.random.default_rng(1000 + s), n)
            fx.append(calibrar(v)[0][0, 0])
        print(f"  {n:2d} vistas: media = {np.mean(fx):8.2f}, desv. tipica = {np.std(fx, ddof=1):7.3f} px")
    assert abs(k[0, 0] - 800) / 800 < 0.01 and abs(k[1, 1] - 800) / 800 < 0.01
    assert abs(dist[0] - DIST_VERDAD[0]) < 0.05
    assert hist[-1][6] < 0.5
    assert rms0 > hist[-1][6]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
