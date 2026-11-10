#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C18: descenso bajo paracaidas, carga de apertura y aterrizaje propulsado (conceptual).

Datos consultados (2026-11-10): rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet); D = Cd q A (NASA Glenn); g_n = 9.80665 m/s2 (NIST CODATA 2022);
ecuacion de cohete ideal con Isp (NASA Glenn).
ILUSTRATIVOS (sinteticos): capsula de 3000 kg, area de arrastre de paracaidas CdA = 850 m2, despliegue a 5000 m con 80 m/s hacia abajo, viento horizontal constante de 10 m/s,
factor de inflado Cx = 1.3, fraccion de area con 'reefing' 0.15; aterrizaje propulsado desde 100 m/s hacia abajo con T/W = 3 (empuje constante), Isp = 300 s.
Sistema: eje vertical local (positivo hacia abajo para la velocidad de descenso), Tierra plana, g constante, SI; deriva horizontal = viento x tiempo.
Modelo: dv/dt = g - rho(h) CdA v^2/(2 m); v_t(h) = sqrt(2 m g/(rho CdA)); tiempo cuasi-estacionario = (2H/v_t0)(1 - exp(-h0/(2H))); carga de apertura F = Cx q CdA_inicial.
Aterrizaje propulsado: altura de encendido h = v^2/(2(a - g)) con a = T/m (masa constante); integracion RK4 con masa constante y con masa variable.
Segunda via: velocidad de contacto final frente a v_t en el suelo; tiempo numerico frente al cuasi-estacionario; altura analitica de encendido frente a la integracion con masa constante.
Tolerancias: v final frente a v_t(0) 2e-2; tiempo de descenso 5e-2; encendido con masa constante 1e-3.
"""
import math, platform

G, RHO0, H = 9.80665, 1.217, 8500.0
M, CDA, H0, V0, W = 3000.0, 850.0, 5000.0, 80.0, 10.0
CX, REEF = 1.3, 0.15


def rho(h):
    return RHO0 * math.exp(-h / H)


def descenso():
    dt = 0.01
    h, v, t = H0, V0, 0.0
    v_max_post = 0.0
    while h > 0:
        f = lambda hh, vv: (-vv, G - rho(hh) * CDA * vv * vv / (2 * M))
        k1 = f(h, v); k2 = f(h + dt / 2 * k1[0], v + dt / 2 * k1[1]); k3 = f(h + dt / 2 * k2[0], v + dt / 2 * k2[1]); k4 = f(h + dt * k3[0], v + dt * k3[1])
        h += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        v += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        t += dt
    return t, v


def aterrizaje(masa_variable, tw=3.0, v0=100.0, isp=300.0, dt=0.002):
    m0 = M
    f_emp = tw * m0 * G
    a0 = f_emp / m0
    h_enc = v0 ** 2 / (2 * (a0 - G))
    h, v, m, t = h_enc, v0, m0, 0.0
    md = f_emp / (isp * G) if masa_variable else 0.0
    mprop = 0.0
    while v > 0 and h > 0:
        a = lambda mm: G - f_emp / mm
        k1v = a(m); k2v = a(m - md * dt / 2); k4v = a(m - md * dt)
        dv = dt * (k1v + 4 * k2v + k4v) / 6
        h -= dt * (v + 0.5 * dv)
        v += dv
        m -= md * dt
        mprop += md * dt
        t += dt
    return h_enc, h, v, t, mprop


def calcular():
    r = {}
    r["vt0"] = math.sqrt(2 * M * G / (RHO0 * CDA))
    r["vt5"] = math.sqrt(2 * M * G / (rho(H0) * CDA))
    t, v = descenso()
    r["t_num"], r["v_fin"] = t, v
    r["t_cuasi"] = 2 * H / r["vt0"] * (1 - math.exp(-H0 / (2 * H)))
    r["err_v"] = abs(v - r["vt0"]) / r["vt0"]
    r["err_t"] = abs(t - r["t_cuasi"]) / r["t_cuasi"]
    r["deriva"] = W * t
    q_apertura = 0.5 * rho(H0) * V0 ** 2
    r["q_ap"] = q_apertura
    r["F_pleno"] = CX * q_apertura * CDA
    r["F_reef"] = CX * q_apertura * CDA * REEF
    r["g_pleno"], r["g_reef"] = r["F_pleno"] / (M * G), r["F_reef"] / (M * G)
    r["energia_impacto_paracaidas"] = 0.5 * M * v * v
    h_enc, h_fin, v_fin, t_b, mp0 = aterrizaje(False)
    r["h_enc"], r["h_fin_cm"], r["v_fin_cm"], r["t_quema"] = h_enc, h_fin, v_fin, t_b
    r["err_enc"] = abs(h_fin) / h_enc
    _, h_fin2, v_fin2, t_b2, mp = aterrizaje(True)
    r["h_fin_mv"], r["v_fin_mv"], r["mprop"] = h_fin2, v_fin2, mp
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Capsula SINTETICA: m = {M:.0f} kg, CdA = {CDA:.0f} m2, despliegue a {H0:.0f} m con {V0:.0f} m/s hacia abajo, viento {W:.0f} m/s")
    print(f"Velocidad terminal: {r['vt5']:.2f} m/s a {H0:.0f} m y {r['vt0']:.3f} m/s al nivel del suelo")
    print(f"Descenso: t = {r['t_num']:.2f} s (cuasi-estacionario {r['t_cuasi']:.2f} s, error {r['err_t']:.1e}); velocidad de contacto = {r['v_fin']:.3f} m/s (v_t suelo {r['vt0']:.3f}, error {r['err_v']:.1e}); deriva = {r['deriva']:.0f} m")
    print(f"Carga de apertura (q = {r['q_ap']:.0f} Pa, Cx = {CX}): area plena {r['F_pleno']/1e3:.0f} kN = {r['g_pleno']:.1f} g; con reefing {REEF}: {r['F_reef']/1e3:.0f} kN = {r['g_reef']:.2f} g")
    print(f"Energia cinetica de contacto bajo paracaidas = {r['energia_impacto_paracaidas']/1e3:.1f} kJ")
    print(f"Aterrizaje propulsado (T/W = 3, 100 m/s): encendido a {r['h_enc']:.1f} m; masa constante -> altura final {r['h_fin_cm']:.4f} m, velocidad {r['v_fin_cm']:.4f} m/s (error relativo {r['err_enc']:.1e}), t = {r['t_quema']:.2f} s")
    print(f"  con masa variable (Isp 300 s): altura al detenerse = {r['h_fin_mv']:.2f} m, velocidad = {r['v_fin_mv']:.3f} m/s; propelente = {r['mprop']:.1f} kg")
    assert r["err_v"] < 2e-2 and r["err_t"] < 5e-2 and r["err_enc"] < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
