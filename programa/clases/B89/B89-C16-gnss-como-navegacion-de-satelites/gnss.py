#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C16. GNSS como navegacion: posicion por pseudodistancias con minimos cuadrados y dilucion de la precision (DOP).
Constelacion y ruido SINTETICOS (semilla 89); radio orbital y radio terrestre ILUSTRATIVOS (no consultados). c: NIST (consultada)."""
import math, random, sys

C = 299_792_458.0
RE = 6371e3
RS = 26_560e3     # radio orbital tipo MEO, ILUSTRATIVO

def resolver(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x

def inversa(A):
    n = len(A)
    cols = [resolver(A, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def constelacion():
    # 24 satelites en 6 planos de 4, inclinacion 55 grados (SINTETICA, tipo Walker 24/6/1)
    sats = []
    i = math.radians(55)
    for p in range(6):
        raan = math.radians(60 * p)
        for k in range(4):
            u = math.radians(90 * k + 15 * p)
            x, y = RS * math.cos(u), RS * math.sin(u) * math.cos(i)
            z = RS * math.sin(u) * math.sin(i)
            sats.append((x * math.cos(raan) - y * math.sin(raan), x * math.sin(raan) + y * math.cos(raan), z))
    return sats

def visibles(sats, rx, mascara=10.0):
    up = [c / math.sqrt(sum(v * v for v in rx)) for c in rx]
    out = []
    for s in sats:
        rho = [s[i] - rx[i] for i in range(3)]
        d = math.sqrt(sum(v * v for v in rho))
        el = math.degrees(math.asin(sum(rho[i] * up[i] for i in range(3)) / d))
        if el >= mascara:
            out.append((s, el))
    return out

def geometria(sats_vis, x):
    G = []
    for s in sats_vis:
        rho = [s[i] - x[i] for i in range(3)]
        d = math.sqrt(sum(v * v for v in rho))
        G.append([-rho[0] / d, -rho[1] / d, -rho[2] / d, 1.0])
    return G

def dop(G, rx):
    GtG = [[sum(G[k][i] * G[k][j] for k in range(len(G))) for j in range(4)] for i in range(4)]
    Q = inversa(GtG)
    lat = math.asin(rx[2] / math.sqrt(sum(v * v for v in rx)))
    lon = math.atan2(rx[1], rx[0])
    E = [-math.sin(lon), math.cos(lon), 0.0]
    N = [-math.sin(lat) * math.cos(lon), -math.sin(lat) * math.sin(lon), math.cos(lat)]
    U = [math.cos(lat) * math.cos(lon), math.cos(lat) * math.sin(lon), math.sin(lat)]
    def cuad(v):
        return sum(v[i] * Q[i][j] * v[j] for i in range(3) for j in range(3))
    return {"GDOP": math.sqrt(sum(Q[i][i] for i in range(4))), "PDOP": math.sqrt(sum(Q[i][i] for i in range(3))),
            "HDOP": math.sqrt(cuad(E) + cuad(N)), "VDOP": math.sqrt(cuad(U)), "TDOP": math.sqrt(Q[3][3])}

def posicionar(sats_vis, pseudo, x0=None):
    x = list(x0) if x0 else [0.0, 0.0, 0.0, 0.0]
    for _ in range(12):
        G = geometria(sats_vis, x)
        res = []
        for k, s in enumerate(sats_vis):
            d = math.sqrt(sum((s[i] - x[i]) ** 2 for i in range(3)))
            res.append(pseudo[k] - (d + x[3]))
        GtG = [[sum(G[k][i] * G[k][j] for k in range(len(G))) for j in range(4)] for i in range(4)]
        Gtr = [sum(G[k][i] * res[k] for k in range(len(G))) for i in range(4)]
        dx = resolver(GtG, Gtr)
        x = [x[i] + dx[i] for i in range(4)]
        if max(abs(v) for v in dx) < 1e-9:
            break
    return x

def calcular():
    R = {}
    lat, lon = math.radians(40), 0.0
    rx = [RE * math.cos(lat) * math.cos(lon), RE * math.cos(lat) * math.sin(lon), RE * math.sin(lat)]
    sats = constelacion()
    vis = visibles(sats, rx)
    R["n_vis"] = len(vis)
    sv = [s for s, _ in vis]
    R["elev"] = sorted(round(e, 1) for _, e in vis)
    dtr = 1.0e-4   # s, sesgo de reloj SINTETICO
    verdad = rx + [C * dtr]
    pseudo0 = [math.sqrt(sum((s[i] - rx[i]) ** 2 for i in range(3))) + C * dtr for s in sv]
    x0 = posicionar(sv, pseudo0)
    R["err_sin_ruido"] = max(abs(x0[i] - verdad[i]) for i in range(4))
    R["dop"] = dop(geometria(sv, rx), rx)
    rng = random.Random(89)
    sigma = 3.0
    errs = []
    for _ in range(400):
        ps = [p + rng.gauss(0, sigma) for p in pseudo0]
        x = posicionar(sv, ps)
        errs.append(math.sqrt(sum((x[i] - rx[i]) ** 2 for i in range(3))))
    R["rms3d"] = math.sqrt(sum(e * e for e in errs) / len(errs))
    R["teo3d"] = sigma * R["dop"]["PDOP"]
    R["sigma"] = sigma
    R["rel"] = abs(R["rms3d"] - R["teo3d"]) / R["teo3d"]
    # geometria mala: solo los 4 satelites de menor elevacion... los 4 de mayor
    orden = sorted(vis, key=lambda t: t[1])
    peor = [s for s, _ in orden[:4]]
    mejor = [s for s, _ in orden[-4:]]
    R["pdop_peor"] = dop(geometria(peor, rx), rx)["PDOP"]
    R["pdop_mejor"] = dop(geometria(mejor, rx), rx)["PDOP"]
    R["tdop_s"] = R["dop"]["TDOP"] * sigma / C
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"SINTETICO: 24 satelites a {RS/1e3:.0f} km (6 planos, 55 grados), receptor 40 N 0 E, mascara 10 grados, sigma = 3 m")
    print(f"Satelites visibles = {R['n_vis']} ; elevaciones = {R['elev']}")
    print(f"Error sin ruido = {R['err_sin_ruido']:.2e} m (posicion y c*dt)")
    d = R["dop"]
    print(f"DOP: GDOP = {d['GDOP']:.2f} ; PDOP = {d['PDOP']:.2f} ; HDOP = {d['HDOP']:.2f} ; VDOP = {d['VDOP']:.2f} ; TDOP = {d['TDOP']:.2f}")
    print(f"Error 3D rms (400 ensayos) = {R['rms3d']:.2f} m ; teoria sigma*PDOP = {R['teo3d']:.2f} m ; diferencia = {100*R['rel']:.1f} %")
    print(f"PDOP con 4 satelites de menor elevacion = {R['pdop_peor']:.2f} ; con 4 de mayor elevacion = {R['pdop_mejor']:.2f}")
    assert R["err_sin_ruido"] < 1e-5 and R["rel"] < 0.1 and R["n_vis"] >= 4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
