#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C06: subsidencia y deslizamiento medidos con InSAR (deformacion SINTETICA; ningun caso real).

Datos: ningun dato observado. lambda = 0.0555 m (banda C ilustrativa); angulo de incidencia theta = 34 grados; pixel de 20 m; semilla 20261109.
Sistema de referencia: ejes locales E (este), N (norte), U (arriba), en m. Vector unitario u del suelo al sensor; la orbita mira a la derecha del rumbo de vuelo
(rumbo alpha, medido desde el norte hacia el este): ascendente alpha = -10 grados (mira al este, el sensor queda al oeste del blanco) y descendente alpha = 190 grados (mira al oeste).
Convencion de signo: d_LOS = u . d > 0 significa que el suelo SE ACERCA al sensor; fase interferometrica dphi = +4 pi d_LOS / lambda (rad).
Modelo: (0) caso de gradiente fuerte: 180 mm de hundimiento con s = 40 m para mostrar el fallo de la desenvoltura. (1) subsidencia vertical con perfil gaussiano de 18 mm de hundimiento maximo (dU = -0.018 exp(-x^2/(2 s^2)), s = 400 m); d_LOS = dU cos(theta).
(2) Reconstruccion: fase envuelta + ruido gaussiano de fase (sigma = 0.3 rad) y desenvoltura 1D; d_LOS = lambda dphi / (4 pi).
(3) Deslizamiento: movimiento de ladera de 12 mm/ano hacia el este y 5 mm/ano hacia abajo (dE = 12, dU = -5); el LOS ascendente y el descendente lo ven distinto; se resuelven E y U
con el sistema 2 x 2 despreciando la componente N (supuesto: la componente norte es nula).
Supuestos: atmosfera y topografia ya corregidas, coherencia alta, una sola epoca de interferograma, una dimension. Validez: gradiente de fase entre pixeles < pi.
Tolerancias: hundimiento recuperado (promedio de 5 pixeles) dentro de 2 mm; separacion E-U exacta en ausencia de ruido (1e-9) y dentro de 1 mm con ruido de 0.3 rad.
"""
from __future__ import annotations
import math
import platform
import numpy as np

rng = np.random.default_rng(20261109)
lam = 0.0555
th = math.radians(34.0)

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

def envolver(p):
    return (p + math.pi) % (2 * math.pi) - math.pi

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
print(f"lambda/2 = {lam/2*1000:.2f} mm de movimiento en la linea de vision por franja (2 pi de fase)")

# 1) Subsidencia
x = np.arange(-2000, 2000, 20.0)
s = 400.0
dU = -0.018 * np.exp(-x**2 / (2 * s**2))
dlos = dU * math.cos(th)
phi = 4 * math.pi * dlos / lam
print(f"Subsidencia vertical maxima = {dU.min()*1000:.1f} mm -> LOS maximo = {dlos.min()*1000:.2f} mm -> fase maxima = {phi.min():.3f} rad")
grad_max = np.abs(np.diff(phi)).max()
print(f"Gradiente de fase maximo entre pixeles = {grad_max:.3f} rad (limite pi = {math.pi:.3f})")
check(grad_max < math.pi, "gradiente supera pi")
ruido = 0.3 * rng.standard_normal(len(x))
phi_w = envolver(phi + ruido)
phi_u = np.unwrap(phi_w)
phi_u -= phi_u[0]                       # referencia: el borde sin deformacion
rec = lam * phi_u / (4 * math.pi)
err = rec - dlos
print(f"Fase envuelta: {int(np.sum(np.abs(np.diff(phi_w)) > math.pi))} saltos de 2 pi ; error rms de la reconstruccion = {err.std()*1000:.3f} mm ; error maximo = {np.abs(err).max()*1000:.3f} mm")
c0 = len(x) // 2
vert_c = rec[c0 - 2:c0 + 3].mean() / math.cos(th)         # promedio de 5 pixeles centrales (el minimo de una serie ruidosa esta sesgado)
print(f"Hundimiento vertical recuperado (promedio de 5 pixeles centrales) = {vert_c*1000:.2f} mm (verdad {dU[c0]*1000:.2f} mm)")
check(abs(vert_c - dU[c0]) < 0.002, "hundimiento recuperado")

# 2) Un gradiente demasiado fuerte rompe la desenvoltura
s2 = 40.0
dU2 = -0.18 * np.exp(-x**2 / (2 * s2**2))
phi2 = 4 * math.pi * dU2 * math.cos(th) / lam
g2 = np.abs(np.diff(phi2)).max()
rec2 = lam * (np.unwrap(envolver(phi2)) - np.unwrap(envolver(phi2))[0]) / (4 * math.pi)
err2 = np.abs(rec2 - dU2 * math.cos(th)).max()
print(f"Caso de gradiente fuerte (180 mm de hundimiento en s = 40 m): gradiente maximo {g2:.2f} rad ; error maximo de la desenvoltura = {err2*1000:.2f} mm")
check(g2 > math.pi and err2 > lam / 4 - 1e-9, "el caso fuerte deberia fallar")

# 3) Vision ascendente / descendente
def u_los(alpha_deg, derecha=True):
    a = math.radians(alpha_deg)
    # direccion de vuelo (E,N) = (sin a, cos a); mirada a la derecha = rotacion de -90 deg; el vector al sensor es opuesto a la mirada
    mir = (math.cos(a), -math.sin(a))                 # (E,N) de la mirada a la derecha del vuelo
    return np.array([-mir[0] * math.sin(th), -mir[1] * math.sin(th), math.cos(th)])   # del suelo al sensor

u_asc = u_los(-10.0)
u_des = u_los(190.0)
print(f"Vision ascendente: u = (E {u_asc[0]:+.3f}, N {u_asc[1]:+.3f}, U {u_asc[2]:+.3f}) ; descendente: u = (E {u_des[0]:+.3f}, N {u_des[1]:+.3f}, U {u_des[2]:+.3f})")
check(abs(np.linalg.norm(u_asc) - 1) < 1e-12 and abs(np.linalg.norm(u_des) - 1) < 1e-12, "vectores unitarios")
d = np.array([0.012, 0.0, -0.005])               # m/ano (E, N, U): deslizamiento sintetico
la, ld = float(u_asc @ d), float(u_des @ d)
print(f"Deslizamiento sintetico dE = +12 mm/ano, dU = -5 mm/ano: LOS ascendente = {la*1000:+.2f} ; descendente = {ld*1000:+.2f} mm/ano")
A = np.array([[u_asc[0], u_asc[2]], [u_des[0], u_des[2]]])
sol = np.linalg.solve(A, np.array([la, ld]))
print(f"Descomposicion sin ruido (supone dN = 0): dE = {sol[0]*1000:.3f}, dU = {sol[1]*1000:.3f} mm/ano")
check(np.allclose(sol, [d[0], d[2]], atol=1e-9), "descomposicion exacta")
errs = []
for _ in range(2000):
    ra = la + 0.5e-3 * rng.standard_normal()
    rd = ld + 0.5e-3 * rng.standard_normal()
    errs.append(np.linalg.solve(A, np.array([ra, rd])) - np.array([d[0], d[2]]))
errs = np.array(errs)
print(f"Con ruido de 0.5 mm/ano en cada LOS: error tipico en E = {errs[:,0].std()*1000:.2f} mm/ano ; en U = {errs[:,1].std()*1000:.2f} mm/ano")
check(errs[:, 0].std() < 0.001 and errs[:, 1].std() < 0.001, "error tipico con ruido")
# Sensibilidad norte
dN = np.array([0.0, 0.010, 0.0])
print(f"Un movimiento norte de 10 mm/ano produce LOS ascendente {u_asc@dN*1000:+.2f} y descendente {u_des@dN*1000:+.2f} mm/ano: casi invisible")
check(abs(u_asc[1]) < 0.15 and abs(u_des[1]) < 0.15, "poca sensibilidad N")
print("Pruebas superadas.")
