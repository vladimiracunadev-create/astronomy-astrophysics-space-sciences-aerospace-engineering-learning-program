#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C03: colapso de pistón de una caldera y hundimiento por volumen evacuado.

Datos: SINTETICOS e ilustrativos (no se modela ninguna caldera real). Resistencia al corte de la falla anular tau, espesor del techo T,
radio R, modulo de compresibilidad efectivo K de la camara y volumen de la camara V_c.
Modelo: un techo cilindrico (pistón) de radio R y espesor T sostenido por la resistencia al corte de la falla anular. La subpresion de la camara
DeltaP respecto de la litostatica carga el pistón hacia abajo con fuerza pi R^2 DeltaP; la resistencia es 2 pi R T tau. Colapso si
DeltaP >= DeltaP_c = 2 T tau / R. La subpresion por volumen evacuado es DeltaP = K dV/V_c (camara elastica linealizada).
Hundimiento del pistón tras el colapso, por balance de volumen: d = V_ev / (pi R^2).
Se verifica DeltaP_c por biseccion sobre el balance de fuerzas y el hundimiento por integracion numerica del volumen del cilindro;
y se recupera por minimos cuadrados el coeficiente 1/pi de d frente a V_ev/R^2 en datos sinteticos con ruido (semilla 20261109).
Supuestos: pistón rigido, falla vertical, techo homogeneo, camara lineal, sin colapso incremental. Validez: ilustrativa.
Tolerancia: 1e-9 relativo en DeltaP_c; 1e-6 en el volumen; 3 errores tipicos en el coeficiente ajustado.
"""
from __future__ import annotations
import math, platform, random

K, VC = 10.0e9, 500.0e9   # Pa, m^3 (ilustrativos)

def dp_critica(T, tau, R):
    return 2 * T * tau / R

def dp_critica_biseccion(T, tau, R):
    resid = lambda dp: math.pi * R**2 * dp - 2 * math.pi * R * T * tau
    lo, hi = 0.0, 1e12
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if resid(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def volumen_cilindro_num(R, d, n=2000):
    h = R / n
    s = 0.0
    for i in range(n):
        r = (i + 0.5) * h
        s += 2 * math.pi * r * d * h
    return s

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    T, tau, R = 2.0e3, 10.0e6, 10.0e3
    dpc = dp_critica(T, tau, R)
    assert abs(dpc - dp_critica_biseccion(T, tau, R)) / dpc < 1e-9
    dV = dpc * VC / K
    print(f"Techo T = {T/1e3:.1f} km, R = {R/1e3:.0f} km, tau = {tau/1e6:.0f} MPa (ilustrativos)")
    print(f"  DeltaP critica = {dpc/1e6:.3f} MPa ; volumen minimo a evacuar = {dV/1e9:.4f} km^3 de {VC/1e9:.0f} km^3 de camara")
    print("Sensibilidad (DeltaP_c proporcional a T/R):")
    for T2, R2 in ((1e3, 10e3), (2e3, 10e3), (4e3, 10e3), (2e3, 20e3), (2e3, 5e3)):
        print(f"  T = {T2/1e3:.0f} km, R = {R2/1e3:.0f} km: DeltaP_c = {dp_critica(T2, tau, R2)/1e6:.2f} MPa ; T/R = {T2/R2:.2f}")
    Vev = 50.0e9
    d = Vev / (math.pi * R**2)
    Vn = volumen_cilindro_num(R, d)
    assert abs(Vn - Vev) / Vev < 1e-6
    print(f"Hundimiento por V_ev = {Vev/1e9:.0f} km^3 sobre R = {R/1e3:.0f} km: d = {d:.1f} m (volumen numerico {Vn/1e9:.4f} km^3)")
    rng = random.Random(20261109)
    xs, ys = [], []
    for _ in range(40):
        r = rng.uniform(3e3, 20e3)
        v = rng.uniform(5e9, 80e9)
        x = v / r**2
        y = x / math.pi * (1 + rng.gauss(0, 0.05))
        xs.append(x); ys.append(y)
    b = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    res = [y - b * x for x, y in zip(xs, ys)]
    s2 = sum(e * e for e in res) / (len(xs) - 1)
    err = math.sqrt(s2 / sum(x * x for x in xs))
    print(f"Ajuste sintetico (40 calderas, ruido 5 %): coeficiente = {b:.5f} +- {err:.5f} ; 1/pi = {1/math.pi:.5f} ; desviacion = {(b-1/math.pi)/err:+.2f} errores tipicos")
    assert abs(b - 1 / math.pi) < 3 * err
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
