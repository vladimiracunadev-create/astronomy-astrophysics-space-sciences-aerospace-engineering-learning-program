#!/usr/bin/env python3
"""B72-C17 — Efectos relativistas orbitales.

Avance relativista del periapsis por orbita, Delta_omega = 6 pi GM / (c^2 a (1-e^2)), para Mercurio y para
satelites terrestres SINTETICOS, y verificacion con una integracion RK4 de la aceleracion post-newtoniana
de Schwarzschild (con y sin el termino relativista, para restar el error del integrador).
Unidades SI. Solo biblioteca estandar.
"""
import math
import sys

C = 299792458.0            # m/s (NIST, exacta)
GM_SOL = 1.3271244e20      # m3/s2 (IAU 2015)
GM_TIERRA = 3.986004e14    # m3/s2 (IAU 2015)
A_MERCURIO = 57.909e9      # m (NSSDC)
E_MERCURIO = 0.2056        # NSSDC
T_MERCURIO = 87.969 * 86400.0   # s (NSSDC)
ARCSEC = 180.0 / math.pi * 3600.0
SIGLO = 100 * 365.25 * 86400.0
ANO = 365.25 * 86400.0


def avance(gm, a, e):
    return 6 * math.pi * gm / (C ** 2 * a * (1 - e * e))


def acel(r, v, gm, gr):
    d = math.sqrt(sum(c * c for c in r))
    a = [-gm * r[i] / d ** 3 for i in range(3)]
    if gr:
        v2 = sum(c * c for c in v); rv = sum(r[i] * v[i] for i in range(3))
        k = gm / (C ** 2 * d ** 3)
        for i in range(3):
            a[i] += k * ((4 * gm / d - v2) * r[i] + 4 * rv * v[i])
    return a


def rk4(r, v, dt, gm, gr):
    a1 = acel(r, v, gm, gr)
    r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
    a2 = acel(r2, v2, gm, gr)
    r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
    a3 = acel(r3, v3, gm, gr)
    r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
    a4 = acel(r4, v4, gm, gr)
    return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
            [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])


def angulo_perihelio(r, v, gm):
    d = math.sqrt(sum(c * c for c in r)); vv = sum(c * c for c in v); rv = sum(r[i] * v[i] for i in range(3))
    ev = [((vv - gm / d) * r[i] - rv * v[i]) / gm for i in range(3)]
    return math.atan2(ev[1], ev[0])


def corrida(gr, norb, pasos_orbita):
    a, e, gm = A_MERCURIO, E_MERCURIO, GM_SOL
    rp = a * (1 - e)
    r = [rp, 0.0, 0.0]; v = [0.0, math.sqrt(gm * (1 + e) / rp), 0.0]
    T = 2 * math.pi * math.sqrt(a ** 3 / gm)
    dt = T / pasos_orbita
    ang = [angulo_perihelio(r, v, gm)]
    for _ in range(norb):
        for _ in range(pasos_orbita):
            r, v = rk4(r, v, dt, gm, gr)
        ang.append(angulo_perihelio(r, v, gm))
    # desenrollado
    out = [ang[0]]
    for x in ang[1:]:
        d = x - out[-1]; d -= 2 * math.pi * round(d / (2 * math.pi)); out.append(out[-1] + d)
    return out, T


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Aceleracion post-newtoniana de Schwarzschild para una particula de prueba (sin Lense-Thirring ni geodesica)")

# 1) Mercurio: formula
d_orb = avance(GM_SOL, A_MERCURIO, E_MERCURIO)
n_orb_siglo = SIGLO / T_MERCURIO
print(f"\nMercurio (a = 57.909e9 m, e = 0.2056, T = 87.969 d): avance por orbita = {d_orb:.4e} rad = {d_orb * ARCSEC:.5f} arcsec")
print(f"  orbitas por siglo = {n_orb_siglo:.2f} ; avance = {d_orb * n_orb_siglo * ARCSEC:.2f} arcsec/siglo")
print("  Valor moderno del avance anomalo citado por Will (2014): 43 arcsec/siglo")
assert abs(d_orb * n_orb_siglo * ARCSEC - 43.0) < 0.5

# 2) Verificacion numerica
norb = 12
con, T = corrida(True, norb, 2500)
sin, _ = corrida(False, norb, 2500)
pend = [(con[k] - sin[k]) for k in range(norb + 1)]
num = (pend[-1] - pend[0]) / norb
print(f"\nIntegracion RK4 de {norb} orbitas (2500 pasos por orbita), con y sin termino relativista:")
print(f"  avance por orbita: numerico = {num:.4e} rad ; formula = {d_orb:.4e} rad ; dif. relativa = {abs(num - d_orb) / d_orb:.2%}")
assert abs(num - d_orb) / d_orb < 0.03

# 3) Satelites terrestres SINTETICOS (precesion secular = 3 GM n / (c^2 a (1-e^2)))
print("\nSatelites terrestres SINTETICOS: avance relativista del perigeo")
print(f"{'caso':<22}{'a [km]':>10}{'e':>8}{'[arcsec/ano]':>16}{'[mas/ano]':>14}")
for nombre, a, e in (("baja 500 km", 6878.137e3, 0.001), ("GPS", 26560e3, 0.01), ("GEO", 42164e3, 0.001), ("Molniya", 26600e3, 0.74)):
    n = math.sqrt(GM_TIERRA / a ** 3)
    w = 3 * GM_TIERRA * n / (C ** 2 * a * (1 - e * e))
    print(f"{nombre:<22}{a / 1e3:>10.1f}{e:>8.3f}{w * ANO * ARCSEC:>16.4f}{w * ANO * ARCSEC * 1e3:>14.1f}")
print("Lense-Thirring y precesion geodesica: NO calculadas ni consultadas en esta clase.")
print("Pruebas superadas.")
