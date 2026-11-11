#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C10: tiempo de carga de una pagina educativa con distinta conectividad y presupuesto de peso.

Consultado (2026-11-11): web.dev, «What are Progressive Web Apps?»: las aplicaciones deben seguir funcionando con redes lentas o sin red,
mantener disponible el contenido visto recientemente y avisar de los fallos en vez de fallar en silencio. NO da cifras de ancho de banda.
ILUSTRATIVOS (inventados, NO medidos ni consultados): los tres perfiles de red, el tamano de las paginas y el numero de peticiones.
Modelo: t = 8*bytes/ancho_de_banda + RTT * ceil(peticiones / 6)  (6 conexiones paralelas, aproximacion didactica; ignora arranque lento de TCP, TLS y CPU).
Unidades: bytes, bit/s, segundos. Segunda via: simulacion explicita por rondas de 6 peticiones con el ancho de banda repartido.
Tolerancia: 1e-9 s. Limite: es un modelo de orden de magnitud, no una prediccion; medir con la red real del grupo.
"""
from __future__ import annotations
import math, platform

PERFILES = {"movil-lento (50 kbit/s, RTT 600 ms)": (50e3, 0.600), "movil-medio (750 kbit/s, RTT 200 ms)": (750e3, 0.200),
            "fija (20 Mbit/s, RTT 30 ms)": (20e6, 0.030)}
PAGINAS = {"original (imagenes pesadas)": (3_500_000, 42), "optimizada (sin recursos externos)": (350_000, 8),
           "version texto (solo HTML + tabla)": (40_000, 2)}
PRESUPUESTO_S = 10.0   # criterio del curso: la pagina util en <= 10 s en el perfil lento (ILUSTRATIVO)


def t_formula(b, n, bw, rtt):
    return 8.0 * b / bw + rtt * math.ceil(n / 6)


def t_rondas(b, n, bw, rtt):
    por_peticion = b / n
    t, rest = 0.0, n
    while rest > 0:
        k = min(6, rest)
        t += rtt + 8.0 * (por_peticion * k) / bw   # la ronda transfiere k peticiones sobre el mismo enlace
        rest -= k
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Perfiles y paginas ILUSTRATIVOS (inventados). Modelo de orden de magnitud.")
    print(f"{'pagina':36s}" + "".join(f"{p.split(' ')[0]:>14s}" for p in PERFILES))
    for pn, (b, n) in PAGINAS.items():
        fila = []
        for bw, rtt in PERFILES.values():
            a, c = t_formula(b, n, bw, rtt), t_rondas(b, n, bw, rtt)
            assert abs(a - c) < 1e-9, (pn, a, c)
            fila.append(a)
        print(f"{pn:36s}" + "".join(f"{x:13.1f}s" for x in fila))
    bw, rtt = list(PERFILES.values())[0]
    print(f"Presupuesto del curso: <= {PRESUPUESTO_S:.0f} s en el perfil lento")
    for pn, (b, n) in PAGINAS.items():
        t = t_formula(b, n, bw, rtt)
        print(f"  {pn:36s} {t:7.1f} s  {'cumple' if t <= PRESUPUESTO_S else 'NO cumple'}")
    # peso maximo que cabe en el presupuesto con 8 peticiones
    n = 8
    bmax = (PRESUPUESTO_S - rtt * math.ceil(n / 6)) * bw / 8.0
    print(f"Peso maximo con {n} peticiones en el perfil lento: {bmax/1000:.1f} kB")
    assert abs(t_formula(bmax, n, bw, rtt) - PRESUPUESTO_S) < 1e-9
    # segunda visita con cache (SINTETICO): solo se descarga lo que cambio
    b, n = PAGINAS["optimizada (sin recursos externos)"]
    cambia = 0.10
    t2 = t_formula(b * cambia, 1, bw, rtt)
    print(f"Segunda visita con cache, cambia {cambia*100:.0f} % del peso en 1 peticion: {t2:.1f} s (frente a {t_formula(b, n, bw, rtt):.1f} s)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
