#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B68-C03: pulverizacion de hielos por iones pesados, dosis, valor G y cinetica de destruccion con productos.

Datos publicados (Dartois et al. 2021, A&A 647, A177, arXiv:2102.04499, texto completo consultado el 2026-11-09), con Se en eV por 1e15 moleculas cm^-2:
 - Rendimiento de pulverizacion de pelicula gruesa Y_inf = Y0 Se^2, con Y0 = 3,87e-2 (CO), 8,65e-3 (CO2) y 5,93e-3 (H2O) [moleculas/ion por (eV/1e15 cm^-2)^2].
 - Pelicula delgada: Y_s(N, Se) = Y0 Se^2 [1 - exp(-N/Nd(Se))], con la profundidad de pulverizacion Nd = 10^14,25 Se^0,95 cm^-2 (CO) y 10^13,20 Se^1,18 cm^-2 (CO2)
   (ajustes de las figuras 8 y 7 de ese articulo; para el H2O el articulo da solo Y0 y aqui no se calcula el efecto del espesor).
 - Temperatura ~10 K; iones pesados rapidos (no protones de baja energia ni rayos cosmicos reales).
SINTETICO / ILUSTRATIVO: los valores de Se evaluados (10, 50, 100), los espesores, y los valores G de destruccion y formacion (20 y 5 moleculas por 100 eV)
de la cadena A -> B -> C. No se integra ningun espectro de rayos cosmicos (no se consulto ningun flujo). 1 ML = 1e15 moleculas cm^-2 (convencion).
Definiciones: dosis D [eV/molecula] = fluencia [iones cm^-2] x Se / 1e15; valor G = moleculas formadas o destruidas por 100 eV depositados, de modo que k = G/100 por (eV/molecula).
Modelo: cinetica de primer orden en la dosis, dA/dD = -k1 A ; dB/dD = k1 A - k2 B ; C = 1 - A - B (fracciones de la cantidad inicial de A).
Referencia independiente: solucion cerrada de Bateman frente a RK4. Tolerancias: Bateman frente a RK4 < 1e-8; cociente Y(2Se)/Y(Se) = 4 exacto en pelicula gruesa.
Unidades: Se en eV por 1e15 moleculas cm^-2; rendimiento en moleculas/ion; espesor en ML; dosis en eV/molecula.
"""
from __future__ import annotations
import math, platform

Y0 = {"CO": 3.87e-2, "CO2": 8.65e-3, "H2O": 5.93e-3}
ND = {"CO": (10 ** 14.25, 0.95), "CO2": (10 ** 13.20, 1.18)}
ML = 1e15


def y_inf(esp: str, Se: float) -> float:
    return Y0[esp] * Se ** 2


def nd(esp: str, Se: float) -> float:
    a, p = ND[esp]
    return a * Se ** p  # cm^-2


def y_s(esp: str, N_ml: float, Se: float) -> float:
    return y_inf(esp, Se) * (1.0 - math.exp(-N_ml * ML / nd(esp, Se)))


def dosis(fluencia: float, Se: float) -> float:
    return fluencia * Se / ML


def bateman(k1: float, k2: float, D: float):
    A = math.exp(-k1 * D)
    B = k1 / (k2 - k1) * (math.exp(-k1 * D) - math.exp(-k2 * D))
    return A, B, 1.0 - A - B


def rk4(k1: float, k2: float, Dmax: float, n: int):
    h = Dmax / n
    A, B = 1.0, 0.0
    f = lambda A, B: (-k1 * A, k1 * A - k2 * B)
    for _ in range(n):
        a1, b1 = f(A, B)
        a2, b2 = f(A + h / 2 * a1, B + h / 2 * b1)
        a3, b3 = f(A + h / 2 * a2, B + h / 2 * b2)
        a4, b4 = f(A + h * a3, B + h * b3)
        A += h / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
        B += h / 6 * (b1 + 2 * b2 + 2 * b3 + b4)
    return A, B, 1.0 - A - B


def calcular():
    Ses = (10.0, 50.0, 100.0)
    tabla_inf = [(esp, Se, y_inf(esp, Se)) for esp in Y0 for Se in Ses]
    espesores = (1.0, 10.0, 100.0)
    tabla_s = []
    for esp in ("CO", "CO2"):
        for Se in Ses:
            tabla_s.append((esp, Se, nd(esp, Se) / ML, [y_s(esp, N, Se) / y_inf(esp, Se) for N in espesores]))
    # fluencia para pulverizar 1 ML de CO grueso con Se = 100
    Y_co_100 = y_inf("CO", 100.0)
    fluencia_1ml = ML / Y_co_100
    # N = Nd da 1 - 1/e
    Nd_co_50 = nd("CO", 50.0)
    frac_Nd = y_s("CO", Nd_co_50 / ML, 50.0) / y_inf("CO", 50.0)
    # cinetica A -> B -> C con G sinteticos
    G1, G2 = 20.0, 5.0
    k1, k2 = G1 / 100.0, G2 / 100.0
    Dstar = math.log(k1 / k2) / (k1 - k2)
    Bmax = bateman(k1, k2, Dstar)[1]
    filas = []
    err_max = 0.0
    for D in (2.0, 5.0, Dstar, 15.0, 30.0):
        a = bateman(k1, k2, D)
        r = rk4(k1, k2, D, 2000)
        err_max = max(err_max, max(abs(x - y) for x, y in zip(a, r)))
        filas.append((D, a))
    # fluencia de iones (Se = 100, SINTETICO) para alcanzar D*
    flu_D = Dstar * ML / 100.0
    # tiempo de ensayo si el flujo de iones fuese 1e9 iones cm^-2 s^-1 (SINTETICO)
    t_ens = flu_D / 1e9
    return dict(tabla_inf=tabla_inf, tabla_s=tabla_s, espesores=espesores, fluencia_1ml=fluencia_1ml, frac_Nd=frac_Nd,
                k1=k1, k2=k2, Dstar=Dstar, Bmax=Bmax, filas=filas, err_max=err_max, flu_D=flu_D, t_ens=t_ens, Nd_co_50=Nd_co_50)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Pulverizacion de pelicula gruesa, Y_inf = Y0 Se^2 [moleculas/ion] (Dartois 2021):")
    for esp, Se, y in r["tabla_inf"]:
        print(f"  {esp:>4} Se = {Se:5.0f} eV/1e15 cm^-2 -> Y_inf = {y:10.2f}")
    print("Pelicula delgada: Nd [ML] y Y_s/Y_inf para N = " + ", ".join(f"{n:g} ML" for n in r["espesores"]))
    for esp, Se, nd_ml, fr in r["tabla_s"]:
        print(f"  {esp:>4} Se = {Se:5.0f} -> Nd = {nd_ml:9.2f} ML ; " + " ; ".join(f"{f:.4f}" for f in fr))
    print(f"CO, Se = 100: fluencia para pulverizar 1 ML grueso = {r['fluencia_1ml']:.3e} iones cm^-2")
    print(f"CO, Se = 50: con N = Nd ({r['Nd_co_50'] / ML:.2f} ML), Y_s/Y_inf = {r['frac_Nd']:.5f} (teorico 1 - 1/e = {1 - 1 / math.e:.5f})")
    print(f"Cadena A->B->C SINTETICA: G1 = 20, G2 = 5 moleculas/100 eV -> k1 = {r['k1']:.2f}, k2 = {r['k2']:.2f} por (eV/molecula)")
    print(f"{'D [eV/mol]':>11} {'A':>9} {'B':>9} {'C':>9}")
    for D, (A, B, C) in r["filas"]:
        print(f"{D:11.3f} {A:9.5f} {B:9.5f} {C:9.5f}")
    print(f"Dosis del maximo de B: D* = ln(k1/k2)/(k1-k2) = {r['Dstar']:.3f} eV/molecula ; B(D*) = {r['Bmax']:.5f}")
    print(f"Diferencia maxima Bateman - RK4 = {r['err_max']:.2e}")
    print(f"Con Se = 100 (SINTETICO): fluencia para D* = {r['flu_D']:.3e} iones cm^-2 ; a 1e9 iones cm^-2 s^-1 -> {r['t_ens']:.2e} s")
    # pruebas
    assert abs(y_inf("CO", 100.0) / y_inf("CO", 50.0) - 4.0) < 1e-12
    assert r["err_max"] < 1e-8
    assert abs(r["frac_Nd"] - (1 - 1 / math.e)) < 1e-12
    for esp, Se, nd_ml, fr in r["tabla_s"]:
        assert fr[0] < fr[1] <= fr[2] <= 1.0
    A, B, C = r["filas"][2][1]
    assert abs(B - r["Bmax"]) < 1e-12 and abs(A + B + C - 1.0) < 1e-12
    eps = 1e-4
    assert bateman(r["k1"], r["k2"], r["Dstar"] - eps)[1] < r["Bmax"] > bateman(r["k1"], r["k2"], r["Dstar"] + eps)[1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
