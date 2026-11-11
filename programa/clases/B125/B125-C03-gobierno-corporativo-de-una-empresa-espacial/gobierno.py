#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C03: votos por clase de accion y poder de voto de un consejo (modelo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, societaria, financiera ni de inversion.
Datos consultados (2026-11-11): en el Formulario 10-K de Planet Labs PBC (SEC, ejercicio cerrado el 2026-01-31) se lee que la empresa es una
sociedad de beneficio publico de Delaware, que las acciones Clase B tienen 20 votos y las Clase A un voto, y que los dos fundadores tienen todas
las Clase B y cerca del 62 % del poder de voto total. SOLO esa relacion 20:1 y el 62 % se usan, como caso de contraste; NO se conoce el numero de
acciones ni la participacion economica real (no consultados). Los principios G20/OCDE de gobierno corporativo (2023) se conocen por un resumen
de busqueda; su texto NO se leyo.
ILUSTRATIVOS (sinteticos): consejo de 7 miembros con pesos de voto 3, 2, 1, 1, 1, 1, 1 y cuota de mayoria simple (mas de la mitad del peso total);
empresa sintetica con 1 000 000 acciones de las cuales una fraccion b es Clase B.
Unidades: fracciones (0-1) y numero de votos. Tolerancias: poder de voto por formula frente a enumeracion < 1e-12;
la suma de los indices de Banzhaf normalizados vale 1 (1e-12).
"""
from __future__ import annotations
import itertools, platform


def poder_voto(b, k):
    """Fraccion del poder de voto total de la Clase B si es una fraccion b de las acciones y cada B vale k votos."""
    return k * b / (k * b + (1.0 - b))


def participacion_minima(v, k):
    """Fraccion de acciones (todas B) para alcanzar la fraccion v del poder de voto: b = v / (k (1 - v) + v)."""
    return v / (k * (1.0 - v) + v)


def banzhaf(pesos, cuota):
    n = len(pesos)
    cuenta = [0] * n
    for mascara in range(1 << n):
        peso = sum(pesos[i] for i in range(n) if mascara >> i & 1)
        if peso >= cuota:
            for i in range(n):
                if mascara >> i & 1 and peso - pesos[i] < cuota:
                    cuenta[i] += 1
    total = sum(cuenta)
    return [c / total for c in cuenta]


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Estructura SINTETICA; solo la relacion 20:1 y el 62 % de voto vienen de un informe consultado (como contraste).")
    k = 20
    print("Fraccion b de acciones Clase B   poder de voto de la Clase B (k = 20)")
    for b in (0.01, 0.0476, 0.075, 0.10, 0.25):
        print(f"{b:30.4f}   {poder_voto(b, k):.4f}")
    b50 = participacion_minima(0.5, k)
    b62 = participacion_minima(0.62, k)
    assert abs(poder_voto(b50, k) - 0.5) < 1e-12 and abs(poder_voto(b62, k) - 0.62) < 1e-12
    print(f"Participacion minima para 50 % del voto con k = 20: {b50:.4f} ({b50*100:.2f} % de las acciones)")
    print(f"Participacion que daria 62 % del voto si TODAS sus acciones fueran B con k = 20: {b62:.4f} ({b62*100:.2f} % de las acciones; ilustrativo)")
    # Comprobacion por enumeracion con 1 000 000 acciones
    N = 1_000_000
    B = round(b62 * N)
    votos_B, votos_A = B * k, (N - B) * 1
    enum = votos_B / (votos_B + votos_A)
    assert abs(enum - 0.62) < 1e-5
    print(f"Enumeracion con {N} acciones: B = {B}, voto B = {enum:.6f}")
    print("k (votos por B)   participacion minima para 50 % del voto")
    for kk in (1, 2, 10, 20, 100):
        print(f"{kk:15d}   {participacion_minima(0.5, kk):.4f}")
    # Poder de voto de un consejo con pesos
    pesos = [3, 2, 1, 1, 1, 1, 1]
    cuota = sum(pesos) // 2 + 1
    bz = banzhaf(pesos, cuota)
    assert abs(sum(bz) - 1.0) < 1e-12
    print(f"Consejo sintetico pesos {pesos}, cuota {cuota} de {sum(pesos)}")
    print("miembro  peso  indice de Banzhaf  peso relativo")
    for i, (p, v) in enumerate(zip(pesos, bz)):
        print(f"{i+1:7d}  {p:4d}  {v:17.4f}  {p/sum(pesos):13.4f}")
    # Un peso dominante: la regla de mayoria convierte a un miembro en dictador aunque no tenga todos los votos
    d = banzhaf([4, 1, 1, 1], 4)
    print(f"Consejo [4, 1, 1, 1] con cuota 4: Banzhaf = {[round(x, 3) for x in d]} (el miembro de peso 4 decide solo)")
    assert d[0] == 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
