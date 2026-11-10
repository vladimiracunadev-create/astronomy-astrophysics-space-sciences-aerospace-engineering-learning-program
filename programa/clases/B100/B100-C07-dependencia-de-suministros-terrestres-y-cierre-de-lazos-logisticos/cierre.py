#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C07: fraccion de suministros que sigue viniendo de la Tierra con lazos cerrados.

ILUSTRATIVOS (no consultados, no medidos): consumo de agua D = 16 kg/d para 4 personas; eficiencia de recuperacion eta = 0, 0.80, 0.90, 0.98;
perdidas por fugas y purgas 0.5 % del flujo por dia sobre el inventario del lazo (en el balance estacionario se agrupan en la eficiencia);
masa del equipo de reciclaje 600 kg; produccion in situ P = 0 o 4 kg/d; repuestos del equipo 8 % de su masa por anio.
Balance estacionario: reposicion terrestre R = max(0, D (1 - eta) - P) + repuestos/365 ; fraccion terrestre = R / D.
Punto de equilibrio del equipo: t_eq = M_equipo / (D eta - repuestos/365) dias.
Segunda via: simulacion diaria de masa con inventario del lazo, 3650 d, con reposicion cuando el inventario baja de un umbral; el promedio de entrega terrestre
se compara con el balance. Tolerancia: 3 % relativa.
"""
from __future__ import annotations
import platform

D = 16.0
M_EQ, REP_ANIO = 600.0, 0.08


def reposicion(eta, p=0.0):
    rep = REP_ANIO * M_EQ / 365.0 if eta > 0 else 0.0
    return max(0.0, D * (1.0 - eta) - p) + rep, rep


def simular(eta, p=0.0, dias=3650):
    inv = 30.0
    umbral, lote = 20.0, 10.0
    entregado = 0.0
    rep = REP_ANIO * M_EQ / 365.0 if eta > 0 else 0.0
    for _ in range(dias):
        inv -= D            # consumo
        inv += D * eta      # recuperado
        inv += p            # produccion in situ
        if inv < umbral:    # reposicion en lotes de masa fija
            n = int((umbral - inv) // lote) + 1
            inv += n * lote
            entregado += n * lote
        entregado += rep    # repuestos del equipo
    return entregado / dias


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos ILUSTRATIVOS: D = 16 kg/d, equipo 600 kg, repuestos 8 %/anio; ningun valor es de una operacion real")
    print(" eta    P [kg/d]   reposicion [kg/d]   fraccion terrestre   simulado [kg/d]   dif. rel.")
    maxdif = 0.0
    for eta, p in ((0.0, 0.0), (0.80, 0.0), (0.90, 0.0), (0.98, 0.0), (0.90, 4.0)):
        r, rep = reposicion(eta, p)
        s = simular(eta, p)
        dif = abs(s - r) / r
        maxdif = max(maxdif, dif)
        print(f"{eta:5.2f}  {p:7.1f}  {r:17.3f}  {r / D * 100:17.1f} %  {s:15.3f}  {dif:9.2e}")
    print("Punto de equilibrio del equipo de reciclaje (600 kg):")
    prev = None
    for eta in (0.80, 0.90, 0.98):
        ahorro = D * eta - REP_ANIO * M_EQ / 365.0
        t_eq = M_EQ / ahorro
        print(f"  eta = {eta:4.2f}: ahorro neto {ahorro:6.3f} kg/d ; equilibrio en {t_eq:6.1f} d")
        if prev is not None:
            assert t_eq < prev
        prev = t_eq
    r98, _ = reposicion(0.98)
    print(f"Con eta = 0.98 la fraccion terrestre baja a {r98 / D * 100:.1f} % pero no a cero: quedan repuestos y fugas")
    assert maxdif < 0.03
    assert r98 > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
