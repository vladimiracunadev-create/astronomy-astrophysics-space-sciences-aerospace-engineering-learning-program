#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C05: reparto de cargas por rueda y margen de vuelco de un rover en pendiente.

Datos consultados (2026-11-10): gravedad media de Marte 3.73 m/s2 y de la Luna 1.62 m/s2 (fichas NASA/NSSDC); Tierra g_n = 9.80665 m/s2
(NIST, CODATA 2022). De la pagina «Rover Components» de Mars 2020 (NASA, science.nasa.gov): diseno para 45 grados de inclinacion en
cualquier direccion sin volcar y evitacion operativa de mas de 30 grados. ILUSTRATIVOS (sinteticos, no de ningun rover real): masa 1000 kg,
base de ruedas L = 2.2 m, via T = 1.6 m, altura del centro de masas h = 0.70 m, centro de masas 0.10 m por delante del centro de la base.
Modelo: cuasiestatico, rover rigido sobre un poligono de apoyo rectangular; el vector gravedad se proyecta sobre el plano de apoyo; el
margen de vuelco es la distancia minima (m) de esa proyeccion a los bordes del poligono. Cabeceo theta (morro arriba) y balanceo phi
(lado derecho abajo). Marco del cuerpo: x adelante, y a la izquierda, z arriba. Supuestos: terreno plano inclinado, rigido, sin
aceleraciones salvo la prueba de giro.
Tolerancias: angulo de vuelco por biseccion frente a la formula cerrada < 1e-9 rad; suma de cargas = M g cos(theta) < 1e-9 relativa.
"""
from __future__ import annotations
import math, platform

M, L, T, H, XC = 1000.0, 2.2, 1.6, 0.70, 0.10
GRAV = {"Tierra": 9.80665, "Marte": 3.73, "Luna": 1.62}


def proyeccion(theta, phi):
    px = XC - H * math.tan(theta) / math.cos(phi)
    py = -H * math.tan(phi)
    return px, py


def margen(theta, phi):
    px, py = proyeccion(theta, phi)
    return min(L / 2 - px, px + L / 2, T / 2 - py, py + T / 2)


def vuelco(eje, signo=1):
    """Angulo en el que el margen se anula, por biseccion, para cabeceo (eje 0) o balanceo (eje 1)."""
    lo, hi = 0.0, math.radians(89.0)
    f = (lambda a: margen(signo * a, 0.0)) if eje == 0 else (lambda a: margen(0.0, signo * a))
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def cargas_ejes(g, theta):
    """Cargas del eje delantero y trasero [N] en pendiente de cabeceo theta (morro arriba)."""
    br = L / 2 + XC
    bf = L / 2 - XC
    w = M * g
    nf = w * (math.cos(theta) * br - math.sin(theta) * H) / L
    nr = w * (math.cos(theta) * bf + math.sin(theta) * H) / L
    return nf, nr


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Rover ILUSTRATIVO: M = {M:.0f} kg, L = {L} m, T = {T} m, h = {H} m, CG {XC} m por delante del centro")
    cerr = {"cab+": math.atan((L / 2 + XC) / H), "cab-": math.atan((L / 2 - XC) / H), "bal": math.atan(T / 2 / H)}
    num = {"cab+": vuelco(0, 1), "cab-": vuelco(0, -1), "bal": vuelco(1)}
    print("Angulos de vuelco (independientes de g):")
    errmax = 0.0
    for k, nom in (("cab+", "cabeceo, subiendo"), ("cab-", "cabeceo, bajando"), ("bal", "balanceo lateral")):
        errmax = max(errmax, abs(num[k] - cerr[k]))
        print(f"  {nom:19s} biseccion = {math.degrees(num[k]):8.4f} deg ; formula cerrada = {math.degrees(cerr[k]):8.4f} deg")
    print(f"Error maximo biseccion frente a formula: {errmax:.2e} rad")
    print("Margen de vuelco [m] a 30 grados (limite operativo de evitacion, valor consultado), cabeceo y balanceo:")
    print(f"  cabeceo 30 deg: {margen(math.radians(30), 0):.4f} m ; balanceo 30 deg: {margen(0, math.radians(30)):.4f} m ; combinado 20+20 deg: {margen(math.radians(20), math.radians(20)):.4f} m")
    print("Cargas por eje en pendiente (cabeceo, morro arriba):")
    print(" cuerpo   pendiente [deg]  N_del [N]  N_tras [N]  suma/(M g cos) ")
    sm = 0.0
    for nom, g in GRAV.items():
        for deg in (0, 15, 30):
            th = math.radians(deg)
            nf, nr = cargas_ejes(g, th)
            rel = (nf + nr) / (M * g * math.cos(th))
            sm = max(sm, abs(rel - 1))
            print(f"{nom:7s} {deg:12d} {nf:12.2f} {nr:11.2f} {rel:12.6f}")
    print(f"Desviacion maxima de la suma de cargas respecto a M g cos(theta): {sm:.2e}")
    print("Transferencia lateral de carga en pendiente transversal 20 grados (diferencia derecha-izquierda / (M g)):")
    for nom, g in GRAV.items():
        ph = math.radians(20)
        n_tot = M * g * math.cos(ph)
        py = proyeccion(0.0, ph)[1]
        dn = n_tot * (T / 2 - py - (py + T / 2)) / T  # via la proyeccion del CG (derecha - izquierda)
        dn_cerr = 2 * M * g * math.cos(ph) * H * math.tan(ph) / T
        assert abs(dn - dn_cerr) / dn_cerr < 1e-12
        print(f"  {nom:7s} dN = {dn_cerr:9.2f} N ; dN/(M g) = {dn_cerr / (M * g):.5f}")
    print("Giro en terreno llano: aceleracion lateral critica a_y = g T/(2h) y velocidad critica en un arco de 5 m:")
    for nom, g in GRAV.items():
        ay = g * T / (2 * H)
        print(f"  {nom:7s} a_y crit = {ay:7.3f} m/s2 ; v crit = {math.sqrt(ay * 5.0):6.3f} m/s")
    assert errmax < 1e-9 and sm < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
