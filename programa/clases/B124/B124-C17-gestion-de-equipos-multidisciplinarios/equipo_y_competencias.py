#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C17: tamano de un equipo (canales de comunicacion) y cobertura de competencias, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria de recursos humanos ni de gestion. Las personas, competencias y la tasa de sobrecarga son SINTETICAS.
Modelo 1: canales de comunicacion de un equipo de n personas = n (n - 1) / 2. Si cada persona pierde una fraccion c de su tiempo por cada otra persona
con la que coordina, la capacidad efectiva es E(n) = n (1 - c (n - 1)) para n <= 1 + 1/c. El maximo continuo esta en n* = (1 + 1/c) / 2 (c = 0.04, sintetica).
Modelo 2: 8 candidatos con subconjuntos de 6 competencias; se busca el equipo minimo que las cubra todas, por busqueda exhaustiva (2^8 subconjuntos) y por
algoritmo voraz (siempre la persona que cubre mas competencias nuevas).
Tolerancias: canales por formula = por conteo de pares; maximo por barrido = entero mas cercano a n*; el voraz cubre todo y no usa menos personas que el exhaustivo.
"""
import itertools, platform

C = 0.04
COMP = ["dinamica orbital", "termica", "software", "operaciones", "adquisiciones", "ciencia"]
PERSONAS = {
    "P1": {"dinamica orbital", "termica"},
    "P2": {"software", "operaciones"},
    "P3": {"adquisiciones"},
    "P4": {"ciencia", "software"},
    "P5": {"termica", "operaciones", "adquisiciones"},
    "P6": {"dinamica orbital", "ciencia"},
    "P7": {"software"},
    "P8": {"operaciones", "ciencia", "termica"},
}


def canales(n):
    return n * (n - 1) // 2


def canales_pares(n):
    return sum(1 for _ in itertools.combinations(range(n), 2))


def efectiva(n, c=C):
    return max(0.0, n * (1 - c * (n - 1)))


def exhaustivo():
    nombres = sorted(PERSONAS)
    todas = set(COMP)
    mejor = None
    n_cubren = 0
    for r in range(1, len(nombres) + 1):
        for sub in itertools.combinations(nombres, r):
            cub = set().union(*(PERSONAS[p] for p in sub))
            if cub == todas:
                n_cubren += 1
                if mejor is None:
                    mejor = sub
        if mejor is not None:
            return mejor, n_cubren_total(len(nombres), todas)
    return None, 0


def n_cubren_total(n, todas):
    nombres = sorted(PERSONAS)
    tot = 0
    for r in range(1, n + 1):
        for sub in itertools.combinations(nombres, r):
            if set().union(*(PERSONAS[p] for p in sub)) == todas:
                tot += 1
    return tot


def voraz():
    cub, elegidos = set(), []
    while cub != set(COMP):
        p = max(sorted(PERSONAS), key=lambda x: len(PERSONAS[x] - cub))
        if not PERSONAS[p] - cub:
            break
        elegidos.append(p)
        cub |= PERSONAS[p]
    return tuple(sorted(elegidos)), cub == set(COMP)


def run():
    n_star = (1 + 1 / C) / 2
    barrido = max(range(1, 40), key=lambda n: efectiva(n))
    mejor, n_cub = exhaustivo()
    vor, ok = voraz()
    R = {"canales_5": canales(5), "canales_10": canales(10), "canales_15": canales(15), "chk_canales": max(abs(canales(n) - canales_pares(n)) for n in range(1, 30)),
         "n_star": n_star, "n_barrido": barrido, "e_max": efectiva(barrido), "e_5": efectiva(5), "e_10": efectiva(10), "e_20": efectiva(20), "e_26": efectiva(26),
         "por_persona_max": efectiva(barrido) / barrido, "por_persona_5": efectiva(5) / 5, "n_min": len(mejor), "n_voraz": len(vor), "voraz_ok": 1 if ok else 0,
         "n_equipos_cubren": n_cub, "equipo_min": ",".join(mejor), "equipo_voraz": ",".join(vor), "eficiencia_10": efectiva(10) / 10}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Modelo 1: sobrecarga c = {C} por cada otra persona (SINTETICA)")
    print(f"  canales n(n-1)/2: n=5 -> {R['canales_5']} ; n=10 -> {R['canales_10']} ; n=15 -> {R['canales_15']} ; formula = conteo de pares (diferencia {R['chk_canales']})")
    print(f"  capacidad efectiva E(n): n=5 {R['e_5']:.2f} ; n=10 {R['e_10']:.2f} ; n=20 {R['e_20']:.2f} ; n=26 {R['e_26']:.2f}")
    print(f"  maximo analitico n* = {R['n_star']:.1f} ; maximo por barrido n = {R['n_barrido']} con E = {R['e_max']:.2f} ({R['por_persona_max']:.3f} por persona; con 5 personas {R['por_persona_5']:.3f})")
    print("Modelo 2: cobertura de 6 competencias con 8 candidatos")
    print(f"  equipos que cubren todo: {R['n_equipos_cubren']} de 255 ; tamano minimo = {R['n_min']} ({R['equipo_min']})")
    print(f"  voraz: {R['equipo_voraz']} ({R['n_voraz']} personas) ; cubre todo: {bool(R['voraz_ok'])}")
    assert R["chk_canales"] == 0 and R["n_barrido"] == round(R["n_star"])
    assert R["voraz_ok"] == 1 and R["n_voraz"] >= R["n_min"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
