#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C08: relevo de control entre dos operadores con perdida de mensajes y fencing por epoca.

Datos: TODOS SINTETICOS (no medidos; no describen ninguna organizacion ni mision; semilla 98008). Unidades: segundos de reloj
de operaciones. Un relevo traspasa la autoridad de comando de A a B sobre el vehiculo. Mensajes en la red de operaciones se
pierden con probabilidad p = 0.15 (SINTETICA) por mensaje; retransmision cada 10 s; el briefing previo no se modela.
Protocolos comparados (10000 relevos cada uno):
  NAIVE: A anuncia 'es tuyo' (un mensaje) y deja de comandar; B comienza al recibirlo; si se pierde, nadie comanda hasta que A
         lo nota 300 s despues (hueco de autoridad).
  CONFIRMADO: A sigue comandando hasta recibir la confirmacion de B (GRANT -> ACK, con retransmision); B empieza al recibir
         GRANT; entre el inicio de B y la llegada de ACK a A hay solapamiento (los dos pueden comandar).
  CONFIRMADO + EPOCA: igual, pero cada orden lleva el numero de epoca de su emisor y el vehiculo rechaza ordenes de una
         epoca menor que la mayor vista (fencing); el solapamiento ya no produce ordenes en conflicto aceptadas.
Invariantes: no hay hueco de autoridad con el protocolo confirmado; con epoca, ordenes en conflicto aceptadas = 0.
Se supone 1 orden por operador cada 5 s mientras comanda. Solo biblioteca estandar.
"""
from __future__ import annotations
import platform, random

P_PERDIDA, RETX, N = 0.15, 10.0, 10000
T_DETECCION, ORDEN_CADA = 300.0, 5.0


def tiempo_entrega(rng):
    """Tiempo hasta que un mensaje con retransmision llega (cuenta de intentos geometrica)."""
    t = 0.0
    while rng.random() < P_PERDIDA:
        t += RETX
    return t


def naive(rng):
    perdido = rng.random() < P_PERDIDA
    return {"hueco": T_DETECCION if perdido else 0.0, "solape": 0.0, "conflictos": 0, "rechazadas": 0}


def confirmado(rng, epoca):
    t_grant = tiempo_entrega(rng)       # B empieza cuando GRANT llega
    t_ack = tiempo_entrega(rng)         # ACK vuelve a A tras empezar B
    solape = t_ack
    n_ord = int(solape // ORDEN_CADA)   # ordenes de A emitidas mientras B ya comanda
    return {"hueco": 0.0, "solape": solape, "conflictos": 0 if epoca else n_ord, "rechazadas": n_ord if epoca else 0}


def campana(f, rng):
    acc = {"hueco": 0.0, "solape": 0.0, "conflictos": 0, "rechazadas": 0, "con_hueco": 0, "con_solape": 0}
    for _ in range(N):
        r = f(rng)
        for k in ("hueco", "solape", "conflictos", "rechazadas"):
            acc[k] += r[k]
        acc["con_hueco"] += r["hueco"] > 0
        acc["con_solape"] += r["solape"] > 0
    return acc


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"DATOS SINTETICOS: p de perdida {P_PERDIDA}, retransmision cada {RETX:.0f} s, {N} relevos por protocolo, semilla 98008")
    rng = random.Random(98008)
    r1 = campana(naive, rng)
    r2 = campana(lambda g: confirmado(g, False), rng)
    r3 = campana(lambda g: confirmado(g, True), rng)
    print(f"{'protocolo':22s} {'relevos con hueco':>18s} {'hueco medio [s]':>16s} {'relevos con solape':>19s} {'ordenes en conflicto':>21s} {'rechazadas':>11s}")
    for nom, r in (("NAIVE", r1), ("CONFIRMADO", r2), ("CONFIRMADO + EPOCA", r3)):
        print(f"{nom:22s} {r['con_hueco']:18d} {r['hueco'] / N:16.2f} {r['con_solape']:19d} {r['conflictos']:21d} {r['rechazadas']:11d}")
    # Formula: P(hueco) = p; fraccion con solape = p (el primer ACK tarda 0 si no se pierde).
    print(f"Fraccion con hueco (NAIVE): {r1['con_hueco'] / N:.4f}; p = {P_PERDIDA}")
    assert abs(r1["con_hueco"] / N - P_PERDIDA) < 0.02
    assert r2["con_hueco"] == 0 and r3["con_hueco"] == 0
    assert r3["conflictos"] == 0 and r2["conflictos"] > 0
    esperado = P_PERDIDA * RETX / (1 - P_PERDIDA)  # esperanza del tiempo de entrega con retransmision
    print(f"Solape medio CONFIRMADO: {r2['solape'] / N:.3f} s; esperanza teorica por mensaje = {esperado:.3f} s")
    assert abs(r2["solape"] / N - esperado) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
