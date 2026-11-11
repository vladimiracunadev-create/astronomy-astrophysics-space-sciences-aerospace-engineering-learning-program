#!/usr/bin/env python3
"""B104-C05: atmosfera de cabina: presion parcial de O2, fuga y acumulacion de CO2 (gas ideal).
Cabina y tasas SINTETICAS/ILUSTRATIVAS; las atmosferas de ejemplo no son especificaciones de ninguna nave."""
import sys
import numpy as np

R = 8.314462618          # J/(mol K)
print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: cabina de 30 m3, 294 K, 4 tripulantes; atmosferas de ejemplo (no consultadas)")
V, T, NT = 30.0, 294.0, 4

# (a) Presion parcial de oxigeno segun la mezcla
atm = [("aire a nivel del mar", 101.325, 0.209), ("mezcla enriquecida ilustrativa", 70.3, 0.265),
       ("O2 puro a baja presion ilustrativo", 34.5, 1.0)]
print("\nMezcla | presion total [kPa] | fraccion O2 | pO2 [kPa]")
for n, p, f in atm:
    print(f"{n:38s} {p:8.1f} {f:8.3f} {p*f:8.2f}")
assert abs(atm[0][1] * atm[0][2] - 21.18) < 0.05

# (b) Fuga con flujo proporcional a la sobrepresion (regimen lineal): dp/dt = -p/tau  ->  p(t) = p0 exp(-t/tau)
p0, p_min = 101.325, 70.0
print("\nTiempo para bajar de 101,3 a 70 kPa segun la constante de fuga tau")
for tau_h in (24, 72, 240):
    t_h = tau_h * np.log(p0 / p_min)
    print(f"  tau = {tau_h:4d} h -> {t_h:7.1f} h")
assert abs(72 * np.log(p0 / p_min) - 26.7) < 0.1

# (c) Consumo de O2 y produccion de CO2 sin depuracion
m_o2_dia = 0.84 * NT          # kg/d (ILUSTRATIVO)
m_co2_dia = 1.00 * NT         # kg/d (ILUSTRATIVO)
n_co2_dia = m_co2_dia * 1000 / 44.01          # mol/d
dpco2_dia = n_co2_dia * R * T / V / 1000      # kPa/d
print(f"\nSin depuracion: CO2 producido {m_co2_dia:.1f} kg/d = {n_co2_dia:.0f} mol/d; sube pCO2 {dpco2_dia:.2f} kPa/d en {V:.0f} m3")
t_1kpa = 1.0 / dpco2_dia * 24
print(f"Tiempo para que pCO2 llegue a 1,0 kPa (umbral ILUSTRATIVO) sin depurar: {t_1kpa:.1f} h")
# masa de O2 que equivale a bajar pO2 de 21,2 a 19,0 kPa en la cabina
dn = (21.18 - 19.0) * 1000 * V / (R * T)
print(f"Perder 2,2 kPa de pO2 equivale a {dn*32/1000:.2f} kg de O2 ({dn:.0f} mol)")
assert abs(dpco2_dia - 7.41) < 0.05
assert abs(dn * 32 / 1000 - 0.8) < 0.15
print("Pruebas superadas.")
