#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C19: cambios de plano simples, combinacion con Hohmann y cambio de RAAN.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3).
ILUSTRATIVOS (sinteticos): inclinacion inicial de 28.5 grados (valor de ejemplo, no el de ninguna base), circular inicial de 400 km de altitud, destino ecuatorial circular
geoestacionaria (r = 42164.2 km), cambio de RAAN de 10 grados con i = 51.6 grados (ilustrativo). Sistema: marco inercial geocentrico, SI; impulsos instantaneos; dos cuerpos.
Modelo: cambio de plano puro en el nodo: dv = 2 v sin(di/2) ; combinado: dv = sqrt(v1^2 + v2^2 - 2 v1 v2 cos di) ;
cambio de RAAN: cos(theta) = cos^2 i + sin^2 i cos(dOmega), dv = 2 v sin(theta/2).
Segunda via: se construye el vector velocidad antes y despues (rotado el angulo en torno a la linea de nodos) y se mide |v2 - v1| con vectores 3D;
el reparto optimo del cambio de inclinacion entre los dos impulsos de la Hohmann se busca barriendo di1 de 0 a di en pasos de 0.01 grados.
Tolerancias: formula frente a vectores 1e-9 relativa; el optimo del barrido frente al refinado por biseccion 0.02 grados.
"""
from __future__ import annotations
import math, platform

MU, RE = 3.986004e14, 6.3781e6


def v_circ(r):
    return math.sqrt(MU / r)


def dv_plano(v, di):
    return 2 * v * math.sin(di / 2)


def dv_comb(v1, v2, di):
    return math.sqrt(v1 * v1 + v2 * v2 - 2 * v1 * v2 * math.cos(di))


def dv_vectores(v, di):
    a = (v, 0.0, 0.0)
    b = (v * math.cos(di), v * math.sin(di), 0.0)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def hohmann_con_plano(r1, r2, di_total, di1):
    a = 0.5 * (r1 + r2)
    vp = math.sqrt(MU * (2 / r1 - 1 / a))
    va = math.sqrt(MU * (2 / r2 - 1 / a))
    v1c, v2c = v_circ(r1), v_circ(r2)
    d1 = dv_comb(v1c, vp, di1)
    d2 = dv_comb(va, v2c, di_total - di1)
    return d1 + d2, d1, d2


def calcular():
    R = {}
    r1, r2 = RE + 400e3, 42164.2e3
    di = math.radians(28.5)
    v1, v2 = v_circ(r1), v_circ(r2)
    R.update(v1=v1, v2=v2)
    R["pl_leo"] = dv_plano(v1, di)
    R["pl_geo"] = dv_plano(v2, di)
    R["pl_leo_vec"] = dv_vectores(v1, di)
    R["dif_vec"] = abs(R["pl_leo"] - R["pl_leo_vec"]) / R["pl_leo"]
    # Hohmann sin plano
    a = 0.5 * (r1 + r2)
    vp = math.sqrt(MU * (2 / r1 - 1 / a))
    va = math.sqrt(MU * (2 / r2 - 1 / a))
    R["hoh"] = (vp - v1) + (v2 - va)
    # opciones
    R["opc_leo"] = R["hoh"] + R["pl_leo"]
    R["opc_geo"] = R["hoh"] + R["pl_geo"]
    tot0, d10, d20 = hohmann_con_plano(r1, r2, di, 0.0)
    totd, d1d, d2d = hohmann_con_plano(r1, r2, di, di)
    R["opc_apogeo"] = tot0
    R["opc_apogeo_d1"], R["opc_apogeo_d2"] = d10, d20
    R["opc_perigeo"] = totd
    # barrido
    best = (1e18, 0.0)
    n = int(math.degrees(di) / 0.01)
    for k in range(n + 1):
        d1_ = math.radians(0.01 * k)
        tot, _, _ = hohmann_con_plano(r1, r2, di, d1_)
        if tot < best[0]:
            best = (tot, math.degrees(d1_))
    R["opt_total"], R["opt_di1"] = best
    # refinado: seccion aurea
    lo, hi = 0.0, di
    g = (math.sqrt(5) - 1) / 2
    for _ in range(100):
        c = hi - g * (hi - lo)
        d_ = lo + g * (hi - lo)
        if hohmann_con_plano(r1, r2, di, c)[0] < hohmann_con_plano(r1, r2, di, d_)[0]:
            hi = d_
        else:
            lo = c
    R["opt_di1_ref"] = math.degrees(0.5 * (lo + hi))
    R["opt_dif"] = abs(R["opt_di1"] - R["opt_di1_ref"])
    R["opt_total_ref"] = hohmann_con_plano(r1, r2, di, math.radians(R["opt_di1_ref"]))[0]
    R["ahorro_vs_leo"] = R["opc_leo"] - R["opt_total_ref"]
    R["ahorro_vs_apogeo"] = R["opc_apogeo"] - R["opt_total_ref"]
    # RAAN
    inc = math.radians(51.6)
    dO = math.radians(10.0)
    ct = math.cos(inc) ** 2 + math.sin(inc) ** 2 * math.cos(dO)
    th = math.acos(ct)
    R["theta_deg"] = math.degrees(th)
    R["raan_dv_leo"] = dv_plano(v1, th)
    R["raan_dv_geo"] = dv_plano(v2, th)
    # 2 sin(di/2) frente a di para angulos pequenos
    R["peq_rel"] = abs(dv_plano(v1, math.radians(1.0)) - v1 * math.radians(1.0)) / (v1 * math.radians(1.0))
    # regla: 60 grados cuesta igual a la velocidad
    R["sesenta"] = dv_plano(1.0, math.radians(60.0))
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"Cambio de plano ILUSTRATIVO de 28.5 grados: v_LEO(400 km) = {R['v1']:.3f} m/s ; v_GEO = {R['v2']:.3f} m/s")
    print(f"  puro en LEO = {R['pl_leo']:.3f} m/s ; en GEO = {R['pl_geo']:.3f} m/s ; vectorial LEO = {R['pl_leo_vec']:.3f} (dif {R['dif_vec']:.1e})")
    print(f"  Hohmann coplanar LEO->GEO = {R['hoh']:.3f} m/s")
    print("Opciones para LEO(i = 28.5) -> GEO ecuatorial:")
    print(f"  Hohmann + plano puro en LEO     = {R['opc_leo']:.1f} m/s")
    print(f"  Hohmann + plano puro en GEO     = {R['opc_geo']:.1f} m/s")
    print(f"  todo el plano en el 2.o impulso = {R['opc_apogeo']:.1f} m/s (dv1 = {R['opc_apogeo_d1']:.1f} ; dv2 = {R['opc_apogeo_d2']:.1f})")
    print(f"  todo el plano en el 1.er impulso = {R['opc_perigeo']:.1f} m/s")
    print(f"  reparto optimo: {R['opt_di1_ref']:.3f} grados en el 1.er impulso (barrido {R['opt_di1']:.2f}) -> {R['opt_total_ref']:.1f} m/s ; ahorro frente a plano en LEO = {R['ahorro_vs_leo']:.1f} m/s ; frente a todo en el 2.o = {R['ahorro_vs_apogeo']:.1f} m/s")
    print(f"Cambio de RAAN de 10 grados con i = 51.6 (ILUSTRATIVO): angulo entre planos = {R['theta_deg']:.4f} grados ; dv en LEO = {R['raan_dv_leo']:.2f} m/s ; en GEO = {R['raan_dv_geo']:.2f} m/s")
    print(f"Un cambio de 60 grados cuesta {R['sesenta']:.6f} v ; para 1 grado la aproximacion v di difiere {R['peq_rel']:.1e}")
    assert R["dif_vec"] < 1e-9
    assert R["opt_dif"] < 0.02
    assert R["opt_total_ref"] <= min(R["opc_apogeo"], R["opc_perigeo"]) + 1e-9
    assert abs(R["sesenta"] - 1.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
