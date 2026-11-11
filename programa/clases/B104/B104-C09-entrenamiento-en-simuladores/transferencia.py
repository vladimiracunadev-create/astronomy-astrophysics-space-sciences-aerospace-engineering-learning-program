#!/usr/bin/env python3
"""B104-C09: razon de efectividad de transferencia (TER) de un simulador y punto de equilibrio de costos.
DATOS SINTETICOS (semilla 104); costos y parametros ILUSTRATIVOS."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): horas hasta el criterio en el sistema real, con y sin horas previas de simulador; costos ilustrativos")
Y0, YMAX, X0 = 20.0, 12.0, 6.0         # horas reales sin simulador; maximo ahorro; escala de saturacion
C_REAL, C_SIM = 20000.0, 800.0         # costo por hora (ILUSTRATIVO)


def y_medio(x):
    return Y0 - YMAX * (1 - np.exp(-x / X0))


def ter(x):
    return (Y0 - y_medio(x)) / x


print("\nhoras en simulador x | horas reales hasta el criterio | ahorro | TER | costo total [miles]")
costos = {}
for x in (0, 2, 5, 10, 20, 40):
    y = y_medio(x)
    costo = x * C_SIM + y * C_REAL
    costos[x] = costo
    t = ter(x) if x else float('nan')
    print(f"{x:20d} {y:30.2f} {Y0-y:8.2f} {t:7.3f} {costo/1000:14.1f}")

xs = np.linspace(0, 60, 6001)
costo_x = xs * C_SIM + y_medio(xs) * C_REAL
x_opt = xs[costo_x.argmin()]
x_teo = X0 * np.log(YMAX * C_REAL / (X0 * C_SIM))
print(f"\nHoras de simulador que minimizan el costo: numerico {x_opt:.2f}; teorico X0 ln(YMAX C_REAL/(X0 C_SIM)) = {x_teo:.2f}")

# Estimacion de TER con 30 aprendices por grupo (ruido log-normal)
rng = np.random.default_rng(104)
x = 10
boot = []
ctrl = Y0 * np.exp(0.2 * rng.standard_normal(30))
sim = y_medio(x) * np.exp(0.2 * rng.standard_normal(30))
for _ in range(2000):
    c = rng.choice(ctrl, 30); s = rng.choice(sim, 30)
    boot.append((c.mean() - s.mean()) / x)
lo, hi = np.percentile(boot, [2.5, 97.5])
print(f"TER medido con 30 por grupo (x = {x} h): {(ctrl.mean()-sim.mean())/x:.3f}; intervalo 95 % por remuestreo [{lo:.3f}, {hi:.3f}]; verdad {ter(x):.3f}")

assert abs(x_opt - x_teo) < 0.05
assert ter(2) > ter(5) > ter(10) > ter(40), "TER decrece con las horas (saturacion)"
assert costos[10] < costos[0]
assert lo < ter(x) < hi * 1.5
print("Pruebas superadas.")
