#!/usr/bin/env python3
"""B104-C11: modelo de tejido de Haldane (un compartimento) para entender la preoxigenacion antes de bajar la presion.
Tiempos medios y razon critica ILUSTRATIVOS (no consultados). Modelo educativo: NO es una pauta de descompresion."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: tiempos medios 5-360 min y razones criticas inventadas; NO es una pauta de descompresion")
P_CAB, F_N2 = 101.325, 0.79
P_TRAJE = 29.6             # kPa (4,3 psi), cifra vista solo en un resultado de busqueda; no consultada
P0 = F_N2 * P_CAB


def n2_tejido(t_min, t_med, p_alv=0.0):
    k = np.log(2) / t_med
    return p_alv + (P0 - p_alv) * np.exp(-k * t_min)


def t_hasta(R, t_med, p0=P0, p_traje=P_TRAJE):
    # tiempo en O2 al 100 % hasta que pN2_tejido / P_traje <= R
    return t_med / np.log(2) * np.log(p0 / (R * p_traje))


print(f"\npN2 inicial en el tejido: {P0:.2f} kPa; presion del traje {P_TRAJE} kPa -> razon inicial {P0/P_TRAJE:.2f}")
print("t medio [min] | razon critica | tiempo de preoxigenacion [min]")
filas = {}
for t_med in (5, 40, 120, 360):
    for R in (1.4, 2.0):
        t = max(0.0, t_hasta(R, t_med))
        filas[(t_med, R)] = t
        print(f"{t_med:12d} {R:14.1f} {t:22.1f}")

# Atmosfera de cabina de menor presion (ILUSTRATIVA 70,3 kPa con 73,5 % de N2)
p0b = 0.735 * 70.3
print(f"\nCabina ilustrativa de 70,3 kPa (73,5 % N2): pN2 tejido {p0b:.1f} kPa; razon inicial {p0b/P_TRAJE:.2f}")
for t_med, R in ((360, 1.4), (360, 2.0)):
    print(f"  t medio {t_med} min, razon {R}: {max(0.0, t_hasta(R, t_med, p0b)):.1f} min")

# Verificacion numerica de la solucion exacta
t = np.linspace(0, 600, 60001)
num = P0 * np.ones_like(t)
k = np.log(2) / 120
dt = t[1] - t[0]
for i in range(1, len(t)):
    num[i] = num[i - 1] + dt * k * (0.0 - num[i - 1])
print(f"\nEuler frente a exacta (t medio 120 min, t = 600 min): {num[-1]:.5f} frente a {n2_tejido(600, 120):.5f} kPa")

assert abs(num[-1] - n2_tejido(600, 120)) < 1e-3
assert filas[(360, 1.4)] > filas[(360, 2.0)] > 0
assert filas[(5, 2.0)] < filas[(360, 2.0)]
assert abs(n2_tejido(120, 120) - P0 / 2) < 1e-9, "tras un tiempo medio queda la mitad"
print("Pruebas superadas.")
