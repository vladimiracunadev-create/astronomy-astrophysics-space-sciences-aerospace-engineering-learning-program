#!/usr/bin/env python3
"""Planificador de misiones interplanetarias de primera aproximación (solo biblioteca estándar).

Para un destino (Venus, Marte, Júpiter…) calcula la transferencia de Hohmann desde la Tierra —duración, velocidad en el infinito de salida y de
llegada, C3, delta-v de salida desde una órbita baja y de captura— y busca las **ventanas de lanzamiento 2027–2050** con las posiciones oficiales
de JPL del repositorio (`simuladores/datos/sol.*`): las fechas en que el destino tiene el ángulo de adelanto que exige la transferencia.

Es una **primera aproximación** (órbitas circulares y coplanares; sin asistencias): para diseñar, use el simulador de trayectorias (Lambert, gráfico
porkchop) y valide con JPL Horizons. Resultados didácticos: no sirven para decisiones de vuelo.

Uso:
  planificador_de_misiones.py ventanas --destino marte [--desde 2027] [--hasta 2050]
  planificador_de_misiones.py hohmann --destino jupiter [--h-salida 300] [--h-captura 400]
  planificador_de_misiones.py resumen
"""
from __future__ import annotations

import argparse
import datetime as dt
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "efemerides"))
import lectura as L  # noqa: E402

MU_SOL = 132712440041.94           # km³/s²
UA = 149597870.7                   # km
DESTINOS = {  # id Horizons, nombre, GM [km³/s²], radio [km], semieje [UA]
    "venus": ("299", "Venus", 324858.59, 6051.8, 0.723332), "marte": ("499", "Marte", 42828.37, 3396.19, 1.523679),
    "jupiter": ("599", "Júpiter", 126686534.0, 71492.0, 5.2044), "saturno": ("699", "Saturno", 37931207.0, 60268.0, 9.5826),
    "urano": ("799", "Urano", 5793951.0, 25559.0, 19.2184), "neptuno": ("899", "Neptuno", 6835100.0, 24764.0, 30.1104),
    "mercurio": ("199", "Mercurio", 22031.86, 2439.4, 0.387098)}
GM_TIERRA, R_TIERRA = 398600.4418, 6378.137


def fecha(jd_tdb: float) -> str:
    return (dt.datetime(2000, 1, 1, 12) + dt.timedelta(days=jd_tdb - 2451545.0)).strftime("%Y-%m-%d")


def hohmann(destino: str, h_salida: float = 300.0, h_captura: float | None = None) -> dict:
    _, nombre, gm, R, a2 = DESTINOS[destino]
    r1, r2 = UA, a2 * UA
    at = (r1 + r2) / 2
    tof = math.pi * math.sqrt(at ** 3 / MU_SOL) / 86400
    v1, v2 = math.sqrt(MU_SOL / r1), math.sqrt(MU_SOL / r2)
    vinf_sal = abs(v1 * (math.sqrt(2 * r2 / (r1 + r2)) - 1))
    vinf_lle = abs(v2 * (1 - math.sqrt(2 * r1 / (r1 + r2))))
    rp = R_TIERRA + h_salida
    dv_salida = math.sqrt(vinf_sal ** 2 + 2 * GM_TIERRA / rp) - math.sqrt(GM_TIERRA / rp)       # desde órbita circular baja
    res = {"destino": nombre, "tof_dias": tof, "vinf_salida": vinf_sal, "c3": vinf_sal ** 2, "dv_salida_orbita_baja": dv_salida, "vinf_llegada": vinf_lle,
           "angulo_adelanto_deg": math.degrees(math.pi - 2 * math.pi * (tof / (2 * math.pi * math.sqrt(r2 ** 3 / MU_SOL) / 86400)))}
    if h_captura is not None:   # inserción en una órbita circular de captura (sobre el nivel de referencia); órbita casi parabólica = más barata
        rc = R + h_captura
        res["dv_captura_circular"] = math.sqrt(vinf_lle ** 2 + 2 * gm / rc) - math.sqrt(gm / rc)
    return res


def ventanas(destino: str, desde: int, hasta: int) -> list[tuple[float, float]]:
    """Fechas (TDB) en que el destino está en el ángulo de adelanto de Hohmann respecto de la Tierra; devuelve (jd, error_grados)."""
    pid, _, _, _, _ = DESTINOS[destino]
    sis = L.Sistema("sol")
    adel = hohmann(destino)["angulo_adelanto_deg"]
    jd0 = 2451545.0 + (dt.date(desde, 1, 1) - dt.date(2000, 1, 1, )).days - 0.5
    jd1 = 2451545.0 + (dt.date(hasta, 12, 31) - dt.date(2000, 1, 1)).days - 0.5

    def f(jd: float) -> float:
        e, p = sis.pos("399", jd), sis.pos(pid, jd)
        d = math.degrees(math.atan2(p[1], p[0]) - math.atan2(e[1], e[0]))
        return (d - adel + 180) % 360 - 180
    out, jd, ant = [], jd0, f(jd0)
    while jd < jd1:
        jd += 1.0
        v = f(jd)
        if (ant < 0 <= v or ant >= 0 > v) and abs(v - ant) < 90:      # el error de fase pasa por cero (sube para los planetas interiores, baja para los exteriores)
            lo, hi = jd - 1, jd
            for _ in range(40):
                m = (lo + hi) / 2
                if (f(m) < 0) == (ant < 0):
                    lo = m
                else:
                    hi = m
            out.append(((lo + hi) / 2, 0.0))
        ant = v
    return out


