#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C20: rubrica ponderada con condiciones criticas no compensables y concordancia entre revisores, con un portafolio SINTETICO.

CONTENIDO EDUCATIVO: no es una evaluacion de personas reales ni asesoria laboral. Los 5 portafolios y los puntajes son SINTETICOS.
Rubrica: 6 criterios con pesos (0.15, 0.20, 0.20, 0.20, 0.15, 0.10) y niveles 1 (inicial) a 4 (destacado). Puntaje = 100 (sum w (nivel - 1)) / 3.
Categoria por puntaje (si no falla ninguna condicion critica): >= 85 destacado, >= 65 logrado, >= 40 en desarrollo, resto inicial (umbrales ILUSTRATIVOS).
Tres condiciones criticas (rotular lo sintetico; no presentar como asesoria; citar solo lo consultado): si falla alguna, la categoria es 'no logrado' sin importar el puntaje.
Concordancia: dos revisores califican 60 criterios (nivel 1-4) con ruido sobre un nivel verdadero (semilla 124); kappa de Cohen por la formula (po - pe)/(1 - pe) con matriz de
confusion y por una segunda implementacion con Counter; kappa ponderado lineal. Cobertura: 7 resultados de aprendizaje del bloque frente a 8 piezas del portafolio.
Tolerancias: ambas implementaciones de kappa iguales dentro de 1e-12; puntaje entre 0 y 100.
"""
import platform, random
from collections import Counter

PESOS = [0.15, 0.20, 0.20, 0.20, 0.15, 0.10]
CRIT = ["conceptos", "calculo", "numerico", "fuentes", "limites", "comunicacion"]
PORTAFOLIOS = {  # niveles por criterio, condiciones criticas (rotula, no asesoria, solo lo consultado)
    "P1": ([4, 4, 3, 4, 3, 3], (True, True, True)),
    "P2": ([4, 4, 4, 4, 4, 4], (True, False, True)),
    "P3": ([3, 3, 3, 2, 3, 3], (True, True, True)),
    "P4": ([2, 2, 2, 2, 2, 3], (True, True, True)),
    "P5": ([1, 2, 1, 1, 2, 2], (True, True, True)),
}
RESULTADOS = {  # resultado de aprendizaje del bloque: piezas que lo evidencian
    "RA1 cadena de valor y mercados": ["C01", "C03"], "RA2 costos y transporte": ["C05", "C23", "C24"], "RA3 financiamiento y contratos": ["C06", "C07", "C10"],
    "RA4 riesgo y servicio": ["C08", "C21"], "RA5 ciencia, etica y datos": ["C12", "C13", "C14"], "RA6 gestion de proyecto": ["C15", "C16", "C19"], "RA7 rotular lo sintetico": [],
}
PIEZAS = ["C01", "C03", "C05", "C23", "C24", "C06", "C07", "C10"]


def puntaje(niveles):
    return 100 * sum(w * (n - 1) for w, n in zip(PESOS, niveles)) / 3


def categoria(niveles, crit):
    if not all(crit):
        return "no logrado"
    p = puntaje(niveles)
    return "destacado" if p >= 85 else "logrado" if p >= 65 else "en desarrollo" if p >= 40 else "inicial"


def kappa_matriz(a, b, k=4):
    n = len(a)
    m = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        m[x - 1][y - 1] += 1
    po = sum(m[i][i] for i in range(k)) / n
    pe = sum(sum(m[i]) * sum(m[j][i] for j in range(k)) for i in range(k)) / n ** 2
    return (po - pe) / (1 - pe), m


def kappa_counter(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[l] * cb[l] for l in set(ca) | set(cb)) / n ** 2
    return (po - pe) / (1 - pe)


def kappa_lineal(a, b, k=4):
    n = len(a)
    m = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        m[x - 1][y - 1] += 1
    fa = [sum(m[i]) / n for i in range(k)]
    fb = [sum(m[j][i] for j in range(k)) / n for i in range(k)]
    num = sum(abs(i - j) * m[i][j] / n for i in range(k) for j in range(k))
    den = sum(abs(i - j) * fa[i] * fb[j] for i in range(k) for j in range(k))
    return 1 - num / den


def run():
    cats = {p: categoria(n, c) for p, (n, c) in PORTAFOLIOS.items()}
    pts = {p: puntaje(n) for p, (n, c) in PORTAFOLIOS.items()}
    rng = random.Random(124)
    verdad = [rng.choice([1, 2, 2, 3, 3, 3, 4, 4]) for _ in range(60)]
    def califica():
        return [min(4, max(1, v + rng.choice([-1, 0, 0, 0, 0, 1]))) for v in verdad]
    r1, r2 = califica(), califica()
    k1, mat = kappa_matriz(r1, r2)
    k2 = kappa_counter(r1, r2)
    kl = kappa_lineal(r1, r2)
    acuerdo = sum(1 for x, y in zip(r1, r2) if x == y) / 60
    cubiertos = [ra for ra, ps in RESULTADOS.items() if any(p in PIEZAS for p in ps)]
    R = {"p1": pts["P1"], "p2": pts["P2"], "p3": pts["P3"], "p4": pts["P4"], "p5": pts["P5"], "c1": cats["P1"], "c2": cats["P2"], "c3": cats["P3"], "c4": cats["P4"], "c5": cats["P5"],
         "kappa": k1, "kappa2": k2, "dif_kappa": abs(k1 - k2), "kappa_lin": kl, "acuerdo": acuerdo, "cob_ra": len(cubiertos) / len(RESULTADOS), "n_ra": len(RESULTADOS), "n_cub": len(cubiertos),
         "sin_ra": ", ".join(ra[:3] for ra in RESULTADOS if ra not in cubiertos), "pmax": max(pts.values()), "pmin": min(pts.values()), "sin_crit_prom": pts["P2"] - pts["P1"]}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Rubrica SINTETICA (6 criterios, niveles 1-4); umbrales ILUSTRATIVOS 85 / 65 / 40")
    for p, (n, c) in PORTAFOLIOS.items():
        print(f"  {p}: niveles {n} ; criticas {tuple(int(x) for x in c)} ; puntaje = {puntaje(n):5.1f} ; categoria = {categoria(n, c)}")
    print(f"P2 tiene el mayor puntaje ({R['p2']:.1f}) pero falla una condicion critica: categoria {R['c2']} (no se compensa con promedio).")
    print(f"Concordancia de dos revisores (60 criterios): acuerdo = {100 * R['acuerdo']:.1f} % ; kappa (matriz) = {R['kappa']:.4f} ; kappa (Counter) = {R['kappa2']:.4f} ; diferencia = {R['dif_kappa']:.1e} ; kappa lineal = {R['kappa_lin']:.4f}")
    print(f"Cobertura de resultados del bloque por las piezas del portafolio: {R['n_cub']} de {R['n_ra']} ({100 * R['cob_ra']:.1f} %) ; sin evidencia: {R['sin_ra']}")
    assert R["dif_kappa"] < 1e-12 and 0 <= R["pmin"] and R["pmax"] <= 100
    assert R["c2"] == "no logrado" and R["p2"] == 100.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
