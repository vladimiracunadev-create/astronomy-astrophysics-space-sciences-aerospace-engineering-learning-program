#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C14: reproducibilidad numerica, huella criptografica y lista FAIR puntuada, con un caso SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria legal ni de licencias. El conjunto de datos y su registro son SINTETICOS.
Consultado (2026-11-11): Wilkinson et al. (2016), Scientific Data 3:160018, principios FAIR (Findable, Accessible, Interoperable, Reusable),
y la Recomendacion de la UNESCO sobre Ciencia Abierta (2021). Las cuatro letras FAIR se usan solo como agrupacion de 12 criterios SINTETICOS de ejemplo.
Parte 1: suma de 100000 numeros pseudoaleatorios de magnitudes mezcladas (semilla 124) en cuatro ordenes: original, inverso, ordenado, y la referencia exacta con
fracciones (Fraction); math.fsum debe coincidir con la referencia exacta redondeada. Parte 2: huella SHA-256 del resultado serializado con formato fijo; con la
misma semilla debe repetirse; con otra, cambiar. Parte 3: lista de 12 criterios (3 por letra) sobre un registro sintetico; puntaje = criterios cumplidos / 12.
Unidades: adimensionales. Tolerancias: fsum = suma exacta redondeada (igualdad exacta); huellas iguales con la misma semilla.
"""
import hashlib, json, math, platform, random
from fractions import Fraction

N = 100000


def numeros(semilla):
    rng = random.Random(semilla)
    return [rng.gauss(0, 1) * 10 ** rng.randint(-6, 6) for _ in range(N)]


def suma_simple(xs):
    s = 0.0
    for x in xs:
        s += x
    return s


def huella(semilla):
    xs = numeros(semilla)
    res = {"semilla": semilla, "n": len(xs), "suma_fsum": repr(math.fsum(xs)), "min": repr(min(xs)), "max": repr(max(xs))}
    texto = json.dumps(res, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


REGISTRO = {  # registro sintetico de un conjunto de datos
    "F1 identificador persistente": True, "F2 metadatos descriptivos": True, "F3 indexado en un repositorio": False,
    "A1 recuperable por protocolo estandar": True, "A2 metadatos disponibles aunque el dato no": False, "A3 condiciones de acceso declaradas": True,
    "I1 formato abierto": True, "I2 vocabulario controlado": False, "I3 enlaces a otros conjuntos": False,
    "R1 licencia explicita": True, "R2 procedencia documentada": True, "R3 version y fecha": True,
}


def run():
    xs = numeros(124)
    exacta = float(sum((Fraction(x) for x in xs), Fraction(0)))
    s1 = suma_simple(xs)
    s2 = suma_simple(xs[::-1])
    s3 = suma_simple(sorted(xs))
    s4 = suma_simple(sorted(xs, key=abs))
    fs = math.fsum(xs)
    scale = max(abs(x) for x in xs)
    h1, h2, h3 = huella(124), huella(124), huella(125)
    por_letra = {l: sum(1 for k, v in REGISTRO.items() if k.startswith(l) and v) for l in "FAIR"}
    R = {"exacta": exacta, "orig": s1, "inv": s2, "orden": s3, "orden_abs": s4, "fsum": fs, "e_orig": abs(s1 - exacta), "e_inv": abs(s2 - exacta),
         "e_orden": abs(s3 - exacta), "e_abs": abs(s4 - exacta), "e_fsum": abs(fs - exacta), "escala": scale, "dist_ordenes": max(s1, s2, s3, s4) - min(s1, s2, s3, s4),
         "igual_huella": 1 if h1 == h2 else 0, "dif_huella": 1 if h1 != h3 else 0, "h1": h1, "h3": h3, "pts": sum(REGISTRO.values()), "total": len(REGISTRO),
         "F": por_letra["F"], "A": por_letra["A"], "I": por_letra["I"], "R": por_letra["R"], "score": sum(REGISTRO.values()) / len(REGISTRO), "h1_corta": h1[:16]}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Parte 1: suma de {N} numeros SINTETICOS (semilla 124, escala maxima {R['escala']:.3e})")
    print(f"  referencia exacta (Fraction) redondeada = {R['exacta']!r}")
    for nom, k, e in [("orden original", "orig", "e_orig"), ("orden inverso", "inv", "e_inv"), ("ordenados", "orden", "e_orden"), ("ordenados por |x|", "orden_abs", "e_abs"), ("math.fsum", "fsum", "e_fsum")]:
        print(f"  {nom:<18} suma = {R[k]!r:<24} error absoluto = {R[e]:.3e}")
    print(f"  dispersion entre ordenes = {R['dist_ordenes']:.3e}")
    print(f"Parte 2: huella SHA-256 semilla 124 = {R['h1'][:16]}... ; repetida igual: {bool(R['igual_huella'])} ; semilla 125 = {R['h3'][:16]}... distinta: {bool(R['dif_huella'])}")
    print(f"Parte 3: lista FAIR sintetica: {R['pts']}/{R['total']} criterios = {100 * R['score']:.1f} % (F {R['F']}/3, A {R['A']}/3, I {R['I']}/3, R {R['R']}/3)")
    for k, v in REGISTRO.items():
        print(f"   [{'x' if v else ' '}] {k}")
    assert R["e_fsum"] == 0.0
    assert R["igual_huella"] == 1 and R["dif_huella"] == 1
    assert R["dist_ordenes"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
