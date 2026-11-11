#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B117-C02: contencion de un contaminante en el aire de una cabina (modelo de volumen mezclado).

CONTENIDO EDUCATIVO: no es un procedimiento de seguridad ni consejo operativo; no sustituye formacion ni supervision profesional.
Datos consultados (2026-11-10): volumen libre de aire de la EEI de 807.3 a 898.8 m3 y presion total de 724 a 770.5 mmHg
(Schaezler y Cook, ICES-2015-146, NASA NTRS 20150010425). La tabla JSC 20584 Rev C (NASA, 2024-06-13) define los SMAC por duraciones de
1 h a 1000 d; sus cifras NO se usan aqui porque la extraccion de texto del PDF no permitio asignar con certeza cada valor a su compuesto.
ILUSTRATIVOS (sinteticos): modulo aislado de 70 m3; masa liberada 5 g de un gas de masa molar 17.03 g/mol (ejemplo generico);
depurador de 100 m3/h con eficiencia 0.9 por paso; limite de EJEMPLO de 5 ppm (NO es un SMAC); intercambio modulo-cabina 20 m3/h.
Constantes: R = 8.314462618 J/(mol K) (valor exacto SI), T = 298.15 K, P = 101325 Pa -> volumen molar 24.465 L/mol (gas ideal).
Modelo: C' = -lambda C con lambda = eta Qs / V; mezcla instantanea y perfecta; sin adsorcion en paredes ni fuentes continuas.
Unidades: m3, h, mg/m3, ppm (volumen). Tolerancias: RK4 frente a analitico < 1e-9 relativa; conservacion de masa < 1e-9.
"""
from __future__ import annotations
import math, platform

R, T, P = 8.314462618, 298.15, 101325.0
VM = R * T / P * 1000.0              # L/mol
M_MOL = 17.03                        # g/mol (ilustrativo)
MASA_MG = 5000.0                     # mg liberados (ilustrativo)
V_MOD, V_CAB_MIN, V_CAB_MAX = 70.0, 807.3, 898.8
QS, ETA, QX = 100.0, 0.9, 20.0
LIM_PPM = 5.0                        # limite de EJEMPLO


def mg_m3_a_ppm(c):
    return c * VM / M_MOL


def lam(v):
    return ETA * QS / v


def tiempo_a_limite(c0_ppm, v):
    return math.log(c0_ppm / LIM_PPM) / lam(v)


def rk4_decaimiento(c0, l, t_fin, n=2000):
    h, c = t_fin / n, c0
    for _ in range(n):
        k1 = -l * c
        k2 = -l * (c + 0.5 * h * k1)
        k3 = -l * (c + 0.5 * h * k2)
        k4 = -l * (c + h * k3)
        c += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return c


def dos_compartimentos(l1, t_fin, n=20000):
    """C1 (modulo, con depurador l1) y C2 (resto de la cabina) con intercambio QX; RK4."""
    def f(c1, c2):
        return (-(QX / V_MOD) * (c1 - c2) - l1 * c1, (QX / V_CAB_MIN) * (c1 - c2))
    c1, c2 = MASA_MG / V_MOD, 0.0
    h = t_fin / n
    for _ in range(n):
        a1, a2 = f(c1, c2)
        b1, b2 = f(c1 + 0.5 * h * a1, c2 + 0.5 * h * a2)
        d1, d2 = f(c1 + 0.5 * h * b1, c2 + 0.5 * h * b2)
        e1, e2 = f(c1 + h * d1, c2 + h * d2)
        c1 += h * (a1 + 2 * b1 + 2 * d1 + e1) / 6.0
        c2 += h * (a2 + 2 * b2 + 2 * d2 + e2) / 6.0
    return c1, c2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Volumen molar a 298.15 K y 101325 Pa = {VM:.3f} L/mol")
    print("Datos consultados: V libre EEI 807.3-898.8 m3; resto ILUSTRATIVO (limite de ejemplo 5 ppm, no es un SMAC).")
    print(" caso              V [m3]  C0 [mg/m3]  C0 [ppm]  lambda [1/h]  t a 5 ppm [min]")
    casos = {"modulo aislado": V_MOD, "cabina (min)": V_CAB_MIN, "cabina (max)": V_CAB_MAX}
    res = {}
    for nom, v in casos.items():
        c0 = MASA_MG / v
        ppm = mg_m3_a_ppm(c0)
        t = tiempo_a_limite(ppm, v) * 60.0 if ppm > LIM_PPM else 0.0
        res[nom] = (ppm, t)
        print(f"{nom:16s} {v:8.1f} {c0:11.3f} {ppm:9.2f} {lam(v):12.4f} {t:15.1f}")
    # verificacion RK4 frente a analitico
    err = 0.0
    for v in casos.values():
        c0 = MASA_MG / v
        c_rk = rk4_decaimiento(c0, lam(v), 2.0)
        c_an = c0 * math.exp(-lam(v) * 2.0)
        err = max(err, abs(c_rk - c_an) / c_an)
    print(f"Error relativo maximo RK4 frente a analitico = {err:.2e}")
    # dos compartimentos: sin depurador se conserva la masa y se llega a mezcla uniforme
    c1, c2 = dos_compartimentos(0.0, 200.0)
    masa = c1 * V_MOD + c2 * V_CAB_MIN
    unif = MASA_MG / (V_MOD + V_CAB_MIN)
    print(f"Sin depurador, t = 200 h: C modulo = {c1:.4f}, C cabina = {c2:.4f} mg/m3; uniforme esperado = {unif:.4f}; masa total = {masa:.3f} mg")
    # con depurador en el modulo
    for t_h in (0.5, 1.0, 2.0):
        a, b = dos_compartimentos(lam(V_MOD), t_h)
        print(f"Con depurador en el modulo, t = {t_h:.1f} h: C modulo = {mg_m3_a_ppm(a):7.2f} ppm ; C cabina = {mg_m3_a_ppm(b):6.3f} ppm")
    assert err < 1e-9
    assert abs(masa - MASA_MG) / MASA_MG < 1e-9
    assert abs(c1 - unif) / unif < 1e-6 and abs(c2 - unif) / unif < 1e-6
    assert res["modulo aislado"][0] > res["cabina (min)"][0] > res["cabina (max)"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
