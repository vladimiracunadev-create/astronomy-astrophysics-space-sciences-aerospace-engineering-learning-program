#!/usr/bin/env python3
"""B104-C19: desaceleracion maxima de un reingreso balistico: formula de Allen-Eggers frente a integracion numerica.
Velocidad, altura de escala y angulos ILUSTRATIVOS; atmosfera exponencial; Tierra plana (aproximacion). No es una prediccion de nave alguna."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: V = 7,8 km/s, H = 7,2 km, rho0 = 1,225 kg/m3, atmosfera exponencial, trayectoria casi recta; beta = masa/(Cd A)")
V0, H, RHO0, G = 7800.0, 7200.0, 1.225, 9.80665
E = np.e


def a_max_teorica(gamma_deg):
    return V0**2 * np.sin(np.radians(gamma_deg)) / (2 * E * H) / G      # en g


def integrar(gamma_deg, beta, h0=120e3, dt=0.01):
    g = np.radians(gamma_deg)
    v, h, amax, t = V0, h0, 0.0, 0.0
    while h > 0 and v > 100:
        rho = RHO0 * np.exp(-h / H)
        d = rho * v * v / (2 * beta)
        amax = max(amax, d)
        v += dt * (-d + G * np.sin(g))
        h -= dt * v * np.sin(g)
        t += dt
    return amax / G, t


print("\nangulo de entrada [grados] | g maximos (Allen-Eggers) | g maximos (numerico, beta = 400) | numerico, beta = 800 | velocidad en el pico [km/s]")
res = {}
for gm in (1.0, 1.5, 2.0, 3.0, 5.0, 8.0):
    a_t = a_max_teorica(gm)
    a4, _ = integrar(gm, 400.0)
    a8, _ = integrar(gm, 800.0)
    res[gm] = (a_t, a4, a8)
    print(f"{gm:20.1f} {a_t:24.2f} {a4:32.2f} {a8:22.2f} {V0/np.sqrt(E)/1000:30.2f}")

print(f"\nCon 3 grados la desaceleracion maxima numerica difiere {100*(res[3.0][1]-res[3.0][0])/res[3.0][0]:+.1f} % de la formula; beta no la cambia (400 -> 800: {100*(res[3.0][2]-res[3.0][1])/res[3.0][1]:+.1f} %)")
print("Sin datos de mision: ninguna salida de este modelo corresponde a una nave ni a un reingreso real")

assert abs(a_max_teorica(3.0) - 8.29) < 0.01
for gm in res:
    a_t, a4, a8 = res[gm]
    assert abs(a4 - a_t) / a_t < 0.20, gm
    assert abs(a8 - a4) / a4 < 0.05, gm
assert res[8.0][0] > res[3.0][0] > res[1.0][0]
assert abs(a_max_teorica(1.0) * 3.0 - a_max_teorica(3.0)) / a_max_teorica(3.0) < 0.002
print("Pruebas superadas.")
