# SPDX-License-Identifier: Apache-2.0
"""B85-C12: entorno de vacío: camino libre medio, Knudsen, bombeo con desgasificación y criterio de masa perdida.

Consultado: K_B (SI exacto). ILUSTRATIVO y NO CONSULTADO: presiones por altitud (órdenes de magnitud), diámetro molecular,
volumen y velocidad de bombeo, tasa de desgasificación, criterio TML/CVCM y materiales sintéticos.
Segunda vía: integración numérica (RK4) de la ecuación de bombeo frente a la solución analítica.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

D_MOL = 3.7e-10
# presion aproximada por altitud: ORDEN DE MAGNITUD ILUSTRATIVO (no consultado)
PRES_ALT = [(0, 101325.0), (100, 3.2e-2), (200, 1.0e-4), (400, 1.0e-5), (800, 1.0e-7)]
V_CAM, S_BOMBA = 2.0, 0.5            # m3, m3/s
Q_ESP, A_SUP = 2e-6, 20.0            # Pa m3/(s m2), m2
P0 = 101325.0


def camino_libre(p, t=300.0):
    return K_B * t / (math.sqrt(2) * math.pi * D_MOL ** 2 * p)


def p_ultima():
    return Q_ESP * A_SUP / S_BOMBA


def p_t(t):
    pu = p_ultima()
    return pu + (P0 - pu) * math.exp(-S_BOMBA * t / V_CAM)


def t_hasta(p_obj):
    pu = p_ultima()
    return -(V_CAM / S_BOMBA) * math.log((p_obj - pu) / (P0 - pu))


def rk4(t_fin, n=20000):
    pu_q = Q_ESP * A_SUP
    f = lambda p: -S_BOMBA / V_CAM * p + pu_q / V_CAM
    h = t_fin / n
    p = P0
    for _ in range(n):
        k1 = f(p); k2 = f(p + 0.5 * h * k1); k3 = f(p + 0.5 * h * k2); k4 = f(p + h * k3)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return p


def aceptable(tml, cvcm):
    """Criterio ILUSTRATIVO de masa perdida total y condensables (no consultado): TML <= 1.0 %, CVCM <= 0.10 %."""
    return tml <= 1.0 and cvcm <= 0.10


def calcular():
    r = {"filas": []}
    for h, p in PRES_ALT:
        lam = camino_libre(p)
        r["filas"].append((h, p, lam, lam / 1.0))
    r["p_u"] = p_ultima()
    r["t_1e2"] = t_hasta(1e2)
    r["t_1e_3"] = t_hasta(1e-3)
    r["t_1e_2"] = t_hasta(1e-2)
    r["p_rk4"] = rk4(r["t_1e_3"])
    r["t_const_bomba"] = V_CAM / S_BOMBA
    r["materiales"] = [("A (sintetico)", 0.45, 0.02), ("B (sintetico)", 1.40, 0.05), ("C (sintetico)", 0.80, 0.15)]
    r["veredictos"] = [(n, t, c_, aceptable(t, c_)) for n, t, c_ in r["materiales"]]
    r["p_u_doble"] = Q_ESP * A_SUP * 2 / S_BOMBA
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Camino libre medio (aire ILUSTRATIVO, T = 300 K, d = {D_MOL*1e9:.2f} nm) y Knudsen para L = 1 m; presiones por altitud: ORDEN DE MAGNITUD no consultado")
    print(f"{'h [km]':>8}{'p [Pa]':>12}{'lambda [m]':>14}{'Kn=lambda/L':>14}")
    for h, p, lam, kn in r["filas"]:
        print(f"{h:>8}{p:>12.2e}{lam:>14.3e}{kn:>14.3e}")
    print(f"Camara ILUSTRATIVA: V = {V_CAM} m3, S = {S_BOMBA} m3/s, desgasificacion = {Q_ESP:.0e} Pa m3/(s m2) sobre {A_SUP:.0f} m2")
    print(f"Presion limite = Q/S = {r['p_u']:.2e} Pa ; constante de tiempo V/S = {r['t_const_bomba']:.1f} s")
    print(f"Tiempo hasta 1e2 Pa = {r['t_1e2']:.1f} s ; hasta 1e-2 Pa = {r['t_1e_2']:.1f} s ; hasta 1e-3 Pa = {r['t_1e_3']:.1f} s")
    print(f"p(t_1e-3) por RK4 = {r['p_rk4']:.6e} Pa (objetivo 1e-3)")
    print(f"Con desgasificacion doble la presion limite sube a {r['p_u_doble']:.2e} Pa")
    for n, t, c_, ok in r["veredictos"]:
        print(f"  Material {n}: TML = {t:.2f} %, CVCM = {c_:.2f} % -> {'cumple' if ok else 'no cumple'} el criterio ilustrativo")
    comprobar(abs(r["p_rk4"] - 1e-3) / 1e-3 < 1e-5, "RK4 frente a analitica")
    comprobar(r["t_1e_3"] > r["t_1e_2"] > r["t_1e2"], "orden de tiempos")
    fin()


if __name__ == "__main__":
    main()
