# SPDX-License-Identifier: Apache-2.0
"""B85-C03: convección natural y su desaparición con la presión y la gravedad; coeficiente radiativo equivalente.

Consultado: SIGMA (NIST). ILUSTRATIVO: propiedades del aire a 300 K y 1 atm, geometría, ΔT, ε.
Relaciones estándar (no consultadas en una fuente concreta): Rayleigh, Ra_crit = 1708 (capa horizontal), Nu = 0.59 Ra^(1/4).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

P0 = 101325.0
T0 = 300.0
NU0, AL0, K_AIRE, CP, R_AIRE = 1.6e-5, 2.2e-5, 0.026, 1005.0, 287.0   # ilustrativos
L, DT, EPS = 0.10, 20.0, 0.80
D_MOL = 3.7e-10  # m, diametro molecular ilustrativo
RA_CRIT = 1708.0


def propiedades(p):
    """A T fija: rho ~ p; mu constante => nu ~ 1/p; alpha = k/(rho cp) ~ 1/p."""
    rho0 = P0 / (R_AIRE * T0)
    rho = p / (R_AIRE * T0)
    mu = NU0 * rho0
    nu = mu / rho
    alpha = K_AIRE / (rho * CP)
    return rho, nu, alpha


def rayleigh(p, g):
    _, nu, alpha = propiedades(p)
    return g * (1.0 / T0) * DT * L ** 3 / (nu * alpha)


def h_conv(p, g):
    ra = rayleigh(p, g)
    nu_n = max(1.0, 0.59 * ra ** 0.25) if ra > RA_CRIT else 1.0
    return nu_n * K_AIRE / L, ra, nu_n


def h_rad(t_medio, eps=EPS):
    return 4 * eps * SIGMA * t_medio ** 3


def camino_libre(p, t=T0):
    return K_B * t / (math.sqrt(2) * math.pi * D_MOL ** 2 * p)


def calcular():
    r = {}
    r["ra_tierra"] = rayleigh(P0, G_E)
    r["h_tierra"], _, r["nu_tierra"] = h_conv(P0, G_E)
    r["ra_micro"] = rayleigh(P0, 1e-6 * G_E)
    r["h_micro"] = h_conv(P0, 1e-6 * G_E)[0]
    r["h_rad"] = h_rad(T0)
    q_exacto = EPS * SIGMA * ((T0 + DT / 2) ** 4 - (T0 - DT / 2) ** 4)
    r["h_rad_exacto"] = q_exacto / DT
    r["p_crit"] = biseccion(lambda p: rayleigh(p, G_E) - RA_CRIT, 1.0, P0)
    r["lambda_crit"] = camino_libre(r["p_crit"])
    r["lambda_1atm"] = camino_libre(P0)
    r["lambda_1e5"] = camino_libre(1e-5 * 100.0)  # 1e-5 mbar = 1e-3 Pa
    r["cociente_p2"] = rayleigh(P0 / 10, G_E) / r["ra_tierra"]
    r["g_marte"] = 3.73
    r["ra_marte"] = rayleigh(P0, 3.73)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Aire ILUSTRATIVO a {T0:.0f} K: nu = {NU0:.1e} m2/s, alpha = {AL0:.1e} m2/s (a 1 atm); placa L = {L} m, DT = {DT:.0f} K, eps = {EPS}")
    print(f"Ra (1 atm, g = 9.82) = {r['ra_tierra']:.3e} ; Nu = {r['nu_tierra']:.2f} ; h_conv = {r['h_tierra']:.2f} W/(m2 K)")
    print(f"Ra (1 atm, g = 1e-6 g) = {r['ra_micro']:.3e} ; h_conv = {r['h_micro']:.2f} W/(m2 K) (solo conduccion)")
    print(f"h_rad = 4 eps sigma T^3 = {r['h_rad']:.3f} W/(m2 K) ; exacto = {r['h_rad_exacto']:.3f} W/(m2 K)")
    print(f"Ra(p/10)/Ra(p) = {r['cociente_p2']:.4f} (esperado 0.01 = (1/10)^2)")
    print(f"Presion con Ra = 1708: {r['p_crit']:.1f} Pa = {r['p_crit']/100:.2f} mbar")
    print(f"Camino libre medio: 1 atm {r['lambda_1atm']*1e9:.1f} nm ; a p_crit {r['lambda_crit']*1e6:.2f} um ; a 1e-3 Pa {r['lambda_1e5']:.2f} m")
    print(f"Ra en Marte (g = 3.73, 1 atm) = {r['ra_marte']:.3e}")
    comprobar(abs(r["cociente_p2"] - 0.01) < 1e-12, "Ra ~ p^2")
    comprobar(abs(rayleigh(r["p_crit"], G_E) - RA_CRIT) < 1e-6, "p_crit")
    comprobar(abs(r["h_rad"] - r["h_rad_exacto"]) / r["h_rad_exacto"] < 1e-2, "linealizacion radiativa")
    fin()


if __name__ == "__main__":
    main()
