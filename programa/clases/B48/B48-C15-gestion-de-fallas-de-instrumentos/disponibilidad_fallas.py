"""Disponibilidad de un instrumento: MTBF, MTTR y redundancia de dos unidades.

Datos: MTBF 400 h y MTTR 8 h; reparaciones lognormales de sigma 0,8; 3000 h de noche al año:
ILUSTRATIVOS (no son datos de fallas de ningún instrumento). No se consultó ninguna fuente externa.
Modelo: A = MTBF / (MTBF + MTTR) para un proceso de renovación alternante (solo importan las medias);
con dos unidades independientes y reparación simultánea, A2 = 1 - (1 - A)^2.
Segunda vía: simulación de intervalos de 4 000 000 h con semilla 20261109.
Supuestos: tiempos de operación exponenciales; reparaciones independientes; sin piezas de repuesto limitadas.
Tolerancia: 0,0005 en la disponibilidad simple y 0,0002 en la doble.
"""
import math
import random

MTBF, MTTR = 400.0, 8.0
SIG = 0.8
H = 4_000_000.0
NOCHE = 3000.0


def intervalos_caida(rng):
    mu = math.log(MTTR) - SIG ** 2 / 2
    t = 0.0
    out = []
    while t < H:
        t += rng.expovariate(1 / MTBF)
        d = rng.lognormvariate(mu, SIG)
        out.append((t, min(t + d, H)))
        t += d
    return out


def interseccion(a, b):
    i = j = 0
    tot = 0.0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if hi > lo:
            tot += hi - lo
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return tot


def calc():
    rng = random.Random(20261109)
    u1 = intervalos_caida(rng)
    u2 = intervalos_caida(rng)
    caida1 = sum(b - a for a, b in u1)
    A = MTBF / (MTBF + MTTR)
    A1_sim = 1 - caida1 / H
    A2 = 1 - (1 - A) ** 2
    A2_sim = 1 - interseccion(u1, u2) / H
    media_rep = caida1 / len(u1)
    return dict(A=A, A1=A1_sim, A2=A2, A2s=A2_sim, rep=media_rep, perdidas=(1 - A) * NOCHE, perdidas2=(1 - A2) * NOCHE, n=len(u1))


def main():
    Q = calc()
    print(f"Averías simuladas: {Q['n']}; reparación media simulada {Q['rep']:.3f} h (objetivo {MTTR})")
    print(f"Disponibilidad simple: analítica {Q['A']:.5f} | simulada {Q['A1']:.5f}")
    print(f"Disponibilidad con dos unidades: analítica {Q['A2']:.6f} | simulada {Q['A2s']:.6f}")
    print(f"Horas de noche perdidas por año: {Q['perdidas']:.1f} con una unidad; {Q['perdidas2']:.2f} con dos")
    assert abs(Q["A"] - Q["A1"]) < 5e-4
    assert abs(Q["A2"] - Q["A2s"]) < 2e-4
    assert abs(Q["rep"] / MTTR - 1) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
