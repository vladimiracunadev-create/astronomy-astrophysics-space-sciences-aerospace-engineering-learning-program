"""B113-C02: habituacion de la activacion ante escenarios simulados repetidos (modelo ILUSTRATIVO).

Pico de activacion en la exposicion n (n = 1, 2, ...):
    A_n = A_inf + (A_1 - A_inf) * exp(-k (n - 1))
Dentro de una exposicion la activacion decae: a(t) = a_pico * exp(-t / tau).
Unidades: A en u.a. (diferencia respecto de la linea base), t en minutos, k adimensional por exposicion.
Todos los datos son SINTETICOS; no miden a nadie ni tienen valor clinico. Solo biblioteca estandar.
"""
import math
import random
import sys

SEMILLA = 7
A1, AINF, K = 10.0, 3.0, 0.45  # ilustrativos
TAU = 8.0  # minutos, ilustrativo
SUJETOS = 30
EXPOSICIONES = 8


def pico(n, a1=A1, ainf=AINF, k=K):
    return ainf + (a1 - ainf) * math.exp(-k * (n - 1))


def ajustar_k(medias, ainf):
    """Regresion lineal de ln(A_n - A_inf) frente a (n-1); devuelve k = -pendiente."""
    xs = list(range(len(medias)))
    ys = [math.log(m - ainf) for m in medias]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return -sxy / sxx


def main():
    print("Python %s (biblioteca estandar)" % sys.version.split()[0])
    print("Datos SINTETICOS: A1=%.1f, Ainf=%.1f, k=%.2f, tau=%.1f min, %d sujetos, semilla %d" % (
        A1, AINF, K, TAU, SUJETOS, SEMILLA))
    rng = random.Random(SEMILLA)
    ks = [max(0.05, rng.gauss(K, 0.08)) for _ in range(SUJETOS)]
    medias = []
    for n in range(1, EXPOSICIONES + 1):
        vals = [pico(n, a1=A1 * rng.uniform(0.9, 1.1), k=k) + rng.gauss(0, 0.25) for k in ks]
        medias.append(sum(vals) / SUJETOS)
    print(" exposicion  pico medio (sim)  pico del modelo")
    for n, m in enumerate(medias, 1):
        print(" %6d %16.3f %16.3f" % (n, m, pico(n)))
    k_aj = ajustar_k(medias, AINF)
    print("k ajustado = %.4f ; k verdadero medio = %.4f ; error relativo = %.1f %%" % (
        k_aj, sum(ks) / SUJETOS, 100 * abs(k_aj - sum(ks) / SUJETOS) / (sum(ks) / SUJETOS)))
    n_mitad = 1 + math.log(2) / K
    print("Exposiciones para reducir a la mitad el exceso sobre Ainf: %.2f" % n_mitad)
    t90 = TAU * math.log(10)
    print("Tiempo para volver al 10 %% del pico dentro de una exposicion: %.2f min" % t90)
    # caso de sensibilizacion (k < 0): el modelo es el mismo con k negativo
    print("Contraejemplo ilustrativo con k = -0.10 (sensibilizacion): picos 1, 4, 8 =",
          ", ".join("%.2f" % pico(n, k=-0.10) for n in (1, 4, 8)))

    assert abs(pico(1) - A1) < 1e-12
    assert abs(pico(1 + math.log(2) / K) - (AINF + (A1 - AINF) / 2)) < 1e-9
    assert abs(ajustar_k([pico(n) for n in range(1, 9)], AINF) - K) < 1e-9
    assert abs(k_aj - sum(ks) / SUJETOS) / (sum(ks) / SUJETOS) < 0.15
    assert abs(TAU * math.log(10) - 18.42068) < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
