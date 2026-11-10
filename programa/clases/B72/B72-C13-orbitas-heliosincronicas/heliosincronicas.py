#!/usr/bin/env python3
"""B72-C13 — Orbitas heliosincronicas.

Inclinacion que hace que el nodo avance con el Sol: cos i = -(dOm/dt)_requerida / (1.5 n J2 (R/p)^2),
verificada con una integracion RK4 con J2, deriva de la hora solar local con un error de inclinacion y altitud maxima.
Orbitas SINTETICAS. Unidades SI; angulos en grados en la salida. Marco: ecuador de la fecha.
Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6
DIA = 86400.0
RAD = 180.0 / math.pi
ANO_TROPICO = 365.2422 * DIA     # s, NO consultado en una fuente concreta
ANO_SIDERAL = 365.256 * DIA      # s, ficha de la Tierra (periodo orbital sideral, NSSDC)
OM_SOL = 2 * math.pi / ANO_TROPICO


def factor(a, e=0.0):
    n = math.sqrt(MU / a ** 3)
    p = a * (1 - e * e)
    return 1.5 * n * J2 * (RE / p) ** 2     # dOm/dt = -factor cos i


def inclinacion_ss(a, e=0.0, om=OM_SOL):
    c = -om / factor(a, e)
    return math.degrees(math.acos(c)) if abs(c) <= 1 else float("nan")


def acel(r):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    return [-MU * x / d ** 3 + k * x * (1 - zz), -MU * y / d ** 3 + k * y * (1 - zz), -MU * z / d ** 3 + k * z * (3 - zz)]


def rk4(r, v, dt):
    a1 = acel(r); r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
    a2 = acel(r2); r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
    a3 = acel(r3); r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
    a4 = acel(r4)
    return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
            [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])


def nodo(r, v):
    h = [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]]
    return math.atan2(h[0], -h[1])


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC), mu = 3.986004e14 (IAU 2015), Re = 6378137 m")
print(f"Nodo requerido: 360 deg / ano tropico (365.2422 d, NO consultado) = {OM_SOL * DIA * RAD:.5f} deg/dia")
print(f"  con el periodo sideral de la ficha (365.256 d): {2 * math.pi / ANO_SIDERAL * DIA * RAD:.5f} deg/dia (diferencia {abs(1 - ANO_TROPICO / ANO_SIDERAL):.2e})")

print("\nInclinacion heliosincrona (e = 0)")
print(f"{'h [km]':>8}{'a [km]':>10}{'i [deg]':>10}{'periodo [min]':>15}")
for h in (100, 400, 600, 700, 800, 1000, 1500):
    a = RE + h * 1e3
    print(f"{h:>8}{a / 1e3:>10.1f}{inclinacion_ss(a):>10.3f}{2 * math.pi * math.sqrt(a ** 3 / MU) / 60:>15.2f}")

# Altitud maxima: cos i = -1
lo, hi = RE, RE * 3
for _ in range(100):
    mid = 0.5 * (lo + hi)
    if OM_SOL / factor(mid) <= 1.0:
        lo = mid
    else:
        hi = mid
print(f"\nEl radio orbital maximo con |cos i| <= 1 es a = {lo / 1e3:.0f} km (altitud {(lo - RE) / 1e3:.0f} km, e = 0): por encima no existe heliosincrona")
# nota: cos i = -om/factor; factor decrece con a, asi que existe a_max

# Verificacion RK4
h = 700e3
a = RE + h
i = math.radians(inclinacion_ss(a))
n = math.sqrt(MU / a ** 3)
r = [a, 0.0, 0.0]; v = [0.0, n * a * math.cos(i), n * a * math.sin(i)]
dt = 10.0; dias = 6
t = 0.0
tt, oo = [], []
base = nodo(r, v); prev = base; acc = 0.0
for k in range(int(dias * DIA / dt) + 1):
    if k % 60 == 0:
        o = nodo(r, v)
        d = o - prev; d -= 2 * math.pi * round(d / (2 * math.pi)); acc += d; prev = o
        tt.append(k * dt); oo.append(acc)
    r, v = rk4(r, v, dt)
tm = sum(tt) / len(tt); om_ = sum(oo) / len(oo)
pend = sum((tt[k] - tm) * (oo[k] - om_) for k in range(len(tt))) / sum((x - tm) ** 2 for x in tt)
pend_dia = pend * DIA * RAD
req = OM_SOL * DIA * RAD
print(f"\nVerificacion RK4 ({dias} dias, h = 700 km, i = {math.degrees(i):.3f} deg): pendiente del nodo = {pend_dia:.5f} deg/dia ; requerida = {req:.5f} deg/dia ; dif. = {abs(pend_dia - req) / req:.2%}")
assert abs(pend_dia - req) / req < 0.01

# Deriva de la hora solar local por error de inclinacion
print("\nDeriva de la hora solar local del nodo con un error de inclinacion, h = 700 km")
a = RE + 700e3
i0 = math.radians(inclinacion_ss(a))
print(f"{'error di [deg]':>15}{'d(dOm/dt) [deg/dia]':>22}{'deriva LTAN [min/ano]':>24}")
for di in (0.01, 0.05, 0.1):
    d_om = factor(a) * math.sin(i0) * math.radians(di) * DIA * RAD     # deg/dia respecto al Sol: 4 min de hora local = 1 deg
    print(f"{di:>15.2f}{d_om:>22.6f}{d_om * 365.25 * 4.0:>24.2f}")
print("(1 grado de longitud del nodo equivale a 4 minutos de hora solar local)")
print("Pruebas superadas.")
