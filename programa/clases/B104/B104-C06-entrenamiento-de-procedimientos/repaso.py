#!/usr/bin/env python3
"""B104-C06: curva de aprendizaje potencial, curva de olvido y calendario de repaso.
DATOS SINTETICOS (semilla 104); parametros ILUSTRATIVOS (no consultados)."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): tiempos de ejecucion generados con T(n) = T1 n^-alfa y ruido; parametros ilustrativos")
rng = np.random.default_rng(104)
T1, ALFA = 600.0, 0.30   # s, ley de practica (ILUSTRATIVO)

# (a) Ajuste de la ley de practica en log-log
n = np.arange(1, 31)
t = T1 * n ** (-ALFA) * np.exp(0.05 * rng.standard_normal(n.size))
pend, orig = np.polyfit(np.log(n), np.log(t), 1)
print(f"\nAjuste log-log: alfa = {-pend:.3f} (verdad {ALFA}); T1 = {np.exp(orig):.1f} s (verdad {T1})")
print("n | T(n) verdad [s] | T(n) ajustado [s]")
for k in (1, 5, 10, 20, 30):
    print(f"{k:3d} {T1*k**-ALFA:10.1f} {np.exp(orig)*k**pend:10.1f}")
assert abs(-pend - ALFA) < 0.03

# (b) Olvido: retencion R = exp(-dt/S); S crece con cada repaso espaciado (ILUSTRATIVO: S0 = 5 d, factor 2,5)
S0, G = 5.0, 2.5


def retencion(repasos, dia):
    S, ultimo = S0, 0.0
    for r in repasos:
        S *= G if r > 0 else 1.0
        ultimo = r
    return np.exp(-(dia - ultimo) / S)


plan_masivo = [0.0] * 1            # 10 repeticiones el dia 0 (una sola "sesion" con S = S0 sin crecer)
masivo = np.exp(-90 / S0)
espaciado_dias = [0.0, 3.0, 10.0, 25.0, 55.0]
S = S0; ult = 0.0
for r in espaciado_dias[1:]:
    S *= G
    ult = r
espaciado = np.exp(-(90 - ult) / S)
print(f"\nRetencion a los 90 dias: masivo (todo el dia 0) = {masivo:.4f}; espaciado ({espaciado_dias}) = {espaciado:.4f}")
print(f"Tiempo esperado de ejecucion a los 90 dias con n = 30 repeticiones y espaciado: T/retencion = {T1*30**-ALFA/espaciado:.0f} s (con retencion casi nula el modelo no es util: se reinicia el aprendizaje)")
assert espaciado > masivo
assert espaciado < 1.0
# (c) Intervalo de repaso para mantener retencion >= 0,8
for S_ in (5.0, 12.5, 31.25):
    print(f"  con S = {S_:6.2f} d, retencion >= 0,8 durante {S_*np.log(1/0.8):5.2f} d")
assert abs(5.0 * np.log(1 / 0.8) - 1.116) < 0.001
print("Pruebas superadas.")
