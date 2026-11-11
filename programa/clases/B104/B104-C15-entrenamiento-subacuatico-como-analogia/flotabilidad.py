#!/usr/bin/env python3
"""B104-C15: flotabilidad neutra como analogia: ajuste de lastre, masa anadida y arrastre frente al vacio.
Cuerpo y coeficientes SINTETICOS/ILUSTRATIVOS; dimensiones del tanque de NASA consultadas (2026-11-10)."""
import sys
import numpy as np

G = 9.80665
RHO_AGUA = 995.8        # kg/m3 a ~29,4 C (valor tipico; no consultado)
print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: cuerpo de 150 kg y 0,152 m3; coeficientes inventados; tanque de NASA: 61,5 x 31,1 x 12,2 m (consultado)")

# (a) Verificacion de las dimensiones consultadas del tanque
L, W, H = 61.5, 31.1, 12.2
vol = L * W * H
gal = 6.2e6 * 3.785411784e-3
print(f"\nVolumen por dimensiones: {vol:,.0f} m3; 6,2 millones de galones: {gal:,.0f} m3; diferencia {100*(gal-vol)/vol:.2f} %")
assert abs(gal - vol) / vol < 0.01
p_fondo = 101_325 + RHO_AGUA * G * H
print(f"Presion absoluta en el fondo ({H} m): {p_fondo/1000:.1f} kPa = {p_fondo/101325:.2f} atm")

# (b) Ajuste de lastre para flotabilidad neutra
m, V = 150.0, 0.152
m_desplazada = RHO_AGUA * V
lastre = m_desplazada - m
print(f"\nMasa desplazada {m_desplazada:.2f} kg; masa del cuerpo {m:.1f} kg; lastre necesario {lastre:+.2f} kg (+ = anadir, - = quitar)")
residual = (m + lastre) * G - m_desplazada * G
assert abs(residual) < 1e-9

# (c) Empuje de 50 N durante 1 s: vacio frente a agua (masa anadida 0,5 rho V; arrastre cuadratico)
F, T_PUSH, CDA = 50.0, 1.0, 1.0 * 0.6
ma = 0.5 * RHO_AGUA * V
print(f"Masa anadida (esfera, 0,5 rho V) = {ma:.1f} kg; masa efectiva en agua = {m + ma:.1f} kg")


def mover(en_agua, t_fin=8.0, dt=1e-3):
    x = v = 0.0
    me = m + (ma if en_agua else 0.0)
    for i in range(int(t_fin / dt)):
        t = i * dt
        f = F if t < T_PUSH else 0.0
        d = 0.5 * RHO_AGUA * CDA * v * abs(v) if en_agua else 0.0
        v += dt * (f - d) / me
        x += dt * v
    return x, v


x_v, v_v = mover(False)
x_a, v_a = mover(True)
print(f"\nTras 8 s (empuje de {F:.0f} N durante 1 s): vacio -> x = {x_v:.2f} m, v = {v_v:.3f} m/s; agua -> x = {x_a:.2f} m, v = {v_a:.3f} m/s")
v_vac_teo = F * T_PUSH / m
print(f"Velocidad en vacio teorica F t/m = {v_vac_teo:.4f} m/s")
a0 = F / (m + ma)
print(f"Aceleracion inicial en agua = {a0:.3f} m/s2 frente a {F/m:.3f} m/s2 en vacio (cociente {a0/(F/m):.2f})")
assert abs(v_v - v_vac_teo) < 1e-6
assert abs(x_v - (0.5 * (F / m) * 1.0**2 + v_vac_teo * 7.0)) < 0.01
assert x_a < 0.5 * x_v and v_a < 0.25 * v_v
print("Pruebas superadas.")
