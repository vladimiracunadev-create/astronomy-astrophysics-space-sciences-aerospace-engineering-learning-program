#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C11: sostenibilidad economica de una constelacion SINTETICA (reposicion de flota y punto de equilibrio).

CONTENIDO EDUCATIVO: no es asesoria financiera ni de inversion. Flota, costos, vida util y tarifas son SINTETICOS.
Modelo: N satelites de vida L (media 5 anios; vida individual ~ Uniforme(0.6 L, 1.4 L)); al fallar o terminar su vida un satelite se repone de inmediato.
Teoria de renovacion: tasa de reposicion en regimen = N / L. Costo anual de reposicion = (N / L) K (1 + r_desorbita), K = costo de construir y lanzar un satelite,
r_desorbita = reserva para desorbitar. Costos operativos fijos O por anio. Ingresos = S x ARPU x 12 (ARPU en um por suscriptor y mes).
Punto de equilibrio S* = (costo de reposicion + O) / (12 ARPU). Unidades: Mum (millones de um sinteticas) por anio; ARPU en um/mes.
Verificacion: simulacion de 200 flotas de 60 satelites durante 90 anios, descartando los primeros 30 de calentamiento (semilla 124), frente a N/L; tolerancia 3 %.
Sin calentamiento la cuenta sale ~4 % baja, porque todos los satelites parten con edad cero.
Despliegue inicial = N K (sin reposicion). Recuperacion simple = N K / (ingresos - costos anuales).
"""
import math, platform, random

N, L, K, R_DES, O = 60, 5.0, 1.5, 0.05, 20.0
ARPU = 50.0
S_BASE = 100_000


def costo_reposicion(vida=L):
    return N / vida * K * (1 + R_DES)


def s_equilibrio(vida=L, arpu=ARPU):
    return (costo_reposicion(vida) + O) * 1e6 / (12 * arpu)


def simular(rng, anios=90.0, calentamiento=30.0, flotas=200):
    tasas = []
    for _ in range(flotas):
        rep = 0
        for _ in range(N):
            t = 0.0
            while True:
                t += rng.uniform(0.6 * L, 1.4 * L)
                if t > anios:
                    break
                if t > calentamiento:
                    rep += 1
        tasas.append(rep / (anios - calentamiento))
    return sum(tasas) / len(tasas)


def run():
    rng = random.Random(124)
    teor = N / L
    sim = simular(rng)
    c_rep = costo_reposicion()
    s_star = s_equilibrio()
    ingreso = S_BASE * ARPU * 12 / 1e6
    margen = ingreso - c_rep - O
    R = {"tasa_teo": teor, "tasa_sim": sim, "err_rel": abs(sim - teor) / teor, "c_rep": c_rep, "costo_anual": c_rep + O, "s_star": s_star,
         "ingreso": ingreso, "margen": margen, "despliegue": N * K, "payback": N * K / margen if margen > 0 else -1.0,
         "costo_sub_mes": (c_rep + O) * 1e6 / (S_BASE * 12), "s_star_L3": s_equilibrio(3.5), "s_star_L7": s_equilibrio(7.0),
         "s_star_arpu": s_equilibrio(L, 40.0), "ratio_L35": s_equilibrio(3.5) / s_star}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Constelacion SINTETICA: N = {N}, L = {L} anios, K = {K} Mum/satelite, desorbita {100 * R_DES:.0f} %, O = {O} Mum/anio, ARPU = {ARPU} um/mes")
    print(f"Tasa de reposicion: teoria N/L = {R['tasa_teo']:.3f} sat/anio ; simulacion = {R['tasa_sim']:.3f} ; error relativo = {100 * R['err_rel']:.2f} %")
    print(f"Costo de reposicion = {R['c_rep']:.3f} Mum/anio ; costo anual total = {R['costo_anual']:.3f} Mum/anio")
    print(f"Punto de equilibrio S* = {R['s_star']:.0f} suscriptores ; con {S_BASE} suscriptores: ingresos = {R['ingreso']:.1f} Mum/anio ; margen = {R['margen']:.3f} Mum/anio")
    print(f"Costo por suscriptor-mes = {R['costo_sub_mes']:.2f} um ; despliegue inicial = {R['despliegue']:.1f} Mum ; recuperacion simple = {R['payback']:.2f} anios")
    print(f"Sensibilidad de S*: vida 3.5 anios -> {R['s_star_L3']:.0f} ; vida 7 anios -> {R['s_star_L7']:.0f} ; ARPU 40 -> {R['s_star_arpu']:.0f}")
    assert R["err_rel"] < 0.03
    assert abs(R["costo_anual"] - (N / L * K * (1 + R_DES) + O)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