def autotest() -> int:
    """Comprueba contra valores de libro (Hohmann Tierra–Marte/Venus) y contra la ventana de Lambert de 2028 de los simuladores."""
    mal = []
    m = hohmann("marte"); v = hohmann("venus")
    for nombre, val, ref, tol in (("Marte: vuelo [d]", m["tof_dias"], 258.9, 1.0), ("Marte: v∞ de salida [km/s]", m["vinf_salida"], 2.94, 0.02), ("Venus: vuelo [d]", v["tof_dias"], 146.0, 1.0), ("Venus: v∞ de salida [km/s]", v["vinf_salida"], 2.50, 0.02)):
        if abs(val - ref) > tol:
            mal.append(f"{nombre}: {val:.3f} (esperado {ref} ± {tol})")
    wm = [fecha(j) for j, _ in ventanas("marte", 2027, 2031)]
    wv = [fecha(j) for j, _ in ventanas("venus", 2027, 2029)]
    if not any(abs((dt.date.fromisoformat(f) - dt.date(2028, 11, 29)).days) < 70 for f in wm):
        mal.append(f"ventana de Marte cerca del 2028-11-29 (óptimo de Lambert): {wm}")
    if not any(abs((dt.date.fromisoformat(f) - dt.date(2028, 3, 25)).days) < 40 for f in wv):
        mal.append(f"ventana de Venus cerca del 2028-03-25 (óptimo de Lambert): {wv}")
    for x in mal:
        print("ERROR", x)
    print("planificador_de_misiones: autotest", "FALLÓ" if mal else "correcto")
    return 1 if mal else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for n in ("ventanas", "hohmann"):
        p = sub.add_parser(n)
        p.add_argument("--destino", required=True, choices=sorted(DESTINOS))
        p.add_argument("--desde", type=int, default=2027)
        p.add_argument("--hasta", type=int, default=2050)
        p.add_argument("--h-salida", type=float, default=300.0, help="altura de la órbita baja de salida [km]")
        p.add_argument("--h-captura", type=float, default=None, help="altura de la órbita circular de captura [km]")
    sub.add_parser("resumen")
    sub.add_parser("autotest")
    a = ap.parse_args()
    if a.cmd == "autotest":
        return autotest()
    if a.cmd == "resumen":
        print(f"{'Destino':9} {'Vuelo [d]':>10} {'v∞ sal':>8} {'C3':>7} {'Δv sal':>8} {'v∞ lle':>8}   (km/s, km²/s²; Δv desde órbita de 300 km)")
        for d in ("venus", "marte", "jupiter", "saturno", "urano", "neptuno"):
            r = hohmann(d)
            print(f"{r['destino']:9} {r['tof_dias']:10.0f} {r['vinf_salida']:8.2f} {r['c3']:7.1f} {r['dv_salida_orbita_baja']:8.2f} {r['vinf_llegada']:8.2f}")
        print("\nHohmann circular y coplanar: primera aproximación. Para diseñar, use el simulador de trayectorias (Lambert).")
        return 0
    r = hohmann(a.destino, a.h_salida, a.h_captura)
    print(f"Hohmann Tierra → {r['destino']}: vuelo {r['tof_dias']:.0f} d ({r['tof_dias'] / 365.25:.2f} años); v∞ salida {r['vinf_salida']:.2f} km/s (C3 {r['c3']:.1f} km²/s²); "
          f"Δv desde órbita de {a.h_salida:.0f} km: {r['dv_salida_orbita_baja']:.2f} km/s; v∞ llegada {r['vinf_llegada']:.2f} km/s; ángulo de adelanto {r['angulo_adelanto_deg']:.1f}°"
          + (f"; Δv de captura circular a {a.h_captura:.0f} km: {r['dv_captura_circular']:.2f} km/s" if 'dv_captura_circular' in r else ""))
    if a.cmd == "ventanas":
        print(f"Ventanas de lanzamiento {a.desde}–{a.hasta} (fecha de salida; llegada = salida + {r['tof_dias']:.0f} d):")
        for jd, _ in ventanas(a.destino, a.desde, a.hasta):
            print(f"  salida {fecha(jd)} → llegada {fecha(jd + r['tof_dias'])}")
        print("Aproximación: el óptimo real (Lambert) puede diferir semanas; compruébelo en el simulador de trayectorias.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
