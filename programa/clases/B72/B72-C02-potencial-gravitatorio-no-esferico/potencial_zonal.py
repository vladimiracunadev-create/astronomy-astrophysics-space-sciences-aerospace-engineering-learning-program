#!/usr/bin/env python3
"""B72-C02 — Potencial gravitatorio no esferico.

Potencial zonal U = mu/r [1 - sum Jn (Re/r)^n Pn(sin phi)] y su gradiente analitico,
verificado contra diferencias finitas. Unidades SI; marco fijo a la Tierra con eje z polar.
Solo biblioteca estandar.
"""
import math
import random
import sys

MU = 3.986004e14      # m3/s2 (IAU 2015 B3)
RE = 6378137.0        # m (NSSDC)
J = {2: 1082.63e-6,       # NSSDC
     3: -2.53881e-6,      # WGS-72, Spacetrack Report 3 (Hoots y Roehrich)
     4: -1.65597e-6}      # WGS-72, Spacetrack Report 3


def legendre(n, s):
    """Pn(s) y su derivada dPn/ds por recurrencia (valida tambien en los polos)."""
    p = [1.0, s]
    dp = [0.0, 1.0]
    for k in range(2, n + 1):
        p.append(((2 * k - 1) * s * p[k - 1] - (k - 1) * p[k - 2]) / k)
        dp.append(dp[k - 2] + (2 * k - 1) * p[k - 1])
    return p[n], dp[n]


def potencial(r, terminos):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    s = z / d
    suma = 1.0
    for n in terminos:
        suma -= J[n] * (RE / d) ** n * legendre(n, s)[0]
    return MU / d * suma


def aceleracion(r, terminos):
    """Gradiente analitico del potencial (aceleracion total, incluida la central)."""
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    s = z / d
    a = [-MU * x / d ** 3, -MU * y / d ** 3, -MU * z / d ** 3]
    for n in terminos:
        pn, dpn = legendre(n, s)
        c = MU * J[n] * RE ** n
        # T = c Pn(s) / d^(n+1) ; la aceleracion es -grad(T)
        gr = [-(n + 1) * pn * x / d ** (n + 3), -(n + 1) * pn * y / d ** (n + 3), -(n + 1) * pn * z / d ** (n + 3)]
        gz = [dpn / d ** (n + 2) * (0 - s * x / d), dpn / d ** (n + 2) * (0 - s * y / d), dpn / d ** (n + 2) * (1 - s * z / d)]
        for i in range(3):
            a[i] += -c * (gr[i] + gz[i])
    return a


def gradiente_fd(r, terminos, h=5.0):
    g = []
    for i in range(3):
        rp = list(r); rm = list(r)
        rp[i] += h; rm[i] -= h
        g.append((potencial(rp, terminos) - potencial(rm, terminos)) / (2 * h))
    return g


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Marco fijo a la Tierra, eje z polar. J2 de NSSDC; J3 y J4 de WGS-72 (Spacetrack Report 3)")

# 1) Verificacion del gradiente analitico frente a diferencias finitas
random.seed(72)
peor = 0.0
for _ in range(200):
    d = random.uniform(6.6e6, 4.3e7)
    lat = math.radians(random.uniform(-89, 89)); lon = random.uniform(0, 2 * math.pi)
    r = [d * math.cos(lat) * math.cos(lon), d * math.cos(lat) * math.sin(lon), d * math.sin(lat)]
    a = aceleracion(r, (2, 3, 4)); g = gradiente_fd(r, (2, 3, 4))
    err = math.dist(a, g) / math.hypot(*a)
    peor = max(peor, err)
print(f"Gradiente analitico vs diferencias finitas (200 puntos al azar, semilla 72): error relativo maximo = {peor:.2e}")
assert peor < 1e-6

# 2) Termino J2 cerrado frente al termino general n=2
r = [5.0e6, 3.0e6, 4.5e6]
d = math.sqrt(sum(c * c for c in r))
k = -1.5 * J[2] * MU * RE ** 2 / d ** 5
zz = 5 * r[2] ** 2 / d ** 2
cerrado = [-MU * r[0] / d ** 3 + k * r[0] * (1 - zz), -MU * r[1] / d ** 3 + k * r[1] * (1 - zz), -MU * r[2] / d ** 3 + k * r[2] * (3 - zz)]
gen = aceleracion(r, (2,))
dif = math.dist(cerrado, gen) / math.hypot(*gen)
print(f"J2 en forma cerrada vs general: diferencia relativa = {dif:.2e}")
assert dif < 1e-12

# 3) Tamano de cada armonico por latitud, a 400 km de altitud
print("\nAceleracion de cada armonico relativa a mu/r^2, r = Re + 400 km")
print(f"{'latitud':>8}{'J2':>12}{'J3':>12}{'J4':>12}")
rr = RE + 400e3
for lat in (0, 30, 60, 90):
    s = math.sin(math.radians(lat))
    r = [rr * math.cos(math.radians(lat)), 0.0, rr * s]
    base = aceleracion(r, ())
    fila = []
    for n in (2, 3, 4):
        an = aceleracion(r, (n,))
        fila.append(math.dist(an, base) / (MU / rr ** 2))
    print(f"{lat:>8}{fila[0]:>12.3e}{fila[1]:>12.3e}{fila[2]:>12.3e}")

# 4) Gravedad en la superficie en el ecuador y en el polo, solo atraccion (sin rotacion)
ge = math.hypot(*aceleracion([RE, 0.0, 0.0], (2, 3, 4)))
gp = math.hypot(*aceleracion([0.0, 0.0, 6356752.0], (2, 3, 4)))
print(f"\nAtraccion en el ecuador (r = Re): {ge:.4f} m/s2; en el polo (r = 6356.752 km): {gp:.4f} m/s2")
print("(radio polar 6356.752 km: ILUSTRATIVO, no consultado; sin termino centrifugo)")
print("Pruebas superadas.")
