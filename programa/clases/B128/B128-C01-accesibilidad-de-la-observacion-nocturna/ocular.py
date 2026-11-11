#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C01: alcance del ocular segun la altitud del objeto y la postura.

TODO es ILUSTRATIVO (sintetico, no medido, no consultado): altura del pivote, largo del tubo, alturas de ojo y holguras.
Modelo geometrico: el ocular de un reflector tipo Newton queda a h = H + L*sin(alt) sobre el suelo (H pivote, L pivote-ocular,
alt altitud del objeto en grados). Se desprecia el desplazamiento lateral del ocular. Una persona alcanza el ocular si
ojo - bajo <= h <= ojo + alto (holguras ilustrativas; la postura se puede ajustar con banco o plataforma).
Unidades: metros y grados. Sistema de referencia: suelo horizontal, altitud medida desde el horizonte.
Segunda via: barrido numerico de la altitud cada 0.01 grados contra la solucion analitica. Tolerancia: 0.01 grados.
"""
from __future__ import annotations
import math, platform

L = 1.10                   # m, pivote-ocular (ilustrativo)
BAJO, ALTO = 0.25, 0.10    # m, holgura por debajo / por encima del ojo (ilustrativo)
OJOS = {"sentada (silla)": 1.15, "nino de pie": 1.30, "adulta de pie": 1.60}
MONTAJES = {"montura alta H=0.90": 0.90, "montura baja H=0.60": 0.60}
ALT_MIN, ALT_MAX = 15.0, 90.0   # altitudes observables en el sitio (ilustrativo)


def altura_ocular(h_piv: float, alt_deg: float) -> float:
    return h_piv + L * math.sin(math.radians(alt_deg))


def intervalo_analitico(h_piv: float, ojo: float):
    """Altitudes (grados) con ojo-BAJO <= h <= ojo+ALTO, recortadas a [ALT_MIN, ALT_MAX]."""
    s_lo = (ojo - BAJO - h_piv) / L
    s_hi = (ojo + ALTO - h_piv) / L
    lo = ALT_MIN if s_lo <= math.sin(math.radians(ALT_MIN)) else math.degrees(math.asin(min(s_lo, 1.0)))
    hi = ALT_MAX if s_hi >= 1.0 else math.degrees(math.asin(max(s_hi, -1.0)))
    lo, hi = max(lo, ALT_MIN), min(hi, ALT_MAX)
    return (lo, hi) if lo <= hi and s_lo <= 1.0 and s_hi >= math.sin(math.radians(ALT_MIN)) else None


def intervalo_barrido(h_piv: float, ojo: float):
    ok = [a / 100 for a in range(int(ALT_MIN * 100), int(ALT_MAX * 100) + 1)
          if ojo - BAJO <= altura_ocular(h_piv, a / 100) <= ojo + ALTO]
    return (ok[0], ok[-1]) if ok else None


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos ILUSTRATIVOS: L = {L} m; holgura -{BAJO}/+{ALTO} m; altitudes {ALT_MIN:.0f}-{ALT_MAX:.0f} grados")
    print("Altura del ocular [m] segun la altitud:")
    print(" alt   " + "  ".join(f"{n:>20s}" for n in MONTAJES))
    for alt in (15, 30, 45, 60, 90):
        print(f"{alt:4d}   " + "  ".join(f"{altura_ocular(h, alt):20.3f}" for h in MONTAJES.values()))
    print("Intervalo de altitudes alcanzable [grados] (analitico | barrido):")
    for mn, h in MONTAJES.items():
        for pn, ojo in OJOS.items():
            a, b = intervalo_analitico(h, ojo), intervalo_barrido(h, ojo)
            if a is None or b is None:
                assert a is None and b is None, (mn, pn, a, b)
                print(f"  {mn:22s} {pn:16s}: ninguna")
                continue
            assert abs(a[0] - b[0]) < 0.011 and abs(a[1] - b[1]) < 0.011, (mn, pn, a, b)
            print(f"  {mn:22s} {pn:16s}: {a[0]:5.1f} a {a[1]:5.1f}   |  {b[0]:5.1f} a {b[1]:5.1f}")
    # plan de noche SINTETICO: objetivo -> altitud a la hora de observacion
    objetivos = {"Luna": 28.0, "Jupiter": 52.0, "Pleyades": 70.0, "Orion M42": 38.0}
    print("Plan de noche SINTETICO (altitudes inventadas):")
    for pn, ojo in OJOS.items():
        for mn, h in MONTAJES.items():
            iv = intervalo_analitico(h, ojo)
            n = sum(1 for a in objetivos.values() if iv and iv[0] <= a <= iv[1])
            print(f"  {pn:16s} {mn:22s}: {n} de {len(objetivos)} objetivos alcanzables sin ajuste")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
