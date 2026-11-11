#!/usr/bin/env python3
"""B104-C04: carga de entrenamiento y modelo de aptitud-fatiga (impulso-respuesta de Banister).
Parametros ILUSTRATIVOS (no consultados en el articulo original). Plan SINTETICO. No es una prescripcion de ejercicio."""
import sys
import numpy as np

K1, K2, TAU1, TAU2 = 0.10, 0.30, 42.0, 7.0   # ILUSTRATIVOS
print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print(f"MODELO ILUSTRATIVO: k1={K1}, k2={K2}, tau1={TAU1} d, tau2={TAU2} d; planes inventados; NO es una prescripcion")

DIAS = 84


def respuesta(w):
    t = np.arange(len(w))
    fit = np.zeros(len(w)); fat = np.zeros(len(w))
    for s in range(len(w)):
        fit[s:] += w[s] * np.exp(-(t[s:] - s) / TAU1)
        fat[s:] += w[s] * np.exp(-(t[s:] - s) / TAU2)
    return K1 * fit, K2 * fat, K1 * fit - K2 * fat


def plan(nombre):
    w = np.zeros(DIAS)
    for d in range(DIAS):
        sem, dia = divmod(d, 7)
        if dia in (0, 2, 4):     # 3 sesiones por semana
            if nombre == "A_constante":
                w[d] = 60
            elif nombre == "B_progresivo_con_descarga":
                base = 40 + 4 * sem
                w[d] = base * (0.5 if sem % 4 == 3 else 1.0)
            elif nombre == "C_misma_carga_total_en_2_dias":
                w[d] = 0
        if nombre == "C_misma_carga_total_en_2_dias" and dia in (0, 3):
            w[d] = 90
    return w


print("\nplan | carga total [u.a.] | aptitud dia 84 | fatiga dia 84 | rendimiento dia 84 | maximo del rendimiento (dia)")
tot = {}
for n in ("A_constante", "B_progresivo_con_descarga", "C_misma_carga_total_en_2_dias"):
    w = plan(n)
    fit, fat, perf = respuesta(w)
    tot[n] = w.sum()
    print(f"{n:30s} {w.sum():8.0f} {fit[-1]:11.2f} {fat[-1]:11.2f} {perf[-1]:11.2f} {perf.max():9.2f} (d {perf.argmax()})")

# TRIMP de Banister (forma ilustrativa) y frecuencia cardiaca de reserva (Karvonen)
fc_reposo, fc_max = 55, 190
for fc in (110, 140, 165):
    x = (fc - fc_reposo) / (fc_max - fc_reposo)
    print(f"FC {fc} lpm: fraccion de reserva {x:.3f}; TRIMP (30 min) = {30 * x * 0.64 * np.exp(1.92 * x):.1f}")

# Prueba analitica: un impulso unico; instante del maximo teorico vs numerico
w = np.zeros(200); w[0] = 100
_, _, perf = respuesta(w)
t_teo = (TAU1 * TAU2 / (TAU1 - TAU2)) * np.log(K2 * TAU1 / (K1 * TAU2))
print(f"\nImpulso unico: maximo teorico en d {t_teo:.2f}; numerico en d {perf.argmax()}")
assert abs(perf.argmax() - t_teo) <= 1.0
assert perf[0] < 0, "inmediatamente despues del impulso predomina la fatiga"
assert abs(tot["A_constante"] - 60 * 36) < 1e-9
print("Pruebas superadas.")
