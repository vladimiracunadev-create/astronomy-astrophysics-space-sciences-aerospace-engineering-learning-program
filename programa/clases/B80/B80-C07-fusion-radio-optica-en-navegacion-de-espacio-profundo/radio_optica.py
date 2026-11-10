#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C07: fusion radio-optica en navegacion de espacio profundo (geometria de informacion en el plano).

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80007); valores de sigma propuestos para el ejemplo, NO medidos ni tomados de una mision.
Sistema de referencia: plano de la geometria; eje u = linea de vision (LOS) Tierra-nave; eje w = perpendicular en el plano del cielo (POS).
Distancia a la nave: d = 1.0e8 km = 1.0e11 m (ilustrativa). Mediciones:
 - Radio (rango/Doppler integrado): informa sobre la componente LOS; sigma_u = 1.0 km (ilustrativa). Informacion en POS despreciable (se modela sigma_w_radio = 1.0e4 km).
 - Optica (imagen de la nave contra estrellas): angulo con sigma_theta = 1.0 microrad (ilustrativa); sigma_w_optico = d sigma_theta = 100 km;
   informacion en LOS despreciable (sigma_u_optico = 1.0e4 km).
Fusion en forma de informacion: Lambda = sum_i Lambda_i, con Lambda_i = R^T diag(1/sigma_u^2, 1/sigma_w^2) R; P = Lambda^-1. R rota el par (u, w) a ejes inerciales por el angulo phi.
Segunda via: minimos cuadrados ponderados por lotes con mediciones simuladas (2000 realizaciones) y comparacion de la covarianza empirica con P.
Tolerancia: cada sigma empirico dentro del 6 % del teorico; invariantes (traza de la informacion) exactos hasta 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, random

D = 1.0e8  # km
SU_R, SW_R = 1.0, 1.0e4
STH = 1.0e-6
SU_O, SW_O = 1.0e4, D * STH


def rotm(phi):
    c, s = math.cos(phi), math.sin(phi)
    return [[c, s], [-s, c]]   # fila 0 = eje u (LOS), fila 1 = eje w (POS) expresados en ejes inerciales


def info_ejes(su, sw, phi):
    R = rotm(phi)
    d = (1.0 / su ** 2, 1.0 / sw ** 2)
    return [[sum(R[k][i] * d[k] * R[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def inv2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def en_ejes_uw(P, phi):
    R = rotm(phi)
    # P_uw = R P R^T
    RP = [[sum(R[i][k] * P[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return [[sum(RP[i][k] * R[j][k] for k in range(2)) for j in range(2)] for i in range(2)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS: d = 1.0e8 km, sigma radio LOS 1 km, sigma optica angular 1 microrad -> 100 km en el plano del cielo (ilustrativos)")
    phi = math.radians(30.0)
    Ir = info_ejes(SU_R, SW_R, phi)
    Io = info_ejes(SU_O, SW_O, phi)
    If = [[Ir[i][j] + Io[i][j] for j in range(2)] for i in range(2)]
    Pf = inv2(If)
    Pu = en_ejes_uw(Pf, phi)
    su_f, sw_f = math.sqrt(Pu[0][0]), math.sqrt(Pu[1][1])
    Pr = en_ejes_uw(inv2(Ir), phi)
    Po = en_ejes_uw(inv2(Io), phi)
    print(" sensor      sigma LOS [km]   sigma POS [km]   correlacion LOS-POS")
    for nom, P in (("radio", Pr), ("optico", Po), ("fusion", Pu)):
        print(f"{nom:8s} {math.sqrt(P[0][0]):17.4f} {math.sqrt(P[1][1]):16.4f} {P[0][1] / math.sqrt(P[0][0] * P[1][1]):14.2e}")
    print(f"El plano del cielo (POS) mejora {math.sqrt(Pr[1][1]) / sw_f:.0f} veces frente a solo radio y el LOS {math.sqrt(Po[0][0]) / su_f:.0f} veces frente a solo optica")
    # Invariancia: la traza de la informacion no depende de phi
    t1 = sum(info_ejes(SU_R, SW_R, 0.3)[i][i] for i in range(2))
    t2 = sum(info_ejes(SU_R, SW_R, 1.1)[i][i] for i in range(2))
    print(f"Traza de la informacion radio para phi = 0.3 y 1.1 rad: {t1:.9e} y {t2:.9e}")
    # Monte Carlo por lotes: mediciones en (u, w)
    rnd = random.Random(80007)
    R = rotm(phi)
    verd = (123.0, -456.0)  # km, posicion verdadera en ejes inerciales (SINTETICA)
    n = 2000
    ex, ey = [], []
    for _ in range(n):
        # mediciones: proyecciones sobre u y w con ruido; radio mide u, optica mide w (y cada una tiene una componente debil en el otro eje)
        zr = [sum(R[k][j] * verd[j] for j in range(2)) + rnd.gauss(0, (SU_R, SW_R)[k]) for k in range(2)]
        zo = [sum(R[k][j] * verd[j] for j in range(2)) + rnd.gauss(0, (SU_O, SW_O)[k]) for k in range(2)]
        # estimacion por lotes: Lambda x = sum R^T W z
        b = [0.0, 0.0]
        for z, su, sw in ((zr, SU_R, SW_R), (zo, SU_O, SW_O)):
            w = (1.0 / su ** 2, 1.0 / sw ** 2)
            for i in range(2):
                b[i] += sum(R[k][i] * w[k] * z[k] for k in range(2))
        x = [Pf[0][0] * b[0] + Pf[0][1] * b[1], Pf[1][0] * b[0] + Pf[1][1] * b[1]]
        e = [x[0] - verd[0], x[1] - verd[1]]
        eu = R[0][0] * e[0] + R[0][1] * e[1]
        ew = R[1][0] * e[0] + R[1][1] * e[1]
        ex.append(eu); ey.append(ew)
    mu = math.sqrt(sum(v * v for v in ex) / n)
    mw = math.sqrt(sum(v * v for v in ey) / n)
    print(f"Monte Carlo ({n} realizaciones): sigma LOS = {mu:.4f} km (teorico {su_f:.4f}) ; sigma POS = {mw:.3f} km (teorico {sw_f:.3f})")
    assert abs(mu / su_f - 1.0) < 0.06 and abs(mw / sw_f - 1.0) < 0.06
    assert abs(t1 - t2) / t1 < 1e-9
    assert sw_f < 0.02 * math.sqrt(Pr[1][1]) and su_f <= math.sqrt(Pr[0][0])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
