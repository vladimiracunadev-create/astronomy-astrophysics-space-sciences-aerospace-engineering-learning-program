#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B60-C04: balance gas-superficie-manto de una especie (modelo de juguete de tres fases).

Datos: constantes CODATA 2022 consultadas en NIST el 2026-11-09 (k_B, u). Todo lo demas es ILUSTRATIVO y SINTETICO:
n_H = 1e5 cm^-3, n_d/n_H = 1e-12, radio del grano 0.1 um, 1.26e5 sitios por grano (1e15 sitios/cm^2), abundancia de la
especie X de 1e-5 respecto a H, masa de 28 u, energia de desorcion de 1150 K, frecuencia de vibracion de 1e12 s^-1 y
tasa de intercambio mantel->superficie de 3e-13 s^-1. No es CO ni ninguna especie real, ni una nube real, y NO
reproduce los resultados publicados del modelo de Ruaud et al. (2016) (articulo consultado solo en su resumen).
Modelo: tres reservorios en cm^-3 de gas: g (gas), s (superficie, capacidad ML = una monocapa), m (manto).
 acrecion F_acc = n_d pi a^2 v_th g, v_th = sqrt(8 k T / (pi m))   [cm^-3 s^-1] (pegado S = 1)
 desorcion termica F_des = nu exp(-E_D/T) s                         (solo la superficie)
 enterramiento F_ent = F_acc (s/ML)^4  (la capa superficial llena se convierte en manto)
 intercambio ascendente F_up = k_sw m max(0, 1 - s/ML)             (el manto solo reaparece si la superficie esta libre)
 Modelo de dos fases: sin manto (m = 0): todo el hielo es superficie y se desorbe por completo.
