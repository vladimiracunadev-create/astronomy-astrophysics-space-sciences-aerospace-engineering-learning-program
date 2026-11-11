#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C03: registro de riesgos (activos, amenazas, controles) de una infraestructura espacial SINTETICA.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad; no describe tecnicas de ataque.
Datos SINTETICOS (inventados). Marco conceptual (solo fichas y resumenes consultados el 2026-11-11): NIST SP 800-30 Rev. 1 (2012,
evaluacion de riesgos) y NIST IR 8401 (2022, segmento terrestre). Riesgo inherente = probabilidad (1-5) x impacto (1-5);
cada control reduce la probabilidad por un factor de eficacia (0-1, ilustrativo): P_res = P (1 - e1)(1 - e2)...
Unidades: puntajes adimensionales. Sistema de referencia: ninguno. Tolerancias: suma de riesgos recalculada por otra via = exacta;
Monte Carlo del riesgo esperado (100000 repeticiones, semilla 122) vs analitico < 1 %.
"""
from __future__ import annotations
import platform, random

# (id, activo, amenaza abstracta, probabilidad 1-5, impacto 1-5, [eficacias de controles])
REGISTRO = [
    ("R1", "Estacion terrena A", "perdida de energia", 3, 4, [0.5, 0.3]),
    ("R2", "Estacion terrena A", "acceso fisico no autorizado", 2, 5, [0.6]),
    ("R3", "Segmento de control", "credencial comprometida", 4, 5, [0.5, 0.4]),
    ("R4", "Enlace de comandos", "interferencia deliberada", 3, 5, [0.4]),
    ("R5", "Archivo de telemetria", "corrupcion de datos", 2, 3, [0.7]),
    ("R6", "Proveedor unico de software", "cese del proveedor", 2, 4, []),
]


def residual(p, efic):
    for e in efic:
        p = p * (1 - e)
    return p


def nivel(r):
    return "ALTO" if r >= 15 else "MEDIO" if r >= 8 else "BAJO"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: activos, amenazas (abstractas), puntajes y eficacias son inventados.")
    tot_inh = tot_res = 0.0
    print(" id  activo                        amenaza                        P  I  inherente  residual  nivel_res")
    for rid, act, am, p, i, ef in REGISTRO:
        inh = p * i
        pres = residual(p, ef)
        res = pres * i
        tot_inh += inh
        tot_res += res
        print(f" {rid:3s} {act:29s} {am:30s} {p}  {i}  {inh:8d}  {res:8.2f}  {nivel(res)}")
    print(f"Suma inherente = {tot_inh:.1f} ; suma residual = {tot_res:.2f} ; reduccion = {100 * (1 - tot_res / tot_inh):.1f} %")
    # segunda via: lista por comprension
    alt = sum(residual(p, ef) * i for _, _, _, p, i, ef in REGISTRO)
    assert abs(alt - tot_res) < 1e-9
    # Monte Carlo: cada riesgo ocurre con probabilidad residual/5 (escala ilustrativa), impacto I
    rng = random.Random(122)
    n = 100000
    esp = 0.0
    for _ in range(n):
        for _, _, _, p, i, ef in REGISTRO:
            if rng.random() < residual(p, ef) / 5:
                esp += i
    mc = esp / n
    an = sum(residual(p, ef) / 5 * i for _, _, _, p, i, ef in REGISTRO)
    print(f"Impacto esperado por periodo (escala ilustrativa): analitico = {an:.4f} ; Monte Carlo = {mc:.4f} ; dif = {abs(an - mc) / an * 100:.2f} %")
    assert abs(an - mc) / an < 0.01
    mayor = max(REGISTRO, key=lambda r: residual(r[3], r[5]) * r[4])
    print(f"Mayor riesgo residual: {mayor[0]} ({mayor[1]} / {mayor[2]})")
    sin = [r[0] for r in REGISTRO if not r[5]]
    print(f"Riesgos sin ningun control: {sin}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
