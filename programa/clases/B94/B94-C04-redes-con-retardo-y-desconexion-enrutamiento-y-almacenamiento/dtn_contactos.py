#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C04: almacenamiento y reenvio con un plan de contactos (red Marte -> relevo -> Tierra, SINTETICA).

Consultado (2026-11-10, CCSDS 734.2-B-1, sept. 2015): el protocolo de paquetes (Bundle Protocol) forma una red de almacenamiento y reenvio
que tolera conectividad intermitente y aprovecha conectividad programada u oportunista; ofrece transferencia de custodia; el parametro de
vida util indica el tiempo tras la creacion tras el cual los agentes pueden descartar el paquete.
NO consultado: el algoritmo de enrutamiento por grafo de contactos del libro de CCSDS (no se implementa su especificacion; aqui hay una
busqueda de llegada mas temprana propia, con volumen residual por contacto) y la capa de convergencia.
Constantes definidas, no consultadas en esta sesion: c = 299792.458 km/s (SI) y 1 UA = 149597870.7 km (IAU 2012).
Plan de contactos, volumenes y distancias SINTETICOS: el retardo unidireccional del enlace relevo-Tierra (750 s ~ 1.5 UA) es ilustrativo.
Contactos (t = 0 es una epoca arbitraria):
  L->R (aterrizador a relevo): pasos de 600 s cada 43200 s desde t = 1000 s, 62500 B/s, retardo 0.01 s.
  R->E (relevo a Tierra): ventanas de 14400 s cada 86400 s desde t = 20000 s, 250000 B/s, retardo 750 s.
