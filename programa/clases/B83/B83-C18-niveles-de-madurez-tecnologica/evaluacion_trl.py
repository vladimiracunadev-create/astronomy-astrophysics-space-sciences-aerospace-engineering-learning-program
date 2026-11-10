#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C18: evaluacion de madurez tecnologica (TRL) por elemento, TRL del sistema y plan de madurizacion.

Reglas tomadas de NASA (S5, Apendice G, consultado 2026-11-10): el TRL del sistema es el menor TRL de sus elementos; un elemento heredado
cuyo entorno o arquitectura cambia baja a TRL 5 al menos inicialmente; integrar elementos nunca integrados puede bajar el TRL de la unidad.
Definiciones de TRL 1-9 de NASA (S6). Datos: SINTETICOS (ocho elementos de ESTRELLA-S con TRL declarado, bandera de herencia con cambio, bandera de
integracion no demostrada y dificultad de avance AD2 de 1 a 5, todo inventado). Costo de madurizacion de ejemplo: 3 meses por nivel x
(1 + 0.25 x (AD2 - 1)). Objetivo para PDR (regla del ejemplo): TRL >= 5; objetivo para CDR: TRL >= 6. Segunda via: minimo y conteos con numpy.
Sin constantes fisicas.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

# nombre, TRL declarado, heredado con cambio de entorno o arquitectura, integracion no demostrada, AD2
ELEM = [("Detector de imagen", 4, False, False, 4), ("Optica", 6, False, False, 2), ("Paneles solares", 9, False, False, 1),
        ("Bateria", 8, False, False, 1), ("Computadora de a bordo", 9, True, False, 2), ("Radio de banda X", 7, False, True, 3),
        ("Control de actitud", 9, False, False, 1), ("Propulsion", 9, True, True, 3)]
MESES_NIVEL, OBJ_PDR, OBJ_CDR = 3.0, 5, 6


def trl_efectivo(t, her, integ):
    e = t
    if her: e = min(e, 5)
    if integ: e = min(e, 6) if t > 6 else e
    return e


def calcular():
    ef = [trl_efectivo(t, h, i) for _, t, h, i, _ in ELEM]
    decl = [t for _, t, *_ in ELEM]
    sys_decl, sys_ef = min(decl), min(ef)
    # segunda via con numpy
    sys_np = int(np.min(np.array(ef)))
    bajo_pdr = [ELEM[i][0] for i, e in enumerate(ef) if e < OBJ_PDR]
    bajo_cdr = [ELEM[i][0] for i, e in enumerate(ef) if e < OBJ_CDR]
    meses = [max(0, OBJ_CDR - e) * MESES_NIVEL * (1 + 0.25 * (a - 1)) for e, (_, _, _, _, a) in zip(ef, ELEM)]
    degradados = [ELEM[i][0] for i in range(len(ELEM)) if ef[i] < decl[i]]
    prior = sorted(range(len(ELEM)), key=lambda i: -meses[i])
    return dict(ef=ef, decl=decl, sys_decl=sys_decl, sys_ef=sys_ef, sys_np=sys_np, bajo_pdr=bajo_pdr, bajo_cdr=bajo_cdr,
                n_bajo_pdr=len(bajo_pdr), n_bajo_cdr=len(bajo_cdr), meses=meses, total_meses=sum(meses), critica=max(meses),
                degradados=degradados, n_deg=len(degradados), mayor=ELEM[prior[0]][0], mayor_m=meses[prior[0]],
                prom_decl=float(np.mean(decl)), prom_ef=float(np.mean(ef)))


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 8 elementos; reglas de TRL de NASA (S5): TRL del sistema = minimo; herencia con cambio baja a 5")
    print(f"{'elemento':26s} {'declarado':>9s} {'efectivo':>9s} {'AD2':>4s} {'meses a TRL 6':>14s}")
    for (n, t, h, i, a), e, m in zip(ELEM, V["ef"], V["meses"]):
        print(f"{n:26s} {t:9d} {e:9d} {a:4d} {m:14.2f}" + ("  (herencia con cambio)" if h else "") + ("  (integracion no demostrada)" if i else ""))
    print(f"TRL del sistema: declarado {V['sys_decl']} ; efectivo {V['sys_ef']} (con numpy: {V['sys_np']}) ; promedio {V['prom_decl']:.2f} -> {V['prom_ef']:.2f}")
    print(f"Elementos degradados por herencia o integracion: {V['n_deg']} -> {', '.join(V['degradados'])}")
    print(f"Por debajo de TRL {OBJ_PDR} (PDR): {V['n_bajo_pdr']} -> {', '.join(V['bajo_pdr'])} ; por debajo de TRL {OBJ_CDR} (CDR): {V['n_bajo_cdr']}")
    print(f"Esfuerzo de madurizacion a TRL {OBJ_CDR}: total {V['total_meses']:.2f} meses-elemento ; ruta critica en paralelo {V['critica']:.2f} meses ; mayor: {V['mayor']} ({V['mayor_m']:.2f} meses)")
    comprobar(V["sys_ef"] == V["sys_np"], "minimo por dos vias")
    comprobar(V["sys_ef"] <= V["sys_decl"], "el TRL efectivo no supera al declarado")
    comprobar(all(e <= t for e, t in zip(V["ef"], V["decl"])), "ningun elemento sube de nivel por herencia")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
