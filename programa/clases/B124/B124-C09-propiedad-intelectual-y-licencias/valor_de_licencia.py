#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C09: valoracion de una licencia de propiedad intelectual con regalias, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria legal, de propiedad intelectual ni financiera. Ventas, tasas y terminos de licencia son SINTETICOS.
Modelo: ventas del licenciatario S_t = S0 (1 + g)^(t-1), t = 1..T; regalia = r S_t; valor actual de las regalias = sum r S_t / (1 + d)^t.
Forma cerrada: VP = r S0 / (1 + d) (1 - q^T) / (1 - q), con q = (1 + g)/(1 + d).
Apilamiento: el licenciatario paga varias regalias; margen restante = m - sum(r_i); la licencia no es viable si sum(r_i) >= m.
Exclusiva (1 licenciatario, ventas f x S0, regalia r_e, cuota inicial U_e) frente a no exclusiva (3 licenciatarios, ventas S0, r_n, U_n):
f* es el factor de ventas que iguala el valor para el licenciante, resuelto de forma analitica y comprobado por sustitucion.
Unidades: Mum (millones de unidades monetarias sinteticas). Tolerancias: bucle frente a forma cerrada < 1e-9; f* por sustitucion < 1e-9.
"""
import platform

S0, G, T, D = 50.0, 0.15, 8, 0.10
R_UNA = 0.05
MARGEN = 0.20
APILADAS = [0.04, 0.06, 0.05]
EXCL = dict(r=0.06, U=5.0, n=1)
NOEX = dict(r=0.04, U=1.0, n=3)
F_EXCL = 1.6


def vp_bucle(r, s0=S0, g=G, t=T, d=D):
    return sum(r * s0 * (1 + g) ** (k - 1) / (1 + d) ** k for k in range(1, t + 1))


def vp_cerrado(r, s0=S0, g=G, t=T, d=D):
    q = (1 + g) / (1 + d)
    return r * s0 / (1 + d) * (1 - q ** t) / (1 - q)


def valor_licenciante(c, f=1.0):
    return c["n"] * (c["U"] + vp_cerrado(c["r"], s0=S0 * f))


def f_igual():
    unit_e = EXCL["r"] * vp_cerrado(1.0)  # VP por unidad de f para la exclusiva (regalia r x factor)
    v_n = valor_licenciante(NOEX)
    return (v_n - EXCL["n"] * EXCL["U"]) / (EXCL["n"] * unit_e)


def run():
    vb, vc = vp_bucle(R_UNA), vp_cerrado(R_UNA)
    apilado = sum(APILADAS)
    fs = f_igual()
    return {"vp_bucle": vb, "vp_cerrado": vc, "dif_vp": abs(vb - vc), "apilado": apilado, "margen_rest": MARGEN - apilado,
            "viable": 1 if apilado < MARGEN else 0, "v_excl": valor_licenciante(EXCL, F_EXCL), "v_noex": valor_licenciante(NOEX),
            "f_star": fs, "chk_f": abs(valor_licenciante(EXCL, fs) - valor_licenciante(NOEX)), "ventas_t8": S0 * (1 + G) ** (T - 1),
            "regalia_t1": R_UNA * S0, "r_max": MARGEN, "vp_factor": vp_cerrado(1.0)}


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Licencia SINTETICA: S0 = {S0} Mum, g = {G}, T = {T} anios, d = {D}, regalia base = {R_UNA}")
    print(f"VP de regalias: bucle = {R['vp_bucle']:.6f} Mum ; forma cerrada = {R['vp_cerrado']:.6f} Mum ; diferencia = {R['dif_vp']:.1e}")
    print(f"Ventas del anio {T} = {R['ventas_t8']:.3f} Mum ; regalia del anio 1 = {R['regalia_t1']:.3f} Mum")
    print(f"Apilamiento de regalias {APILADAS}: total = {R['apilado']:.2f} ; margen del licenciatario = {MARGEN:.2f} ; margen restante = {R['margen_rest']:.2f} ; viable = {bool(R['viable'])}")
    print(f"Valor para el licenciante: exclusiva (ventas x{F_EXCL}) = {R['v_excl']:.3f} Mum ; no exclusiva (3 licenciatarios) = {R['v_noex']:.3f} Mum")
    print(f"Factor de ventas de equilibrio f* = {R['f_star']:.4f} ; comprobacion por sustitucion = {R['chk_f']:.1e}")
    assert R["dif_vp"] < 1e-9 and R["chk_f"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
