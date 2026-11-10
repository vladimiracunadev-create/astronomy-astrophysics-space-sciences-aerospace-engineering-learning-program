#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C08: tabla de control de interfaces (ICD) electricas y de datos.

Datos: SINTETICOS (seis interfaces de la mision de ejemplo ESTRELLA-S con tensiones, corrientes, longitudes de arnes y tasas
de datos inventadas). Resistividad del cobre 1.68e-8 ohm*m: valor estandar NO consultado. Reglas del ejemplo (no de una norma):
caida de tension del arnes <= 2 % de la tension de la fuente; tension en la carga dentro del rango admitido; capacidad de un
enlace de datos >= 1.3 x la demanda (margen del 30 %). Metodo 1: formula cerrada V_L = V_s - I * R_ida_vuelta.
Segunda via: analisis nodal con numpy.linalg.solve y carga como resistencia constante. Tolerancia: 1e-6 V. La nota de la ficha de
NASA SmallSat (S7) de buses tipicos de 8.2 V, 5.0 V y 3.3 V se usa solo para escoger tensiones de ejemplo.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

RHO = 1.68e-8
# id, origen, destino, V fuente, I (A), largo (m), area (mm2), rango de la carga (V)
ELEC = [("I1", "EPS", "C&DH", 5.0, 0.40, 0.4, 0.129, (4.75, 5.25)),
        ("I2", "EPS", "Radio", 8.2, 1.20, 0.6, 0.326, (6.0, 9.0)),
        ("I3", "EPS", "Carga util", 3.3, 0.90, 0.8, 0.205, (3.135, 3.465)),
        ("I6", "EPS", "Sensor solo 3.3 V", 5.0, 0.05, 0.3, 0.129, (3.0, 3.6))]
# id, origen, destino, capacidad (kbit/s), demanda (kbit/s)
DATOS = [("I4", "Carga util", "C&DH", 100000.0, 60000.0), ("I5", "C&DH", "Radio", 115.2, 150.0)]
MARGEN_DATOS = 1.3
CAIDA_MAX = 0.02


def evaluar_elec(v, i, largo, area):
    r = 2 * RHO * largo / (area * 1e-6)
    v_cerrada = v - i * r
    rl = v_cerrada / i
    # nodal: nodos 1 (fuente tras Rs=0) y 2 (carga); fuente ideal: G (V2 - V1)... se resuelve [1/r + 1/rl] V2 = v / r
    A = np.array([[1.0 / r + 1.0 / rl]])
    b = np.array([v / r])
    v_nodal = float(np.linalg.solve(A, b)[0])
    return r, v_cerrada, v_nodal, i * i * r


def calcular():
    filas = []
    for (id_, o, d, v, i, L, a, rng) in ELEC:
        r, vl, vn, p = evaluar_elec(v, i, L, a)
        caida = (v - vl) / v
        ok_rango = rng[0] <= vl <= rng[1]
        ok_caida = caida <= CAIDA_MAX
        filas.append(dict(id=id_, o=o, d=d, r=r, vl=vl, vn=vn, p=p, caida=caida * 100, ok_rango=ok_rango, ok_caida=ok_caida,
                          ok=ok_rango and ok_caida))
    datos = []
    for (id_, o, d, cap, dem) in DATOS:
        m = cap / dem
        datos.append(dict(id=id_, o=o, d=d, cap=cap, dem=dem, m=m, ok=m >= MARGEN_DATOS))
    todos = filas + datos
    por = {f["id"]: f for f in todos}
    V = dict(filas=filas, datos=datos, n=len(todos), n_ok=sum(1 for f in todos if f["ok"]),
             fallan=[f["id"] for f in todos if not f["ok"]], dif_max=max(abs(f["vl"] - f["vn"]) for f in filas),
             p_total=sum(f["p"] for f in filas))
    for k in ("I1", "I2", "I3", "I6"):
        V[f"vl_{k}"] = por[k]["vl"]; V[f"c_{k}"] = por[k]["caida"]; V[f"r_{k}"] = por[k]["r"] * 1000
    V["m_I4"] = por["I4"]["m"]; V["m_I5"] = por["I5"]["m"]
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 4 interfaces electricas y 2 de datos; rho(Cu) = 1.68e-8 ohm*m (no consultado)")
    print("Reglas del ejemplo: caida <= 2 %, tension de carga en rango, capacidad >= 1.3 x demanda")
    for f in V["filas"]:
        print(f"  {f['id']} {f['o']:>4s}->{f['d']:<18s} R = {f['r']*1000:6.1f} mohm  V_carga = {f['vl']:.4f} V  caida = {f['caida']:.2f} %  "
              f"P_arnes = {f['p']*1000:.1f} mW  {'CUMPLE' if f['ok'] else 'NO CUMPLE'}")
    for f in V["datos"]:
        print(f"  {f['id']} {f['o']:>10s}->{f['d']:<6s} capacidad {f['cap']:.1f} kbit/s  demanda {f['dem']:.1f}  razon {f['m']:.2f}  {'CUMPLE' if f['ok'] else 'NO CUMPLE'}")
    print(f"Interfaces que cumplen: {V['n_ok']} de {V['n']} ; no cumplen: {', '.join(V['fallan'])}")
    print(f"Diferencia maxima formula cerrada - analisis nodal = {V['dif_max']:.2e} V ; potencia total disipada en arneses = {V['p_total']*1000:.1f} mW")
    comprobar(V["dif_max"] < 1e-6, "formula cerrada y analisis nodal coinciden")
    comprobar(V["fallan"] == ["I3", "I6", "I5"] or sorted(V["fallan"]) == ["I3", "I5", "I6"], "defectos plantados detectados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
