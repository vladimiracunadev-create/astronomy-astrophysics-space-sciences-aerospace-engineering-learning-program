#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C07: simulacion longitudinal de un rover sobre pendientes con traccion dependiente del patinaje.

Datos consultados (2026-11-10): gravedad media de Marte 3.73 m/s2 y de la Luna 1.62 m/s2 (fichas NASA/NSSDC); Tierra g_n = 9.80665 m/s2
(NIST, CODATA 2022). De la pagina «Rover Components» de Mars 2020 (NASA): velocidad maxima en terreno llano duro 152 m/h (0.042 m/s),
usada solo como escala de la velocidad de mando; evitacion operativa de mas de 30 grados. ILUSTRATIVOS (sinteticos, no de ningun rover ni
suelo real): masa 1000 kg; coeficiente de traccion maximo mu = 0.50; constante de patinaje s0 = 0.20; coeficiente de resistencia a la
rodadura c_r = 0.10; velocidad circunferencial de las ruedas v_c = 0.042 m/s constante.
Modelo: M dv/dt = M g [cos(theta) (mu (1 - exp(-s/s0)) - c_r) - sin(theta)], s = 1 - v/v_c; integracion RK4 con dt = 2e-4 s.
Equilibrio: s* = -s0 ln(1 - (c_r + tan(theta))/mu), posible si c_r + tan(theta) < mu, es decir theta < atan(mu - c_r).
Sistema: eje x a lo largo de la pendiente (subida positiva); v en m/s; terreno homogeneo, sin vuelco ni limite de potencia.
Tolerancias: patinaje simulado frente al de equilibrio < 1e-6; cambio al reducir dt a la mitad < 1e-8.
"""
from __future__ import annotations
import math, platform

M_ROVER, MU, S0, CR, VC = 1000.0, 0.50, 0.20, 0.10, 0.042
GRAV = {"Tierra": 9.80665, "Marte": 3.73, "Luna": 1.62}


def acel(v, g, th):
    s = min(max(1.0 - v / VC, -1.0), 1.0)
    return g * (math.cos(th) * (MU * (1.0 - math.exp(-s / S0)) - CR) - math.sin(th))


def simula(g, th, t_fin=3.0, dt=2e-4, v0=None):
    v = VC if v0 is None else v0
    for _ in range(int(t_fin / dt)):
        k1 = acel(v, g, th)
        k2 = acel(v + 0.5 * dt * k1, g, th)
        k3 = acel(v + 0.5 * dt * k2, g, th)
        k4 = acel(v + dt * k3, g, th)
        v += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return v


def s_equilibrio(th):
    x = (CR + math.tan(th)) / MU
    return None if x >= 1.0 else -S0 * math.log(1.0 - x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Rover y suelo ILUSTRATIVOS: mu = {MU}, s0 = {S0}, c_r = {CR}, v_c = {VC} m/s; pendiente maxima atan(mu - c_r) = {math.degrees(math.atan(MU - CR)):.3f} deg")
    print("Patinaje de equilibrio y velocidad de avance (Marte), simulacion frente a analitica:")
    print(" pendiente [deg]  s* analitico   s simulado   v [mm/s]   tiempo para 100 m [min]")
    dmax = 0.0
    for deg in (0, 5, 10, 15, 20):
        th = math.radians(deg)
        s_an = s_equilibrio(th)
        v = simula(GRAV["Marte"], th)
        s_sim = 1.0 - v / VC
        dmax = max(dmax, abs(s_sim - s_an))
        print(f"{deg:13d} {s_an:14.6f} {s_sim:12.6f} {v * 1000:10.3f} {100.0 / v / 60:20.2f}")
    print(f"Diferencia maxima simulacion-analitica: {dmax:.2e}")
    print("Efecto de la gravedad a 15 grados: mismo patinaje, distinta rapidez de la transitoria")
    th = math.radians(15)
    for nom, g in GRAV.items():
        v = simula(g, th, t_fin=6.0)
        # tiempo para alcanzar el 99 % del cambio
        vv, t, dt = VC, 0.0, 2e-4
        v_inf = VC * (1 - s_equilibrio(th))
        while abs(vv - v_inf) > 0.01 * abs(VC - v_inf) and t < 20:
            k1 = acel(vv, g, th)
            k2 = acel(vv + 0.5 * dt * k1, g, th)
            k3 = acel(vv + 0.5 * dt * k2, g, th)
            k4 = acel(vv + dt * k3, g, th)
            vv += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            t += dt
        print(f"  {nom:7s} g = {g:7.5f} m/s2 ; s = {1 - v / VC:.6f} ; tiempo al 99 % del regimen = {t * 1000:7.1f} ms")
    # convergencia
    v1 = simula(3.73, th, t_fin=1.0, dt=2e-4)
    v2 = simula(3.73, th, t_fin=1.0, dt=1e-4)
    conv = abs(v1 - v2)
    print(f"Cambio de v al reducir dt a la mitad: {conv:.2e} m/s")
    # pendiente por encima del maximo
    th_alta = math.radians(25)
    v_alta = simula(3.73, th_alta, t_fin=3.0)
    print(f"A 25 grados (> {math.degrees(math.atan(MU - CR)):.1f}) no hay equilibrio con s < 1: v tras 3 s = {v_alta * 1000:.1f} mm/s (negativa = retrocede)")
    # perfil de ruta por tramos
    tramos = [(30.0, 0), (40.0, 10), (30.0, 18)]
    tiempo = 0.0
    print("Ruta por tramos (Marte): longitud [m], pendiente [deg], s, v [mm/s], tiempo [min]")
    for ln, deg in tramos:
        s = s_equilibrio(math.radians(deg))
        v = VC * (1 - s)
        tt = ln / v / 60
        tiempo += tt
        print(f"  {ln:5.1f} {deg:6d} {s:8.4f} {v * 1000:8.3f} {tt:8.2f}")
    print(f"  tiempo total = {tiempo:.2f} min ; sin patinaje habria sido {100.0 / VC / 60:.2f} min")
    assert dmax < 1e-6 and conv < 1e-8 and v_alta < 0.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
