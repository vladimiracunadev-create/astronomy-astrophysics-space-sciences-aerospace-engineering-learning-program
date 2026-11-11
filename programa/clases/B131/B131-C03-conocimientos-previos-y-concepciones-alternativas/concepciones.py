#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C03: diagnostico de concepciones alternativas, ganancia normalizada y la fisica de las estaciones.

CONTENIDO EDUCATIVO. CONSULTADOS (2026-11-11):
  - Bailey y Slater (2004), Astronomy Education Review 2(2):20-45, PDF leido con PyMuPDF: la explicacion alternativa mas comun de las estaciones
    es el cambio de distancia Sol-Tierra; la de las fases lunares es un modelo de eclipse/sombra de la Tierra. Una entrevista video citada en la
    revision: 21 de 23 personas no dieron una explicacion cientifica de las estaciones o las fases (muestra pequena y no representativa).
  - Hake (1998), Am. J. Phys. 66:64-74, solo el RESUMEN: ganancia normalizada media 0.23 +- 0.04 en 14 cursos tradicionales y 0.48 +- 0.14 en 48
    cursos de 'interactive engagement' (mecanica, fisica introductoria; no es astronomia ni se generaliza).
NO CONSULTADOS (valores estandar): excentricidad e = 0.0167 y oblicuidad 23.44 deg; los umbrales 0.3 y 0.7 para clasificar la ganancia.
SINTETICO: el curso de 60 estudiantes (semilla 131), sus probabilidades de acierto y sus errores. Unidades: UA, grados, porcentajes.
Tolerancias: ganancia del curso calculada por dos vias (con medias y con conteos) coincide a 1e-12.
"""
from __future__ import annotations
import math, platform, random

E_ORB, OBLICUIDAD = 0.0167, 23.44


def flujo_relativo():
    q, Q = 1 - E_ORB, 1 + E_ORB  # perihelio y afelio en UA (semieje 1)
    return q, Q, (Q / q) ** 2


def insolacion_mediodia(lat, decl):
    cz = math.cos(math.radians(lat - decl))
    return max(cz, 0.0)


def ganancia(pre, post):
    return (post - pre) / (100.0 - pre)


def simular(n=60, p_pre=0.35, p_post=0.62, seed=131):
    rng = random.Random(seed)
    resp = []
    for _ in range(n):
        fila = []
        for it in range(2):  # item 1: estaciones ; item 2: fases
            for fase, p in (("pre", p_pre), ("post", p_post)):
                if rng.random() < p:
                    r = "correcta"
                else:
                    r = rng.choices(["distancia" if it == 0 else "sombra", "otra"], weights=[0.7, 0.3])[0]
                fila.append((it, fase, r))
        resp.append(fila)
    return resp


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Bailey y Slater 2004 CONSULTADO (PDF); Hake 1998 solo RESUMEN; e y oblicuidad estandar NO consultados; el curso es SINTETICO.")
    q, Q, fr = flujo_relativo()
    print(f"Distancia Sol-Tierra: perihelio {q:.4f} UA, afelio {Q:.4f} UA ; flujo perihelio/afelio = {fr:.4f} (+{100 * (fr - 1):.1f} %)")
    print("  El perihelio ocurre en enero: el hemisferio norte esta mas cerca en su invierno, de modo que la distancia no explica las estaciones.")
    lat = 45.0
    s_ver = insolacion_mediodia(lat, +OBLICUIDAD)
    s_inv = insolacion_mediodia(lat, -OBLICUIDAD)
    print(f"Insolacion al mediodia a {lat:.0f} deg N (cos del angulo cenital): solsticio de junio {s_ver:.4f} ; de diciembre {s_inv:.4f} ; cociente {s_ver / s_inv:.2f}")
    print(f"  Efecto de la inclinacion / efecto de la distancia = {(s_ver / s_inv - 1) / (fr - 1):.1f} veces")
    # curso sintetico
    resp = simular()
    n = len(resp)
    print(f"Curso SINTETICO de {n} estudiantes (semilla 131), 2 items: estaciones y fases lunares")
    for it, nom, alt in ((0, "estaciones", "distancia"), (1, "fases lunares", "sombra")):
        for fase in ("pre", "post"):
            xs = [r for f in resp for (i, fa, r) in f if i == it and fa == fase]
            ok = xs.count("correcta") / n
            print(f"  {nom:14s} {fase:4s}: correcta {100 * ok:5.1f} % ; distractor '{alt}' {100 * xs.count(alt) / n:5.1f} % ; otra {100 * xs.count('otra') / n:5.1f} %")
    # ganancia normalizada del curso (dos vias)
    pre = [sum(1 for (i, fa, r) in f if fa == "pre" and r == "correcta") for f in resp]
    post = [sum(1 for (i, fa, r) in f if fa == "post" and r == "correcta") for f in resp]
    pre_pct, post_pct = 100 * sum(pre) / (2 * n), 100 * sum(post) / (2 * n)
    g1 = ganancia(pre_pct, post_pct)
    g2 = (sum(post) - sum(pre)) / (2 * n - sum(pre))
    print(f"Pre {pre_pct:.1f} % ; post {post_pct:.1f} % ; ganancia normalizada del curso g = {g1:.3f} (por conteos {g2:.3f})")
    indiv = [(b - a) / (2 - a) for a, b in zip(pre, post) if a < 2]
    print(f"Media de ganancias individuales (solo con pre < maximo) = {sum(indiv) / len(indiv):.3f} sobre {len(indiv)} estudiantes")
    print(f"Referencia consultada (Hake, resumen): tradicional 0.23, interactivo 0.48; este g sintetico NO prueba ningun metodo.")
    assert abs(g1 - g2) < 1e-12
    assert abs(fr - 1.0689) < 5e-4
    assert s_ver / s_inv > 2.4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
