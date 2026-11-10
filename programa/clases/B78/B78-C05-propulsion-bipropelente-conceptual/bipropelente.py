#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C05: relacion oxidante/combustible (O/F) de un bipropelente H2/O2 y escape.

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K), g0 = 9.80665 m/s2 (NIST); rango de Isp de mono y bipropelentes
alternativos 150-310 s (Tabla 4-1 NASA SSVI).
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): masas molares H2 = 2.016, O2 = 31.998, H2O = 18.015 g/mol;
calor liberado de 241.8 kJ por mol de H2O (gas); calor especifico molar medio de los productos Cp = 40 J/(mol K);
gamma = 1.20; razon de presiones pc/pe = 100; temperatura inicial 298 K.
Modelo: combustion completa 2 H2 + O2 -> 2 H2O sin disociacion; el reactivo en exceso queda inerte en los productos;
temperatura adiabatica con Cp constante (sobreestima la temperatura, porque ignora la disociacion y la variacion de Cp);
gas ideal, tobera isentropica adaptada. Es un modelo de TENDENCIA, no un calculo de equilibrio quimico.
Segunda via: la razon estequiometrica O/F = M(O2)/(2 M(H2)) y la conservacion de la masa para cada O/F.
Tolerancia: conservacion de masa 1e-12; O/F estequiometrico 7.936 +/- 1e-3.
"""
from __future__ import annotations
import math, platform

R, G0 = 8.314462618, 9.80665
MH2, MO2, MH2O = 2.016e-3, 31.998e-3, 18.015e-3
Q_MOL, CP, GAMMA, RAZON, T0 = 241.8e3, 40.0, 1.20, 100.0, 298.0


def producto(of):
    """Por 1 kg de combustible: moles de H2, O2 en exceso y H2O. of = masa de O2 / masa de H2."""
    n_h2 = 1.0 / MH2
    n_o2 = of / MO2
    reac = min(n_h2, 2 * n_o2)          # mol de H2 que reaccionan
    n_h2o = reac
    h2_ex = n_h2 - reac
    o2_ex = n_o2 - reac / 2
    masa = h2_ex * MH2 + o2_ex * MO2 + n_h2o * MH2O
    assert abs(masa - (1.0 + of)) < 1e-12 * (1.0 + of) + 1e-9
    return n_h2o, h2_ex, o2_ex, h2_ex + o2_ex + n_h2o, masa


def ve_isp(of):
    n_h2o, h2_ex, o2_ex, n, masa = producto(of)
    t = T0 + n_h2o * Q_MOL / (n * CP)
    mm = masa / n
    ve = math.sqrt(2 * GAMMA / (GAMMA - 1) * R * t / mm * (1 - RAZON ** (-(GAMMA - 1) / GAMMA)))
    return t, mm, ve


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    of_st = MO2 / (2 * MH2)
    assert abs(of_st - 7.936) < 1e-3
    print(f"O/F estequiometrico (masa) = {of_st:.3f}")
    print("Bipropelente ILUSTRATIVO H2/O2 (valores de manual no consultados; solo tendencia)")
    print("  O/F    T [K]   M [g/mol]   Ve [m/s]   Isp_ve [s]")
    mejor = (0.0, 0.0)
    for i in range(1, 19):
        of = 0.5 * i
        t, mm, ve = ve_isp(of)
        print(f" {of:>5.1f} {t:>8.1f} {mm*1e3:>10.3f} {ve:>10.1f} {ve/G0:>10.1f}")
        if ve > mejor[1]:
            mejor = (of, ve)
    # refinamiento del maximo por busqueda de seccion aurea y comprobacion contra la malla fina
    a, b = 0.5, 8.5
    fi = (math.sqrt(5) - 1) / 2
    for _ in range(80):
        c, d = b - fi * (b - a), a + fi * (b - a)
        if ve_isp(c)[2] > ve_isp(d)[2]:
            b = d
        else:
            a = c
    of_opt = 0.5 * (a + b)
    fina = max((ve_isp(0.001 * k)[2], 0.001 * k) for k in range(500, 8500))
    assert abs(fina[1] - of_opt) < 2e-3
    print(f"Maximo de Ve (modelo): O/F = {of_opt:.3f} (seccion aurea) ; malla fina: {fina[1]:.3f} ; Ve = {ve_isp(of_opt)[2]:.1f} m/s")
    print(f"Ve en el estequiometrico = {ve_isp(of_st)[2]:.1f} m/s ; en el optimo = {ve_isp(of_opt)[2]:.1f} m/s (diferencia {100*(ve_isp(of_opt)[2]/ve_isp(of_st)[2]-1):.3f} %: sin disociacion el optimo cae en el estequiometrico)")
    print(f"Rango consultado de Isp (alternativos mono y bipropelentes) 150-310 s ; este modelo con H2/O2 da {ve_isp(of_opt)[2]/G0:.0f} s, fuera de rango: es otro propelente y un modelo ideal")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
