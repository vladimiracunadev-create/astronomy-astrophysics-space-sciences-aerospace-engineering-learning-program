#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C04: reparto del excedente de una alianza (valor de Shapley) y dependencia de socios (modelo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, comercial ni de inversion.
Datos consultados (2026-11-11): la pagina de los Acuerdos Artemis de la NASA describe principios compartidos (usos pacificos, transparencia,
interoperabilidad, asistencia en emergencias, registro de objetos, datos cientificos, deconflicto, desechos) y reporta 78 signatarios tras la
firma del 2026-10-28; son compromisos entre Estados, no contratos entre empresas. El Reglamento (UE) 2021/821 (doble uso) se consulto como
contexto del limite legal de las alianzas (clase C05). Ninguna cifra de alianzas reales entra al calculo.
ILUSTRATIVOS (sinteticos): tres socios A (fabricante de plataformas, pais 1), B (operador de lanzamiento, pais 2), C (proveedor de datos terrestres,
pais 3) con valores de coalicion v(S) en millones de u.m.: v(A)=10, v(B)=20, v(C)=0, v(AB)=60, v(AC)=30, v(BC)=40, v(ABC)=100.
Dependencia: cuotas de suministro de un componente critico entre proveedores de 3 paises.
Unidades: millones de u.m. Tolerancias: eficiencia sum(Shapley) = v(N) (1e-9); Shapley por permutaciones frente a formula por tamanos (1e-9).
"""
from __future__ import annotations
import itertools, math, platform

V = {frozenset(): 0.0, frozenset("A"): 10.0, frozenset("B"): 20.0, frozenset("C"): 0.0,
     frozenset("AB"): 60.0, frozenset("AC"): 30.0, frozenset("BC"): 40.0, frozenset("ABC"): 100.0}
JUG = ["A", "B", "C"]


def shapley_permutaciones(v, jug):
    res = {j: 0.0 for j in jug}
    perms = list(itertools.permutations(jug))
    for p in perms:
        acum = frozenset()
        for j in p:
            nuevo = acum | {j}
            res[j] += v[nuevo] - v[acum]
            acum = nuevo
    return {j: x / len(perms) for j, x in res.items()}


def shapley_formula(v, jug):
    n = len(jug)
    res = {}
    for j in jug:
        otros = [x for x in jug if x != j]
        s = 0.0
        for r in range(len(otros) + 1):
            for S in itertools.combinations(otros, r):
                S = frozenset(S)
                peso = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                s += peso * (v[S | {j}] - v[S])
        res[j] = s
    return res


def en_el_nucleo(x, v, jug):
    """Una asignacion esta en el nucleo si ninguna coalicion obtiene menos de lo que puede lograr sola."""
    for r in range(1, len(jug)):
        for S in itertools.combinations(jug, r):
            if sum(x[j] for j in S) < v[frozenset(S)] - 1e-9:
                return False, "".join(S)
    return abs(sum(x.values()) - v[frozenset(jug)]) < 1e-9, ""


def hhi(cuotas):
    return sum((100 * c) ** 2 for c in cuotas)


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Alianza SINTETICA de 3 socios; valores en millones de u.m.; sin cifras de alianzas reales.")
    a = shapley_permutaciones(V, JUG)
    b = shapley_formula(V, JUG)
    for j in JUG:
        assert abs(a[j] - b[j]) < 1e-9
    assert abs(sum(a.values()) - V[frozenset(JUG)]) < 1e-9
    print("socio  valor solo  Shapley (permutaciones)  Shapley (formula)  reparto proporcional a v(solo)")
    tot_solo = sum(V[frozenset(j)] for j in JUG)
    for j in JUG:
        prop = V[frozenset(JUG)] * V[frozenset(j)] / tot_solo
        print(f"{j:5s}  {V[frozenset(j)]:10.1f}  {a[j]:23.2f}  {b[j]:17.2f}  {prop:28.2f}")
    print(f"Suma de Shapley = {sum(a.values()):.2f} = v(ABC) = {V[frozenset(JUG)]:.1f}")
    ok, S = en_el_nucleo(a, V, JUG)
    print(f"Shapley en el nucleo (ninguna coalicion gana mas yendose): {ok} {('(rompe: ' + S + ')') if S else ''}")
    ok2, S2 = en_el_nucleo({"A": 10.0, "B": 50.0, "C": 40.0}, V, JUG)
    print(f"Reparto A=10, B=50, C=40 en el nucleo: {ok2} {('(rompe: ' + S2 + ')') if S2 else ''}")
    # Dependencia
    print("Dependencia de un componente critico (cuota por pais proveedor):")
    for nombre, c in (("un solo pais", [1.0]), ("2 paises 80/20", [0.8, 0.2]), ("3 paises 50/30/20", [0.5, 0.3, 0.2]), ("3 paises iguales", [1/3]*3)):
        print(f"  {nombre:18s} HHI = {hhi(c):7.1f}")
    assert abs(hhi([1.0]) - 10000.0) < 1e-9 and abs(hhi([0.25]*4) - 2500.0) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
