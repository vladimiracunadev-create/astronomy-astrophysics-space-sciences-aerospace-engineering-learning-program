"""Campaña observacional: probabilidad de completar las noches necesarias, con clima independiente y persistente.

Datos: SINTÉTICOS. Ventana de 30 noches y 18 noches despejadas necesarias; probabilidad de noche despejada 0,7273
(estacionaria de una cadena de Markov con P(despejado tras despejado) = 0,85 y P(despejado tras nublado) = 0,40).
No se consultó ninguna fuente externa ni se usa clima de ningún sitio real.
Modelo independiente: P(X >= k) binomial; ventana mínima para alcanzar 95 % de éxito. Modelo persistente:
cadena de Markov de dos estados simulada (semilla 20261109).
Supuestos: cada noche despejada rinde el mismo trabajo; sin Luna ni fallas técnicas.
Tolerancia: simulación independiente a 4 sigmas del binomial; la cadena persistente debe dar MENOS éxito.
"""
import math
import random

N, K = 30, 18
P_CC, P_NC = 0.85, 0.40
PI = P_NC / (1 - P_CC + P_NC)
REPS = 100000


def cola(n, k, p):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def ventana(k, p, objetivo=0.95):
    n = k
    while cola(n, k, p) < objetivo:
        n += 1
    return n


def markov(rng, n):
    estado = rng.random() < PI
    c = 0
    for _ in range(n):
        c += estado
        estado = rng.random() < (P_CC if estado else P_NC)
    return c


def calc():
    rng = random.Random(20261109)
    ind = cola(N, K, PI)
    sim_ind = sum(1 for _ in range(REPS) if sum(rng.random() < PI for _ in range(N)) >= K) / REPS
    sim_mk = sum(1 for _ in range(REPS) if markov(rng, N) >= K) / REPS
    return dict(pi=PI, ind=ind, sim_ind=sim_ind, sim_mk=sim_mk, esperadas=N * PI, w_ind=ventana(K, PI))


def main():
    Q = calc()
    print(f"Probabilidad estacionaria de noche despejada = {Q['pi']:.4f}; noches esperadas en 30 = {Q['esperadas']:.2f}")
    print(f"P(al menos {K} de {N}) independiente: analítica {Q['ind']:.5f} | simulada {Q['sim_ind']:.5f}")
    print(f"Con persistencia de Markov: {Q['sim_mk']:.5f}")
    print(f"Ventana mínima independiente para 95 % con {K} noches: {Q['w_ind']} noches")
    sig = math.sqrt(Q["ind"] * (1 - Q["ind"]) / REPS)
    assert abs(Q["ind"] - Q["sim_ind"]) < 4 * sig
    assert Q["sim_mk"] < Q["sim_ind"]
    assert cola(Q["w_ind"], K, PI) >= 0.95 > cola(Q["w_ind"] - 1, K, PI)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
