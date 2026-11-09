"""Revisores ruidosos: correlación entre la nota media y el mérito verdadero.

Datos: SINTÉTICOS. Mérito verdadero normal (0, 1) de 400 propuestas; cada revisor añade ruido normal
de desviación 1,2 (ilustrativo). No se consultó ninguna fuente externa ni se modela un comité real.
Modelo: nota media de k revisores; correlación teórica r = 1 / sqrt(1 + s_e^2 / k) con s_mérito = 1.
Segunda vía: simulación con semilla 20261109 y también la fracción de aciertos al elegir el 25 % superior.
Supuestos: errores independientes y gaussianos, sin sesgos entre revisores.
Tolerancia: la correlación simulada a menos de 0,03 de la teórica (400 propuestas, 40 repeticiones).
"""
import math
import random
import statistics

SIG_E = 1.2
NPROP = 400
REP = 40
SEMILLA = 20261109


def teorica(k, se=SIG_E):
    return 1.0 / math.sqrt(1.0 + se * se / k)


def una_vez(rng, k):
    m = [rng.gauss(0, 1) for _ in range(NPROP)]
    nota = [mi + statistics.fmean(rng.gauss(0, SIG_E) for _ in range(k)) for mi in m]
    r = statistics.correlation(m, nota)
    n_sel = NPROP // 4
    top_v = set(sorted(range(NPROP), key=lambda i: m[i], reverse=True)[:n_sel])
    top_n = set(sorted(range(NPROP), key=lambda i: nota[i], reverse=True)[:n_sel])
    return r, len(top_v & top_n) / n_sel


def calc():
    rng = random.Random(SEMILLA)
    out = {}
    for k in (1, 2, 3, 5, 8):
        rs, ac = [], []
        for _ in range(REP):
            r, a = una_vez(rng, k)
            rs.append(r)
            ac.append(a)
        out[k] = dict(teo=teorica(k), sim=statistics.fmean(rs), acierto=statistics.fmean(ac))
    return out


def main():
    R = calc()
    for k, v in R.items():
        print(f"k = {k}: r teórica {v['teo']:.4f} | r simulada {v['sim']:.4f} | aciertos en el 25 % superior {v['acierto']:.3f}")
    for k, v in R.items():
        assert abs(v["teo"] - v["sim"]) < 0.03
    ks = list(R)
    assert all(R[a]["sim"] < R[b]["sim"] for a, b in zip(ks, ks[1:]))
    assert abs(teorica(1, 0.0) - 1.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
