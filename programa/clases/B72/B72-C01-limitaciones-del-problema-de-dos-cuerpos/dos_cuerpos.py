#!/usr/bin/env python3
"""B72-C01 — Limitaciones del problema de dos cuerpos.

Compara las aceleraciones perturbadoras con la central y mide cuanto se separa una
orbita kepleriana de una orbita con J2 integrada numericamente (RK4).
Unidades SI. Marco: inercial geocentrico (ecuador de la fecha), orbita SINTETICA.
Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14        # m3/s2, (GM)N Tierra, IAU 2015 B3
RE = 6378137.0          # m, radio ecuatorial (NSSDC)
J2 = 1082.63e-6         # NSSDC
C = 299792458.0         # m/s, NIST
LSUN = 3.828e26         # W, NSSDC
AU = 149.598e9          # m, semieje mayor de la Tierra (NSSDC)
MU_SUN = 1.3271244e20   # m3/s2, IAU 2015
MU_MOON = 4902.800e9    # m3/s2, JPL SSD
D_MOON = 0.3844e9       # m, NSSDC
S0 = LSUN / (4 * math.pi * AU ** 2)   # irradiancia a 1 UA (derivada)


def cinematica_kepler(a, e, inc, raan, argp, M0, t):
    """Elementos -> (r, v) a t segundos de la epoca (problema de dos cuerpos)."""
    n = math.sqrt(MU / a ** 3)
    M = (M0 + n * t) % (2 * math.pi)
    E = M
    for _ in range(50):
        E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    rp = [r * math.cos(nu), r * math.sin(nu), 0.0]
    vp = [-math.sqrt(MU / p) * math.sin(nu), math.sqrt(MU / p) * (e + math.cos(nu)), 0.0]
    cO, sO, ci, si, cw, sw = math.cos(raan), math.sin(raan), math.cos(inc), math.sin(inc), math.cos(argp), math.sin(argp)
    R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
         [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
         [sw * si, cw * si, ci]]
    f = lambda x: [sum(R[i][j] * x[j] for j in range(3)) for i in range(3)]
    return f(rp), f(vp)


def acel(r, con_j2):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    a = [-MU * x / d ** 3, -MU * y / d ** 3, -MU * z / d ** 3]
    if con_j2:
        k = -1.5 * J2 * MU * RE ** 2 / d ** 5
        zz = 5 * z * z / (d * d)
        a[0] += k * x * (1 - zz)
        a[1] += k * y * (1 - zz)
        a[2] += k * z * (3 - zz)
    return a


def rk4(r, v, dt, con_j2):
    def f(r, v):
        return v, acel(r, con_j2)
    k1r, k1v = f(r, v)
    k2r, k2v = f([r[i] + 0.5 * dt * k1r[i] for i in range(3)], [v[i] + 0.5 * dt * k1v[i] for i in range(3)])
    k3r, k3v = f([r[i] + 0.5 * dt * k2r[i] for i in range(3)], [v[i] + 0.5 * dt * k2v[i] for i in range(3)])
    k4r, k4v = f([r[i] + dt * k3r[i] for i in range(3)], [v[i] + dt * k3v[i] for i in range(3)])
    return ([r[i] + dt / 6 * (k1r[i] + 2 * k2r[i] + 2 * k3r[i] + k4r[i]) for i in range(3)],
            [v[i] + dt / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i]) for i in range(3)])


def integra(r, v, t, dt, con_j2):
    n = int(round(t / dt))
    for _ in range(n):
        r, v = rk4(r, v, dt, con_j2)
    return r, v


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Marco inercial geocentrico; orbitas y parametros SINTETICOS o ILUSTRATIVOS")
print(f"Irradiancia derivada S0 = L/(4 pi UA^2) = {S0:.1f} W/m2")

# 1) Tabla de aceleraciones perturbadoras relativas a la central
print("\nAceleraciones relativas a mu/r^2 (A/m = 0.01 m2/kg, Cr = 1.3, Cd = 2.2: ILUSTRATIVOS)")
print(f"{'orbita':<8}{'r [km]':>10}{'central [m/s2]':>16}{'J2':>10}{'Luna':>10}{'Sol':>10}{'SRP':>10}{'arrastre':>10}")
casos = [("LEO", 6778.137e3, 3.0e-12), ("GPS", 26560e3, 0.0), ("GEO", 42164e3, 0.0)]
for nombre, r, rho in casos:
    ac = MU / r ** 2
    aj2 = 1.5 * J2 * MU * RE ** 2 / r ** 4
    amoon = 2 * MU_MOON * r / D_MOON ** 3
    asun = 2 * MU_SUN * r / AU ** 3
    asrp = 1.3 * 0.01 * S0 / C
    v = math.sqrt(MU / r)
    adrag = 0.5 * rho * 2.2 * 0.01 * v * v
    print(f"{nombre:<8}{r/1e3:>10.1f}{ac:>16.4e}{aj2/ac:>10.1e}{amoon/ac:>10.1e}{asun/ac:>10.1e}{asrp/ac:>10.1e}{adrag/ac:>10.1e}")

# 2) Kepler frente a J2 integrado
a, e, inc = 6778.137e3, 0.01, math.radians(51.6)
raan, argp, M0 = math.radians(40.0), math.radians(30.0), 0.0
r0, v0 = cinematica_kepler(a, e, inc, raan, argp, M0, 0.0)
T = 2 * math.pi * math.sqrt(a ** 3 / MU)
dt = 5.0
print(f"\nOrbita sintetica: a = {a/1e3:.3f} km, e = {e}, i = 51.6 deg; periodo = {T:.1f} s; paso RK4 = {dt} s")

# Comprobacion: RK4 sin J2 reproduce Kepler
rA, vA = integra(r0, v0, 10 * T, dt, False)
rK, _ = cinematica_kepler(a, e, inc, raan, argp, M0, round(10 * T / dt) * dt)
err0 = math.dist(rA, rK)
print(f"Comprobacion sin J2, 10 orbitas: |RK4 - Kepler| = {err0:.2e} m")
assert err0 < 1.0, "RK4 no reproduce Kepler"

print(f"\n{'orbitas':>8}{'t [h]':>9}{'|r_J2 - r_Kepler| [km]':>26}")
r, v = r0, v0
t = 0.0
for k in (1, 5, 15, 30):
    objetivo = k * T
    r, v = integra(r, v, round(objetivo / dt) * dt - t, dt, True)
    t = round(objetivo / dt) * dt
    rk, _ = cinematica_kepler(a, e, inc, raan, argp, M0, t)
    print(f"{k:>8}{t/3600:>9.2f}{math.dist(r, rk)/1e3:>26.3f}")
print("Pruebas superadas.")
