#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C22: centro de masa e inercia de un lanzador SINTETICO durante el consumo de propelente.

Datos consultados (2026-11-10): definicion del centro de gravedad como punto alrededor del cual rota el cohete y criterio de estabilidad (NASA Glenn, Rocket Stability).
SINTETICOS / ILUSTRATIVOS (inventados): vehiculo de 20 m y radio de tanques 0.75 m; x desde la punta (m); masas secas: ojiva y carga 1500 kg en x = 2; tanque superior (estructura 1500 kg) y propelente 8 000 kg
llenando x entre 4 y 9 m; tanque inferior (estructura 1500 kg) y propelente 10 000 kg entre 9.5 y 16 m; motor 2000 kg en x = 18.5; centro de presion fijo en 14.0 m (de C21); d = 1.5 m.
Los dos tanques se vacian en proporcion a su masa de propelente; el liquido se acumula en el extremo trasero de cada tanque (aceleracion axial hacia adelante), superficie plana, sin oleaje.
Sistema: eje longitudinal x desde la punta; inercia de cabeceo respecto del centro de masa instantaneo, SI.
Modelo: columna cilindrica de liquido de masa m_l y longitud L_l = m_l/(rho A): su centro esta a x_trasero - L_l/2 y su inercia transversal propia es m_l (R^2/4 + L_l^2/12); teorema de ejes paralelos.
Segunda via: discretizacion en 4000 rebanadas de cada tanque para recalcular x_cg e I_y.
Tolerancias: x_cg e I_y por rebanadas frente a la forma cerrada 1e-6 relativo.
"""
import math, platform

D, RT, XCP = 1.5, 0.75, 14.0
RHO_PROP = 1000.0
AT = math.pi * RT ** 2
SECOS = [("ojiva y carga", 1500.0, 2.0, 0.0), ("estructura tanque superior", 1500.0, 6.5, 5.0), ("estructura tanque inferior", 1500.0, 12.75, 6.5), ("motor", 2000.0, 18.5, 0.0)]
TANQUES = [dict(nom="superior", x_trasero=9.0, mp0=8000.0, largo=5.0), dict(nom="inferior", x_trasero=16.0, mp0=10000.0, largo=6.5)]


def masas(f):
    """f = fraccion de propelente restante (0..1). Devuelve lista de (masa, x_cg_propio, inercia_propia)."""
    el = []
    for _, m, x, L in SECOS:
        el.append((m, x, m * L * L / 12.0))
    for t in TANQUES:
        ml = t["mp0"] * f
        if ml > 0:
            Ll = ml / (RHO_PROP * AT)
            el.append((ml, t["x_trasero"] - Ll / 2, ml * (RT ** 2 / 4 + Ll ** 2 / 12)))
    return el


def cg_inercia(f):
    el = masas(f)
    m = sum(e[0] for e in el)
    xcg = sum(e[0] * e[1] for e in el) / m
    iy = sum(e[2] + e[0] * (e[1] - xcg) ** 2 for e in el)
    return m, xcg, iy


def cg_inercia_rebanadas(f, n=4000):
    el = []
    for _, m, x, L in SECOS:
        el.append((m, x, m * L * L / 12.0))
    sl = []
    for t in TANQUES:
        ml = t["mp0"] * f
        if ml > 0:
            Ll = ml / (RHO_PROP * AT)
            dm = ml / n
            for i in range(n):
                xi = t["x_trasero"] - Ll + (i + 0.5) * Ll / n
                sl.append((dm, xi, dm * RT ** 2 / 4))
    todo = el + sl
    m = sum(e[0] for e in todo)
    xcg = sum(e[0] * e[1] for e in todo) / m
    iy = sum(e[2] + e[0] * (e[1] - xcg) ** 2 for e in todo)
    return m, xcg, iy


def calcular():
    r = {"filas": []}
    r["llenado"] = [(t["nom"], t["mp0"] / (RHO_PROP * AT), t["largo"]) for t in TANQUES]
    assert all(c <= L for _, c, L in r["llenado"])
    for f in (1.0, 0.75, 0.5, 0.25, 0.0):
        m, xcg, iy = cg_inercia(f)
        r["filas"].append(dict(f=f, m=m, xcg=xcg, iy=iy, sm=(XCP - xcg) / D))
    errs = []
    for f in (1.0, 0.5, 0.1, 0.0):
        a, b = cg_inercia(f), cg_inercia_rebanadas(f)
        errs.append(max(abs(a[1] - b[1]) / a[1], abs(a[2] - b[2]) / a[2], abs(a[0] - b[0]) / a[0]))
    r["err"] = max(errs)
    sm = [x["sm"] for x in r["filas"]]
    r["sm_min"], r["sm_max"] = min(sm), max(sm)
    r["dx_cg"] = r["filas"][-1]["xcg"] - r["filas"][0]["xcg"]
    # pendiente dx_cg/dm al inicio
    f1, f2 = 1.0, 0.99
    m1, x1, _ = cg_inercia(f1)
    m2, x2, _ = cg_inercia(f2)
    r["dxdm_ini"] = (x1 - x2) / (m1 - m2)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Vehiculo SINTETICO: dos tanques cilindricos (R = 0.75 m); CP fijo en 14.0 m; d = 1.5 m")
    print("Columna de liquido a tanque lleno / largo del tanque [m]: " + "; ".join(f"{n} {c:.2f} / {L:.1f}" for n, c, L in r["llenado"]))
    print(" prop. restante   masa [kg]   x_cg [m]   I_y [kg m2]   margen [calibres]")
    for x in r["filas"]:
        print(f"   {x['f']*100:6.0f} %     {x['m']:9.0f}   {x['xcg']:8.4f}   {x['iy']:12.4g}   {x['sm']:8.4f}")
    print(f"Desplazamiento neto del centro de masa hacia la cola = {r["dx_cg"]:.4f} m ({r["dx_cg"]/D:.3f} calibres); maximo {max(x["xcg"] for x in r["filas"]):.4f} m; pendiente inicial dx_cg/dm = {r['dxdm_ini']*1e3:.4f} mm/kg")
    print(f"Margen estatico minimo = {r['sm_min']:.4f} y maximo = {r['sm_max']:.4f} calibres")
    print(f"Comprobacion por rebanadas (4000 por tanque): error relativo maximo en masa, x_cg e I_y = {r['err']:.2e}")
    assert r["err"] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
