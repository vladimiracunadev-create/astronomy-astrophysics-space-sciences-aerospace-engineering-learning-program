#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C17. Constelaciones y cobertura: constelacion Walker delta i:T/P/F, fraccion de cobertura y satelites visibles por banda de latitud.
Parametros SINTETICOS; mu y radio terrestre ILUSTRATIVOS (no consultados). Verificacion: media global de visibles = T (1 - cos lambda)/2."""
import math, sys

MU = 398600.4418   # km3/s2 ILUSTRATIVO
RE = 6371.0        # km ILUSTRATIVO

def walker(inc_deg, T, P, F, alt):
    a = RE + alt
    n = math.sqrt(MU / a ** 3)
    S = T // P
    sats = []
    for p in range(P):
        raan = 2 * math.pi * p / P
        for s in range(S):
            u0 = 2 * math.pi * s / S + 2 * math.pi * F * p / T
            sats.append((raan, u0))
    return a, n, sats

def posiciones(a, n, sats, inc_deg, t):
    i = math.radians(inc_deg)
    out = []
    for raan, u0 in sats:
        u = u0 + n * t
        x, y = a * math.cos(u), a * math.sin(u) * math.cos(i)
        z = a * math.sin(u) * math.sin(i)
        out.append((x * math.cos(raan) - y * math.sin(raan), x * math.sin(raan) + y * math.cos(raan), z))
    return out

def semi_angulo(alt, el_deg):
    el = math.radians(el_deg)
    return math.acos(RE * math.cos(el) / (RE + alt)) - el

def cobertura(inc, T, P, F, alt, mascara=10.0, paso=120.0):
    a, n, sats = walker(inc, T, P, F, alt)
    per = 2 * math.pi / n
    pasos = int(per // paso)
    lam = semi_angulo(alt, mascara)
    cos_lam = math.cos(lam)
    lats = [-82.5 + 15 * k for k in range(12)]
    lons = [7.5 + 15 * k for k in range(24)]
    puntos = []
    for la in lats:
        for lo in lons:
            lr, lor = math.radians(la), math.radians(lo)
            puntos.append((la, (math.cos(lr) * math.cos(lor), math.cos(lr) * math.sin(lor), math.sin(lr))))
    acum = {}
    for k in range(pasos):
        pos = posiciones(a, n, sats, inc, k * paso)
        unit = [(x / a, y / a, z / a) for x, y, z in pos]
        for la, u in puntos:
            vis = sum(1 for s in unit if u[0] * s[0] + u[1] * s[1] + u[2] * s[2] >= cos_lam)
            d = acum.setdefault(la, [0, 0, 0, 0])
            d[0] += 1
            d[1] += vis
            d[2] += vis >= 1
            d[3] += vis >= 4
    return lats, acum, lam

def calcular():
    R = {}
    inc, T, P, F, alt = 55.0, 24, 6, 1, 1200.0
    lats, acum, lam = cobertura(inc, T, P, F, alt)
    R["lam_deg"] = math.degrees(lam)
    peso = {la: math.cos(math.radians(la)) for la in lats}
    sw = sum(peso.values())
    R["bandas"] = {la: (d[1] / d[0], d[2] / d[0], d[3] / d[0]) for la, d in acum.items()}
    R["media_vis"] = sum(peso[la] * R["bandas"][la][0] for la in lats) / sw
    R["cob1"] = sum(peso[la] * R["bandas"][la][1] for la in lats) / sw
    R["cob4"] = sum(peso[la] * R["bandas"][la][2] for la in lats) / sw
    R["teo_media"] = T * (1 - math.cos(lam)) / 2
    R["rel"] = abs(R["media_vis"] - R["teo_media"]) / R["teo_media"]
    R["T"], R["alt"] = T, alt
    # constelacion menor
    lats2, acum2, lam2 = cobertura(inc, 12, 3, 1, alt)
    R["cob1_12"] = sum(peso[la] * acum2[la][2] / acum2[la][0] for la in lats) / sw
    R["media_12"] = sum(peso[la] * acum2[la][1] / acum2[la][0] for la in lats) / sw
    R["teo_12"] = 12 * (1 - math.cos(lam2)) / 2
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print(f"SINTETICO: Walker delta 55: 24/6/1, altitud {R['alt']:.0f} km, mascara 10 grados ; semi-angulo de huella = {R['lam_deg']:.2f} grados")
    print(f"{'lat [deg]':>10s}{'visibles (media)':>18s}{'cob >= 1':>10s}{'cob >= 4':>10s}")
    for la, (m, c1, c4) in R["bandas"].items():
        print(f"{la:10.1f}{m:18.2f}{c1:10.3f}{c4:10.3f}")
    print(f"Global ponderado por area: visibles = {R['media_vis']:.3f} ; cobertura >= 1 = {R['cob1']:.3f} ; >= 4 = {R['cob4']:.3f}")
    print(f"Teoria T(1 - cos lambda)/2 = {R['teo_media']:.3f} (diferencia {100*R['rel']:.1f} %)")
    print(f"Constelacion 12/3/1: visibles = {R['media_12']:.3f} (teoria {R['teo_12']:.3f}) ; cobertura >= 1 = {R['cob1_12']:.3f}")
    assert R["rel"] < 0.05 and abs(R["media_12"] - R["teo_12"]) / R["teo_12"] < 0.08
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
