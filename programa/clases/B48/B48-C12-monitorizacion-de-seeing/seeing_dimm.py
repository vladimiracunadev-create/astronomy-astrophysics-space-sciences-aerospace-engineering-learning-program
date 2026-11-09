"""Monitor de seeing por movimiento diferencial de imagen: de la varianza a r0 y al seeing.

Datos: r0 = 0,100 m (ilustrativo), lambda = 500 nm, subaperturas de D = 0,10 m con separación d = 0,20 m.
Los coeficientes 0,179 y 0,0968 de la varianza longitudinal son los que recuerda el autor del texto de
Sarazin y Roddier (1990); NO se verificaron contra el artículo. No se consultó ninguna fuente externa.
Modelo: var_long = 2 lambda^2 r0^(-5/3) [0,179 D^(-1/3) - 0,0968 d^(-1/3)]; seeing = 0,98 lambda / r0.
Como var ~ r0^(-5/3), la incertidumbre relativa de r0 es (3/5) sqrt(2/N) con N medidas gaussianas.
Segunda vía: 600 repeticiones con N = 1000 medidas, semilla 20261109.
Supuestos: turbulencia de Kolmogorov, exposición corta, movimientos gaussianos, sin ruido de centroide.
Tolerancia: desviación relativa simulada de r0 a menos del 8 % de la analítica.
"""
import math
import random
import statistics

LAM = 500e-9
D, SEP = 0.10, 0.20
R0 = 0.100
N = 1000
REP = 600
ARC = 206264.806


def var_long(r0):
    return 2 * LAM ** 2 * r0 ** (-5 / 3) * (0.179 * D ** (-1 / 3) - 0.0968 * SEP ** (-1 / 3))


def r0_de_var(v):
    return (2 * LAM ** 2 * (0.179 * D ** (-1 / 3) - 0.0968 * SEP ** (-1 / 3)) / v) ** (3 / 5)


def seeing(r0):
    return 0.98 * LAM / r0 * ARC


def calc():
    v = var_long(R0)
    rng = random.Random(20261109)
    est = []
    for _ in range(REP):
        x = [rng.gauss(0, math.sqrt(v)) for _ in range(N)]
        vm = sum(t * t for t in x) / N
        est.append(r0_de_var(vm))
    return dict(v=v, sd=math.sqrt(v), r0_ida=r0_de_var(v), s_ver=seeing(R0), media=statistics.fmean(est),
                rel_sim=statistics.stdev(est) / R0, rel_teo=0.6 * math.sqrt(2 / N), s_med=seeing(statistics.fmean(est)))


def main():
    R = calc()
    print(f"Varianza longitudinal = {R['v']:.4e} rad^2; desviación = {R['sd'] * ARC:.4f} arcsec")
    print(f"r0 recuperado sin ruido = {R['r0_ida']:.6f} m; seeing verdadero = {R['s_ver']:.4f} arcsec")
    print(f"r0 medio con N = {N}: {R['media']:.5f} m; incertidumbre relativa simulada {R['rel_sim']:.4f} | analítica {R['rel_teo']:.4f}")
    print(f"Seeing medio estimado = {R['s_med']:.4f} arcsec")
    assert abs(R["r0_ida"] - R0) < 1e-12
    assert abs(R["rel_sim"] / R["rel_teo"] - 1) < 0.08
    assert abs(R["media"] / R0 - 1) < 0.004
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
