#!/usr/bin/env python3
"""B72-C11 — Resonancias orbitales.

(1) Relacion de Laplace n1 - 3 n2 + 2 n3 de Io, Europa y Ganimedes con periodos de la ficha NSSDC.
(2) Semiejes de orbitas resonantes con la rotacion terrestre (1:1, 2:1, 3:1, 15:1).
(3) Modelo de pendulo de una resonancia: periodo de libracion frente a la amplitud (RK4 vs serie)
    y separatriz. Orbitas y condiciones iniciales del pendulo SINTETICAS.
Unidades SI salvo mencion. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14                 # m3/s2 (IAU 2015)
DIA_SIDERAL = 23.9345 * 3600.0   # s (NSSDC, rotacion sideral)

print(f"Python {sys.version.split()[0]} (biblioteca estandar)")

# 1) Laplace
P = {"Io": 1.769138, "Europa": 3.551181, "Ganimedes": 7.154553, "Calisto": 16.689017}   # dias, NSSDC
n = {k: 360.0 / v for k, v in P.items()}
print("\nMovimiento medio [grados/dia] con los periodos de la ficha NSSDC")
for k in P:
    print(f"  {k:<10}{P[k]:>10.6f} d  {n[k]:>12.6f} deg/d")
print(f"Cocientes de periodos: Io/Europa = {P['Io'] / P['Europa']:.5f} ; Europa/Ganimedes = {P['Europa'] / P['Ganimedes']:.5f} ; Ganimedes/Calisto = {P['Ganimedes'] / P['Calisto']:.5f}")
lap = n["Io"] - 3 * n["Europa"] + 2 * n["Ganimedes"]
print(f"n_Io - 3 n_Europa + 2 n_Ganimedes = {lap:.6f} deg/d  ({abs(lap) / n['Io']:.2e} de n_Io)")
assert abs(lap) / n["Io"] < 1e-3
print(f"Calisto no participa: n_Ganimedes/n_Calisto = {n['Ganimedes'] / n['Calisto']:.4f}")

# 2) Orbitas resonantes con la rotacion terrestre
print("\nOrbitas con q vueltas por dia sideral (rotacion 23.9345 h, NSSDC), circulares, mu IAU")
print(f"{'q':>4}{'periodo [h]':>14}{'a [km]':>12}{'h sobre 6378.137 km [km]':>28}")
for q in (1, 2, 3, 15):
    T = DIA_SIDERAL / q
    a = (MU * (T / (2 * math.pi)) ** 2) ** (1.0 / 3.0)
    print(f"{q:>4}{T / 3600:>14.4f}{a / 1e3:>12.1f}{a / 1e3 - 6378.137:>28.1f}")

# 3) Pendulo de resonancia: phi'' = -w0^2 sin(phi)
w0 = 1.0   # unidad adimensional


def libracion(theta0, dt=1e-3):
    """Periodo por cruces de phi = 0 (un cuarto de periodo entre cruce y maximo) con RK4."""
    phi, om, t = theta0, 0.0, 0.0
    f = lambda p, o: (o, -w0 * w0 * math.sin(p))
    t_cruce = None
    while True:
        k1 = f(phi, om); k2 = f(phi + dt / 2 * k1[0], om + dt / 2 * k1[1])
        k3 = f(phi + dt / 2 * k2[0], om + dt / 2 * k2[1]); k4 = f(phi + dt * k3[0], om + dt * k3[1])
        nphi = phi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        nom = om + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if phi > 0 >= nphi:      # cruce por cero: fraccion lineal
            t_cruce = t + dt * phi / (phi - nphi)
            return 4.0 * t_cruce
        phi, om, t = nphi, nom, t + dt


def serie(theta0):
    return 2 * math.pi / w0 * (1 + theta0 ** 2 / 16 + 11 * theta0 ** 4 / 3072)


print("\nPeriodo de libracion T/T0 del pendulo de resonancia (T0 = 2 pi / w0) frente a la amplitud")
print(f"{'amplitud [deg]':>15}{'RK4 T/T0':>12}{'serie T/T0':>13}{'dif. relativa':>15}")
for deg in (10, 30, 60, 90):
    th = math.radians(deg)
    num = libracion(th) / (2 * math.pi / w0)
    ser = serie(th) / (2 * math.pi / w0)
    print(f"{deg:>15}{num:>12.6f}{ser:>13.6f}{abs(num - ser) / num:>15.2e}")
    if deg <= 60:
        assert abs(num - ser) / num < 1e-3

print("\nSeparatriz: energia E = phi'^2/2 - w0^2 cos(phi); libra si E < w0^2, circula si E > w0^2")
for phi0, om0 in ((0.0, 1.5), (0.0, 1.99), (0.0, 2.01), (math.pi / 2, 1.0)):
    E = 0.5 * om0 ** 2 - w0 ** 2 * math.cos(phi0)
    print(f"  phi0 = {math.degrees(phi0):>5.1f} deg, phi'0 = {om0:.2f} w0 -> E = {E:+.4f} -> {'libra' if E < w0 ** 2 else 'circula'}")
print(f"Semianchura maxima de la resonancia en velocidad: |phi'|max = 2 w0 = {2 * w0:.1f} w0")
print("Pruebas superadas.")
