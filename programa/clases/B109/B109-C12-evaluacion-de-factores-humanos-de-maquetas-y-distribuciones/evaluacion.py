#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C12: evaluacion de dos maquetas con NMSUS, contraste exacto de signos y acuerdo entre inspectores (kappa de Cohen).

Datos consultados (2026-11-10; NASA, resumen del NASA Modified System Usability Scale, NMSUS): 8 items de 1 a 5; NMSUS = 3.125 * ((Q1-1)+(5-Q2)+(Q3-1)+(5-Q4)+(Q5-1)+(5-Q6)+(Q7-1)+(5-Q8));
la validacion de la fuente uso 35 participantes con dos prototipos; el NMSUS es sensible a diferencias entre un prototipo bien y mal disenado.
SINTETICOS (las respuestas NO son de ninguna evaluacion real; las maquetas A y B no existen): 12 evaluadores simulados con respuestas a los 8 items (semilla 109012), listas de verificacion de 20 items
de dos inspectores simulados (semilla 109112), medias latentes de respuesta 3.4 (A) y 4.0 (B), cumplimiento base del primer inspector 0.80 y probabilidad 0.88 de que el segundo coincida.
Los 13 primeros items de una lista de habitabilidad real saldrian de las funciones minimas del concepto de Burke et al. (2022); aqui la lista es solo un vector de 20 si/no sinteticos.
Modelo: diferencia pareada d_i = NMSUS_B - NMSUS_A; contraste exacto de signos (2^12 = 4096 combinaciones) para la media; IC del 95 % por bootstrap (10000 remuestreos, semilla 109212).
Segunda via: casos extremos del NMSUS (todas las respuestas favorables = 100; todas neutras = 50; todas desfavorables = 0); el contraste exacto coincide con un sorteo Monte Carlo de signos (tolerancia 0.02);
kappa por la formula po-pe y por la forma cerrada 2(ad-bc)/((a+b)(b+d)+(a+c)(c+d)) (1e-12).
Unidades: NMSUS en puntos 0-100 (sin unidad); acuerdo en proporcion.
"""
from __future__ import annotations
import itertools, platform, random


def nmsus(q):
    s = sum((q[i] - 1) if i % 2 == 0 else (5 - q[i]) for i in range(8))
    return 3.125 * s


def respuestas(rng, mu):
    q = []
    for i in range(8):
        x = rng.gauss(mu, 0.8)
        v = x if i % 2 == 0 else 6 - x  # items pares (2,4,6,8) estan redactados en negativo
        q.append(min(5, max(1, round(v))))
    return q


def kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return po, (po - pe) / (1 - pe)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Respuestas y listas SINTETICAS (12 evaluadores simulados, 2 maquetas inexistentes); formula del NMSUS de la nota tecnica de NASA")
    # casos extremos
    fav = [5, 1, 5, 1, 5, 1, 5, 1]
    neu = [3] * 8
    des = [1, 5, 1, 5, 1, 5, 1, 5]
    print(f"Casos extremos: favorable = {nmsus(fav):.1f} ; neutro = {nmsus(neu):.1f} ; desfavorable = {nmsus(des):.1f}")
    assert nmsus(fav) == 100 and nmsus(neu) == 50 and nmsus(des) == 0
    rng = random.Random(109012)
    A = [nmsus(respuestas(rng, 3.4)) for _ in range(12)]
    B = [nmsus(respuestas(rng, 4.0)) for _ in range(12)]
    d = [b - a for a, b in zip(A, B)]
    media = sum(d) / 12
    print(f"NMSUS medio: maqueta A = {sum(A) / 12:.1f} ; maqueta B = {sum(B) / 12:.1f} ; diferencia media (B - A) = {media:.2f}")
    # contraste exacto de signos
    obs = abs(media)
    mayores = 0
    for signos in itertools.product((1, -1), repeat=12):
        if abs(sum(s * abs(x) for s, x in zip(signos, d)) / 12) >= obs - 1e-12:
            mayores += 1
    p_exacto = mayores / 4096
    rng2 = random.Random(7)
    mc = sum(1 for _ in range(20000) if abs(sum(rng2.choice((1, -1)) * abs(x) for x in d) / 12) >= obs - 1e-12) / 20000
    print(f"Contraste exacto de signos (4096 combinaciones): p = {p_exacto:.4f} ; Monte Carlo = {mc:.4f}")
    assert abs(p_exacto - mc) < 0.02
    rng3 = random.Random(109212)
    boots = sorted(sum(rng3.choice(d) for _ in range(12)) / 12 for _ in range(10000))
    print(f"IC 95 % bootstrap de la diferencia = [{boots[250]:.2f}, {boots[9750]:.2f}]")
    # lista de verificacion de 20 items por dos inspectores
    r1 = random.Random(109112)
    ins1 = [1 if r1.random() < 0.80 else 0 for _ in range(20)]
    ins2 = [x if r1.random() < 0.88 else 1 - x for x in ins1]
    po, k = kappa(ins1, ins2)
    a_ = sum(1 for x, y in zip(ins1, ins2) if x == 1 and y == 1)
    b_ = sum(1 for x, y in zip(ins1, ins2) if x == 1 and y == 0)
    c_ = sum(1 for x, y in zip(ins1, ins2) if x == 0 and y == 1)
    d_ = sum(1 for x, y in zip(ins1, ins2) if x == 0 and y == 0)
    k2 = 2 * (a_ * d_ - b_ * c_) / ((a_ + b_) * (b_ + d_) + (a_ + c_) * (c_ + d_))
    print(f"Lista de 20 items, 2 inspectores: cumple/cumple = {a_}, cumple/no = {b_}, no/cumple = {c_}, no/no = {d_}")
    print(f"Acuerdo observado = {po:.2f} ; kappa de Cohen = {k:.3f} (forma cerrada {k2:.3f})")
    assert abs(k - k2) < 1e-12
    cumple = (sum(ins1) + sum(ins2)) / 40
    print(f"Cumplimiento medio de la lista = {cumple:.2f} ({int(sum(ins1))} y {int(sum(ins2))} de 20 items)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
