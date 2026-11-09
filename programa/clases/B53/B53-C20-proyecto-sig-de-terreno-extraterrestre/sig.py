#!/usr/bin/env python3
"""B53-C20: proyecto SIG sobre un MDE SINTETICO de 101 x 101 celdas de 10 m. Colina gaussiana (120 m, sigma 200 m) + inclinacion 0.02.
Pendiente de Horn; sombreado; transitabilidad con umbral 15 grados; camino por busqueda en anchura (4 vecinos).
Tolerancias: plano 1e-6 grados; paraboloide 0.05 grados."""
import math, platform
from collections import deque

N, H = 101, 10.0

def horn(z):
    s = [[None] * N for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            a, b, c = z[i - 1][j - 1], z[i - 1][j], z[i - 1][j + 1]
            d, f = z[i][j - 1], z[i][j + 1]
            g, h, k = z[i + 1][j - 1], z[i + 1][j], z[i + 1][j + 1]
            dzdx = ((c + 2 * f + k) - (a + 2 * d + g)) / (8 * H)
            dzdy = ((g + 2 * h + k) - (a + 2 * b + c)) / (8 * H)
            s[i][j] = (math.degrees(math.atan(math.hypot(dzdx, dzdy))), dzdx, dzdy)
    return s

def mdes():
    plano = [[0.1 * (j * H) for j in range(N)] for i in range(N)]
    par = [[((i - 50) * H) ** 2 / 1000.0 + ((j - 50) * H) ** 2 / 1000.0 for j in range(N)] for i in range(N)]
    terr = [[120 * math.exp(-(((i - 50) * H) ** 2 + ((j - 50) * H) ** 2) / (2 * 200.0 ** 2)) + 0.02 * j * H for j in range(N)] for i in range(N)]
    return plano, par, terr

def bfs(ok, ini, fin):
    dist = {ini: 0}
    q = deque([ini])
    while q:
        c = q.popleft()
        if c == fin:
            return dist[c]
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (c[0] + d[0], c[1] + d[1])
            if n not in dist and 0 <= n[0] < N and 0 <= n[1] < N and ok[n[0]][n[1]]:
                dist[n] = dist[c] + 1
                q.append(n)
    return None

def compute():
    plano, par, terr = mdes()
    sp = horn(plano)
    err_plano = max(abs(sp[i][j][0] - math.degrees(math.atan(0.1))) for i in range(1, N - 1) for j in range(1, N - 1))
    sq = horn(par)
    err_par = max(abs(sq[i][j][0] - math.degrees(math.atan(math.hypot((i - 50) * H, (j - 50) * H) / 500.0))) for i in range(1, N - 1) for j in range(1, N - 1))
    st = horn(terr)
    smax = max(st[i][j][0] for i in range(1, N - 1) for j in range(1, N - 1))
    ok = [[False] * N for _ in range(N)]
    n_ok = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            ok[i][j] = st[i][j][0] < 15.0
            n_ok += ok[i][j]
    frac = 100 * n_ok / ((N - 2) ** 2)
    pasos = bfs(ok, (1, 1), (N - 2, N - 2))
    ruta = pasos * H if pasos is not None else float("nan")
    recta = (2 * (N - 3)) * H
    # sombreado en el plano z = 0.02 x: sol a 30 grados de elevacion, azimut 135 grados
    zen, azs = math.radians(60), math.radians(135)
    pend, asp = math.atan(0.02), math.atan2(0.0, -0.02)
    hs = math.cos(zen) * math.cos(pend) + math.sin(zen) * math.sin(pend) * math.cos(azs - (math.pi / 2 - asp))
    return dict(err_plano=err_plano, err_par=err_par, smax=smax, frac=frac, ruta=ruta, recta=recta, hs=hs)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"error maximo de pendiente: plano {r['err_plano']:.2e} grados ; paraboloide {r['err_par']:.3e} grados")
    print(f"pendiente maxima del terreno = {r['smax']:.2f} grados ; celdas transitables (<15) = {r['frac']:.2f} %")
    print(f"camino mas corto = {r['ruta']:.0f} m ; Manhattan entre esquinas = {r['recta']:.0f} m")
    print(f"sombreado en el plano inclinado = {r['hs']:.4f}")
    assert r["err_plano"] < 1e-6 and r["err_par"] < 0.05 and r["ruta"] >= r["recta"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
