#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B133-C02: retencion de un relato SINTETICO a traves de generaciones segun sus canales.

Todo es SINTETICO (inventado, no medido): el relato (12 elementos), las tasas de perdida q y de corrupcion e por canal y
generacion, el numero de canales k y los 25 años por generacion. Ningun numero describe ninguna tradicion oral real.
Modelo: cada elemento del relato lo sostienen k canales independientes (p. ej. relato, lugar, canto, practica). En cada
generacion cada canal conserva el elemento (prob 1-q-e), lo pierde (q) o lo corrompe (e, siempre la misma version erronea:
caso desfavorable). Regla de reparacion: gana la version con mas canales; si gana la correcta, todos los canales se
restauran; si gana la erronea o hay empate o no queda ninguno, el elemento se pierde (estado absorbente).
Retencion por generacion r = P(conservados > corruptos) (multinomial); tras G generaciones, r^G.
Segunda via: simulacion Monte Carlo con semilla fija; tolerancia 4 desviaciones estandar del binomio.
Verificacion adicional: con k = 1, r = 1 - q - e exactamente.
"""
from __future__ import annotations
import math, platform, random

Q, E = 0.15, 0.05          # SINTETICOS
ANIOS_GEN = 25             # SINTETICO
SEMILLA = 20261111


def retencion(k: int, q: float, e: float) -> float:
    """P(el elemento sobrevive correcto una generacion) con k canales."""
    p_keep = 1 - q - e
    total = 0.0
    for a in range(k + 1):              # a conservados
        for c in range(k - a + 1):      # c corruptos; k-a-c perdidos
            l = k - a - c
            if a > c:
                coef = math.factorial(k) / (math.factorial(a) * math.factorial(c) * math.factorial(l))
                total += coef * p_keep ** a * e ** c * q ** l
    return total


def simular(k: int, q: float, e: float, G: int, n: int, rng: random.Random) -> float:
    vivos = 0
    for _ in range(n):
        ok = True
        for _g in range(G):
            a = c = 0
            for _ in range(k):
                u = rng.random()
                if u < q:
                    pass
                elif u < q + e:
                    c += 1
                else:
                    a += 1
            if not a > c:
                ok = False
                break
        vivos += ok
    return vivos / n


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Relato SINTETICO; q = {Q}, e = {E} por canal y generacion; {ANIOS_GEN} años por generacion (sinteticos)")
    print(" k   r (1 gen)   G de retencion 50%   retencion a 10 gen   (analitica)")
    rs = {}
    for k in (1, 2, 3, 5):
        r = retencion(k, Q, E)
        rs[k] = r
        g50 = math.log(0.5) / math.log(r)
        print(f" {k}   {r:.6f}   {g50:10.2f}           {r ** 10:.6f}")
    assert abs(rs[1] - (1 - Q - E)) < 1e-12
    rng = random.Random(SEMILLA)
    print("Monte Carlo (n = 20000 elementos por celda; semilla 20261111): simulado frente a analitico")
    worst = 0.0
    for k in (1, 3):
        for G in (1, 5, 10):
            p = rs[k] ** G
            s = simular(k, Q, E, G, 20000, rng)
            sd = math.sqrt(p * (1 - p) / 20000)
            z = (s - p) / sd if sd > 0 else 0.0
            worst = max(worst, abs(z))
            print(f"  k={k} G={G:2d}  simulado {s:.4f}  analitico {p:.4f}  z = {z:+.2f}")
    print(f"|z| maximo = {worst:.2f} (tolerancia 4)")
    assert worst < 4
    # Identificabilidad: que combinaciones (k, q) dan la misma retencion por generacion, con e = 0
    G_total = 400   # 10 000 años a 25 años por generacion (ILUSTRATIVO)
    r_req = 0.5 ** (1 / G_total)
    print(f"Para conservar 50% tras {G_total} generaciones ({G_total * ANIOS_GEN} años, ILUSTRATIVO) hace falta r = {r_req:.6f} por generacion")
    print(" k   q de cada canal que da ese r (e = 0)")
    qs = {}
    for k in (1, 2, 3, 5):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if retencion(k, mid, 0.0) > r_req:
                lo = mid
            else:
                hi = mid
        qs[k] = lo
        print(f" {k}   {lo:.6f}")
    assert all(abs(retencion(k, qs[k], 0.0) - r_req) < 1e-9 for k in qs)
    assert qs[1] < qs[2] < qs[3] < qs[5]
    print("Combinaciones distintas (k, q) producen la misma retencion: la retencion sola no identifica el mecanismo ni la edad.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
