#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C03: concentracion (HHI) y margen de precio en un mercado aguas arriba y otro aguas abajo, SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de competencia (antimonopolio). Todos los datos son SINTETICOS.
Modelo: oligopolio de Cournot con demanda lineal P = a - b Q y costos marginales c_i. Equilibrio: Q = sum(a - c_i) / ((n + 1) b),
q_i = (a - c_i)/b - Q. Indice de Lerner de la empresa i: L_i = (P - c_i)/P = s_i / e, con e = P/(b Q) la elasticidad de la demanda;
promedio ponderado por cuota: sum(s_i L_i) = HHI / e (HHI en fraccion, suma de s_i^2).
Unidades: precio en um por unidad (sinteticas), cantidad en unidades sinteticas. HHI en puntos (0-10000) = 10000 x fraccion.
Tolerancias: cierre por mejor respuesta frente a la forma cerrada < 1e-9; identidad de Lerner < 1e-12; variacion del HHI por fusion < 1e-9.
"""
import platform


def cournot(a, b, costos):
    n = len(costos)
    Q = sum(a - c for c in costos) / ((n + 1) * b)
    q = [(a - c) / b - Q for c in costos]
    return Q, q


def mejor_respuesta(a, b, costos, iteraciones=2000):
    n = len(costos)
    q = [1.0] * n
    for _ in range(iteraciones):
        for i in range(n):
            otros = sum(q) - q[i]
            q[i] = max(0.0, (a - costos[i] - b * otros) / (2 * b))
    return q


def hhi(cuotas):
    return sum(s * s for s in cuotas)


def mercado(a, b, costos):
    Q, q = cournot(a, b, costos)
    P = a - b * Q
    s = [x / Q for x in q]
    eps = P / (b * Q)
    L = [(P - c) / P for c in costos]
    h = hhi(s)
    lerner_prom = sum(si * li for si, li in zip(s, L))
    ident = max(abs(li - si / eps) for si, li in zip(s, L))
    q_br = mejor_respuesta(a, b, costos)
    br_err = max(abs(x - y) for x, y in zip(q, q_br))
    return dict(Q=Q, P=P, s=s, eps=eps, L=L, h=h, lerner=lerner_prom, ident=ident, br_err=br_err, q=q)


def run():
    up = mercado(100.0, 1.0, [20.0, 30.0, 40.0])
    dn = mercado(100.0, 1.0, [30.0, 30.0, 35.0, 35.0, 40.0, 40.0])
    s = sorted(up["s"])
    dh_formula = 2 * s[0] * s[1] * 10000
    fus = [s[0] + s[1]] + s[2:]
    dh_num = (hhi(fus) - hhi(s)) * 10000
    R = {"hhi_up": up["h"] * 10000, "hhi_dn": dn["h"] * 10000, "p_up": up["P"], "p_dn": dn["P"], "q_up": up["Q"], "q_dn": dn["Q"],
         "eps_up": up["eps"], "eps_dn": dn["eps"], "lerner_up": up["lerner"], "lerner_dn": dn["lerner"],
         "lerner_hhi_up": up["h"] / up["eps"], "ident_up": up["ident"], "ident_dn": dn["ident"],
         "br_up": up["br_err"], "br_dn": dn["br_err"], "dh_formula": dh_formula, "dh_num": dh_num,
         "hhi_fus": hhi(fus) * 10000, "s_mayor": max(up["s"]), "l1_up": up["L"][0], "sdn_mayor": max(dn["s"]),
         "cuota_menor": s[0], "cuota_segunda": s[1]}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Mercados SINTETICOS (ilustrativos); Cournot con demanda P = 100 - Q; precio en um/unidad.")
    print(f" aguas arriba (3 empresas, c = 20/30/40): Q = {R['q_up']:.3f} ; P = {R['p_up']:.3f} ; HHI = {R['hhi_up']:.0f} ; elasticidad = {R['eps_up']:.4f}")
    print(f"   Lerner medio ponderado = {R['lerner_up']:.4f} ; HHI/e = {R['lerner_hhi_up']:.4f} ; mayor cuota = {R['s_mayor']:.4f}")
    print(f" aguas abajo (6 empresas): Q = {R['q_dn']:.3f} ; P = {R['p_dn']:.3f} ; HHI = {R['hhi_dn']:.0f} ; elasticidad = {R['eps_dn']:.4f}")
    print(f"   Lerner medio ponderado = {R['lerner_dn']:.4f} ; mayor cuota = {R['sdn_mayor']:.4f}")
    print(f"Fusion de las dos menores empresas aguas arriba: dHHI formula 2 s1 s2 = {R['dh_formula']:.1f} ; directo = {R['dh_num']:.1f} ; HHI nuevo = {R['hhi_fus']:.0f}")
    print(f"Errores: Lerner arriba {R['ident_up']:.1e} ; abajo {R['ident_dn']:.1e} ; mejor respuesta arriba {R['br_up']:.1e} ; abajo {R['br_dn']:.1e}")
    assert R["ident_up"] < 1e-12 and R["ident_dn"] < 1e-12
    assert R["br_up"] < 1e-9 and R["br_dn"] < 1e-9
    assert abs(R["dh_formula"] - R["dh_num"]) < 1e-9
    assert abs(R["lerner_up"] - R["lerner_hhi_up"]) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
