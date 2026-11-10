#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C16: registro de riesgos tecnicos con matriz 5x5, exposicion esperada y consumo de reserva de calendario.

Datos: SINTETICOS (diez riesgos de ESTRELLA-S, con probabilidad por nivel de verosimilitud, consecuencia 1-5 y retraso en dias
inventados). Convencion de ejemplo: puntaje = L x C; alto si >= 15, medio si 8-14, bajo si < 8. Probabilidades por nivel L: 0.05, 0.15,
0.30, 0.50, 0.70. Reserva de calendario 60 dias. Modelo: riesgos independientes tipo Bernoulli; exposicion = p x retraso.
Metodo 1: Monte Carlo (100000 muestras, semilla 83016). Segunda via: enumeracion exacta de los 2^10 subconjuntos de riesgos que ocurren.
Tolerancia: P(retraso <= reserva) entre ambas vias a 0.01. Mitigacion: bajar un nivel la verosimilitud de los tres puntajes mayores.
Sin constantes fisicas.
"""
import sys
from itertools import product
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

PL = {1: 0.05, 2: 0.15, 3: 0.30, 4: 0.50, 5: 0.70}
RIESGOS = [("K1", "Retraso del proveedor de la camara", 4, 4, 45), ("K2", "Crecimiento de masa", 4, 3, 20),
           ("K3", "Detector con TRL bajo", 3, 5, 60), ("K4", "Interferencia de espectro", 2, 4, 30),
           ("K5", "Fallo en el ensayo de vibracion", 2, 5, 50), ("K6", "Estacion de tierra indisponible", 3, 2, 7),
           ("K7", "Retraso del software de a bordo", 3, 3, 25), ("K8", "Envejecimiento de la bateria", 2, 3, 15),
           ("K9", "Cambio de fecha de lanzamiento", 3, 4, 40), ("K10", "Perdida de personal clave", 2, 3, 20)]
RESERVA = 60.0


def nivel(s): return "alto" if s >= 15 else ("medio" if s >= 8 else "bajo")


def exacta(ps, ds, reserva):
    ps, ds = np.array(ps), np.array(ds)
    prob = 0.0
    for bits in product([0, 1], repeat=len(ps)):
        b = np.array(bits)
        if (b * ds).sum() <= reserva:
            prob += float(np.prod(np.where(b == 1, ps, 1 - ps)))
    return prob


def montecarlo(ps, ds, reserva, n=100000):
    rng = np.random.default_rng(83016)
    ocurre = rng.random((n, len(ps))) < np.array(ps)
    tot = (ocurre * np.array(ds)).sum(axis=1)
    return float((tot <= reserva).mean()), float(tot.mean()), float(np.percentile(tot, 90))


def calcular(riesgos=RIESGOS):
    ps = [PL[r[2]] for r in riesgos]; ds = [r[4] for r in riesgos]
    pun = [r[2] * r[3] for r in riesgos]
    exp_ = [p * d for p, d in zip(ps, ds)]
    p_mc, media_mc, p90 = montecarlo(ps, ds, RESERVA)
    p_ex = exacta(ps, ds, RESERVA)
    # mitigacion de los tres mayores puntajes
    orden = sorted(range(len(riesgos)), key=lambda i: -pun[i])[:3]
    mit = [(r[0], r[1], max(1, r[2] - 1) if i in orden else r[2], r[3], r[4]) for i, r in enumerate(riesgos)]
    ps2 = [PL[r[2]] for r in mit]
    p_ex2 = exacta(ps2, ds, RESERVA)
    niveles = [nivel(s) for s in pun]
    return dict(pun=pun, niv=niveles, n_alto=niveles.count("alto"), n_medio=niveles.count("medio"), n_bajo=niveles.count("bajo"),
                exp=exp_, exp_total=sum(exp_), p_mc=100 * p_mc, p_ex=100 * p_ex, media_mc=media_mc, p90=p90, dif=abs(p_mc - p_ex),
                orden_top=[riesgos[i][0] for i in orden], p_ex2=100 * p_ex2, mayor_exp=riesgos[int(np.argmax(exp_))][0],
                exp_mayor=max(exp_), reserva=RESERVA, suma_max=sum(ds))


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 10 riesgos; puntaje = L x C (alto >= 15, medio 8-14, bajo < 8); reserva de calendario 60 dias")
    for r, s, n, e in zip(RIESGOS, V["pun"], V["niv"], V["exp"]):
        print(f"  {r[0]:3s} L{r[2]} C{r[3]} puntaje {s:2d} {n:5s} p={PL[r[2]]:.2f} retraso {r[4]:2d} d exposicion {e:5.2f} d  {r[1]}")
    print(f"Niveles: alto {V['n_alto']}, medio {V['n_medio']}, bajo {V['n_bajo']} ; exposicion esperada total = {V['exp_total']:.2f} d ; mayor: {V['mayor_exp']} ({V['exp_mayor']:.2f} d)")
    print(f"Retraso total simulado: media {V['media_mc']:.2f} d ; P90 {V['p90']:.1f} d ; maximo posible {V['suma_max']} d")
    print(f"P(retraso <= {V['reserva']:.0f} d): Monte Carlo {V['p_mc']:.2f} % ; enumeracion exacta {V['p_ex']:.2f} %")
    print(f"Mitigando {', '.join(V['orden_top'])} (L-1): P(retraso <= reserva) = {V['p_ex2']:.2f} %")
    comprobar(V["dif"] < 0.01, "Monte Carlo y enumeracion exacta")
    comprobar(abs(V["media_mc"] - V["exp_total"]) < 0.3, "la media simulada es la exposicion esperada")
    comprobar(V["p_ex2"] > V["p_ex"], "mitigar aumenta la probabilidad de cumplir la reserva")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
