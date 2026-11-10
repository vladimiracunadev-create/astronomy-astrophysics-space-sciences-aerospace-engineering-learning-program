#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C16: respuesta termica de un escudo (conduccion 1D transitoria con re-radiacion) y recesion conceptual.

Datos consultados (2026-11-10): flujo de remanso de Sutton-Graves y constantes k = 1.7415e-4, sigma = 5.67e-8 (diapositivas TFAWS 2012); rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos, no son de ningun material real): conductividad 0.5 W/(m K), densidad 1500 kg/m3, calor especifico 1200 J/(kg K), espesor 0.03 m,
cara trasera adiabatica, T inicial 300 K, emisividad 0.8, entrada de C15 (v_E = 7800 m/s, 5 grados, beta = 300 kg/m2, R_n = 1 m), energia de ablacion efectiva
Q* = 25 MJ/kg (solo para ilustrar el calculo de recesion).
Sistema: coordenada x desde la superficie hacia el interior, SI; el tiempo cero es la entrada a 120 km.
Modelo: rho c dT/dt = k d2T/dx2 con flujo en x = 0: q_in(t) - eps sigma (T_s^4 - T_0^4), esquema implicito (Euler hacia atras) con 120 nodos, dt = 0.05 s;
la radiacion se evalua con la temperatura del paso anterior.
Segunda via: con flujo constante q0, sin radiacion y losa de 5 cm (gruesa para 10 s), T_s(t) = T_0 + 2 q0 sqrt(alpha t / pi)/k (solido semi-infinito); balance de energia: energia entrante = energia almacenada + re-radiada.
Tolerancias: semi-infinito 5e-3 relativo; balance de energia 1e-3 relativo a la energia entrante.
"""
import math, platform

RHO0, H = 1.217, 8500.0
K_SG, SIGMA, EPS = 1.7415e-4, 5.67e-8, 0.8
VE, GAM, BETA, RN = 7800.0, math.radians(5.0), 300.0, 1.0
KC, RHOM, CP, ESP, T0 = 0.5, 1500.0, 1200.0, 0.03, 300.0
QSTAR = 25e6


def serie_flujo():
    """q_in(t) en W/m2 con t desde 120 km; devuelve (tiempos, flujos) con paso de 0.05 s hasta que v < 0.2 v_E."""
    s = math.sin(GAM)
    K = RHO0 * H / (2 * BETA * s)
    dt = 0.05
    t, h = 0.0, 120e3
    ts, qs = [], []
    while h > 0:
        x = math.exp(-h / H)
        v = VE * math.exp(-K * x)
        if v < 0.2 * VE:
            break
        ts.append(t)
        qs.append(K_SG * math.sqrt(RHO0 * x / RN) * v ** 3)
        h -= v * s * dt
        t += dt
    return ts, qs


def tridiag(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m if i < n - 1 else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def conduccion(flujo, dt, n_pasos, espesor, nodos, rad=True, k=KC):
    """flujo(i) -> W/m2 en el paso i. Devuelve T_s(t), T_trasera(t), energia entrante, almacenada y re-radiada."""
    dx = espesor / (nodos - 1)
    alpha = k / (RHOM * CP)
    r = alpha * dt / dx ** 2
    T = [T0] * nodos
    ts_, tb_ = [T0], [T0]
    e_in = e_rad = 0.0
    for i in range(n_pasos):
        q_in = flujo(i)
        q_rad = EPS * SIGMA * (T[0] ** 4 - T0 ** 4) if rad else 0.0
        e_in += q_in * dt
        e_rad += q_rad * dt
        a = [0.0] * nodos
        b = [1 + 2 * r] * nodos
        c = [-r] * nodos
        d = list(T)
        # nodo 0 (volumen medio): rho c dx/2 dT/dt = k (T1 - T0)/dx + q_neto
        a[0], b[0], c[0] = 0.0, 1 + 2 * r, -2 * r
        d[0] = T[0] + 2 * dt * (q_in - q_rad) / (RHOM * CP * dx)
        # ultimo nodo adiabatico
        a[-1], b[-1], c[-1] = -2 * r, 1 + 2 * r, 0.0
        for j in range(1, nodos - 1):
            a[j], b[j], c[j] = -r, 1 + 2 * r, -r
        T = tridiag(a, b, c, d)
        ts_.append(T[0])
        tb_.append(T[-1])
    alm = sum((T[j] - T0) * RHOM * CP * dx * (0.5 if j in (0, nodos - 1) else 1.0) for j in range(nodos))
    return ts_, tb_, e_in, alm, e_rad


def calcular():
    r = {}
    # verificacion semi-infinito
    q0, dt, tt = 1.0e5, 0.01, 10.0
    n = int(tt / dt)
    ts_, _, _, _, _ = conduccion(lambda i: q0, dt, n, 0.05, 400, rad=False)
    alpha = KC / (RHOM * CP)
    ana = T0 + 2 * q0 * math.sqrt(alpha * tt / math.pi) / KC
    r["semi_num"], r["semi_ana"] = ts_[-1], ana
    r["err_semi"] = abs(ts_[-1] - ana) / (ana - T0)
    # entrada
    tq, qs = serie_flujo()
    dt = 0.05
    n = len(qs)
    ext = n + int(120.0 / dt)  # 120 s adicionales sin flujo
    flujo = lambda i: qs[i] if i < n else 0.0
    res_rad = conduccion(flujo, dt, ext, ESP, 120, rad=True)
    res_sin = conduccion(flujo, dt, ext, ESP, 120, rad=False)
    for nom, rs in (("rad", res_rad), ("sin", res_sin)):
        ts_, tb_, ein, alm, erad = rs
        r[nom] = dict(Ts_max=max(ts_), t_Ts=ts_.index(max(ts_)) * dt, Tb_max=max(tb_), t_Tb=tb_.index(max(tb_)) * dt, e_in=ein, alm=alm, e_rad=erad,
                      bal=abs(ein - alm - erad) / ein, Tb_fin=tb_[-1])
    r["duracion"] = n * dt
    r["q_pico"] = max(qs)
    r["recesion_kg"] = r["rad"]["e_in"] / QSTAR
    r["recesion_mm"] = r["recesion_kg"] / RHOM * 1e3
    r["recesion_frac_neta"] = (r["rad"]["e_in"] - r["rad"]["e_rad"]) / QSTAR
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Verificacion con solido semi-infinito (q0 = 1e5 W/m2, 10 s, sin radiacion): T_s numerica = {r['semi_num']:.3f} K; analitica = {r['semi_ana']:.3f} K; error relativo al salto = {r['err_semi']:.2e}")
    print(f"Escudo SINTETICO: k = {KC} W/(m K), rho = {RHOM:.0f}, cp = {CP:.0f}, espesor {ESP*100:.0f} cm, cara trasera adiabatica; entrada de C15 (duracion con v > 0.2 v_E: {r['duracion']:.1f} s; q_pico = {r['q_pico']/1e4:.1f} W/cm2)")
    for nom, tit in (("rad", "con re-radiacion (eps = 0.8)"), ("sin", "sin re-radiacion")):
        x = r[nom]
        print(f"[{tit}] T_s max = {x['Ts_max']:.0f} K (t = {x['t_Ts']:.1f} s); T trasera max = {x['Tb_max']:.1f} K (t = {x['t_Tb']:.1f} s); energia entrante = {x['e_in']/1e6:.2f} MJ/m2, almacenada = {x['alm']/1e6:.3f}, re-radiada = {x['e_rad']/1e6:.3f}; balance = {x['bal']:.1e}")
    print(f"Recesion conceptual con Q* = {QSTAR/1e6:.0f} MJ/kg (ILUSTRATIVO): energia entrante / Q* = {r['recesion_kg']:.3f} kg/m2 ({r['recesion_mm']:.2f} mm de material de {RHOM:.0f} kg/m3) como cota superior sin re-radiacion ni conduccion")
    assert r["err_semi"] < 5e-3
    assert r["rad"]["bal"] < 1e-3 and r["sin"]["bal"] < 1e-3
    assert r["rad"]["Ts_max"] < r["sin"]["Ts_max"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
