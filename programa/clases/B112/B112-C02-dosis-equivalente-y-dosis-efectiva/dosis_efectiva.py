#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C02: dosis equivalente y dosis efectiva (cifras ILUSTRATIVAS).

Datos SINTETICOS: dosis absorbidas por organo y por tipo de radiacion de un campo inventado (semilla 113). Los factores de ponderacion de
la radiacion wR (fotones y electrones 1; protones 2; alfa e iones pesados 20) y de los tejidos wT (gonadas 0.08; medula, colon, pulmon,
estomago, mama y restantes 0.12; vejiga, higado, esofago, tiroides 0.04; superficie osea, cerebro, glandulas salivales, piel 0.01) son los
de uso corriente en proteccion radiologica; la tabla numerica de ICRP 103 NO estaba en el extracto consultado y debe verificarse en la
fuente. Del extracto si se verificaron las definiciones (wR multiplica la dosis absorbida de un tejido; la suma de wT es 1; para neutrones
wR es una funcion continua de la energia). Definiciones: H_T = sum_R wR * D_T,R [Sv]; E = sum_T wT * H_T [Sv]. Verificacion: sum wT = 1
dentro de 1e-12; con wR = 1 en todo, E = media ponderada de las dosis absorbidas; el orden de los organos no cambia E. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

WR = {"foton/electron": 1.0, "proton": 2.0, "alfa/ion pesado": 20.0}
WT = {"gonadas": 0.08, "medula osea": 0.12, "colon": 0.12, "pulmon": 0.12, "estomago": 0.12, "mama": 0.12, "restantes": 0.12,
      "vejiga": 0.04, "higado": 0.04, "esofago": 0.04, "tiroides": 0.04,
      "superficie osea": 0.01, "cerebro": 0.01, "glandulas salivales": 0.01, "piel": 0.01}


def equivalente(dosis_por_radiacion):
    return sum(WR[r] * d for r, d in dosis_por_radiacion.items())


def efectiva(h_por_organo):
    return sum(WT[t] * h for t, h in h_por_organo.items())


def q_de_let(l):
    """Funcion Q(L) habitual (L en keV/um); definicion NO consultada en este bloque, uso ilustrativo."""
    if l < 10:
        return 1.0
    if l <= 100:
        return 0.32 * l - 2.2
    return 300 / np.sqrt(l)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 113); factores wR y wT de uso corriente, tabla de ICRP 103 no consultada en el extracto")
    suma = sum(WT.values())
    print(f"Suma de wT = {suma:.12f}")
    assert abs(suma - 1) < 1e-12
    rng = np.random.default_rng(113)
    base = {"foton/electron": 0.30e-3, "proton": 0.45e-3, "alfa/ion pesado": 0.05e-3}  # Gy por dia, campo inventado
    dias = 100
    print(f"Campo inventado, {dias} dias: dosis absorbida media de cuerpo entero por radiacion [mGy]")
    for r, d in base.items():
        print(f"  {r:18s} {d*dias*1e3:8.2f} mGy  (wR = {WR[r]:.0f}) -> H = {WR[r]*d*dias*1e3:8.2f} mSv")
    d_total = sum(base.values()) * dias
    h_cuerpo = equivalente({r: d * dias for r, d in base.items()})
    print(f"Dosis absorbida total = {d_total*1e3:.2f} mGy; dosis equivalente de cuerpo entero = {h_cuerpo*1e3:.2f} mSv; razon H/D = {h_cuerpo/d_total:.3f} Sv/Gy")
    # dosis por organo: la media se modula con un factor de blindaje propio de cada organo (inventado)
    factor = {t: float(rng.uniform(0.7, 1.3)) for t in WT}
    h_org = {}
    for t in WT:
        h_org[t] = equivalente({r: d * dias * factor[t] for r, d in base.items()})
    e = efectiva(h_org)
    print(f"Dosis efectiva E = sum wT*H_T = {e*1e3:.2f} mSv (cuerpo entero uniforme: {h_cuerpo*1e3:.2f} mSv)")
    print(f"{'organo':22s} {'factor':>7s} {'H_T [mSv]':>10s} {'wT*H_T [mSv]':>13s}")
    for t in WT:
        print(f"{t:22s} {factor[t]:7.3f} {h_org[t]*1e3:10.2f} {WT[t]*h_org[t]*1e3:13.3f}")
    # verificaciones
    h_unif = {t: h_cuerpo for t in WT}
    assert abs(efectiva(h_unif) - h_cuerpo) < 1e-12, "con dosis uniforme E debe igualar H"
    orden = list(WT)
    rng.shuffle(orden)
    assert abs(sum(WT[t] * h_org[t] for t in orden) - e) < 1e-12
    # con wR = 1 en todo, E es media ponderada de las dosis absorbidas
    d_org = {t: sum(base.values()) * dias * factor[t] for t in WT}
    assert abs(efectiva(d_org) - sum(WT[t] * d_org[t] for t in WT)) < 1e-12
    # sensibilidad: la misma dosis absorbida con distinta calidad
    print("Misma dosis absorbida de cuerpo entero (10 mGy) segun la calidad de la radiacion:")
    for r in WR:
        print(f"  solo {r:18s}: E = {WR[r]*10:6.1f} mSv")
    # Q(L) frente a wR por LET
    print("Q(L) ilustrativo segun el LET [keV/um]: " + "; ".join(f"{l:g} -> {q_de_let(l):.2f}" for l in (0.3, 5, 10, 30, 100, 150, 500)))
    assert q_de_let(150) < q_de_let(100) + 1e-9 or q_de_let(150) < 30
    # la dosis efectiva no es la dosis de una persona concreta: dispersion por factores de organo
    n = 20000
    sim = []
    for _ in range(n):
        f = rng.uniform(0.7, 1.3, len(WT))
        sim.append(sum(WT[t] * h_cuerpo * fi for t, fi in zip(WT, f)))
    sim = np.array(sim)
    print(f"Dispersion de E por factores de organo inventados (20000 sorteos): media {sim.mean()*1e3:.2f} mSv, desv. tip. {sim.std()*1e3:.2f} mSv")
    assert abs(sim.mean() - h_cuerpo) / h_cuerpo < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
