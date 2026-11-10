#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C14: preparacion de CDR y TRR: cobertura de verificacion, preparacion de ensayos y nivel de vibracion (Grms).

Datos: SINTETICOS. Matriz de verificacion de ocho requisitos de ESTRELLA-S (metodos A/I/D/T segun el manual de NASA, S3), seis ensayos
con su lista de preparacion (TRR) y un perfil de vibracion aleatoria de ejemplo: (20 Hz, 0.01), (50 Hz, 0.04), (800 Hz, 0.04),
(2000 Hz, 0.01) en g2/Hz. Nivel de calificacion = nivel de aceptacion x 2 en DSP (+3 dB); duraciones de ejemplo. Modelo: Grms =
sqrt(integral de DSP df) con tramos log-log (formula analitica). Segunda via: integral numerica trapezoidal en rejilla logaritmica de
200000 puntos. Tolerancia: 1e-4 relativo. Sin sistema de referencia; g = 9.80665 m/s2 (NASA/NSSDC) solo para convertir a m/s2.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

PERFIL = [(20.0, 0.01), (50.0, 0.04), (800.0, 0.04), (2000.0, 0.01)]
# requisito: (metodo, ensayo asociado o None)
MATRIZ = {"R01": ("T", "E1"), "R02": ("T", "E2"), "R03": ("A", None), "R04": ("T", "E3"), "R05": ("A", None), "R06": ("T", "E4"),
          "R07": ("I", None), "R08": ("T", "E5")}
# ensayo: [procedimiento aprobado, equipo calibrado, configuracion congelada, personal capacitado, instalacion lista]
ENSAYOS = {"E1": [1, 1, 1, 1, 1], "E2": [1, 1, 1, 1, 1], "E3": [1, 0, 1, 1, 1], "E4": [1, 1, 0, 1, 1], "E5": [1, 1, 1, 1, 1], "E6": [1, 1, 1, 0, 0]}
CDR = [("Planos liberados [%]", 94.0, 90.0), ("Analisis cerrados [%]", 88.0, 95.0), ("Elementos criticos de compra adjudicados [%]", 100.0, 100.0)]


def grms_analitico(perfil, factor=1.0):
    area = 0.0
    for (f1, p1), (f2, p2) in zip(perfil[:-1], perfil[1:]):
        s = math.log(p2 / p1) / math.log(f2 / f1)
        r = f2 / f1
        area += p1 * f1 * math.log(r) if abs(s + 1) < 1e-12 else p1 * f1 / (s + 1) * (r ** (s + 1) - 1)
    return math.sqrt(area * factor)


def grms_numerico(perfil, factor=1.0):
    f = np.logspace(math.log10(perfil[0][0]), math.log10(perfil[-1][0]), 200000)
    lf, lp = np.log([p[0] for p in perfil]), np.log([p[1] for p in perfil])
    p = np.exp(np.interp(np.log(f), lf, lp))
    return math.sqrt(float(np.trapezoid(p * factor, f)))


def calcular():
    metodos = {m: sum(1 for v in MATRIZ.values() if v[0] == m) for m in "AIDT"}
    n = len(MATRIZ)
    ensayos_req = {v[1] for v in MATRIZ.values() if v[1]}
    listos = {k: all(v) for k, v in ENSAYOS.items()}
    n_list = sum(listos.values())
    faltan = {k: [i for i, x in enumerate(v) if not x] for k, v in ENSAYOS.items() if not all(v)}
    ga, gq = grms_analitico(PERFIL), grms_analitico(PERFIL, 2.0)
    gn = grms_numerico(PERFIL)
    cdr_ok = [v >= u for _, v, u in CDR]
    return dict(n_req=n, nA=metodos["A"], nI=metodos["I"], nD=metodos["D"], nT=metodos["T"], pct_T=100 * metodos["T"] / n,
                n_ensayos_req=len(ensayos_req), n_ensayos=len(ENSAYOS), n_listos=n_list, listos=listos, faltan=faltan,
                grms_a=ga, grms_q=gq, grms_num=gn, dif_rel=abs(ga - gn) / ga, ms2_a=ga * G0, razon_q=gq / ga,
                dosis_a=ga ** 2 * 60.0, dosis_q=gq ** 2 * 120.0, cdr_ok=cdr_ok, n_cdr_ok=sum(cdr_ok),
                trr_lista=all(listos[k] for k in ensayos_req))


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 8 requisitos, 6 ensayos, perfil de vibracion de ejemplo; metodos A/I/D/T segun S3; g = 9.80665 m/s2 (NASA/NSSDC)")
    print(f"Metodos de verificacion: analisis {V['nA']}, inspeccion {V['nI']}, demostracion {V['nD']}, ensayo {V['nT']} ({V['pct_T']:.1f} % por ensayo)")
    print(f"Ensayos necesarios para los requisitos: {V['n_ensayos_req']} de {V['n_ensayos']} definidos")
    nombres = ["procedimiento", "equipo calibrado", "configuracion", "personal", "instalacion"]
    for k, ok in V["listos"].items():
        falt = ", ".join(nombres[i] for i in V["faltan"].get(k, [])) or "-"
        print(f"  {k}: {'LISTO' if ok else 'NO LISTO'} ; falta: {falt}")
    print(f"Ensayos listos: {V['n_listos']} de {V['n_ensayos']} ; TRR de los ensayos requeridos: {'LISTA' if V['trr_lista'] else 'NO LISTA'}")
    print(f"Grms de aceptacion = {V['grms_a']:.4f} g ({V['ms2_a']:.3f} m/s2 rms) ; calificacion (+3 dB) = {V['grms_q']:.4f} g ; razon = {V['razon_q']:.4f}")
    print(f"Grms por integracion numerica = {V['grms_num']:.4f} g ; diferencia relativa = {V['dif_rel']:.2e}")
    print(f"Dosis g2*s por eje: aceptacion 60 s = {V['dosis_a']:.2f} ; calificacion 120 s = {V['dosis_q']:.2f}")
    print(f"Criterios de CDR de ejemplo cumplidos: {V['n_cdr_ok']} de {len(CDR)}")
    comprobar(V["dif_rel"] < 1e-4, "Grms analitico y numerico")
    comprobar(abs(V["razon_q"] - math.sqrt(2)) < 1e-12, "+3 dB en DSP multiplica Grms por raiz de 2")
    comprobar(V["n_req"] == V["nA"] + V["nI"] + V["nD"] + V["nT"], "todo requisito tiene un metodo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