Integracion: Euler implicito con Newton (Jacobiano por diferencias finitas) y doble paso con Richardson; rtol 1e-4, atol 1e-10.
Supuestos: especie unica sin reacciones; temperatura de gas y de grano iguales; sin fotodesorcion ni rayos cosmicos.
Tolerancias: conservacion g + s + m = total con error relativo < 1e-9.
"""
from __future__ import annotations
import math, platform

KB = 1.380649e-23        # J/K (exacto, CODATA 2022)
U = 1.66053906892e-27    # kg (CODATA 2022)
YR = 3.15576e7           # s (ano juliano)
NH, ND_REL = 1.0e5, 1.0e-12
A_GR, SITIOS = 1.0e-5, 1.26e5       # cm, sitios/grano
X_REL, MASA = 1.0e-5, 28.0 * U
E_D, NU, K_SW = 1150.0, 1.0e12, 3.0e-13
ND = NH * ND_REL
ML = ND * SITIOS
TOTAL = NH * X_REL


def derivadas(T, y, tres):
    g, s, m = y
    vth = math.sqrt(8 * KB * T / (math.pi * MASA)) * 100.0     # cm/s
    f_acc = ND * math.pi * A_GR ** 2 * vth * g
    f_des = NU * math.exp(-E_D / T) * s
    if tres:
        f_ent = f_acc * min(1.0, max(s, 0.0) / ML) ** 4
        f_up = K_SW * m * max(0.0, 1.0 - s / ML)
    else:
        f_ent = f_up = 0.0
    return [-f_acc + f_des, f_acc - f_des - f_ent + f_up, f_ent - f_up]


def resolver(A, b):
    n = len(b)
    M = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            fac = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= fac * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][c] * x[c] for c in range(i + 1, n))) / M[i][i]
    return x


def paso_implicito(y, h, T, tres):
    z = y[:]
    for _ in range(60):
        f0 = derivadas(T, z, tres)
        F = [z[i] - y[i] - h * f0[i] for i in range(3)]
        J = [[0.0] * 3 for _ in range(3)]
        for j in range(3):
            d = 1e-7 * max(abs(z[j]), 1e-6 * TOTAL)
            zz = z[:]
            zz[j] += d
            fj = derivadas(T, zz, tres)
            for i in range(3):
                J[i][j] = (fj[i] - f0[i]) / d
        A = [[(1.0 if i == j else 0.0) - h * J[i][j] for j in range(3)] for i in range(3)]
        dz = resolver(A, [-v for v in F])
        z = [z[i] + dz[i] for i in range(3)]
        if max(abs(v) for v in dz) < 1e-11 * TOTAL + 1e-9 * max(abs(v) for v in z):
            return z
    raise RuntimeError("Newton no convergio")


def integrar(y0, t0, t1, Tfun, tres, rtol=1e-4, atol=1e-10):
    t, y, h, pasos = t0, y0[:], (t1 - t0) * 1e-6, 0
    while t < t1 * (1 - 1e-12):
        h = min(h, t1 - t)
        T = Tfun(t + h / 2)
        completo = paso_implicito(y, h, T, tres)
        medio = paso_implicito(paso_implicito(y, h / 2, T, tres), h / 2, T, tres)
        err = max(abs(medio[i] - completo[i]) / (atol + rtol * abs(medio[i])) for i in range(3))
        if err <= 1.0:
            y = [2 * medio[i] - completo[i] for i in range(3)]
            t += h
            pasos += 1
        h *= min(3.0, max(0.2, 0.9 / math.sqrt(max(err, 1e-10))))
    return y, pasos


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Parametros ILUSTRATIVOS y SINTETICOS (ver la cabecera); unidades: cm^-3, s, K")
    vth = math.sqrt(8 * KB * 10.0 / (math.pi * MASA)) * 100.0
    k_acc = ND * math.pi * A_GR ** 2 * vth
    print(f"n_d = {ND:.2e} cm^-3 ; monocapa ML = {ML:.3e} cm^-3 ; X total = {TOTAL:.2f} cm^-3 = {TOTAL / ML:.0f} ML")
    print(f"k_acc(10 K) = {k_acc:.3e} s^-1 (t_acc = {1 / k_acc / YR:.3e} anos) ; k_des(10 K) = {NU * math.exp(-E_D / 10.0):.2e} s^-1 ; k_des(20 K) = {NU * math.exp(-E_D / 20.0):.2e} s^-1")
    T10 = lambda t: 10.0
    estados = {}
    for etiqueta, tres in (("2 fases", False), ("3 fases", True)):
        y, t_prev = [TOTAL, 0.0, 0.0], 0.0
        print(f"\nAcrecion isoterma a 10 K, {etiqueta}:")
        print("  t [anos]     gas/total   superficie [ML]   manto/total")
        for t_ano in (1e3, 1e4, 1e5, 3e5, 1e6):
            y, _ = integrar(y, t_prev, t_ano * YR, T10, tres)
            t_prev = t_ano * YR
            print(f"  {t_ano:8.0e}   {y[0] / TOTAL:9.4f}   {y[1] / ML:15.2f}   {y[2] / TOTAL:10.4f}")
        estados[tres] = y
        assert abs(sum(y) - TOTAL) < 1e-9 * TOTAL
    t_w = 1.0e5 * YR
    rampa = lambda t: 10.0 + 40.0 * min(max(t / t_w, 0.0), 1.0)    # 10 -> 50 K lineal en 1e5 anos
    print("\nCalentamiento lineal 10 -> 50 K en 1e5 anos desde el estado a 1e6 anos (fraccion de X en hielo = (s + m)/total):")
    print("  T [K]   hielo 2 fases   hielo 3 fases   manto 3 fases/total")
    objetivos = (15.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0)
    ys = {tres: estados[tres][:] for tres in (False, True)}
    tp = 0.0
    maximo = 0.0
    for T in objetivos:
        t_obj = (T - 10.0) / 40.0 * t_w
        fila = []
        for tres in (False, True):
            ys[tres], _ = integrar(ys[tres], tp, t_obj, rampa, tres)
            maximo = max(maximo, abs(sum(ys[tres]) - TOTAL) / TOTAL)
            fila.append(ys[tres])
        tp = t_obj
        print(f"  {T:5.0f}   {(fila[0][1] + fila[0][2]) / TOTAL:13.4f}   {(fila[1][1] + fila[1][2]) / TOTAL:13.4f}   {fila[1][2] / TOTAL:17.4f}")
    print(f"\nMaximo error relativo de conservacion de la masa = {maximo:.1e}")
    assert maximo < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
