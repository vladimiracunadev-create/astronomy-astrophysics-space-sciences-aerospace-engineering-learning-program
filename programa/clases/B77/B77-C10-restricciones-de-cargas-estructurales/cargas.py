#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C10: cargas axiales y laterales de un ascenso SINTETICO y limitacion por estrangulamiento (throttle).

Datos consultados (2026-11-10): rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet); q = rho V^2/2 y D = Cd q A (NASA Glenn);
g0 = 9.80665 m/s2 (NIST CODATA 2022).
ILUSTRATIVOS (sinteticos): cohete de C09 (m0 = 50 000 kg, mf = 12 000 kg, Isp = 300 s, F0 = 1.2 MN, A = 10 m2, Cd = 0.30), limite de aceleracion axial 4.5 g,
racha lateral de viento w = 10 m/s, factor de seguridad 1.4. Ninguno de estos limites procede de una norma o de un vehiculo real (normas de cargas: no consultadas).
Sistema: eje vertical local (axial), plano horizontal (lateral); alfa = w/v (angulo de ataque inducido por la racha, pequeno); SI.
Modelo: n_ax = (F - D)/(m g0); producto q*alfa ~ 0.5 rho v w (carga lateral por unidad de area y de CN_alfa); estrangulamiento F = min(F0, n_lim g0 m + D).
Segunda via: sin limite, n_ax maximo analitico al agotar propelente ~ (F - D)/(mf g0); con limite, n_ax <= n_lim con tolerancia de 1e-3 g.
Tolerancias: maximo con limite <= 4.5 g + 1e-3; masa final = MF dentro de 1e-6.
"""
import math, platform

G0, RHO0, H = 9.80665, 1.217, 8500.0
M0, MF, ISP, F0, AREA, CD, NLIM, W, FS = 50000.0, 12000.0, 300.0, 1.2e6, 10.0, 0.30, 4.5, 10.0, 1.4


def simula(limite, dt=0.02):
    c = ISP * G0
    s = [0.0, 0.0, M0]
    t = 0.0
    nmax = qmax = qamax = 0.0
    tq = tqa = 0.0

    def emp(h, v, m):
        d = CD * 0.5 * RHO0 * math.exp(-h / H) * v * v * AREA if v > 0 else 0.0
        f = min(F0, NLIM * G0 * m + d) if limite else F0
        return f, d

    def der(x):
        h, v, m = x
        f, d = emp(h, v, m)
        return (v, (f - d) / m - G0, -f / c)
    while s[2] > MF:
        k1 = der(s)
        k2 = der([a + dt / 2 * b for a, b in zip(s, k1)])
        k3 = der([a + dt / 2 * b for a, b in zip(s, k2)])
        k4 = der([a + dt * b for a, b in zip(s, k3)])
        prev = list(s)
        s = [a + dt * (b + 2 * cc + 2 * d + e) / 6 for a, b, cc, d, e in zip(s, k1, k2, k3, k4)]
        if s[2] < MF:  # ajusta el ultimo paso para terminar exactamente en MF
            fr = (prev[2] - MF) / (prev[2] - s[2])
            s = [p + fr * (q - p) for p, q in zip(prev, s)]
            dt_eff = dt * fr
            t += dt_eff
            break
        t += dt
        f, d = emp(*s)
        n = (f - d) / (s[2] * G0)
        q = 0.5 * RHO0 * math.exp(-s[0] / H) * s[1] ** 2
        qa = 0.5 * RHO0 * math.exp(-s[0] / H) * s[1] * W
        if n > nmax: nmax = n
        if q > qmax: qmax, tq = q, t
        if qa > qamax: qamax, tqa = qa, t
    return dict(tb=t, v=s[1], h=s[0], m=s[2], nmax=nmax, qmax=qmax, tq=tq, qamax=qamax, tqa=tqa)


def calcular():
    sin, con = simula(False), simula(True)
    c = ISP * G0
    return dict(sin=sin, con=con, n_ana=F0 / (MF * G0), dv_ideal=c * math.log(M0 / MF), seguridad=NLIM * FS)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cohete SINTETICO de C09 con Cd = {CD}; limite axial ILUSTRATIVO = {NLIM} g; racha lateral w = {W} m/s; factor de seguridad ilustrativo = {FS}")
    print("                  t_b [s]   v_f [m/s]  h_f [km]  n_ax max [g]  q max [kPa] (t)      q*alfa max [kPa*rad] (t)")
    for nom, x in (("sin limite", r["sin"]), ("con limite", r["con"])):
        print(f"{nom:12s}  {x['tb']:8.2f}  {x['v']:9.1f}  {x['h']/1e3:8.2f}  {x['nmax']:10.3f}  {x['qmax']/1e3:8.1f} ({x['tq']:5.1f} s)  {x['qamax']/1e3:8.2f} ({x['tqa']:5.1f} s)")
    print(f"n_ax maximo analitico al agotar propelente sin aire ~ F0/(mf g0) = {r['n_ana']:.3f} g (referencia; con arrastre el simulado es menor)")
    print(f"Carga de diseno ilustrativa = limite x factor de seguridad = {r['seguridad']:.2f} g")
    print(f"Costo del limite: velocidad final {r['sin']['v'] - r['con']['v']:.1f} m/s menor y t_b {r['con']['tb'] - r['sin']['tb']:.1f} s mayor")
    assert r["con"]["nmax"] <= NLIM + 1e-3 and abs(r["con"]["m"] - MF) < 1e-6 * M0
    assert r["sin"]["nmax"] > NLIM
    assert r["con"]["v"] < r["sin"]["v"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
