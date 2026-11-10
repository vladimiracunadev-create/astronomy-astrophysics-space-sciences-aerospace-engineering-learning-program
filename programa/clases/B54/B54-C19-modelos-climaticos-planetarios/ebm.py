#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C19: modelo de balance de energia de dimension cero con retroalimentacion hielo-albedo.

Datos: S = 1361.0 W/m^2 y T superficial 288 K de la ficha NASA/NSSDC de la Tierra, sigma de NIST CODATA 2022 (consulta 2026-11-09).
La capacidad calorifica efectiva (C = 4.0e8 J m^-2 K^-1) y la rampa de albedo (0.62 por debajo de 250 K, 0.294 por encima de 280 K, lineal entre ambas) son
PARAMETROS SINTETICOS de la clase; la emisividad efectiva eps se CALIBRA para que T = 288 K sea un equilibrio con albedo 0.294 (valor de la ficha).
Modelo: C dT/dt = (S/4)(1 - alfa(T)) - eps sigma T^4. Supuestos: planeta homogeneo, sin transporte ni estacionalidad. Es un modelo de ENSENANZA, no una prediccion.
Tolerancias: sin retroalimentacion el equilibrio coincide con la solucion cerrada (1e-9 K); RK4 frente a la relajacion lineal exacta (1e-3 K); los equilibrios cambian de signo de dT/dt.
"""
import math, platform
SIG, S, C = 5.670374419e-8, 1361.0, 4.0e8
print(f"Python {platform.python_version()} (biblioteca estandar)")
eps = (S / 4) * (1 - 0.294) / (SIG * 288.0 ** 4)
print(f"eps calibrada = {eps:.4f}")
alfa = lambda T: 0.62 if T <= 250.0 else (0.294 if T >= 280.0 else 0.62 + (0.294 - 0.62) * (T - 250.0) / 30.0)
dTdt = lambda T, Sx=S, al=alfa: ((Sx / 4) * (1 - al(T)) - eps * SIG * T ** 4) / C
# prueba 1: albedo constante -> equilibrio cerrado
al0 = lambda T: 0.294
Teq = ((S / 4) * (1 - 0.294) / (eps * SIG)) ** 0.25
assert abs(Teq - 288.0) < 1e-9
# prueba 2: relajacion lineal alrededor del equilibrio: tau = C / (4 eps sigma T^3)
tau = C / (4 * eps * SIG * Teq ** 3)
print(f"Escala de tiempo de relajacion = {tau/3.156e7:.2f} anios")
T0, t_fin, dt = 290.0, 3 * tau, 3600.0 * 24
T, t = T0, 0.0
f = lambda T: dTdt(T, S, al0)
while t < t_fin:
    k1 = f(T); k2 = f(T + dt * k1 / 2); k3 = f(T + dt * k2 / 2); k4 = f(T + dt * k3)
    T += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += dt
ex = Teq + (T0 - Teq) * math.exp(-t / tau)
print(f"Relajacion a 3 tau desde 290 K: numerico = {T:.4f} K ; lineal exacto = {ex:.4f} K")
assert abs(T - ex) < 1e-3
# equilibrios con la rampa de albedo: busqueda de ceros de dT/dt
def ceros(Sx):
    out, prev = [], None
    for i in range(1800, 3501):
        T = i / 10
        v = dTdt(T, Sx)
        if prev is not None and prev[1] * v < 0:
            lo, hi = prev[0], T
            for _ in range(60):
                m = (lo + hi) / 2
                if dTdt(lo, Sx) * dTdt(m, Sx) <= 0: hi = m
                else: lo = m
            r = (lo + hi) / 2
            est = "estable" if (dTdt(r + 0.01, Sx) < 0 < dTdt(r - 0.01, Sx)) else "inestable"
            out.append((r, est))
        prev = (T, v)
    return out
print("S/S_0   equilibrios [K] (estabilidad)")
for fS in (0.80, 0.90, 0.95, 1.00, 1.05, 1.10):
    z = ceros(S * fS)
    print(f"{fS:5.2f}   " + ", ".join(f"{r:6.1f} ({e})" for r, e in z))
z1 = ceros(S)
assert any(abs(r - 288.0) < 0.5 and e == "estable" for r, e in z1)
z90 = ceros(0.8 * S)
assert len(z90) >= 1
# histeresis: barrido lento ascendente y descendente
def barrido(valores):
    T = 288.0 if valores[0] >= 1.0 else 230.0
    res = []
    for fS in valores:
        for _ in range(4000):
            T += 3600.0 * 24 * 10 * dTdt(T, S * fS)
        res.append((fS, T))
    return res
bajada = barrido([1.0 - 0.02 * i for i in range(0, 16)])
subida = barrido([0.70 + 0.02 * i for i in range(0, 16)])
print("S/S_0   T al bajar S [K]   T al subir S [K]")
for (fb, tb), (fs, ts) in zip(bajada, reversed(subida)):
    print(f"{fb:5.2f} {tb:16.1f} {ts:18.1f}")
print("Pruebas superadas.")
