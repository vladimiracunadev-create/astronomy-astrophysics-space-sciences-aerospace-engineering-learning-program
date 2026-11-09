#!/usr/bin/env python3
"""B53-C09: estratigrafia SINTETICA de seis unidades. Edades en unidades arbitrarias (ua), no son anos.
Semilla 20261109. Tolerancia: cobertura 2 sigma en [0.90, 0.99]."""
import itertools, math, platform, random

NODOS = list("ABCDEF")
EDAD = dict(zip(NODOS, [3.9, 3.6, 3.3, 2.5, 1.2, 0.4]))
ARISTAS = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("D", "F")]
AREA, TASA = 5000.0, 0.002

def kahn(aristas):
    grado = {n: 0 for n in NODOS}
    for _, b in aristas:
        grado[b] += 1
    listos = sorted(n for n in NODOS if grado[n] == 0)
    orden = []
    while listos:
        n = listos.pop(0)
        orden.append(n)
        for a, b in aristas:
            if a == n:
                grado[b] -= 1
                if grado[b] == 0:
                    listos.append(b); listos.sort()
    return orden

def cuenta_ordenes(aristas):
    k = 0
    for p in itertools.permutations(NODOS):
        pos = {n: i for i, n in enumerate(p)}
        if all(pos[a] < pos[b] for a, b in aristas):
            k += 1
    return k

def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def compute():
    rng = random.Random(20261109)
    topo = kahn(ARISTAS)
    ciclo = len(kahn(ARISTAS + [("F", "A")])) < len(NODOS)
    n_ext = cuenta_ordenes(ARISTAS)
    rep = 20000
    ok_af = ok_bc = 0
    cubre = tot = 0
    for _ in range(rep):
        n = {u: poisson(rng, TASA * EDAD[u] * AREA) for u in NODOS}
        ok_af += n["F"] < n["A"]
        ok_bc += n["C"] < n["B"]
        for u in NODOS:
            est = n[u] / (TASA * AREA)
            err = math.sqrt(max(n[u], 1)) / (TASA * AREA)
            cubre += abs(est - EDAD[u]) <= 2 * err
            tot += 1
    return dict(topo=" ".join(topo), n_ext=n_ext, ciclo=ciclo, p_AF=ok_af / rep, p_BC=ok_bc / rep, cover=cubre / tot, tasa=TASA)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"orden topologico (Kahn): {r['topo']}")
    print(f"ordenes totales compatibles (fuerza bruta, 720 permutaciones): {r['n_ext']}")
    print(f"con la relacion F->A agregada, ciclo detectado: {r['ciclo']}")
    print(f"densidad ordena bien A-F: {r['p_AF']:.4f} ; B-C: {r['p_BC']:.4f}")
    print(f"cobertura de la edad de modelo a 2 sigma: {r['cover']:.4f}")
    assert r["n_ext"] == 4 and r["ciclo"] and 0.90 <= r["cover"] <= 0.99 and r["p_AF"] > r["p_BC"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
