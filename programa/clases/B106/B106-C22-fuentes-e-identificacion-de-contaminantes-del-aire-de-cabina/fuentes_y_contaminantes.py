#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C22: fuentes de contaminantes de una cabina cerrada y su identificacion por espectros SINTETICOS.

Consultado (OCHMO-TB-002): el resumen lista el monitoreo de trazas (V2 6023), de combustion (V2 6024) y de contaminacion (V2 6025), y el limite de contaminacion atmosferica (V2 6050); no da valores.
Todo lo numerico es SINTETICO o ILUSTRATIVO: dos materiales con emision exponencial E0 exp(-t/tau) (50 mg/h con tau = 100 h y 10 mg/h con tau = 2000 h), una fuente constante de equipos
de 1 mg/h, un volumen de 100 m3 con caudal de depuracion de 0.0095 m3/s; una biblioteca de 6 espectros de masas INVENTADOS (no son de ningun compuesto real; 24 canales m/z) y una mezcla de
tres de ellos con ruido (semilla 106). Identificacion por minimos cuadrados no negativos (descenso por coordenadas) y por similitud coseno.
Verificacion: la emision acumulada coincide con la integral analitica; el NNLS recupera los pesos verdaderos con error pequeno; los componentes ausentes quedan casi en cero.
"""
from __future__ import annotations
import math
import platform
import numpy as np

V, QE = 100.0, 0.0095


def emision(t, e0, tau):
    return e0 * math.exp(-t / tau)


def acumulada(t, e0, tau):
    return e0 * tau * (1 - math.exp(-t / tau))


def nnls(A, b, it=3000):
    x = np.zeros(A.shape[1])
    AtA, Atb = A.T @ A, A.T @ b
    for _ in range(it):
        for j in range(len(x)):
            r = Atb[j] - AtA[j] @ x + AtA[j, j] * x[j]
            x[j] = max(0.0, r / AtA[j, j])
    return x


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: emisiones y espectros SINTETICOS e inventados (semilla 106); no corresponden a ningun material ni compuesto real")
    R = {}
    mats = {"material A": (50.0, 100.0), "material B": (10.0, 2000.0)}
    print("Emision [mg/h] en el tiempo y concentracion estacionaria con depuracion Q = 0.0095 m3/s:")
    print("   fuente        t = 1 d   t = 30 d   t = 180 d   acumulada 30 d [g]")
    tot = {}
    for nom, (e0, tau) in mats.items():
        e = [emision(24.0 * d, e0, tau) for d in (1, 30, 180)]
        ac = acumulada(24.0 * 30, e0, tau) / 1000.0
        tot[nom] = (e, ac)
        print(f"   {nom:12s}  {e[0]:7.2f}   {e[1]:8.2f}   {e[2]:9.2f}   {ac:14.1f}")
    equipos = 1.0
    print(f"   equipos (cte)  {equipos:7.2f}   {equipos:8.2f}   {equipos:9.2f}   {equipos*720/1000:14.1f}")
    R["eA1"], R["eA30"], R["eB30"], R["acA"], R["acB"] = tot["material A"][0][0], tot["material A"][0][1], tot["material B"][0][1], tot["material A"][1], tot["material B"][1]
    assert abs(acumulada(720, 50, 100) - sum(emision(i + 0.5, 50, 100) for i in range(720)) * 1.0) / acumulada(720, 50, 100) < 1e-3
    c1 = (tot["material A"][0][0] + tot["material B"][0][0] + equipos) / 3600.0 / QE
    c30 = (tot["material A"][0][1] + tot["material B"][0][1] + equipos) / 3600.0 / QE
    R["c1"], R["c30"] = c1, c30
    print(f"Concentracion estacionaria total (mg/m3): dia 1 {c1:.3f}; dia 30 {c30:.3f}  -> la fuente dominante cambia de A a B")
    print(f"Dominante el dia 1: {'material A' if tot['material A'][0][0] > tot['material B'][0][0] else 'material B'}; el dia 30: {'material A' if tot['material A'][0][1] > tot['material B'][0][1] else 'material B'}")
    rng = np.random.default_rng(106)
    nm, nc = 24, 6
    L = np.abs(rng.normal(0, 1, (nm, nc))) ** 2
    L /= np.linalg.norm(L, axis=0)
    w_true = np.array([0.0, 3.0, 0.0, 1.2, 0.0, 0.6])
    y = L @ w_true + rng.normal(0, 0.02, nm)
    w = nnls(L, y)
    err = np.abs(w - w_true)
    R["w"], R["w_true"], R["err"] = w, w_true, err.max()
    print("Identificacion de una mezcla (biblioteca de 6 espectros inventados, 24 canales, ruido 0.02):")
    print("   compuesto   peso verdadero   peso NNLS   similitud coseno con la mezcla")
    cos = (L.T @ y) / (np.linalg.norm(L, axis=0) * np.linalg.norm(y))
    for j in range(nc):
        print(f"   {j+1:9d}   {w_true[j]:14.2f}   {w[j]:9.3f}   {cos[j]:28.3f}")
    print(f"Error maximo de los pesos: {err.max():.3f}")
    assert err.max() < 0.15 and w[0] < 0.1 and w[2] < 0.1 and w[4] < 0.1
    R["cos"] = cos
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
