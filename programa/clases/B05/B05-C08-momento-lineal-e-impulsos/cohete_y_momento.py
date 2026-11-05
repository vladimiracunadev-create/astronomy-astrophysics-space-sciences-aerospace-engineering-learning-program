#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C08: conservación del momento lineal y ecuación del cohete.

Datos: SINTÉTICOS (masas, velocidad de escape de gases y acoplamiento inventados para
enseñanza). Modelo: expulsión de masa en N paquetes iguales con velocidad relativa v_e
constante, en una recta y sin fuerzas externas; se compara con la ecuación de Tsiolkovsky
dv = v_e ln(m0/mf). Supuestos: 1D, sin gravedad ni atmósfera, v_e constante.
Dominio de validez: v mucho menor que c. Tolerancia: error relativo < 1e-3 con N = 10 000.
"""
from __future__ import annotations
import math
import sys

def cohete_discreto(m0: float, mf: float, ve: float, n: int) -> float:
    """dv tras expulsar (m0-mf) en n paquetes iguales, conservando el momento en cada paso."""
    dm = (m0 - mf) / n
    m, v = m0, 0.0
    for _ in range(n):
        # m v = (m-dm)(v+dv) + dm (v+dv-ve)  =>  dv = dm*ve/(m)   (se usa m antes de expulsar)
        v += dm * ve / m
        m -= dm
    return v

def acoplamiento(m1: float, v1: float, m2: float, v2: float) -> float:
    return (m1 * v1 + m2 * v2) / (m1 + m2)

def main() -> int:
    m0, mf, ve = 1000.0, 400.0, 3000.0
    dv_ana = ve * math.log(m0 / mf)
    dv_num = cohete_discreto(m0, mf, ve, 10_000)
    assert abs(dv_num - dv_ana) / dv_ana < 1e-3, (dv_num, dv_ana)
    v = acoplamiento(2000.0, 1.0, 500.0, -0.5)
    assert abs((2000 + 500) * v - (2000 * 1.0 + 500 * -0.5)) < 1e-12
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Tsiolkovsky: dv = {dv_ana:.2f} m/s (m0/mf = {m0/mf:.2f}, v_e = {ve:.0f} m/s)")
    for n in (1, 10, 100, 10_000):
        d = cohete_discreto(m0, mf, ve, n)
        print(f"  N = {n:6d} paquetes: dv = {d:8.2f} m/s (error rel. {abs(d-dv_ana)/dv_ana:.2e})")
    print(f"Acoplamiento 2000 kg a 1,0 m/s con 500 kg a -0,5 m/s: v final = {v:.4f} m/s")
    ek0 = 0.5 * 2000 * 1.0**2 + 0.5 * 500 * 0.5**2
    ek1 = 0.5 * 2500 * v**2
    print(f"Energía cinética: antes {ek0:.2f} J, después {ek1:.2f} J (se disipa {ek0-ek1:.2f} J)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
