#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C15: parametros de Stokes, matrices de Mueller y calculo de Jones por dos vias.

Datos: ninguna constante externa. Los estados de luz (grado de polarizacion 0,30 y angulo de 20 grados; luz parcialmente polarizada de Stokes (1; 0,2; 0,1; -0,05)) son SINTETICOS e ILUSTRATIVOS.
Modelo: Mueller de polarizador lineal y de retardador (retardancia delta, eje rapido theta); Jones con las mismas piezas; conversion Jones-Stokes con S3 = 2 Im(Ex* Ey) (convencion fijada en el codigo).
Supuestos: componentes ideales, haz colimado, longitud de onda unica. Validez: no modela cromatismo del retardador ni polarizacion instrumental.
Tolerancia: Mueller y Jones coinciden a 1e-12; ley de Malus a 1e-12; el retardador conserva el grado de polarizacion a 1e-12.
"""
from __future__ import annotations
import cmath, math, platform, sys


def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def pol(theta):
    c, s = math.cos(2 * theta), math.sin(2 * theta)
    return [[0.5, 0.5 * c, 0.5 * s, 0], [0.5 * c, 0.5 * c * c, 0.5 * c * s, 0], [0.5 * s, 0.5 * c * s, 0.5 * s * s, 0], [0, 0, 0, 0]]


def ret(delta, theta):
    c, s = math.cos(2 * theta), math.sin(2 * theta)
    cd, sd = math.cos(delta), math.sin(delta)
    return [[1, 0, 0, 0],
            [0, c * c + s * s * cd, c * s * (1 - cd), s * sd],
            [0, c * s * (1 - cd), s * s + c * c * cd, -c * sd],
            [0, -s * sd, c * sd, cd]]


def jones_rot(J, theta):
    c, s = math.cos(theta), math.sin(theta)
    R = [[c, s], [-s, c]]
    Ri = [[c, -s], [s, c]]
    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return mm(Ri, mm(J, R))


def jones_ret(delta, theta):
    return jones_rot([[cmath.exp(-1j * delta / 2), 0], [0, cmath.exp(1j * delta / 2)]], theta)


def jones_pol(theta):
    return jones_rot([[1, 0], [0, 0]], theta)


def jones_a_stokes(E):
    ex, ey = E
    return [abs(ex) ** 2 + abs(ey) ** 2, abs(ex) ** 2 - abs(ey) ** 2, 2 * (ex * ey.conjugate()).real, 2 * (ex.conjugate() * ey).imag]


def jv(J, E):
    return [J[0][0] * E[0] + J[0][1] * E[1], J[1][0] * E[0] + J[1][1] * E[1]]


def grado(S):
    return math.sqrt(S[1] ** 2 + S[2] ** 2 + S[3] ** 2) / S[0]


def angulo(S):
    return 0.5 * math.degrees(math.atan2(S[2], S[1]))


def calcular():
    r = {}
    p, chi = 0.30, math.radians(20.0)
    S = [1.0, p * math.cos(2 * chi), p * math.sin(2 * chi), 0.0]
    r["S"] = S
    r["P"], r["psi"] = grado(S), angulo(S)
    # Malus con luz 100 % polarizada a 0 grados
    r["malus"] = []
    for th in (0, 30, 45, 60, 90):
        out = mat_vec(pol(math.radians(th)), [1, 1, 0, 0])[0]
        r["malus"].append((th, out, math.cos(math.radians(th)) ** 2))
    # media onda a phi: psi -> 2 phi - psi
    r["hwp"] = []
    for phi in (0.0, 10.0, 22.5, 45.0):
        o = mat_vec(ret(math.pi, math.radians(phi)), S)
        r["hwp"].append((phi, angulo(o), grado(o), 2 * phi - 20.0))
    # cuarto de onda a 45 grados sobre luz horizontal: circular
    o = mat_vec(ret(math.pi / 2, math.radians(45.0)), [1, 1, 0, 0])
    r["qwp"] = o
    # cadena: no polarizada -> polarizador 0 -> QWP 45 -> analizador a theta
    r["cadena"] = []
    for th in (0, 45, 90, 135):
        M = mat_mul(pol(math.radians(th)), mat_mul(ret(math.pi / 2, math.radians(45.0)), pol(0.0)))
        sm = mat_vec(M, [1, 1, 0, 0])[0]
        E = [1 + 0j, 0j]
        E = jv(jones_pol(0.0), E)
        E = jv(jones_ret(math.pi / 2, math.radians(45.0)), E)
        E = jv(jones_pol(math.radians(th)), E)
        sj = jones_a_stokes(E)[0]
        r["cadena"].append((th, sm, sj))
    # polarizacion parcial a traves de un retardador cualquiera: P conservado
    S2 = [1.0, 0.2, 0.1, -0.05]
    o2 = mat_vec(ret(math.radians(77.0), math.radians(13.0)), S2)
    r["P_antes"], r["P_despues"] = grado(S2), grado(o2)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    S = r["S"]
    print(f"estado inicial: S = ({S[0]:.4f}; {S[1]:.4f}; {S[2]:.4f}; {S[3]:.4f}) ; P = {r['P']:.4f} ; angulo = {r['psi']:.3f} grados")
    print("ley de Malus (polarizador a theta, luz 100 % polarizada a 0 grados): theta, I salida, cos^2")
    for th, o, m in r["malus"]:
        print(f"  {th:3d} {o:.6f} {m:.6f}")
    print("lamina de media onda a phi sobre el estado inicial: phi, angulo salida, P, 2 phi - angulo inicial")
    for phi, a, P, esp in r["hwp"]:
        print(f"  {phi:5.1f} {a:8.3f} {P:.4f} {esp:8.3f}")
    q = r["qwp"]
    print(f"cuarto de onda a 45 grados sobre luz horizontal: S = ({q[0]:.4f}; {q[1]:.4f}; {q[2]:.4f}; {q[3]:.4f})")
    print("cadena: luz horizontal, polarizador 0, cuarto de onda 45 y analizador: theta, intensidad Mueller, intensidad Jones")
    for th, a, b in r["cadena"]:
        print(f"  {th:3d} {a:.6f} {b:.6f}")
    print(f"P antes {r['P_antes']:.6f} ; P despues del retardador {r['P_despues']:.6f}")
    for th, o, m in r["malus"]:
        assert abs(o - m) < 1e-12
    for phi, a, P, esp in r["hwp"]:
        assert abs(((a - esp + 90) % 180) - 90) < 1e-9 and abs(P - r["P"]) < 1e-12
    assert abs(r["qwp"][3]) > 0.999999 and abs(r["qwp"][1]) < 1e-12
    for th, a, b in r["cadena"]:
        assert abs(a - b) < 1e-12
    assert abs(r["P_antes"] - r["P_despues"]) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
