#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C05: grafo de trazabilidad necesidad -> requisito -> diseno -> verificacion.

Datos: SINTETICOS (seis necesidades, ocho requisitos, seis elementos de diseno y seis verificaciones de la mision de ejemplo
ESTRELLA-S, con cuatro defectos plantados: una necesidad sin requisito, un requisito sin necesidad, un requisito sin verificacion
y un elemento de diseno sin requisito). Modelo: grafo dirigido. Metodo 1: recorrido en anchura (BFS). Segunda via: clausura
transitiva de Warshall sobre la matriz de adyacencia. Tolerancia: ambos conjuntos de impacto deben ser iguales. Sin constantes fisicas.
"""
import sys
from collections import deque
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

NEC = ["N1", "N2", "N3", "N4", "N5", "N6"]
REQ = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]
DIS = ["D1 Camara", "D2 Panel solar", "D3 Bateria", "D4 Computadora", "D5 Radio", "D6 Radiador decorativo"]
VER = ["V1 Ensayo de resolucion", "V2 Pesaje", "V3 Ensayo de enlace", "V4 Analisis de vida", "V5 Ensayo de potencia", "V6 Prueba de memoria"]
ARISTAS = (
    [("N1", "R01"), ("N2", "R02"), ("N3", "R03"), ("N3", "R04"), ("N4", "R04"), ("N5", "R05"), ("N2", "R06"), ("N3", "R08")]
    + [("R01", "D1 Camara")] + [("R02", d) for d in DIS[:5]] + [("R03", "D5 Radio"), ("R03", "D4 Computadora"), ("R04", "D5 Radio"),
       ("R05", "D2 Panel solar"), ("R05", "D3 Bateria"), ("R06", "D2 Panel solar"), ("R06", "D3 Bateria"), ("R06", "D4 Computadora"),
       ("R07", "D4 Computadora"), ("R08", "D4 Computadora")]
    + [("R01", "V1 Ensayo de resolucion"), ("R02", "V2 Pesaje"), ("R03", "V3 Ensayo de enlace"), ("R04", "V3 Ensayo de enlace"),
       ("R05", "V4 Analisis de vida"), ("R06", "V5 Ensayo de potencia"), ("R08", "V6 Prueba de memoria")]
)
NODOS = NEC + REQ + DIS + VER
IDX = {n: i for i, n in enumerate(NODOS)}


def descendientes(origen):
    ady = {}
    for a, b in ARISTAS: ady.setdefault(a, []).append(b)
    vis, q = set(), deque([origen])
    while q:
        x = q.popleft()
        for y in ady.get(x, []):
            if y not in vis: vis.add(y); q.append(y)
    return vis


def warshall():
    n = len(NODOS)
    M = np.zeros((n, n), dtype=bool)
    for a, b in ARISTAS: M[IDX[a], IDX[b]] = True
    for k in range(n):
        M |= np.outer(M[:, k], M[k, :])
    return M


def calcular():
    pa = {r: [a for a, b in ARISTAS if b == r and a in NEC] for r in REQ}
    huerf = [r for r in REQ if not pa[r]]
    sin_ver = [r for r in REQ if not any(a == r and b in VER for a, b in ARISTAS)]
    nec_sin = [n for n in NEC if not any(a == n for a, b in ARISTAS)]
    dis_sin = [d for d in DIS if not any(b == d and a in REQ for a, b in ARISTAS)]
    imp = descendientes("R03")
    M = warshall()
    imp2 = {NODOS[j] for j in range(len(NODOS)) if M[IDX["R03"], j]}
    ancestros = {NODOS[i] for i in range(len(NODOS)) if M[i, IDX["R03"]]}
    imp_n3 = descendientes("N3")
    return dict(n_aristas=len(ARISTAS), huerf=huerf, sin_ver=sin_ver, nec_sin=nec_sin, dis_sin=dis_sin, imp=sorted(imp),
                imp2=sorted(imp2), ancestros=sorted(ancestros), n_imp=len(imp), n_imp_n3=len(imp_n3),
                cob_nec=100.0 * (len(NEC) - len(nec_sin)) / len(NEC), cob_req=100.0 * (len(REQ) - len(huerf)) / len(REQ),
                cob_ver=100.0 * (len(REQ) - len(sin_ver)) / len(REQ), cob_dis=100.0 * (len(DIS) - len(dis_sin)) / len(DIS))


def main():
    V = calcular()
    print(cabecera())
    print(f"Datos SINTETICOS: {len(NEC)} necesidades, {len(REQ)} requisitos, {len(DIS)} elementos de diseno, {len(VER)} verificaciones, {V['n_aristas']} enlaces")
    print(f"Necesidades sin requisito: {V['nec_sin']} ; requisitos sin necesidad: {V['huerf']}")
    print(f"Requisitos sin verificacion: {V['sin_ver']} ; elementos de diseno sin requisito: {V['dis_sin']}")
    print(f"Cobertura: necesidades {V['cob_nec']:.1f} % ; requisitos con origen {V['cob_req']:.1f} % ; requisitos verificados {V['cob_ver']:.1f} % ; diseno con requisito {V['cob_dis']:.1f} %")
    print(f"Impacto de cambiar R03 (BFS): {V['imp']}")
    print(f"Impacto de cambiar R03 (Warshall): {V['imp2']}")
    print(f"Ancestros de R03: {V['ancestros']} ; elementos alcanzados desde N3: {V['n_imp_n3']}")
    comprobar(V["imp"] == V["imp2"], "BFS y Warshall dan el mismo impacto")
    comprobar(V["huerf"] == ["R07"] and V["sin_ver"] == ["R07"] and V["nec_sin"] == ["N6"] and V["dis_sin"] == ["D6 Radiador decorativo"], "defectos plantados detectados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
