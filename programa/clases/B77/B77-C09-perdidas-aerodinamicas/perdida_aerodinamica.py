#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C09: perdidas aerodinamicas en un ascenso vertical SINTETICO.

Datos consultados (2026-11-10): rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet); D = Cd (rho V^2/2) A (NASA Glenn, Drag Coefficient);
ecuacion de cohete ideal con gravedad (NASA Glenn); g0 = 9.80665 m/s2 (NIST CODATA 2022).
ILUSTRATIVOS (sinteticos): m0 = 50 000 kg, masa final 12 000 kg, Isp = 300 s (constante), empuje 1.2 MN (T/W0 = 2.45), A = 10 m2, Cd = 0.15, 0.30, 0.60 (constantes).
Sistema: eje vertical local, Tierra plana (g = g0 constante), altitud sobre el suelo, SI.
Modelo: dv/dt = (F - D)/m - g ; dm/dt = -F/(Isp g0); D = Cd 0.5 rho(h) v^2 A. Se integran tambien L_g = int g dt y L_d = int D/m dt (RK4, dt = 0.01 s).
Segunda via (identidad contable): c ln(m0/mf) = v_f + L_g + L_d (exacta salvo error de integracion).
Tolerancias: residuo de la identidad < 1e-8 relativo al Delta_v ideal; sin arrastre (Cd = 0) la velocidad final es c ln(MR) - g t_b con 1e-8.
"""
import math, platform

G0, RHO0, H = 9.80665, 1.217, 8500.0
M0, MF, ISP, F, AREA = 50000.0, 12000.0, 300.0, 1.2e6, 10.0


def simula(cd, dt=0.01):
    c = ISP * G0
    mdot = F / c
    tb = (M0 - MF) / mdot
    n = int(round(tb / dt))
    dt = tb / n
    # estado: h, v, Lg, Ld; m(t) = M0 - mdot t es conocido
    def f(t, s):
        h, v, lg, ld = s
        m = M0 - mdot * t
        d = cd * 0.5 * RHO0 * math.exp(-h / H) * v * v * AREA if v > 0 else 0.0
        return (v, (F - d) / m - G0, G0, d / m)
    s, t = (0.0, 0.0, 0.0, 0.0), 0.0
    qmax = 0.0
    for _ in range(n):
        k1 = f(t, s)
        k2 = f(t + dt / 2, tuple(a + dt / 2 * b for a, b in zip(s, k1)))
        k3 = f(t + dt / 2, tuple(a + dt / 2 * b for a, b in zip(s, k2)))
        k4 = f(t + dt, tuple(a + dt * b for a, b in zip(s, k3)))
        s = tuple(a + dt * (b + 2 * cc + 2 * d + e) / 6 for a, b, cc, d, e in zip(s, k1, k2, k3, k4))
        t += dt
        qmax = max(qmax, 0.5 * RHO0 * math.exp(-s[0] / H) * s[1] ** 2)
    h, v, lg, ld = s
    dvi = c * math.log(M0 / MF)
    return dict(cd=cd, tb=tb, h=h, v=v, lg=lg, ld=ld, dvi=dvi, resid=abs(dvi - v - lg - ld) / dvi, qmax=qmax)


def calcular():
    r = {"casos": [simula(cd) for cd in (0.0, 0.15, 0.30, 0.60)]}
    c0 = r["casos"][0]
    r["v_sin_aire_ana"] = ISP * G0 * math.log(M0 / MF) - G0 * c0["tb"]
    r["err_sin_aire"] = abs(c0["v"] - r["v_sin_aire_ana"]) / r["v_sin_aire_ana"]
    r["resid_max"] = max(x["resid"] for x in r["casos"])
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    c0 = r["casos"][0]
    print(f"Cohete SINTETICO: m0 = {M0:.0f} kg, mf = {MF:.0f} kg, Isp = {ISP} s, F = {F/1e6} MN, A = {AREA} m2; DV ideal = {c0['dvi']:.1f} m/s; t_b = {c0['tb']:.2f} s")
    print("  Cd    v_final [m/s]  h_final [km]  perd.grav [m/s]  perd.aero [m/s]  q_max [kPa]  residuo identidad")
    for x in r["casos"]:
        print(f" {x['cd']:5.2f}  {x['v']:11.2f}  {x['h']/1e3:11.2f}  {x['lg']:13.2f}  {x['ld']:14.2f}  {x['qmax']/1e3:10.1f}  {x['resid']:.1e}")
    print(f"Sin aire: v numerica = {c0['v']:.4f}; analitica c ln(MR) - g t_b = {r['v_sin_aire_ana']:.4f}; error relativo = {r['err_sin_aire']:.1e}")
    assert r["resid_max"] < 1e-8 and r["err_sin_aire"] < 1e-8
    assert r["casos"][3]["ld"] > r["casos"][1]["ld"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
