#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C16: ruta critica (CPM), holguras y probabilidad de cumplir el plazo con duraciones inciertas, SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria de gestion de proyectos. Actividades, duraciones y dependencias son SINTETICAS.
Consultado (2026-11-11), NASA Systems Engineering Handbook (SP-6105 Rev 2): la ruta critica es la secuencia de tareas dependientes que determina la duracion
mas larga del proyecto; las tareas con holgura (float) tienen tiempo de sobra; la ruta critica cambia a medida que avanza el proyecto.
Modelo CPM: paso hacia adelante (ES, EF), hacia atras (LS, LF), holgura = LS - ES; critica si holgura = 0.
Verificacion: la duracion del proyecto es igual al camino mas largo, obtenido por enumeracion de todos los caminos (DFS).
Incertidumbre: duracion triangular (minimo 0.8 d, moda d, maximo 1.6 d); 20000 simulaciones (semilla 124). Efecto de convergencia de caminos:
E[max de caminos] >= max de E[caminos] (desigualdad de Jensen).
Unidades: semanas. Tolerancias: CPM = camino mas largo (igualdad exacta); media simulada >= duracion con medias.
"""
import platform, random

ACT = {  # nombre: (duracion, predecesoras)
    "A requisitos": (4, []),
    "B diseno preliminar": (6, ["A requisitos"]),
    "C plan de adquisiciones": (5, ["A requisitos"]),
    "D diseno detallado": (8, ["B diseno preliminar", "C plan de adquisiciones"]),
    "E contratar instrumento": (7, ["C plan de adquisiciones"]),
    "F integracion": (5, ["D diseno detallado", "E contratar instrumento"]),
    "G pruebas ambientales": (3, ["F integracion"]),
    "H software de tierra": (4, ["F integracion"]),
    "I revision de preparacion": (2, ["G pruebas ambientales", "H software de tierra"]),
    "J lanzamiento": (2, ["I revision de preparacion"]),
}


def orden_topologico(act):
    vis, res = set(), []

    def visita(n):
        if n in vis:
            return
        vis.add(n)
        for p in act[n][1]:
            visita(p)
        res.append(n)
    for n in act:
        visita(n)
    return res


def cpm(dur):
    orden = orden_topologico(ACT)
    es, ef = {}, {}
    for n in orden:
        es[n] = max([ef[p] for p in ACT[n][1]], default=0)
        ef[n] = es[n] + dur[n]
    fin = max(ef.values())
    suc = {n: [m for m in ACT if n in ACT[m][1]] for n in ACT}
    lf, ls = {}, {}
    for n in reversed(orden):
        lf[n] = min([ls[s] for s in suc[n]], default=fin)
        ls[n] = lf[n] - dur[n]
    holg = {n: ls[n] - es[n] for n in ACT}
    return es, ef, ls, lf, holg, fin


def camino_mas_largo(dur):
    suc = {n: [m for m in ACT if n in ACT[m][1]] for n in ACT}
    inicios = [n for n in ACT if not ACT[n][1]]
    mejor = (0, None)

    def dfs(n, acum, ruta):
        nonlocal mejor
        acum += dur[n]
        ruta = ruta + [n]
        if not suc[n]:
            if acum > mejor[0]:
                mejor = (acum, ruta)
            return
        for m in suc[n]:
            dfs(m, acum, ruta)
    for n in inicios:
        dfs(n, 0, [])
    return mejor


def run():
    dur = {n: v[0] for n, v in ACT.items()}
    es, ef, ls, lf, holg, fin = cpm(dur)
    largo, ruta = camino_mas_largo(dur)
    critica = [n for n in orden_topologico(ACT) if holg[n] == 0]
    rng = random.Random(124)
    n = 20000
    tot = []
    for _ in range(n):
        d = {k: rng.triangular(0.8 * v, 1.6 * v, v) for k, v in dur.items()}
        tot.append(cpm(d)[5])
    tot.sort()
    media = sum(tot) / n
    dur_medias = {k: (0.8 + 1.6 + 1.0) / 3 * v for k, v in dur.items()}
    fin_medias = cpm(dur_medias)[5]
    R = {"fin": fin, "largo": largo, "ruta": ruta, "critica": critica, "holg": holg, "media": media, "p50": tot[n // 2], "p80": tot[int(0.8 * n)], "p95": tot[int(0.95 * n)],
         "p_plazo": sum(1 for t in tot if t <= fin) / n, "fin_medias": fin_medias, "sesgo": media - fin_medias, "n_crit": len(critica),
         "holg_max": max(holg.values()), "es": es, "ef": ef, "ls": ls, "lf": lf, "dur_total_actividades": sum(dur.values()), "paralelismo": sum(dur.values()) / fin,
         "p_plazo_medias": sum(1 for t in tot if t <= fin_medias) / n}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Proyecto SINTETICO de 10 actividades (semanas)")
    print(" actividad                    dur  ES  EF  LS  LF  holgura")
    for n in orden_topologico(ACT):
        print(f" {n:<27} {ACT[n][0]:3d} {R['es'][n]:3d} {R['ef'][n]:3d} {R['ls'][n]:3d} {R['lf'][n]:3d} {R['holg'][n]:6d}{'  critica' if R['holg'][n] == 0 else ''}")
    print(f"Duracion CPM = {R['fin']} semanas ; camino mas largo por enumeracion = {R['largo']} ; ruta: {' > '.join(x[0] for x in R['ruta'])}")
    print(f"Duraciones triangulares (0.8 d, d, 1.6 d), 20000 simulaciones: media = {R['media']:.2f} ; P50 = {R['p50']:.2f} ; P80 = {R['p80']:.2f} ; P95 = {R['p95']:.2f}")
    print(f"  duracion CPM con duraciones medias = {R['fin_medias']:.2f} ; sesgo por convergencia de caminos = {R['sesgo']:.2f} semanas")
    print(f"  P(terminar en {R['fin']} semanas) = {R['p_plazo']:.4f} ; P(terminar en {R['fin_medias']:.1f}) = {R['p_plazo_medias']:.4f}")
    assert R["fin"] == R["largo"] and R["media"] >= R["fin_medias"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
