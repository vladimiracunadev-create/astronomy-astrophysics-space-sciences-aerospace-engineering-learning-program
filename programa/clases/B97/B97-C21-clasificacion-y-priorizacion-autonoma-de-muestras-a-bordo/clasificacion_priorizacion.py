#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C21: clasificacion autonoma de muestras con espectros sinteticos y seleccion de datos bajo un presupuesto de enlace.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): dos clases (fondo y objetivo) con dos rasgos (profundidades de banda adimensionales), medias (0.10, 0.20) y (0.25, 0.10),
desviacion 0.06 en ambos rasgos, a priori iguales, 400 muestras de entrenamiento, 100000 de prueba, semilla fija. 40 observaciones candidatas con 50 a 500 kbit y valor cientifico de 1 a 10.
Ninguna cifra representa una mineralogia ni un instrumento real.
Modelo: clasificador gaussiano de varianzas iguales (media y varianza estimadas); probabilidad posterior por Bayes; valor esperado = posterior x valor cientifico;
seleccion bajo un presupuesto de 2400 kbit: voraz por valor/tamano y optimo exacto por programacion dinamica (0/1).
Segunda via: error de Bayes analitico Phi(-d/2) con d la distancia de Mahalanobis (tolerancia 3 sigma binomial) y programacion dinamica frente a fuerza bruta en una instancia de 16 elementos.
Unidades: kbit y adimensional. Sin ruido de instrumento mas alla del modelo, sin deriva de calibracion y sin dependencia entre observaciones.
"""
from __future__ import annotations
import itertools, math, platform, random

MU0, MU1, SIG, NTR, NTE, SEMILLA = (0.10, 0.20), (0.25, 0.10), 0.06, 400, 100000, 20261110     # SINTETICOS
NOBS, PRESUP = 40, 2400


def muestra(rng, clase):
    mu = MU1 if clase else MU0
    return (rng.gauss(mu[0], SIG), rng.gauss(mu[1], SIG))


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def entrenar(rng):
    datos = {c: [muestra(rng, c) for _ in range(NTR // 2)] for c in (0, 1)}
    medias = {c: tuple(sum(x[k] for x in datos[c]) / len(datos[c]) for k in (0, 1)) for c in (0, 1)}
    var = sum((x[k] - medias[c][k]) ** 2 for c in (0, 1) for x in datos[c] for k in (0, 1)) / (2 * NTR - 4)
    return medias, var


def posterior(x, medias, var):
    l = {c: -sum((x[k] - medias[c][k]) ** 2 for k in (0, 1)) / (2 * var) for c in (0, 1)}
    return 1.0 / (1.0 + math.exp(l[0] - l[1]))


def voraz(tam, val, presup):
    orden = sorted(range(len(tam)), key=lambda i: -val[i] / tam[i])
    tot, usado, sel = 0.0, 0, []
    for i in orden:
        if usado + tam[i] <= presup:
            usado += tam[i]; tot += val[i]; sel.append(i)
    return tot, usado


def dp(tam, val, presup):
    mejor = [0.0] * (presup + 1)
    for t, v in zip(tam, val):
        for c in range(presup, t - 1, -1):
            mejor[c] = max(mejor[c], mejor[c - t] + v)
    return mejor[presup]


def fuerza_bruta(tam, val, presup):
    best = 0.0
    for m in itertools.product((0, 1), repeat=len(tam)):
        if sum(t for t, b in zip(tam, m) if b) <= presup:
            best = max(best, sum(v for v, b in zip(val, m) if b))
    return best


def calc():
    rng = random.Random(SEMILLA)
    medias, var = entrenar(rng)
    errores = [0, 0]
    for _ in range(NTE):
        c = rng.random() < 0.5
        x = muestra(rng, int(c))
        pred = posterior(x, medias, var) > 0.5
        errores[int(c)] += pred != c
    err = sum(errores) / NTE
    d = math.hypot(MU1[0] - MU0[0], MU1[1] - MU0[1]) / SIG
    bayes = phi(-d / 2)
    sig = math.sqrt(bayes * (1 - bayes) / NTE)
    # priorizacion
    tam = [rng.randrange(50, 501) for _ in range(NOBS)]
    cient = [rng.randrange(1, 11) for _ in range(NOBS)]
    clases = [rng.random() < 0.3 for _ in range(NOBS)]
    post = [posterior(muestra(rng, int(c)), medias, var) for c in clases]
    val = [p * v for p, v in zip(post, cient)]
    v_g, usado = voraz(tam, val, PRESUP)
    v_o = dp([int(t) for t in tam], val, PRESUP)
    # verificacion de la DP contra fuerza bruta (16 elementos)
    t16, v16 = tam[:16], val[:16]
    dif_dp = abs(dp(t16, v16, 1200) - fuerza_bruta(t16, v16, 1200))
    return dict(err=err, bayes=bayes, d=d, z=abs(err - bayes) / sig, fpr=errores[0] / (NTE / 2), fnr=errores[1] / (NTE / 2), var=var, medias=medias,
                total_kbit=sum(tam), v_g=v_g, v_o=v_o, usado=usado, brecha=1 - v_g / v_o, dif_dp=dif_dp, v_total=sum(val), enviados=voraz(tam, val, PRESUP)[1],
                frac_v=v_o / sum(val), frac_bits=PRESUP / sum(tam), sig=math.sqrt(var), n_obj=sum(clases))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: d = {r['d']:.3f} (Mahalanobis); entrenamiento {NTR}; prueba {NTE}; semilla {SEMILLA}; desviacion estimada {r['sig']:.4f} (verdadera {SIG})")
    print(f"Error de prueba = {100*r['err']:.3f} %; error de Bayes analitico = {100*r['bayes']:.3f} % ({r['z']:.2f} sigma); falsos positivos {100*r['fpr']:.2f} %; falsos negativos {100*r['fnr']:.2f} %")
    print(f"Candidatas: {NOBS} observaciones ({r['n_obj']} del objetivo), {r['total_kbit']} kbit en total; presupuesto {PRESUP} kbit ({100*r['frac_bits']:.1f} % del total)")
    print(f"Valor esperado total = {r['v_total']:.2f}; voraz = {r['v_g']:.2f} ({r['usado']} kbit); optimo (DP) = {r['v_o']:.2f} ({100*r['frac_v']:.1f} % del valor); brecha del voraz = {100*r['brecha']:.2f} %")
    print(f"Diferencia DP frente a fuerza bruta (16 elementos) = {r['dif_dp']:.2e}")
    assert r["z"] < 3 and r["dif_dp"] < 1e-9 and r["v_o"] >= r["v_g"] - 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
