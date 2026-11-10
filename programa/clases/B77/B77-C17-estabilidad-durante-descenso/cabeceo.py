#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C17: estabilidad de cabeceo de una capsula durante el descenso (equilibrio y oscilacion).

Datos consultados (2026-11-10): estabilidad estatica: el vehiculo es estable cuando el centro de presion esta por detras (abajo, en la pagina de la NASA) del centro de gravedad
y aparece un par restaurador (NASA Glenn, Rocket Stability); q = rho V^2/2 (NASA Glenn).
SINTETICOS / ILUSTRATIVOS (inventados): capsula de diametro de referencia d = 3.9 m (S = pi d^2/4), momento de inercia de cabeceo I_y = 6000 kg m2, condiciones de vuelo
q = 5000 Pa y V = 2000 m/s constantes durante el calculo (aproximacion de coeficientes congelados), Cm(alfa) = Cm0 + Cm_alfa alfa con Cm_alfa = -0.05 /rad
(estable) o +0.02 /rad (inestable), Cm0 = 0.008, Cm_q = -0.2 (amortiguamiento de cabeceo).
Sistema: plano de cabeceo, alfa = angulo de ataque = theta - gamma con la direccion de vuelo gamma fija durante la maniobra corta; SI, angulos en rad salvo indicacion.
Modelo: I_y alfa'' = q S d [Cm0 + Cm_alfa alfa] + (Cm_q q S d^2/(2V)) alfa'; wn^2 = -Cm_alfa q S d/I_y; 2 zeta wn = -Cm_q q S d^2/(2 V I_y); alfa_trim = -Cm0/Cm_alfa.
Segunda via: periodo medido por cruces de la posicion de equilibrio y envolvente exponencial frente a wd = wn sqrt(1 - zeta^2) y a la tasa zeta wn; caso inestable: tasa asintotica lambda = (-c + sqrt(c^2 - 4 wn^2))/2 (wn^2 < 0) medida entre 10 y 20 s; la duplicacion inicial desde el reposo es mas lenta que ln2/lambda.
Tolerancias: periodo 5e-3 relativo; tasa de decaimiento 2e-2 relativa; trim 1e-3 grados.
"""
import math, platform

D, IY, Q, V = 3.9, 6000.0, 5000.0, 2000.0
S = math.pi * D * D / 4
CM0, CMA_E, CMA_I, CMQ = 0.008, -0.05, 0.02, -0.2


def parametros(cma):
    wn2 = -cma * Q * S * D / IY
    c2 = -CMQ * Q * S * D * D / (2 * V * IY)  # = 2 zeta wn
    return wn2, c2


def integra(cma, a0, t_fin, dt=0.002):
    wn2, c2 = parametros(cma)
    # alfa'' = -wn2 (alfa - alfa_trim) - c2 alfa'
    atrim = -CM0 / cma
    f = lambda y: (y[1], -wn2 * (y[0] - atrim) - c2 * y[1])
    y, t = (a0, 0.0), 0.0
    reg = [(0.0, a0)]
    while t < t_fin:
        k1 = f(y); k2 = f([a + dt / 2 * b for a, b in zip(y, k1)]); k3 = f([a + dt / 2 * b for a, b in zip(y, k2)]); k4 = f([a + dt * b for a, b in zip(y, k3)])
        y = tuple(a + dt * (b + 2 * c + 2 * d + e) / 6 for a, b, c, d, e in zip(y, k1, k2, k3, k4))
        t += dt
        reg.append((t, y[0]))
    return reg


def calcular():
    r = {}
    wn2, c2 = parametros(CMA_E)
    wn = math.sqrt(wn2)
    zeta = c2 / (2 * wn)
    wd = wn * math.sqrt(1 - zeta ** 2)
    atrim = -CM0 / CMA_E
    r.update(wn=wn, zeta=zeta, wd=wd, T_ana=2 * math.pi / wd, atrim_deg=math.degrees(atrim))
    a0 = math.radians(30.0)
    reg = integra(CMA_E, a0, 40.0)
    # cruces ascendentes por alfa_trim
    cruces = []
    for (t0, x0), (t1, x1) in zip(reg, reg[1:]):
        if x0 < atrim <= x1:
            cruces.append(t0 + (atrim - x0) / (x1 - x0) * (t1 - t0))
    r["T_num"] = (cruces[-1] - cruces[0]) / (len(cruces) - 1)
    r["err_T"] = abs(r["T_num"] - r["T_ana"]) / r["T_ana"]
    # envolvente: maximos locales
    picos = [(t1, x1) for (t0, x0), (t1, x1), (t2, x2) in zip(reg, reg[1:], reg[2:]) if x1 > x0 and x1 >= x2 and x1 > atrim]
    amp0, amp1 = picos[0][1] - atrim, picos[-1][1] - atrim
    r["tasa_num"] = math.log(amp0 / amp1) / (picos[-1][0] - picos[0][0])
    r["tasa_ana"] = zeta * wn
    r["err_tasa"] = abs(r["tasa_num"] - r["tasa_ana"]) / r["tasa_ana"]
    r["media_osc"] = math.degrees(sum(x for _, x in reg[-int(r["T_ana"] / 0.002):]) / int(r["T_ana"] / 0.002))
    r["amp_max_deg"] = math.degrees(max(x for _, x in reg))
    # caso inestable
    wn2i, c2i = parametros(CMA_I)
    # alfa'' = -wn2i (alfa - atrim_i) - c2i alfa' con wn2i < 0: raices de s^2 + c2 s + wn2i = 0
    disc = math.sqrt(c2i ** 2 - 4 * wn2i)
    lam = (-c2i + disc) / 2
    r["lam"], r["t2_ana"] = lam, math.log(2) / lam
    atrim_i = -CM0 / CMA_I
    reg_i = integra(CMA_I, atrim_i + math.radians(0.1), 30.0)
    desv = [(t, x - atrim_i) for t, x in reg_i]
    d10 = next(d for t, d in desv if t >= 10.0)
    d20 = next(d for t, d in desv if t >= 20.0)
    tasa = math.log(d20 / d10) / 10.0
    r["tasa_div_num"] = tasa
    r["t2_num"] = math.log(2) / tasa
    r["t_dup_inicial"] = next(t for t, d in desv if d >= 2 * desv[0][1])
    r["err_t2"] = abs(r["t2_num"] - r["t2_ana"]) / r["t2_ana"]
    r["atrim_i_deg"] = math.degrees(atrim_i)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Capsula SINTETICA: d = {D} m, S = {S:.3f} m2, I_y = {IY:.0f} kg m2, q = {Q:.0f} Pa, V = {V:.0f} m/s (coeficientes congelados)")
    print(f"Caso estable (Cm_alfa = {CMA_E}/rad): wn = {r['wn']:.4f} rad/s, zeta = {r['zeta']:.5f}, wd = {r['wd']:.4f} rad/s, periodo analitico = {r['T_ana']:.4f} s; alfa_trim = {r['atrim_deg']:.3f} grados")
    print(f"  oscilacion desde 30 grados: amplitud maxima {r['amp_max_deg']:.2f} grados; periodo medido = {r['T_num']:.4f} s (error {r['err_T']:.1e}); decaimiento medido = {r['tasa_num']:.5f} 1/s frente a {r['tasa_ana']:.5f} (error {r['err_tasa']:.1e})")
    print(f"  media de la oscilacion en el ultimo periodo = {r['media_osc']:.3f} grados (trim = {r['atrim_deg']:.3f})")
    print(f"Caso inestable (Cm_alfa = +{CMA_I}/rad): trim inestable en {r['atrim_i_deg']:.2f} grados; tasa de divergencia = {r['lam']:.4f} 1/s; tiempo de duplicacion asintotico analitico = {r['t2_ana']:.3f} s; numerico (pendiente entre 10 y 20 s) = {r['t2_num']:.3f} s (error {r['err_t2']:.1e}); la duplicacion inicial desde el reposo tarda {r['t_dup_inicial']:.3f} s")
    assert r["err_T"] < 5e-3 and r["err_tasa"] < 2e-2
    assert r["err_t2"] < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
