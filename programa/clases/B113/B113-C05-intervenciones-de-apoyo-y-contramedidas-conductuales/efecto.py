"""B113-C05: tamano del efecto de una contramedida SINTETICA e incertidumbre por remuestreo.

Dos grupos (control y con contramedida) con una puntuacion de bienestar SINTETICA en u.a.
Efecto verdadero (generado) delta = 0.5 desviaciones tipicas. Se calcula d de Cohen, g de Hedges,
intervalo por remuestreo (bootstrap percentil, 2000 remuestreos) y el error tipico analitico
SE = sqrt((n1+n2)/(n1 n2) + d^2 / (2 (n1+n2))). No es evidencia clinica. Solo biblioteca estandar.
"""
import math
import random
import sys

SEMILLA = 2026
DELTA = 0.5
SD = 10.0
MEDIA_CTRL = 50.0
B = 2000


def cohen_d(a, b):
    na, nb = len(a), len(b)
    ma, mb = sum(a) / na, sum(b) / nb
    va = sum((x - ma) ** 2 for x in a) / (na - 1)
    vb = sum((x - mb) ** 2 for x in b) / (nb - 1)
    sp = math.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    return (mb - ma) / sp


def hedges_g(d, n1, n2):
    return d * (1 - 3 / (4 * (n1 + n2) - 9))


def se_analitico(d, n1, n2):
    return math.sqrt((n1 + n2) / (n1 * n2) + d * d / (2 * (n1 + n2)))


def bootstrap(a, b, rng, reps=B):
    ds = []
    for _ in range(reps):
        ra = [rng.choice(a) for _ in a]
        rb = [rng.choice(b) for _ in b]
        ds.append(cohen_d(ra, rb))
    ds.sort()
    m = sum(ds) / reps
    sd = math.sqrt(sum((x - m) ** 2 for x in ds) / (reps - 1))
    return ds[int(0.025 * reps)], ds[int(0.975 * reps) - 1], sd


def main():
    print("Python %s (biblioteca estandar)" % sys.version.split()[0])
    print("Datos SINTETICOS: control N(%.0f, %.0f); con contramedida N(%.0f, %.0f) (delta = %.1f sd); semilla %d" % (
        MEDIA_CTRL, SD, MEDIA_CTRL + DELTA * SD, SD, DELTA, SEMILLA))
    rng = random.Random(SEMILLA)
    print("   n/grupo   d      g     SE analitico  SE bootstrap  IC95 % bootstrap       contiene delta")
    filas = []
    for n in (10, 30, 100, 300):
        a = [rng.gauss(MEDIA_CTRL, SD) for _ in range(n)]
        b = [rng.gauss(MEDIA_CTRL + DELTA * SD, SD) for _ in range(n)]
        d = cohen_d(a, b)
        lo, hi, sdb = bootstrap(a, b, rng)
        se = se_analitico(d, n, n)
        filas.append((n, d, se, sdb, lo, hi))
        print(" %8d %6.3f %6.3f %12.3f %13.3f   [%6.3f, %6.3f]   %s" % (
            n, d, hedges_g(d, n, n), se, sdb, lo, hi, "si" if lo <= DELTA <= hi else "no"))
    # potencia empirica: fraccion de ensayos con IC (aprox. normal, 1.96 SE) que excluye 0
    print("Fraccion de 400 ensayos sinteticos cuyo IC aproximado (d +- 1.96 SE) excluye 0:")
    pot = {}
    for n in (10, 30, 100):
        cnt = 0
        for _ in range(400):
            a = [rng.gauss(MEDIA_CTRL, SD) for _ in range(n)]
            b = [rng.gauss(MEDIA_CTRL + DELTA * SD, SD) for _ in range(n)]
            d = cohen_d(a, b)
            if abs(d) - 1.96 * se_analitico(d, n, n) > 0:
                cnt += 1
        pot[n] = cnt / 400
        print("  n = %3d por grupo: %.3f" % (n, pot[n]))

    for n, d, se, sdb, lo, hi in filas[1:]:
        assert abs(sdb - se) / se < 0.20, (n, sdb, se)
    assert filas[-1][5] - filas[-1][4] < filas[0][5] - filas[0][4]
    assert pot[10] < pot[30] < pot[100]
    assert abs(hedges_g(0.5, 15, 15) - 0.5 * (1 - 3 / 111)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
