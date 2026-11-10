#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Utilidades comunes de los laboratorios del bloque B99 (localizacion y mapeo robotico).

Convenciones del bloque: mundo 2D, metros y radianes; una pose es (x, y, theta) con theta antihorario respecto del eje x del
marco del mundo; el marco del cuerpo tiene x hacia adelante. TODO dato de los laboratorios es SINTETICO (generado con
semilla fija), no una medicion de un robot. Solo numpy. Salida solo ASCII para que sea identica en cualquier consola.
"""
from __future__ import annotations
import sys
import numpy as np


def cabecera(titulo: str) -> None:
    print(f"Python {sys.version.split()[0]} | numpy {np.__version__}")
    print(titulo)


def comprobar(condicion: bool, mensaje: str) -> None:
    """Falla con un mensaje claro si una comprobacion no se cumple."""
    if not condicion:
        raise AssertionError(mensaje)


def fin() -> None:
    print("Pruebas superadas.")


# ---------------------------------------------------------------- geometria SE(2)
def wrap(a):
    """Lleva un angulo (o un arreglo) al intervalo [-pi, pi)."""
    return (np.asarray(a) + np.pi) % (2 * np.pi) - np.pi


def rot(th: float) -> np.ndarray:
    c, s = np.cos(th), np.sin(th)
    return np.array([[c, -s], [s, c]])


def componer(a, b):
    """a (+) b: la pose b expresada en el marco de a, llevada al marco del mundo."""
    p = np.asarray(a[:2]) + rot(a[2]) @ np.asarray(b[:2])
    return np.array([p[0], p[1], float(wrap(a[2] + b[2]))])


def inversa(a):
    t = -rot(a[2]).T @ np.asarray(a[:2])
    return np.array([t[0], t[1], float(wrap(-a[2]))])


def entre(a, b):
    """Pose relativa de b vista desde a: inversa(a) (+) b."""
    return componer(inversa(a), b)


def integrar(rel, origen=(0.0, 0.0, 0.0)):
    """Integra movimientos relativos (n,3) a poses absolutas (n+1,3)."""
    poses = [np.array(origen, dtype=float)]
    for r in rel:
        poses.append(componer(poses[-1], r))
    return np.array(poses)


def lazo_cuadrado(lado_pasos: int = 40, paso: float = 0.5):
    """Verdad sintetica: cuadrado de lado_pasos*paso metros recorrido antihorario, con giro de 90 grados en cada
    esquina. Devuelve las poses absolutas (4*lado_pasos+1, 3) y los movimientos relativos (4*lado_pasos, 3).
    La ultima pose coincide con la primera."""
    rel = []
    for lado in range(4):
        for k in range(lado_pasos):
            giro = np.pi / 2 if k == lado_pasos - 1 else 0.0
            rel.append([paso, 0.0, giro])
    rel = np.array(rel)
    return integrar(rel), rel


def odometria_ruidosa(rel, rng, sig_t=0.02, sig_r=0.005, sesgo_rot=0.0):
    """Movimientos relativos medidos = verdad (+) ruido gaussiano en el marco del cuerpo (+ sesgo de rotacion por paso)."""
    n = len(rel)
    ruido = np.column_stack([rng.normal(0, sig_t, n), rng.normal(0, sig_t, n), rng.normal(0, sig_r, n) + sesgo_rot])
    return np.array([componer(r, e) for r, e in zip(rel, ruido)])


# ---------------------------------------------------------------- ajuste de cuerpo rigido 2D
def kabsch2d(P, Q, w=None, escala=False):
    """Encuentra (s, R, t) con Q ~ s R P + t por minimos cuadrados ponderados (SVD, Horn/Umeyama). P, Q: (n,2)."""
    P = np.asarray(P, float)
    Q = np.asarray(Q, float)
    w = np.ones(len(P)) if w is None else np.asarray(w, float)
    w = w / w.sum()
    mp, mq = w @ P, w @ Q
    Pc, Qc = P - mp, Q - mq
    H = (Pc * w[:, None]).T @ Qc
    U, S, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1.0, d])
    R = Vt.T @ D @ U.T
    s = 1.0
    if escala:
        s = float(np.trace(np.diag(S) @ D) / (w @ np.sum(Pc**2, axis=1)))
    t = mq - s * R @ mp
    return s, R, t


# ---------------------------------------------------------------- error de trayectoria
def ate_rmse(est_xy, gt_xy, escala=False):
    """Error absoluto de trayectoria: RMSE de la traslacion tras alinear est con gt por cuerpo rigido (SVD)."""
    s, R, t = kabsch2d(est_xy, gt_xy, escala=escala)
    al = (s * (R @ np.asarray(est_xy).T)).T + t
    e = np.linalg.norm(al - np.asarray(gt_xy), axis=1)
    return float(np.sqrt(np.mean(e**2))), al


def rpe_trans(est, gt, delta=1):
    """Error relativo de pose: para cada par (i, i+delta) compara el movimiento relativo estimado con el verdadero.
    Devuelve (rmse_traslacion [m], rmse_rotacion [rad]). No requiere alineacion."""
    et, er = [], []
    for i in range(len(est) - delta):
        dg = entre(gt[i], gt[i + delta])
        de = entre(est[i], est[i + delta])
        err = entre(dg, de)
        et.append(np.hypot(err[0], err[1]))
        er.append(abs(err[2]))
    et, er = np.array(et), np.array(er)
    return float(np.sqrt(np.mean(et**2))), float(np.sqrt(np.mean(er**2)))


# ---------------------------------------------------------------- grafo de poses
def error_arista(xi, xj, z):
    """e = (R_i^T (t_j - t_i) - z_xy, wrap(th_j - th_i - z_th))."""
    d = xj[:2] - xi[:2]
    e = np.empty(3)
    e[:2] = rot(xi[2]).T @ d - z[:2]
    e[2] = float(wrap(xj[2] - xi[2] - z[2]))
    return e


def jacobianos_arista(xi, xj):
    """Jacobianos analiticos (3x3) de e respecto de x_i y de x_j."""
    c, s = np.cos(xi[2]), np.sin(xi[2])
    Rt = np.array([[c, s], [-s, c]])
    dRt = np.array([[-s, c], [-c, -s]])
    d = xj[:2] - xi[:2]
    Ji = np.zeros((3, 3))
    Jj = np.zeros((3, 3))
    Ji[:2, :2] = -Rt
    Ji[:2, 2] = dRt @ d
    Ji[2, 2] = -1.0
    Jj[:2, :2] = Rt
    Jj[2, 2] = 1.0
    return Ji, Jj


def jacobiano_numerico(xi, xj, z, h=1e-6):
    Ji = np.zeros((3, 3))
    Jj = np.zeros((3, 3))
    for k in range(3):
        d = np.zeros(3)
        d[k] = h
        Ji[:, k] = (error_arista(xi + d, xj, z) - error_arista(xi - d, xj, z)) / (2 * h)
        Jj[:, k] = (error_arista(xi, xj + d, z) - error_arista(xi, xj - d, z)) / (2 * h)
    return Ji, Jj


def info_diag(sig_t, sig_r):
    return np.diag([1 / sig_t**2, 1 / sig_t**2, 1 / sig_r**2])


def chi2_total(x, aristas):
    return float(sum(e @ Om @ e for e, Om in ((error_arista(x[i], x[j], z), Om) for i, j, z, Om in aristas)))


def optimizar_grafo(x0, aristas, iteraciones=30, huber=None, tol=1e-9):
    """Gauss-Newton sobre un grafo de poses 2D con la primera pose fija. aristas: lista de (i, j, z, Omega).
    Si huber no es None, cada arista se pondera con la funcion de Huber (IRLS) sobre r = sqrt(e^T Omega e).
    Devuelve (x, historial de chi2)."""
    x = np.array(x0, dtype=float)
    n = len(x)
    hist = [chi2_total(x, aristas)]
    for _ in range(iteraciones):
        H = np.zeros((3 * n, 3 * n))
        b = np.zeros(3 * n)
        for i, j, z, Om in aristas:
            e = error_arista(x[i], x[j], z)
            Ji, Jj = jacobianos_arista(x[i], x[j])
            w = 1.0
            if huber is not None:
                r = np.sqrt(e @ Om @ e)
                w = 1.0 if r <= huber else huber / r
            Om_w = w * Om
            si, sj = slice(3 * i, 3 * i + 3), slice(3 * j, 3 * j + 3)
            H[si, si] += Ji.T @ Om_w @ Ji
            H[si, sj] += Ji.T @ Om_w @ Jj
            H[sj, si] += Jj.T @ Om_w @ Ji
            H[sj, sj] += Jj.T @ Om_w @ Jj
            b[si] += Ji.T @ Om_w @ e
            b[sj] += Jj.T @ Om_w @ e
        dx = np.zeros(3 * n)
        dx[3:] = np.linalg.solve(H[3:, 3:] + 1e-9 * np.eye(3 * n - 3), -b[3:])
        x = x + dx.reshape(n, 3)
        x[:, 2] = wrap(x[:, 2])
        hist.append(chi2_total(x, aristas))
        if np.max(np.abs(dx)) < tol:
            break
    return x, hist
