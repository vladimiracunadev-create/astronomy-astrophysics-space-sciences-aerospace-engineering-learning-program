#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C06: perfil de gasto de un proyecto frente a un tope anual de financiamiento publico, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de politica publica. El perfil, el tope y el costo de espera son SINTETICOS.
Consultado (2026-11-11), NASA OIG IG-20-005 (noviembre de 2019): al agosto de 2019 el programa de tripulacion comercial habia
comprometido (obligated) unos 5 500 millones de USD de 8 500 millones adjudicados. Es el unico dato real y solo se usa para una proporcion.
Modelo: demanda acumulada D(t) = TOTAL (3u^2 - 2u^3), u = t/8, t en anios; gasto anual = min(tope, atraso + demanda del anio) (recursion de Lindley);
el gasto acumulado cumple C_t = min_{0<=s<=t} (D_s + tope (t - s)) (segunda via). Tras el anio 8 no hay demanda nueva y se paga el atraso.
Costo de espera: cada anio adicional sobre 8 cuesta 6 % del TOTAL (sintetico). TOTAL = 100 unidades de costo sinteticas (uc).
Tolerancias: recursion frente a minimo < 1e-9; tope minimo analitico frente a busqueda < 1e-4.
"""
import platform

TOTAL = 100.0
T = 8
ESPERA = 0.06


def dem_acum(t):
    u = min(max(t / T, 0.0), 1.0)
    return TOTAL * (3 * u * u - 2 * u ** 3)


def demanda(t):
    return dem_acum(t) - dem_acum(t - 1)


def simular(tope, maxanios=60):
    atraso, cum, hist = 0.0, 0.0, []
    for t in range(1, maxanios + 1):
        disp = atraso + demanda(t)
        gasto = min(tope, disp)
        atraso = disp - gasto
        cum += gasto
        hist.append((t, demanda(t), gasto, atraso, cum))
        if cum >= TOTAL - 1e-9:
            return t, hist
    return None, hist


def acum_minimo(tope, t):
    return min(dem_acum(s) + tope * (t - s) for s in range(0, t + 1))


def tope_minimo_analitico():
    return max((TOTAL - dem_acum(s)) / (T - s) for s in range(0, T))


def tope_minimo_busqueda():
    lo, hi = 1.0, 60.0
    for _ in range(80):
        mid = (lo + hi) / 2
        fin, _ = simular(mid)
        if fin is not None and fin <= T:
            hi = mid
        else:
            lo = mid
    return hi


def run():
    tope = 14.0
    fin, hist = simular(tope)
    err = max(abs(h[4] - min(TOTAL, acum_minimo(tope, h[0]))) for h in hist)
    pico = max(demanda(t) for t in range(1, T + 1))
    ta, tb = tope_minimo_analitico(), tope_minimo_busqueda()
    atraso_anios = fin - T
    R = {"tope": tope, "pico": pico, "fin": fin, "atraso": atraso_anios, "err": err, "ta": ta, "tb": tb, "dif_tope": abs(ta - tb),
         "costo_espera": ESPERA * TOTAL * atraso_anios, "crec": 100 * ESPERA * atraso_anios, "frac_obl": 5500.0 / 8500.0,
         "max_atraso": max(h[3] for h in hist), "total": TOTAL, "ratio": pico / (TOTAL / T)}
    for t, d, g, a, c in hist:
        if t <= 11:
            R[f"d{t}"], R[f"g{t}"], R[f"a{t}"] = d, g, a
    return R


def main():
    R = run()
    fin, hist = simular(R["tope"])
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Proyecto SINTETICO: TOTAL = {TOTAL:.0f} uc, 8 anios, tope anual = {R['tope']:.0f} uc ; pico de demanda = {R['pico']:.3f} uc/anio")
    print(f"Dato consultado (NASA OIG IG-20-005, 2019): comprometido/adjudicado = 5500/8500 = {100 * R['frac_obl']:.1f} %")
    print(" anio  demanda  gasto  atraso  acumulado")
    for t, d, g, a, c in hist:
        print(f" {t:4d} {d:8.3f} {g:6.3f} {a:7.3f} {c:10.3f}")
    print(f"Termina en el anio {R['fin']} (atraso de {R['atraso']} anio(s)) ; costo de espera = {R['costo_espera']:.1f} uc = {R['crec']:.1f} % del total")
    print(f"Recursion frente a formula del minimo (error) = {R['err']:.1e}")
    print(f"Tope minimo para terminar en 8 anios: analitico = {R['ta']:.4f} ; busqueda = {R['tb']:.4f} ; diferencia = {R['dif_tope']:.1e}")
    assert R["err"] < 1e-9 and R["dif_tope"] < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
