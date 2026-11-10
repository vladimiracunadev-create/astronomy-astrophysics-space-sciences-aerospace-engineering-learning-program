#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C20: diseno preliminar completo: cierre iterativo de masa, energia, datos y propelente.

Constantes consultadas el 2026-11-10: g0 = 9.80665 m/s2, RE, GM (NASA/NSSDC); potencia especifica de arreglos solares de pequenos satelites
~30 W/kg (valor central de la distribucion de S7) y energia especifica de paquetes de baterias 90-180 Wh/kg (S7, se usa 120).
SINTETICOS: carga util 21.6 kg (MEV de C09), resto de subsistemas fijos 19.285 kg (MEV de C09), estructura = 18 % de la masa seca,
potencia de reposo = 25 W + 0.35 W por kg de masa seca, toma 110 W x 8 min y comunicaciones 40 W x 7 min por orbita, beta = 0 (eclipse maximo),
rendimientos 0.95, DoD maxima 30 %, margen de diseno del panel 20 %, delta-v 150 m/s, Isp 220 s, limite 80 kg. Los margenes de datos
vienen de B83-C11. Modelo: lazo de punto fijo m_seca -> potencia -> panel y bateria -> m_seca. Segunda via: biseccion sobre la ecuacion
f(m) = m - g(m) = 0. Tolerancia: 1e-9 kg.
"""
import importlib.util
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

M_CARGA, M_FIJA, F_ESTR = 21.6, 19.285, 0.18
DV, ISP, LIMITE = 150.0, 220.0, 80.0
W_KG_PANEL, WH_KG_BAT = 30.0, 120.0
ETA, DOD, MARGEN_PANEL = 0.95, 0.30, 1.20


def datos_c11():
    ruta = Path(__file__).resolve().parents[1] / "B83-C11-presupuestos-de-datos" / "presupuesto_de_datos.py"
    sp = importlib.util.spec_from_file_location("presupuesto_de_datos", ruta)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m.calcular()


def energia(m_seca):
    T = periodo_s() / 60.0
    fe = fraccion_eclipse(H_KM, 0.0)
    te, ts = fe * T, (1 - fe) * T
    ph = 25.0 + 0.35 * m_seca
    e_luz = ph * ts + 110.0 * 8.0 + 40.0 * 7.0
    e_ecl = ph * te
    req = e_luz + e_ecl / (ETA * ETA)
    p_sa = MARGEN_PANEL * req / (ts * ETA)
    cap_wh = e_ecl / 60.0 / ETA / DOD
    return dict(ph=ph, p_sa=p_sa, cap=cap_wh, m_panel=p_sa / W_KG_PANEL, m_bat=cap_wh / WH_KG_BAT, e_req_wh=req / 60.0, te=te, ts=ts)


def g(m_seca):
    e = energia(m_seca)
    base = M_CARGA + M_FIJA + e["m_panel"] + e["m_bat"]
    return base / (1.0 - F_ESTR)


def punto_fijo(m0=60.0):
    m, it = m0, 0
    for it in range(1, 500):
        nuevo = g(m)
        if abs(nuevo - m) < 1e-12: m = nuevo; break
        m = nuevo
    return m, it


def biseccion():
    lo, hi = 10.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid - g(mid) < 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def calcular():
    m, it = punto_fijo()
    mb = biseccion()
    e = energia(m)
    prop = m * (math.exp(DV / (G0 * ISP)) - 1.0)
    total = m + prop
    d = datos_c11()
    return dict(m_seca=m, iteraciones=it, m_bis=mb, dif=abs(m - mb), m_estr=F_ESTR * m, m_panel=e["m_panel"], m_bat=e["m_bat"], p_sa=e["p_sa"],
                cap=e["cap"], ph=e["ph"], e_req=e["e_req_wh"], prop=prop, total=total, margen_kg=LIMITE - total,
                margen_pct=100 * (LIMITE - total) / LIMITE, md=d["margen"], prod=d["prod_dia"], capd=d["cap_dia"],
                cierra=total <= LIMITE and d["margen"] >= 25.0, m_eps=e["m_panel"] + e["m_bat"], te=e["te"])


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS salvo g0, RE, GM (NASA/NSSDC) y 30 W/kg de paneles y 120 Wh/kg de baterias (rangos de S7); datos de C11 importados")
    print(f"Lazo de punto fijo: {V['iteraciones']} iteraciones ; masa seca = {V['m_seca']:.6f} kg ; biseccion = {V['m_bis']:.6f} kg ; diferencia = {V['dif']:.2e} kg")
    print(f"Desglose seco: carga util {M_CARGA:.3f} + resto {M_FIJA:.3f} + paneles {V['m_panel']:.3f} + bateria {V['m_bat']:.3f} + estructura {V['m_estr']:.3f} kg")
    print(f"Energia (beta = 0): reposo {V['ph']:.2f} W ; eclipse {V['te']:.2f} min ; requerida {V['e_req']:.2f} Wh/orbita ; panel {V['p_sa']:.2f} W ; bateria {V['cap']:.2f} Wh")
    print(f"Propelente = {V['prop']:.3f} kg ; masa de lanzamiento = {V['total']:.3f} kg ; limite {LIMITE:.1f} kg ; margen = {V['margen_kg']:.3f} kg ({V['margen_pct']:.2f} %)")
    print(f"Datos (B83-C11): produccion {V['prod']:.2f} Gbit/dia ; capacidad {V['capd']:.2f} Gbit/dia ; margen {V['md']:.2f} %")
    print(f"Cierre tecnico preliminar (masa <= limite y margen de datos >= 25 %): {'SI' if V['cierra'] else 'NO'}")
    comprobar(V["dif"] < 1e-9, "punto fijo y biseccion")
    comprobar(abs(V["m_seca"] - g(V["m_seca"])) < 1e-9, "la masa seca es punto fijo")
    comprobar(V["cierra"], "el diseno cierra")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
