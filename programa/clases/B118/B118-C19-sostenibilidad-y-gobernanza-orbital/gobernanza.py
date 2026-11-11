"""B118-C19 · Sostenibilidad y gobernanza orbital.

Cuadro de cumplimiento de 30 operadores SINTÉTICOS frente a las 7 directrices de mitigación de la COPUOS (2010; consultadas el 2026-11-11
en el PDF de la UNOOSA) y estimación de la probabilidad de disposición exitosa con intervalo bootstrap (semilla 118).
Las tasas de cumplimiento por directriz son ILUSTRATIVAS: no describen a ningún operador ni Estado reales.
Las directrices COPUOS son voluntarias; el cuadro es una herramienta pedagógica, no una evaluación legal.
Unidades: adimensional. Tolerancia: la media bootstrap debe coincidir con la media muestral dentro de 0,01.
"""
import random
import sys

DIRECTRICES = [
    "1 Limitar desechos en operacion normal",
    "2 Minimizar rupturas en fase operativa",
    "3 Limitar la probabilidad de colision",
    "4 Evitar destruccion intencional",
    "5 Minimizar rupturas por energia almacenada",
    "6 Limitar presencia en LEO tras el fin de mision",
    "7 Limitar interferencia con la region GEO",
]
P_TRUE = [0.85, 0.80, 0.75, 0.95, 0.70, 0.65, 0.78]  # ILUSTRATIVAS


def generar(n=30, semilla=118):
    rng = random.Random(semilla)
    return [[1 if rng.random() < p else 0 for p in P_TRUE] for _ in range(n)]


def bootstrap(valores, B=4000, semilla=118):
    rng = random.Random(semilla)
    n = len(valores)
    medias = sorted(sum(valores[rng.randrange(n)] for _ in range(n)) / n for _ in range(B))
    return sum(medias) / B, medias[int(0.025 * B)], medias[int(0.975 * B)]


def compute():
    v = {}
    M = generar()
    v["n"] = len(M)
    v["por_directriz"] = [sum(f[k] for f in M) / len(M) for k in range(7)]
    v["por_operador"] = [sum(f) for f in M]
    v["pleno"] = sum(1 for s in v["por_operador"] if s == 7) / len(M)
    esperado_pleno = 1.0
    for p in P_TRUE:
        esperado_pleno *= p
    v["pleno_esperado"] = esperado_pleno
    # probabilidad de disposición exitosa: operadores que cumplen la directriz 6
    d6 = [f[5] for f in M]
    v["pmd"] = sum(d6) / len(d6)
    v["boot"] = bootstrap(d6)
    v["vs_90"] = v["pmd"] >= 0.90
    # sensibilidad: con n = 300 el intervalo se estrecha
    M300 = generar(300)
    v["boot300"] = bootstrap([f[5] for f in M300])
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("30 operadores SINTETICOS; cumplimiento por directriz ILUSTRATIVO (semilla 118). Directrices COPUOS 2010 (consultadas): voluntarias.")
    v = compute()
    for d, c in zip(DIRECTRICES, v["por_directriz"]):
        print(f"  {d:52s} {c:.3f}")
    print(f"Operadores que cumplen las 7: {v['pleno']:.3f} (esperado si fueran independientes: {v['pleno_esperado']:.3f})")
    print(f"Disposicion en LEO (directriz 6): {v['pmd']:.3f}; bootstrap media {v['boot'][0]:.3f}, IC95 [{v['boot'][1]:.3f}, {v['boot'][2]:.3f}]")
    print(f"Comparado con el 0.90 de IADC Rev.4 (consultado): {'cumple' if v['vs_90'] else 'NO cumple'}")
    print(f"Con 300 operadores sinteticos: IC95 [{v['boot300'][1]:.3f}, {v['boot300'][2]:.3f}]")
    assert abs(v["boot"][0] - v["pmd"]) < 0.01
    assert (v["boot300"][2] - v["boot300"][1]) < (v["boot"][2] - v["boot"][1])
    print("Pruebas superadas (bootstrap coherente con la media; el intervalo se estrecha con n).")


if __name__ == "__main__":
    main()
