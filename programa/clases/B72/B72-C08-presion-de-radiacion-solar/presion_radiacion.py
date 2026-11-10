#!/usr/bin/env python3
"""B72-C08 — Presion de radiacion solar.

Presion S/c, aceleracion Cr (A/m) S/c, sombra cilindrica y crecimiento de la excentricidad
en una orbita geoestacionaria SINTETICA con direccion solar fija (verificacion de la teoria
de primer orden). Unidades SI; marco inercial geocentrico. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
C = 299792458.0              # m/s (NIST, exacta)
LSUN = 3.828e26              # W (NSSDC)
AU = 149.598e9               # m (NSSDC, semieje mayor de la Tierra)
AU_MARTE = 227.956e9         # m (NSSDC)
S0 = LSUN / (4 * math.pi * AU ** 2)
DIA = 86400.0


def sombra_numerica(r, paso=0.0005):
    """Fraccion de orbita circular (beta = 0) dentro de la sombra cilindrica, contando muestras."""
    en = 0; N = int(2 * math.pi / paso)
    for k in range(N):
        th = k * paso
        x, y = r * math.cos(th), r * math.sin(th)    # Sol en +x
        if x < 0 and abs(y) < RE:
            en += 1
    return en / N


def e_vec(r, v):
    d = math.sqrt(sum(c * c for c in r)); rv = sum(r[i] * v[i] for i in range(3)); vv = sum(c * c for c in v)
    return [((vv - MU / d) * r[i] - rv * v[i]) / MU for i in range(3)]


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print(f"S0 = L/(4 pi UA^2) = {S0:.2f} W/m2 (derivada de la luminosidad y de la distancia media); P0 = S0/c = {S0 / C * 1e6:.3f} micro-Pa")
Sm = LSUN / (4 * math.pi * AU_MARTE ** 2)
print(f"A la distancia media de Marte: S = {Sm:.1f} W/m2 (cociente {Sm / S0:.3f} = (UA/UA_Marte)^2 = {(AU / AU_MARTE) ** 2:.3f})")
assert abs(Sm / S0 - (AU / AU_MARTE) ** 2) < 1e-12

print("\nAceleracion por presion de radiacion, Cr = 1.3 (ILUSTRATIVO), a 1 UA")
print(f"{'objeto (A/m ILUSTRATIVO)':<34}{'A/m [m2/kg]':>13}{'a [m/s2]':>14}")
for nombre, am in (("satelite macizo", 0.005), ("satelite con paneles", 0.02), ("panel ligero", 0.2), ("vela solar", 1.0)):
    print(f"{nombre:<34}{am:>13.3f}{1.3 * am * S0 / C:>14.3e}")

print("\nSombra cilindrica (beta = 0): fraccion de la orbita y duracion")
print(f"{'orbita':<8}{'r [km]':>10}{'fraccion analitica':>20}{'fraccion numerica':>19}{'duracion [min]':>16}")
for nombre, r in (("LEO", RE + 400e3), ("GEO", 42164e3)):
    ana = math.asin(RE / r) / math.pi
    num = sombra_numerica(r)
    T = 2 * math.pi * math.sqrt(r ** 3 / MU)
    print(f"{nombre:<8}{r / 1e3:>10.1f}{ana:>20.4f}{num:>19.4f}{ana * T / 60:>16.1f}")
    assert abs(ana - num) < 1e-3

# Excentricidad forzada: orbita GEO circular, direccion solar fija +x en el plano, solo SRP
a = 42164e3
n = math.sqrt(MU / a ** 3)
am, cr = 0.02, 1.3
asrp = cr * am * S0 / C
dt = 60.0
dias = 20
r = [0.0, a, 0.0]
v = [-math.sqrt(MU / a), 0.0, 0.0]


# El Sol esta en +x: la presion empuja al satelite en la direccion Sol -> satelite, es decir -x.
def acel(r):
    d = math.sqrt(sum(c * c for c in r))
    return [-MU * r[0] / d ** 3 - asrp, -MU * r[1] / d ** 3, -MU * r[2] / d ** 3]


def rk4(r, v, dt):
    k1r, k1v = v, acel(r)
    r2 = [r[i] + 0.5 * dt * k1r[i] for i in range(3)]; v2 = [v[i] + 0.5 * dt * k1v[i] for i in range(3)]
    k2r, k2v = v2, acel(r2)
    r3 = [r[i] + 0.5 * dt * k2r[i] for i in range(3)]; v3 = [v[i] + 0.5 * dt * k2v[i] for i in range(3)]
    k3r, k3v = v3, acel(r3)
    r4 = [r[i] + dt * k3r[i] for i in range(3)]; v4 = [v[i] + dt * k3v[i] for i in range(3)]
    k4r, k4v = v4, acel(r4)
    return ([r[i] + dt / 6 * (k1r[i] + 2 * k2r[i] + 2 * k3r[i] + k4r[i]) for i in range(3)],
            [v[i] + dt / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i]) for i in range(3)])


pasos = int(dias * DIA / dt)
print(f"\nGEO sintetica, A/m = {am}, Cr = {cr}: a_SRP = {asrp:.3e} m/s2 ; Sol fijo en +x ; {dias} dias, RK4 paso {dt:.0f} s")
print(f"{'dias':>6}{'|e| numerica':>16}{'|e| teoria 1.5 a_SRP t/(n a)':>32}")
for k in range(1, pasos + 1):
    r, v = rk4(r, v, dt)
    if k % int(5 * DIA / dt) == 0:
        t = k * dt
        e_num = math.hypot(*e_vec(r, v))
        e_teo = 1.5 * asrp / (n * a) * t
        print(f"{t / DIA:>6.0f}{e_num:>16.3e}{e_teo:>32.3e}")
assert abs(e_num - e_teo) / e_teo < 0.03
print("Pruebas superadas.")
