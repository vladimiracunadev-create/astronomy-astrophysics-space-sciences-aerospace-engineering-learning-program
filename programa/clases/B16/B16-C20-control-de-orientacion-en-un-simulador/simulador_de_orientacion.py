#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C20: simulador de orientación de un cuerpo rígido con cuaterniones.

Datos: SINTÉTICOS (simulados). Cuerpo rígido con tensor de inercia
J = [[50, 1, 0.5], [1, 40, 2], [0.5, 2, 30]] kg m^2 (definido positivo),
ley PD de actitud con límite de par por eje u_max.
Convenciones: cuaternión unitario q = [q0, qv] (escalar primero), rotación del
sistema inercial al del cuerpo; cinemática q' = (1/2) q ⊗ [0, w] con w en el
sistema del cuerpo; cuaternión de error q_e = q_obj^-1 ⊗ q.
Ley: u = -2 Kp sgn(q_e0) q_ev - Kd w, saturada por eje.
Integración: DOP853, rtol 1e-12, atol 1e-14.
Referencias independientes:
  (1) sin par: el momento angular en el sistema inercial H_i = R(q) J w y la
      energía T = (1/2) w.J w se conservan; |q| = 1 (sin renormalizar);
  (2) ángulos pequeños con J diagonal y giro de 0.02 rad alrededor de x: la
      respuesta coincide con el segundo orden theta'' + (Kd/J1) theta' + (Kp/J1) theta = 0;
  (3) sgn(q_e0): si el cuaternión inicial está a 0.1 rad del objetivo pero se
      representa con q_e0 < 0 (el opuesto, misma orientación), la ley con signo
      corrige 0.1 rad; la ley sin signo gira por el camino largo;
  (4) maniobra grande de 90 grados con saturación: converge a la orientación objetivo.
Supuestos: cuerpo rígido, par exacto, sin perturbaciones ni ruido de sensor.
Tolerancia: 1e-9 en (1); 1e-5 rad en (2); 1e-4 rad en (4).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp

Jm = np.array([[50.0, 1.0, 0.5], [1.0, 40.0, 2.0], [0.5, 2.0, 30.0]])
Kp, Kd = 12.0, 90.0


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def qmul(a, b):
    a0, av, b0, bv = a[0], a[1:], b[0], b[1:]
    return np.concatenate([[a0 * b0 - av @ bv], a0 * bv + b0 * av + np.cross(av, bv)])


