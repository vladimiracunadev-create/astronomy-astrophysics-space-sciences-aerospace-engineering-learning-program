"""Clasificación de la calidad de imagen: fracción de noches por clase, analítica y simulada.

Datos: SINTÉTICOS. Seeing por noche lognormal con mediana 0,90 arcsec y sigma del logaritmo 0,30; clases
A (hasta 0,7), B (hasta 1,0), C (hasta 1,5) y D (más): umbrales INVENTADOS, no son los de ningún observatorio.
No se consultó ninguna fuente externa.
Modelo: P(seeing <= s) = Phi((ln s - ln mediana) / sigma); noches de espera hasta una clase A: 1 / p_A.
Segunda vía: 400000 noches simuladas con semilla 20261109.
Supuestos: noches independientes; un solo valor representativo por noche.
Tolerancia: 4 desviaciones binomiales por clase.
"""
import math
import random
from statistics import NormalDist

MED, SIG = 0.90, 0.30
UMBRALES = [("A", 0.7), ("B", 1.0), ("C", 1.5), ("D", math.inf)]
N = 400000


def probas():
    nd = NormalDist(math.log(MED), SIG)
    ant = 0.0
    out = {}
    for nombre, u in UMBRALES:
        c = 1.0 if math.isinf(u) else nd.cdf(math.log(u))
        out[nombre] = c - ant
        ant = c
    return out


def clase(s):
    for nombre, u in UMBRALES:
        if s <= u:
            return nombre


def calc():
    teo = probas()
    rng = random.Random(20261109)
    cuenta = {k: 0 for k in teo}
    for _ in range(N):
        cuenta[clase(math.exp(rng.gauss(math.log(MED), SIG)))] += 1
    sim = {k: v / N for k, v in cuenta.items()}
    return dict(teo=teo, sim=sim, espera=1 / teo["A"], por_ano=365 * teo["A"])


def main():
    R = calc()
    for k in R["teo"]:
        sig = math.sqrt(R["teo"][k] * (1 - R["teo"][k]) / N)
        print(f"Clase {k}: analítica {R['teo'][k]:.5f} | simulada {R['sim'][k]:.5f} | sigma {sig:.5f}")
        assert abs(R["teo"][k] - R["sim"][k]) < 4 * sig
    print(f"Espera media hasta una noche A = {R['espera']:.2f} noches; noches A por año = {R['por_ano']:.1f}")
    assert abs(sum(R["teo"].values()) - 1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
