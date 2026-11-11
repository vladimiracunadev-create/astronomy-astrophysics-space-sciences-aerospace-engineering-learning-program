#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C23: costo de transporte por kilogramo a orbita baja y a superficie, con la ecuacion del cohete, SINTETICO/ILUSTRATIVO.

CONTENIDO EDUCATIVO: no es asesoria financiera ni una cotizacion de lanzamiento. Precios, masas, impulsos especificos y coeficientes estructurales son ILUSTRATIVOS
(no se consulto ningun vehiculo ni precio de lanzamiento real).
Ecuacion del cohete (Tsiolkovsky): dv = g0 Isp ln(m0/mf), g0 = 9.80665 m/s^2 (valor convencional; no consultado en esta clase). Para una etapa con coeficiente
estructural e = m_s/(m_s + m_p) y razon de masas r = exp(dv/(g0 Isp)): fraccion de carga util lam = (1/r - e)/(1 - e). Varias etapas: producto de las fracciones.
Orbita baja: dv_total = 9400 m/s (incluye perdidas, ilustrativo) repartido entre 2 etapas (Isp 300 y 340 s; e = 0.07 y 0.09); reparto igual y reparto optimo
(busqueda ternaria frente a barrido de 0.001). Lanzador de masa inicial 550000 kg y precio 60 Mum por lanzamiento; reutilizacion: ahorro de 30 % del precio.
Superficie lunar (ilustrativa): etapa de descenso desde orbita baja, dv = 6000 m/s, Isp 340 s, e = 0.12. Costo por kg a superficie = costo por kg a orbita / fraccion.
Verificacion: dv recalculado desde las masas (hacia adelante) igual al dv de diseno dentro de 1e-6 m/s; optimo ternario = barrido dentro de 0.002 en la fraccion de reparto.
Unidades: m/s, s, kg, Mum, um por kg (um = unidad monetaria sintetica).
"""
import math, platform

G0 = 9.80665
DV_LEO, ISP1, ISP2, E1, E2 = 9400.0, 300.0, 340.0, 0.07, 0.09
DV_SUP, ISP_S, E_S = 6000.0, 340.0, 0.12
M0, PRECIO, AHORRO = 550000.0, 60.0, 0.30


def lam_etapa(dv, isp, e):
    r = math.exp(dv / (G0 * isp))
    return (1 / r - e) / (1 - e)


def lam_leo(f, isp1=ISP1, isp2=ISP2, e1=E1, e2=E2, dv=DV_LEO):
    return lam_etapa(f * dv, isp1, e1) * lam_etapa((1 - f) * dv, isp2, e2)


def dv_hacia_adelante(lam1, lam2):
    """Recalcula dv desde las masas con m0 = 1 (hacia adelante)."""
    # etapa 1: m0 = 1, carga = lam1 (la etapa 2 completa), masa final = carga + estructura
    e1, e2 = E1, E2
    mf1 = lam1 + e1 * (1 - lam1)  # masa tras agotar el propelente de la etapa 1
    dv1 = G0 * ISP1 * math.log(1 / mf1)
    # etapa 2: masa inicial = lam1; carga util = lam1 * lam2
    m02 = lam1
    mf2 = m02 * (lam2 + e2 * (1 - lam2))
    dv2 = G0 * ISP2 * math.log(m02 / mf2)
    return dv1 + dv2


def optimo_ternario(f=lam_leo):
    lo, hi = 0.05, 0.95
    for _ in range(100):
        a, b = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if f(a) < f(b):
            lo = a
        else:
            hi = b
    return (lo + hi) / 2


def optimo_barrido():
    return max((i / 1000 for i in range(50, 951)), key=lam_leo)


def run():
    f_eq = 0.5
    lam_eq = lam_leo(f_eq)
    f_opt = optimo_ternario()
    f_bar = optimo_barrido()
    lam_opt = lam_leo(f_opt)
    dv_chk = abs(dv_hacia_adelante(lam_etapa(f_opt * DV_LEO, ISP1, E1), lam_etapa((1 - f_opt) * DV_LEO, ISP2, E2)) - DV_LEO)
    carga = lam_opt * M0
    precio_efectivo = PRECIO * (1 - AHORRO)
    c_kg = PRECIO * 1e6 / carga
    c_kg_reut = precio_efectivo * 1e6 / carga
    lam_s = lam_etapa(DV_SUP, ISP_S, E_S)
    c_sup = c_kg / lam_s
    # sensibilidades sobre el costo por kg a superficie
    base = c_sup
    def costo_sup(isp1=ISP1, isp2=ISP2, e1=E1, e2=E2, isp_s=ISP_S, e_s=E_S):
        fopt = optimo_ternario(lambda f: lam_leo(f, isp1, isp2, e1, e2))
        lleo = lam_leo(fopt, isp1, isp2, e1, e2)
        return PRECIO * 1e6 / (lleo * M0) / lam_etapa(DV_SUP, isp_s, e_s)
    R = {"lam_eq": lam_eq, "f_opt": f_opt, "f_bar": f_bar, "dif_f": abs(f_opt - f_bar), "lam_opt": lam_opt, "gana_opt": lam_opt / lam_eq - 1, "dv_chk": dv_chk,
         "carga": carga, "c_kg": c_kg, "c_kg_reut": c_kg_reut, "lam_s": lam_s, "c_sup": c_sup, "razon_sup": c_sup / c_kg,
         "s_isp": costo_sup(isp1=ISP1 + 10, isp2=ISP2 + 10, isp_s=ISP_S + 10) / base - 1, "s_e": costo_sup(e1=E1 + 0.01, e2=E2 + 0.01, e_s=E_S + 0.01) / base - 1,
         "s_dv": None, "c_sup_reut": c_kg_reut / lam_s, "lam1": lam_etapa(f_opt * DV_LEO, ISP1, E1), "lam2": lam_etapa((1 - f_opt) * DV_LEO, ISP2, E2),
         "r_dv": 0.0}
    # sensibilidad a dv (+300 m/s a orbita baja)
    f2 = optimo_ternario(lambda f: lam_leo(f, dv=DV_LEO + 300))
    l2 = lam_leo(f2, dv=DV_LEO + 300)
    R["s_dv"] = (PRECIO * 1e6 / (l2 * M0) / lam_s) / base - 1
    R["s_dv_pct"], R["s_isp_pct"], R["s_e_pct"], R["lam_eq_pct"] = 100 * R["s_dv"], 100 * R["s_isp"], 100 * R["s_e"], 100 * R["lam_eq"]
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Parametros ILUSTRATIVOS: dv a orbita baja = {DV_LEO:.0f} m/s ; etapas Isp {ISP1:.0f}/{ISP2:.0f} s, e = {E1}/{E2} ; lanzador de {M0:.0f} kg a {PRECIO} Mum")
    print(f"Fraccion de carga util con reparto igual de dv: {R['lam_eq']:.5f}")
    print(f"Reparto optimo de dv a la etapa 1: ternario = {R['f_opt']:.4f} ; barrido = {R['f_bar']:.3f} ; diferencia = {R['dif_f']:.4f} ; fraccion optima = {R['lam_opt']:.5f} (+{100 * R['gana_opt']:.2f} %)")
    print(f"  fracciones por etapa: {R['lam1']:.5f} y {R['lam2']:.5f} ; dv recalculado desde masas - dv de diseno (error) = {R['dv_chk']:.2e} m/s")
    print(f"Carga util a orbita baja = {R['carga']:.0f} kg ; costo = {R['c_kg']:.0f} um/kg ; con reutilizacion (-{100 * AHORRO:.0f} % del precio) = {R['c_kg_reut']:.0f} um/kg")
    print(f"Superficie (descenso dv = {DV_SUP:.0f} m/s, Isp {ISP_S:.0f} s, e = {E_S}): fraccion = {R['lam_s']:.5f} ; costo = {R['c_sup']:.0f} um/kg ({R['razon_sup']:.1f} veces el de orbita) ; con reutilizacion = {R['c_sup_reut']:.0f}")
    print(f"Sensibilidades del costo a superficie: Isp +10 s en todas las etapas -> {100 * R['s_isp']:+.1f} % ; e +0.01 -> {100 * R['s_e']:+.1f} % ; dv +300 m/s a orbita baja -> {100 * R['s_dv']:+.1f} %")
    assert R["dv_chk"] < 1e-6 and R["dif_f"] < 0.002 and R["lam_opt"] >= R["lam_eq"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
