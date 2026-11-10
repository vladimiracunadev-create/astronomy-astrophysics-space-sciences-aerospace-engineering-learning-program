#!/usr/bin/env python3
"""B72-C07 — Modelos de densidad atmosferica.

Modelo hidrostatico ILUSTRATIVO de la termosfera (perfil de temperatura tipo Bates, masa media
decreciente) integrado numericamente y verificado contra la solucion analitica isoterma.
NO es un modelo operativo (no es NRLMSISE ni JB2008) y las cifras no son densidades medidas.
Unidades SI. Solo biblioteca estandar.
"""
import math
import sys

K = 1.380649e-23            # J/K (NIST CODATA 2022, exacta)
U = 1.66053906892e-27       # kg (NIST CODATA 2022)
MU = 3.986004e14
RE = 6378137.0
Z0 = 120e3                  # m, base ILUSTRATIVA
RHO0 = 2.2e-8               # kg/m3 a 120 km, ILUSTRATIVA (no consultada)
T0 = 360.0                  # K a 120 km, ILUSTRATIVA


def g(z):
    return MU / (RE + z) ** 2


def masa_media(z):
    """Masa media (kg) ILUSTRATIVA: 28 u en 120 km -> 16 u hacia 800 km (interpolacion suave)."""
    f = min(max((z - 120e3) / 680e3, 0.0), 1.0)
    return (28.0 - 12.0 * f) * U


def temperatura(z, tinf, s=0.025e-3):
    return tinf - (tinf - T0) * math.exp(-s * (z - Z0))


def densidad(zfin, tinf, masa=masa_media, temp=temperatura, dz=250.0):
    """Integra d ln(rho)/dz = -(m g/(k T) + dT/dz /T) con RK4 de 250 m."""
    def f(z, lnr):
        h = 1.0
        dT = (temp(z + h, tinf) - temp(z - h, tinf)) / (2 * h)
        T = temp(z, tinf)
        return -(masa(z) * g(z) / (K * T) + dT / T)
    z = Z0; lnr = math.log(RHO0)
    n = int(round((zfin - Z0) / dz))
    for _ in range(n):
        k1 = f(z, lnr); k2 = f(z + dz / 2, lnr + dz / 2 * k1)
        k3 = f(z + dz / 2, lnr + dz / 2 * k2); k4 = f(z + dz, lnr + dz * k3)
        lnr += dz / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        z += dz
    return math.exp(lnr)


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Modelo ILUSTRATIVO: rho(120 km) = 2.2e-8 kg/m3, T(120 km) = 360 K, masa media 28 -> 16 u. No es un modelo operativo.")

# Verificacion: perfil isotermo y masa constante, con g constante -> exponencial analitica
def temp_iso(z, tinf):
    return 800.0
masa_cte = lambda z: 20.0 * U
g_real = g
# se compara con la solucion analitica ln(rho) = ln(rho0) - integral m g/(kT) dz
# integral exacta con g = mu/(Re+z)^2: m mu/(k T) * (1/(Re+z) - 1/(Re+Z0))
def analitica(zfin):
    return RHO0 * math.exp(20.0 * U * MU / (K * 800.0) * (1.0 / (RE + zfin) - 1.0 / (RE + Z0)))
num = densidad(400e3, 0.0, masa_cte, temp_iso)
ana = analitica(400e3)
err = abs(num - ana) / ana
print(f"\nVerificacion isoterma (800 K, 20 u): rho(400 km) numerica = {num:.6e} ; analitica = {ana:.6e} ; dif. relativa = {err:.2e}")
assert err < 1e-9

print("\nDensidad [kg/m3] segun la temperatura exosferica (temperaturas ILUSTRATIVAS, no asociadas a un indice solar medido)")
alts = (200, 300, 400, 500, 600, 800)
print(f"{'T_inf [K]':>10}" + "".join(f"{str(z) + ' km':>12}" for z in alts))
res = {}
for tinf in (700.0, 1000.0, 1400.0):
    fila = [densidad(z * 1e3, tinf) for z in alts]
    res[tinf] = fila
    print(f"{tinf:>10.0f}" + "".join(f"{x:>12.2e}" for x in fila))

print("\nCociente 1400 K / 700 K por altitud")
for k, z in enumerate(alts):
    print(f"  {z} km: {res[1400.0][k] / res[700.0][k]:.1f}")

zs = 400e3
T4 = temperatura(zs, 1000.0)
H = K * T4 / (masa_media(zs) * g(zs))
print(f"\nAltura de escala a 400 km con T_inf = 1000 K: T = {T4:.0f} K ; H = k T/(m g) = {H/1e3:.1f} km")
assert res[1400.0][2] > res[700.0][2] > 0
print("Pruebas superadas.")
