"""B114-C01 - Rutas de evacuacion en un habitat SINTETICO.

Unidades: m, s, personas. Sin sistema de referencia espacial (grafo de modulos).
Todos los datos son ILUSTRATIVOS; no describen ningun habitat real.
Solo biblioteca estandar. Python 3.12.
"""
import heapq
import sys

# Habitat sintetico: nodos = modulos; aristas = pasillos (longitud en m)
EDGES = {
    ("LAB", "NODO"): 8.0, ("DORM", "NODO"): 6.0, ("NODO", "ESCLUSA"): 10.0,
    ("NODO", "TALLER"): 7.0, ("TALLER", "SALIDA_B"): 9.0, ("LAB", "TALLER"): 12.0,
    ("ESCLUSA", "SALIDA_A"): 4.0, ("DORM", "TALLER"): 11.0,
}
SALIDAS = ["SALIDA_A", "SALIDA_B"]
V_CAMINATA = 1.0        # m/s, velocidad ilustrativa con visibilidad reducida
Q_PUERTA = 0.5          # personas/s por salida (flujo especifico ilustrativo)
PERSONAS = 6            # tripulacion sintetica
T_REACCION = 20.0       # s, ilustrativo


def vecinos(edges):
    g = {}
    for (a, b), w in edges.items():
        g.setdefault(a, []).append((b, w))
        g.setdefault(b, []).append((a, w))
    return g


def dijkstra(g, origen):
    dist = {origen: 0.0}
    prev = {}
    cola = [(0.0, origen)]
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist.get(u, 1e18):
            continue
        for v, w in g.get(u, []):
            nd = d + w
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(cola, (nd, v))
    return dist, prev


def camino(prev, destino):
    ruta = [destino]
    while ruta[-1] in prev:
        ruta.append(prev[ruta[-1]])
    return ruta[::-1]


def mejor_salida(edges, origen):
    g = vecinos(edges)
    dist, prev = dijkstra(g, origen)
    cand = [(dist[s], s) for s in SALIDAS if s in dist]
    if not cand:
        return None
    d, s = min(cand)
    return d, camino(prev, s)


def aristas_de(ruta):
    return {tuple(sorted(p)) for p in zip(ruta[:-1], ruta[1:])}


def fuerza_bruta(edges, origen):
    """Segunda via: enumera todos los caminos simples (DFS) y toma el minimo."""
    g = vecinos(edges)
    mejor = [1e18]

    def dfs(u, vis, acc):
        if u in SALIDAS:
            mejor[0] = min(mejor[0], acc)
            return
        for v, w in g[u]:
            if v not in vis:
                dfs(v, vis | {v}, acc + w)
    dfs(origen, {origen}, 0.0)
    return mejor[0]


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Habitat SINTETICO: v = %.1f m/s, flujo de puerta = %.1f pers/s, "
          "reaccion = %.0f s" % (V_CAMINATA, Q_PUERTA, T_REACCION))
    print(" origen   d_min [m]  t_salida [s]  ruta")
    peor = 0.0
    resultados = {}
    for o in ["LAB", "DORM", "TALLER", "NODO"]:
        d, ruta = mejor_salida(EDGES, o)
        t = T_REACCION + d / V_CAMINATA
        resultados[o] = (d, ruta)
        peor = max(peor, t)
        print("%-7s %9.1f %12.1f  %s" % (o, d, t, "->".join(ruta)))
        assert abs(d - fuerza_bruta(EDGES, o)) < 1e-9
    print("Peor tiempo de salida individual = %.1f s" % peor)

    # Ruta alternativa independiente (sin aristas de la ruta principal)
    print("Ruta alternativa tras bloquear la ruta principal:")
    for o in ["LAB", "DORM"]:
        d, ruta = resultados[o]
        bloq = aristas_de(ruta)
        e2 = {k: w for k, w in EDGES.items() if tuple(sorted(k)) not in bloq}
        alt = mejor_salida(e2, o)
        if alt is None:
            print("  %-5s SIN ruta alternativa" % o)
        else:
            print("  %-5s d = %.1f m (principal %.1f m)  %s" %
                  (o, alt[0], d, "->".join(alt[1])))
            assert alt[0] >= d - 1e-9

    # Cuello de botella: todas las personas por la salida mas cercana
    t_cola = PERSONAS / Q_PUERTA
    print("Cola en una sola salida: %d personas / %.1f pers/s = %.1f s" %
          (PERSONAS, Q_PUERTA, t_cola))
    print("Reparto en dos salidas: %.1f s" % (PERSONAS / 2 / Q_PUERTA))
    t_total = peor + PERSONAS / 2 / Q_PUERTA
    print("Tiempo total de evacuacion (reparto en 2 salidas) = %.1f s" % t_total)
    assert t_total < peor + t_cola
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
