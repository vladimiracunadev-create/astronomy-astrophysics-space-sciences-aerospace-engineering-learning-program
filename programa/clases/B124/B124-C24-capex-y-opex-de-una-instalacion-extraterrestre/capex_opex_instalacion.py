#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C24: CapEx, OpEx y costo nivelado de una instalacion extraterrestre SINTETICA que produce un bien en superficie.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de inversion. La instalacion, sus masas, costos y produccion son SINTETICOS/ILUSTRATIVOS.
Modelo: CapEx = M (h + c_t) (1 + i), con M la masa de equipo (kg), h el costo de fabricar un kg en la Tierra, c_t el costo de llevar un kg a la superficie
(ilustrativo, del orden del de la clase C23) e i el recargo de instalacion y puesta en marcha. OpEx anual = repuestos (f_r h M) + transporte de repuestos (m_r c_t) + operacion remota O.
Factor de recuperacion de capital CRF = r (1 + r)^n / ((1 + r)^n - 1); costo nivelado del producto LCOP = (CapEx CRF + OpEx) / Q.
Segunda via: valor actual de costos / valor actual de la produccion con un bucle anual (capex en el anio 0; opex y produccion en los anios 1..n).
Alternativa de traer el producto desde la Tierra al costo por kg a superficie c_t; produccion de equilibrio Q* = costo anual / c_t.
Unidades: kg, um/kg, Mum, anios. Tolerancias: LCOP por CRF = por valor actual < 1e-9; comprobacion de Q* por sustitucion < 1e-9.
"""
import platform

M, H, C_T, INST = 10000.0, 800.0, 90000.0, 0.10
FREP, M_REP, OPER = 0.03, 300.0, 12.0e6
R_DESC, N_VIDA, Q = 0.08, 15, 50000.0


def crf(r, n):
    return r * (1 + r) ** n / ((1 + r) ** n - 1)


def capex(c_t=C_T, m=M):
    return m * (H + c_t) * (1 + INST)


def opex(c_t=C_T, m=M):
    return FREP * H * m + M_REP * c_t + OPER


def lcop_crf(c_t=C_T, q=Q, r=R_DESC, n=N_VIDA, m=M):
    return (capex(c_t, m) * crf(r, n) + opex(c_t, m)) / q


def lcop_vp(c_t=C_T, q=Q, r=R_DESC, n=N_VIDA, m=M):
    vp_c = capex(c_t, m) + sum(opex(c_t, m) / (1 + r) ** t for t in range(1, n + 1))
    vp_q = sum(q / (1 + r) ** t for t in range(1, n + 1))
    return vp_c / vp_q


def run():
    cx, ox = capex(), opex()
    c_anual = cx * crf(R_DESC, N_VIDA) + ox
    l1, l2 = lcop_crf(), lcop_vp()
    q_eq = c_anual / C_T
    chk_q = abs(lcop_crf(q=q_eq) - C_T)
    R = {"capex": cx, "opex": ox, "crf": crf(R_DESC, N_VIDA), "anualidad": cx * crf(R_DESC, N_VIDA), "c_anual": c_anual, "lcop": l1, "lcop_vp": l2, "dif": abs(l1 - l2),
         "q_eq": q_eq, "chk_q": chk_q, "ahorro_kg": C_T - l1, "razon": l1 / C_T, "frac_transp_capex": M * C_T * (1 + INST) / cx, "frac_transp_opex": M_REP * C_T / ox,
         "l_t50": lcop_crf(c_t=0.5 * C_T), "l_t150": lcop_crf(c_t=1.5 * C_T), "l_q25": lcop_crf(q=0.25 * Q), "l_r12": lcop_crf(r=0.12), "l_n10": lcop_crf(n=10), "l_n20": lcop_crf(n=20),
         "costo_tierra_total": C_T * Q * N_VIDA, "pv_tierra": sum(C_T * Q / (1 + R_DESC) ** t for t in range(1, N_VIDA + 1)),
         "pv_inst": cx + sum(ox / (1 + R_DESC) ** t for t in range(1, N_VIDA + 1))}
    R.update({"capex_m": cx / 1e6, "opex_m": ox / 1e6, "ftc": 100 * R["frac_transp_capex"], "fto": 100 * R["frac_transp_opex"], "anualidad_m": R["anualidad"] / 1e6,
              "c_anual_m": c_anual / 1e6, "razon_pct": 100 * R["razon"], "pv_inst_m": R["pv_inst"] / 1e6, "pv_tierra_m": R["pv_tierra"] / 1e6})
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Instalacion ILUSTRATIVA: equipo {M:.0f} kg ; fabricar {H:.0f} um/kg ; transporte a superficie {C_T:.0f} um/kg ; recargo de instalacion {100 * INST:.0f} % ; vida {N_VIDA} anios ; tasa {100 * R_DESC:.0f} % ; produccion {Q:.0f} kg/anio")
    print(f"CapEx = {R['capex'] / 1e6:.3f} Mum (transporte = {100 * R['frac_transp_capex']:.1f} % del CapEx) ; OpEx = {R['opex'] / 1e6:.3f} Mum/anio (transporte de repuestos = {100 * R['frac_transp_opex']:.1f} %)")
    print(f"CRF = {R['crf']:.5f} ; anualidad del CapEx = {R['anualidad'] / 1e6:.3f} Mum/anio ; costo anual total = {R['c_anual'] / 1e6:.3f} Mum/anio")
    print(f"Costo nivelado del producto: por CRF = {R['lcop']:.4f} um/kg ; por valor actual = {R['lcop_vp']:.4f} um/kg ; diferencia = {R['dif']:.1e}")
    print(f"Traerlo de la Tierra cuesta {C_T:.0f} um/kg: ahorro = {R['ahorro_kg']:.0f} um/kg ; razon = {100 * R['razon']:.2f} % ; produccion de equilibrio = {R['q_eq']:.0f} kg/anio (control por sustitucion {R['chk_q']:.1e})")
    print(f"Sensibilidad del costo nivelado: transporte -50 % -> {R['l_t50']:.0f} ; +50 % -> {R['l_t150']:.0f} ; produccion /4 -> {R['l_q25']:.0f} ; tasa 12 % -> {R['l_r12']:.0f} ; vida 10 anios -> {R['l_n10']:.0f} ; 20 anios -> {R['l_n20']:.0f} (um/kg)")
    print(f"Valor actual (15 anios): instalacion = {R['pv_inst'] / 1e6:.1f} Mum ; traer todo de la Tierra = {R['pv_tierra'] / 1e6:.1f} Mum")
    assert R["dif"] < 1e-9 and R["chk_q"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
