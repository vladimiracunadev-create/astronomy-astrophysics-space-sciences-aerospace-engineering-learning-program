#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C06: percentiles de una poblacion mixta SINTETICA y dimensiones de diseno para un hábitat.

Datos consultados (2026-11-10; Burke, Howard y Kessler 2022): los volumenes funcionales se definen con antropometria del percentil 99 de hombres y mujeres, la altura estandar es 2.4 m
(sueno 1 m, esclusa 2.6 m) y la pista de traslado tiene 1.00 m de ancho. NASA/NSSDC Moon Fact Sheet: g = 1.62 m/s2.
SINTETICOS / ILUSTRATIVOS (no son datos de ninguna poblacion real; ANSUR II y la norma NASA-STD-3001 NO se consultaron): medias y desviaciones de estatura, anchura de hombros y alcance vertical
de hombres y mujeres, supuestos normales, mezcla 50 % / 50 %, holguras de 100 mm.
Modelo: percentil p de la mezcla por biseccion sobre F(x) = 0.5 F_h(x) + 0.5 F_m(x). Las dimensiones de holgura (cabeza, hombros) usan P99; las de alcance usan P1 (alcanza el 99 %).
Segunda via: percentiles empiricos de 200000 individuos simulados (semilla 109006) deben coincidir con los analiticos con una tolerancia de 5 mm; ademas P50 de la mezcla esta entre las medias.
Unidades: mm; masas no se usan.
"""
from __future__ import annotations
import platform, random
from statistics import NormalDist

DIMS = {  # nombre: (media_h, sd_h, media_m, sd_m) en mm, SINTETICOS
    "estatura": (1755.0, 70.0, 1630.0, 65.0),
    "anchura de hombros": (480.0, 25.0, 430.0, 22.0),
    "alcance vertical de pie": (2150.0, 90.0, 2000.0, 85.0),
}
ALTURA_ESTANDAR = 2400.0  # mm, Burke et al. 2022
PISTA = 1000.0  # mm


def cdf_mezcla(x, d):
    mh, sh, mm, sm = d
    return 0.5 * NormalDist(mh, sh).cdf(x) + 0.5 * NormalDist(mm, sm).cdf(x)


def percentil(p, d):
    lo, hi = d[2] - 6 * d[3], d[0] + 6 * d[1]
    for _ in range(200):
        mid = (lo + hi) / 2
        if cdf_mezcla(mid, d) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Poblacion SINTETICA normal (50 % hombres, 50 % mujeres); ANSUR II y NASA-STD-3001 no consultados; g lunar 1.62 m/s2 (NASA/NSSDC)")
    rng = random.Random(109006)
    N = 200000
    print(" dimension                      P1      P5     P50     P95     P99   [mm]")
    res = {}
    for nom, d in DIMS.items():
        ps = [percentil(p, d) for p in (0.01, 0.05, 0.50, 0.95, 0.99)]
        res[nom] = ps
        print(f"{nom:26s} " + " ".join(f"{x:7.1f}" for x in ps))
        muestra = sorted((rng.gauss(d[0], d[1]) if rng.random() < 0.5 else rng.gauss(d[2], d[3])) for _ in range(N))
        for p, ana in zip((0.01, 0.05, 0.50, 0.95, 0.99), ps):
            emp = muestra[int(p * N)]
            assert abs(emp - ana) < 5.0, (nom, p, emp, ana)
        assert d[2] < ps[2] < d[0]
    est = res["estatura"]
    hombros = res["anchura de hombros"]
    alc = res["alcance vertical de pie"]
    print("Dimensiones de diseno derivadas:")
    print(f"  Holgura sobre la cabeza con altura estandar 2400 mm y P99 de estatura = {ALTURA_ESTANDAR - est[4]:.0f} mm")
    print(f"  Largo de litera = P99 de estatura + 100 mm = {est[4] + 100:.0f} mm")
    print(f"  Ancho libre minimo por hombros P99 + 2 x 100 mm = {hombros[4] + 200:.0f} mm (pista de 1000 mm: margen {PISTA - hombros[4] - 200:.0f} mm)")
    print(f"  Altura maxima de un control que alcanza el 99 % de la poblacion = P1 del alcance vertical = {alc[0]:.0f} mm")
    # cobertura por tamano de diseno
    cov = cdf_mezcla(est[4] + 100, DIMS["estatura"])
    print(f"  Fraccion de la poblacion que cabe en una litera de {est[4] + 100:.0f} mm = {cov:.4f}")
    assert cov >= 0.99
    assert ALTURA_ESTANDAR > est[4]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
