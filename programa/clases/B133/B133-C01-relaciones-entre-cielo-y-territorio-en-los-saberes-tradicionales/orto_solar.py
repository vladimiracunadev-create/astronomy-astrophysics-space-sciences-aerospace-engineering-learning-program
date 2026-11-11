#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B133-C01: acimut de salida del sol, horizonte local y marcador de rayo en una pared.

Dato consultado (2026-11-11): Fu (2016), Boletin del Museo Chileno de Arte Precolombino 21(2): la comunidad de
Trapa Trapa esta en 37 deg 41' S, 71 deg 18' W; el autor describe el orto solar entre ~60 deg (solsticio de junio)
y ~120 deg (solsticio de diciembre) y un agujero en una pared oriental con un rayo que cae a ~5 m. Aqui solo se usan
la LATITUD y la LONGITUD DE 5 m como valores de ejemplo; este script NO reproduce ni mide ninguna practica de esa comunidad.
SINTETICO (inventado, no medido): elevaciones del horizonte (0, 3 y 8 deg), geometria de la pared y umbral de 2.9 mm
(el error medio que Fu informa para su propio experimento de marcado, usado aqui solo como orden de magnitud).
Modelo: declinacion solar con longitud eclíptica uniforme (aprox.; error < 0.1 deg cerca de los solsticios, hasta ~0.7 deg
en los equinoccios del hemisferio sur, ~1.3 deg el 23-09); acimut medido desde el norte hacia el este; el centro del sol esta a h = e - 0.833 deg sobre el horizonte
geometrico cuando su borde superior toca un horizonte de elevacion e (radio 0.267 deg + refraccion 0.566 deg).
Segunda via: se resuelve numericamente el angulo horario con biseccion y se compara con la forma cerrada.
Tolerancias: forma cerrada frente a numerica < 1e-6 deg; simetria de solsticios < 1e-9 deg.
"""
from __future__ import annotations
import math, platform, datetime

PHI = -(37 + 41 / 60)          # latitud [deg], Fu (2016), consultada
D_PARED = 5.0                  # [m], longitud de ejemplo (Fu 2016 menciona ~5 m); aqui sintetica
UMBRAL_M = 0.0029              # [m], orden de magnitud tomado de Fu (2016); aqui sintetico
EPS = 23.44                    # oblicuidad [deg] (valor convencional redondeado)
RAD = math.pi / 180


def decl(n: float) -> float:
    """Declinacion [deg] del dia del año n (1 = 1 de enero)."""
    lam = 2 * math.pi * (n - 80) / 365.25
    return math.degrees(math.asin(math.sin(EPS * RAD) * math.sin(lam)))


def acimut_cerrado(phi: float, d: float, h: float) -> float:
    c = (math.sin(d * RAD) - math.sin(phi * RAD) * math.sin(h * RAD)) / (math.cos(phi * RAD) * math.cos(h * RAD))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def acimut_numerico(phi: float, d: float, h: float) -> float:
    """Biseccion sobre el angulo horario H (-pi..0, mañana) hasta que la altura valga h; acimut por vectores."""
    def alt(H):
        return math.asin(math.sin(phi * RAD) * math.sin(d * RAD) + math.cos(phi * RAD) * math.cos(d * RAD) * math.cos(H))
    lo, hi = -math.pi, 0.0       # alt(-pi) mínima, alt(0) maxima (culminacion)
    for _ in range(200):
        mid = (lo + hi) / 2
        if alt(mid) < h * RAD:
            lo = mid
        else:
            hi = mid
    H = (lo + hi) / 2
    # vector unitario del sol en (este, norte, cenit)
    e = -math.cos(d * RAD) * math.sin(H)
    nrt = math.sin(d * RAD) * math.cos(phi * RAD) - math.cos(d * RAD) * math.sin(phi * RAD) * math.cos(H)
    return math.degrees(math.atan2(e, nrt)) % 360


def fecha(n: int) -> str:
    return (datetime.date(2027, 1, 1) + datetime.timedelta(days=n - 1)).strftime("%d-%m")


def x_rayo(A: float) -> float:
    """Desplazamiento lateral [m] (sur positivo) del rayo en la pared opuesta, a D_PARED del agujero."""
    return D_PARED * math.tan((90.0 - A) * RAD)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Latitud {PHI:.4f} deg (Fu 2016); pared a {D_PARED} m (ejemplo SINTETICO)")
    print("Horizonte e [deg]: 0, 3, 8 (SINTETICOS); h_centro = e - 0.833")
    print("Acimut de salida [deg desde el norte hacia el este]")
    print(" fecha   dia  decl[deg]   e=0       e=3       e=8")
    for n in (80, 172, 266, 355):
        d = decl(n)
        fila = [acimut_cerrado(PHI, d, e - 0.833) for e in (0, 3, 8)]
        print(f" {fecha(n)}  {n:4d}  {d:8.3f}  {fila[0]:8.3f}  {fila[1]:8.3f}  {fila[2]:8.3f}")
    # Segunda via
    peor = 0.0
    for n in range(1, 366, 7):
        for e in (0, 3, 8):
            d = decl(n)
            peor = max(peor, abs(acimut_cerrado(PHI, d, e - 0.833) - acimut_numerico(PHI, d, e - 0.833)))
    print(f"Diferencia maxima forma cerrada vs biseccion = {peor:.2e} deg")
    # Simetria de solsticios y equinoccio
    s1 = acimut_cerrado(PHI, EPS, 0.0)
    s2 = acimut_cerrado(PHI, -EPS, 0.0)
    print(f"Solsticios con horizonte matematico (h = 0): {s1:.4f} y {s2:.4f} deg; suma = {s1 + s2:.9f} (esperada 180)")
    r1 = acimut_cerrado(PHI, EPS, -0.833)
    r2 = acimut_cerrado(PHI, -EPS, -0.833)
    print(f"Con h = -0.833 la simetria se rompe: suma = {r1 + r2:.4f} deg (el sol sale algo mas al sur en ambos casos)")
    eq = max(abs(acimut_cerrado(p, 0.0, 0.0) - 90.0) for p in (-60, -37.68, 0, 37.68, 60))
    print(f"Equinoccio con h = 0: desviacion maxima respecto de 90 deg = {eq:.2e}")
    # Desplazamiento diario del rayo alrededor del solsticio de junio (n = 172)
    print("Rayo en la pared (e = 0): desplazamiento diario alrededor del solsticio de junio, en mm")
    sin_resolver = []
    for n in range(160, 185):
        dx = x_rayo(acimut_cerrado(PHI, decl(n + 1), -0.833)) - x_rayo(acimut_cerrado(PHI, decl(n), -0.833))
        if abs(dx) < UMBRAL_M:
            sin_resolver.append(n)
        if 166 <= n <= 178:
            print(f"  {fecha(n)}->{fecha(n + 1)}  {dx * 1000:8.3f} mm")
    print(f"Dias con |desplazamiento diario| < {UMBRAL_M * 1000:.1f} mm: {fecha(sin_resolver[0])} a {fecha(sin_resolver[-1])} ({len(sin_resolver)} dias)")
    # Efecto del horizonte sobre el acimut de solsticio
    d_e = [acimut_cerrado(PHI, EPS, e - 0.833) for e in (0, 3, 8)]
    print(f"Acimut del solsticio de junio con e = 0, 3, 8 deg: {d_e[0]:.3f}, {d_e[1]:.3f}, {d_e[2]:.3f}")
    assert peor < 1e-6 and abs(s1 + s2 - 180) < 1e-9 and eq < 1e-9 and r1 + r2 > 180
    assert d_e[0] > d_e[1] > d_e[2] and d_e[0] < 90 and len(sin_resolver) >= 3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
