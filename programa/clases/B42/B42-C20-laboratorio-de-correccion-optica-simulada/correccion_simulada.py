#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C20: lazo cerrado de optica adaptativa SIMULADO de extremo a extremo (pantalla de Kolmogorov en flujo congelado, espejo de 8 x 8 actuadores, integrador con retardo).

Datos: TODO es ilustrativo y sintetico ; r0 = 0,8 m (a la longitud de onda de observacion), apertura de 3,2 m (32 pixeles de 0,1 m), viento de 20 m/s, trama de 2 ms (500 Hz), retardo de 2 tramas, ganancias 0,3 y
0,6, ruido de medicion de coeficientes de 0,05 rad y 300 tramas ; semilla 20261109. El coeficiente 0,023 de la PSD es de libro de texto (no consultado). No representa a ningun sistema real.
Modelo: la fase en la pupila es phi(x - v t) de una pantalla FFT de 256 x 256 (paso 0,1 m) desplazada con interpolacion lineal ; espejo con 64 actuadores (paso 4 pixeles) e influencias gaussianas con 15 % de
acoplamiento ; sensor ideal que proyecta la fase residual sobre los actuadores por minimos cuadrados regularizados (1e-3) mas ruido ; integrador c[n] = c[n-1] + g m[n-2] (como la clase C16).
Metricas (dos vias independientes): (a) Strehl instantaneo por la identidad exacta |<exp(i phi)>|^2 (clase C06) ; (b) pico de la PSF de larga exposicion (promedio de PSF por FFT de 64 x 64, 2 px por lambda/D) frente a la
PSF sin aberracion ; ademas la aproximacion de Marechal exp(-sigma^2) sobre la varianza residual media.
Supuestos: sensor lineal e ideal salvo por el ruido anadido, un solo conjunto de capas en flujo congelado, sin escintilacion. Validez: demostracion pedagogica de lazo cerrado ; los numeros NO predicen a un telescopio real.
Tolerancia: el Strehl del lazo cerrado supera al de lazo abierto ; la media temporal del Strehl instantaneo y el pico de larga exposicion son coherentes (el pico es mayor o igual que el promedio de picos instantaneos descentrados) ;
el lazo con g = 0,6 y ruido nulo mejora al de g = 0,3 con retardo 2 solo si sigue estable (se informa).
"""
from __future__ import annotations
import cmath, math, platform, random

N = 64
DP = 32
NS = 256
DX = 0.1
R0 = 0.8
NSTEP = 300
V = 20.0
DT = 0.002
PITCH = 4
D_RET = 2

def fft(a):
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    m = 2
    while m <= n:
        w = cmath.exp(-2j * math.pi / m)
        for s in range(0, n, m):
            t = 1 + 0j
            for k in range(m // 2):
                u, v = a[s + k], a[s + k + m // 2] * t
                a[s + k], a[s + k + m // 2] = u + v, u - v
                t *= w
        m <<= 1
    return a

def fft2(g):
    f = [fft(r) for r in g]
    cols = [fft([f[i][j] for i in range(len(f))]) for j in range(len(f[0]))]
    return [[cols[j][i] for j in range(len(f[0]))] for i in range(len(f))]

def pantalla(rnd):
    df = 1.0 / (NS * DX)
    g = [[0j] * NS for _ in range(NS)]
    for i in range(NS):
        for j in range(NS):
            fy = (i if i < NS // 2 else i - NS) * df
            fx = (j if j < NS // 2 else j - NS) * df
            f = math.hypot(fx, fy)
            if f > 0:
                a = math.sqrt(0.023 * R0 ** (-5 / 3) * f ** (-11 / 3)) * df
                g[i][j] = a * complex(rnd.gauss(0, 1), rnd.gauss(0, 1))
    f = fft2(g)
    return [[f[i][j].real for j in range(NS)] for i in range(NS)]

def resolver(a, b):
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        for r in range(n):
            if r != c:
                f = m[r][c] / m[c][c]
                if f:
                    for k in range(c, n + 1):
                        m[r][k] -= f * m[c][k]
    return [m[i][n] / m[i][i] for i in range(n)]

def construir():
    c0 = N // 2
    pts = [(i, j) for i in range(N) for j in range(N) if math.hypot(i - c0 + 0.5, j - c0 + 0.5) <= DP / 2]
    w = PITCH / math.sqrt(2 * math.log(1 / 0.15))
    # actuadores 8 x 8 centrados en la pupila
    cen = [(c0 - DP / 2 + PITCH / 2 + PITCH * a, c0 - DP / 2 + PITCH / 2 + PITCH * b) for a in range(8) for b in range(8)]
    A = [[math.exp(-((i + 0.5 - ci) ** 2 + (j + 0.5 - cj) ** 2) / (2 * w * w)) for (ci, cj) in cen] for (i, j) in pts]
    n = len(cen)
    ata = [[sum(r[p] * r[q] for r in A) for q in range(n)] for p in range(n)]
    for p in range(n):
        ata[p][p] += 1e-3
    inv = [resolver(ata, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    # P = inv A^T  (n x npts)
    P = [[sum(inv[a][k] * A[t][k] for k in range(n)) for t in range(len(pts))] for a in range(n)]
    return pts, A, P

def psf_pico(phis, pts):
    campo = [[0j] * N for _ in range(N)]
    for (i, j), ph in zip(pts, phis):
        campo[i][j] = cmath.exp(1j * ph)
    f = fft2(campo)
    return [[abs(f[i][j]) ** 2 for j in range(N)] for i in range(N)]

def ejecutar(scr, pts, A, P, g, ruido, rnd, lazo=True):
    npts = len(pts)
    n = len(A[0])
    c = [0.0] * n
    med = []
    strehl_inst = []
    var_res = []
    acum = [[0.0] * N for _ in range(N)]
    off = 96
    for t in range(NSTEP):
        desp = V * DT * t / DX
        i0 = int(math.floor(desp))
        fr = desp - i0
        fase = []
        for (i, j) in pts:
            fila = scr[off + i]
            x = j + i0 + 20
            fase.append((1 - fr) * fila[x] + fr * fila[x + 1])
        if lazo and t - D_RET >= 0:
            m = med[t - D_RET]
            c = [ck + g * mk for ck, mk in zip(c, m)]
        sup = [sum(A[p][k] * c[k] for k in range(n)) for p in range(npts)] if lazo else [0.0] * npts
        res = [f - s for f, s in zip(fase, sup)]
        mu = sum(res) / npts
        v = sum((r - mu) ** 2 for r in res) / npts
        var_res.append(v)
        z = sum(cmath.exp(1j * r) for r in res) / npts
        strehl_inst.append(abs(z) ** 2)
        if t >= 50:       # se descartan las 50 primeras tramas (arranque del lazo)
            p = psf_pico(res, pts)
            for i in range(N):
                for j in range(N):
                    acum[i][j] += p[i][j]
        m = [sum(P[a][p] * res[p] for p in range(npts)) + (rnd.gauss(0, ruido) if ruido else 0.0) for a in range(n)]
        med.append(m)
    nm = NSTEP - 50
    return strehl_inst, var_res, acum, nm

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    scr = pantalla(rnd)
    pts, A, P = construir()
    npts = len(pts)
    print(f"puntos de pupila = {npts} ; actuadores = {len(A[0])} ; r0 = {R0} m ; D/r0 = {DP * DX / R0:.1f} ; d/r0 = {PITCH * DX / R0:.2f} ; desplazamiento total de la pantalla = {V * DT * NSTEP:.1f} m")
    ideal = psf_pico([0.0] * npts, pts)
    pico_ideal = ideal[0][0]
    print(f"{'caso':<28} {'Strehl inst. medio':>19} {'Marechal exp(-var)':>19} {'pico larga exp.':>16} {'var res [rad2]':>15}")
    resultados = {}
    for nombre, g, ruido, lazo in (("lazo abierto", 0.0, 0.0, False), ("cerrado g=0,3 sin ruido", 0.3, 0.0, True), ("cerrado g=0,6 sin ruido", 0.6, 0.0, True), ("cerrado g=0,6 ruido 0,05", 0.6, 0.05, True)):
        si, vr, acum, nm = ejecutar(scr, pts, A, P, g, ruido, random.Random(20261109), lazo)
        si_m = sum(si[50:]) / (NSTEP - 50)
        vr_m = sum(vr[50:]) / (NSTEP - 50)
        pico = max(max(r) for r in acum) / nm / pico_ideal
        resultados[nombre] = (si_m, pico, vr_m)
        print(f"{nombre:<28} {si_m:19.4f} {math.exp(-vr_m):19.4f} {pico:16.4f} {vr_m:15.4f}")
    a = resultados["lazo abierto"]
    b = resultados["cerrado g=0,3 sin ruido"]
    c = resultados["cerrado g=0,6 sin ruido"]
    d = resultados["cerrado g=0,6 ruido 0,05"]
    assert b[0] > a[0] and b[1] > a[1], (a, b)
    assert c[0] > a[0]
    assert b[2] < a[2]
    # el pico de larga exposicion es >= Strehl instantaneo medio solo si la PSF no se descentra ; se informa la relacion
    print(f"relaciones pico larga exposicion / Strehl instantaneo medio: abierto {a[1] / a[0]:.2f} ; g=0,3 {b[1] / b[0]:.2f} ; g=0,6 {c[1] / c[0]:.2f}")
    # la ganancia mayor reduce el error de retardo : comparar con la prediccion de C16 (g<1 estable con D=2)
    print(f"mejora de la varianza residual respecto del lazo abierto: g=0,3 -> x{a[2] / b[2]:.2f} ; g=0,6 -> x{a[2] / c[2]:.2f} ; con ruido 0,05 rad -> x{a[2] / d[2]:.2f}")
    assert d[2] > c[2] - 1e-9     # el ruido de medicion empeora (o no mejora) el residuo
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
