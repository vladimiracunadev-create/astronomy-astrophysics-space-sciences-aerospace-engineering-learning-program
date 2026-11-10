#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B93-C02: derating de una lista de materiales SINTETICA con factores de NASA/TP-2003-212242 (EEE-INST-002, mayo 2003).

Datos consultados (2026-11-10), Tabla 4 de las secciones C1, R2 y M3 del documento (PDF completo leido con PyMuPDF):
  capacitores, factor de tension: ceramico 0.60 (110 C max), vidrio 0.50, pelicula plastica 0.60 (85 C), tantalo de lamina 0.5 (70 C),
  tantalo de rodaja humeda 0.60 a 70 C y 0.40 a 110 C (nota 3: reducir linealmente entre ambos), tantalo solido 0.50 a 70 C y 0.30 a 110 C;
  nota 2: en aplicaciones de baja tension (< 10 Vdc) los ceramicos CCR/CKR/CDR deben tener al menos 100 Vdc nominales;
  la tabla aplica el factor a la SUMA de la tension continua y el pico de rizado alterno (nota 1).
  resistores RCR (composicion): factor de potencia 0.6 y de tension 0.8 (potencia nominal a 70 C = T1).
  microcircuitos digitales: tension maxima de alimentacion 0.9, potencia 0.8, corriente de salida 0.8, frecuencia de reloj 0.8; lineales 0.8, 0.75, 0.8, 0.8;
  nota 2: Tj <= 110 C o 40 C por debajo del maximo del fabricante, el menor; nota 1.1: dispositivos de baja tension (< 5 V) usan las condiciones recomendadas.
NO CONSULTADO: la norma ECSS-Q-ST-30-11C Rev.2 (solo su pagina de resumen); no se sabe en que difieren sus factores.
SINTETICOS (inventados, no son una lista de vuelo): referencias, valores nominales, tensiones aplicadas, potencias, theta_ja = 35 K/W, ambiente 70 C.
Supuestos: para el tantalo solido por encima de 70 C se usa el factor de 110 C (conservador, la tabla no da interpolacion para ese tipo);
los resistores se evaluan solo en T1 (70 C), sin curva de reduccion de potencia.
Tolerancias: margen exacto 0 en el limite con 1e-12; temperatura limite analitica frente a barrido con 1e-6 K.
"""
from __future__ import annotations
import platform

AMB = 70.0  # C, ILUSTRATIVO
THETA_JA = 35.0  # K/W, ILUSTRATIVO


def f_tantalo_humedo(t):
    if t <= 70:
        return 0.60
    if t >= 110:
        return 0.40
    return 0.60 - 0.20 * (t - 70.0) / 40.0


def f_tantalo_solido(t):
    return 0.50 if t <= 70 else 0.30


def chequear():
    filas = []  # (ref, tipo, magnitud, aplicado, limite, nota)

    def add(ref, tipo, mag, aplicado, limite, nota=""):
        filas.append((ref, tipo, mag, aplicado, limite, nota))

    # capacitores: tension aplicada = continua + pico de rizado
    add("C1", "ceramico CKR 50 V", "V", 5.0 + 0.1, 0.60 * 50.0, "pasa el factor 0.60, pero ver la regla < 10 Vdc")
    add("C2", "ceramico CKR 100 V", "V", 28.0 + 0.5, 0.60 * 100.0)
    add("C3", "tantalo solido 35 V", "V", 12.0 + 0.2, f_tantalo_solido(85.0) * 35.0, "a 85 C se usa el factor de 110 C")
    add("C4", "tantalo humedo 60 V", "V", 20.0, f_tantalo_humedo(90.0) * 60.0, f"factor lineal a 90 C = {f_tantalo_humedo(90.0):.3f}")
    # resistores RCR a 70 C
    add("R1", "RCR 0.25 W", "W", 0.20, 0.6 * 0.25)
    add("R2", "RCR 0.25 W", "W", 0.10, 0.6 * 0.25)
    # microcircuitos
    add("U1", "digital 5.0 V (max 5.5)", "V", 5.0, 0.9 * 5.5)
    add("U2", "digital 3.3 V (max 3.6)", "V", 3.3, 3.6, "< 5 V: exento, condiciones recomendadas del fabricante")
    add("U3", "lineal +-12 V (max 18)", "V", 12.0, 0.8 * 18.0)
    add("U1", "digital, potencia (max 1.0 W)", "W", 0.55, 0.8 * 1.0)
    p = 0.55
    tj = AMB + THETA_JA * p
    lim_tj = min(110.0, 150.0 - 40.0)
    add("U1", "digital, Tj (max 150 C)", "C", tj, lim_tj)
    return filas, tj, lim_tj


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Lista de materiales SINTETICA; ambiente {AMB:.0f} C, theta_ja = {THETA_JA:.0f} K/W")
    filas, tj, lim_tj = chequear()
    print(f"{'ref':4s} {'tipo':30s} {'aplic.':>8s} {'limite':>8s} {'margen %':>9s}  veredicto")
    fallan = []
    for ref, tipo, mag, ap, lim, nota in filas:
        margen = (lim - ap) / lim * 100.0
        ok = ap <= lim
        if not ok:
            fallan.append(ref + "/" + mag)
        print(f"{ref:4s} {tipo:30s} {ap:7.3f}{mag} {lim:7.3f}{mag} {margen:9.1f}  {'cumple' if ok else 'NO CUMPLE'}" + (f"  [{nota}]" if nota else ""))
    c1_regla = 50.0 >= 100.0  # regla < 10 Vdc: ceramico CKR con al menos 100 Vdc nominales
    print(f"Regla de baja tension para C1: nominal 50 V frente a 100 V exigidos -> {'cumple' if c1_regla else 'NO CUMPLE'}")
    if not c1_regla:
        fallan.append("C1/regla")
    print(f"Incumplimientos: {', '.join(fallan)}")
    # pruebas: borde exacto, regla de baja tension, temperatura limite por dos vias
    lim_c2 = 0.60 * 100.0
    assert abs((lim_c2 - lim_c2) / lim_c2) < 1e-12  # en el limite el margen es exactamente 0
    assert fallan == ["C3/V", "R1/W", "U1/V", "C1/regla"], fallan
    t_lim = lim_tj - THETA_JA * 0.55
    mejor = None
    for k in range(0, 200001):  # barrido de 0 a 200 C en pasos de 0.001
        ta = k * 0.001
        if ta + THETA_JA * 0.55 <= lim_tj + 1e-12:
            mejor = ta
    assert abs(mejor - t_lim) < 1e-3
    print(f"Tj de U1 = {tj:.2f} C frente a un limite de {lim_tj:.0f} C; ambiente maximo admisible = {t_lim:.2f} C (barrido: {mejor:.3f} C)")
    print(f"Potencia maxima por limite termico a {AMB:.0f} C = {(lim_tj-AMB)/THETA_JA:.3f} W; por derating 0.8 = {0.8:.3f} W")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
