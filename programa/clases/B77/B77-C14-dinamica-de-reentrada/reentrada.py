#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C14: reentrada balistica (solucion de Allen-Eggers frente a integracion numerica).

Datos consultados (2026-11-10): resumen del NACA Report 1381 (Allen y Eggers): analisis simplificado con Cd constante y densidad exponencial; la desaceleracion
maxima depende solo de la velocidad de entrada y del angulo de trayectoria, no de la masa ni de Cd (solo el resumen del registro NTRS); rho0 = 1.217 kg/m3 y H = 8.5 km
(NASA/NSSDC Earth Fact Sheet); radio 6378.137 km; D = Cd q A (NASA Glenn); g_n = 9.80665 m/s2 (NIST).
NO CONSULTADO (valor estandar rotulado): mu = 3.986004418e14 m3/s2. La formula a_max = v_E^2 sin(gamma)/(2 e H) y la solucion cerrada se DERIVAN en la clase y se verifican aqui.
ILUSTRATIVOS (sinteticos): v_E = 7800 m/s a 120 km de altitud, angulos de entrada de 3 a 20 grados bajo el horizonte, coeficientes balisticos beta = m/(Cd A) de 100, 300 y 1000 kg/m2.
Sistema: plano vertical local, trayectoria recta con gamma constante y SIN gravedad (modelo de Allen-Eggers); segunda integracion con gravedad y Tierra esferica (plano orbital).
Modelo: dv/dt = -rho(h) v^2/(2 beta); dh/dt = -v sin(gamma_E); solucion v = v_E exp(-K e^(-h/H)), K = rho0 H/(2 beta sin gamma_E); a = -dv/dt; h_pico = H ln(2K).
Criterio de parada: suelo, v < 2 % de v_E (el vehiculo ya no desacelera de forma relevante) o 20 000 pasos.
Tolerancias: a_max numerica (sin gravedad) frente a la formula cerrada 5e-3 relativa; independencia de beta 5e-3.
"""
import math, platform

RHO0, H, RE, MU, G0 = 1.217, 8500.0, 6378137.0, 3.986004418e14, 9.80665
VE, HE = 7800.0, 120e3


def analitico(beta, gam_deg):
    s = math.sin(math.radians(gam_deg))
    K = RHO0 * H / (2 * beta * s)
    return dict(K=K, a_max=VE ** 2 * s / (2 * math.e * H), h_pico=H * math.log(2 * K), v_pico=VE * math.exp(-0.5))


def sin_gravedad(beta, gam_deg, dt=0.1):
    s = math.sin(math.radians(gam_deg))

    def f(x):
        h, v = x
        return (-v * s, -RHO0 * math.exp(-h / H) * v * v / (2 * beta))
    x, t = (HE, VE), 0.0
    amax, hpk, vpk = 0.0, 0.0, 0.0
    while x[0] > 0.0 and x[1] > 0.02 * VE:
        k1 = f(x); k2 = f([a + dt / 2 * b for a, b in zip(x, k1)]); k3 = f([a + dt / 2 * b for a, b in zip(x, k2)]); k4 = f([a + dt * b for a, b in zip(x, k3)])
        x = [a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(x, k1, k2, k3, k4)]
        t += dt
        a = RHO0 * math.exp(-x[0] / H) * x[1] ** 2 / (2 * beta)
        if a > amax:
            amax, hpk, vpk = a, x[0], x[1]
    return dict(a_max=amax, h_pico=hpk, v_pico=vpk, t=t, v_suelo=x[1])


def con_gravedad(beta, gam_deg, dt=0.1):
    def f(x):
        r, th, v, g = x
        h = r - RE
        gr = MU / (r * r)
        d = RHO0 * math.exp(-h / H) * v * v / (2 * beta)
        return (v * math.sin(g), v * math.cos(g) / r, -d - gr * math.sin(g), -(gr - v * v / r) * math.cos(g) / v)
    x = [RE + HE, 0.0, VE, -math.radians(gam_deg)]
    amax, hpk = 0.0, 0.0
    pasos = 0
    while x[0] > RE and x[2] > 0.02 * VE and pasos < 20000:
        pasos += 1
        k1 = f(x); k2 = f([a + dt / 2 * b for a, b in zip(x, k1)]); k3 = f([a + dt / 2 * b for a, b in zip(x, k2)]); k4 = f([a + dt * b for a, b in zip(x, k3)])
        x = [a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(x, k1, k2, k3, k4)]
        a = RHO0 * math.exp(-(x[0] - RE) / H) * x[2] ** 2 / (2 * beta)
        if a > amax:
            amax, hpk = a, x[0] - RE
    return dict(a_max=amax, h_pico=hpk)


def calcular():
    r = {"filas": []}
    peor_a, dif_beta = 0.0, 0.0
    for gam in (3.0, 5.0, 10.0, 20.0):
        fila = {"gam": gam, "casos": []}
        for beta in (100.0, 300.0, 1000.0):
            an, nu = analitico(beta, gam), sin_gravedad(beta, gam)
            peor_a = max(peor_a, abs(nu["a_max"] - an["a_max"]) / an["a_max"])
            fila["casos"].append(dict(beta=beta, an=an, nu=nu))
        am = [c["nu"]["a_max"] for c in fila["casos"]]
        fila["dif_beta"] = (max(am) - min(am)) / min(am)
        dif_beta = max(dif_beta, fila["dif_beta"])
        r["filas"].append(fila)
    r["peor_a"], r["dif_beta"] = peor_a, dif_beta
    r["grav"] = [(gam, beta, analitico(beta, gam)["a_max"], con_gravedad(beta, gam)) for gam, beta in ((5.0, 300.0), (10.0, 300.0))]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Entrada SINTETICA: v_E = {VE:.0f} m/s a {HE/1e3:.0f} km; atmosfera exponencial rho0 = {RHO0}, H = {H/1e3} km")
    print(" gamma_E  beta   a_max analitica [g]  a_max numerica [g]  h_pico analitica/numerica [km]  v_pico num [m/s]")
    for fila in r["filas"]:
        for c in fila["casos"]:
            print(f"  {fila['gam']:4.1f}  {c['beta']:6.0f}  {c['an']['a_max']/G0:14.3f}  {c['nu']['a_max']/G0:16.3f}  {c['an']['h_pico']/1e3:10.2f}/{c['nu']['h_pico']/1e3:6.2f}  {c['nu']['v_pico']:12.1f}")
    print(f"Error relativo maximo de a_max (numerica vs cerrada) = {r['peor_a']:.2e}; dispersion maxima de a_max entre beta = {r['dif_beta']:.2e}")
    print("Con gravedad y Tierra esferica (la trayectoria se curva hacia abajo al perder velocidad):")
    for gam, beta, a_an, c in r["grav"]:
        print(f"  gamma_E = {gam:.0f} grados, beta = {beta:.0f}: a_max = {c['a_max']/G0:.3f} g frente a {a_an/G0:.3f} g de Allen-Eggers ({(c['a_max']/a_an-1)*100:+.1f} %); h_pico = {c['h_pico']/1e3:.1f} km")
    assert r["peor_a"] < 5e-3 and r["dif_beta"] < 5e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
