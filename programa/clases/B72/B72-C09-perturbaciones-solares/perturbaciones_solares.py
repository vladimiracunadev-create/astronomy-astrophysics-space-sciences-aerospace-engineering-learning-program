#!/usr/bin/env python3
"""B72-C09 — Perturbaciones solares.

Marea gravitatoria del Sol sobre un satelite: aceleracion exacta frente a la aproximacion
cuadrupolar 2 mu r/d^3, y precesion del polo orbital por el Sol (formula vectorial promediada)
frente a una integracion RK4 con el Sol en orbita circular inclinada 23.44 deg al ecuador.
Orbitas SINTETICAS. Unidades SI; marco inercial del ecuador de la fecha. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14           # m3/s2 (IAU 2015)
RE = 6378137.0             # m (NSSDC)
MU_SOL = 1.3271244e20      # m3/s2 (IAU 2015)
MU_LUNA = 4902.800e9       # m3/s2 (JPL SSD)
AU = 149.598e9             # m (NSSDC)
D_LUNA = 0.3844e9          # m (NSSDC)
T_LUNA = 27.3217 * 86400.0 # s, periodo sideral (NSSDC)
EPS = math.radians(23.44)  # oblicuidad (NSSDC); plano del perturbador respecto al ecuador
DIA = 86400.0


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def pos_pert(t, dist, n_p, eps=EPS):
    th = n_p * t
    return [dist * math.cos(th), dist * math.sin(th) * math.cos(eps), dist * math.sin(th) * math.sin(eps)]


def acel(r, t, mu_p, dist, n_p):
    d = pos_pert(t, dist, n_p)
    dm = math.sqrt(sum(c * c for c in d)); rr = math.sqrt(sum(c * c for c in r))
    q = [d[i] - r[i] for i in range(3)]; qm = math.sqrt(sum(c * c for c in q))
    return [-MU * r[i] / rr ** 3 + mu_p * (q[i] / qm ** 3 - d[i] / dm ** 3) for i in range(3)]


def rk4(r, v, t, dt, mu_p, dist, n_p):
    a1 = acel(r, t, mu_p, dist, n_p)
    r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
    a2 = acel(r2, t + dt / 2, mu_p, dist, n_p)
    r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
    a3 = acel(r3, t + dt / 2, mu_p, dist, n_p)
    r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
    a4 = acel(r4, t + dt, mu_p, dist, n_p)
    return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
            [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])


def nodo_incl(r, v):
    h = cross(r, v)
    return math.atan2(h[0], -h[1]), math.acos(h[2] / math.sqrt(sum(c * c for c in h)))


def tasas_vectoriales(a, inc, mu_p, dist, eps=EPS):
    """Tasas (dOmega/dt, |dh/dt|, kappa cos gamma) en rad/s de un polo orbital circular que precesa por la
    marea de un perturbador circular, promediada sobre ambas orbitas: dh/dt = kappa cos(gamma) (h x h_p),
    con Omega = 0 inicial."""
    n = math.sqrt(MU / a ** 3)
    kappa = 0.75 * mu_p / (dist ** 3 * n)
    h = [0.0, -math.sin(inc), math.cos(inc)]
    hp = [0.0, -math.sin(eps), math.cos(eps)]
    cg = sum(h[i] * hp[i] for i in range(3))
    dh = [kappa * cg * c for c in cross(h, hp)]
    dOm = dh[0] / math.sin(inc)
    return dOm, math.sqrt(sum(c * c for c in dh)), kappa * cg


def integra_nodo(a, inc, mu_p, dist, n_p, dias, dt):
    n = math.sqrt(MU / a ** 3)
    r = [a, 0.0, 0.0]; v = [0.0, n * a * math.cos(inc), n * a * math.sin(inc)]
    O0, i0 = nodo_incl(r, v)
    t = 0.0
    for _ in range(int(dias * DIA / dt)):
        r, v = rk4(r, v, t, dt, mu_p, dist, n_p)
        t += dt
    O1, i1 = nodo_incl(r, v)
    h0 = [0.0, -math.sin(inc), math.cos(inc)]
    h1 = cross(r, v); m = math.sqrt(sum(c * c for c in h1)); h1 = [c / m for c in h1]
    giro = math.acos(max(-1.0, min(1.0, sum(h0[k] * h1[k] for k in range(3)))))
    return ((O1 - O0 + math.pi) % (2 * math.pi) - math.pi), giro

N_SOL = math.sqrt(MU_SOL / AU ** 3)

print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Sol en orbita circular de radio 1 UA inclinada 23.44 deg al ecuador (modelo SIMPLIFICADO; satelite SINTETICO)")

print("\nMarea solar: aceleracion maxima (sobre la linea Sol-Tierra) exacta vs 2 mu r/d^3")
print(f"{'orbita':<12}{'r [km]':>10}{'exacta [m/s2]':>16}{'2 mu r/d^3':>14}{'dif. relativa':>15}")
for nombre, r in (("LEO", RE + 400e3), ("GPS", 26560e3), ("GEO", 42164e3), ("60000 km", 60000e3)):
    ex = MU_SOL * (1.0 / (AU - r) ** 2 - 1.0 / AU ** 2)
    ap = 2 * MU_SOL * r / AU ** 3
    print(f"{nombre:<12}{r / 1e3:>10.1f}{ex:>16.4e}{ap:>14.4e}{abs(ex - ap) / ap:>15.2e}")

print("\nPrecesion del polo orbital por el Sol (formula vectorial): dOmega/dt, |dh/dt| (giro del polo)")
print(f"{'a [km]':>9}{'i [deg]':>9}{'dOm [deg/ano]':>15}{'|dh/dt| [deg/ano]':>19}{'periodo del polo [anos]':>25}")
for a_km, i in ((26560.0, 55.0), (42164.0, 0.5), (42164.0, 10.0), (60000.0, 40.0)):
    dO, di, kc = tasas_vectoriales(a_km * 1e3, math.radians(i), MU_SOL, AU)
    por_ano = 365.25 * DIA * 180 / math.pi
    print(f"{a_km:>9.0f}{i:>9.1f}{dO * por_ano:>15.4f}{di * por_ano:>19.4f}{2 * math.pi / abs(kc) / (365.25 * DIA):>25.1f}")

print("\nVerificacion numerica (RK4, paso 600 s, 180 dias): a = 60000 km, i = 40 deg, e = 0")
a, i = 60000e3, math.radians(40.0)
dO_n, di_n = integra_nodo(a, i, MU_SOL, AU, N_SOL, 180, 600.0)
dO_f, di_f, _ = tasas_vectoriales(a, i, MU_SOL, AU)
dt_s = 180 * DIA
print(f"  dOmega: numerico = {math.degrees(dO_n):.4f} deg ; formula = {math.degrees(dO_f * dt_s):.4f} deg")
print(f"  giro del polo: numerico = {math.degrees(di_n):.5f} deg ; formula = {math.degrees(di_f * dt_s):.5f} deg")
err = abs(dO_n - dO_f * dt_s) / abs(dO_f * dt_s)
print(f"  diferencia relativa de dOmega = {err:.2%}")
assert err < 0.05
print("Pruebas superadas.")
