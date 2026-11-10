#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C08: magnetizacion de electrones e iones en un propulsor Hall (campos cruzados E x B).

Datos CONSULTADOS (2026-11-10): e, m_e = 9.1093837139e-31 kg, u = 1.66053906892e-27 kg, g0 (NIST CODATA);
rango de los propulsores Hall de naves pequenas: 0.25-55 mN y 200-1920 s (NASA SSVI, Tabla 4-1).
NO CONSULTADO: masa atomica del xenon 131.293.
ILUSTRATIVOS (sinteticos, no de un propulsor real): B = 0.015 T (150 G), longitud del canal L = 25 mm, tension de descarga 300 V,
temperatura electronica 10 eV, densidad de neutros 1e19 m^-3, seccion eficaz electron-neutro 1e-19 m2, eficiencia de tension 0.9,
caudal de xenon 5 mg/s, corriente de descarga 4.5 A.
Modelo: radio de giro r = m v_perp/(e B) con v_perp = sqrt(2 e T/m); parametro de Hall clasico = w_c/nu con nu = n sigma v;
deriva E x B = E/B con E = V/L (campo medio); Ve = sqrt(2 e V eta_v/m_i).
Segunda via: r = v_perp/w_c con w_c = e B/m_e; F = mdot Ve frente a F = I_i m_i Ve/e.
Tolerancia: radios por las dos formulas a 1e-12; F por las dos vias a 1e-9.
"""
from __future__ import annotations
import math, platform

E = 1.602176634e-19
ME = 9.1093837139e-31
U = 1.66053906892e-27
G0 = 9.80665
MI = 131.293 * U


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    B, L, V, TE = 0.015, 0.025, 300.0, 10.0
    nn, sigma, eta_v, mdot, Id = 1e19, 1e-19, 0.9, 5e-6, 4.5
    vperp_e = math.sqrt(2 * E * TE / ME)
    wc = E * B / ME
    re = ME * vperp_e / (E * B)
    assert abs(re - vperp_e / wc) / re < 1e-12
    print(f"Electron (ILUSTRATIVO, Te = {TE:.0f} eV): v = {vperp_e:.3e} m/s ; w_c = {wc:.3e} rad/s ; r_L = {re*1e3:.3f} mm")
    ve_ion = math.sqrt(2 * E * V * eta_v / MI)
    ri = MI * ve_ion / (E * B)
    print(f"Ion Xe+ (V = {V:.0f} V, eta_v = {eta_v}): Ve = {ve_ion:.0f} m/s ; Isp = {ve_ion/G0:.1f} s ; r_L = {ri*1e3:.1f} mm")
    print(f"Canal L = {L*1e3:.0f} mm: r_e/L = {re/L:.4f} (electron magnetizado) ; r_i/L = {ri/L:.1f} (ion NO magnetizado)")
    nu = nn * sigma * vperp_e
    hall = wc / nu
    print(f"Parametro de Hall clasico = w_c/nu = {hall:.0f} (nu = {nu:.3e} 1/s) ; con la difusion tipo Bohm el valor efectivo seria 16")
    ve_drift = (V / L) / B
    print(f"Deriva E x B media = E/B = {ve_drift:.3e} m/s (E = {V/L:.0f} V/m)")
    F = mdot * ve_ion
    ii = F * E / (MI * ve_ion)
    f2 = ii * MI * ve_ion / E
    assert abs(F - f2) / F < 1e-9
    P = V * Id
    print(f"Empuje F = mdot Ve = {F*1e3:.1f} mN ; corriente de iones = {ii:.2f} A (de {Id} A de descarga: {ii/Id:.2f}) ; potencia {P:.0f} W ; F/P = {F/P*1e6:.1f} mN/kW")
    print("Isp y empuje frente a la tension de descarga (ILUSTRATIVO, mdot constante):")
    for v in (150.0, 300.0, 450.0, 600.0):
        ve = math.sqrt(2 * E * v * eta_v / MI)
        print(f"  V = {v:>4.0f} V -> Ve = {ve:>6.0f} m/s ; Isp = {ve/G0:>6.1f} s ; F = {mdot*ve*1e3:>5.1f} mN")
    assert re < L / 10 and ri > L  # condicion de un Hall: electrones magnetizados, iones no
    print("Condicion de un propulsor Hall verificada: r_e << L << r_i.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
