#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B93-C04: tasa de fallas, MTBF y confiabilidad de una unidad electronica SINTETICA, con y sin redundancia.

Datos consultados (2026-11-10), MIL-HDBK-217F (diciembre de 1991; copia universitaria, lectura de un escaneo con OCR ruidoso):
  Apendice A, ecuacion 1 (conteo de partes): lambda_EQUIP = sum_i N_i (lambda_g * pi_Q)_i, en fallas por 1e6 horas.
  Seccion 6.11 (optoelectronica, LED): lambda_b = 0.00023 fallas/1e6 h; factor de temperatura pi_T = exp(-2790 (1/(Tj+273) - 1/298)) con la tabla
  pi_T(25..115 C) = 1.0 1.2 1.4 1.6 1.8 2.1 2.4 2.7 3.0 3.4 3.8 4.3 4.8 5.3 5.9 6.6 7.3 8.0 8.8; pi_Q: JANTX 1.0, plastico 8.0;
  pi_E: GB 1.0, GF 2.0, GM 8.0, SF (vuelo espacial) 0.50 (por posicion en la fila; el escaneo es ruidoso).
NO CONSULTADOS (relaciones estandar): confiabilidad exponencial R = exp(-lambda t); redundancia activa R = 2e^{-lt} - e^{-2lt};
redundancia fria con conmutador perfecto R = e^{-lt}(1 + lt); constante de Boltzmann 8.617333e-5 eV/K (para convertir 2790 K a energia).
SINTETICOS / ILUSTRATIVOS: la lista de partes, sus cantidades y sus tasas genericas, la mision de 5 anios (43 830 h), las temperaturas.
Supuestos: tasas constantes (sin mortalidad infantil ni desgaste), fallas independientes, partes ya en su entorno de vuelo, conmutador perfecto.
Tolerancias: pi_T calculado frente a la tabla dentro de 0.06; Monte Carlo (semilla 20261110, 400 000 muestras) frente a la formula dentro de 4 sigma binomial.
"""
from __future__ import annotations
import math, platform, random

TABLA_PI_T = {25: 1.0, 30: 1.2, 35: 1.4, 40: 1.6, 45: 1.8, 50: 2.1, 55: 2.4, 60: 2.7, 65: 3.0, 70: 3.4, 75: 3.8,
              80: 4.3, 85: 4.8, 90: 5.3, 95: 5.9, 100: 6.6, 105: 7.3, 110: 8.0, 115: 8.8}
K_EV = 8.617333e-5
HORAS_MISION = 5 * 8766.0  # 5 anios de 365.25 d


def pi_t(tj):
    return math.exp(-2790.0 * (1.0 / (tj + 273.0) - 1.0 / 298.0))


def lambda_led(tj, pi_q, pi_e):
    return 0.00023 * pi_t(tj) * pi_q * pi_e  # fallas / 1e6 h


def mc(lam_h, t, n, rng, modo):
    """Fraccion de muestras vivas en t. modo: 'uno', 'activa', 'fria'."""
    vivos = 0
    for _ in range(n):
        if modo == "uno":
            ok = rng.expovariate(lam_h) > t
        elif modo == "activa":
            ok = max(rng.expovariate(lam_h), rng.expovariate(lam_h)) > t
        else:
            ok = (rng.expovariate(lam_h) + rng.expovariate(lam_h)) > t
        vivos += ok
    return vivos / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dif = max(abs(round(pi_t(t), 1) - v) for t, v in TABLA_PI_T.items())
    dmax = max(abs(pi_t(t) - v) for t, v in TABLA_PI_T.items())
    print(f"pi_T de Arrhenius frente a la tabla del manual (25..115 C): diferencia maxima = {dmax:.3f} (redondeada a 1 decimal: {dif:.1f})")
    assert dmax < 0.06
    print(f"Energia equivalente de 2790 K = {2790*K_EV:.3f} eV")
    print("LED, JANTX, entorno SF (pi_E = 0.50): tasa por 1e6 h segun la temperatura de union")
    for tj in (60, 85, 110):
        print(f"  Tj = {tj:3d} C: pi_T = {pi_t(tj):.2f}; lambda = {lambda_led(tj, 1.0, 0.5):.6f}")
    r = pi_t(110) / pi_t(85)
    print(f"Bajar Tj de 110 a 85 C divide la tasa por {r:.2f} (reduccion del {(1-1/r)*100:.0f} %); plastico en vez de JANTX la multiplica por 8.0")
    # equipo: conteo de partes
    partes = [  # (nombre, N, lambda_g [fallas/1e6 h], pi_Q)   ILUSTRATIVOS salvo el LED (consultado)
        ("CI digital", 14, 0.040, 1.0),
        ("CI lineal", 6, 0.030, 1.0),
        ("capacitor ceramico", 60, 0.0015, 1.0),
        ("capacitor de tantalo", 12, 0.012, 1.0),
        ("resistor de pelicula", 120, 0.0007, 1.0),
        ("conector (contactos)", 4, 0.050, 1.0),
        ("juntas soldadas (lote)", 1, 0.100, 1.0),
        ("LED indicador (Tj 60 C, SF)", 2, lambda_led(60, 1.0, 0.5), 1.0),
    ]
    total = 0.0
    print(f"{'parte':30s} {'N':>4s} {'lambda_g':>9s} {'N*lambda*piQ':>13s}")
    for nombre, n, lg, pq in partes:
        li = n * lg * pq
        total += li
        print(f"{nombre:30s} {n:4d} {lg:9.5f} {li:13.5f}")
    lam_h = total * 1e-6
    mtbf = 1.0 / lam_h
    print(f"lambda_EQUIP = {total:.4f} fallas/1e6 h; MTBF = {mtbf:,.0f} h = {mtbf/8766:.1f} anios")
    t = HORAS_MISION
    r1 = math.exp(-lam_h * t)
    r_act = 2 * math.exp(-lam_h * t) - math.exp(-2 * lam_h * t)
    r_fria = math.exp(-lam_h * t) * (1 + lam_h * t)
    print(f"Mision de {t:,.0f} h: R(una unidad) = {r1:.5f}; activa 1 de 2 = {r_act:.6f}; fria con conmutador perfecto = {r_fria:.6f}")
    print(f"MTTF: una = {1/lam_h:,.0f} h; activa = {1.5/lam_h:,.0f} h (1.5x); fria = {2/lam_h:,.0f} h (2x)")
    # segunda via: Monte Carlo. Para tener senal se acelera la tasa x20 (sintetico) y se compara con la formula a esa tasa
    rng = random.Random(20261110)
    lam_acc = lam_h * 20.0
    n = 400000
    print(f"Monte Carlo (semilla 20261110, n = {n}) con tasa acelerada x20 (lambda = {lam_acc*1e6:.3f} fallas/1e6 h):")
    for modo, f in (("uno", lambda l, t: math.exp(-l * t)),
                    ("activa", lambda l, t: 2 * math.exp(-l * t) - math.exp(-2 * l * t)),
                    ("fria", lambda l, t: math.exp(-l * t) * (1 + l * t))):
        est = mc(lam_acc, t, n, rng, modo)
        ex = f(lam_acc, t)
        sig = math.sqrt(ex * (1 - ex) / n)
        z = (est - ex) / sig
        print(f"  {modo:7s}: formula = {ex:.5f}  Monte Carlo = {est:.5f}  z = {z:+.2f}")
        assert abs(z) < 4.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
