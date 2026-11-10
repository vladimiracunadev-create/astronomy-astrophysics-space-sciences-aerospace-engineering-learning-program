#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C17: verificacion (producto frente a requisitos) y validacion (producto frente a la necesidad).

Distincion de NASA (S3): verificar = «se realizo bien el producto» frente a los requisitos; validar = «se realizo el producto correcto»
frente al CONOPS y el uso previsto. Datos: SINTETICOS. Mediciones de laboratorio inventadas: GSD 4.8 m (req. <= 5 m), MTF en Nyquist 0.12
(req. >= 0.10), SNR 105 a albedo 0.3 (req. >= 100). Escenario de validacion: detectar cambios de costa de 10 m con contraste relativo 0.08.
Modelo: MTF gaussiana MTF(f) = exp(-(f/f0)^2) con MTF(Nyquist) = 0.12; SNR proporcional a sqrt(albedo) (limite de ruido de disparo);
relacion contraste-ruido CNR = contraste x SNR x MTF(f); deteccion si CNR >= 5 (criterio de Rose: valor estandar NO consultado).
Metodo 1: Monte Carlo de 100000 escenas con albedo uniforme en [0.03, 0.40] (semilla 83017). Segunda via: albedo umbral analitico
y probabilidad exacta de deteccion = (0.40 - A*)/(0.40 - 0.03). Tolerancia: 0.5 puntos porcentuales. Sin constantes fisicas.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

REQ = [("GSD <= 5 m", 4.8, 5.0, "<="), ("MTF en Nyquist >= 0.10", 0.12, 0.10, ">="), ("SNR >= 100 a albedo 0.3", 105.0, 100.0, ">=")]
NECESIDADES = [("Cobertura de cultivos", True), ("Cambio de costa", None), ("Hielo estacional", True), ("Calidad del aire", True)]
RASGO, CONTRASTE, UMBRAL_CNR = 10.0, 0.08, 5.0
GSD_MED, MTF_NYQ, SNR_REF, ALB_REF = 4.8, 0.12, 105.0, 0.3
ALB_MIN, ALB_MAX = 0.03, 0.40


def mtf(f):
    nyq = 1 / (2 * GSD_MED)
    f0 = nyq / math.sqrt(-math.log(MTF_NYQ))
    return math.exp(-(f / f0) ** 2)


def cnr(albedo):
    f = 1 / (2 * RASGO)
    return CONTRASTE * SNR_REF * math.sqrt(albedo / ALB_REF) * mtf(f)


def calcular():
    ver = [(n, v, u, (v <= u) if op == "<=" else (v >= u)) for n, v, u, op in REQ]
    cnr_ref, cnr_agua = cnr(0.3), cnr(0.05)
    rng = np.random.default_rng(83017)
    alb = rng.uniform(ALB_MIN, ALB_MAX, 100000)
    f = 1 / (2 * RASGO)
    cn = CONTRASTE * SNR_REF * np.sqrt(alb / ALB_REF) * mtf(f)
    p_mc = float((cn >= UMBRAL_CNR).mean())
    snr_nec = UMBRAL_CNR / (CONTRASTE * mtf(f))
    a_umbral = ALB_REF * (snr_nec / SNR_REF) ** 2
    p_ex = (ALB_MAX - a_umbral) / (ALB_MAX - ALB_MIN)
    p_ex = min(1.0, max(0.0, p_ex))
    nec = [(n, (p_mc >= 0.95) if r is None else r) for n, r in NECESIDADES]
    return dict(ver=ver, n_ver_ok=sum(1 for x in ver if x[3]), n_req=len(ver), mtf_rasgo=mtf(f), cnr_ref=cnr_ref, cnr_agua=cnr_agua,
                p_mc=100 * p_mc, p_ex=100 * p_ex, dif=abs(p_mc - p_ex) * 100, snr_nec=snr_nec, a_umbral=a_umbral,
                nec=nec, n_val_ok=sum(1 for x in nec if x[1]), n_nec=len(nec), nyq=1 / (2 * GSD_MED), f_rasgo=f)


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: mediciones de laboratorio y escena inventadas; criterio de Rose (CNR >= 5) estandar no consultado")
    print("VERIFICACION (producto frente a requisitos):")
    for n, v, u, ok in V["ver"]:
        print(f"  {n:28s} medido {v:7.3f} umbral {u:7.3f}  {'CUMPLE' if ok else 'NO CUMPLE'}")
    print(f"  Requisitos verificados: {V['n_ver_ok']} de {V['n_req']}")
    print("VALIDACION (producto frente a la necesidad: detectar cambios de costa de 10 m, contraste 0.08):")
    print(f"  frecuencia del rasgo = {V['f_rasgo']:.4f} ciclos/m ; Nyquist = {V['nyq']:.4f} ; MTF en el rasgo = {V['mtf_rasgo']:.3f}")
    print(f"  CNR con albedo 0.30 = {V['cnr_ref']:.2f} ; con albedo 0.05 (agua) = {V['cnr_agua']:.2f} ; umbral = {UMBRAL_CNR:.1f}")
    print(f"  SNR necesaria = {V['snr_nec']:.1f} ; albedo umbral = {V['a_umbral']:.4f}")
    print(f"  Probabilidad de deteccion en escenas con albedo U[0.03, 0.40]: Monte Carlo {V['p_mc']:.2f} % ; analitica {V['p_ex']:.2f} %")
    for n, ok in V["nec"]:
        print(f"  Necesidad {n:24s} {'VALIDADA' if ok else 'NO VALIDADA'}")
    print(f"Necesidades validadas: {V['n_val_ok']} de {V['n_nec']} aunque se verificaron {V['n_ver_ok']} de {V['n_req']} requisitos")
    comprobar(V["n_ver_ok"] == V["n_req"] and V["n_val_ok"] < V["n_nec"], "todo verificado y no todo validado")
    comprobar(V["dif"] < 0.5, "Monte Carlo y probabilidad analitica")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
