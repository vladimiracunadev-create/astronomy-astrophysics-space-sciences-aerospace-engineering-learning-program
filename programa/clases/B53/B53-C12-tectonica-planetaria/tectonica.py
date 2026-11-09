#!/usr/bin/env python3
"""B53-C12: flexion de una placa elastica ILUSTRATIVA y contraccion global SINTETICA. SI.
D w(4) + k w = P delta(x), k = rho g; T = 20 km, E = 1e11 Pa, nu = 0.25, rho = 3300, g = 3.71, P = 1e11 N/m.
Dominio +-8 alfa, 40 puntos por alfa, w = 0 en los extremos. Tolerancia: error maximo < 1 % de w0."""
import math, platform

T, E, NU, RHO, G, P = 20e3, 1.0e11, 0.25, 3300.0, 3.71, 1.0e11
D = E * T ** 3 / (12 * (1 - NU ** 2))
K = RHO * G
ALFA = (4 * D / K) ** 0.25

def w_ana(x):
    a = abs(x) / ALFA
    return P * ALFA ** 3 / (8 * D) * math.exp(-a) * (math.cos(a) + math.sin(a))

def compute():
    h = ALFA / 40
    n = 641
    mid = n // 2
    A = [[0.0] * 5 for _ in range(n)]
    b = [0.0] * n
    c4 = D / h ** 4
    for i in range(n):
        if i < 2 or i > n - 3:
            A[i][2] = 1.0
            continue
        A[i][0], A[i][1], A[i][2], A[i][3], A[i][4] = c4, -4 * c4, 6 * c4 + K, -4 * c4, c4
    b[mid] = P / h
    # eliminacion hacia adelante
    for i in range(n):
        for r in range(i + 1, min(i + 3, n)):
            col = i - r + 2
            f = A[r][col] / A[i][2] if A[r][col] != 0 else 0.0
            if f == 0.0:
                continue
            for dj in range(0, 3):
                j = i + dj
                if j < n and 0 <= j - r + 2 < 5:
                    A[r][j - r + 2] -= f * A[i][dj + 2]
            b[r] -= f * b[i]
    w = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = b[i]
        for dj in (1, 2):
            if i + dj < n:
                s -= A[i][dj + 2] * w[i + dj]
        w[i] = s / A[i][2]
    w0 = w[mid]
    err = max(abs(w[i] - w_ana((i - mid) * h)) for i in range(n)) / w0
    imin = min(range(mid, n), key=lambda i: w[i])
    xb = (imin - mid) * h
    R_, s_, l_, N_ = 2440e3, 1.0e3, 100e3, 300
    eps = N_ * s_ * l_ / (4 * math.pi * R_ ** 2)
    return dict(D=D, alfa_km=ALFA / 1e3, w0=w0, w0_ana=w_ana(0), xb=xb / 1e3, xb_ana=math.pi * ALFA / 1e3, err=err,
                eps=eps, dR=R_ * eps / 2 / 1e3, dR2=R_ * 2 * eps / 2 / 1e3, cociente=w_ana(math.pi * ALFA) / w_ana(0))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"D = {r['D']:.4e} N m ; alfa = {r['alfa_km']:.3f} km")
    print(f"w0: diferencias finitas {r['w0']:.3f} m ; analitica {r['w0_ana']:.3f} m ; error maximo relativo a w0 = {r['err']:.2e}")
    print(f"abombamiento periferico: x = {r['xb']:.1f} km (pi*alfa = {r['xb_ana']:.1f} km) ; w(pi alfa)/w0 = {r['cociente']:.4f}")
    print(f"contraccion: eps = {r['eps']:.3e} ; dR = {r['dR']:.3f} km")
    assert r["err"] < 0.01 and abs(r["xb"] - r["xb_ana"]) < 2.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
