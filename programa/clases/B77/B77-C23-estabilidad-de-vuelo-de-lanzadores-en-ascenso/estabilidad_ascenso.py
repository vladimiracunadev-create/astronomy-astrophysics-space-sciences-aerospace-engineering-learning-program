#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C23: estabilidad de cabeceo de un lanzador SINTETICO aerodinamicamente inestable durante el ascenso.

Datos consultados (2026-11-10): criterio de estabilidad de la NASA Glenn (Rocket Stability): estable si el centro de presion esta detras del centro de gravedad; si esta delante, el par
es desestabilizador y un pequeno desplazamiento de la nariz tiende a crecer. q = rho V^2/2 (NASA Glenn, Drag Coefficient).
SINTETICOS / ILUSTRATIVOS (inventados): condicion cercana a max-q: q = 35 kPa, V = 400 m/s, area de referencia S = 1.767 m2 (d = 1.5 m), CN_alfa = 3.0 /rad, centro de presion 1.5 m DELANTE
del centro de gravedad (l = 1.5 m), I_y = 3.0e5 kg m2, empuje 800 kN con brazo de la tobera 8 m, racha lateral w = 20 m/s, limite de la tobera 5 grados. Coeficientes congelados.
Sistema: plano de cabeceo; theta = actitud respecto de la direccion de vuelo (suposicion de trayectoria fija en el intervalo corto); alfa = theta + w/V; delta = deflexion de la tobera; SI, rad.
Modelo: theta'' = mu_a alfa + mu_c delta, con mu_a = q S CN_alfa l/I_y (>0: inestable) y mu_c = T lt/I_y; control PD: delta = -Kp theta - Kd theta'.
Segunda via: raices de s^2 - mu_a = 0 (lazo abierto) y de s^2 + mu_c Kd s + (mu_c Kp - mu_a) = 0 (lazo cerrado); estado estacionario ante racha: alfa/alfa_w = mu_c Kp/(mu_c Kp - mu_a).
Tolerancias: tiempo de duplicacion asintotico 1e-3 relativo; estado estacionario 1e-3 relativo.
"""
import math, platform

Q, V, S, CNA, L, IY, T, LT, W, DELTA_MAX = 35000.0, 400.0, 1.767, 3.0, 1.5, 3.0e5, 800e3, 8.0, 20.0, math.radians(5.0)
MU_A = Q * S * CNA * L / IY
MU_C = T * LT / IY
ALFA_W = W / V


def rk4_lineal(f, y, dt, n):
    out = [(0.0, y[0])]
    t = 0.0
    for _ in range(n):
        k1 = f(t, y); k2 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(y, k1)]); k3 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(y, k2)]); k4 = f(t + dt, [a + dt * b for a, b in zip(y, k3)])
        y = [a + dt * (p + 2 * q + 2 * w + e) / 6 for a, p, q, w, e in zip(y, k1, k2, k3, k4)]
        t += dt
        out.append((t, y[0]))
    return out


def calcular():
    r = {}
    r["mu_a"], r["mu_c"] = MU_A, MU_C
    r["lam"] = math.sqrt(MU_A)
    r["t2_ana"] = math.log(2) / r["lam"]
    a0 = math.radians(0.5)
    reg = rk4_lineal(lambda t, y: [y[1], MU_A * y[0]], [a0, 0.0], 0.002, int(10.0 / 0.002))
    d5 = next(x for t, x in reg if t >= 5.0)
    d8 = next(x for t, x in reg if t >= 8.0)
    tasa = math.log(d8 / d5) / 3.0
    r["tasa_num"], r["t2_num"] = tasa, math.log(2) / tasa
    r["err_t2"] = abs(r["t2_num"] - r["t2_ana"]) / r["t2_ana"]
    r["factor_10s"] = reg[-1][1] / a0
    r["kp_min"] = MU_A / MU_C
    r["alfa_w_deg"] = math.degrees(ALFA_W)
    r["q_alfa_hold_sin_control"] = Q * ALFA_W
    filas = []
    for m in (1.5, 2.0, 4.0, 8.0):
        kp = m * r["kp_min"]
        wn2 = MU_C * kp - MU_A
        wn = math.sqrt(wn2)
        kd = 2 * 0.7 * wn / MU_C
        # simulacion de la racha constante: theta'' = mu_a (theta + alfa_w) + mu_c (-kp theta - kd theta')
        f = lambda t, y: [y[1], MU_A * (y[0] + ALFA_W) + MU_C * (-kp * y[0] - kd * y[1])]
        reg2 = rk4_lineal(f, [0.0, 0.0], 0.002, int(30.0 / 0.002))
        th = reg2[-1][1]
        alfa_ss = th + ALFA_W
        alfa_ana = ALFA_W * MU_C * kp / (MU_C * kp - MU_A)
        delta_ss = -kp * th
        filas.append(dict(m=m, kp=kp, kd=kd, wn=wn, alfa_ss=alfa_ss, alfa_ana=alfa_ana, err=abs(alfa_ss - alfa_ana) / alfa_ana, delta_deg=math.degrees(delta_ss),
                          q_alfa=Q * alfa_ss, ok_lim=abs(delta_ss) <= DELTA_MAX))
    r["filas"] = filas
    # kp por debajo del minimo: divergencia
    kp = 0.5 * r["kp_min"]
    f = lambda t, y: [y[1], MU_A * y[0] + MU_C * (-kp * y[0] - 0.5 * y[1])]
    reg3 = rk4_lineal(f, [a0, 0.0], 0.002, int(10.0 / 0.002))
    r["div_sub"] = reg3[-1][1] / a0
    c, k0 = MU_C * 0.5, MU_C * kp - MU_A
    lam_sub = (-c + math.sqrt(c * c - 4 * k0)) / 2
    r["lam_sub"] = lam_sub
    r["tasa_sub_num"] = math.log(reg3[-1][1] / reg3[len(reg3) // 2][1]) / 5.0
    r["err_ss"] = max(x["err"] for x in filas)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Lanzador SINTETICO cerca de max-q: mu_a = {r['mu_a']:.4f} 1/s2 (inestable), mu_c = {r['mu_c']:.3f} 1/s2; racha alfa_w = w/V = {r['alfa_w_deg']:.3f} grados")
    print(f"Lazo abierto: lambda = {r['lam']:.4f} 1/s; duplicacion asintotica analitica = {r['t2_ana']:.4f} s; numerica = {r['t2_num']:.4f} s (error {r['err_t2']:.1e}); amplificacion en 10 s desde reposo = {r['factor_10s']:.3g}")
    print(f"Ganancia proporcional minima Kp_min = mu_a/mu_c = {r['kp_min']:.5f} rad/rad; con 0.5 Kp_min (y Kd = 0.5) el angulo se amplifica {r['div_sub']:.3g} veces en 10 s; tasa asintotica numerica {r['tasa_sub_num']:.4f} 1/s frente a la raiz positiva {r['lam_sub']:.4f} 1/s")
    print("Racha constante con control PD (zeta = 0.7) - estado estacionario:")
    print("  Kp/Kp_min   Kp       Kd      wn [rad/s]  alfa_ss/alfa_w   alfa_ss [grados]  delta [grados]  q*alfa [kPa*rad]  respeta 5 grados")
    for x in r["filas"]:
        print(f"  {x['m']:7.1f}  {x['kp']:7.4f}  {x['kd']:6.3f}  {x['wn']:9.3f}  {x['alfa_ss']/ALFA_W:12.4f}  {math.degrees(x['alfa_ss']):12.3f}  {x['delta_deg']:12.3f}  {x['q_alfa']/1e3:12.3f}  {'si' if x['ok_lim'] else 'NO'}")
    print(f"Error relativo maximo del estado estacionario frente a la formula = {r['err_ss']:.1e}")
    assert r["err_t2"] < 1e-3 and r["err_ss"] < 1e-3 and r["div_sub"] > 1.0 and abs(r["tasa_sub_num"] - r["lam_sub"]) / r["lam_sub"] < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
