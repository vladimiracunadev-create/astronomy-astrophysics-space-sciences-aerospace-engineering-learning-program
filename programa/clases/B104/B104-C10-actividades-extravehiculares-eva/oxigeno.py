#!/usr/bin/env python3
"""B104-C10: presupuesto de oxigeno de una actividad extravehicular a partir de un perfil metabolico.
Perfil SINTETICO (semilla 104); capacidad y tasas ILUSTRATIVAS. No es una planificacion de EVA."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): perfil metabolico por tarea; capacidad de O2 ilustrativa (no es la de ningun traje)")
E_POR_LITRO = 20.1e3      # J por litro de O2 consumido (valor tipico de calorimetria indirecta; no consultado)
G_POR_LITRO = 1.429       # g por litro de O2 a 0 C y 101,325 kPa
CAP_KG = 0.90             # capacidad utilizable ilustrativa

tareas = [("preparacion y salida", 0.5, 250), ("traslado por pasamanos", 1.0, 320), ("instalacion de equipo", 2.5, 360),
          ("trabajo con herramienta", 1.5, 400), ("regreso y cierre", 0.5, 280)]
print("\ntarea | horas | tasa metabolica media [W] | O2 [kg]")
total_h, total_kg = 0.0, 0.0
for n, h, w in tareas:
    kg = w * h * 3600 / E_POR_LITRO * G_POR_LITRO / 1000
    total_h += h; total_kg += kg
    print(f"{n:28s} {h:5.1f} {w:20d} {kg:9.3f}")
print(f"Total: {total_h:.1f} h; O2 = {total_kg:.3f} kg; fraccion de la capacidad ilustrativa de {CAP_KG} kg = {total_kg/CAP_KG:.2f}")
w_medio = sum(w * h for _, h, w in tareas) / total_h
print(f"Tasa metabolica media ponderada: {w_medio:.0f} W")

# Monte Carlo: la tasa de cada tarea varia (log-normal 15 %)
rng = np.random.default_rng(104)
N = 100_000
kg = np.zeros(N)
for _, h, w in tareas:
    kg += w * np.exp(0.15 * rng.standard_normal(N) - 0.15**2 / 2) * h * 3600 / E_POR_LITRO * G_POR_LITRO / 1000
p_exc = (kg > CAP_KG).mean()
p95 = np.percentile(kg, 95)
print(f"\nMonte Carlo ({N} corridas, variacion 15 % por tarea): media {kg.mean():.3f} kg; percentil 95 {p95:.3f} kg; P(superar {CAP_KG} kg) = {p_exc:.4f}")
margen_95 = CAP_KG - p95
print(f"Margen frente al percentil 95: {margen_95:.3f} kg = {margen_95/ (w_medio*3600/E_POR_LITRO*G_POR_LITRO/1000):.2f} h a la tasa media")

# Duraciones consultadas en la pagina de NASA (para contexto)
print("\nContexto consultado (NASA, 2026-11-10): mas larga 8 h 56 min; mas corta 19 min; tipicas ~5 a 7 h; 286 caminatas en el grafico")
print(f"Duracion planificada aqui: {total_h:.1f} h (dentro del rango tipico consultado)")

assert abs(total_kg - sum(w * h * 3600 for _, h, w in tareas) / 20.1e3 * 1.429 / 1000) < 1e-12
assert abs(kg.mean() - total_kg) / total_kg < 0.01
assert 5 <= total_h <= 7
print("Pruebas superadas.")
