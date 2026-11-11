"""B118-C06 · Probabilidad de colisión.

Plano de encuentro 2D: Pc = integral sobre el disco de radio R (radio combinado de los dos objetos) de una gaussiana 2D centrada
en el vector de desfase (miss) con covarianza combinada diagonal (sx, sy). Datos SINTÉTICOS (ningún evento real).
Unidades: m, adimensional. Sistema: plano de encuentro, x a lo largo del desfase, y perpendicular.
Verificación por tres vías: cuadratura 2D, aproximación de disco pequeño y Monte Carlo (semilla 118).
Tolerancias: cuadratura vs aproximación 1 % (R << sigma); Monte Carlo 3 sigma binomial.
"""
import math
import random
import sys


def pc_cuadratura(miss, sx, sy, radio, n=400):
    """Integral de la gaussiana sobre el disco con malla polar (n x n puntos medios)."""
    total = 0.0
    dr = radio / n
    dth = 2 * math.pi / n
    for i in range(n):
        r = (i + 0.5) * dr
        for j in range(n):
            th = (j + 0.5) * dth
            x, y = r * math.cos(th), r * math.sin(th)
            e = -0.5 * (((x - miss) / sx) ** 2 + (y / sy) ** 2)
            total += math.exp(e) * r * dr * dth
    return total / (2 * math.pi * sx * sy)


def pc_disco_pequeno(miss, sx, sy, radio):
    return radio ** 2 / (2 * sx * sy) * math.exp(-0.5 * (miss / sx) ** 2)


def pc_montecarlo(miss, sx, sy, radio, n=2_000_000, semilla=118):
    rng = random.Random(semilla)
    k = 0
    for _ in range(n):
        x = rng.gauss(miss, sx)
        y = rng.gauss(0.0, sy)
        if x * x + y * y <= radio * radio:
            k += 1
    return k / n, math.sqrt(max(k, 1)) / n


def compute():
    v = {}
    # Caso A: miss 200 m, sigmas 150 x 100 m, radio combinado 10 m
    v["A"] = dict(miss=200.0, sx=150.0, sy=100.0, R=10.0)
    A = v["A"]
    v["pcA_q"] = pc_cuadratura(A["miss"], A["sx"], A["sy"], A["R"], n=300)
    v["pcA_a"] = pc_disco_pequeno(A["miss"], A["sx"], A["sy"], A["R"])
    # Monte Carlo con un caso de Pc mayor para tener estadística: miss 50 m, sigmas 60x40, R 20 m
    v["B"] = dict(miss=50.0, sx=60.0, sy=40.0, R=20.0)
    B = v["B"]
    v["pcB_q"] = pc_cuadratura(B["miss"], B["sx"], B["sy"], B["R"], n=300)
    v["pcB_mc"], v["pcB_err"] = pc_montecarlo(B["miss"], B["sx"], B["sy"], B["R"])
    # Dilución: Pc frente a la escala de la covarianza (barrido), máximo
    barrido = []
    for s in (20, 50, 100, 200, 400, 800, 1600):
        barrido.append((s, pc_cuadratura(200.0, float(s), float(s), 10.0, n=120)))
    v["barrido"] = barrido
    v["s_max"] = max(barrido, key=lambda t: t[1])[0]
    # Pc con miss cero: R^2/(2 sx sy) (cuando R<<sigma)
    v["pc0_a"] = pc_disco_pequeno(0.0, 150.0, 100.0, 10.0)
    v["pc0_q"] = pc_cuadratura(0.0, 150.0, 100.0, 10.0, n=300)
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Eventos SINTETICOS en el plano de encuentro; relaciones estandar de la Pc 2D (no consultadas en una fuente concreta).")
    v = compute()
    A, B = v["A"], v["B"]
    print(f"Caso A: miss {A['miss']:.0f} m, sigmas {A['sx']:.0f} x {A['sy']:.0f} m, R {A['R']:.0f} m")
    print(f"  Pc cuadratura = {v['pcA_q']:.4e}; disco pequeno = {v['pcA_a']:.4e}; relacion {v['pcA_q'] / v['pcA_a']:.4f}")
    print(f"Caso B: miss {B['miss']:.0f} m, sigmas {B['sx']:.0f} x {B['sy']:.0f} m, R {B['R']:.0f} m")
    print(f"  Pc cuadratura = {v['pcB_q']:.5f}; Monte Carlo (2e6) = {v['pcB_mc']:.5f} +- {v['pcB_err']:.5f}")
    print("Dilucion (miss 200 m, R 10 m, sigma isotropica):")
    for s, p in v["barrido"]:
        print(f"  sigma {s:5d} m  Pc = {p:.4e}")
    print(f"Pc maxima en sigma = {v['s_max']} m (no en la covarianza mas pequena)")
    print(f"Miss 0, 150 x 100 m, R 10 m: cuadratura {v['pc0_q']:.4e}; R^2/(2 sx sy) = {v['pc0_a']:.4e}")
    assert abs(v["pcA_q"] / v["pcA_a"] - 1) < 0.01
    assert abs(v["pcB_q"] - v["pcB_mc"]) < 3 * v["pcB_err"] + 1e-4
    assert abs(v["pc0_q"] / v["pc0_a"] - 1) < 0.01
    assert 50 < v["s_max"] < 800
    print("Pruebas superadas (tres vias de calculo concordantes; maximo de dilucion).")


if __name__ == "__main__":
    main()
