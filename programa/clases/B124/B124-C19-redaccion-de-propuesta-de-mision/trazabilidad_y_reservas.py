#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C19: matriz de trazabilidad de una propuesta de mision y presupuesto de masa con reservas, SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria de redaccion de propuestas ni de ingenieria de sistemas. Objetivos, requisitos, secciones y masas son SINTETICOS.
Los porcentajes de crecimiento por madurez (5, 10, 20, 30 %) son ILUSTRATIVOS (no provienen de ninguna norma consultada).
Parte 1: trazabilidad objetivo -> requisito -> seccion. Cobertura de requisitos = requisitos citados por al menos una seccion / total; seccion huerfana = no cita
ningun requisito. Se calcula por filas y por columnas (transpuesta) y deben coincidir.
Parte 2: masa maxima esperada MEV = sum CBE (1 + g). Margen = (limite - MEV) / limite. Crecimiento real de cada componente ~ Triangular(0, 2 g, moda g), de media g y varianza g^2/6
por unidad de CBE al cuadrado. 40000 simulaciones (semilla 124); la media y la desviacion simuladas se comparan con las analiticas y P(masa > limite) con la aproximacion normal.
Unidades: kg. Tolerancias: media simulada dentro de 0.5 %, desviacion dentro de 3 %, probabilidad dentro de 0.02.
"""
import math, platform, random

REQ = {  # requisito: objetivo
    "R1": "G1", "R2": "G1", "R3": "G2", "R4": "G2", "R5": "G2", "R6": "G3", "R7": "G3", "R8": "G1",
}
SECC = {  # seccion: requisitos que cita
    "S1 resumen": ["R1", "R3", "R6"],
    "S2 objetivos cientificos": ["R1", "R2", "R8"],
    "S3 implementacion tecnica": ["R3", "R4", "R5"],
    "S4 plan de gestion": ["R6"],
    "S5 presupuesto": ["R4", "R5"],
    "S6 anexo de CVs": [],
}
COMP = [  # nombre, CBE kg, madurez
    ("estructura", 90.0, "modificado"), ("potencia", 70.0, "heredado"), ("computadora", 20.0, "heredado"), ("comunicaciones", 25.0, "modificado"),
    ("termica", 30.0, "modificado"), ("propulsion", 55.0, "nuevo diseno"), ("instrumento A", 40.0, "nueva tecnologia"), ("instrumento B", 25.0, "nuevo diseno"),
]
G = {"heredado": 0.05, "modificado": 0.10, "nuevo diseno": 0.20, "nueva tecnologia": 0.30}
LIMITE = 420.0


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def run():
    citados = {r for rs in SECC.values() for r in rs}
    cobertura_filas = len(citados & set(REQ)) / len(REQ)
    cobertura_cols = sum(1 for r in REQ if any(r in rs for rs in SECC.values())) / len(REQ)
    sin_cubrir = sorted(set(REQ) - citados)
    huerfanas = [s for s, rs in SECC.items() if not rs]
    por_objetivo = {}
    for r, g in REQ.items():
        por_objetivo.setdefault(g, []).append(r)
    cbe = sum(c[1] for c in COMP)
    mev = sum(c[1] * (1 + G[c[2]]) for c in COMP)
    margen = (LIMITE - mev) / LIMITE
    sd = math.sqrt(sum((c[1] * G[c[2]]) ** 2 / 6 for c in COMP))
    lineal = sum(c[1] * G[c[2]] for c in COMP)
    rng = random.Random(124)
    n = 40000
    tot = []
    for _ in range(n):
        tot.append(sum(c[1] * (1 + rng.triangular(0, 2 * G[c[2]], G[c[2]])) for c in COMP))
    media = sum(tot) / n
    sd_mc = math.sqrt(sum((t - media) ** 2 for t in tot) / n)
    p_mc = sum(1 for t in tot if t > LIMITE) / n
    p_norm = 1 - phi((LIMITE - mev) / sd)
    R = {"cob": cobertura_filas, "cob2": cobertura_cols, "n_sin": len(sin_cubrir), "sin_cubrir": ",".join(sin_cubrir), "huerfanas": ",".join(huerfanas), "n_huerf": len(huerfanas),
         "cbe": cbe, "mev": mev, "crecim": mev - cbe, "pct_crec": (mev - cbe) / cbe, "margen": margen, "limite": LIMITE, "sd": sd, "rss_sd": sd, "lineal": lineal,
         "media_mc": media, "dif_media": abs(media - mev) / mev, "sd_mc": sd_mc, "dif_sd": abs(sd_mc - sd) / sd, "p_mc": p_mc, "p_norm": p_norm, "dif_p": abs(p_mc - p_norm),
         "n_g1": len(por_objetivo["G1"]), "n_g2": len(por_objetivo["G2"]), "n_g3": len(por_objetivo["G3"]), "n_req": len(REQ)}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Parte 1 - trazabilidad SINTETICA: 3 objetivos, 8 requisitos, 6 secciones")
    for s, rs in SECC.items():
        print(f"  {s:<26} cita: {', '.join(rs) if rs else '(ninguno)'}")
    print(f"  cobertura de requisitos = {100 * R['cob']:.1f} % (por columnas {100 * R['cob2']:.1f} %) ; sin cubrir: {R['sin_cubrir']} ; secciones huerfanas: {R['huerfanas']}")
    print("Parte 2 - presupuesto de masa (kg); crecimiento por madurez ILUSTRATIVO")
    for nom, m, mad in COMP:
        print(f"  {nom:<16} CBE = {m:6.1f}  {mad:<17} g = {100 * G[mad]:4.0f} %  MEV = {m * (1 + G[mad]):7.2f}")
    print(f"  CBE total = {R['cbe']:.1f} ; MEV = {R['mev']:.2f} ; reserva total = {R['crecim']:.2f} ({100 * R['pct_crec']:.1f} %) ; limite = {R['limite']:.0f} ; margen = {100 * R['margen']:.2f} %")
    print(f"  desviacion analitica = {R['sd']:.3f} ; Monte Carlo: media = {R['media_mc']:.2f} (dif {100 * R['dif_media']:.2f} %), desviacion = {R['sd_mc']:.3f} (dif {100 * R['dif_sd']:.2f} %)")
    print(f"  P(masa > limite): Monte Carlo = {R['p_mc']:.4f} ; aproximacion normal = {R['p_norm']:.4f} ; diferencia = {R['dif_p']:.4f}")
    assert R["cob"] == R["cob2"] and R["dif_media"] < 0.005 and R["dif_sd"] < 0.03 and R["dif_p"] < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
