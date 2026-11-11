#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C12: retorno cientifico con rendimientos decrecientes y frontera de Pareto costo-ciencia, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni una evaluacion de misiones reales. Opciones, costos y capacidades son SINTETICOS.
Modelo: cada opcion de mision tiene un costo C (Mum) y capacidades y_k para 3 objetivos; el valor por objetivo es v_k = 1 - exp(-y_k / tau_k)
(rendimientos decrecientes) y el valor cientifico V = sum w_k v_k con w = (0.5, 0.3, 0.2) y tau = (4, 6, 3) (unidades de capacidad).
Frontera de Pareto: opciones no dominadas (ninguna otra tiene V mayor o igual y C menor o igual con una desigualdad estricta).
Se calcula por comparacion exhaustiva O(n^2) y por barrido ordenado por costo; deben coincidir. Efectividad = V / C; pendiente marginal = delta V / delta C, medida de la opcion mas barata de la frontera a la intermedia
y de la intermedia a la mas cara. Robustez: 5000 vectores de pesos Dirichlet (concentracion 20 alrededor de w, semilla 124)
y frecuencia de pertenencia a la frontera de cada opcion.
Tolerancias: ambas fronteras identicas; V en [0, 1].
"""
import math, platform, random

W = [0.5, 0.3, 0.2]
TAU = [4.0, 6.0, 3.0]


def opciones():
    rng = random.Random(124)
    out = []
    for i in range(12):
        c = round(rng.uniform(50, 400), 1)
        k = c / 100.0
        y = [round(max(0.2, rng.gauss(2.2 * k, 0.9)), 2) for _ in range(3)]
        out.append((f"M{i + 1:02d}", c, y))
    return out


def valor(y, w=W):
    return sum(wk * (1 - math.exp(-yk / t)) for wk, yk, t in zip(w, y, TAU))


def frontera_exhaustiva(pts):
    n = len(pts)
    res = []
    for i in range(n):
        ci, vi = pts[i]
        dom = any((pts[j][0] <= ci and pts[j][1] >= vi) and (pts[j][0] < ci or pts[j][1] > vi) for j in range(n) if j != i)
        if not dom:
            res.append(i)
    return sorted(res)


def frontera_barrido(pts):
    orden = sorted(range(len(pts)), key=lambda i: (pts[i][0], -pts[i][1]))
    mejor, res = -1.0, []
    for i in orden:
        if pts[i][1] > mejor + 1e-15:
            res.append(i)
            mejor = pts[i][1]
    return sorted(res)


def run():
    ops = opciones()
    pts = [(c, valor(y)) for _, c, y in ops]
    fe, fb = frontera_exhaustiva(pts), frontera_barrido(pts)
    rng = random.Random(124)
    cuenta = [0] * len(ops)
    n = 5000
    for _ in range(n):
        g = [rng.gammavariate(20 * w, 1.0) for w in W]
        s = sum(g)
        w = [x / s for x in g]
        p = [(c, valor(y, w)) for _, c, y in ops]
        for i in frontera_exhaustiva(p):
            cuenta[i] += 1
    ef = [pts[i][1] / pts[i][0] for i in range(len(ops))]
    mejor_ef = max(range(len(ops)), key=lambda i: ef[i])
    fr = sorted(fe, key=lambda i: pts[i][0])
    mid = len(fr) // 2
    pend = [(pts[fr[mid]][1] - pts[fr[0]][1]) / (pts[fr[mid]][0] - pts[fr[0]][0]),
            (pts[fr[-1]][1] - pts[fr[mid]][1]) / (pts[fr[-1]][0] - pts[fr[mid]][0])]
    R = {"n_front": len(fe), "iguales": 1 if fe == fb else 0, "mejor_ef_id": mejor_ef, "mejor_ef": ef[mejor_ef] * 100, "vmax": max(p[1] for p in pts),
         "vmin": min(p[1] for p in pts), "pend_primera": pend[0] if pend else 0.0, "pend_ultima": pend[-1] if pend else 0.0, "cuenta": cuenta, "fr": fr, "pts": pts,
         "ops": ops, "ef": ef, "fe": fe, "robusta": sum(1 for i in fe if cuenta[i] / n > 0.9), "n_sim": n, "f_mejor": cuenta[mejor_ef] / n, "mejor_ef_nom": ops[mejor_ef][0]}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("12 opciones de mision SINTETICAS; V = sum w_k (1 - exp(-y_k/tau_k)), w = (0.5, 0.3, 0.2), tau = (4, 6, 3)")
    print(" opcion  costo[Mum]  y1     y2     y3     V      V/C x100  en frontera  freq (pesos Dirichlet)")
    for i, (nom, c, y) in enumerate(R["ops"]):
        print(f" {nom}   {c:8.1f}  {y[0]:5.2f}  {y[1]:5.2f}  {y[2]:5.2f}  {R['pts'][i][1]:.4f}  {100 * R['ef'][i]:7.3f}   {'si' if i in R['fe'] else 'no':>5}      {R['cuenta'][i] / R['n_sim']:.3f}")
    print(f"Frontera de Pareto: {[R['ops'][i][0] for i in R['fr']]} ; exhaustiva = barrido: {bool(R['iguales'])}")
    print(f"Mayor efectividad V/C: {R['ops'][R['mejor_ef_id']][0]} ({R['mejor_ef']:.3f} por 100 Mum) ; pendiente marginal (barata->intermedia / intermedia->cara) = {R['pend_primera']:.5f} / {R['pend_ultima']:.5f} V por Mum")
    print(f"Opciones de la frontera presentes en mas del 90 % de las simulaciones de pesos: {R['robusta']} de {R['n_front']}")
    assert R["iguales"] == 1 and 0 <= R["vmin"] and R["vmax"] <= 1
    assert R["pend_primera"] > R["pend_ultima"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
