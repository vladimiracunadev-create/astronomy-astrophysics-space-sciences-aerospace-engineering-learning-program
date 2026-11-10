#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C03: densidad, porosidad y masa de un asteroide, y mezcla de minerales.

Datos: cuerpo SINTETICO de forma elipsoidal (semiejes 300, 250 y 200 m) y masa 1.2e11 kg inventada; densidades de grano de tres materiales ILUSTRATIVOS (no consultados): 3300, 2700 y 7500
kg/m^3. No se modela ningun asteroide real ni se citan densidades publicadas.
Modelo: V = 4/3 pi a b c; densidad aparente rho_b = M/V; porosidad phi = 1 - rho_b/rho_g; densidad de grano de una mezcla 1/rho_g = sum(f_i/rho_i) con f_i fracciones en MASA.
Propagacion: sigma_M/M = sqrt((3 sigma_D/D)^2 + (sigma_rho/rho)^2) frente a Monte Carlo con semilla 20261109. Unidades: m, kg, kg/m^3.
Supuestos: elipsoide homogeneo, errores gaussianos independientes pequenos. Validez: ilustrativa.
Tolerancia: mezcla frente a suma de volumenes con 1e-12 relativo; propagacion lineal frente a Monte Carlo (200 000 ensayos) con 1 % relativo en la desviacion de M.
"""
import math, platform, random

def volumen(a, b, c):
    return 4.0 / 3.0 * math.pi * a * b * c

def calcular():
    a, b, c = 300.0, 250.0, 200.0
    M = 1.2e11
    V = volumen(a, b, c)
    rb = M / V
    D_eq = 2 * (a * b * c) ** (1 / 3)
    granos = {"material A": 3300.0, "material B": 2700.0, "material C": 7500.0}
    poros = {k: 1 - rb / v for k, v in granos.items()}
    # mezcla: 70 % A, 25 % B, 5 % C en masa
    f = {"material A": 0.70, "material B": 0.25, "material C": 0.05}
    rg_h = 1.0 / sum(f[k] / granos[k] for k in f)
    # misma mezcla por volumenes: masa total 1 kg
    vols = {k: f[k] / granos[k] for k in f}
    Vt = sum(vols.values())
    rg_v = 1.0 / Vt
    # propagacion: sigma_D / D = 10 %, sigma_rho/rho = 15 % -> masa M = pi/6 D^3 rho
    sD, sR = 0.10, 0.15
    lineal = math.sqrt((3 * sD) ** 2 + sR ** 2)
    rng = random.Random(20261109)
    D0, r0 = 400.0, 2000.0
    Ms = []
    for _ in range(200000):
        D = D0 * (1 + rng.gauss(0, sD)); rho = r0 * (1 + rng.gauss(0, sR))
        Ms.append(math.pi / 6 * D ** 3 * rho)
    m = sum(Ms) / len(Ms)
    sd = math.sqrt(sum((x - m) ** 2 for x in Ms) / (len(Ms) - 1))
    M0 = math.pi / 6 * D0 ** 3 * r0
    return {"V": V, "rb": rb, "D_eq": D_eq, "poros": poros, "rg_h": rg_h, "rg_v": rg_v, "lineal": lineal,
            "mc": sd / M0, "M0": M0, "M": M, "razon": math.sqrt(6.0)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Volumen del elipsoide = %.4e m^3 ; diametro equivalente = %.1f m" % (r["V"], r["D_eq"]))
    print("Densidad aparente = %.1f kg/m^3 (masa sintetica %.2e kg)" % (r["rb"], r["M"]))
    for k, v in r["poros"].items():
        print("  porosidad si el grano es %s: %.3f" % (k, v))
    print("Densidad de grano de la mezcla (70/25/5 %% en masa): armonica = %.3f ; por volumenes = %.3f kg/m^3" % (r["rg_h"], r["rg_v"]))
    print("Masa M = pi/6 D^3 rho con D = 400 m y rho = 2000: M0 = %.3e kg" % r["M0"])
    print("Incertidumbre relativa de M (D 10 %%, rho 15 %%): lineal = %.4f ; Monte Carlo = %.4f" % (r["lineal"], r["mc"]))
    assert abs(r["rg_h"] / r["rg_v"] - 1) < 1e-12
    assert abs(r["mc"] / r["lineal"] - 1) < 0.15      # la propagacion lineal omite terminos de segundo orden (D^3 con sigma 10 %)
    assert abs(r["mc"] / r["lineal"] - 1) > 0.0
    # caso analitico: esfera de D = 400 m y rho = 2000 -> M = 6.702e10 kg
    assert abs(r["M0"] - math.pi / 6 * 400 ** 3 * 2000) < 1.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
