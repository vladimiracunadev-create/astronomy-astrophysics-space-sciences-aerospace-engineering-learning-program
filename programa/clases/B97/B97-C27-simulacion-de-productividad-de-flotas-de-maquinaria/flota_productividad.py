#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C27: productividad de una flota de camiones robot con una excavadora compartida (simulacion de eventos discretos frente al modelo analitico).

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): una excavadora que carga un camion a la vez (tiempo medio de carga 120 s, exponencial), camiones que acarrean, descargan y
regresan (tiempo medio de ida y vuelta 600 s: exponencial en el modelo analitico y tambien en la simulacion de comparacion; deterministico en una segunda simulacion), carga util 300 kg,
de 1 a 10 camiones, 60 000 cargas simuladas por caso, semilla fija. Ninguna cifra describe una flota real.
Modelo analitico (poblacion finita, un servidor, exponenciales; 'problema del reparador de maquinas'): P_k proporcional a n!/(n-k)! (S/Z)^k, productividad X = (1 - P_0)/S, utilizacion de la excavadora U = 1 - P_0.
Cota de saturacion: X <= min(n/(S + Z), 1/S); numero de camiones en el codo n* = 1 + Z/S.
Segunda via: simulacion de eventos discretos con ida y vuelta exponencial (tolerancia 3 % en X frente al modelo analitico) y con ida y vuelta deterministica (comparacion, sin tolerancia).
Unidades: segundos, kg y toneladas por hora. Sin averias, sin colas de descarga y sin variaciones del terreno.
"""
from __future__ import annotations
import heapq, math, platform, random

S, Z, CARGA, NCARGAS, SEMILLA = 120.0, 600.0, 300.0, 60000, 20261110                # SINTETICOS


def analitico(n):
    pesos = [math.factorial(n) / math.factorial(n - k) * (S / Z) ** k for k in range(n + 1)]
    p0 = 1.0 / sum(pesos)
    u = 1 - p0
    x = u / S
    l_cola = sum((k - 1) * pesos[k] * p0 for k in range(1, n + 1))        # camiones esperando (sin contar el que se carga)
    return dict(u=u, x=x, cola=l_cola, espera=l_cola / x if x > 0 else 0.0)


def simular(n, det, rng):
    """Eventos: ('fin_carga', t) y ('regreso', t, camion). Devuelve (cargas por segundo, utilizacion)."""
    ev = []
    for i in range(n):
        heapq.heappush(ev, (Z if det else rng.expovariate(1 / Z), i))
    cola, libre, t, cargas, ocupado, t_ocup = [], True, 0.0, 0, 0.0, 0.0
    fin_carga = None
    while cargas < NCARGAS:
        # siguiente evento: regreso de un camion o fin de carga
        if ev and (fin_carga is None or ev[0][0] <= fin_carga[0]):
            tt, i = heapq.heappop(ev)
            if not libre:
                pass
            t = tt
            if libre:
                libre = False
                dur = rng.expovariate(1 / S)
                fin_carga = (t + dur, i)
                ocupado += dur
            else:
                cola.append(i)
        else:
            t, i = fin_carga
            cargas += 1
            heapq.heappush(ev, (t + (Z if det else rng.expovariate(1 / Z)), i))
            if cola:
                j = cola.pop(0)
                dur = rng.expovariate(1 / S)
                fin_carga = (t + dur, j)
                ocupado += dur
            else:
                libre = True
                fin_carga = None
    return cargas / t, min(1.0, ocupado / t)


def calc():
    rng = random.Random(SEMILLA)
    filas, maxdif = [], 0.0
    for n in range(1, 11):
        a = analitico(n)
        xe, ue = simular(n, False, rng)
        xd, ud = simular(n, True, rng)
        dif = abs(xe - a["x"]) / a["x"]
        maxdif = max(maxdif, dif)
        filas.append((n, a["x"] * 3600, a["u"], xe * 3600, dif, xd * 3600, ud, a["espera"]))
    t_h = lambda x: x * CARGA / 1000.0       # t/h a partir de cargas/h
    n_codo = 1 + Z / S
    mejor = max(filas, key=lambda f: f[1])
    return dict(filas=filas, maxdif=maxdif, n_codo=n_codo, x_max=3600 / S, t_max=t_h(3600 / S), t6=t_h(filas[5][1]), t3=t_h(filas[2][1]), t10=t_h(filas[9][1]),
                u3=filas[2][2], u6=filas[5][2], u10=filas[9][2], esp3=filas[2][7], esp10=filas[9][7], det6=t_h(filas[5][5]), ana6=t_h(filas[5][1]), carga=CARGA,
                x1=filas[0][1], x3=filas[2][1], x6=filas[5][1], x10=filas[9][1], gan_3_6=filas[5][1] / filas[2][1], gan_6_10=filas[9][1] / filas[5][1])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Flota SINTETICA: carga media S = {S:.0f} s; ida y vuelta Z = {Z:.0f} s; carga util {CARGA:.0f} kg; {NCARGAS} cargas por caso; semilla {SEMILLA}")
    print(" n   X analitica [cargas/h]  U excav.  X simulada (exp.)  dif. [%]   X simulada (det.)  U (det.)  espera analitica [s]")
    for n, xa, u, xe, dif, xd, ud, esp in r["filas"]:
        print(f"{n:2d} {xa:20.2f} {u:9.3f} {xe:16.2f} {100*dif:9.2f} {xd:17.2f} {ud:9.3f} {esp:20.1f}")
    print(f"Codo n* = 1 + Z/S = {r['n_codo']:.1f}; cota de la excavadora 1/S = {r['x_max']:.1f} cargas/h = {r['t_max']:.2f} t/h")
    print(f"Productividad con 3 / 6 / 10 camiones = {r['t3']:.2f} / {r['t6']:.2f} / {r['t10']:.2f} t/h; la ganancia de 6 a 10 camiones es x{r['gan_6_10']:.3f}")
    print(f"Diferencia maxima de X entre simulacion exponencial y modelo analitico = {100*r['maxdif']:.2f} %")
    assert r["maxdif"] < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
