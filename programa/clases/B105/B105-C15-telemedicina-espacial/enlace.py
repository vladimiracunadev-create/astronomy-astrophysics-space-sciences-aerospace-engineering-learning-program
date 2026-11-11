#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C15: retardo de luz y presupuesto de latencia de una consulta medica remota (calculo; datos de enlace SINTETICOS).

Constantes: c = 299 792.458 km/s (valor exacto del SI); 1 UA = 149 597 870.7 km (valor exacto de la IAU). Distancia Tierra-Luna media 384 400 km (valor de
referencia de orden de magnitud, NO consultado aqui). Marte: orbitas circulares coplanares de 1 UA y 1.524 UA (modelo didactico) con periodo sinodico
de 779.9 dias; da distancias de 0.524 a 2.524 UA. Presupuesto de una consulta: tiempo = n_turnos x RTT + volumen/ancho de banda + procesamiento. El ancho de banda,
el tamano de las imagenes y el numero de turnos son SINTETICOS/ILUSTRATIVOS. Se compara con el umbral de conversacion de 'tiempo real' de 1 s de ida y vuelta (ilustrativo).
Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

C = 299792.458
UA = 149597870.7
SIN = 779.9


def retardo_s(d_km):
    return d_km / C


def dist_marte(t_dias):
    th = 2 * np.pi * t_dias / SIN
    return UA * np.sqrt(1.0 + 1.524 ** 2 - 2 * 1.524 * np.cos(th))


def consulta(n_turnos, rtt, mbytes, mbps, proc=60.0):
    return n_turnos * rtt + mbytes * 8 / mbps + proc


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: c y 1 UA exactos; distancia a la Luna de orden de magnitud no consultada; enlace y consulta SINTETICOS/ILUSTRATIVOS")
    destinos = {"Luna (384 400 km)": 384400.0, "Marte (distancia minima, 0.524 UA)": 0.524 * UA, "Marte (distancia maxima, 2.524 UA)": 2.524 * UA}
    print("destino                                   ida [s]   ida y vuelta [s]")
    for nombre, d in destinos.items():
        t = retardo_s(d)
        print(f"  {nombre:40s} {t:8.2f}   {2 * t:9.2f}   ({2 * t / 60:6.2f} min ida y vuelta)")
    t = np.linspace(0, SIN, 78001)
    d = dist_marte(t)
    print(f"Ciclo sinodico (modelo circular): distancia entre {d.min() / UA:.3f} y {d.max() / UA:.3f} UA; retardo de ida {retardo_s(d.min()) / 60:.2f} a {retardo_s(d.max()) / 60:.2f} min; media {retardo_s(d.mean()) / 60:.2f} min")
    frac = np.mean(2 * retardo_s(d) > 20 * 60)
    print(f"Fraccion del ciclo con ida y vuelta mayor que 20 min = {frac:.3f}; mayor que 1 s = {np.mean(2 * retardo_s(d) > 1.0):.3f}")
    print("Presupuesto de una consulta (6 turnos de pregunta-respuesta, 5 MB de imagenes, 1 Mbps, 60 s de proceso):")
    resumen = {}
    for nombre, dd in destinos.items():
        rtt = 2 * retardo_s(dd)
        tc = consulta(6, rtt, 5.0, 1.0)
        resumen[nombre] = tc
        print(f"  {nombre:40s} tiempo total = {tc:9.1f} s = {tc / 60:7.1f} min")
    # modo almacenar y reenviar: un solo turno con toda la informacion
    rtt_max = 2 * retardo_s(2.524 * UA)
    sf = consulta(1, rtt_max, 5.0, 1.0)
    print(f"Almacenar y reenviar (1 turno, todo el paquete) con retardo maximo: {sf / 60:.1f} min frente a {consulta(6, rtt_max, 5.0, 1.0) / 60:.1f} min con 6 turnos")
    assert abs(retardo_s(384400.0) - 1.282) < 0.001
    assert abs(retardo_s(0.524 * UA) / 60 - 4.36) < 0.02
    assert abs(retardo_s(2.524 * UA) / 60 - 21.0) < 0.1
    assert abs(d.min() / UA - 0.524) < 1e-3 and abs(d.max() / UA - 2.524) < 1e-3
    assert sf < consulta(6, rtt_max, 5.0, 1.0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