def qinv(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def rot(q):
    """Matriz que pasa componentes del sistema inercial al del cuerpo."""
    q0, (q1, q2, q3) = q[0], q[1:]
    return np.array([
        [1 - 2*(q2*q2 + q3*q3), 2*(q1*q2 + q0*q3), 2*(q1*q3 - q0*q2)],
        [2*(q1*q2 - q0*q3), 1 - 2*(q1*q1 + q3*q3), 2*(q2*q3 + q0*q1)],
        [2*(q1*q3 + q0*q2), 2*(q2*q3 - q0*q1), 1 - 2*(q1*q1 + q2*q2)]])


def eje_angulo(eje, ang):
    eje = np.asarray(eje, float); eje /= np.linalg.norm(eje)
    return np.concatenate([[math.cos(ang / 2)], math.sin(ang / 2) * eje])


def angulo_error(q, qobj):
    qe = qmul(qinv(qobj), q)
    return 2 * math.atan2(np.linalg.norm(qe[1:]), abs(qe[0]))


def modelo(J, qobj, umax, signo=True, libre=False):
    def f(t, x):
        q, w = x[:4], x[4:]
        if libre:
            u = np.zeros(3)
        else:
            qe = qmul(qinv(qobj), q)
            s = (1.0 if qe[0] >= 0 else -1.0) if signo else 1.0
            u = np.clip(-2 * Kp * s * qe[1:] - Kd * w, -umax, umax)
        dq = 0.5 * qmul(q, np.concatenate([[0.0], w]))
        dw = np.linalg.solve(J, -np.cross(w, J @ w) + u)
        return np.concatenate([dq, dw])
    return f


def corre(J, q0, w0, qobj, T, umax=1e9, signo=True, libre=False, n=2001):
    t = np.linspace(0, T, n)
    s = solve_ivp(modelo(J, qobj, umax, signo, libre), [0, T], np.concatenate([q0, w0]),
                  t_eval=t, method="DOP853", rtol=1e-12, atol=1e-14)
    return t, s.y


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    qid = np.array([1.0, 0, 0, 0])

    # (1) conservación sin par
    q0 = eje_angulo([1, 2, -1], 0.7); w0 = np.array([0.05, -0.03, 0.04])
    t, y = corre(Jm, q0, w0, qid, 200.0, libre=True, n=4001)
    H = np.array([rot(y[:4, k]).T @ (Jm @ y[4:, k]) for k in range(y.shape[1])])
    E = 0.5 * np.einsum("ti,ij,tj->t", y[4:].T, Jm, y[4:].T)
    nq = np.linalg.norm(y[:4], axis=0)
    dH = np.max(np.linalg.norm(H - H[0], axis=1)) / np.linalg.norm(H[0])
    dE, dq = np.ptp(E) / E[0], np.max(np.abs(nq - 1))
    print(f"sin par, 200 s: dH/H = {dH:.2e}, dE/E = {dE:.2e}, max||q|-1| = {dq:.2e}")
    prueba(dH < 1e-9 and dE < 1e-9 and dq < 1e-9, "invariantes")

    # (2) ángulos pequeños con J diagonal
    Jd = np.diag([50.0, 40.0, 30.0])
    th0 = 0.02
    t, y = corre(Jd, eje_angulo([1, 0, 0], th0), np.zeros(3), qid, 60.0, n=3001)
    ang = np.array([2 * math.atan2(y[1, k], y[0, k]) for k in range(y.shape[1])])
    wn, z = math.sqrt(Kp / 50.0), Kd / (2 * math.sqrt(Kp * 50.0))
    wd = wn * math.sqrt(1 - z * z) if z < 1 else None
    if z < 1:
        lin = th0 * np.exp(-z * wn * t) * (np.cos(wd * t) + z * wn / wd * np.sin(wd * t))
    else:
        s1, s2 = -wn * (z - math.sqrt(z*z - 1)), -wn * (z + math.sqrt(z*z - 1))
        lin = th0 * (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t)) / (s2 - s1)
    err = np.max(np.abs(ang - lin))
    print(f"pequeño ángulo: wn = {wn:.4f} rad/s, zeta = {z:.3f}; error máx frente al modelo lineal = {err:.2e} rad")
    prueba(err < 1e-5, "ángulos pequeños")

    # (3) signo del escalar: el opuesto de un cuaternión es la misma orientación
    qobj = eje_angulo([0, 0, 1], math.radians(30))
    qini = -qmul(qobj, eje_angulo([1, 0, 0], 0.1))      # 0.1 rad de error, representado con q0 < 0
    print(f"orientación inicial a {angulo_error(qini, qobj):.3f} rad del objetivo (q_e0 = {qmul(qinv(qobj), qini)[0]:+.4f})")
    maxang = {}
    for signo in (True, False):
        t, y = corre(Jm, qini, np.zeros(3), qobj, 300.0, signo=signo, n=3001)
        e = np.array([angulo_error(y[:4, k], qobj) for k in range(y.shape[1])])
        maxang[signo] = e.max()
        print(f"  ley {'con' if signo else 'sin'} sgn(q_e0): ángulo de error máx = {math.degrees(e.max()):7.2f}°, final = {math.degrees(e[-1]):.2e}°")
    prueba(maxang[True] <= 0.1 + 1e-9, "con signo: giro corto")
    prueba(maxang[False] > 3.0, "sin signo: desenrolla casi media vuelta o más")

    # (4) maniobra de 90 grados con saturación
    for umax in (1e9, 0.5):
        qobj = eje_angulo([1, 1, 1], math.radians(90))
        t, y = corre(Jm, qid, np.zeros(3), qobj, 600.0, umax=umax, n=3001)
        e = np.array([angulo_error(y[:4, k], qobj) for k in range(y.shape[1])])
        fuera = np.nonzero(e > math.radians(1.0))[0]
        ts = t[fuera[-1]] if len(fuera) else 0.0
        etiqueta = "sin límite" if umax > 1e6 else f"u_max = {umax} N m por eje"
        print(f"90° alrededor de (1,1,1), {etiqueta}: error final {math.degrees(e[-1]):.2e}°; "
              f"entra y se queda en 1° a los {ts:.1f} s; |w| máx {np.max(np.linalg.norm(y[4:], axis=0)):.4f} rad/s")
        prueba(e[-1] < 1e-4, "convergencia")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
