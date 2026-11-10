"""B96-C08: maquina de estados del satelite (SINTETICA): alcanzabilidad y propiedad de seguridad."""
import sys
from collections import deque
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: estados y transiciones ficticios")
T = {
 "LEOP": ["SEGURO", "COMISIONADO"],
 "SEGURO": ["COMISIONADO", "NOMINAL", "LEOP"],
 "COMISIONADO": ["NOMINAL", "SEGURO"],
 "NOMINAL": ["CIENCIA", "MANTENIMIENTO", "SEGURO", "DESORBITANDO"],
 "CIENCIA": ["NOMINAL", "SEGURO"],
 "MANTENIMIENTO": ["NOMINAL", "SEGURO"],
 "DESORBITANDO": ["SEGURO", "FIN"],
 "FIN": [],
}
estados = list(T)
def bfs(origen):
    dist = {origen: 0}; padre = {}; q = deque([origen])
    while q:
        u = q.popleft()
        for v in T[u]:
            if v not in dist:
                dist[v] = dist[u] + 1; padre[v] = u; q.append(v)
    return dist, padre
dist, padre = bfs("LEOP")
print("Alcanzables desde LEOP:", {k: dist[k] for k in estados if k in dist})
camino = ["CIENCIA"]
while camino[-1] != "LEOP": camino.append(padre[camino[-1]])
print("Camino mas corto LEOP -> CIENCIA:", " -> ".join(reversed(camino)))
def dfs(origen):
    vis = set(); pila = [origen]
    while pila:
        u = pila.pop()
        if u in vis: continue
        vis.add(u); pila.extend(T[u])
    return vis
assert dfs("LEOP") == set(dist)
sin_salida = [e for e in estados if e not in ("FIN", "SEGURO") and "SEGURO" not in bfs(e)[0]]
print(f"Estados desde los que no se llega a SEGURO = {sin_salida}")
assert sin_salida == []
entrantes = [u for u in estados if "FIN" in T[u]]
print("Estados con transicion a FIN:", entrantes)
assert entrantes == ["DESORBITANDO"] and T["FIN"] == []
n = len(estados)
M = [[1 if b in T[a] else 0 for b in estados] for a in estados]
print("Transiciones permitidas =", sum(map(sum, M)), "de", n*n, "posibles")
cmd_ciencia = ["NOMINAL", "CIENCIA"]
rechazados = [e for e in estados if e not in cmd_ciencia]
print("Estados que rechazan el comando de ciencia:", rechazados)
assert len(rechazados) == 6
print("Pruebas superadas.")
