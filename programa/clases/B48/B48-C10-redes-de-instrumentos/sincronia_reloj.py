"""Estimación del desfase de un reloj con cuatro marcas de tiempo y rutas asimétricas.

Datos: SINTÉTICOS. Desfase verdadero +12,0 ms; retardo base de subida 5,0 ms y de bajada 9,0 ms; retardo
aleatorio extra exponencial de media 3,0 ms por sentido; procesamiento en el servidor 0,1 ms. No se consultó
ninguna fuente externa ni se reproduce la especificación de ningún protocolo de tiempo.
Modelo: theta = ((t1 - t0) + (t2 - t3)) / 2 = theta0 + (d_sube - d_baja) / 2; retardo = (t3 - t0) - (t2 - t1).
Estrategia de filtro: de 8 intercambios se usa el de menor retardo.
Supuestos: reloj local sin deriva durante el intercambio; los retardos aleatorios son independientes.
Tolerancia: media del error a menos de 4 errores estándar de -2,0 ms; desviación a menos del 3 % de 2,121 ms.
"""
import math
import random
import statistics

TH0 = 12.0
UP, DOWN = 5.0, 9.0
JIT = 3.0
PROC = 0.1
N = 20000


def intercambio(rng):
    du = UP + rng.expovariate(1 / JIT)
    dd = DOWN + rng.expovariate(1 / JIT)
    t0 = 0.0
    t1 = t0 + du + TH0
    t2 = t1 + PROC
    t3 = t2 - TH0 + dd
    theta = ((t1 - t0) + (t2 - t3)) / 2
    delta = (t3 - t0) - (t2 - t1)
    return theta, delta


def calc():
    rng = random.Random(20261109)
    err1 = []
    err8 = []
    for _ in range(N):
        err1.append(intercambio(rng)[0] - TH0)
    for _ in range(N):
        lote = [intercambio(rng) for _ in range(8)]
        th, _ = min(lote, key=lambda x: x[1])
        err8.append(th - TH0)
    return dict(m1=statistics.fmean(err1), s1=statistics.stdev(err1), m8=statistics.fmean(err8), s8=statistics.stdev(err8),
                teo_m=(UP - DOWN) / 2, teo_s=math.sqrt(2) * JIT / 2)


def main():
    R = calc()
    print(f"Un intercambio: error medio {R['m1']:+.3f} ms (teórico {R['teo_m']:+.3f}); desviación {R['s1']:.3f} ms (teórica {R['teo_s']:.3f})")
    print(f"Filtro de menor retardo de 8: error medio {R['m8']:+.3f} ms; desviación {R['s8']:.3f} ms")
    assert abs(R["m1"] - R["teo_m"]) < 4 * R["teo_s"] / math.sqrt(N)
    assert abs(R["s1"] / R["teo_s"] - 1) < 0.03
    assert R["s8"] < R["s1"]
    assert abs(R["m8"] - R["teo_m"]) < 0.2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
