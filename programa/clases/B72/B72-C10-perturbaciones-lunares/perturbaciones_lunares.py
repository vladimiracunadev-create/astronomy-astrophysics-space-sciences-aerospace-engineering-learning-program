#!/usr/bin/env python3
"""B72-C10 — Perturbaciones lunares.

Comparacion de la marea lunar y solar (mu/d^3), verificacion numerica de la precesion del polo
orbital por la Luna y deriva de inclinacion de una orbita geoestacionaria SINTETICA por Sol y Luna.
La Luna se modela en orbita circular de radio 384 400 km con inclinacion media 23.44 deg al ecuador
(SIMPLIFICACION: se ignora la variacion de +-5.145 deg y la regresion de 18.6 anos).
Unidades SI; marco inercial del ecuador de la fecha. Solo biblioteca estandar.
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

N_LUNA = 2 * math.pi / T_LUNA

print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
cs = MU_SOL / AU ** 3
cl = MU_LUNA / D_LUNA ** 3
print(f"mu/d^3 Sol = {cs:.4e} s^-2 ; Luna = {cl:.4e} s^-2 ; cociente Luna/Sol = {cl / cs:.3f}")
print(f"Movimiento medio lunar (periodo sideral 27.3217 d) = {N_LUNA:.4e} rad/s")

print("\nVerificacion numerica (RK4, paso 600 s, 180 dias): solo Luna, a = 60000 km, i = 40 deg, e = 0")
a, i = 60000e3, math.radians(40.0)
dO_n, di_n = integra_nodo(a, i, MU_LUNA, D_LUNA, N_LUNA, 180, 600.0)
dO_f, di_f, _ = tasas_vectoriales(a, i, MU_LUNA, D_LUNA)
dt_s = 180 * DIA
print(f"  dOmega: numerico = {math.degrees(dO_n):.4f} deg ; formula = {math.degrees(dO_f * dt_s):.4f} deg")
print(f"  giro del polo: numerico = {math.degrees(di_n):.5f} deg ; formula = {math.degrees(di_f * dt_s):.5f} deg")
err = abs(dO_n - dO_f * dt_s) / abs(dO_f * dt_s)
print(f"  diferencia relativa de dOmega = {err:.2%}")
assert err < 0.08

print("\nDeriva de la inclinacion (giro del polo) de una orbita circular geoestacionaria, i0 = 0.5 deg")
a = 42164e3
por_ano = 365.25 * DIA * 180 / math.pi
_, ds, _ = tasas_vectoriales(a, math.radians(0.5), MU_SOL, AU)
_, dl, _ = tasas_vectoriales(a, math.radians(0.5), MU_LUNA, D_LUNA)
print(f"  Sol : |dh/dt| = {ds * por_ano:.3f} deg/ano")
print(f"  Luna: |dh/dt| = {dl * por_ano:.3f} deg/ano  (plano lunar a 23.44 deg: valor MEDIO simplificado)")
print(f"  Suma: {(ds + dl) * por_ano:.3f} deg/ano")
print("  La amplitud real de la parte lunar varia con el ciclo de 18.6 anos: no se modela aqui.")
print("Pruebas superadas.")
