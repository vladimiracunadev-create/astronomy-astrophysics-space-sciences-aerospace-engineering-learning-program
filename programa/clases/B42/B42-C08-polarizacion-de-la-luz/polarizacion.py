#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C08: vectores de Jones, ley de Malus, laminas de retardo y parametros de Stokes.

Datos: ninguna constante fisica. Angulos de los elementos, la fraccion polarizada 0,6 y los 20000 fotones de la muestra son ILUSTRATIVOS (semilla 20261109).
Modelo: estados como vectores de Jones (Ex, Ey) complejos; polarizador lineal y lamina de retardo como matrices de Jones rotadas; parametros de Stokes
S0 = |Ex|^2+|Ey|^2, S1 = |Ex|^2-|Ey|^2, S2 = 2 Re(Ex Ey*), S3 = -2 Im(Ex Ey*) (convenio con exp(-i w t)); tambien se miden con seis intensidades de analizador
(H, V, +45, -45, circular derecha, circular izquierda). Luz parcialmente polarizada: mezcla incoherente de una fraccion p polarizada y 1-p natural (estados aleatorios).
Supuestos: elementos ideales, monocromatica; matrices de Jones solo describen luz totalmente polarizada (la mezcla se hace con Stokes). Validez: ilustrativa.
Tolerancia: Malus a 1e-12 ; Stokes frente a las seis medidas a 1e-12 ; grado de polarizacion muestral frente a la teoria a 0,02.
"""
from __future__ import annotations
import cmath, math, platform, random

def mat_vec(m, v):
    return (m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1])

def rot(t):
    c, s = math.cos(t), math.sin(t)
    return ((c, -s), (s, c))

def mat_mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def girado(m, t):
    return mat_mul(rot(t), mat_mul(m, rot(-t)))

POL = ((1, 0), (0, 0))
def retardo(gamma):
    return ((1, 0), (0, cmath.exp(1j * gamma)))

def inten(v):
    return abs(v[0]) ** 2 + abs(v[1]) ** 2

def stokes(v):
    ex, ey = v
    return (inten(v), abs(ex) ** 2 - abs(ey) ** 2, 2 * (ex * ey.conjugate()).real, -2 * (ex * ey.conjugate()).imag)

def analizador(v, base):
    # intensidad tras proyectar sobre el vector de base (ya normalizado)
    p = base[0].conjugate() * v[0] + base[1].conjugate() * v[1]
    return abs(p) ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    # Malus
    print(f"{'theta [grados]':>15} {'I/I0 numerico':>14} {'cos^2':>10}")
    peor = 0.0
    for deg in (0, 30, 45, 60, 90):
        t = math.radians(deg)
        v = mat_vec(girado(POL, t), (1 + 0j, 0j))
        i = inten(v)
        peor = max(peor, abs(i - math.cos(t) ** 2))
        print(f"{deg:15d} {i:14.6f} {math.cos(t) ** 2:10.6f}")
    assert peor < 1e-12
    # lamina de cuarto de onda a 45 grados sobre luz lineal horizontal: circular
    qwp = girado(retardo(math.pi / 2), math.pi / 4)
    v = mat_vec(qwp, (1 + 0j, 0j))
    s = stokes(v)
    print(f"QWP a 45 grados sobre horizontal: Stokes = ({s[0]:.4f}, {s[1]:.4f}, {s[2]:.4f}, {s[3]:+.4f}) -> circular")
    assert abs(abs(s[3]) - 1) < 1e-12 and abs(s[1]) < 1e-12 and abs(s[2]) < 1e-12
    # lamina de media onda a theta gira la polarizacion en 2 theta
    th = math.radians(20)
    v = mat_vec(girado(retardo(math.pi), th), (1 + 0j, 0j))
    s = stokes(v)
    ang = 0.5 * math.atan2(s[2], s[1])
    print(f"HWP a 20 grados sobre horizontal: azimut resultante = {math.degrees(ang):.4f} grados (esperado 2 x 20 = 40)")
    assert abs(math.degrees(ang) - 40) < 1e-9
    # Stokes por seis medidas frente a Jones
    r2 = 1 / math.sqrt(2)
    bases = {"H": (1, 0), "V": (0, 1), "P45": (r2, r2), "M45": (r2, -r2), "RC": (r2, 1j * r2), "LC": (r2, -1j * r2)}
    est = (0.8 * cmath.exp(0.3j), 0.5 * cmath.exp(-1.1j))
    est = (est[0], est[1])
    m = {k: analizador(est, tuple(complex(c) for c in b)) for k, b in bases.items()}
    s_med = (m["H"] + m["V"], m["H"] - m["V"], m["P45"] - m["M45"], m["RC"] - m["LC"])
    s_jones = stokes(est)
    print(f"Stokes por Jones = {tuple(round(x, 6) for x in s_jones)}")
    print(f"Stokes por 6 medidas = {tuple(round(x, 6) for x in s_med)}")
    dif = max(abs(a - b) for a, b in zip(s_med, s_jones))
    print(f"diferencia maxima = {dif:.2e}")
    assert dif < 1e-12   # "RC" y "LC" se rotulan segun el signo de S3 de este convenio, no segun una lateralidad astronomica o de la IEEE
    pur = math.sqrt(s_jones[1] ** 2 + s_jones[2] ** 2 + s_jones[3] ** 2) / s_jones[0]
    print(f"grado de polarizacion del estado puro = {pur:.12f}")
    assert abs(pur - 1) < 1e-12
    # luz parcialmente polarizada: p = 0,6 polarizada (el estado anterior) + natural
    p = 0.6
    n = 20000
    acum = [0.0, 0.0, 0.0, 0.0]
    for _ in range(n):
        if rnd.random() < p:
            vv = est
            w = 1.0 / inten(est)
        else:
            a = rnd.gauss(0, 1) + 1j * rnd.gauss(0, 1)
            b = rnd.gauss(0, 1) + 1j * rnd.gauss(0, 1)
            nrm = math.sqrt(inten((a, b)))
            vv = (a / nrm, b / nrm)
            w = 1.0
        sv = stokes(vv)
        # el estado natural se muestrea con polarizacion uniforme en la esfera de Poincare: media de S1,S2,S3 = 0
        for i in range(4):
            acum[i] += w * sv[i]
    s_m = [x / n for x in acum]
    dop = math.sqrt(s_m[1] ** 2 + s_m[2] ** 2 + s_m[3] ** 2) / s_m[0]
    print(f"mezcla p = {p}: Stokes muestral = {tuple(round(x, 4) for x in s_m)} ; DOP muestral = {dop:.4f} ; esperado = {p:.4f}")
    assert abs(dop - p) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
