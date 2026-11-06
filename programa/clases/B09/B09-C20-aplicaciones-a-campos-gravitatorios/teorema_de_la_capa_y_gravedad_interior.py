#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C20: campos gravitatorios por integración.

Datos (PUBLICADOS): (GM)_Tierra nominal = 3.986004e14 m3/s2 (IAU 2015 B3,
arXiv:1510.07674); J2 = 1.08263e-3, a_E = 6378137 m, omega = 7.292115e-5 rad/s y
1/f = 298.257222101 (IERS Conventions 2010, TN36, tablas 1.1-1.2, GRS80);
g_n = 9.80665 m/s2 (CODATA 2022, NIST); masa 5.9722e24 kg, radio medio
6371.000 km, I/(M R^2) = 0.3308 (NASA/NSSDC, Earth Fact Sheet, 2024-11-15).
Núcleo de 3500 km: SINTÉTICO (como en B09-C18). Densidades de las capas: ESTIMADAS
por ajuste a M e I (no un modelo sísmico).
Modelos: (1) teorema de la capa: Phi(r) = -(G M_s/2) int_0^pi sin(t) dt / s(t),
s = sqrt(r^2 + a^2 - 2 r a cos t), integral simple obtenida al integrar en phi;
(2) g(r) = GM M(<r)/(M r^2) para dos capas; (3) J2 y rotación:
g_r = GM/r^2 [1 - 3 J2 (a/r)^2 P2(sin phi)] - omega^2 r cos^2(phi) (cos phi sólo en el ecuador).
Supuestos: simetría esférica en (1) y (2); campo axisimétrico en (3). Validez: ilustrativa.
Tolerancias: capa: 1e-6 relativa (Simpson n = 2000); (2) continuidad de g en r_c a 1e-9.
"""
from __future__ import annotations
import math, platform, sys

GM = 3.986004e14
J2, A_E, OMEGA, INV_F = 1.08263e-3, 6378137.0, 7.292115e-5, 298.257222101
G_N = 9.80665
M_T, R_T, K = 5.9722e24, 6.371e6, 0.3308
RC = 3.5e6


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    return s * h / 3


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def phi_capa(r, a, GMs):
    return -(GMs / 2) * simpson(lambda t: math.sin(t) / math.sqrt(r * r + a * a - 2 * r * a * math.cos(t)), 0.0, math.pi)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # 1) teorema de la capa
    a = 1.0e7
    print("1) Capa delgada uniforme de radio a = 1e7 m, GM_s = (GM)_E:")
    for r in (0.25 * a, 0.5 * a, 0.9 * a, 1.1 * a, 2.0 * a, 5.0 * a):
        num = phi_capa(r, a, GM)
        esp = -GM / a if r < a else -GM / r
        prueba(abs(num / esp - 1) < 1e-6, f"capa en r = {r/a} a")
        print(f"   r = {r/a:4.2f} a: Phi numérico = {num:.6e};  esperado ({'-GM/a' if r < a else '-GM/r'}) = {esp:.6e} J/kg")
    # 2) gravedad interior: dos capas
    a11, a12 = 4 * math.pi / 3 * RC**3, 4 * math.pi / 3 * (R_T**3 - RC**3)
    a21, a22 = 8 * math.pi / 15 * RC**5, 8 * math.pi / 15 * (R_T**5 - RC**5)
    b1, b2 = M_T, K * M_T * R_T**2
    det = a11 * a22 - a12 * a21
    rho_c, rho_m = (b1 * a22 - a12 * b2) / det, (a11 * b2 - a21 * b1) / det
    def masa_dentro(r):
        if r <= RC:
            return 4 * math.pi / 3 * rho_c * r**3
        return 4 * math.pi / 3 * (rho_c * RC**3 + rho_m * (r**3 - RC**3))
    g_int = lambda r: GM * (masa_dentro(r) / M_T) / r**2
    print(f"\n2) Dos capas (núcleo {RC/1e3:.0f} km): rho_c = {rho_c:.0f}, rho_m = {rho_m:.0f} kg/m3 (estimadas)")
    print("   r [km]      M(<r)/M      g(r) [m/s2]")
    for r in (1.0e6, 2.0e6, 3.5e6, 4.5e6, 5.5e6, R_T):
        print(f"   {r/1e3:7.0f}   {masa_dentro(r)/M_T:9.5f}   {g_int(r):9.4f}")
    prueba(abs(masa_dentro(RC * (1 + 1e-12)) / masa_dentro(RC * (1 - 1e-12)) - 1) < 1e-9, "M(<r) continua")
    prueba(abs(g_int(R_T) - GM / R_T**2) < 1e-9 * GM / R_T**2, "g(R) = GM/R^2")
    g_max_r = max((g_int(r), r) for r in [1e5 * i for i in range(1, 64)])
    print(f"   máximo de g en el modelo: {g_max_r[0]:.4f} m/s2 a r = {g_max_r[1]/1e3:.0f} km (cerca del límite núcleo-manto)")
    g_uniforme = lambda r: GM * r / R_T**3
    print(f"   esfera uniforme: g(R/2) = {g_uniforme(R_T/2):.4f} m/s2 (= g(R)/2 = {GM/R_T**2/2:.4f})")
    # 3) J2 y rotación
    f = 1 / INV_F
    c = A_E * (1 - f)
    P2 = lambda s: 0.5 * (3 * s * s - 1)
    g_eq = GM / A_E**2 * (1 - 3 * J2 * P2(0.0)) - OMEGA**2 * A_E
    g_pol = GM / c**2 * (1 - 3 * J2 * (A_E / c) ** 2 * P2(1.0))
    print(f"\n3) Modelo con J2 y rotación: radio polar c = {c:.1f} m")
    print(f"   g_ecuador = {g_eq:.4f} m/s2;  g_polo = {g_pol:.4f} m/s2;  diferencia = {g_pol-g_eq:.4f} m/s2")
    print(f"   g_n = {G_N} m/s2 queda entre ambas: {g_eq < G_N < g_pol}")
    prueba(g_eq < G_N < g_pol, "g_n entre ecuador y polo")
    print(f"   aceleración centrífuga en el ecuador = {OMEGA**2*A_E:.5f} m/s2 ({OMEGA**2*A_E/ (GM/A_E**2):.4%} de GM/a^2)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
