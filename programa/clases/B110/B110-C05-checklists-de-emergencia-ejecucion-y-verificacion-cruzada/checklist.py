#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B110-C05: probabilidad de un error sin detectar en un checklist con y sin verificacion cruzada.

CONSULTADO (2026-11-10): los procedimientos de emergencia se memorizan en sus acciones iniciales y la tripulacion los ejecuta tambien con procedimientos
impresos y comprobando posiciones fisicas de valvulas cuando fallan los sistemas (Tobias y McMillan, SpaceOps 2023, NASA JSC);
el estudio de Haynes et al. (NEJM 2009) sobre el checklist quirurgico, solo por la nota de prensa de Harvard (muertes hospitalarias 1,5 % -> 0,8 %;
complicaciones 11,0 % -> 7,0 %; estudio no aleatorizado): se cita como contexto y NO se usa en el calculo.
El informe de Degani y Wiener (NASA CR-177549) solo se vio como registro bibliografico; su texto NO se leyo.
ILUSTRATIVOS (sinteticos, no medidos): N = 20 pasos, 5 de ellos criticos, probabilidad de error de ejecucion por paso p = 0,01 (x3 bajo estres),
probabilidad de que el propio ejecutor lo note s = 0,3, probabilidad de detectar del verificador d = 0,9, correlacion de modo comun rho (0 a 0,8),
tiempos 6 s por paso (lectura-hacer), 12 s por paso con respuesta verificada, +6 s por paso critico verificado.
Modelo: errores independientes por paso; un error pasa sin detectar con probabilidad u = p (1 - s) (1 - d (1 - rho)); P(al menos uno) = 1 - (1 - u)^N.
Tolerancias: analitico frente a Monte Carlo (200000 corridas, semilla 110) dentro de 4 desviaciones estandar binomiales.
Contenido educativo: NO es un procedimiento ni un checklist real.
"""
from __future__ import annotations
import math, platform, random

N, N_CRIT = 20, 5
P_ERR, S_SELF, D_DET = 0.01, 0.3, 0.9
T_SOLO, T_CR, T_CRIT_EXTRA = 6.0, 12.0, 6.0


def u_paso(p, s, d, rho):
    return p * (1 - s) * (1 - d * (1 - rho))


def p_alguno(u, n):
    return 1 - (1 - u) ** n


def monte_carlo(rng, p, s, d, rho, n, corridas):
    uu = u_paso(p, s, d, rho)
    cuenta = 0
    for _ in range(corridas):
        hay = False
        for _ in range(n):
            if rng.random() < p:  # hay error de ejecucion
                if rng.random() < s:  # lo nota quien ejecuta
                    continue
                # verificador: detecta con prob d si no hay modo comun; con modo comun rho se pierde la deteccion
                if rng.random() < rho:
                    det = False
                else:
                    det = rng.random() < d
                if not det:
                    hay = True
                    break
        cuenta += hay
    return cuenta / corridas, uu


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Checklist ILUSTRATIVO: N = {N} pasos ({N_CRIT} criticos); p = {P_ERR}; s = {S_SELF}; d = {D_DET}")
    # verificacion analitico vs Monte Carlo
    rng = random.Random(110)
    corridas = 200000
    print("Verificacion Monte Carlo frente a la formula (rho = 0,5):")
    ok = True
    for nombre, d in (("solo ejecutor", 0.0), ("con verificador", D_DET)):
        pm, uu = monte_carlo(rng, P_ERR, S_SELF, d, 0.5, N, corridas)
        pa = p_alguno(uu, N)
        sd = math.sqrt(pa * (1 - pa) / corridas)
        z = abs(pm - pa) / sd
        ok = ok and z < 4
        print(f"  {nombre:16s} analitico = {pa:.5f}  MC = {pm:.5f}  desviaciones = {z:.2f}")
    assert ok
    print("Comparacion de modalidades (p = 0,01; rho = 0,5 salvo que se indique):")
    print(" modalidad                        u por paso   P(error sin detectar)   tiempo [s]")
    filas = []
    modos = [
        ("A  lectura-hacer sin verificar", 0.0, 0.5, N * T_SOLO, N),
        ("B  respuesta verificada, todos", D_DET, 0.5, N * T_CR, N),
        ("C  verificar solo los criticos", None, 0.5, N * T_SOLO + N_CRIT * T_CRIT_EXTRA, None),
    ]
    for nom, d, rho, tiempo, n in modos:
        if d is None:  # criticos verificados: 5 pasos con d, 15 sin
            uc = u_paso(P_ERR, S_SELF, D_DET, rho)
            un = u_paso(P_ERR, S_SELF, 0.0, rho)
            pa = 1 - (1 - uc) ** N_CRIT * (1 - un) ** (N - N_CRIT)
            pcrit = p_alguno(uc, N_CRIT)
            filas.append((nom, pa))
            print(f" {nom:32s} {uc:5.5f}/{un:5.5f} {pa:14.5f} {tiempo:16.0f}   (solo en criticos: {pcrit:.5f})")
        else:
            uu = u_paso(P_ERR, S_SELF, d, rho)
            pa = p_alguno(uu, n)
            filas.append((nom, pa))
            print(f" {nom:32s} {uu:10.5f} {pa:14.5f} {tiempo:16.0f}")
    assert filas[1][1] < filas[2][1] < filas[0][1]
    print("Sensibilidad a la correlacion de modo comun rho (modalidad B):")
    prev = 0.0
    for rho in (0.0, 0.2, 0.5, 0.8):
        pa = p_alguno(u_paso(P_ERR, S_SELF, D_DET, rho), N)
        print(f"  rho = {rho:3.1f}  P = {pa:.5f}")
        assert pa >= prev
        prev = pa
    print("Estres (p x 3 = 0,03), rho = 0,5:")
    for nom, d in (("A  sin verificar", 0.0), ("B  verificada", D_DET)):
        print(f"  {nom:18s} P = {p_alguno(u_paso(3 * P_ERR, S_SELF, d, 0.5), N):.5f}")
    # coste en tiempo por error evitado
    pa_a, pa_b = filas[0][1], filas[1][1]
    extra = N * (T_CR - T_SOLO)
    print(f"B frente a A: reduce P de {pa_a:.4f} a {pa_b:.4f} (factor {pa_a/pa_b:.2f}) con {extra:.0f} s extra; {extra/(pa_a-pa_b):.0f} s por cada unidad de probabilidad evitada")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
