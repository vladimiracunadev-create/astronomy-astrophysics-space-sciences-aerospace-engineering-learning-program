#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C12: perfil de ascenso orbital (giro de gravedad) de un lanzador SINTETICO de dos etapas.

Datos consultados (2026-11-10): radio ecuatorial 6378.137 km, rho0 = 1.217 kg/m3, H = 8.5 km (NASA/NSSDC Earth Fact Sheet); g0 = 9.80665 m/s2 (NIST CODATA 2022);
D = Cd q A (NASA Glenn).
NO CONSULTADO en esta sesion (valor estandar rotulado): mu = 3.986004418e14 m3/s2.
ILUSTRATIVOS (sinteticos): etapa 1: masa de despegue 132 500 kg, propelente 110 000 kg, estructura 7 000 kg, F = 2.2 MN, Isp = 300 s;
etapa 2: propelente 11 000 kg, estructura 1 500 kg, carga util 3 000 kg, F = 0.25 MN, Isp = 350 s; A = 10 m2, Cd = 0.3; vertical durante 10 s,
luego un giro de gravedad en la etapa 1 (empuje alineado con la velocidad, gamma0 = 85 grados al terminar la fase vertical) y, en la etapa 2, un empuje desviado un angulo
constante delta respecto de la velocidad (delta negativo = empuje por debajo de la velocidad), ajustado por biseccion para que gamma = 0 al agotar la etapa 2.
Sistema: plano orbital, Tierra esferica NO rotante, coordenadas polares (r, theta); v inercial = v relativa (sin rotacion); SI; gamma = angulo sobre el horizonte local.
Modelo: r' = v sin g; theta' = v cos g / r; v' = (F - D)/m - mu sin g / r^2; g' = -(mu/r^2 - v^2/r) cos g / v (giro de gravedad). RK4, dt = 0.05 s.
Segunda via: tras el agotamiento se propaga el vuelo balistico con RK4 (cartesianas) y se verifican la energia y el momento angular; ademas
perigeo y apogeo por vis-viva frente a los extremos de r en la propagacion.
Tolerancias: energia y momento angular en el vuelo balistico 1e-8 relativos; perigeo/apogeo 1e-4 relativos.
"""
import math, platform

MU, RE, G0 = 3.986004418e14, 6378137.0, 9.80665
RHO0, H, CD, A = 1.217, 8500.0, 0.3, 10.0
M1, P1, S1, F1, I1 = 132500.0, 110000.0, 7000.0, 2.2e6, 300.0
P2, S2, PL, F2, I2 = 11000.0, 1500.0, 3000.0, 0.25e6, 350.0
T_VERT = 10.0
GAMMA0 = 85.0
DELTA = 0.0  # desvio del empuje respecto de la velocidad en la etapa 2 [rad]


def deriv(s, f, mdot, tipo):
    r, th, v, g, m = s
    h = r - RE
    d = CD * 0.5 * RHO0 * math.exp(-h / H) * v * v * A
    gr = MU / (r * r)
    if tipo == "vert":
        return (v, 0.0, (f - d) / m - gr, 0.0, -mdot)
    dl = DELTA if tipo == "s2" else 0.0
    return (v * math.sin(g), v * math.cos(g) / r, (f * math.cos(dl) - d) / m - gr * math.sin(g), (f * math.sin(dl) / m - (gr - v * v / r) * math.cos(g)) / v, -mdot)


def rk4(s, dt, f, mdot, tipo):
    k1 = deriv(s, f, mdot, tipo)
    k2 = deriv([a + dt / 2 * b for a, b in zip(s, k1)], f, mdot, tipo)
    k3 = deriv([a + dt / 2 * b for a, b in zip(s, k2)], f, mdot, tipo)
    k4 = deriv([a + dt * b for a, b in zip(s, k3)], f, mdot, tipo)
    return [a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def tramo(s, t_ini, t_fin, f, mdot, tipo, dt, qmax, registro, traza):
    """Integra de t_ini a t_fin con pasos <= dt (el ultimo se recorta)."""
    t = t_ini
    n = 0
    while t < t_fin - 1e-9:
        paso = min(dt, t_fin - t)
        s = rk4(s, paso, f, mdot, tipo)
        t += paso
        n += 1
        qmax = max(qmax, 0.5 * RHO0 * math.exp(-(s[0] - RE) / H) * s[2] ** 2)
        if traza and n % 200 == 0:
            registro.append((t, s[0] - RE, s[2], math.degrees(s[3])))
    return s, t, qmax


def ascenso(gamma0_deg, dt=0.05, traza=False):
    c1, c2 = I1 * G0, I2 * G0
    md1, md2 = F1 / c1, F2 / c2
    tb1, tb2 = P1 / md1, P2 / md2
    s = [RE, 0.0, 0.0, math.pi / 2, M1]
    registro, qmax = [], 0.0
    s, t, qmax = tramo(s, 0.0, T_VERT, F1, md1, "vert", dt, qmax, registro, False)
    s[3] = math.radians(gamma0_deg)
    s, t, qmax = tramo(s, t, tb1, F1, md1, "gt", dt, qmax, registro, traza)
    s[4] -= S1  # descarte de la estructura de la etapa 1
    s_sep, t_sep = list(s), t
    s, t2, qmax = tramo(s, 0.0, tb2, F2, md2, "s2", dt, qmax, [], False)
    return dict(s=s, s_sep=s_sep, t_sep=t_sep, tb1=tb1, tb2=tb2, qmax=qmax, registro=registro)


def elementos(r, v, g):
    h = r * v * math.cos(g)
    e_esp = 0.5 * v * v - MU / r
    a = -MU / (2 * e_esp) if e_esp < 0 else float("inf")
    ecc = math.sqrt(max(0.0, 1 + 2 * e_esp * h * h / MU ** 2))
    return h, e_esp, a, ecc, a * (1 - ecc), a * (1 + ecc)


def biseccion():
    """Ajusta el desvio DELTA del empuje de la etapa 2 para que gamma = 0 al agotarse."""
    global DELTA
    lo, hi = math.radians(-30.0), math.radians(-15.0)  # gamma_final crece cuando DELTA crece
    for _ in range(30):
        DELTA = 0.5 * (lo + hi)
        if ascenso(GAMMA0, dt=0.1)["s"][3] > 0.0:
            hi = DELTA
        else:
            lo = DELTA
    DELTA = 0.5 * (lo + hi)
    return DELTA


def coasting(s0, n_t=6000, dt=1.0):
    r, th, v, g, m = s0
    x = [r * math.cos(th), r * math.sin(th), v * (math.sin(g) * math.cos(th) - math.cos(g) * math.sin(th)), v * (math.sin(g) * math.sin(th) + math.cos(g) * math.cos(th))]

    def f(y):
        rr = math.hypot(y[0], y[1])
        k = -MU / rr ** 3
        return [y[2], y[3], k * y[0], k * y[1]]
    rmin = rmax = math.hypot(x[0], x[1])
    e0 = 0.5 * (x[2] ** 2 + x[3] ** 2) - MU / rmin
    h0 = x[0] * x[3] - x[1] * x[2]
    for _ in range(n_t):
        k1 = f(x)
        k2 = f([a + dt / 2 * b for a, b in zip(x, k1)])
        k3 = f([a + dt / 2 * b for a, b in zip(x, k2)])
        k4 = f([a + dt * b for a, b in zip(x, k3)])
        x = [a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(x, k1, k2, k3, k4)]
        rr = math.hypot(x[0], x[1])
        rmin, rmax = min(rmin, rr), max(rmax, rr)
    e1 = 0.5 * (x[2] ** 2 + x[3] ** 2) - MU / math.hypot(x[0], x[1])
    h1 = x[0] * x[3] - x[1] * x[2]
    return rmin, rmax, abs(e1 - e0) / abs(e0), abs(h1 - h0) / abs(h0)


def calcular():
    dl = biseccion()
    a = ascenso(GAMMA0, traza=True)
    r, th, v, g, m = a["s"]
    h, e, sm, ecc, rp, ra = elementos(r, v, g)
    rm, rM, ee, eh = coasting(a["s"])
    res = dict(gamma0=GAMMA0, delta=math.degrees(dl), h_bo=r - RE, v_bo=v, g_bo=math.degrees(g), m_bo=m, downrange=th * RE / 1e3, a=sm, ecc=ecc,
               perigeo=rp - RE, apogeo=ra - RE, qmax=a["qmax"], t_sep=a["t_sep"], tb2=a["tb2"], tb_total=a["t_sep"] + a["tb2"],
               h_sep=a["s_sep"][0] - RE, v_sep=a["s_sep"][2], g_sep=math.degrees(a["s_sep"][3]),
               rmin_prop=rm - RE, rmax_prop=rM - RE, err_e=ee, err_h=eh, reg=a["registro"], v_circ=math.sqrt(MU / r),
               dv_ideal=I1 * G0 * math.log(M1 / (M1 - P1)) + I2 * G0 * math.log((PL + S2 + P2) / (PL + S2)))
    res["err_peri"] = abs(res["rmin_prop"] - res["perigeo"]) / rp
    res["err_apo"] = abs(res["rmax_prop"] - res["apogeo"]) / ra
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Lanzador SINTETICO de dos etapas; Delta_v ideal total = {r['dv_ideal']:.1f} m/s; vertical {T_VERT:.0f} s; gamma0 = {r['gamma0']:.1f} grados; desvio del empuje en la etapa 2 (biseccion) delta = {r['delta']:.4f} grados")
    print("  t [s]   h [km]   v [m/s]  gamma [grados]")
    for t, h, v, g in r["reg"]:
        print(f"  {t:6.1f}  {h/1e3:7.2f}  {v:8.1f}  {g:8.3f}")
    print(f"Separacion de etapas: t = {r['t_sep']:.1f} s, h = {r['h_sep']/1e3:.1f} km, v = {r['v_sep']:.1f} m/s, gamma = {r['g_sep']:.2f} grados")
    print(f"Agotamiento (t = {r['tb_total']:.1f} s): h = {r['h_bo']/1e3:.2f} km, v = {r['v_bo']:.1f} m/s (circular a esa altitud: {r['v_circ']:.1f}), gamma = {r['g_bo']:.4f} grados, alcance = {r['downrange']:.0f} km, m = {r['m_bo']:.0f} kg")
    print(f"Presion dinamica maxima = {r['qmax']/1e3:.1f} kPa")
    print(f"Orbita resultante (vis-viva): perigeo = {r['perigeo']/1e3:.1f} km, apogeo = {r['apogeo']/1e3:.1f} km, e = {r['ecc']:.4f}")
    print(f"Propagacion balistica: r minimo/maximo = {r['rmin_prop']/1e3:.1f} / {r['rmax_prop']/1e3:.1f} km; errores relativos: perigeo {r['err_peri']:.1e}, apogeo {r['err_apo']:.1e}, energia {r['err_e']:.1e}, momento angular {r['err_h']:.1e}")
    assert r["err_e"] < 1e-8 and r["err_h"] < 1e-8
    assert r["err_peri"] < 1e-4 and r["err_apo"] < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
