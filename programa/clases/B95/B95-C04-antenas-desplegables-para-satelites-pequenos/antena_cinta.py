#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B95-C04: monopolo de cuarto de onda con cinta elastica enrollada en un tambor, para una cara de 1U.

CONSULTADO: NIST/CODATA, velocidad de la luz en el vacio c = 299 792 458 m/s (valor exacto, definicion del SI; no se re-consulto en linea
  en esta sesion: se usa el valor definicional). NASA State-of-the-Art of Small Spacecraft Technology (2026-11-10), cap. 9, Tabla 9-2:
  ejemplos declarados por fabricantes de antenas desplegables UHF de 0 dBi en 10 x 10 x 3 cm plegada (SENyT); cap. 6: los mecanismos
  contribuyeron a mas del 10 % de las fallas reportadas. CDS Rev. 14.1: 2.4.4 (esperar >= 30 min antes de desplegar), 2.3.8 (3 inhibidores).
ILUSTRATIVOS (sinteticos): frecuencia 437.5 MHz, factor de acortamiento 0.95, cinta de espesor t = 0.1 mm y ancho 6 mm, limite elastico
  de la aleacion 1100 MPa y modulo E = 130 GPa (valores genericos para un resorte de cobre-berilio: NO consultados en una ficha), radio del tambor
  y holgura entre vueltas, volumen disponible 90 x 90 x 10 mm.
Modelo: L = k c / (4 f). Cinta plana enrollada en espiral de Arquimedes: longitud L = pi (r_ext^2 - r_int^2) / (t + h).
  Deformacion de flexion al enrollar en radio r: eps = t / (2 r); tension max sigma = E eps; seguro si sigma <= sigma_y / FS.
Unidades: m, mm donde se indica, Hz, MPa, GPa. Tolerancias: longitud de espiral por dos vias (area y suma de vueltas) < 1e-3 relativa.
"""
from __future__ import annotations
import math, platform

C = 299_792_458.0
F = 437.5e6
K = 0.95
T_MM, H_MM = 0.1, 0.05
E_GPA, SY_MPA, FS = 130.0, 1100.0, 1.5
VOL = (90.0, 90.0, 10.0)  # mm, ILUSTRATIVO: espacio dentro de una cara de 1U
R_INT_MM = 10.0


def longitud_monopolo(f, k=K):
    return k * C / (4.0 * f)


def radio_minimo_mm(t_mm, e_gpa, sy_mpa, fs):
    """eps = t/(2 r) <= sy/(E fs)  ->  r >= t E fs / (2 sy)."""
    return t_mm * (e_gpa * 1e3) * fs / (2.0 * sy_mpa)


def longitud_espiral_area(r_ext, r_int, t, h):
    return math.pi * (r_ext ** 2 - r_int ** 2) / (t + h)


def longitud_espiral_vueltas(r_ext, r_int, t, h):
    paso = t + h
    n = int(round((r_ext - r_int) / paso))
    return sum(2.0 * math.pi * (r_int + (i + 0.5) * paso) for i in range(n))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    L = longitud_monopolo(F)
    lam = C / F
    print(f"Frecuencia ILUSTRATIVA f = {F / 1e6:.1f} MHz ; lambda = {lam * 100:.2f} cm ; L = {K} x lambda/4 = {L * 100:.2f} cm")
    rmin = radio_minimo_mm(T_MM, E_GPA, SY_MPA, FS)
    eps = T_MM / (2.0 * R_INT_MM)
    sig = E_GPA * 1e3 * eps
    print(f"Cinta t = {T_MM} mm: radio interior minimo con FS = {FS}: {rmin:.3f} mm ; usado r_int = {R_INT_MM} mm")
    print(f"  deformacion al enrollar eps = {eps:.5f} ; tension = {sig:.1f} MPa ; limite/FS = {SY_MPA / FS:.1f} MPa ; seguro: {sig <= SY_MPA / FS}")
    # radio exterior del rollo para alojar L
    paso = round(T_MM + H_MM, 6)
    r_ext = math.sqrt(L * 1e3 * paso / math.pi + R_INT_MM ** 2)
    print(f"Rollo en espiral (paso {paso} mm): r_ext necesario = {r_ext:.3f} mm ; diametro = {2 * r_ext:.2f} mm")
    r_ext_q = R_INT_MM + round((r_ext - R_INT_MM) / paso) * paso
    La = longitud_espiral_area(r_ext_q, R_INT_MM, T_MM, H_MM)
    Lv = longitud_espiral_vueltas(r_ext_q, R_INT_MM, T_MM, H_MM)
    print(f"  r_ext cuantizado a vueltas enteras = {r_ext_q:.3f} mm ; L(area) = {La:.2f} mm ; L(vueltas) = {Lv:.2f} mm ; dif. relativa = {abs(La - Lv) / La:.2e}")
    cabe = (2 * r_ext_q <= min(VOL[0], VOL[1])) and (6.0 <= VOL[2])
    print(f"Ancho de cinta 6 mm <= alto disponible {VOL[2]} mm y diametro {2 * r_ext_q:.1f} mm <= {min(VOL[0], VOL[1])} mm: cabe = {cabe}")
    # ganancia ideal de un dipolo/monopolo corto: referencia teorica, no medida
    print(f"Referencia teorica: dipolo de media onda 2.15 dBi ; monopolo de cuarto de onda sobre plano ideal 5.15 dBi (modelo ideal, no medido)")
    # tiempos del CDS
    t_espera = 30.0
    print(f"CDS 2.4.4: despliegue no antes de {t_espera:.0f} min ; si el quemado dura 5 s el despliegue ocurre a {t_espera + 5 / 60:.3f} min")
    # riesgo: probabilidad de que n mecanismos independientes funcionen (ILUSTRATIVO)
    for n, p in ((1, 0.98), (2, 0.98), (4, 0.98)):
        print(f"  {n} mecanismo(s) en serie con fiabilidad ILUSTRATIVA {p}: {p ** n:.4f}")
    assert abs(La - Lv) / La < 1e-3
    assert R_INT_MM >= rmin and sig <= SY_MPA / FS and cabe
    assert abs(L - 0.95 * lam / 4.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
