#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C21: disponibilidad, presupuesto de error y plazo de entrega de un producto de datos (acuerdo de nivel de servicio), SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria legal ni un contrato real. MTBF, MTTR, plazos y creditos son SINTETICOS.
Modelo: tres componentes en serie (ingesta, procesamiento, distribucion), cada uno alterna entre funcionar (duracion exponencial de media MTBF) y reparacion
(exponencial de media MTTR). Disponibilidad estacionaria A = MTBF / (MTBF + MTTR). Serie: A_s = producto de A_i. Con dos instancias independientes en paralelo
del procesamiento: A_p' = 1 - (1 - A_p)^2.
Presupuesto de error de un objetivo de nivel de servicio (SLO) de 99.5 % en un mes de 720 h: 0.005 x 720 = 3.6 h de caida.
Plazo: tiempo de procesamiento por producto ~ lognormal(mediana 3 h, sigma 0.4); P(<= 6 h) = Phi(ln(6/3)/0.4), contrastada con Monte Carlo (200000, semilla 124).
Simulacion de disponibilidad: 2000 meses (1 440 000 h), semilla 124, union de intervalos de caida de los tres componentes; fraccion mensual de caida por mes.
Creditos de servicio (ilustrativos): disponibilidad mensual >= 99.5 %: 0 %; entre 99.0 y 99.5 %: 10 %; < 99.0 %: 25 % de la cuota mensual.
Tolerancias: disponibilidad simulada frente a analitica < 0.002 (ruido estadistico de la simulacion); probabilidad del plazo < 0.005.
"""
import math, platform, random

COMP = {"ingesta": (720.0, 4.0), "procesamiento": (500.0, 6.0), "distribucion": (1000.0, 2.0)}
MES = 720.0
MESES = 2000
SLO = 0.995


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def disp(mtbf, mttr):
    return mtbf / (mtbf + mttr)


def intervalos_caida(rng, mtbf, mttr, horizonte):
    t, out = 0.0, []
    while t < horizonte:
        t += rng.expovariate(1 / mtbf)
        d = rng.expovariate(1 / mttr)
        out.append((t, min(t + d, horizonte)))
        t += d
    return out


def union(ints):
    ints = sorted(ints)
    res = []
    for a, b in ints:
        if res and a <= res[-1][1]:
            res[-1] = (res[-1][0], max(res[-1][1], b))
        else:
            res.append((a, b))
    return res


def caida_mensual(merged, meses):
    c = [0.0] * meses
    for a, b in merged:
        m0, m1 = int(a // MES), min(int(b // MES), meses - 1)
        for m in range(m0, m1 + 1):
            lo, hi = max(a, m * MES), min(b, (m + 1) * MES)
            if hi > lo:
                c[m] += hi - lo
    return c


def run():
    A = {k: disp(*v) for k, v in COMP.items()}
    a_s = 1.0
    for v in A.values():
        a_s *= v
    ap2 = 1 - (1 - A["procesamiento"]) ** 2
    a_red = a_s / A["procesamiento"] * ap2
    rng = random.Random(124)
    horizonte = MES * MESES
    todos = []
    for k, (mtbf, mttr) in COMP.items():
        todos += intervalos_caida(rng, mtbf, mttr, horizonte)
    m = union(todos)
    cm = caida_mensual(m, MESES)
    a_sim = 1 - sum(cm) / horizonte
    disp_mes = [1 - c / MES for c in cm]
    p_exc = sum(1 for d in disp_mes if d < SLO) / MESES
    p_c10 = sum(1 for d in disp_mes if 0.99 <= d < SLO) / MESES
    p_c25 = sum(1 for d in disp_mes if d < 0.99) / MESES
    p_lat_an = phi(math.log(6 / 3) / 0.4)
    rr = random.Random(124)
    p_lat_mc = sum(1 for _ in range(200000) if math.exp(math.log(3) + 0.4 * rr.gauss(0, 1)) <= 6) / 200000
    R = {"a_ing": A["ingesta"], "a_pro": A["procesamiento"], "a_dis": A["distribucion"], "a_serie": a_s, "a_red": a_red, "ap2": ap2, "a_sim": a_sim, "dif_a": abs(a_sim - a_s),
         "presupuesto_h": (1 - SLO) * MES, "caida_esp_h": (1 - a_s) * MES, "caida_red_h": (1 - a_red) * MES, "p_exc": p_exc, "p_c10": p_c10, "p_c25": p_c25,
         "credito_esp": 0.10 * p_c10 + 0.25 * p_c25, "p_lat_an": p_lat_an, "p_lat_mc": p_lat_mc, "dif_lat": abs(p_lat_an - p_lat_mc), "cumple_slo": 1 if a_s >= SLO else 0, "a_ing_dis": A["ingesta"] * A["distribucion"],
         "cumple_red": 1 if a_red >= SLO else 0, "mejor_mes": max(disp_mes), "peor_mes": min(disp_mes)}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Producto de datos SINTETICO: 3 componentes en serie; SLO de disponibilidad mensual = 99.5 % (mes de 720 h)")
    for k, (mtbf, mttr) in COMP.items():
        print(f"  {k:<14} MTBF = {mtbf:6.0f} h ; MTTR = {mttr:4.1f} h ; A = {disp(mtbf, mttr):.5f}")
    print(f"Disponibilidad en serie = {R['a_serie']:.5f} ; presupuesto de error = {R['presupuesto_h']:.2f} h/mes ; caida esperada = {R['caida_esp_h']:.2f} h/mes ; cumple el SLO en promedio: {bool(R['cumple_slo'])}")
    print(f"Aun con procesamiento perfecto, ingesta x distribucion = {R['a_ing_dis']:.5f} (< {SLO}): el SLO no se alcanza con esos componentes")
    print(f"Con procesamiento redundante (2 instancias): A = {R['a_red']:.5f} ; caida esperada = {R['caida_red_h']:.2f} h/mes ; cumple: {bool(R['cumple_red'])}")
    print(f"Simulacion de {MESES} meses: disponibilidad = {R['a_sim']:.5f} ; diferencia con la analitica = {R['dif_a']:.5f}")
    print(f"  P(mes bajo 99.5 %) = {R['p_exc']:.4f} ; credito 10 %: {R['p_c10']:.4f} ; credito 25 %: {R['p_c25']:.4f} ; credito esperado = {100 * R['credito_esp']:.2f} % de la cuota ; mejor/peor mes = {R['mejor_mes']:.5f} / {R['peor_mes']:.5f}")
    print(f"Plazo de procesamiento <= 6 h: analitico = {R['p_lat_an']:.4f} ; Monte Carlo = {R['p_lat_mc']:.4f} ; diferencia = {R['dif_lat']:.4f}")
    assert R["dif_a"] < 0.002 and R["dif_lat"] < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
