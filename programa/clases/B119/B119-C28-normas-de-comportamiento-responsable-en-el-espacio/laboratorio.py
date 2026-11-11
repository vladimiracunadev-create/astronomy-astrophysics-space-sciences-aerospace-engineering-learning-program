#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C28: conducta responsable: maniobras de proximidad y distancias relativas en orbita con las ecuaciones de Clohessy-Wiltshire (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no es una guia de operaciones de proximidad.
Texto consultado (2026-11-11, nota de legal.un.org): art. IX del Tratado del Espacio Ultraterrestre: consideracion de los intereses de los demas Estados y consultas internacionales previas cuando una actividad
pueda causar interferencia perjudicial a otras actividades. NO consultado: resoluciones de la Asamblea General sobre normas de comportamiento responsable ni ninguna practica de operaciones de proximidad;
la distancia de exclusion de 200 m es ILUSTRATIVA.
Ecuaciones (no consultadas en una fuente concreta; verificadas contra integracion RK4 de las ecuaciones diferenciales): sistema LVLH, x radial, y a lo largo de la traza, orbita circular de radio a, n = sqrt(GM / a^3):
x'' = 3 n^2 x + 2 n y' ; y'' = -2 n x'. Solucion cerrada estandar. Condicion de ausencia de deriva: y'(0) = -2 n x(0).
Datos SINTETICOS: a = 6778.137 km (400 km de altura), GM = 398600.4418 km^3/s^2. Posicion inicial del satelite vecino: x0 = 0.5 km, y0 = 1.5 km (movimiento plano).
Tolerancia: cerrada vs RK4 < 1e-6 km tras 3 orbitas.
"""
import json, math, platform

GM, A = 398600.4418, 6778.137
n = math.sqrt(GM / A ** 3)
P = 2 * math.pi / n
def cw(t, x0, y0, vx0, vy0):
    s, c = math.sin(n * t), math.cos(n * t)
    x = (4 - 3 * c) * x0 + s / n * vx0 + 2 / n * (1 - c) * vy0
    y = 6 * (s - n * t) * x0 + y0 + 2 / n * (c - 1) * vx0 + (4 * s - 3 * n * t) / n * vy0
    return x, y
def rk4(t_fin, x0, y0, vx0, vy0, dt=1.0):
    def f(s):
        x, y, vx, vy = s
        return (vx, vy, 3 * n * n * x + 2 * n * vy, -2 * n * vx)
    s = (x0, y0, vx0, vy0); t = 0.0
    while t < t_fin - 1e-9:
        h = min(dt, t_fin - t)
        k1 = f(s)
        k2 = f(tuple(a + h / 2 * b for a, b in zip(s, k1)))
        k3 = f(tuple(a + h / 2 * b for a, b in zip(s, k2)))
        k4 = f(tuple(a + h * b for a, b in zip(s, k3)))
        s = tuple(a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4))
        t += h
    return s
x0, y0 = 0.5, 1.5
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Escenario SINTETICO; art. IX consultado (2026-11-11); normas de conducta responsable y practica de proximidad NO consultadas; distancia de exclusion 200 m ILUSTRATIVA.")
print(f"n = {n:.6e} rad/s ; periodo = {P / 60:.2f} min")
casos = {"sin deriva (y'0 = -2 n x0)": (0.0, -2 * n * x0), "con velocidad relativa nula": (0.0, 0.0)}
resumen = {}
for nombre, (vx0, vy0) in casos.items():
    t_fin = 3 * P
    xa, ya = cw(t_fin, x0, y0, vx0, vy0)
    xn, yn, _, _ = rk4(t_fin, x0, y0, vx0, vy0)
    err = math.hypot(xa - xn, ya - yn)
    assert err < 1e-6, (nombre, err)
    dmin = min(math.hypot(*cw(k * P / 600, x0, y0, vx0, vy0)) for k in range(0, 1801))
    dfin = math.hypot(xa, ya)
    resumen[nombre] = (dmin, dfin, err)
    print(f"{nombre:30s}: distancia minima en 3 orbitas {1000 * dmin:8.1f} m ; al final {1000 * dfin:9.1f} m ; |cerrada - RK4| = {err:.1e} km")
dmin0 = resumen["sin deriva (y'0 = -2 n x0)"][0] * 1000
dmin1 = resumen["con velocidad relativa nula"][0] * 1000
# acotado no significa seguro: con y0 = 1.0 km la misma geometria sin deriva pasa por el origen
dcol = min(math.hypot(*cw(k * P / 600, x0, 1.0, 0.0, -2 * n * x0)) for k in range(0, 1801)) * 1000
print(f"Misma geometria sin deriva pero con y0 = 1.0 km: distancia minima {dcol:.1f} m (trayectoria acotada que pasa por el origen)")
assert dcol < 1.0
print(f"Cruza la zona de exclusion de 200 m: sin deriva {'si' if dmin0 < 200 else 'no'} ; con velocidad nula {'si' if dmin1 < 200 else 'no'}")
dfin1 = resumen["con velocidad relativa nula"][1]
print(f"Deriva a lo largo de la traza por orbita con x0 = {x0} km y velocidad nula: {abs(-12 * math.pi * x0):.3f} km (formula -12 pi x0)")
assert abs(abs(cw(P, x0, y0, 0.0, 0.0)[1] - y0) - 12 * math.pi * x0) < 1e-6
print("CLAVES " + json.dumps({"n": "%.4e" % n, "P": "%.2f" % (P / 60), "d0": "%.1f" % dmin0, "d1": "%.1f" % dmin1, "df1": "%.1f" % (1000 * dfin1), "der": "%.3f" % (12 * math.pi * x0), "dcol": "%.1f" % dcol}))
print("Pruebas superadas.")
