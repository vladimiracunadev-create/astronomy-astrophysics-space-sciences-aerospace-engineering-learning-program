"""Clasificación por voluntarios: voto mayoritario y voto ponderado por log-verosimilitud.

Datos: SINTÉTICOS. Aciertos de 0,70 por voluntario; grupo mixto de 2 expertos (0,90) y 3 novatos (0,60).
No se consultó ninguna fuente externa ni se describe ningún proyecto real de ciencia ciudadana.
Modelo: mayoría de n votantes independientes: P = suma_{k>n/2} C(n,k) p^k (1-p)^(n-k); voto ponderado con pesos
w = ln(p / (1 - p)) (óptimo si los votantes son independientes y el prior es 1/2), evaluado por enumeración exacta.
Segunda vía: simulación de 300000 clasificaciones con semilla 20261109.
Supuestos: independencia entre voluntarios (en la práctica hay correlación), dos categorías equiprobables.
Tolerancia: 4 desviaciones binomiales.
"""
import itertools
import math
import random


def mayoria(n, p):
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n // 2 + 1, n + 1))


def grupo_exacto(ps, ponderado):
    w = [math.log(p / (1 - p)) if ponderado else 1.0 for p in ps]
    tot = 0.0
    for aciertos in itertools.product((0, 1), repeat=len(ps)):
        pr = 1.0
        for a, p in zip(aciertos, ps):
            pr *= p if a else 1 - p
        s = sum(wi if a else -wi for wi, a in zip(w, aciertos))
        if s > 1e-12:
            tot += pr
        elif abs(s) <= 1e-12:
            tot += pr / 2
    return tot


def sim(rng, ps, ponderado, n=300000):
    w = [math.log(p / (1 - p)) if ponderado else 1.0 for p in ps]
    ok = 0.0
    for _ in range(n):
        s = sum(wi if rng.random() < p else -wi for wi, p in zip(w, ps))
        ok += 1.0 if s > 1e-12 else (0.5 if abs(s) <= 1e-12 else 0.0)
    return ok / n


def calc():
    rng = random.Random(20261109)
    mix = [0.9, 0.9, 0.6, 0.6, 0.6]
    return dict(may={n: mayoria(n, 0.7) for n in (1, 3, 5, 9, 15)}, may5_sim=sim(rng, [0.7] * 5, False),
                e_may=grupo_exacto(mix, False), e_pon=grupo_exacto(mix, True), s_may=sim(rng, mix, False), s_pon=sim(rng, mix, True))


def main():
    Q = calc()
    for n, v in Q["may"].items():
        print(f"Mayoría de {n:2d} voluntarios con 0,70: {v:.5f}")
    print(f"Simulación con 5: {Q['may5_sim']:.5f}")
    print(f"Grupo mixto, mayoría: exacta {Q['e_may']:.5f} | simulada {Q['s_may']:.5f}")
    print(f"Grupo mixto, ponderado: exacta {Q['e_pon']:.5f} | simulada {Q['s_pon']:.5f}")
    for a, b in ((Q["may"][5], Q["may5_sim"]), (Q["e_may"], Q["s_may"]), (Q["e_pon"], Q["s_pon"])):
        assert abs(a - b) < 4 * math.sqrt(a * (1 - a) / 300000)
    assert Q["e_pon"] > Q["e_may"]
    assert abs(Q["may"][3] - (3 * 0.49 * 0.3 + 0.343)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
