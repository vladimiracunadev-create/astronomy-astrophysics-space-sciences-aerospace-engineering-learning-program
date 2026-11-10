#!/usr/bin/env python3
"""B72-C06 — Arrastre atmosferico.

Aceleracion de arrastre, coeficiente balistico, decaimiento del semieje por vuelta
(formula de orbita circular) frente a una integracion RK4 con atmosfera exponencial
ILUSTRATIVA que gira con la Tierra, y vida util orbital. Orbitas SINTETICAS.
Unidades SI; marco inercial geocentrico. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14           # m3/s2 (IAU 2015)
RE = 6378137.0             # m (NSSDC)
OMEGA_T = 2 * math.pi / (23.9345 * 3600)   # rad/s, rotacion sideral (NSSDC)
RHO_REF, H_REF, ESC = 3.0e-12, 400e3, 60e3  # ILUSTRATIVOS: densidad a 400 km y altura de escala
CD = 2.2                   # ILUSTRATIVO
DIA = 86400.0


def rho(h):
    return RHO_REF * math.exp(-(h - H_REF) / ESC)


def a_drag(r, v, B):
    """Arrastre con viento co-rotante; B = m/(Cd A) en kg/m2."""
    vr = [v[0] + OMEGA_T * r[1], v[1] - OMEGA_T * r[0], v[2]]
    vm = math.sqrt(sum(c * c for c in vr))
    h = math.sqrt(sum(c * c for c in r)) - RE
    k = -0.5 * rho(h) * vm / B
    return [k * vr[i] for i in range(3)]


def acel(r, v, B):
    d = math.sqrt(sum(c * c for c in r))
    ad = a_drag(r, v, B)
    return [-MU * r[i] / d ** 3 + ad[i] for i in range(3)]


def rk4(r, v, dt, B):
    k1r, k1v = v, acel(r, v, B)
    r2 = [r[i] + 0.5 * dt * k1r[i] for i in range(3)]; v2 = [v[i] + 0.5 * dt * k1v[i] for i in range(3)]
    k2r, k2v = v2, acel(r2, v2, B)
    r3 = [r[i] + 0.5 * dt * k2r[i] for i in range(3)]; v3 = [v[i] + 0.5 * dt * k2v[i] for i in range(3)]
    k3r, k3v = v3, acel(r3, v3, B)
    r4 = [r[i] + dt * k3r[i] for i in range(3)]; v4 = [v[i] + dt * k3v[i] for i in range(3)]
    k4r, k4v = v4, acel(r4, v4, B)
    return ([r[i] + dt / 6 * (k1r[i] + 2 * k2r[i] + 2 * k3r[i] + k4r[i]) for i in range(3)],
            [v[i] + dt / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i]) for i in range(3)])


def semieje(r, v):
    d = math.sqrt(sum(c * c for c in r)); vv = sum(c * c for c in v)
    return 1.0 / (2.0 / d - vv / MU)


def da_por_vuelta(a, B, h):
    """Orbita circular, viento co-rotante ignorado: da = -2 pi rho a^2 / B."""
    return -2 * math.pi * rho(h) * a * a / B


def factor_rotacion(a):
    """(1 - omega/n)^2 para una orbita ecuatorial directa (atmosfera co-rotante)."""
    n = math.sqrt(MU / a ** 3)
    return (1 - OMEGA_T / n) ** 2


def vida_util(h0, B, h_fin=180e3):
    """Dias hasta bajar de h_fin (orbita circular, paso de una vuelta)."""
    a = RE + h0; t = 0.0
    while a - RE > h_fin and t < 3650 * DIA:
        T = 2 * math.pi * math.sqrt(a ** 3 / MU)
        a += da_por_vuelta(a, B, a - RE)
        t += T
    return t / DIA


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print(f"Atmosfera exponencial ILUSTRATIVA: rho(400 km) = {RHO_REF:.1e} kg/m3, H = {ESC/1e3:.0f} km, Cd = {CD} (no son un modelo atmosferico)")

print("\nAceleracion de arrastre y coeficiente balistico a 400 km (v circular)")
print(f"{'m [kg]':>8}{'A [m2]':>8}{'B=m/(Cd A) [kg/m2]':>22}{'a_drag [m/s2]':>16}")
v = math.sqrt(MU / (RE + 400e3))
for m, A in ((1000.0, 10.0), (100.0, 1.0), (10.0, 0.1), (4.0, 0.1)):
    B = m / (CD * A)
    print(f"{m:>8.0f}{A:>8.2f}{B:>22.2f}{0.5 * rho(400e3) * v * v / B:>16.3e}")

# Verificacion: formula por vuelta frente a la integracion
B = 100.0 / (CD * 1.0)
a0 = RE + 400e3
r = [a0, 0.0, 0.0]; vv = [0.0, math.sqrt(MU / a0), 0.0]
dt = 10.0
T0 = 2 * math.pi * math.sqrt(a0 ** 3 / MU)
nvueltas = 60
n = int(nvueltas * T0 / dt)
for _ in range(n):
    r, vv = rk4(r, vv, dt, B)
a1 = semieje(r, vv)
num = a1 - a0
teo = da_por_vuelta(a0, B, 400e3) * (n * dt / T0)
print(f"\nVerificacion con B = {B:.2f} kg/m2, {n * dt / T0:.1f} vueltas ({n * dt / 3600:.1f} h), RK4 paso {dt:.0f} s")
print(f"  semieje: variacion numerica = {num:.2f} m ; formula circular = {teo:.2f} m ; dif. relativa = {abs(num - teo) / abs(teo):.2%}")
teo2 = teo * factor_rotacion(a0)
print(f"  con el factor de rotacion (1 - omega/n)^2 = {factor_rotacion(a0):.4f} (orbita ecuatorial directa): formula = {teo2:.2f} m ; dif. relativa = {abs(num - teo2) / abs(teo2):.2%}")
print("  (la diferencia restante viene de que rho cae con la altura mientras el semieje decae)")
assert abs(num - teo2) / abs(teo2) < 0.03

print("\nVida util (hasta 180 km) en dias, orbita circular, atmosfera ilustrativa")
print(f"{'h0 [km]':>8}" + "".join(f"{'B=' + str(b):>15}" for b in (10, 45, 200)))
for h0 in (300, 400, 500):
    print(f"{h0:>8}" + "".join((f"{vida_util(h0 * 1e3, b):>15.1f}" if vida_util(h0 * 1e3, b) < 3650 else f"{'>3650 (tope)':>15}") for b in (10, 45, 200)))
base = vida_util(400e3, 45.0)
RHO_REF *= 3.0
triple = vida_util(400e3, 45.0)
print(f"\nSi la densidad se triplica: la vida util de 400 km con B = 45 pasa de {base:.1f} a {triple:.1f} dias")
print("Pruebas superadas.")
