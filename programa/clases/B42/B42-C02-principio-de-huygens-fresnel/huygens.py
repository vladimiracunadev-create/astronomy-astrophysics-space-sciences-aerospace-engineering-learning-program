#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C02: principio de Huygens-Fresnel con una rendija, suma de ondas secundarias frente a la formula de Fraunhofer.

Datos: ninguna constante fisica. Longitud de onda 633 nm, rendija de 100 um y pantalla a 5 m son ILUSTRATIVAS.
Modelo: campo en la pantalla U(x) = sum_j exp(i k r_j) / sqrt(r_j) sobre N fuentes secundarias uniformes en la rendija (aproximacion
escalar 2D, sin factor de oblicuidad); se compara con I(x) = sinc^2(a x / (lambda z)) en el limite de Fraunhofer. Se calcula el numero de Fresnel
N_F = a^2 / (4 lambda z) (convenio con a ancho completo) para decidir cuando vale cada regimen.
Supuestos: onda plana incidente, rendija infinita en una direccion, aproximacion paraxial. Validez: ilustrativa de la teoria escalar.
Tolerancia: posicion del primer cero a 2 % ; intensidad normalizada a 3e-2 en el lobulo central; N_F << 1 en el campo lejano.
"""
from __future__ import annotations
import cmath, math, platform

LAM = 633e-9
A = 100e-6
Z = 5.0
N = 400

def campo(x, z, a, n):
    k = 2 * math.pi / LAM
    s = 0j
    for j in range(n):
        xs = -a / 2 + (j + 0.5) * a / n
        r = math.hypot(z, x - xs)
        s += cmath.exp(1j * k * r) / math.sqrt(r)
    return s

def sinc2(u):
    return 1.0 if u == 0 else (math.sin(math.pi * u) / (math.pi * u)) ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nf = A * A / (4 * LAM * Z)
    print(f"lambda = {LAM * 1e9:.0f} nm ; a = {A * 1e6:.0f} um ; z = {Z} m ; numero de Fresnel N_F = {nf:.4f}")
    assert nf < 0.05
    i0 = abs(campo(0.0, Z, A, N)) ** 2
    x1 = LAM * Z / A
    print(f"primer cero esperado en x = lambda z / a = {x1 * 1e3:.4f} mm")
    print(f"{'x/(lambda z/a)':>16} {'I suma':>10} {'I sinc2':>10} {'dif':>10}")
    peor = 0.0
    for u in (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5):
        i_num = abs(campo(u * x1, Z, A, N)) ** 2 / i0
        i_teo = sinc2(u)
        peor = max(peor, abs(i_num - i_teo) if u <= 0.75 else 0)
        print(f"{u:16.2f} {i_num:10.4f} {i_teo:10.4f} {i_num - i_teo:+10.4f}")
    assert peor < 3e-2
    # busqueda del primer minimo
    mejor_x, mejor_i = None, 1e9
    for m in range(800, 1201):
        x = x1 * m / 1000.0
        i = abs(campo(x, Z, A, 200)) ** 2 / i0
        if i < mejor_i:
            mejor_i, mejor_x = i, x
    print(f"primer minimo numerico en x = {mejor_x * 1e3:.4f} mm (I = {mejor_i:.2e}) ; error relativo = {abs(mejor_x - x1) / x1:.2%}")
    assert abs(mejor_x - x1) / x1 < 0.02
    # regimen de Fresnel: z corto
    z_cerca = 0.002
    nf2 = A * A / (4 * LAM * z_cerca)
    i_c0 = abs(campo(0.0, z_cerca, A, N)) ** 2
    d = max(abs(abs(campo(u * x1 * z_cerca / Z, z_cerca, A, N)) ** 2 / i_c0 - sinc2(u)) for u in (0.5, 1.0, 1.5))
    print(f"z = {z_cerca} m: N_F = {nf2:.3f} ; maxima diferencia con sinc2 = {d:.3f} (Fraunhofer ya no describe el patron)")
    assert nf2 > 0.5 and d > 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
