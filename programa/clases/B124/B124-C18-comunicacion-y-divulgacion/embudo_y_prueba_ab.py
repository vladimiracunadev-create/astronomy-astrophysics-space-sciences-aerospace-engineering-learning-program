#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C18: embudo de alcance de una campana de divulgacion y prueba A/B de dos mensajes, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria de marketing. Audiencias, tasas y mensajes son SINTETICOS.
Embudo: impresiones -> clics -> lectura completa -> comparticion -> seguidores nuevos; cada paso multiplica por una tasa.
Prueba A/B: dos mensajes con tasas verdaderas pA = 0.040 y pB = 0.046 de interaccion; n por brazo calculado para alfa = 0.05 (dos colas) y potencia 0.80:
n = (z_a sqrt(2 p q) + z_b sqrt(pA qA + pB qB))^2 / (pB - pA)^2, con p = (pA + pB)/2. Los cuantiles z se calculan por biseccion sobre la funcion de error.
Verificacion: 4000 experimentos simulados (semilla 124) con random.binomialvariate (Python >= 3.12): fraccion que rechaza H0 = potencia empirica (~0.80);
con pA = pB = 0.040 la fraccion que rechaza = alfa empirico (~0.05). Prueba z de dos proporciones con varianza agrupada.
Tolerancias: potencia empirica dentro de 0.03 de 0.80; alfa empirico dentro de 0.015 de 0.05.
"""
import math, platform, random

EMBUDO = [("impresiones", 200000, None), ("clics", None, 0.025), ("lectura completa", None, 0.40), ("comparticiones", None, 0.06), ("seguidores nuevos", None, 0.10)]
PA, PB = 0.040, 0.046
ALFA, POT = 0.05, 0.80


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def cuantil(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def tam_muestra(pa, pb, alfa=ALFA, pot=POT):
    za, zb = cuantil(1 - alfa / 2), cuantil(pot)
    p = (pa + pb) / 2
    num = (za * math.sqrt(2 * p * (1 - p)) + zb * math.sqrt(pa * (1 - pa) + pb * (1 - pb))) ** 2
    return math.ceil(num / (pb - pa) ** 2), za, zb


def z_dos_prop(xa, xb, n):
    p = (xa + xb) / (2 * n)
    se = math.sqrt(2 * p * (1 - p) / n)
    return (xb / n - xa / n) / se if se > 0 else 0.0


def rechaza(pa, pb, n, rng, reps, za):
    cuenta = 0
    for _ in range(reps):
        xa, xb = rng.binomialvariate(n, pa), rng.binomialvariate(n, pb)
        if abs(z_dos_prop(xa, xb, n)) > za:
            cuenta += 1
    return cuenta / reps


def run():
    cur, etapas = 0, []
    for nom, base, tasa in EMBUDO:
        cur = base if base is not None else cur * tasa
        etapas.append((nom, cur))
    n, za, zb = tam_muestra(PA, PB)
    rng = random.Random(124)
    pot_emp = rechaza(PA, PB, n, rng, 4000, za)
    alfa_emp = rechaza(PA, PA, n, rng, 4000, za)
    n_chico = n // 4
    pot_chico = rechaza(PA, PB, n_chico, rng, 4000, za)
    R = {"za": za, "zb": zb, "n": n, "pot_emp": pot_emp, "alfa_emp": alfa_emp, "n_chico": n_chico, "pot_chico": pot_chico, "efecto": PB / PA - 1,
         "retencion": etapas[-1][1] / etapas[0][1], "seguidores": etapas[-1][1], "comp": etapas[3][1], "clics": etapas[1][1], "lect": etapas[2][1], "etapas": etapas,
         "z_ejemplo": z_dos_prop(400, 460, 10000), "p_valor_ejemplo": 2 * (1 - phi(abs(z_dos_prop(400, 460, 10000))))}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar; random.binomialvariate requiere 3.12 o superior)")
    print("Campana SINTETICA de divulgacion (embudo):")
    for nom, v in R["etapas"]:
        print(f"  {nom:<20} {v:12.1f}")
    print(f"  retencion total impresiones -> seguidores = {100 * R['retencion']:.4f} %")
    print(f"Prueba A/B: pA = {PA}, pB = {PB} (efecto relativo {100 * R['efecto']:.1f} %) ; z_alfa/2 = {R['za']:.4f} ; z_potencia = {R['zb']:.4f} ; n por brazo = {R['n']}")
    print(f"  potencia empirica (4000 experimentos) = {R['pot_emp']:.4f} ; alfa empirico con pA = pB = {PA} -> {R['alfa_emp']:.4f}")
    print(f"  con la cuarta parte de la muestra ({R['n_chico']} por brazo): potencia empirica = {R['pot_chico']:.4f}")
    print(f"  ejemplo: 400/10000 frente a 460/10000 -> z = {R['z_ejemplo']:.3f} ; p-valor aprox. = {R['p_valor_ejemplo']:.4f}")
    assert abs(R["za"] - 1.959964) < 1e-5 and abs(R["zb"] - 0.841621) < 1e-5
    assert abs(R["pot_emp"] - POT) < 0.03 and abs(R["alfa_emp"] - ALFA) < 0.015
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
