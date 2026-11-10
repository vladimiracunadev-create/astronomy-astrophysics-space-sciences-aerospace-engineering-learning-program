#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C02: movimiento vertical de un cuerpo en una atmosfera exponencial.

Datos consultados (2026-11-10): rho0 = 1.217 kg/m3 y altura de escala H = 8.5 km (NASA/NSSDC Earth Fact Sheet);
g_n = 9.80665 m/s2 (NIST CODATA 2022); definicion de arrastre D = Cd (rho V^2/2) A (NASA Glenn).
ILUSTRATIVOS (sinteticos): masa 100 kg, Cd = 0.3, A = 0.05 m2 (beta = m/(Cd A) = 6666.7 kg/m2), velocidad inicial 300 m/s hacia arriba.
Sistema: eje vertical local (Tierra plana, g constante), unidades SI, altitud sobre el suelo.
Modelo: dv/dt = -g - sgn(v) (rho(h) Cd A /(2 m)) v^2, dh/dt = v, RK4 con paso fijo.
Segunda via: con densidad constante la velocidad de caida tiene solucion analitica v = -vt tanh(g t/vt), vt = sqrt(2 m g/(rho Cd A)).
Tolerancias: RK4 frente a analitica 1e-6 relativa; sin arrastre el apogeo es v0^2/(2g) con 1e-5 (paso de 1 ms).
"""
import math, platform

G, RHO0, H = 9.80665, 1.217, 8500.0
M, CD, A, V0 = 100.0, 0.3, 0.05, 300.0


def rho(h, const=False):
    return RHO0 if const else RHO0 * math.exp(-h / H)


def deriv(s, const, cd_a_m):
    h, v = s
    return (v, -G - math.copysign(1.0, v) * 0.5 * rho(h, const) * cd_a_m * v * v)


def rk4(s, dt, const, k):
    def f(x):
        return deriv(x, const, k)
    k1 = f(s)
    k2 = f((s[0] + 0.5 * dt * k1[0], s[1] + 0.5 * dt * k1[1]))
    k3 = f((s[0] + 0.5 * dt * k2[0], s[1] + 0.5 * dt * k2[1]))
    k4 = f((s[0] + dt * k3[0], s[1] + dt * k3[1]))
    return (s[0] + dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6, s[1] + dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)


def vuelo(h0, v0, const=False, k=CD * A / M, dt=0.001, tmax=400.0):
    s, t, apogeo, t_ap = (h0, v0), 0.0, h0, 0.0
    while t < tmax:
        s = rk4(s, dt, const, k)
        t += dt
        if s[0] > apogeo:
            apogeo, t_ap = s[0], t
        if s[0] <= 0.0 and t > 1.0:
            break
    return apogeo, t_ap, t, s[1]


def calcular():
    r = {}
    r["vt0"] = math.sqrt(2 * M * G / (RHO0 * CD * A))
    # caida con densidad constante frente a la solucion analitica
    s, t, dt = (1.0e9, 0.0), 0.0, 0.001
    for _ in range(int(20.0 / dt)):
        s = rk4(s, dt, True, CD * A / M)
        t += dt
    r["v_num"] = s[1]
    r["v_ana"] = -r["vt0"] * math.tanh(G * t / r["vt0"])
    r["err_tanh"] = abs(s[1] - r["v_ana"]) / abs(r["v_ana"])
    # apogeo sin arrastre y con arrastre
    ap0, tap0, _, _ = vuelo(0.0, V0, k=0.0)
    r["ap_vacio"], r["ap_vacio_ana"] = ap0, V0 ** 2 / (2 * G)
    ap, tap, tt, vimp = vuelo(0.0, V0)
    r["ap_atm"], r["t_ap"], r["t_vuelo"], r["v_impacto"] = ap, tap, tt, vimp
    r["vt_nivel_mar"] = r["vt0"]
    r["beta"] = M / (CD * A)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cuerpo SINTETICO: m = {M} kg, Cd = {CD}, A = {A} m2, beta = {r['beta']:.1f} kg/m2, v0 = {V0} m/s (vertical)")
    print(f"Velocidad terminal a nivel del mar (rho = {RHO0} kg/m3): {r['vt0']:.3f} m/s")
    print(f"Caida a densidad constante, t = 20 s: v numerica = {r['v_num']:.6f}; analitica = {r['v_ana']:.6f}; error relativo = {r['err_tanh']:.2e}")
    print(f"Apogeo sin arrastre: {r['ap_vacio']:.3f} m (analitico {r['ap_vacio_ana']:.3f} m)")
    print(f"Apogeo en atmosfera exponencial: {r['ap_atm']:.1f} m en t = {r['t_ap']:.2f} s; vuelo total {r['t_vuelo']:.2f} s; velocidad de retorno {r['v_impacto']:.2f} m/s")
    assert r["err_tanh"] < 1e-6
    assert abs(r["ap_vacio"] - r["ap_vacio_ana"]) / r["ap_vacio_ana"] < 1e-5
    assert r["ap_atm"] < r["ap_vacio"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