Los paquetes (bundles) son de 15 MB (15e6 B); no se fragmentan; uno cada 10800 s en el aterrizador durante 12 pasos de generacion.
Segunda via: enumeracion exhaustiva de secuencias de contactos frente a la busqueda de llegada mas temprana.
Tolerancias: tiempos en segundos con 1e-9; igualdad exacta de recuentos.
"""
from __future__ import annotations
import itertools, platform

C_KMS = 299792.458
UA_KM = 149597870.7
TAM = 15e6


def plan():
    cs = []
    for k in range(12):
        cs.append({"id": f"LR{k}", "de": "L", "a": "R", "ini": 1000 + 43200 * k, "fin": 1600 + 43200 * k, "tasa": 62500.0, "owlt": 0.01, "ocupado": 0.0})
    for k in range(5):
        cs.append({"id": f"RE{k}", "de": "R", "a": "E", "ini": 20000 + 86400 * k, "fin": 34400 + 86400 * k, "tasa": 250000.0, "owlt": 750.0, "ocupado": 0.0})
    return cs


def mejor_ruta(cs, origen, destino, t0, tam, limite):
    """Llegada mas temprana: relajacion de tiempos por nodo con espera ilimitada (almacenamiento) y volumen residual."""
    mejor = {origen: (t0, None)}
    cola = [origen]
    visto = set()
    while cola:
        u = min((n for n in cola if n not in visto), key=lambda n: mejor[n][0], default=None)
        if u is None:
            break
        visto.add(u)
        cola = [n for n in cola if n != u]
        tu = mejor[u][0]
        for c in cs:
            if c["de"] != u:
                continue
            ini = max(tu, c["ini"], c["ocupado"])
            fin = ini + tam / c["tasa"]
            if fin > c["fin"] + 1e-9:
                continue
            llega = fin + c["owlt"]
            if llega > limite:
                continue
            v = c["a"]
            if v not in mejor or llega < mejor[v][0] - 1e-12:
                mejor[v] = (llega, (u, c, ini, fin))
                if v not in visto:
                    cola.append(v)
    if destino not in mejor:
        return None
    ruta, n = [], destino
    while mejor[n][1] is not None:
        u, c, ini, fin = mejor[n][1]
        ruta.append((u, c, ini, fin))
        n = u
    ruta.reverse()
    return mejor[destino][0], ruta


def fuerza_bruta(cs, origen, destino, t0, tam):
    mejor = None
    for k in (1, 2):
        for seq in itertools.permutations(cs, k):
            nodo, t, ok = origen, t0, True
            for c in seq:
                if c["de"] != nodo:
                    ok = False
                    break
                ini = max(t, c["ini"], c["ocupado"])
                fin = ini + tam / c["tasa"]
                if fin > c["fin"] + 1e-9:
                    ok = False
                    break
                t, nodo = fin + c["owlt"], c["a"]
            if ok and nodo == destino and (mejor is None or t < mejor):
                mejor = t
    return mejor


def simula(vida):
    cs = plan()
    res = []
    for i in range(12):
        t0 = 10800.0 * i
        r = mejor_ruta(cs, "L", "E", t0, TAM, t0 + vida)
        if r is None:
            res.append((t0, None, None))
            continue
        llega, ruta = r
        for (_, c, ini, fin) in ruta:
            c["ocupado"] = fin
        res.append((t0, llega, ruta))
    return res


def ocupacion_pico(res, nodo):
    ev = []
    for t0, llega, ruta in res:
        if ruta is None:
            continue
        if nodo == "L":
            ev += [(t0, 1), (ruta[0][2], -1)]
        else:
            ev += [(ruta[0][3] + ruta[0][1]["owlt"], 1), (ruta[1][2], -1)]
    ev.sort(key=lambda e: (e[0], e[1]))
    n = pico = 0
    for _, d in ev:
        n += d
        pico = max(pico, n)
    return pico


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Retardo unidireccional por distancia (ILUSTRATIVO), owlt = d / c:")
    for ua in (0.5, 1.0, 1.5, 2.5):
        print(f"  {ua:3.1f} UA -> {ua * UA_KM / C_KMS:7.1f} s ({ua * UA_KM / C_KMS / 60:5.1f} min); ida y vuelta {2 * ua * UA_KM / C_KMS:7.1f} s")
    rtt = 1500.0
    for ventana in (1, 8, 64):
        print(f"  parada y espera con ventana {ventana:2d} tramas de 1 MB y RTT {rtt:.0f} s: {min(250000.0, ventana * 1e6 / rtt):9.1f} B/s de {250000.0:.0f} B/s")
    cs = plan()
    # 1) un paquete aislado, y segunda via
    r = mejor_ruta(cs, "L", "E", 0.0, TAM, 1e12)
    llega, ruta = r
    bf = fuerza_bruta(cs, "L", "E", 0.0, TAM)
    print(f"Paquete de 15 MB creado en t = 0: llega a la Tierra en t = {llega:.2f} s ({llega / 3600:.2f} h); fuerza bruta = {bf:.2f} s")
    for (u, c, ini, fin) in ruta:
        print(f"   contacto {c['id']} ({c['de']}->{c['a']}): transmite de {ini:.1f} a {fin:.1f} s")
    espera = ruta[1][2] - (ruta[0][3] + ruta[0][1]["owlt"])
    print(f"   espera almacenado en el relevo = {espera:.1f} s ({espera / 3600:.2f} h)")
    assert abs(llega - bf) < 1e-9
    # 2) conexion extremo a extremo: ventanas que se solapan
    solap = [(a["id"], b["id"]) for a in cs if a["de"] == "L" for b in cs if b["de"] == "R" if max(a["ini"], b["ini"]) < min(a["fin"], b["fin"])]
    print(f"Pares de contactos L->R y R->E simultaneos (necesarios para un camino extremo a extremo): {len(solap)}")
    assert len(solap) == 0
    # 3) vida util y trafico
    print("12 paquetes de 15 MB, uno cada 10800 s en el aterrizador; un paso de 600 s admite 2 paquetes (37.5 MB):")
    print(" vida util [h]  entregados  latencia mediana [h]  pico almacen. aterrizador  pico almacen. relevo")
    previo = -1
    for vida_h in (12, 24, 48, 96, 240):
        res = simula(vida_h * 3600.0)
        ent = [x for x in res if x[1] is not None]
        lat = sorted((x[1] - x[0]) / 3600 for x in ent)
        med = lat[len(lat) // 2] if lat else float("nan")
        print(f"   {vida_h:5d}          {len(ent):3d} de 12        {med:8.2f}                {ocupacion_pico(res, 'L'):3d} paquetes               {ocupacion_pico(res, 'R'):3d} paquetes")
        assert len(ent) >= previo
        previo = len(ent)
    # 4) conservacion de volumen
    res = simula(240 * 3600.0)
    usado = {}
    for _, llega, ruta in res:
        for (_, c, ini, fin) in ruta or []:
            usado[c["id"]] = usado.get(c["id"], 0.0) + TAM
    maximo = max(usado[k] / (next(c for c in plan() if c["id"] == k)["tasa"] * (next(c for c in plan() if c["id"] == k)["fin"] - next(c for c in plan() if c["id"] == k)["ini"])) for k in usado)
    print(f"Mayor fraccion del volumen de un contacto usada = {maximo:.3f} (debe ser <= 1)")
    assert maximo <= 1.0 + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
