#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C20: analizar una bitácora de gnomon (datos SINTÉTICOS de ejemplo).

Datos SINTÉTICOS: gnomon de 1,000 ± 0,002 m y cinco sombras mínimas simuladas con ruido
gaussiano de 0,004 m alrededor del valor del modelo para el equinoccio a φ = −33,45°
(lugar HIPOTÉTICO). Modelo (C11): altura meridiana h = 90° − |φ − δ| con δ = 0 y
sombra L = g / tan h. Propagación (GUM 5.1.2, entradas independientes): h = arctan(g/L);
∂h/∂g = L/(g²+L²), ∂h/∂L = −g/(g²+L²). Supuestos: gnomon vertical, suelo horizontal, la
sombra mínima corresponde al mediodía solar, sin penumbra. Dominio de validez: alturas
solares entre ~10° y ~80°. Tolerancias: caso analítico g = L → 45° a 1e-12; incertidumbre
propagada frente a Monte Carlo independiente dentro del 3 %. Criterio de refutación (fijado
antes): se refuta el modelo si |h_medida − h_modelo| > 2·u_c(h).
"""

from __future__ import annotations

import math
import platform
import random
import statistics
import sys

PHI, DELTA = -33.45, 0.0
G, U_G = 1.000, 0.002


def altura_deg(g: float, l: float) -> float:
    return math.degrees(math.atan2(g, l))


def u_altura_deg(g: float, l: float, u_g: float, u_l: float) -> float:
    d = g**2 + l**2
    return math.degrees(math.hypot(l / d * u_g, g / d * u_l))


def pruebas() -> None:
    assert abs(altura_deg(1.0, 1.0) - 45.0) < 1e-12
    assert abs(u_altura_deg(1, 1, 0.01, 0.01) - math.degrees(math.sqrt(2) * 0.5 * 0.01)) < 1e-12
    rnd = random.Random(5)
    g0, l0, ug, ul = 1.0, 0.661, 0.002, 0.005
    hs = [altura_deg(rnd.gauss(g0, ug), rnd.gauss(l0, ul)) for _ in range(200_000)]
    ref = u_altura_deg(g0, l0, ug, ul)
    assert abs(statistics.pstdev(hs) - ref) / ref < 0.03, (statistics.pstdev(hs), ref)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    h_mod = 90.0 - abs(PHI - DELTA)
    l_mod = G / math.tan(math.radians(h_mod))
    rnd = random.Random(2026)
    sombras = [rnd.gauss(l_mod, 0.004) for _ in range(5)]
    m = sum(sombras) / 5
    s = math.sqrt(sum((x - m) ** 2 for x in sombras) / 4)
    u_l = s / math.sqrt(5)
    h = altura_deg(G, m)
    u_h = u_altura_deg(G, m, U_G, u_l)
    print(f"Modelo: h = {h_mod:.2f}° ; sombra esperada = {l_mod:.3f} m")
    print("Sombras (m): " + " ".join(f"{x:.3f}" for x in sombras))
    print(f"media = {m:.4f} m ; s = {s:.4f} m ; u(media) = {u_l:.4f} m")
    print(f"h medida = {h:.2f}° ± {u_h:.2f}° (u estándar) ; k = 2: ± {2 * u_h:.2f}°")
    dif = abs(h - h_mod)
    print(f"|h − h_modelo| = {dif:.2f}° ; 2·u = {2 * u_h:.2f}° -> " + ("compatible con el modelo" if dif <= 2 * u_h else "REFUTA el modelo"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
