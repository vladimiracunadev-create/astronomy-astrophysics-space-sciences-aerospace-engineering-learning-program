#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C03: solucion nutritiva tipo Hoagland, dosificacion y agotamiento en circuito cerrado.

Receta CONSULTADA (Hoagland y Arnon, circular 347, solucion 1; lectura del texto escaneado, 2026-11-10): por litro,
1 mL de KH2PO4, 5 mL de KNO3, 5 mL de Ca(NO3)2 y 2 mL de MgSO4 (el OCR pierde la molaridad de las soluciones madre:
SUPUESTO 1 M) y 1 mL de la solucion de micronutrientes cuyas masas y ppm aparecen en el texto. pH ~ 6.
SINTETICO: el volumen del deposito (40 L), el consumo de agua (8.64 L/dia, de B115-C01) y los factores de absorcion
de iones `a_i` (absorcion = a_i * C_i * Q_agua). ILUSTRATIVO: la conductividad electrica (EC) estimada con
conductividades equivalentes limite estandar (no consultadas) y un factor de actividad. Unidades: mM, mg/L, mS/cm, g, L.
Metodo: (1) comprobar la receta: electroneutralidad y ppm de micronutrientes frente al texto; (2) simular 28 dias
con agua de reposicion pura y tres reglas de dosificacion; (3) comparar la simulacion de Euler con la solucion analitica.
Verificacion: ppm de micronutrientes dentro del 5 % de los del texto; |cationes - aniones| < 1 %; Euler dentro del 1 %.
Solo numpy y la biblioteca estandar.
"""
from __future__ import annotations
import math
import platform
import numpy as np

M = {"K": 39.098, "P": 30.974, "N": 14.007, "O": 15.999, "H": 1.008, "Ca": 40.078, "Mg": 24.305, "S": 32.06,
     "B": 10.81, "Mn": 54.938, "Zn": 65.38, "Cu": 63.546, "Mo": 95.95, "Cl": 35.45}
MM_SAL = {"KH2PO4": 136.086, "KNO3": 101.103, "Ca(NO3)2.4H2O": 236.15, "MgSO4.7H2O": 246.47}
# mM por litro de solucion final (1 mL de solucion madre 1 M por litro = 1 mM) -> iones
RECETA_ML = {"KH2PO4": 1, "KNO3": 5, "Ca(NO3)2": 5, "MgSO4": 2}
IONES = ["K", "Ca", "Mg", "NO3", "H2PO4", "SO4"]
Z = {"K": 1, "Ca": 2, "Mg": 2, "NO3": 1, "H2PO4": 1, "SO4": 2}
LAMBDA_EQ = {"K": 73.5, "Ca": 59.5, "Mg": 53.0, "NO3": 71.4, "H2PO4": 36.0, "SO4": 80.0}  # S cm2/eq (estandar, no consultado)
ELEM_DE_ION = {"K": "K", "Ca": "Ca", "Mg": "Mg", "NO3": "N", "H2PO4": "P", "SO4": "S"}
N_ATOMOS = {"K": 1, "Ca": 1, "Mg": 1, "NO3": 1, "H2PO4": 1, "SO4": 1}


def receta_mM():
    r = RECETA_ML
    return {"K": r["KH2PO4"] + r["KNO3"], "Ca": r["Ca(NO3)2"], "Mg": r["MgSO4"], "NO3": r["KNO3"] + 2 * r["Ca(NO3)2"],
            "H2PO4": r["KH2PO4"], "SO4": r["MgSO4"]}


def ec_estimada(c):
    """EC en mS/cm a partir de mM por ion (conductividades limite con un factor de actividad 1 - 0.6 sqrt(I))."""
    eq = {i: c[i] * Z[i] / 1000.0 for i in IONES}
    fuerza = 0.5 * sum(c[i] / 1000.0 * Z[i] ** 2 for i in IONES)
    f = max(0.5, 1 - 0.6 * math.sqrt(fuerza))
    return f * sum(LAMBDA_EQ[i] * eq[i] for i in IONES)


def ppm(c):
    return {ELEM_DE_ION[i]: c[i] * M[ELEM_DE_ION[i]] for i in IONES}


MICRO = [  # compuesto, g/L de la solucion madre, masa molar, fraccion del elemento, elemento, ppm del texto
    ("H3BO3", 2.86, 61.83, M["B"] / 61.83, "B", 0.5),
    ("MnCl2.4H2O", 1.81, 197.91, M["Mn"] / 197.91, "Mn", 0.5),
    ("ZnSO4.7H2O", 0.22, 287.56, M["Zn"] / 287.56, "Zn", 0.05),
    ("CuSO4.5H2O", 0.08, 249.68, M["Cu"] / 249.68, "Cu", 0.02),
    ("H2MoO4.H2O (85 % MoO3)", 0.09, 161.97, 0.85 * M["Mo"] / 143.95, "Mo", 0.05),
]


def simular(regla, dias=28, dt=0.01, v=40.0, q=8.64, a=None, c0=None, ec0=None):
    a = a or {"K": 0.6, "Ca": 0.2, "Mg": 0.3, "NO3": 0.5, "H2PO4": 0.6, "SO4": 0.15}
    c = dict(c0)
    r = receta_mM()
    eventos, sal_mM = 0, {i: 0.0 for i in IONES}
    hist = []
    pasos_dia = int(round(1 / dt))
    for k in range(int(round(dias / dt)) + 1):
        if k % pasos_dia == 0:
            hist.append(dict(c))
            if regla == "ec" and ec_estimada(c) < 0.8 * ec0:
                lo, hi = 0.0, 1.0
                for _ in range(60):
                    s = 0.5 * (lo + hi)
                    if ec_estimada({i: c[i] + s * r[i] for i in IONES}) < ec0:
                        lo = s
                    else:
                        hi = s
                for i in IONES:
                    c[i] += hi * r[i]
                    sal_mM[i] += hi * r[i]
                eventos += 1
            elif regla == "ion" and any(c[i] < 0.8 * r[i] for i in IONES):
                for i in IONES:
                    if c[i] < 0.8 * r[i]:
                        sal_mM[i] += r[i] - c[i]
                        c[i] = r[i]
                eventos += 1
        for i in IONES:
            c[i] -= a[i] * q / v * c[i] * dt
    return hist, eventos, sal_mM


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: receta de Hoagland y Arnon (consultada, molaridad de las madres supuesta 1 M); consumo y absorcion SINTETICOS")
    r = receta_mM()
    cat = sum(r[i] * Z[i] for i in ("K", "Ca", "Mg"))
    ani = sum(r[i] * Z[i] for i in ("NO3", "H2PO4", "SO4"))
    print("Receta (solucion 1) en mM: " + ", ".join(f"{i} {r[i]:.0f}" for i in IONES))
    print(f"   cationes = {cat:.0f} meq/L; aniones = {ani:.0f} meq/L (electroneutralidad)")
    p = ppm(r)
    print("   ppm de elemento: " + ", ".join(f"{k} {v:.1f}" for k, v in p.items()))
    ec0 = ec_estimada(r)
    fuerza = 0.5 * sum(r[i] / 1000 * Z[i] ** 2 for i in IONES)
    print(f"   fuerza ionica = {fuerza*1000:.1f} mM; EC estimada = {ec0:.2f} mS/cm (ilustrativa, +-15 %)")
    assert abs(cat - ani) / cat < 0.01

    sales = {"KH2PO4": r["H2PO4"], "KNO3": RECETA_ML["KNO3"], "Ca(NO3)2.4H2O": r["Ca"], "MgSO4.7H2O": r["Mg"]}
    print("Masas de sal para 40 L (g): " + ", ".join(f"{n} {MM_SAL[n] * mM * 40 / 1000:.2f}" for n, mM in sales.items()))

    print("Micronutrientes: 1 mL de solucion madre por litro (comprobacion contra los ppm del texto)")
    for nom, g, mm, frac, el, texto in MICRO:
        ppm_calc = g * frac            # mg/L con 1 mL/L: g/L * 1 mL/L = mg/L
        err = abs(ppm_calc - texto) / texto
        print(f"   {el:2s} desde {nom:24s}: {ppm_calc:.3f} mg/L (texto {texto}); error {err*100:.1f} %")
        assert err < 0.05

    print("Agotamiento en circuito cerrado (28 dias, V = 40 L, agua de reposicion pura, factores a_i sinteticos)")
    c0 = dict(r)
    hist, _, _ = simular("ninguna", c0=c0, ec0=ec0)
    a_ref = {"K": 0.6, "Ca": 0.2, "Mg": 0.3, "NO3": 0.5, "H2PO4": 0.6, "SO4": 0.15}
    err_max = 0.0
    for d in (7, 14, 28):
        for i in IONES:
            ana = c0[i] * math.exp(-a_ref[i] * 8.64 / 40.0 * d)
            err_max = max(err_max, abs(hist[d][i] - ana) / c0[i])
    print(f"   Euler (dt = 0.01 d) frente a la solucion analitica: error maximo = {err_max:.2e} de la concentracion inicial")
    assert err_max < 0.01
    print("   dia   EC[mS/cm]   %N   %P   %K  %Ca  %Mg   %S")
    for d in (0, 7, 14, 21, 28):
        h = hist[d]
        print(f"   {d:3d}   {ec_estimada(h):8.2f} " + " ".join(f"{100*h[i]/r[i]:4.0f}" for i in ("NO3", "H2PO4", "K", "Ca", "Mg", "SO4")))

    for regla, nombre in (("ec", "Regla A: reponer receta completa cuando la EC baja al 80 %"),
                          ("ion", "Regla B: reponer cada ion hasta su objetivo cuando baja al 80 %")):
        hist, ev, sal = simular(regla, c0=c0, ec0=ec0)
        desv = max(abs(hist[28][i] / r[i] - 1) for i in IONES)
        rel = [hist[d]["Ca"] / hist[d]["NO3"] / (r["Ca"] / r["NO3"]) for d in range(29)]
        print(f"{nombre}")
        print(f"   eventos = {ev}; EC dia 28 = {ec_estimada(hist[28]):.2f} mS/cm; razon Ca/N respecto de la receta: dia 14 = {rel[14]:.2f}, dia 28 = {rel[28]:.2f}")
        print("   porcentaje del objetivo en el dia 28: " + " ".join(f"{i} {100*hist[28][i]/r[i]:.0f}" for i in IONES))
        print(f"   desviacion maxima de un ion en el dia 28 = {desv*100:.0f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
