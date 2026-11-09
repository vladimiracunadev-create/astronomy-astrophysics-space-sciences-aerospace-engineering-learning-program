#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C17: cierre de fase, solucion de ganancias de antena y referencia de fase (semilla fija).

Datos: ninguno externo. Las 6 antenas, los errores de fase (gaussianos de 60 grados), el calibrador puntual de 1 Jy, el ruido de 0,03 Jy por parte y la deriva
atmosferica de 0,5 grados por raiz de segundo (marcha aleatoria) son SINTETICOS (semilla 20261109).
Modelo: V_ij = g_i g_j* S + ruido, g_i = exp(i phi_i). Fase de cierre arg(V_ij V_jk V_ki) = 0 para un calibrador puntual en el centro, independiente de las g_i.
Solucion por iteracion (g_i = suma_j V_ij g_j / suma_j |g_j|^2, con amortiguacion). Referencia de fase: interpolacion lineal entre dos
calibradores separados T segundos; la marcha aleatoria deja un residuo cuadratico medio sigma^2 T/6 (puente browniano).
Supuestos: fuente puntual en el centro de fase, ganancias constantes en la integracion. Validez: orientativa.
Tolerancia: cierre sin ruido < 1e-12 rad; fases recuperadas dentro de 3 grados; residuo simulado dentro del 8 % de sigma sqrt(T/6).
"""
from __future__ import annotations
import cmath, math, platform, random

def calc():
    rng = random.Random(20261109)
    n, S, sg = 6, 1.0, 0.03
    ph = [math.radians(rng.gauss(0, 60)) for _ in range(n)]
    g = [cmath.exp(1j * p) for p in ph]
    V0 = [[g[i] * g[j].conjugate() * S for j in range(n)] for i in range(n)]
    cierre = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                c = cmath.phase(V0[i][j] * V0[j][k] * V0[k][i])
                cierre = max(cierre, abs(c))
    V = [[V0[i][j] + complex(rng.gauss(0, sg), rng.gauss(0, sg)) if i != j else 0j for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            V[j][i] = V[i][j].conjugate()
    # ruido de la fase de cierre (con ruido)
    cn = []
    for i, j, k in ((0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)):
        cn.append(math.degrees(cmath.phase(V[i][j] * V[j][k] * V[k][i])))
    est = [1 + 0j] * n
    for _ in range(200):
        nuevo = []
        for i in range(n):
            num = sum(V[i][j] * est[j] for j in range(n) if j != i)
            den = sum(abs(est[j]) ** 2 for j in range(n) if j != i) * S
            nuevo.append(num / den)
        est = [0.5 * a + 0.5 * b for a, b in zip(est, nuevo)]
    ref = cmath.phase(est[0])
    rec = [math.degrees(cmath.phase(e * cmath.exp(-1j * ref))) for e in est]
    ver = [math.degrees(p - ph[0]) for p in ph]
    errs = []
    for a, b in zip(rec, ver):
        d = (a - b + 180) % 360 - 180
        errs.append(d)
    # referencia de fase
    sig = 0.5
    filas = []
    for T in (30, 60, 120, 240):
        acum, cnt = 0.0, 0
        for _ in range(1500):
            w = [0.0]
            for _ in range(T):
                w.append(w[-1] + rng.gauss(0, sig))
            for s in range(1, T):
                interp = w[0] + (w[T] - w[0]) * s / T
                acum += (w[s] - interp) ** 2
                cnt += 1
        filas.append((T, math.sqrt(acum / cnt), sig * math.sqrt(T / 6)))
    return dict(cierre=cierre, cn=cn, rec=rec, ver=ver, errs=errs, filas=filas, sg=sg)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"cierre de fase sin ruido: maximo |c| = {r['cierre']:.2e} rad")
    print("cierre de fase con ruido (grados), triangulos 012 123 234 345: " + " ".join(f"{c:.2f}" for c in r["cn"]))
    print(f"{'antena':>7} {'fase verdadera [grados]':>24} {'recuperada [grados]':>20} {'error':>7}")
    for i, (a, b, e) in enumerate(zip(r["ver"], r["rec"], r["errs"])):
        print(f"{i:7d} {a:24.2f} {b:20.2f} {e:7.2f}")
    print(f"{'T [s]':>6} {'residuo simulado [grados]':>26} {'sigma sqrt(T/6)':>16}")
    for T, a, b in r["filas"]:
        print(f"{T:6d} {a:26.3f} {b:16.3f}")
    assert r["cierre"] < 1e-12
    assert max(abs(e) for e in r["errs"]) < 3.0
    for T, a, b in r["filas"]:
        assert abs(a / b - 1) < 0.08
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
