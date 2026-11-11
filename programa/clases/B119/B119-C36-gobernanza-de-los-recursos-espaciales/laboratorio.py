#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C36: gobernanza de los recursos espaciales: reparto de beneficios con tres reglas (igual, proporcional, valor de Shapley) en una empresa conjunta SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no valora ningun proyecto ni propone un reparto real.
Texto consultado (2026-11-11): Acuerdo sobre la Luna (UNOOSA), art. 11: reparto equitativo de los beneficios de la explotacion de recursos, con especial consideracion a los paises en desarrollo y a los Estados que
hayan contribuido a la exploracion; art. II del tratado de 1967 (nota legal.un.org): sin apropiacion nacional. NO consultados: los Acuerdos Artemis, las leyes nacionales ni ningun regimen internacional vigente.
Modelo (teoria de juegos cooperativos, no consultada en una fuente concreta; verificada por dos metodos de calculo y la propiedad de eficiencia): tres actores sinteticos A (tecnologia), B (capital) y C (acceso al sitio)
con funcion caracteristica v(S) en unidades de valor sinteticas: v(A)=10, v(B)=0, v(C)=20, v(AB)=40, v(AC)=50, v(BC)=30, v(ABC)=100. Reglas: (1) igual: v(ABC)/3; (2) proporcional al valor individual v({i}) (con un piso comun si hay ceros: se reparte proporcional a v({i}) + 5);
(3) Shapley: promedio de contribuciones marginales sobre las 6 ordenaciones. Verificaciones: eficiencia (suma = v(ABC)); Shapley por permutaciones == por formula de subconjuntos; el nucleo no vacio se comprueba con las restricciones de coalicion.
"""
import itertools, json, math, platform

A = ("A", "B", "C")
V = {(): 0.0, ("A",): 10.0, ("B",): 0.0, ("C",): 20.0, ("A", "B"): 40.0, ("A", "C"): 50.0, ("B", "C"): 30.0, ("A", "B", "C"): 100.0}
def v(S): return V[tuple(sorted(S))]
def shapley_perm():
    phi = dict.fromkeys(A, 0.0)
    for perm in itertools.permutations(A):
        antes = []
        for i in perm:
            phi[i] += v(antes + [i]) - v(antes)
            antes.append(i)
    return {i: x / math.factorial(len(A)) for i, x in phi.items()}
def shapley_formula():
    n = len(A); phi = {}
    for i in A:
        otros = [j for j in A if j != i]
        tot = 0.0
        for k in range(len(otros) + 1):
            for S in itertools.combinations(otros, k):
                w = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                tot += w * (v(list(S) + [i]) - v(list(S)))
        phi[i] = tot
    return phi
sp, sf = shapley_perm(), shapley_formula()
assert all(abs(sp[i] - sf[i]) < 1e-12 for i in A)
T = v(A)
assert abs(sum(sp.values()) - T) < 1e-12
igual = {i: T / 3 for i in A}
prop = {i: T * (v([i]) + 5) / sum(v([j]) + 5 for j in A) for i in A}
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Empresa conjunta SINTETICA de 3 actores; art. 11 de la Luna y art. II consultados 2026-11-11; Acuerdos Artemis y leyes nacionales NO consultados.")
print("   actor   igual  proporcional  Shapley   v(individual)")
for i in A:
    print(f"   {i:5s} {igual[i]:7.2f} {prop[i]:11.2f} {sp[i]:9.2f} {v([i]):10.1f}")
# nucleo: ninguna coalicion recibe menos de lo que puede obtener sola
def en_nucleo(x):
    return all(sum(x[i] for i in S) >= v(S) - 1e-9 for r in (1, 2) for S in itertools.combinations(A, r))
print("Pertenece al nucleo (ninguna coalicion mejora por separado): igual", en_nucleo(igual), "; proporcional", en_nucleo(prop), "; Shapley", en_nucleo(sp))
assert en_nucleo(sp)
dif_max = max(abs(sp[i] - igual[i]) for i in A)
print(f"Diferencia maxima entre Shapley y reparto igual: {dif_max:.2f} u.v.")
print("CLAVES " + json.dumps({"sA": "%.2f" % sp["A"], "sB": "%.2f" % sp["B"], "sC": "%.2f" % sp["C"], "pA": "%.2f" % prop["A"], "pB": "%.2f" % prop["B"], "pC": "%.2f" % prop["C"], "ig": "%.2f" % igual["A"], "dm": "%.2f" % dif_max, "ni": str(en_nucleo(igual)), "np": str(en_nucleo(prop)), "ns": str(en_nucleo(sp))}))
print("Pruebas superadas.")
