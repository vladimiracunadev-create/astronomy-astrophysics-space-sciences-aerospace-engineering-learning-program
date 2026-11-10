#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C10: proteccion por fusible contra un cortocircuito en un bus SINTETICO de 28 V (modelo termico de primer orden).

Datos consultados (2026-11-10): ninguno numerico; se cita el contexto de bus de 28 V y de PCDU en el capitulo de potencia del estado del arte de naves pequenas
de la NASA, y la ficha de ECSS-E-ST-20C Rev.2 (solo existencia, fecha y alcance; no se leyo su texto).
ILUSTRATIVOS (sinteticos, no medidos): fuente = paquete 8S3P (resistencia equivalente 0.1333 ohm), arnes 0.30 ohm de ida y vuelta, fusible aguas abajo F2 con corriente de fusion
I_f = 3.0 A y constante termica tau = 0.5 s, fusible aguas arriba F1 con I_f = 15.0 A y tau = 1.5 s, factor de despeje (fusion + arco) de 3 sobre la integral de fusion.
Modelo: dtheta/dt = (I^2 R - h theta)/C con fusion en theta_m  ->  t_fusion = tau ln(I^2 / (I^2 - I_f^2)), tau = C/h; I^2 t_fusion = tau I^2 ln(I^2/(I^2 - I_f^2)).
Segunda via: integracion numerica de la ecuacion termica (Euler con paso adaptado) frente a la formula cerrada.
Criterio de selectividad: I^2 t de despeje de F2 < I^2 t de fusion de F1.
Tolerancia: tiempo de fusion numerico frente a la formula < 0.5 %.
"""
from __future__ import annotations
import math, platform

R_FUENTE, R_ARNES = 0.1333, 0.30
VBUS = 28.0
F2 = (3.0, 0.5)       # I_f [A], tau [s]
F1 = (15.0, 1.5)
K_DESPEJE = 3.0


def t_fusion(i, f):
    if_, tau = f
    if i <= if_:
        return math.inf
    return tau * math.log(i * i / (i * i - if_ * if_))


def t_fusion_numerico(i, f, n=200000):
    if_, tau = f
    if i <= if_:
        return math.inf
    # variable adimensional x = theta/theta_m ; dx/dt = ((i/if_)^2 - x)/tau ; fusion en x = 1
    x, t = 0.0, 0.0
    t_est = t_fusion(i, f)
    dt = t_est / n
    a = (i / if_) ** 2
    while x < 1.0:
        x += (a - x) / tau * dt
        t += dt
        if t > 20.0 * t_est:
            break
    # interpola el cruce de x = 1 dentro del ultimo paso
    return t - (x - 1.0) / ((a - x) / tau + 1e-300)


def i2t(i, f):
    return i * i * t_fusion(i, f)


def corriente_falla(r_falla=0.0):
    return VBUS / (R_FUENTE + R_ARNES + r_falla)


def resultados():
    r = dict(Isc=corriente_falla(), Isc_dura=corriente_falla(0.0))
    r["t2_sc"] = t_fusion(r["Isc"], F2)
    r["t1_sc"] = t_fusion(r["Isc"], F1)
    r["i2t_f2_lim"] = F2[1] * F2[0] ** 2
    r["i2t_f1_lim"] = F1[1] * F1[0] ** 2
    r["i2t_f2_sc"] = i2t(r["Isc"], F2)
    r["i2t_f1_sc"] = i2t(r["Isc"], F1)
    r["despeje_f2"] = K_DESPEJE * r["i2t_f2_sc"]
    r["selectivo_sc"] = r["despeje_f2"] < r["i2t_f1_sc"]
    r["cociente_sel"] = r["i2t_f1_sc"] / r["despeje_f2"]
    # corrientes de falla de distinta resistencia
    filas = []
    for rf in (0.0, 0.3, 1.0, 3.0):
        i = corriente_falla(rf)
        filas.append((rf, i, t_fusion(i, F2), t_fusion(i, F1), K_DESPEJE * i2t(i, F2) < i2t(i, F1)))
    r["filas"] = filas
    for k, (rf, i, t2, t1, sl) in enumerate(filas):
        r[f"I{k}"], r[f"tf2_{k}"], r[f"tf1_{k}"], r[f"sel_{k}"] = i, t2, t1, ("sí" if sl else "no")
    r["t32"] = t_fusion(3.2, F2)
    # verificacion numerica
    errs = []
    for i in (4.0, 6.0, 10.0, 30.0, r["Isc"]):
        errs.append(abs(t_fusion_numerico(i, F2) - t_fusion(i, F2)) / t_fusion(i, F2) * 100.0)
    r["err_num"] = max(errs)
    r["t4"], r["t6"], r["t10"], r["t30"] = (t_fusion(i, F2) for i in (4.0, 6.0, 10.0, 30.0))
    r["i2t_asint"] = F2[1] * F2[0] ** 2
    r["t2_sc_ms"] = r["t2_sc"] * 1e3
    r["t1_sc_ms"] = r["t1_sc"] * 1e3
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Bus SINTETICO de {VBUS:.0f} V; fuente {R_FUENTE} ohm + arnes {R_ARNES} ohm; corriente de cortocircuito franco = {r['Isc']:.2f} A")
    print(f"F2 (aguas abajo): I_f = {F2[0]} A, tau = {F2[1]} s ; F1 (aguas arriba): I_f = {F1[0]} A, tau = {F1[1]} s")
    print(" I [A]   t_fusion F2 [s]")
    for i, t in ((4.0, r["t4"]), (6.0, r["t6"]), (10.0, r["t10"]), (30.0, r["t30"]), (r["Isc"], r["t2_sc"])):
        print(f" {i:6.2f}  {t:12.6f}")
    print(f"Cortocircuito franco: F2 funde en {r['t2_sc']*1e3:.2f} ms ; F1 fundiria en {r['t1_sc']*1e3:.2f} ms")
    print(f"I2t de fusion de F2 = {r['i2t_f2_sc']:.3f} A2s ; despeje (x{K_DESPEJE:.0f}) = {r['despeje_f2']:.3f} A2s ; I2t de fusion de F1 = {r['i2t_f1_sc']:.3f} A2s")
    print(f"Cociente de selectividad I2t(F1)/I2t_despeje(F2) = {r['cociente_sel']:.2f} -> {'SELECTIVO' if r['selectivo_sc'] else 'NO SELECTIVO'}")
    print(" R_falla [ohm]  I_falla [A]  t_F2 [s]   t_F1 [s]   selectivo")
    for rf, i, t2, t1, s in r["filas"]:
        print(f" {rf:12.2f}  {i:10.2f}  {t2:9.4f}  {t1:9.4f}   {'si' if s else 'no'}")
    print(f"Diferencia maxima entre el tiempo de fusion numerico y el cerrado = {r['err_num']:.4f} %")
    assert r["err_num"] < 0.5
    assert r["selectivo_sc"]
    assert r["t2_sc"] < r["t1_sc"]
    assert abs(r["i2t_f2_sc"] - r["i2t_asint"]) / r["i2t_asint"] < 0.05, "a corriente alta I2t tiende a tau I_f^2"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
