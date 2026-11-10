#!/usr/bin/env python3
"""B72-C16 — Modelado de mareas.

Modelo de mareas de Q constante para el sistema Tierra-Luna: radio sincrono, aceleracion de marea en
la superficie, marea de equilibrio, tasa de variacion del semieje da/dt = 3 (k2/Q)(m/M)(R/a)^5 n a,
integral de da/dt (RK4 frente a la solucion analitica) y balance de momento angular.
k2/Q, h2 y el momento de inercia son ILUSTRATIVOS. Unidades SI. Solo biblioteca estandar.
"""
import math
import sys

MU_T = 3.986004e14          # m3/s2, (GM)N Tierra (IAU 2015)
MU_L = 4902.800e9           # m3/s2, JPL SSD
M_T = 5.9722e24             # kg (NSSDC)
M_L = 0.07346e24            # kg (NSSDC)
R_T = 6378137.0             # m (NSSDC, ecuatorial)
R_MEDIO = 6371.0e3          # m (NSSDC, volumetrico medio)
A_L = 0.3844e9              # m (NSSDC)
T_L = 27.3217 * 86400.0     # s (NSSDC)
OM_T = 2 * math.pi / (23.9345 * 3600.0)   # rad/s (NSSDC)
ANO = 365.25 * 86400.0

K2_Q = 0.01     # ILUSTRATIVO
H2 = 0.6        # ILUSTRATIVO
ALFA = 0.33     # ILUSTRATIVO, I = ALFA M R^2

print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print(f"ILUSTRATIVOS: k2/Q = {K2_Q}, h2 = {H2}, I = {ALFA} M R^2. Datos de masa, radio, distancia y periodos de las fichas NSSDC.")

# 1) Radio sincrono
a_sinc = (MU_T / OM_T ** 2) ** (1.0 / 3.0)
print(f"\nRadio sincrono de la Tierra: a_sinc = (mu/w^2)^(1/3) = {a_sinc / 1e3:.1f} km ; a_Luna/a_sinc = {A_L / a_sinc:.2f} (la Luna esta fuera: la marea la aleja)")
assert A_L > a_sinc

# 2) Aceleracion de marea y marea de equilibrio
a_marea = 2 * MU_L * R_T / A_L ** 3
print(f"\nAceleracion de marea lunar en la superficie: 2 mu_L R/d^3 = {a_marea:.3e} m/s2 = {a_marea / 9.80665:.2e} g")
dh = 1.5 * H2 * (M_L / M_T) * (R_T / A_L) ** 3 * R_T
print(f"Marea de equilibrio ILUSTRATIVA (h2 = {H2}): (3/2) h2 (m/M) (R/d)^3 R = {dh:.3f} m")

# 3) da/dt
n = 2 * math.pi / T_L
def dadt(a, k2q=K2_Q):
    n_ = math.sqrt(MU_T / a ** 3)
    return 3 * k2q * (M_L / M_T) * (R_T / a) ** 5 * n_ * a
r0 = dadt(A_L)
print(f"\nda/dt hoy = 3 (k2/Q)(m/M)(R/a)^5 n a = {r0:.3e} m/s = {r0 * ANO * 100:.2f} cm/ano")
k2q_38 = K2_Q * (0.038 / ANO) / r0
print(f"(k2/Q que daria 3.8 cm/ano, cifra de medidas laser lunares NO consultada: {k2q_38:.4f})")

# 4) Integracion de da/dt (a^-11/2) hacia atras: de a0 a 0.5 a0
C = r0 * A_L ** 5.5          # da/dt = C a^-5.5
def rk4_a(a, dt):
    f = lambda x: C * x ** -5.5
    k1 = f(a); k2 = f(a + dt / 2 * k1); k3 = f(a + dt / 2 * k2); k4 = f(a + dt * k3)
    return a + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
a = A_L; t = 0.0; dt = -1.0e13
while a > 0.5 * A_L:
    a_nuevo = rk4_a(a, dt)
    if a_nuevo < 0.5 * A_L:
        dt = dt * (a - 0.5 * A_L) / (a - a_nuevo)
        a = rk4_a(a, dt); t += dt
        break
    a, t = a_nuevo, t + dt
t_num = -t
t_ana = (A_L ** 6.5 - (0.5 * A_L) ** 6.5) / (6.5 * C)
print(f"\nTiempo para que a pase de a0 a 0.5 a0 (hacia atras, k2/Q constante): numerico = {t_num / ANO / 1e9:.4f} Ga ; analitico = {t_ana / ANO / 1e9:.4f} Ga ; dif. = {abs(t_num - t_ana) / t_ana:.2e}")
assert abs(t_num - t_ana) / t_ana < 1e-6

# 5) Balance de momento angular y alargamiento del dia
dL = M_L * math.sqrt(MU_T) / (2 * math.sqrt(A_L)) * r0
I = ALFA * M_T * R_MEDIO ** 2
dw = -dL / I
dia = 2 * math.pi / OM_T
dT = -dw / OM_T * dia
print(f"\nMomento angular orbital ganado por la Luna: dL/dt = {dL:.3e} kg m2/s2")
print(f"Perdido por la rotacion terrestre: d(omega)/dt = {dw:.3e} rad/s2 -> el dia sideral crece {dT * 1e3 * 100 * ANO:.2f} ms por siglo (solo esta marea y k2/Q ilustrativo)")
print("Pruebas superadas.")
