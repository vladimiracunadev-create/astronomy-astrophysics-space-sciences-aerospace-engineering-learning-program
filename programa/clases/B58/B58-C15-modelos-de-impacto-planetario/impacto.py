#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C15: energia de impacto y escalamiento del crater transitorio.

Datos: escenario SINTETICO: impactor de 470 m (tamano mediano del escenario ficticio del ejercicio PDC 2023 de CNEOS, consultado el 2026-11-09), densidad 2600 kg/m^3, velocidad 20 km/s, angulo 45 deg
(densidad, velocidad y angulo ILUSTRATIVOS); blanco de 2500 kg/m^3 y g = 9.81 m/s^2. La relacion D_tc = 1.161 (rho_i/rho_t)^(1/3) L^0.78 v^0.44 g^(-0.22) sin^(1/3)(theta) (SI) y el factor 1.25 al crater
simple final son del autor, recordados de la literatura (Collins y otros, 2005) y NO consultados (el resumen de ADS no abrio, 405); se tratan como modelo de escalamiento por verificar. 1 Mt = 4.184e15 J.
Modelo: E = (1/2) m v^2 con m = rho pi L^3 / 6; D_tc por la ley de potencias; D_final = 1.25 D_tc (simple). Unidades SI, resultados en km y Mt.
Supuestos: impacto en roca competente, sin atmosfera ni fragmentacion previa, cuerpo esferico. Validez: cualitativa; solo el escalamiento, no los coeficientes, se verifica aqui.
Tolerancia: E por dos vias (1/2 m v^2 y p^2/2m) con 1e-12; exponentes de L, v, g y sin(theta) por diferencias centrales con 1e-6; cociente 2^0.78 al duplicar L con 1e-12.
"""
import math, platform

MT = 4.184e15

def masa(L, rho):
    return rho * math.pi * L ** 3 / 6.0

def energia(L, rho, v):
    return 0.5 * masa(L, rho) * v * v

def Dtc(L, rho_i, v, theta_deg, rho_t=2500.0, g=9.81):
    return 1.161 * (rho_i / rho_t) ** (1 / 3) * L ** 0.78 * v ** 0.44 * g ** -0.22 * math.sin(math.radians(theta_deg)) ** (1 / 3)

def exponente(f, x0, h=1e-6):
    return (math.log(f(x0 * (1 + h))) - math.log(f(x0 * (1 - h)))) / (math.log(1 + h) - math.log(1 - h))

def calcular():
    L, rho, v, th = 470.0, 2600.0, 20e3, 45.0
    E = energia(L, rho, v)
    p = masa(L, rho) * v
    E2 = p * p / (2 * masa(L, rho))
    D = Dtc(L, rho, v, th)
    ex = {"L": exponente(lambda x: Dtc(x, rho, v, th), L), "v": exponente(lambda x: Dtc(L, rho, x, th), v),
          "g": exponente(lambda x: Dtc(L, rho, v, th, g=x), 9.81)}
    # exponente del seno: d ln D / d ln sin(theta) = 1/3
    ex["sin"] = (math.log(Dtc(L, rho, v, th + 1e-4)) - math.log(Dtc(L, rho, v, th - 1e-4))) / (math.log(math.sin(math.radians(th + 1e-4))) - math.log(math.sin(math.radians(th - 1e-4))))
    razon_L = Dtc(2 * L, rho, v, th) / D
    tabla = []
    for vv in (12e3, 20e3, 30e3):
        for tt in (30.0, 45.0, 90.0):
            tabla.append((vv / 1e3, tt, Dtc(L, rho, vv, tt) / 1e3, 1.25 * Dtc(L, rho, vv, tt) / 1e3))
    # misma energia, cuerpo menor y mas rapido
    L2 = L * (v / 30e3) ** (2 / 3)
    return {"E": E, "E_Mt": E / MT, "E2": E2, "D": D, "Df": 1.25 * D, "ex": ex, "razon_L": razon_L, "tabla": tabla,
            "L2": L2, "E_mism": energia(L2, rho, 30e3) / MT, "D2": Dtc(L2, rho, 30e3, th), "masa": masa(L, rho)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Masa = %.4e kg ; E = %.4e J = %.1f Mt (via p^2/2m: %.4e J)" % (r["masa"], r["E"], r["E_Mt"], r["E2"]))
    print("Crater transitorio D_tc = %.3f km ; crater simple final = %.3f km" % (r["D"] / 1e3, r["Df"] / 1e3))
    print("Exponentes numericos: L = %.6f (0.78) ; v = %.6f (0.44) ; g = %.6f (-0.22) ; sin(theta) = %.6f (1/3)" % (r["ex"]["L"], r["ex"]["v"], r["ex"]["g"], r["ex"]["sin"]))
    print("Duplicar L multiplica D_tc por %.6f (2^0.78 = %.6f)" % (r["razon_L"], 2 ** 0.78))
    print("%8s %8s %10s %10s" % ("v[km/s]", "theta", "D_tc[km]", "D_final[km]"))
    for t in r["tabla"]:
        print("%8.0f %8.0f %10.3f %10.3f" % t)
    print("Misma energia con v = 30 km/s: L = %.1f m (E = %.1f Mt) -> D_tc = %.3f km" % (r["L2"], r["E_mism"], r["D2"] / 1e3))
    assert abs(r["E"] / r["E2"] - 1) < 1e-12
    for k, v in (("L", 0.78), ("v", 0.44), ("g", -0.22), ("sin", 1 / 3)):
        assert abs(r["ex"][k] - v) < 1e-6, k
    assert abs(r["razon_L"] - 2 ** 0.78) < 1e-12
    assert abs(r["E_mism"] / r["E_Mt"] - 1) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
