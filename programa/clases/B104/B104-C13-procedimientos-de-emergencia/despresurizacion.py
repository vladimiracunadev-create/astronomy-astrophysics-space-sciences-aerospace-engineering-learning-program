#!/usr/bin/env python3
"""B104-C13: despresurizacion de una cabina por un orificio (flujo ahogado) y margen de tiempo de respuesta.
Cabina, orificios y umbrales ILUSTRATIVOS (no son de ninguna nave); gas ideal isotermo (simplificacion)."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: cabina de 30 m3 a 294 K, aire, orificio con Cd = 0,6; exterior en vacio; umbral de 70 kPa ilustrativo")
V, T, P0, CD = 30.0, 294.0, 101_325.0, 0.6
GAM, RS = 1.4, 287.05
FAC = (2 / (GAM + 1)) ** ((GAM + 1) / (2 * (GAM - 1)))     # 0,5787 para gamma = 1,4


def tau(d_mm):
    A = np.pi * (d_mm * 1e-3 / 2) ** 2
    return V / (CD * A * np.sqrt(GAM * RS * T) * FAC)


def tiempo_a(p_obj, d_mm):
    return tau(d_mm) * np.log(P0 / p_obj)


print(f"factor de flujo ahogado (2/(g+1))^((g+1)/(2(g-1))) = {FAC:.4f}")
print("\ndiametro [mm] | tau [h] | t hasta 70 kPa [min] | t hasta 50 kPa [min]")
res = {}
for d in (1, 3, 6, 10, 30):
    res[d] = tiempo_a(70e3, d)
    print(f"{d:12d} {tau(d)/3600:11.2f} {res[d]/60:16.1f} {tiempo_a(50e3, d)/60:18.1f}")

# verificacion numerica por Euler (6 mm)
d = 6
dt, p, t = 0.5, P0, 0.0
k = 1 / tau(d)
while p > 70e3:
    p -= dt * k * p
    t += dt
print(f"\nVerificacion Euler (6 mm): {t/60:.2f} min frente a analitico {res[6]/60:.2f} min")

# Margen frente a un tiempo de respuesta ilustrativo
T_RESP = 15 * 60       # 15 min para detectar, decidir y actuar (ILUSTRATIVO)
print(f"\nTiempo de respuesta ilustrativo: {T_RESP/60:.0f} min; margen = t(70 kPa) - respuesta")
for d in (1, 3, 6, 10, 30):
    m = res[d] - T_RESP
    print(f"  {d:3d} mm: margen {m/60:8.1f} min {'(INSUFICIENTE)' if m < 0 else ''}")
# tamano de orificio que deja exactamente el tiempo de respuesta
d_crit = d_c = 6 * np.sqrt(res[6] / T_RESP)
print(f"Diametro que agota el tiempo de respuesta antes de 70 kPa: {d_crit:.1f} mm")

assert abs(t - res[6]) / res[6] < 0.005
assert abs(res[3] / res[6] - 4.0) < 1e-9, "el tiempo es inversamente proporcional al area"
assert abs(FAC - 0.5787) < 1e-4
assert res[30] < T_RESP < res[6]
print("Pruebas superadas.")
