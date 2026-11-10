#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Utilidades comunes de los laboratorios del bloque B101 (manipuladores roboticos espaciales).

Convenciones: SI (m, rad, s, N, kg) salvo que el rotulo diga otra cosa. Marco de la base {0} y marco del extremo {E}.
Convencion Denavit-Hartenberg ESTANDAR (distal): T_i = Rz(theta) Tz(d) Tx(a) Rx(alpha); el eje de la articulacion i es z_{i-1}.
TODO dato es SINTETICO (el brazo de 7 articulaciones es un modelo didactico, no el de un brazo real).
Sin aleatoriedad sin semilla fija. Salida solo ASCII.
"""
from __future__ import annotations
import sys
import numpy as np


def cabecera(titulo: str) -> None:
    print(f"Python {sys.version.split()[0]} | numpy {np.__version__}")
    print(titulo)


def comprobar(condicion: bool, mensaje: str) -> None:
    if not condicion:
        raise AssertionError(mensaje)


def fin() -> None:
    print("Pruebas superadas.")


def rotx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def rotz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def homogenea(R, p):
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = p
    return T


def dh(a, alpha, d, theta):
    """Matriz homogenea D-H estandar en forma cerrada."""
    ct, st, ca, sa = np.cos(theta), np.sin(theta), np.cos(alpha), np.sin(alpha)
    return np.array([[ct, -st * ca, st * sa, a * ct],
                     [st, ct * ca, -ct * sa, a * st],
                     [0, sa, ca, d],
                     [0, 0, 0, 1.0]])


def dh_elemental(a, alpha, d, theta):
    """Misma matriz D-H como producto de cuatro movimientos elementales (comprobacion independiente)."""
    Tz = homogenea(rotz(theta), [0, 0, d])
    Tx = homogenea(rotx(alpha), [a, 0, 0])
    return Tz @ Tx


# Brazo SINTETICO de 7 articulaciones (rotacionales) tipo hombro-codo-muneca, sin desplazamientos laterales.
# Longitudes en m: base 0.4, brazo 0.6, antebrazo 0.6, mano 0.3 (alcance total 1.9 m con el brazo extendido en z).
D_NOM = np.array([0.4, 0.0, 0.6, 0.0, 0.6, 0.0, 0.3])
A_NOM = np.zeros(7)
ALPHA_NOM = np.radians([-90, 90, -90, 90, -90, 90, 0])
THETA0_NOM = np.zeros(7)
LIM_NOM = np.radians(170.0)   # limite articular sintetico simetrico, rad


def cadena(q, d=D_NOM, a=A_NOM, alpha=ALPHA_NOM, th0=THETA0_NOM):
    """Lista de transformaciones acumuladas T_0^i, i = 0..7 (T_0^0 = I)."""
    Ts = [np.eye(4)]
    for i in range(7):
        Ts.append(Ts[-1] @ dh(a[i], alpha[i], d[i], q[i] + th0[i]))
    return Ts


def fk(q, **kw):
    return cadena(q, **kw)[-1]


def jacobiano(q, **kw):
    """Jacobiano geometrico 6x7 (v; w) respecto del marco {0}."""
    Ts = cadena(q, **kw)
    pe = Ts[-1][:3, 3]
    J = np.zeros((6, 7))
    for i in range(7):
        z = Ts[i][:3, 2]
        o = Ts[i][:3, 3]
        J[:3, i] = np.cross(z, pe - o)
        J[3:, i] = z
    return J


def error_pose(T_des, T_act):
    """Error de pose 6x1: posicion y vector de rotacion (R_des R_act^T) en {0}."""
    ep = T_des[:3, 3] - T_act[:3, 3]
    Re = T_des[:3, :3] @ T_act[:3, :3].T
    c = (np.trace(Re) - 1) / 2
    ang = np.arccos(np.clip(c, -1, 1))
    if ang < 1e-12:
        w = np.zeros(3)
    else:
        w = ang / (2 * np.sin(ang)) * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
    return np.concatenate([ep, w])


def ik_amortiguada(T_des, q0, lam=0.05, tol=1e-9, itmax=300, **kw):
    """Newton con pseudoinversa amortiguada. Devuelve (q, iteraciones, error)."""
    q = np.array(q0, float)
    for it in range(itmax):
        e = error_pose(T_des, fk(q, **kw))
        if np.linalg.norm(e) < tol:
            return q, it, np.linalg.norm(e)
        J = jacobiano(q, **kw)
        q = q + J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(6), e)
    return q, itmax, np.linalg.norm(error_pose(T_des, fk(q, **kw)))


# --- calibracion cinematica (B101-C05 y B101-C08) ---
TOOL = np.array([0.05, 0.02, 0.15])   # herramienta sintetica en {7}, m (fuera del eje z7)
NPAR = 10                              # 7 desfases de angulo + errores de d1, d3, d5


def pos_tool(q, p):
    """Posicion de la herramienta en {0} con el vector de parametros p = [dtheta1..7, dd1, dd3, dd5]."""
    d = D_NOM.copy()
    d[[0, 2, 4]] += p[7:10]
    T = fk(q, d=d, th0=THETA0_NOM + p[:7])
    return T[:3, :3] @ TOOL + T[:3, 3]


def jac_param(qs, p, h=1e-6):
    """Jacobiano de las posiciones (3 por pose) respecto de los NPAR parametros, por diferencias centrales."""
    cols = []
    for k in range(NPAR):
        dp = np.zeros(NPAR)
        dp[k] = h
        a = np.concatenate([pos_tool(q, p + dp) for q in qs])
        b = np.concatenate([pos_tool(q, p - dp) for q in qs])
        cols.append((a - b) / (2 * h))
    return np.array(cols).T


def calibrar(qs, medidas, p0=None, iteraciones=15):
    """Gauss-Newton con mejor ajuste de norma minima (lstsq con corte de valores singulares)."""
    p = np.zeros(NPAR) if p0 is None else np.array(p0, float)
    y = np.concatenate(medidas)
    for _ in range(iteraciones):
        r = y - np.concatenate([pos_tool(q, p) for q in qs])
        J = jac_param(qs, p)
        dp = np.linalg.lstsq(J, r, rcond=1e-9)[0]
        p = p + dp
        if np.linalg.norm(dp) < 1e-13:
            break
    return p
