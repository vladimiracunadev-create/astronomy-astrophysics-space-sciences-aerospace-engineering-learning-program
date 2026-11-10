#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C23: diseno de orbita y revisita: orbita heliosincrona, trazas repetidas y espaciado entre trazas.

Datos: Sentinel-1: altitud 693 km, inclinacion 98.18 grados, periodo 98.6 min, ciclo de 175 orbitas en 12 dias, modo IW de 250 km (SentiWiki, consultada 2026-11-09).
Landsat 8: 705 km, barrido 185 km, ciclo de 16 dias (USGS, consultada 2026-11-09). Constantes de referencia NO CONSULTADAS: GM = 3.986004418e14 m^3 s^-2,
R_e = 6378.137 km, J2 = 1.08262668e-3, dia sideral aproximado y anio tropico 365.2422 dias, rotacion terrestre 7.2921159e-5 rad/s.
Modelo: orbita circular; precesion nodal secular dOmega/dt = -1.5 J2 n (R_e/a)^2 cos i ; condicion heliosincrona dOmega/dt = 2 pi/(365.2422 d) ;
periodo nodal con correcciones seculares de J2; condicion de traza repetida N T_nodal = D T_dia_nodal ; espaciado de trazas en el ecuador = 2 pi R_e / N.
Validez: orbita circular, solo J2 secular, Tierra esferica para el espaciado. Tolerancia: inclinacion heliosincrona frente a 98.18 grados < 0.05 grados;
periodo frente a 98.6 min < 0.1 min; altitud de la traza repetida 175/12 frente a 693 km < 5 km.
"""
import math, platform

GM, RE, J2 = 3.986004418e14, 6378137.0, 1.08262668e-3
WE = 7.2921159e-5
OM_SOL = 2 * math.pi / (365.2422 * 86400)


def inclinacion_ss(alt):
    a = RE + alt
    n = math.sqrt(GM / a**3)
    c = -OM_SOL / (1.5 * J2 * n * (RE / a) ** 2)
    return math.degrees(math.acos(c))


def periodo_kepler(alt):
    return 2 * math.pi * math.sqrt((RE + alt) ** 3 / GM)


def periodo_nodal(alt, inc):
    a = RE + alt
    n = math.sqrt(GM / a**3)
    f = (RE / a) ** 2
    s2 = math.sin(inc) ** 2
    nbar = n * (1 + 1.5 * J2 * f * (1 - 1.5 * s2))
    wdot = 0.75 * n * J2 * f * (5 * math.cos(inc) ** 2 - 1) * -1 * -1
    # el argumento del perigeo (circular) y la anomalia media suman: usamos n_bar + wdot
    return 2 * math.pi / (nbar + wdot)


def alt_repeticion(N, D):
    lo, hi = 400e3, 1000e3
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        inc = math.radians(inclinacion_ss(mid))
        T = periodo_nodal(mid, inc)
        dia_nodal = 2 * math.pi / (WE - OM_SOL)
        if N * T > D * dia_nodal:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def calcular():
    r = {}
    r["inc_693"] = inclinacion_ss(693e3)
    r["inc_705"] = inclinacion_ss(705e3)
    r["T_693"] = periodo_kepler(693e3) / 60
    r["alt_175_12"] = alt_repeticion(175, 12) / 1e3
    r["espaciado_175"] = 2 * math.pi * RE / 175 / 1e3
    r["alt_233_16"] = alt_repeticion(233, 16) / 1e3
    r["espaciado_233"] = 2 * math.pi * RE / 233 / 1e3
    r["cubre_iw"] = r["espaciado_175"] < 250
    r["cubre_l8"] = r["espaciado_233"] < 185
    r["T_nod_693"] = periodo_nodal(693e3, math.radians(r["inc_693"])) / 60
    r["dia_nodal_h"] = 2 * math.pi / (WE - OM_SOL) / 3600
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Heliosincrona a 693 km: inclinacion = {r['inc_693']:.3f} grados (publicada: 98.18) ; periodo kepleriano = {r['T_693']:.2f} min (publicado: 98.6)")
    print(f"Heliosincrona a 705 km: inclinacion = {r['inc_705']:.3f} grados")
    print(f"Periodo nodal a 693 km = {r['T_nod_693']:.3f} min ; dia nodal relativo = {r['dia_nodal_h']:.4f} h")
    print(f"Traza repetida 175 orbitas / 12 dias: altitud = {r['alt_175_12']:.1f} km (publicada: 693) ; espaciado en el ecuador = {r['espaciado_175']:.1f} km (barrido IW 250 km: cubre = {r['cubre_iw']})")
    print(f"Traza repetida 233 orbitas / 16 dias (hipotesis, no consultada): altitud = {r['alt_233_16']:.1f} km ; espaciado = {r['espaciado_233']:.1f} km (barrido 185 km: cubre = {r['cubre_l8']})")
    assert abs(r["inc_693"] - 98.18) < 0.05
    assert abs(r["T_693"] - 98.6) < 0.1
    assert abs(r["alt_175_12"] - 693.0) < 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
