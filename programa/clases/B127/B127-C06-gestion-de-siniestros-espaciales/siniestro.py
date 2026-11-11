#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C06: liquidacion de un siniestro SINTETICO y calendario de plazos.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de seguros; no sustituye a un perito ni a un abogado.
Consultado (2026-11-11): Convenio de Responsabilidad 1972 (compilacion UNOOSA ST/SPACE/61/Rev.1): Art. IX (via diplomatica),
Art. X (reclamacion como maximo un anio tras el dano o la identificacion del Estado de lanzamiento; revision hasta un anio
despues de conocida la extension), Art. XIV (Comision de Reclamaciones si no hay arreglo un anio despues de notificada la
documentacion). Son plazos entre ESTADOS; aqui se usan como ejemplo de calendario, no como plazos de una poliza.
Consultado (via resumen): 14 CFR 440.13/440.15: el aviso y la evidencia tienen plazos explicitos.
ILUSTRATIVOS: capacidad perdida, umbral de perdida total, salvamento, deducible, fechas, distribucion del tiempo de peritaje.
Modelo: pago = max(0, perdida_bruta - salvamento - deducible), con perdida total constructiva si la capacidad perdida >= umbral;
perdida_bruta = valor asegurado * (1 si total, si no fraccion de capacidad perdida).
Unidades: MUSD ficticios, dias. Tolerancias: Monte Carlo (100000 expedientes, semilla 127) frente al valor esperado: < 1 %.
"""
from __future__ import annotations
import datetime as dt, math, platform, random

V = 120.0
DEDUCIBLE = 3.0
UMBRAL_TOTAL = 0.75
SALVAMENTO_TOTAL = 4.0


def liquidar(fraccion_perdida, salvamento_total=SALVAMENTO_TOTAL):
    total = fraccion_perdida >= UMBRAL_TOTAL
    bruta = V if total else V * fraccion_perdida
    salv = salvamento_total if total else 0.0
    return total, bruta, salv, max(0.0, bruta - salv - DEDUCIBLE)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Expedientes SINTETICOS; consultados solo los plazos de los Arts. IX, X y XIV del Convenio de 1972 (entre Estados).")
    print(f"V = {V} MUSD ; deducible = {DEDUCIBLE} ; umbral de perdida total = {UMBRAL_TOTAL:.0%} ; salvamento si total = {SALVAMENTO_TOTAL}")
    print(" capacidad perdida  total?  bruta  salvam.  pago")
    for f in (0.10, 0.30, 0.60, 0.74, 0.75, 0.90):
        t, b, s, p = liquidar(f)
        print(f" {f:15.0%}  {str(t):6s} {b:6.1f} {s:7.1f} {p:6.2f}")
    # salto en el umbral
    _, _, _, p_justo_antes = liquidar(0.74)
    _, _, _, p_umbral = liquidar(0.75)
    print(f"Salto de pago al cruzar el umbral: {p_justo_antes:.2f} -> {p_umbral:.2f} MUSD")
    # calendario a la manera del Convenio (ejemplo, fechas ficticias)
    dano = dt.date(2027, 3, 14)
    limite_x = dano.replace(year=dano.year + 1)
    notifica_doc = dt.date(2027, 9, 1)
    comision_xiv = notifica_doc.replace(year=notifica_doc.year + 1)
    print(f"Calendario ejemplo: dano {dano} ; reclamacion (Art. X) hasta {limite_x} ({(limite_x - dano).days} dias)")
    print(f"  documentacion notificada {notifica_doc} ; Comision de Reclamaciones (Art. XIV) a pedido desde {comision_xiv}")
    # Monte Carlo: fraccion de perdida ~ Beta(0.6, 1.4) (sintetica) y tiempo de peritaje lognormal
    rng = random.Random(127)
    n = 100000
    pagos = dias = 0.0
    ntot = 0
    for _ in range(n):
        f = rng.betavariate(0.6, 1.4)
        t, b, s, p = liquidar(f)
        ntot += t
        pagos += p
        dias += rng.lognormvariate(math.log(90), 0.5)
    # valor esperado por integracion numerica (punto medio) de la densidad Beta(0.6, 1.4)
    a_, b_ = 0.6, 1.4
    B = math.gamma(a_) * math.gamma(b_) / math.gamma(a_ + b_)
    m = 20000
    esp = 0.0
    ptot = 0.0
    for i in range(m):
        x = (i + 0.5) / m
        dens = x ** (a_ - 1) * (1 - x) ** (b_ - 1) / B / m
        esp += liquidar(x)[3] * dens
        ptot += dens * (x >= UMBRAL_TOTAL)
    err = abs(pagos / n - esp) / esp
    print(f"Pago esperado por siniestro: integracion = {esp:.3f} ; Monte Carlo = {pagos / n:.3f} MUSD ; error relativo = {err:.2%}")
    print(f"P(perdida total): integracion = {ptot:.4f} ; Monte Carlo = {ntot / n:.4f}")
    print(f"Tiempo medio de peritaje (lognormal, mediana 90 d, sigma 0.5): {dias / n:.1f} d (teorico {90 * math.exp(0.125):.1f})")
    assert err < 0.01
    assert abs(dias / n - 90 * math.exp(0.125)) / (90 * math.exp(0.125)) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
