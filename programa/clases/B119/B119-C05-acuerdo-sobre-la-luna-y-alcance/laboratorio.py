#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C05: Acuerdo sobre la Luna: superficie lunar ocupada por instalaciones y reparto equitativo de beneficios (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, pagina de UNOOSA del Acuerdo sobre la Luna; WebFetch): art. 3 (usos pacificos; sin ADM, bases militares ni ensayos de armas),
art. 11 (la Luna y sus recursos son patrimonio comun de la humanidad; sin soberania ni propiedad por colocar equipo; regimen internacional futuro con reparto equitativo
y consideracion especial a paises en desarrollo y a quienes contribuyeron), art. 12 (jurisdiccion y control sobre el personal y el equipo). Resolucion 34/68 de la AG, 5-12-1979.
NO consultados: numero de partes y fecha de entrada en vigor (la pagina no los muestra).
Constante (no consultada en esta sesion; valor estandar): radio medio lunar R = 1737.4 km.
SINTETICO: 12 instalaciones con zona de seguridad de 5 km de radio; cinco Estados genericos con contribuciones 0.40, 0.25, 0.15, 0.12, 0.08.
Reparto: w_i = a/n + (1 - a) c_i, con a = peso del criterio de igualdad. Tolerancia: pesos suman 1 (1e-12); area de casquete == formula exacta (1e-9 relativo).
"""
import json, math, platform

R = 1737.4
AREA = 4 * math.pi * R ** 2
r_zona, n_inst = 5.0, 12
a_zona = math.pi * r_zona ** 2          # aproximacion plana (r << R)
exacta = 2 * math.pi * R ** 2 * (1 - math.cos(r_zona / R))
ocupada = n_inst * a_zona
frac = ocupada / AREA
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Datos SINTETICOS; articulos del Acuerdo parafraseados de la pagina de UNOOSA (consultada 2026-11-11); R lunar = 1737.4 km (valor estandar, no consultado).")
print(f"Superficie lunar = {AREA:.4e} km2")
print(f"Zona de seguridad de 5 km: plana {a_zona:.4f} km2 ; casquete exacto {exacta:.4f} km2 ; diferencia relativa {(a_zona - exacta) / exacta:.2e}")
assert abs(a_zona - exacta) / exacta < 1e-4
print(f"12 instalaciones (sin solape): {ocupada:.2f} km2 = fraccion {frac:.3e} de la superficie ({frac * 100:.5f} %)")

contrib = [0.40, 0.25, 0.15, 0.12, 0.08]
assert abs(sum(contrib) - 1) < 1e-12
print("Reparto de 100 unidades de beneficio sinteticas entre cinco Estados genericos, segun el peso a de la igualdad:")
res = {}
for a in (0.0, 0.5, 1.0):
    w = [a / 5 + (1 - a) * c for c in contrib]
    assert abs(sum(w) - 1) < 1e-12
    res[a] = w
    print(f"  a = {a:.1f}: " + "  ".join(f"{100 * x:5.1f}" for x in w))
mayor_menor = res[0.0][0] / res[0.0][4]
print(f"Razon mayor/menor con a = 0: {mayor_menor:.2f}; con a = 0.5: {res[0.5][0] / res[0.5][4]:.2f}; con a = 1: 1.00")
print("CLAVES " + json.dumps({"area": "%.4e" % AREA, "zona": "%.2f" % a_zona, "ocup": "%.1f" % ocupada, "frac": "%.2e" % frac, "w0": "%.1f" % (100 * res[0.0][4]), "w05": "%.1f" % (100 * res[0.5][4]), "razon0": "%.2f" % mayor_menor, "razon05": "%.2f" % (res[0.5][0] / res[0.5][4])}))
print("Pruebas superadas.")
