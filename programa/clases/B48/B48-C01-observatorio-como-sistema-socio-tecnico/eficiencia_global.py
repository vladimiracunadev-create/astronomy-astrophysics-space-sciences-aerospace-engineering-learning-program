"""Eficiencia global de un observatorio como producto de factores independientes.

Datos: factores ILUSTRATIVOS (no medidos en ningún observatorio): clima 0,72; telescopio 0,95;
instrumento 0,93; software 0,98; operación 0,85. No se consultó ninguna fuente externa.
Modelo: una noche es útil si todos los subsistemas funcionan; con independencia, P = producto de los factores.
Segunda vía: simulación de 200000 noches con semilla 20261109.
Supuestos: factores independientes y constantes; sin correlación entre clima y fallas.
Tolerancia: la simulación debe estar a menos de 4 desviaciones binomiales del producto.
"""
import math
import random

FACTORES = [("clima", 0.72), ("telescopio", 0.95), ("instrumento", 0.93), ("software", 0.98), ("operación", 0.85)]
N = 200000
SEMILLA = 20261109


def producto(fs):
    p = 1.0
    for _, f in fs:
        p *= f
    return p


def calc():
    rng = random.Random(SEMILLA)
    p = producto(FACTORES)
    utiles = 0
    for _ in range(N):
        if all(rng.random() < f for _, f in FACTORES):
            utiles += 1
    sim = utiles / N
    sigma = math.sqrt(p * (1 - p) / N)
    # sensibilidad: ganancia de subir 0,02 cada factor por separado
    gan = {}
    for nombre, f in FACTORES:
        gan[nombre] = p / f * 0.02
    # instrumento duplicado en paralelo (dos instrumentos intercambiables)
    f_inst = dict(FACTORES)["instrumento"]
    f_par = 1 - (1 - f_inst) ** 2
    p_par = p / f_inst * f_par
    return dict(p=p, sim=sim, sigma=sigma, z=(sim - p) / sigma, gan=gan, f_par=f_par, p_par=p_par, horas=p * 365 * 10)


def main():
    R = calc()
    print(f"Producto analítico P = {R['p']:.5f}")
    print(f"Simulación ({N} noches) = {R['sim']:.5f}  (sigma binomial {R['sigma']:.5f}, z = {R['z']:+.2f})")
    for k, v in R["gan"].items():
        print(f"Ganancia de subir {k} en 0,02: {v:.5f}")
    print(f"Instrumento duplicado: factor {R['f_par']:.4f}, P = {R['p_par']:.5f}")
    print(f"Horas útiles al año con 10 h de noche: {R['horas']:.1f}")
    assert abs(R["z"]) < 4
    assert max(R["gan"], key=R["gan"].get) == "clima"
    assert abs(R["gan"]["clima"] - R["p"] / 0.72 * 0.02) < 1e-12
    assert R["p_par"] > R["p"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
