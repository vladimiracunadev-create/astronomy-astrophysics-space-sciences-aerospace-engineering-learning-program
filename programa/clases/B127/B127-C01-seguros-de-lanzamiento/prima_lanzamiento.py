#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C01: tasa de prima de un lanzamiento SINTETICO.

CONTENIDO EDUCATIVO: no es una cotizacion ni asesoria financiera, legal o de seguros.
Consultado (2026-11-11): 14 CFR parte 440 (via resumen): la cobertura orbital llega hasta el mayor de 30 dias tras la
separacion de la carga o 30 dias desde el encendido (concepto de ventana de cobertura). Ningun numero sale de ahi.
ILUSTRATIVOS (sinteticos): probabilidad de exito, distribucion de resultados parciales, valor asegurado y recargo.
Modelo: resultados mutuamente excluyentes {exito, perdida parcial (fraccion f), perdida total}; pago = f * valor asegurado.
Prima pura = sum(p_i * f_i) * V; tasa pura = prima pura / V; prima comercial = prima pura * (1 + recargo).
Unidades: millones de USD ficticios (MUSD). Tolerancias: Monte Carlo (200000 lanzamientos, semilla 127) frente a la
formula cerrada: error relativo de la perdida media < 2 %.
"""
from __future__ import annotations
import platform, random

V = 200.0  # valor asegurado, MUSD ficticios
RESULTADOS = [  # nombre, probabilidad, fraccion de perdida
    ("exito", 0.940, 0.0),
    ("perdida parcial leve", 0.025, 0.25),
    ("perdida parcial grave", 0.015, 0.60),
    ("perdida total", 0.020, 1.00),
]
RECARGO = 0.35


def tasa_pura(res):
    return sum(p * f for _, p, f in res)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS; solo la ventana de 30 dias de 14 CFR 440 es conceptual y consultada.")
    assert abs(sum(p for _, p, _ in RESULTADOS) - 1.0) < 1e-12
    tp = tasa_pura(RESULTADOS)
    prima_pura = tp * V
    prima = prima_pura * (1 + RECARGO)
    print(f"Valor asegurado V = {V:.1f} MUSD ; recargo = {RECARGO:.0%}")
    print(f"Tasa pura = {tp:.4%} ; prima pura = {prima_pura:.3f} MUSD")
    print(f"Prima comercial = {prima:.3f} MUSD ; tasa comercial = {prima / V:.4%}")
    # Monte Carlo
    rng = random.Random(127)
    n = 200000
    acum = [p for _, p, _ in RESULTADOS]
    for i in range(1, len(acum)):
        acum[i] += acum[i - 1]
    tot, ntot, nfallo = 0.0, 0, 0
    for _ in range(n):
        u = rng.random()
        for (nom, _, f), c in zip(RESULTADOS, acum):
            if u < c:
                tot += f * V
                nfallo += f > 0
                ntot += f == 1.0
                break
    mc = tot / n
    err = abs(mc - prima_pura) / prima_pura
    print(f"Monte Carlo ({n} lanzamientos): perdida media = {mc:.3f} MUSD ; error relativo = {err:.2%}")
    print(f"Frecuencia de siniestro MC = {nfallo / n:.4f} (teorica 0.0600) ; perdida total MC = {ntot / n:.4f} (teorica 0.0200)")
    # sensibilidad a la probabilidad de exito: se mueve masa de 'exito' a 'perdida total'
    print("Sensibilidad: tasa comercial segun la probabilidad de perdida total")
    for pt in (0.010, 0.020, 0.040, 0.080):
        res = [("exito", 0.940 - (pt - 0.020), 0.0)] + RESULTADOS[1:3] + [("perdida total", pt, 1.0)]
        print(f"  P(total) = {pt:.3f} -> tasa comercial = {tasa_pura(res) * (1 + RECARGO):.4%}")
    # relacion prima / perdida maxima
    print(f"Perdida maxima por lanzamiento = {V:.1f} MUSD ; prima/perdida maxima = {prima / V:.2%}")
    assert err < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
