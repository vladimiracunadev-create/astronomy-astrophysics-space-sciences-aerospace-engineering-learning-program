#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C20: validacion de una cadena de medida (telemetro por tiempo de vuelo).

Datos: SINTETICOS (semilla fija). Cadena: cronometro -> retardo electronico
t0 (desconocido, verdadero 30.0 ns) -> indice del aire n -> distancia
d = c (t - t0)/(2 n), con c exacta (299 792 458 m/s).
Pasos: (1) CALIBRACION en una base de referencia de 1000.000 m (u = 0.002 m)
con m = 200 lecturas: t0_hat = media(t) - 2 n D/c; (2) PRESUPUESTO con
u(t) = sigma_t/sqrt(m_med), u(t0_hat), u(n) = 3e-6 (GUM 5.1.2, independientes);
(3) VALIDACION frente a tres blancos de referencia independientes (500, 2000,
8000 m; u_ref = 0.003, 0.005, 0.010 m): se acepta si z = |d - d_ref| /
sqrt(u_c^2 + u_ref^2) <= 2 en todos.
Verdad simulada: n = 1.000300; en el caso DEFECTUOSO el n real es 1.000310
pero el modelo sigue usando 1.000300 (error de escala oculto de 1e-5).
Supuestos: ruido blanco gaussiano sigma_t = 0.5 ns; vacio salvo n; sin deriva.
Tolerancia: cadena sin ruido recupera la distancia a 1e-9 m; la tasa de
aceptacion simulada (3000 validaciones) esta entre 0.90 y 0.99 con la cadena
correcta (u(n) declarada excede el error real de n, que aqui es nulo, por lo que
la tasa supera el 0.86 = 0.95^3 de un presupuesto exacto) y por debajo de 0.35
con el defecto.
"""
from __future__ import annotations
import math
import platform
import random
import sys

C = 299_792_458.0
SIG_T = 0.5e-9
T0_V = 30.0e-9
N_V, N_MODELO, U_N = 1.000300, 1.000300, 3e-6
D_REF, U_DREF, M_CAL, M_MED = 1000.000, 0.002, 200, 100
BLANCOS = [(500.0, 0.003), (2000.0, 0.005), (8000.0, 0.010)]


def lectura(d, rng, n_real, ruido=True):
    t = 2 * n_real * d / C + T0_V
    return t + (rng.gauss(0, SIG_T) if ruido else 0.0)


def calibrar(rng, n_real, ruido=True):
    tm = sum(lectura(D_REF, rng, n_real, ruido) for _ in range(M_CAL)) / M_CAL
    t0 = tm - 2 * N_MODELO * D_REF / C
    u_t0 = math.hypot(SIG_T / math.sqrt(M_CAL), 2 * N_MODELO * U_DREF / C)
    return t0, u_t0


def medir(d_verd, rng, t0, u_t0, n_real, ruido=True):
    tm = sum(lectura(d_verd, rng, n_real, ruido) for _ in range(M_MED)) / M_MED
    d = C * (tm - t0) / (2 * N_MODELO)
    ut = SIG_T / math.sqrt(M_MED) * C / (2 * N_MODELO)
    ut0 = u_t0 * C / (2 * N_MODELO)
    un = d * U_N / N_MODELO
    uc = math.sqrt(ut ** 2 + ut0 ** 2 + un ** 2)
    return d, uc, (ut, ut0, un)


def validar(rng, n_real, ruido=True):
    t0, u_t0 = calibrar(rng, n_real, ruido)
    filas = []
    ok = True
    for d_ref, u_ref in BLANCOS:
        # el valor de referencia independiente tambien tiene su error
        ref = d_ref + (rng.gauss(0, u_ref) if ruido else 0.0)
        d, uc, parts = medir(d_ref, rng, t0, u_t0, n_real, ruido)
        z = abs(d - ref) / math.hypot(uc, u_ref)
        filas.append((d_ref, d - d_ref, uc, z, parts))
        ok &= z <= 2.0
    return ok, filas, t0, u_t0


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20)
    # 1) Cadena sin ruido: recuperacion exacta
    ok, filas, t0, _ = validar(rng, N_V, ruido=False)
    assert abs(t0 - T0_V) < 1e-18
    assert all(abs(f[1]) < 1e-9 for f in filas) and ok
    # 2) Una validacion con ruido (cadena correcta)
    ok, filas, t0, u_t0 = validar(random.Random(5), N_V)
    print(f"t0_hat = {t0*1e9:.3f} ns +/- {u_t0*1e9:.3f} ns (verdadero {T0_V*1e9:.1f} ns)")
    print("blanco(m)   d - d_ref (m)   u_c (m)    z    contribuciones (cronometro, t0, n) en m")
    for d_ref, dd, uc, z, p in filas:
        print(f"{d_ref:8.0f}   {dd:+10.4f}   {uc:8.4f}  {z:5.2f}   {p[0]:.4f}, {p[1]:.4f}, {p[2]:.4f}")
    print(f"validacion: {'ACEPTADA' if ok else 'RECHAZADA'}")
    # 3) Tasa de aceptacion, cadena correcta y defectuosa
    R = 3000
    ac_ok = sum(validar(rng, N_V)[0] for _ in range(R)) / R
    ac_mal = sum(validar(rng, 1.000310)[0] for _ in range(R)) / R
    print(f"tasa de aceptacion: cadena correcta = {ac_ok:.3f} (presupuesto conservador) ; con error de n de 1e-5 = {ac_mal:.3f}")
    assert 0.90 < ac_ok < 0.99 and ac_mal < 0.35
    # 4) Efecto del defecto en el blanco de 8000 m
    print(f"error esperado por n en 8000 m = {8000*1e-5:.3f} m")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
