"""B132-C01: ciclos del Mecanismo de Anticitera y matriz de critica de fuentes.

Parte A: ciclos (inscripciones citadas por Freeth et al. 2006, consultadas) contra valores modernos.
Parte B: matriz de critica de fuentes con datos SINTETICOS (semilla fija).
Solo biblioteca estandar. Unidades: dias, anios, adimensional.
"""
import math
import random
import sys

SEMILLA = 20261111
MES_SINODICO = 29.530589      # d, valor moderno estandar (no consultado en una fuente concreta)
ANIO_TROPICO = 365.2422       # d, valor moderno estandar (no consultado en una fuente concreta)


def ciclos():
    """Compara ciclos con la aritmetica de sus periodos. 235, 223 y 'cuatro Metonicos menos un dia' son cifras de Freeth 2006."""
    meton_meses = 235
    meton_dias_tradicional = 6940                      # 19 anios de 365,25 d redondeados (valor tradicional)
    meton_sinodico = meton_meses * MES_SINODICO
    meton_tropico = 19 * ANIO_TROPICO
    callipo_dias = 4 * meton_dias_tradicional - 1      # Freeth 2006: cuatro Metonicos menos un dia
    callipo_tropico = 76 * ANIO_TROPICO
    saros_dias = 223 * MES_SINODICO
    return {
        "meton_sinodico": meton_sinodico, "meton_tropico": meton_tropico,
        "meton_dif": meton_sinodico - meton_tropico,
        "callipo_dias": callipo_dias, "callipo_tropico": callipo_tropico,
        "callipo_dif": callipo_dias - callipo_tropico,
        "saros_dias": saros_dias,
    }


# Parte B: fuentes SINTETICAS sobre un hecho ficticio. tipo: P primaria, S secundaria, T terciaria.
FUENTES = [
    # id, tipo, anios de distancia al hecho, grupo (copias comparten grupo), sesgo 0..1
    ("F1", "P", 0, "g1", 0.20),
    ("F2", "S", 40, "g1", 0.10),   # copia de F1
    ("F3", "S", 90, "g1", 0.10),   # copia de F1
    ("F4", "P", 20, "g2", 0.10),
    ("F5", "T", 400, "g3", 0.05),
]
PESO_TIPO = {"P": 1.0, "S": 0.6, "T": 0.3}
APOYA = {"A": ["F1", "F2", "F3"], "B": ["F4", "F5"]}   # afirmaciones rivales


def peso(f, tau):
    _, tipo, dist, _, sesgo = f
    return PESO_TIPO[tipo] * math.exp(-dist / tau) * (1.0 - sesgo)


def soporte(afirmacion, tau, ingenuo, pesos_mod=None):
    ids = APOYA[afirmacion]
    fs = [f for f in FUENTES if f[0] in ids]
    pw = {f[0]: peso(f, tau) * (pesos_mod[f[0]] if pesos_mod else 1.0) for f in fs}
    if ingenuo:
        return sum(pw.values())
    por_grupo = {}
    for f in fs:
        por_grupo[f[3]] = max(por_grupo.get(f[3], 0.0), pw[f[0]])
    return sum(por_grupo.values())


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    c = ciclos()
    print("Parte A. Ciclos (cifras 235, 223 y 4 Metonicos - 1 dia: Freeth et al. 2006; valores modernos: estandar)")
    print("  Metonico: 235 meses sinodicos = %.4f d ; 19 anios tropicos = %.4f d ; dif = %.4f d" % (c["meton_sinodico"], c["meton_tropico"], c["meton_dif"]))
    print("  Calipico: 4*6940-1 = %d d ; 76 anios tropicos = %.4f d ; dif = %.4f d" % (c["callipo_dias"], c["callipo_tropico"], c["callipo_dif"]))
    print("  Saros: 223 meses sinodicos = %.4f d (= %.4f anios tropicos)" % (c["saros_dias"], c["saros_dias"] / ANIO_TROPICO))
    assert abs(c["meton_dif"]) < 0.2
    assert abs(c["callipo_dif"]) < 1.0
    assert abs(c["callipo_dias"] - 27759) == 0

    print("Parte B. Matriz de critica de fuentes (datos SINTETICOS, hecho ficticio)")
    print(" id tipo dist[a] grupo sesgo  peso(tau=100)")
    for f in FUENTES:
        print(" %s   %s   %4d    %s    %.2f   %.3f" % (f[0], f[1], f[2], f[3], f[4], peso(f, 100.0)))
    for ing, nom in ((True, "ingenuo (suma de todas)"), (False, "por grupos independientes")):
        a = soporte("A", 100.0, ing)
        b = soporte("B", 100.0, ing)
        print("  %-27s A = %.3f  B = %.3f  -> gana %s" % (nom, a, b, "A" if a > b else "B"))
    assert soporte("A", 100.0, True) > soporte("B", 100.0, True)
    assert soporte("A", 100.0, False) < soporte("A", 100.0, True)

    rng = random.Random(SEMILLA)
    gana_a = 0
    n = 10000
    for _ in range(n):
        tau = rng.uniform(50.0, 400.0)
        mod = {f[0]: rng.uniform(0.8, 1.2) for f in FUENTES}
        if soporte("A", tau, False, mod) > soporte("B", tau, False, mod):
            gana_a += 1
    print("Sensibilidad (semilla %d, %d sorteos, tau 50-400 a, pesos +-20 %%): A gana en %.1f %% de los casos" % (SEMILLA, n, 100.0 * gana_a / n))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
