#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C16: ligadura, periodo y perturbacion por el paso de una estrella de un cometa de la nube de Oort.

Datos consultados el 2026-11-09: (GM)_sol nominal de la IAU 2015 (Resolucion B3). La unidad astronomica (1.495978707e11 m) no se consulto.
El resumen de Vokrouhlicky, Nesvorny y Dones (2019) indica que los cometas de largo periodo observados proceden de la nube externa, con semiejes de ~1e4 ua o mas
(solo resumen, via un buscador; no se leyo el texto).
Datos ILUSTRATIVOS (sinteticos): cometa con a = 2e4 ua y e = 0.999 (en el afelio); estrella de 0.5 M_sol con velocidad 30 km/s y parametro de impacto
3e4 ua respecto del cometa. No se trata de un encuentro real (ningun catalogo de estrellas consultado).
Sistema de referencia: heliocentrico (no inercial: se incluye el termino indirecto), 3D; SI.
Via 1: aproximacion impulsiva, Delta v = 2 G M* / v* (1/b_cometa - 1/b_sol) hacia la estrella, para b >> distancia recorrida durante el encuentro.
Via 2: integracion RK4 (h = 2e9 s, ventana de +-12 b / v) del cometa sometido al Sol y a la estrella (aceleracion de la estrella sobre el cometa menos sobre el Sol), con la estrella en linea recta.
Tolerancias: Delta v numerico frente al impulsivo 5 %.
"""
from __future__ import annotations
import math, platform

GM = 1.3271244e20
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
A_C, E_C = 2.0e4 * UA, 0.999
GM_S, V_S, B = 0.5 * GM, 30e3, 3.0e4 * UA


def acel(rc, rs):
    d = [rs[i] - rc[i] for i in range(3)]
    dn = math.sqrt(sum(x * x for x in d)) ** 3
    sn = math.sqrt(sum(x * x for x in rs)) ** 3
    cn = math.sqrt(sum(x * x for x in rc)) ** 3
    return [-GM * rc[i] / cn + GM_S * (d[i] / dn - rs[i] / sn) for i in range(3)]


def integrar(con_estrella=True, h=2e9):
    q_afelio = A_C * (1.0 + E_C)
    v_afelio = math.sqrt(GM * (1.0 - E_C) / (A_C * (1.0 + E_C)))
    rc = [q_afelio, 0.0, 0.0]
    vc = [0.0, v_afelio, 0.0]
    z0 = -12.0 * B
    t0 = abs(z0) / V_S
    n = int(2 * t0 / h)
    t = 0.0
    def estado(t_):
        return [q_afelio + B, 0.0, z0 + V_S * t_]
    def f(t_, y):
        rcc, vcc = y[:3], y[3:]
        a = acel(rcc, estado(t_)) if con_estrella else [-GM * rcc[i] / math.sqrt(sum(x * x for x in rcc)) ** 3 for i in range(3)]
        return list(vcc) + a
    y = rc + vc
    for _ in range(n):
        k1 = f(t, y); k2 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k1)]); k3 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k2)]); k4 = f(t + h, [a + h * b for a, b in zip(y, k3)])
        y = [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]
        t += h
    return y, q_afelio, v_afelio


def r_dv_tang(dv, va):
    """Cambio relativo de j si el impulso fuese tangencial: j = r v_t, luego Delta j / j = Delta v / v_afelio."""
    return dv / va


def calcular():
    P = 2 * math.pi * math.sqrt(A_C ** 3 / GM)
    energia = -GM / (2 * A_C)
    q_peri = A_C * (1.0 - E_C)
    yc, qa, va = integrar(False)
    ye, _, _ = integrar(True)
    dv_num = [ye[3 + i] - yc[3 + i] for i in range(3)]
    b_sol = qa + B
    dv_imp = 2 * GM_S / V_S * (1.0 / B - 1.0 / b_sol)
    # cambio relativo del momento angular especifico
    def jmag(y):
        r, v = y[:3], y[3:]
        return math.sqrt(sum(c * c for c in [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]]))
    j0 = qa * va
    return dict(P=P, energia=energia, q_peri=q_peri, v_afelio=va, v_circ=math.sqrt(GM / A_C), dv_num=dv_num, dv_imp=dv_imp, j_rel=jmag(ye) / j0 - 1.0,
                sin_estrella=jmag(yc) / j0 - 1.0, j_tang=r_dv_tang(dv_imp, va), q_nueva=(jmag(ye) ** 2) / (2 * GM) , q_vieja=j0 ** 2 / (2 * GM))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cometa ilustrativo: a = {A_C / UA:.0f} ua, e = {E_C} ; periodo = {r['P'] / ANIO:.3e} anios ; energia especifica = {r['energia']:.3e} J/kg")
    print(f"Perihelio = {r['q_peri'] / UA:.2f} ua ; velocidad en el afelio = {r['v_afelio']:.2f} m/s ; velocidad circular a = {r['v_circ']:.1f} m/s")
    print(f"Encuentro ilustrativo: 0.5 M_sol, {V_S / 1e3:.0f} km/s, b = {B / UA:.0e} ua")
    print(f"Delta v impulsivo (hacia la estrella) = {r['dv_imp']:.4f} m/s ; Delta v integrado = ({r['dv_num'][0]:.4f}, {r['dv_num'][1]:.4f}, {r['dv_num'][2]:.4f}) m/s")
    print(f"Cambio relativo de j sin estrella (control) = {r['sin_estrella']:.1e} ; con estrella = {r['j_rel']:+.3f}")
    print(f"Perihelio aproximado antes = {r['q_vieja'] / UA:.2f} ua ; despues = {r['q_nueva'] / UA:.2f} ua (q ~ j^2/(2GM))")
    print(f"Si el mismo impulso fuese tangencial: Delta j / j = {r['j_tang']:.3f} y el perihelio (q ~ j^2) cambiaria {((1 + r['j_tang']) ** 2 - 1) * 100:+.0f} % (o {((1 - r['j_tang']) ** 2 - 1) * 100:+.0f} %)")
    err = abs(r["dv_num"][0] / r["dv_imp"] - 1)
    print(f"Diferencia relativa entre el impulso integrado (componente x) y el impulsivo = {err:.2e}")
    assert abs(r["sin_estrella"]) < 1e-6
    assert err < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
