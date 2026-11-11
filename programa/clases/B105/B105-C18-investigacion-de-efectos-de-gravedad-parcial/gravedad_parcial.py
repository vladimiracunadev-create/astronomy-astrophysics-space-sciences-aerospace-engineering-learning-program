#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C18: gravedad parcial: peso, marcha, salto y presion hidrostatica (calculo con parametros de ENSENANZA).

Gravedades de superficie de referencia (valores usuales, NO consultados aqui): Tierra 9.81, Marte 3.71, Luna 1.62 m/s2. Masa 75 kg; longitud de pierna 0.90 m.
Transicion marcha-carrera por numero de Froude: v = sqrt(Fr g L) con Fr = 0.5 (valor empirico de ensenanza; el umbral real varia con la persona).
Salto vertical con la misma velocidad de despegue v0 = 2.5 m/s: h = v0^2/(2 g). Caida desde 1 m: t = sqrt(2 h/g), v = sqrt(2 g h). Presion hidrostatica de la
sangre a 0.35 m sobre el corazon (rho 1060 kg/m3, como en B105-C01). Lo que NO se sabe: la dosis minima de gravedad que protege hueso o musculo; esta clase NO
la calcula. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

G = {"Tierra": 9.81, "Marte": 3.71, "Luna": 1.62}
M, LP, FR, V0 = 75.0, 0.90, 0.5, 2.5


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: gravedades usuales no consultadas; parametros de enseñanza (m = 75 kg, L = 0.90 m, Fr = 0.5); no hay mediciones")
    print("cuerpo   g [m/s2]  g/g_T   peso [N]  v marcha-carrera [m/s] [km/h]  salto h [m]  caida 1 m: t [s], v [m/s]  P cabeza [mmHg]")
    res = {}
    for nombre, g in G.items():
        peso = M * g
        vt = np.sqrt(FR * g * LP)
        h = V0 ** 2 / (2 * g)
        t_c = np.sqrt(2 * 1.0 / g)
        v_c = np.sqrt(2 * g * 1.0)
        p = 1060 * g * 0.35 / 133.322
        res[nombre] = (peso, vt, h, t_c)
        print(f"{nombre:7s}  {g:6.2f}   {g / 9.81:5.3f}   {peso:7.1f}   {vt:6.2f}  {3.6 * vt:6.2f}               {h:6.2f}         {t_c:5.3f}, {v_c:5.2f}              {p:5.1f}")
    print(f"Cociente de pesos: Marte/Tierra = {res['Marte'][0] / res['Tierra'][0]:.3f}; Luna/Tierra = {res['Luna'][0] / res['Tierra'][0]:.3f}")
    print(f"Cociente de velocidades de transicion: Marte/Tierra = {res['Marte'][1] / res['Tierra'][1]:.3f} (= raiz de g/g_T = {np.sqrt(3.71 / 9.81):.3f}); Luna/Tierra = {res['Luna'][1] / res['Tierra'][1]:.3f}")
    # tiempo de vuelo de un paso y fraccion de ciclo en aire a velocidad dada
    print("Longitud de zancada de salto, v = 2.5 m/s, angulo 45 grados (alcance = v^2 sen(2 theta)/g):")
    for nombre, g in G.items():
        print(f"  {nombre:7s} alcance = {V0 ** 2 / g:5.2f} m; tiempo de vuelo = {2 * V0 * np.sin(np.radians(45)) / g:5.2f} s")
    # la energia potencial para subir 1 m
    print("Energia para elevar el centro de masa 0.30 m: " + ", ".join(f"{n} {M * g * 0.30:6.1f} J" for n, g in G.items()))
    assert abs(res["Marte"][0] - 278.25) < 0.01
    assert abs(res["Marte"][1] / res["Tierra"][1] - np.sqrt(3.71 / 9.81)) < 1e-12
    assert abs(res["Luna"][2] - 1.9290) < 0.001 or abs(res["Luna"][2] - 1.93) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
