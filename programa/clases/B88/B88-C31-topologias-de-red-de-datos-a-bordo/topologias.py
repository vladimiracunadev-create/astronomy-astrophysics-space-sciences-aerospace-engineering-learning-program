"""B88-C31: topologias de red de datos a bordo: diametro, saltos y tolerancia a fallo de enlace (SINTETICO)."""
import sys
from collections import deque
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: redes de 7 nodos inventadas; nodo 0 = computador de vuelo")

N = 7
def malla(): return {(i, j) for i in range(N) for j in range(i + 1, N)}
TOP = {
 "estrella (hub=0)": {(0, i) for i in range(1, N)},
 "anillo": {(i, (i + 1) % N) if i < (i + 1) % N else ((i + 1) % N, i) for i in range(N)},
 "arbol binario": {(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)},
 "doble estrella (0 y 1)": {(0, i) for i in range(1, N)} | {(1, i) for i in range(2, N)},
 "malla completa": malla(),
}
def vecinos(E, rm=None):
    g = {i: [] for i in range(N)}
    for a, b in E:
        if (a, b) == rm: continue
        g[a].append(b); g[b].append(a)
    return g
def dist(g, s):
    d = {s: 0}; q = deque([s])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in d: d[v] = d[u] + 1; q.append(v)
    return d
def metricas(E):
    g = vecinos(E)
    diam = 0; tot = 0; cnt = 0
    for s in range(N):
        d = dist(g, s)
        diam = max(diam, max(d.values()))
        for t, x in d.items():
            if t != s: tot += x; cnt += 1
    puentes = [e for e in sorted(E) if len(dist(vecinos(E, e), 0)) < N]
    d0 = dist(g, 0)
    return len(E), diam, tot / cnt, puentes, sum(d0.values()) / (N - 1)
print(f"{'topologia':24s} enlaces diametro saltos_medios puentes  saltos_desde_0")
res = {}
for k, E in TOP.items():
    e, d, m, p, d0 = metricas(E)
    res[k] = (e, d, p)
    print(f"{k:24s} {e:7d} {d:8d} {m:13.3f} {len(p):7d}  {d0:.3f}")
print("Puentes (enlaces cuya falla desconecta) por topologia:")
for k, (e, d, p) in res.items(): print(f"  {k:24s}: {p if p else 'ninguno'}")
assert res["anillo"][2] == [] and len(res["estrella (hub=0)"][2]) == 6 and res["malla completa"][0] == 21
assert res["doble estrella (0 y 1)"][2] == []
# Costo: enlaces por tolerancia
print("Enlaces: malla = n(n-1)/2 =", N * (N - 1) // 2, "; anillo = n =", N, "; estrella = n-1 =", N - 1)
print("Pruebas superadas.")
