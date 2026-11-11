#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C05: VPN, TIR y sensibilidad de un negocio espacial SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion.
Consultado (2026-11-11): Circular A-94 de la OMB (revision del 2023-11-09; PDF leido con PyMuPDF): la tasa de descuento debe corresponder a
la medicion de los flujos (real para flujos en dolares constantes, nominal para flujos nominales; seccion 8.a); los resultados deben
recalcularse para ver su sensibilidad a los supuestos principales (seccion 9.c); el Apendice B ilustra el descuento con una tasa de 3,1 %
solo como ejemplo. Esa circular guia el analisis de programas federales de EE. UU. y NO fija la tasa de una empresa privada.
ILUSTRATIVOS (sinteticos): los flujos de caja (los del caso base de B126-C03, anos 0 a 9, M USD constantes), las tasas de 6 a 14 %,
la inflacion de 3 % y el valor terminal nulo.
Pruebas: (1) VPN(TIR) = 0 (1e-9); (2) TIR por biseccion frente a Newton (1e-9); (3) VPN nominal a tasa nominal = VPN real a tasa real
(relacion de Fisher, 1e-9); (4) VPN por suma directa frente a evaluacion de Horner (1e-9).
"""
from __future__ import annotations
import platform

FLUJOS = [-21.00, -17.00, -8.75, 6.75, 20.875, 31.375, 39.25, 44.5, 47.125, 48.4375]  # M USD constantes (caso base de C03)
CLIENTES = [0, 0, 20, 60, 110, 150, 180, 200, 210, 215]


def vpn(f, r):
    return sum(x / (1 + r) ** t for t, x in enumerate(f))


def vpn_horner(f, r):
    acc = 0.0
    for x in reversed(f):
        acc = x + acc / (1 + r)
    return acc


def tir_biseccion(f, lo=-0.5, hi=5.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        if vpn(f, lo) * vpn(f, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def tir_newton(f, r=0.1):
    for _ in range(100):
        d = sum(-t * x / (1 + r) ** (t + 1) for t, x in enumerate(f))
        n = r - vpn(f, r) / d
        if abs(n - r) < 1e-14:
            return n
        r = n
    return r


def payback_desc(f, r):
    acc = 0.0
    for t, x in enumerate(f):
        acc += x / (1 + r) ** t
        if acc >= 0:
            return t
    return None


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); de la Circular A-94 solo se consultaron la regla de tasa real/nominal y la sensibilidad (2026-11-11).")
    print("Unidades: M USD constantes; anos 0 a 9; valor terminal nulo")
    for r in (0.06, 0.08, 0.10, 0.12, 0.14):
        a, b = vpn(FLUJOS, r), vpn_horner(FLUJOS, r)
        assert abs(a - b) < 1e-9
        print(f" tasa {r:4.0%}: VPN = {a:8.2f} M USD ; payback descontado = ano {payback_desc(FLUJOS, r)}")
    t1, t2 = tir_biseccion(FLUJOS), tir_newton(FLUJOS)
    print(f"TIR (biseccion) = {t1:.6%} ; TIR (Newton) = {t2:.6%} ; VPN(TIR) = {vpn(FLUJOS, t1):.2e}")
    assert abs(t1 - t2) < 1e-9 and abs(vpn(FLUJOS, t1)) < 1e-9
    # Fisher: flujos nominales a tasa nominal = flujos reales a tasa real
    pi, real = 0.03, 0.10
    nominal = (1 + real) * (1 + pi) - 1
    f_nom = [x * (1 + pi) ** t for t, x in enumerate(FLUJOS)]
    v_real, v_nom = vpn(FLUJOS, real), vpn(f_nom, nominal)
    print(f"Fisher: real 10 % e inflacion 3 % -> nominal {nominal:.4%} ; VPN real = {v_real:.6f} ; VPN nominal = {v_nom:.6f}")
    assert abs(v_real - v_nom) < 1e-9
    v_mal = vpn(f_nom, real)
    print(f"Error tipico (flujos nominales con tasa real): VPN = {v_mal:.2f} M USD (sobrestima {v_mal - v_real:.2f})")
    print("Sensibilidad del VPN (M USD) al factor de ingresos y a la tasa (flujo = ingreso*factor*0,75 - costos fijos - capex)")
    ing = [c * 0.35 for c in CLIENTES]
    # reconstruir costos no variables: flujo = 0,75*ing - resto  ->  resto = 0,75*ing - flujo
    resto = [0.75 * i - f for i, f in zip(ing, FLUJOS)]
    tasas = (0.06, 0.10, 0.14)
    print("   factor  " + "".join(f"{r:>10.0%}" for r in tasas) + "     TIR")
    for k in (0.6, 0.8, 1.0, 1.2):
        f = [0.75 * i * k - x for i, x in zip(ing, resto)]
        print(f"   {k:5.1f}   " + "".join(f"{vpn(f, r):10.2f}" for r in tasas) + f"   {tir_biseccion(f):7.2%}")
    k_eq = None
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        f = [0.75 * i * mid - x for i, x in zip(ing, resto)]
        if vpn(f, 0.10) > 0:
            hi = mid
        else:
            lo = mid
    k_eq = (lo + hi) / 2
    print(f"Factor de ingresos con VPN = 0 a 10 %: {k_eq:.4f} (los ingresos pueden caer {1-k_eq:.1%} antes de perder valor)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
