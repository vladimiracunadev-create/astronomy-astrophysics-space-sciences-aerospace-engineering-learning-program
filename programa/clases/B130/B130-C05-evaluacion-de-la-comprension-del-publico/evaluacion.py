#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C05: evaluacion pre/post de la comprension de un publico (datos SINTETICOS).

CONSULTADO (2026-11-11): Hake (1998), Am. J. Phys. 66, 64 (PDF leido con PyMuPDF): ganancia normalizada de un curso
<g> = (<Sf> - <Si>) / (100 - <Si>), con <Sf> y <Si> promedios (%) final e inicial; cursos de ganancia alta (<g> >= 0.7), media
(0.3 <= <g> < 0.7) y baja (<g> < 0.3). Hake estudio 62 cursos de fisica introductoria (N = 6542) con pruebas de mecanica; NO es astronomia
ni divulgacion, y sus medias (0.23 y 0.48) NO se usan aqui como referencia de nada.
NO CONSULTADO: la formula de KR-20 y de alfa de Cronbach (el servidor de la fuente respondio con una verificacion); se verifican entre si:
KR-20 y alfa deben coincidir para items dicotomicos (tolerancia 1e-12).
SINTETICOS: 60 personas, 12 items, modelo logistico (Rasch) con semilla 130, habilidades y dificultades inventadas. No describe a nadie.
Tolerancias: <g> a mano (40 -> 70 da 0.5) exacto a 1e-12; bootstrap con 2000 remuestreos, semilla 130.
"""
from __future__ import annotations
import math
import platform
import random

N, K = 60, 12


def generar(rng):
    dif = [-1.5 + 3.0 * i / (K - 1) for i in range(K)]  # dificultades de -1.5 a 1.5
    hab = [rng.gauss(-0.5, 1.0) for _ in range(N)]
    mejora = [max(0.0, rng.gauss(1.2, 0.6)) for _ in range(N)]

    def respuestas(theta):
        return [1 if rng.random() < 1 / (1 + math.exp(-(theta - d))) else 0 for d in dif]

    pre = [respuestas(t) for t in hab]
    post = [respuestas(t + m) for t, m in zip(hab, mejora)]
    return pre, post


def media_pct(matriz):
    return 100.0 * sum(sum(f) for f in matriz) / (len(matriz) * len(matriz[0]))


def ganancia_normalizada(pre_pct, post_pct):
    return (post_pct - pre_pct) / (100.0 - pre_pct)


def categoria(g):
    return "alta" if g >= 0.7 else ("media" if g >= 0.3 else "baja")


def varianza(x):
    m = sum(x) / len(x)
    return sum((v - m) ** 2 for v in x) / len(x)


def kr20(matriz):
    k = len(matriz[0])
    n = len(matriz)
    pq = sum((sum(f[j] for f in matriz) / n) * (1 - sum(f[j] for f in matriz) / n) for j in range(k))
    return k / (k - 1) * (1 - pq / varianza([sum(f) for f in matriz]))


def alfa(matriz):
    k = len(matriz[0])
    vi = sum(varianza([f[j] for f in matriz]) for j in range(k))
    return k / (k - 1) * (1 - vi / varianza([sum(f) for f in matriz]))


def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sx = math.sqrt(sum((a - mx) ** 2 for a in x))
    sy = math.sqrt(sum((b - my) ** 2 for b in y))
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def discriminacion(matriz, j):
    resto = [sum(f) - f[j] for f in matriz]
    return corr([f[j] for f in matriz], resto)


def bootstrap_g(pre, post, rng, reps=2000):
    gs = []
    for _ in range(reps):
        idx = [rng.randrange(N) for _ in range(N)]
        p = media_pct([pre[i] for i in idx])
        q = media_pct([post[i] for i in idx])
        gs.append(ganancia_normalizada(p, q))
    gs.sort()
    return gs[int(0.025 * reps)], gs[int(0.975 * reps) - 1]


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    assert abs(ganancia_normalizada(40.0, 70.0) - 0.5) < 1e-12
    rng = random.Random(130)
    pre, post = generar(rng)
    p, q = media_pct(pre), media_pct(post)
    g = ganancia_normalizada(p, q)
    print(f"Datos SINTETICOS: {N} personas, {K} items. Media pre = {p:.2f} %, media post = {q:.2f} %")
    print(f"Ganancia normalizada de la clase <g> = {g:.3f} ({categoria(g)}, umbrales de Hake 0.3 y 0.7)")
    lo, hi = bootstrap_g(pre, post, random.Random(130))
    print(f"Intervalo bootstrap 95 % de <g> (2000 remuestreos): [{lo:.3f}, {hi:.3f}]")
    assert lo <= g <= hi
    print("Items (dificultad = proporcion correcta; discriminacion = correlacion con el resto, post):")
    print("  item  pre   post  disc")
    for j in range(K):
        dp = sum(f[j] for f in pre) / N
        dq = sum(f[j] for f in post) / N
        print(f"  {j+1:>3}  {dp:.2f}  {dq:.2f}  {discriminacion(post, j):5.2f}")
    k1, a1 = kr20(post), alfa(post)
    print(f"Fiabilidad (post): KR-20 = {k1:.4f} ; alfa de Cronbach = {a1:.4f} ; diferencia = {abs(k1-a1):.1e}")
    assert abs(k1 - a1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
