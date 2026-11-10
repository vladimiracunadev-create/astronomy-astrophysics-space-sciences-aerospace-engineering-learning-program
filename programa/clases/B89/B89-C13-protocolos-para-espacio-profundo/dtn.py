#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C13. Protocolos para espacio profundo: almacenamiento y reenvio (estilo Bundle Protocol) sobre un plan de contactos SINTETICO.
Ruta de llegada mas temprana (Dijkstra en tiempo) contrastada con enumeracion exhaustiva de rutas. Sin libreria externa."""
import heapq, sys

H = 3600.0
# (origen, destino, inicio s, fin s, tasa bit/s, retardo unidireccional s)  -- todo SINTETICO
CONTACTOS = [
    ("rover", "orbiter", 1 * H, 1 * H + 600, 2e6, 0.01),
    ("rover", "orbiter", 13 * H, 13 * H + 600, 2e6, 0.01),
    ("rover", "orbiter", 25 * H, 25 * H + 600, 2e6, 0.01),
    ("orbiter", "dsn", 4 * H, 4 * H + 3600, 500e3, 750.0),
    ("orbiter", "dsn", 16 * H, 16 * H + 3600, 500e3, 750.0),
    ("orbiter", "dsn", 28 * H, 28 * H + 3600, 500e3, 750.0),
    ("dsn", "centro", 0.0, 1e9, 10e6, 0.05),
]

def llegada_temprana(origen, destino, t0, bits, contactos=CONTACTOS):
    mejor = {origen: t0}
    cola = [(t0, origen)]
    while cola:
        t, u = heapq.heappop(cola)
        if t > mejor.get(u, 1e30):
            continue
        for (a, b, ini, fin, tasa, ret) in contactos:
            if a != u or fin <= t:
                continue
            sale = max(t, ini)
            dur = bits / tasa
            if sale + dur > fin:
                continue          # no cabe el paquete en la ventana
            llega = sale + dur + ret
            if llega < mejor.get(b, 1e30):
                mejor[b] = llega
                heapq.heappush(cola, (llega, b))
    return mejor.get(destino)

def exhaustivo(origen, destino, t0, bits, contactos=CONTACTOS):
    """Segunda via: enumera todas las secuencias de contactos sin repetir nodo."""
    mejor = [None]
    def rec(u, t, visitados):
        if u == destino:
            if mejor[0] is None or t < mejor[0]:
                mejor[0] = t
            return
        for (a, b, ini, fin, tasa, ret) in contactos:
            if a != u or b in visitados or fin <= t:
                continue
            sale = max(t, ini)
            dur = bits / tasa
            if sale + dur > fin:
                continue
            rec(b, sale + dur + ret, visitados | {b})
    rec(origen, t0, {origen})
    return mejor[0]

def conexion_continua(t_max=40 * H, paso=60.0):
    """Hay algun instante con rover-orbiter y orbiter-dsn simultaneos (ignorando retardos)?"""
    t = 0.0
    while t < t_max:
        a = any(c[0] == "rover" and c[2] <= t < c[3] for c in CONTACTOS)
        b = any(c[0] == "orbiter" and c[2] <= t < c[3] for c in CONTACTOS)
        if a and b:
            return True
        t += paso
    return False

def calcular():
    R = {"casos": []}
    for t0_h, mbit in ((0.0, 100), (2.0, 100), (2.0, 600), (14.0, 100), (26.0, 100)):
        bits = mbit * 1e6
        a = llegada_temprana("rover", "centro", t0_h * H, bits)
        b = exhaustivo("rover", "centro", t0_h * H, bits)
        R["casos"].append((t0_h, mbit, a, b))
    R["capacidad_rover"] = 2e6 * 600
    R["capacidad_orbiter"] = 500e3 * 3600
    R["continua"] = conexion_continua()
    R["owlt"] = 750.0
    R["dif_max"] = max(abs(a - b) for _, _, a, b in R["casos"] if a is not None and b is not None)
    R["imposible"] = llegada_temprana("rover", "centro", 26 * H, 2.5e9)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: rover -> orbiter (10 min cada 12 h, 2 Mbit/s) -> DSN (1 h cada 12 h, 500 kbit/s, retardo 750 s) -> centro")
    print(f"Capacidad por contacto: rover-orbiter = {R['capacidad_rover']/1e6:.0f} Mbit ; orbiter-DSN = {R['capacidad_orbiter']/1e6:.0f} Mbit")
    print(f"{'creado [h]':>10s}{'tamano [Mbit]':>15s}{'llegada [h]':>13s}{'latencia [h]':>14s}{'exhaustivo [h]':>16s}")
    for t0, mb, a, b in R["casos"]:
        if a is None:
            print(f"{t0:10.1f}{mb:15d}{'no llega':>13s}")
        else:
            print(f"{t0:10.1f}{mb:15d}{a/H:13.3f}{(a-t0*H)/H:14.3f}{b/H:16.3f}")
    print(f"Conexion extremo a extremo simultanea alguna vez: {R['continua']}")
    print(f"Paquete de 2500 Mbit creado a las 26 h: {'no cabe en ningun contacto' if R['imposible'] is None else R['imposible']}")
    print(f"Diferencia maxima entre Dijkstra y exhaustivo = {R['dif_max']:.3e} s")
    assert R["dif_max"] < 1e-6 and R["continua"] is False and R["imposible"] is None
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
