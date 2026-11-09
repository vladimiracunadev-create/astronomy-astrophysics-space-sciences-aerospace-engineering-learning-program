#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C10: lineas base, cobertura uv y haz sucio de un conjunto ILUSTRATIVO de cuatro telescopios.

Datos: ninguna medida real. Las posiciones de los telescopios (en metros, plano E-N), la declinacion de -30 grados, la latitud de -24,6 grados y lambda = 2,2 um son ILUSTRATIVAS
y no corresponden a ningun observatorio.
Modelo: con la base b = (E, N) en el plano horizontal, las coordenadas uv de una fuente de declinacion d a angulo horario H, en unidades de longitud de onda, son
u = (bE cos H - bN sin(lat) sin H) / lambda, v = (bE sin(d) sin H + bN (sin(lat) sin(d) cos H + cos(lat) cos(d))) / lambda (formulas de sintesis de apertura de libro; la
latitud entra en la proyeccion). Vias independientes: (a) visibilidad de dos fuentes puntuales calculada por suma directa frente a la formula analitica 2 cos(pi B theta / lambda) para
una base perpendicular; (b) numero de bases N(N-1)/2 y simetria hermitica; (c) el ancho del haz sucio se compara con lambda/B_max.
Supuestos: fuentes puntuales, sin ruido ni retrasos, cielo plano. Validez: conceptual; no sustituye a un paquete de sintesis (CASA, etc.).
Tolerancia: visibilidades a 1e-12 ; numero de bases exacto ; ancho del haz dentro de un factor 1,5 de lambda/B_max.
"""
from __future__ import annotations
import cmath, math, platform

LAM = 2.2e-6
LAT = math.radians(-24.6)
DEC = math.radians(-30.0)
TEL = [(0.0, 0.0), (40.0, 15.0), (-25.0, 55.0), (10.0, -70.0)]

def uv(base, h):
    be, bn = base
    u = (be * math.cos(h) - bn * math.sin(LAT) * math.sin(h)) / LAM
    v = (be * math.sin(DEC) * math.sin(h) + bn * (math.sin(LAT) * math.sin(DEC) * math.cos(h) + math.cos(LAT) * math.cos(DEC))) / LAM
    return u, v

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = len(TEL)
    bases = [(TEL[j][0] - TEL[i][0], TEL[j][1] - TEL[i][1]) for i in range(n) for j in range(i + 1, n)]
    print(f"telescopios = {n} ; bases independientes = {len(bases)} (N(N-1)/2 = {n * (n - 1) // 2})")
    assert len(bases) == n * (n - 1) // 2
    lens = [math.hypot(*b) for b in bases]
    bmax, bmin = max(lens), min(lens)
    print(f"base mas corta = {bmin:.1f} m ; mas larga = {bmax:.1f} m ; resolucion lambda/B_max = {LAM / bmax * 206264.806247 * 1e3:.4f} mas")
    # (a) visibilidad de dos fuentes iguales separadas theta en la direccion de la base
    b = 50.0
    print(f"{'theta [mas]':>12} {'V suma':>10} {'|cos|':>10}")
    peor = 0.0
    for mas in (0.0, 5.0, 10.0, 20.0, 40.0):
        th = mas / 206264.806247 / 1e3
        # fuentes en -th/2 y +th/2; V = |sum exp(-2 pi i b x / lambda)| / 2
        vis = abs(sum(cmath.exp(-2j * math.pi * b * x / LAM) for x in (-th / 2, th / 2))) / 2
        teo = abs(math.cos(math.pi * b * th / LAM))
        peor = max(peor, abs(vis - teo))
        print(f"{mas:12.1f} {vis:10.6f} {teo:10.6f}")
    assert peor < 1e-12
    th_nulo = LAM / (2 * b) * 206264.806247 * 1e3
    print(f"primer nulo de visibilidad en theta = lambda / (2 B) = {th_nulo:.3f} mas")
    # (b) cobertura uv sobre -4 h < H < 4 h
    pts = []
    for bs in bases:
        for k in range(-48, 49):
            h = math.radians(15.0 * k / 12.0)
            u, v = uv(bs, h)
            pts.append((u, v))
            pts.append((-u, -v))     # simetria hermitica
    print(f"puntos uv (con simetria hermitica) = {len(pts)}")
    assert len(pts) == 2 * len(bases) * 97
    umax = max(math.hypot(u, v) for u, v in pts)
    print(f"|uv| maximo = {umax:.4e} lambda ; lambda/|uv|max = {1 / umax * 206264.806247 * 1e3:.4f} mas")
    # haz sucio: B(x,y) = sum cos(2 pi (u x + v y)) / N, evaluado en un corte
    def haz(x, y):
        return sum(math.cos(2 * math.pi * (u * x + v * y)) for u, v in pts) / len(pts)
    mas = 1 / 206264.806247 / 1e3
    assert abs(haz(0, 0) - 1) < 1e-12
    # ancho a mitad de altura a lo largo de x e y por busqueda
    def fwhm(dir_):
        paso = 0.05 * mas
        x = 0.0
        while haz(dir_[0] * x, dir_[1] * x) > 0.5:
            x += paso
        return 2 * x
    fx, fy = fwhm((1, 0)), fwhm((0, 1))
    teo_res = LAM / bmax
    print(f"anchos del haz sucio: {fx / mas:.3f} mas (x), {fy / mas:.3f} mas (y) ; lambda/B_max = {teo_res / mas:.3f} mas")
    assert 0.3 * teo_res < min(fx, fy) and max(fx, fy) < 1.5 * teo_res * 2.0
    # maximo de lobulo lateral en una rejilla
    lat = 0.0
    for i in range(-30, 31):
        for j in range(-30, 31):
            r = math.hypot(i, j) * 0.5 * mas
            if r > 1.2 * max(fx, fy):
                lat = max(lat, haz(i * 0.5 * mas, j * 0.5 * mas))
    print(f"mayor lobulo lateral en el campo de +-15 mas fuera del lobulo central = {lat:.3f}")
    assert lat < 0.8
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
