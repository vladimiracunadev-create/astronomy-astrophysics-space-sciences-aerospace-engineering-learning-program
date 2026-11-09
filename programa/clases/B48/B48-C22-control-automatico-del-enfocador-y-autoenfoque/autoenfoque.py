"""Autoenfoque: curva en V, ajuste cuadrático de HFD^2 y mínimo de enfoque.

Datos: telescopio f/8, 5 µm por paso del enfocador, HFD mínimo 3,0 µm y mejor foco en el paso 1234; ruido de
0,15 µm en cada HFD: ILUSTRATIVOS (no son de ningún instrumento). No se consultó ninguna fuente externa.
Modelo: el diámetro de desenfoque geométrico es dz / N (N = número f); HFD^2 = h0^2 + (dz / N)^2 con dz = 5 µm * (x - x0),
que es una parábola en x; el mínimo se obtiene del ajuste cuadrático por mínimos cuadrados (ecuaciones normales).
Segunda vía: sección áurea sobre la función HFD(x) sin ruido.
Supuestos: pasos exactos, sin holgura mecánica, sin deriva térmica durante la serie; el HFD se toma proporcional
al diámetro geométrico con factor 1 (simplificación).
Tolerancia: sin ruido, 1e-6 pasos; con ruido, sesgo a menos de 4 errores estándar.
"""
import math
import random
import statistics

NF = 8.0
UM = 5.0
H0 = 3.0
X0 = 1234.0
SIGMA = 0.15
POS = [X0 + d for d in range(-400, 401, 100)]


def hfd(x):
    return math.sqrt(H0 ** 2 + (UM * (x - X0) / NF) ** 2)


def resolver3(A, b):
    n = 3
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def ajuste(xs, hs):
    u = [x - 1234.0 for x in xs]
    y = [h * h for h in hs]
    S = [sum(t ** k for t in u) for k in range(5)]
    T = [sum((t ** k) * yy for t, yy in zip(u, y)) for k in range(3)]
    c, b, a = resolver3([[S[0], S[1], S[2]], [S[1], S[2], S[3]], [S[2], S[3], S[4]]], T)
    return 1234.0 - b / (2 * a)


def aurea(a=900.0, b=1600.0):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    while b - a > 1e-9:
        if hfd(c) < hfd(d):
            b, d = d, c
            c = b - g * (b - a)
        else:
            a, c = c, d
            d = a + g * (b - a)
    return 0.5 * (a + b)


def calc():
    x_aj = ajuste(POS, [hfd(x) for x in POS])
    x_au = aurea()
    rng = random.Random(20261109)
    est = [ajuste(POS, [hfd(x) + rng.gauss(0, SIGMA) for x in POS]) for _ in range(4000)]
    m, s = statistics.fmean(est), statistics.stdev(est)
    return dict(x_aj=x_aj, x_au=x_au, m=m, s=s, se=s / math.sqrt(4000), hmin=hfd(X0), h_borde=hfd(POS[0]), k=UM / NF)


def main():
    Q = calc()
    print(f"Pendiente de desenfoque = {Q['k']:.4f} µm de HFD por paso; HFD en el borde = {Q['h_borde']:.3f} µm")
    print(f"Mínimo sin ruido: ajuste cuadrático {Q['x_aj']:.6f} | sección áurea {Q['x_au']:.6f}")
    print(f"Con ruido de {SIGMA} µm: media {Q['m']:.3f} pasos, desviación {Q['s']:.3f} pasos")
    assert abs(Q["x_aj"] - X0) < 1e-6 and abs(Q["x_au"] - X0) < 1e-4
    assert abs(Q["m"] - X0) < 4 * Q["se"]
    assert Q["s"] < 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
