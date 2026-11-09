#!/usr/bin/env python3
"""B53-C07: altimetria SINTETICA con ajuste por cruces. Unidades m. Terreno z = 500 sin(2 pi x/20e3) cos(2 pi y/20e3).
Pasadas verticales (x fija) y horizontales (y fija), muestras cada 1 km, interpolacion lineal. Semilla 20261109.
Restriccion: suma de sesgos = 0. Tolerancia: RMS final < 2*sqrt(2)*sigma."""
import math, platform, random

C_LUZ = 299792458.0
SIG, SIG_B = 1.0, 20.0
L = 20000.0

def terreno(x, y):
    return 500 * math.sin(2 * math.pi * x / L) * math.cos(2 * math.pi * y / L)

def muestrear(f, t_cruce):
    h = 1000.0
    i = int(t_cruce // h)
    a, b = f(i * h), f((i + 1) * h)
    return a + (b - a) * (t_cruce - i * h) / h

def resolver(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x

def compute():
    rng = random.Random(20261109)
    pos = [2000.0 * (k + 1) for k in range(8)]
    b = [rng.gauss(0, SIG_B) for _ in range(16)]  # 0..7 verticales, 8..15 horizontales
    # cada muestra de cada pasada lleva ruido; se guardan muestras por pasada
    mv = [[terreno(pos[i], k * 1000.0) + b[i] + rng.gauss(0, SIG) for k in range(21)] for i in range(8)]
    mh = [[terreno(k * 1000.0, pos[j]) + b[8 + j] + rng.gauss(0, SIG) for k in range(21)] for j in range(8)]
    d, idx = [], []
    for i in range(8):
        for j in range(8):
            zv = muestrear(lambda t, i=i: mv[i][int(round(t / 1000.0))], pos[j])
            zh = muestrear(lambda t, j=j: mh[j][int(round(t / 1000.0))], pos[i])
            d.append(zv - zh); idx.append((i, 8 + j))
    n = 16
    ata = [[0.0] * (n + 1) for _ in range(n + 1)]
    atb = [0.0] * (n + 1)
    for (p, q), y in zip(idx, d):
        ata[p][p] += 1; ata[q][q] += 1; ata[p][q] -= 1; ata[q][p] -= 1
        atb[p] += y; atb[q] -= y
    for k in range(n):
        ata[k][n] = ata[n][k] = 1.0
    sol = resolver(ata, atb)[:n]
    rms = lambda v: math.sqrt(sum(e * e for e in v) / len(v))
    despues = [y - (sol[p] - sol[q]) for (p, q), y in zip(idx, d)]
    media_b = sum(b) / n
    err_b = [sol[k] - (b[k] - media_b) for k in range(n)]
    return dict(ncross=len(d), rms_before=rms(d), rms_after=rms(despues), rms_b=rms(err_b),
                ruido_cruce=math.sqrt(2) * SIG, dr_1ns=C_LUZ * 1e-9 / 2, dr_half=C_LUZ * 0.5e-9 / 2)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"1 ns de tiempo de vuelo = {r['dr_1ns']:.5f} m de alcance")
    print(f"cruces: {r['ncross']} ; RMS de discrepancia antes = {r['rms_before']:.3f} m ; despues = {r['rms_after']:.3f} m")
    print(f"error RMS de los sesgos estimados = {r['rms_b']:.3f} m ; ruido esperado por cruce = {r['ruido_cruce']:.3f} m")
    assert r["rms_after"] < 2 * r["ruido_cruce"] and r["rms_after"] < r["rms_before"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
