#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C20: simulacion academica completa de una trayectoria de ascenso (plano, dos etapas, rotacion terrestre, Mach, convergencia).

Datos consultados (2026-11-10): radio ecuatorial 6378.137 km, periodo sideral 23.9345 h, rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet);
g0 = 9.80665 m/s2 (NIST CODATA 2022); D = Cd q A (NASA Glenn); ecuacion de cohete ideal (NASA Glenn).
NO CONSULTADO (valor estandar rotulado): mu = 3.986004418e14 m3/s2.
ILUSTRATIVOS (sinteticos, inventados): el vehiculo de C12 (etapa 1: 132 500 kg, 110 000 kg de propelente, 7 000 kg de estructura, 2.2 MN, Isp 300 s; etapa 2: 11 000 kg de
propelente, 1 500 kg de estructura, 3 000 kg de carga, 0.25 MN, Isp 350 s), A = 10 m2, Cd(M) por tramos (0.25 subsonico, pico 0.45 en M = 1.1, 0.30 en M = 3, 0.28 despues),
velocidad del sonido sintetica (340 m/s al suelo, 295 m/s desde 11 km), latitud del sitio 28.5 grados (solo para informar omega R cos(phi)), vertical 10 s, gamma0 = 85 grados, y en la etapa 2 un desvio constante del empuje respecto de la velocidad ajustado por biseccion para que gamma = 0 al agotarse.
Sistema: plano orbital inercial, coordenadas polares (r, theta) con componentes radial v_r y tangencial v_t de la velocidad; Tierra NO rotante y aire en reposo (la rotacion solo se
informa como credito de velocidad, no se simula); SI.
Modelo: r' = v_r; theta' = v_t/r; v_r' = v_t^2/r - mu/r^2 + (F sin(psi) - D_r)/m; v_t' = -v_r v_t/r + (F cos(psi) - D_t)/m; psi = gamma + delta (delta = 0 en la etapa 1).
Perdidas integradas junto al estado: L_g = int (mu/r^2) sin(gamma) dt; L_d = int D_paralelo/m dt; L_s = int F (1 - cos(delta))/m dt; velocidad ganada = |v|_final - |v|_inicial.
Segunda via: identidad contable V_eq-ideal = Delta|v| + L_g + L_d + L_s; convergencia en el paso (RK4, dt = 0.2, 0.1, 0.05 s); energia en el vuelo balistico posterior.
Tolerancias: identidad 1e-6 relativa al Delta_v ideal; diferencias de perigeo y apogeo decrecientes con dt; energia y momento angular en coasting 1e-8.
"""
import math, platform

MU, RE, G0 = 3.986004418e14, 6378137.0, 9.80665
RHO0, H, A = 1.217, 8500.0, 10.0
M1, P1, S1, F1, I1 = 132500.0, 110000.0, 7000.0, 2.2e6, 300.0
P2, S2, PL, F2, I2 = 11000.0, 1500.0, 3000.0, 0.25e6, 350.0
T_VERT, GAMMA0 = 10.0, math.radians(85.0)
PHI, T_SID = math.radians(28.5), 23.9345 * 3600.0
OMEGA = 2 * math.pi / T_SID


def sonido(h):
    return 340.0 - 45.0 * min(h, 11000.0) / 11000.0


def cd_mach(m):
    tabla = [(0.0, 0.25), (0.8, 0.25), (1.1, 0.45), (3.0, 0.30), (10.0, 0.28)]
    for (m0, c0), (m1, c1) in zip(tabla, tabla[1:]):
        if m0 <= m <= m1:
            return c0 + (c1 - c0) * (m - m0) / (m1 - m0)
    return 0.28


def deriv(s, f, mdot, fase, delta, rotacion):
    r, th, vr, vt, m, lg, ld, ls = s
    h = r - RE
    vrel_t = vt - (OMEGA * r * math.cos(PHI) if rotacion else 0.0)
    vrel = math.hypot(vr, vrel_t)
    rho = RHO0 * math.exp(-h / H)
    cd = cd_mach(vrel / sonido(h))
    d = cd * 0.5 * rho * vrel * vrel * A
    dr_, dt_ = (-d * vr / vrel, -d * vrel_t / vrel) if vrel > 1e-9 else (0.0, 0.0)
    v = math.hypot(vr, vt)
    gr = MU / (r * r)
    if fase == "vert":
        psi, dl = math.pi / 2, 0.0
    else:
        gam = math.atan2(vr, vt)
        dl = delta if fase == "s2" else 0.0
        psi = gam + dl
    if fase == "vert" or v < 1e-9:
        gam = math.pi / 2
    else:
        gam = math.atan2(vr, vt)
    dvr = vt * vt / r - gr + (f * math.sin(psi) + dr_) / m
    dvt = -vr * vt / r + (f * math.cos(psi) + dt_) / m
    # D paralelo a la velocidad inercial (positivo = frena)
    dpar = -(dr_ * vr + dt_ * vt) / v / m if v > 1e-9 else 0.0
    return (vr, vt / r, dvr, dvt, -mdot, gr * math.sin(gam), dpar, f * (1 - math.cos(dl)) / m)


def rk4(s, dt, *a):
    k1 = deriv(s, *a)
    k2 = deriv([x + dt / 2 * y for x, y in zip(s, k1)], *a)
    k3 = deriv([x + dt / 2 * y for x, y in zip(s, k2)], *a)
    k4 = deriv([x + dt * y for x, y in zip(s, k3)], *a)
    return [x + dt * (p + 2 * q + 2 * w + e) / 6 for x, p, q, w, e in zip(s, k1, k2, k3, k4)]


def tramo(s, t0, t1, f, mdot, fase, delta, rot, dt, ev):
    t = t0
    while t < t1 - 1e-9:
        paso = min(dt, t1 - t)
        s = rk4(s, paso, f, mdot, fase, delta, rot)
        t += paso
        h = s[0] - RE
        vrel_t = s[3] - (OMEGA * s[0] * math.cos(PHI) if rot else 0.0)
        vrel = math.hypot(s[2], vrel_t)
        q = 0.5 * RHO0 * math.exp(-h / H) * vrel ** 2
        if q > ev["qmax"]:
            ev.update(qmax=q, t_q=t, h_q=h, mach_q=vrel / sonido(h))
        if ev["t_sup"] is None and vrel >= sonido(h):
            ev["t_sup"] = t
    return s, t


def vuelo(delta, dt=0.1, rotacion=False):
    c1, c2 = I1 * G0, I2 * G0
    md1, md2 = F1 / c1, F2 / c2
    tb1, tb2 = P1 / md1, P2 / md2
    vt0 = OMEGA * RE * math.cos(PHI) if rotacion else 0.0
    s = [RE, 0.0, 0.0, vt0, M1, 0.0, 0.0, 0.0]
    ev = dict(qmax=0.0, t_q=0.0, h_q=0.0, mach_q=0.0, t_sup=None)
    s, t = tramo(s, 0.0, T_VERT, F1, md1, "vert", 0.0, rotacion, dt, ev)
    # inclinacion: se fija vr y vt para dar gamma0 con la rapidez actual
    v = math.hypot(s[2], s[3])
    s[2], s[3] = v * math.sin(GAMMA0), v * math.cos(GAMMA0)
    s, t = tramo(s, t, tb1, F1, md1, "s1", 0.0, rotacion, dt, ev)
    t_sep, h_sep, v_sep = t, s[0] - RE, math.hypot(s[2], s[3])
    s[4] -= S1
    s, t2 = tramo(s, 0.0, tb2, F2, md2, "s2", delta, rotacion, dt, ev)
    return dict(s=s, t_sep=t_sep, h_sep=h_sep, v_sep=v_sep, tb=t_sep + tb2, ev=ev, v0=math.hypot(0.0, vt0))


def gamma_final(delta, dt=0.2, rotacion=False):
    s = vuelo(delta, dt, rotacion)["s"]
    return math.atan2(s[2], s[3])


def biseccion(rotacion=False):
    lo, hi = math.radians(-40.0), math.radians(-10.0)
    for _ in range(26):
        mid = 0.5 * (lo + hi)
        if gamma_final(mid, 0.2, rotacion) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def orbita(s):
    r, th, vr, vt = s[0], s[1], s[2], s[3]
    v2 = vr * vr + vt * vt
    eps = 0.5 * v2 - MU / r
    a = -MU / (2 * eps)
    h = r * vt
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU ** 2))
    return a * (1 - e) - RE, a * (1 + e) - RE, e, eps, h


def calcular():
    res = {}
    dl = biseccion(False)
    res["delta"] = math.degrees(dl)
    out = {}
    for dt in (0.2, 0.1, 0.05):
        v = vuelo(dl, dt, False)
        per, apo, e, eps, h = orbita(v["s"])
        out[dt] = dict(v=v, per=per, apo=apo, e=e)
    res["conv"] = out
    base = out[0.05]
    v = base["v"]
    s = v["s"]
    res["base"] = base
    res["h_bo"], res["v_bo"] = s[0] - RE, math.hypot(s[2], s[3])
    res["gam_bo"] = math.degrees(math.atan2(s[2], s[3]))
    res["alcance"] = s[1] * RE / 1e3
    res["m_bo"] = s[4]
    dvi = I1 * G0 * math.log(M1 / (M1 - P1)) + I2 * G0 * math.log((PL + S2 + P2) / (PL + S2))
    res["dv_ideal"] = dvi
    res["dv_ganado"] = res["v_bo"] - v["v0"]
    res["Lg"], res["Ld"], res["Ls"] = s[5], s[6], s[7]
    res["resid"] = abs(dvi - res["dv_ganado"] - s[5] - s[6] - s[7]) / dvi
    res["ev"] = v["ev"]
    res["t_sep"], res["h_sep"], res["v_sep"], res["tb"] = v["t_sep"], v["h_sep"] / 1e3, v["v_sep"], v["tb"]
    res["d_per"] = [abs(out[0.2]["per"] - out[0.1]["per"]), abs(out[0.1]["per"] - out[0.05]["per"])]
    res["d_apo"] = [abs(out[0.2]["apo"] - out[0.1]["apo"]), abs(out[0.1]["apo"] - out[0.05]["apo"])]
    # credito de rotacion (NO simulado): velocidad tangencial de la superficie en el sitio
    res["v_rot"] = OMEGA * RE * math.cos(PHI)
    # conservacion en vuelo balistico
    eps0, h0 = orbita(s)[3], orbita(s)[4]
    x = [s[0] * math.cos(s[1]), s[0] * math.sin(s[1])]
    th = s[1]
    vx = s[2] * math.cos(th) - s[3] * math.sin(th)
    vy = s[2] * math.sin(th) + s[3] * math.cos(th)
    y = [x[0], x[1], vx, vy]
    f = lambda q: (lambda rr: [q[2], q[3], -MU * q[0] / rr ** 3, -MU * q[1] / rr ** 3])(math.hypot(q[0], q[1]))
    for _ in range(5400):
        k1 = f(y); k2 = f([a + 0.5 * b for a, b in zip(y, k1)]); k3 = f([a + 0.5 * b for a, b in zip(y, k2)]); k4 = f([a + b for a, b in zip(y, k3)])
        y = [a + (p + 2 * q + 2 * w + e) / 6 for a, p, q, w, e in zip(y, k1, k2, k3, k4)]
    eps1 = 0.5 * (y[2] ** 2 + y[3] ** 2) - MU / math.hypot(y[0], y[1])
    h1 = y[0] * y[3] - y[1] * y[2]
    res["err_e"], res["err_h"] = abs(eps1 - eps0) / abs(eps0), abs(h1 - h0) / abs(h0)
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    ev, b = r["ev"], r["base"]
    print(f"Vehiculo SINTETICO de C12 con Cd(M), aire en reposo y Tierra NO rotante; desvio del empuje en la etapa 2 (biseccion) = {r['delta']:.4f} grados")
    print(f"Eventos: supersonico a t = {ev['t_sup']:.1f} s; max-q = {ev['qmax']/1e3:.1f} kPa a t = {ev['t_q']:.1f} s, h = {ev['h_q']/1e3:.1f} km, Mach {ev['mach_q']:.2f}; separacion t = {r['t_sep']:.1f} s, h = {r['h_sep']:.1f} km, v = {r['v_sep']:.0f} m/s; agotamiento t = {r['tb']:.1f} s")
    print(f"Agotamiento: h = {r['h_bo']/1e3:.2f} km, v inercial = {r['v_bo']:.1f} m/s, gamma = {r['gam_bo']:.4f} grados, alcance = {r['alcance']:.0f} km, m = {r['m_bo']:.0f} kg; orbita {b['per']/1e3:.1f} x {b['apo']/1e3:.1f} km, e = {b['e']:.4f}")
    print("Presupuesto de velocidad [m/s]:")
    print(f"  Delta_v ideal (cohete)      = {r['dv_ideal']:.2f}")
    print(f"  ganancia de |v| inercial    = {r['dv_ganado']:.2f}")
    print(f"  perdida gravitacional       = {r['Lg']:.2f}")
    print(f"  perdida aerodinamica        = {r['Ld']:.2f}")
    print(f"  perdida por direccion (empuje desviado) = {r['Ls']:.2f}")
    print(f"  residuo de la identidad     = {r['resid']:.1e} (relativo al Delta_v ideal)")
    print("Convergencia en el paso (dt [s]: perigeo / apogeo [km]):")
    for dt, o in r["conv"].items():
        print(f"  dt = {dt:5.2f}: {o['per']/1e3:10.4f} / {o['apo']/1e3:10.4f}")
    print(f"  |cambio| perigeo: 0.2->0.1 = {r['d_per'][0]:.2f} m; 0.1->0.05 = {r['d_per'][1]:.2f} m; apogeo: {r['d_apo'][0]:.2f} m; {r['d_apo'][1]:.2f} m")
    print(f"Rotacion terrestre NO simulada: la velocidad tangencial de la superficie en el sitio seria {r['v_rot']:.1f} m/s (omega R cos(phi)); un lanzamiento hacia el este la aprovecharia solo en parte (no se modela el acimut)")
    print(f"Vuelo balistico posterior: energia {r['err_e']:.1e}; momento angular {r['err_h']:.1e}")
    assert r["resid"] < 1e-6
    assert r["d_per"][1] < r["d_per"][0] and r["d_apo"][1] < r["d_apo"][0]
    assert r["err_e"] < 1e-8 and r["err_h"] < 1e-8
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
