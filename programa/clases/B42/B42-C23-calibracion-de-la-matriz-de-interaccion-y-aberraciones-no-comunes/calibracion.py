#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C23: calibracion de la matriz de interaccion por empuje-tiron y aberraciones no comunes (NCPA) corregidas por nitidez de imagen.

Datos: TODO es sintetico e ILUSTRATIVO ; espejo de 6 x 6 actuadores gaussianos con 15 % de acoplamiento sobre una red de 11 x 11 nodos (10 x 10 subaperturas, pendientes de Fried como en la clase C22),
amplitudes de empuje de 0,05 a 0,8 rad, ruido de medicion de pendiente de 0,02 rad, NCPA de 0,12 rad rms de desenfoque y 0,08 y -0,05 rad rms de astigmatismo y pupila de 24 pixeles ; semilla 20261109.
Modelo: M = S A (pendientes por unidad de comando). Calibracion: para cada actuador se mide (s(+a) - s(-a)) / (2a) con ruido independiente ; M_est = M + E, E con desviacion sqrt(2) sigma/(2a) por elemento.
Matriz de control C = (M^T M + eps I)^(-1) M^T. Los valores singulares de M se obtienen del metodo de Jacobi aplicado a M^T M (via independiente de la inversa). NCPA: la fase en el camino de ciencia es phi = phi_AO + phi_nc donde
el sensor solo ve phi_AO ; se maximiza el pico de la PSF, S(c) = |<exp(i (phi_nc + c . modos))>|^2, con busqueda de seccion aurea por coordenadas sobre 3 modos (identidad exacta del pico, clase C06).
Supuestos: respuesta lineal, sin histeresis, camino comun perfecto, metrica con ruido opcional. Validez: ilustrativa de la logica de calibracion.
Tolerancia: error relativo del comando reconstruido proporcional a 1/a (pendiente log-log -1 a 0,25 en el tramo de amplitudes 1,6 a 6,4 rad, donde el error ya no satura) ; autovalores de Jacobi con residuo de ortogonalidad < 1e-9 y suma = traza a 1e-9 ; coeficientes NCPA recuperados a 1e-3 rad sin ruido.
"""
from __future__ import annotations
import math, platform, random

M = 11
NS = M - 1
NA = 6

def idx(i, j):
    return i * M + j

def operador_s():
    S = []
    for i in range(NS):
        for j in range(NS):
            f = [0.0] * (M * M)
            f[idx(i, j + 1)] += 0.5; f[idx(i, j)] -= 0.5; f[idx(i + 1, j + 1)] += 0.5; f[idx(i + 1, j)] -= 0.5
            S.append(f)
    for i in range(NS):
        for j in range(NS):
            f = [0.0] * (M * M)
            f[idx(i + 1, j)] += 0.5; f[idx(i, j)] -= 0.5; f[idx(i + 1, j + 1)] += 0.5; f[idx(i, j + 1)] -= 0.5
            S.append(f)
    return S

def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(r, c)) for c in bt] for r in a]

def transp(a):
    return [list(r) for r in zip(*a)]

def inversa(a):
    n = len(a)
    m = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        piv = m[c][c]
        m[c] = [v / piv for v in m[c]]
        for r in range(n):
            if r != c and m[r][c] != 0.0:
                f = m[r][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [row[n:] for row in m]

def jacobi(a, tol=1e-14):
    n = len(a)
    a = [r[:] for r in a]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(60):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
                c, s = math.cos(th), math.sin(th)
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p], v[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    return [a[i][i] for i in range(n)], v

def secc_aurea(f, a, b, it=60):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(it):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a); fd = f(d)
    return 0.5 * (a + b)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    S = operador_s()
    # espejo: actuadores en nodos pares
    w = 2.0 / math.sqrt(2 * math.log(1 / 0.15))
    cen = [(2.0 * a, 2.0 * b) for a in range(NA) for b in range(NA)]
    A = [[math.exp(-((i - ci) ** 2 + (j - cj) ** 2) / (2 * w * w)) for (ci, cj) in cen] for i in range(M) for j in range(M)]
    Mi = matmul(S, A)
    n = NA * NA
    G = matmul(transp(Mi), Mi)
    traza = sum(G[i][i] for i in range(n))
    lam, V = jacobi(G)
    ort = max(abs(sum(V[k][p] * V[k][q] for k in range(n)) - (1.0 if p == q else 0.0)) for p in range(n) for q in range(n))
    lam_s = sorted(lam, reverse=True)
    print(f"matriz de interaccion {len(Mi)} x {n} ; suma de autovalores = {sum(lam):.6f} ; traza de M^T M = {traza:.6f} ; ortogonalidad de Jacobi = {ort:.1e}")
    assert abs(sum(lam) - traza) < 1e-9 * traza and ort < 1e-9
    sv = [math.sqrt(max(l, 0.0)) for l in lam_s]
    print(f"valores singulares: maximo = {sv[0]:.4f} ; minimo = {sv[-1]:.2e} ; los 3 menores = {', '.join(f'{x:.2e}' for x in sv[-3:])} ; cociente = {sv[0] / max(sv[-1], 1e-300):.2e}")
    n_debiles = sum(1 for x in sv if x < 1e-3 * sv[0])
    print(f"modos de control con valor singular < 1e-3 del maximo = {n_debiles} (en este modelo ninguno es exactamente invisible: el piston y el tablero se ven poco, no nada)")
    eps = 1e-3
    Cinv = inversa([[G[i][j] + (eps if i == j else 0.0) for j in range(n)] for i in range(n)])
    # calibracion por empuje-tiron
    sigma = 0.02
    c_true = [rnd.gauss(0, 1) for _ in range(n)]
    # quitar la parte no observable (modos con valor singular casi nulo) del comando de prueba
    c_obs = [sum(V[k][q] * c_true[k] for k in range(n)) for q in range(n)]
    c_obs = [c if lam[q] > 1e-3 * lam_s[0] else 0.0 for q, c in enumerate(c_obs)]
    c_true = [sum(V[k][q] * c_obs[q] for q in range(n)) for k in range(n)]
    s_ref = [sum(m * c for m, c in zip(r, c_true)) for r in Mi]
    nc = math.sqrt(sum(c * c for c in c_true))
    print(f"{'amplitud a [rad]':>17} {'error rel. del comando (MC 30)':>31} {'sigma_E por elemento':>21}")
    pts = []
    for a in (0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4):
        acum = 0.0
        for _ in range(30):
            E = [[rnd.gauss(0, math.sqrt(2) * sigma / (2 * a)) for _ in range(n)] for _ in range(len(Mi))]
            Me = [[Mi[i][j] + E[i][j] for j in range(n)] for i in range(len(Mi))]
            Ge = matmul(transp(Me), Me)
            for i in range(n):
                Ge[i][i] += eps
            Ce = matmul(inversa(Ge), transp(Me))
            c_est = [sum(cr * s for cr, s in zip(r, s_ref)) for r in Ce]
            acum += math.sqrt(sum((x - y) ** 2 for x, y in zip(c_est, c_true))) / nc
        e = acum / 30
        if a >= 1.6:       # con amplitudes pequenas el error satura cerca de 1 (la matriz estimada es ruido)
            pts.append((math.log(a), math.log(e)))
        print(f"{a:17.2f} {e:31.5f} {math.sqrt(2) * sigma / (2 * a):21.4f}")
    mx = sum(x for x, _ in pts) / len(pts); my = sum(y for _, y in pts) / len(pts)
    pend = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    print(f"pendiente log-log error vs amplitud = {pend:.3f} (esperada -1: el error del empuje-tiron escala como sigma / a)")
    assert abs(pend + 1) < 0.25
    # NCPA : nitidez
    npix = 24
    c0 = npix / 2
    pts_p = [((i + 0.5 - c0) / (npix / 2), (j + 0.5 - c0) / (npix / 2)) for i in range(npix) for j in range(npix) if math.hypot((i + 0.5 - c0) / (npix / 2), (j + 0.5 - c0) / (npix / 2)) <= 1]
    def modos(x, y):
        r = math.hypot(x, y); t = math.atan2(y, x)
        return (math.sqrt(3) * (2 * r * r - 1), math.sqrt(6) * r * r * math.cos(2 * t), math.sqrt(6) * r * r * math.sin(2 * t))
    mod = [modos(x, y) for x, y in pts_p]
    nc_true = (0.12, 0.08, -0.05)
    def strehl(c, ruido=0.0):
        z = sum(complex(math.cos(sum((nc_true[k] + c[k]) * m[k] for k in range(3))), math.sin(sum((nc_true[k] + c[k]) * m[k] for k in range(3)))) for m in mod) / len(mod)
        return abs(z) ** 2 + (rnd.gauss(0, ruido) if ruido else 0.0)
    s0 = strehl((0, 0, 0))
    print(f"NCPA: rms total = {math.sqrt(sum(v * v for v in nc_true)):.4f} rad ; Strehl sin corregir = {s0:.5f} ; Marechal exp(-sigma^2) = {math.exp(-sum(v * v for v in nc_true)):.5f}")
    c = [0.0, 0.0, 0.0]
    for ronda in range(4):
        for k in range(3):
            def f(x, k=k):
                cc = c[:]; cc[k] = x
                return strehl(cc)
            c[k] = secc_aurea(f, -0.5, 0.5)
    print(f"coeficientes recuperados (nitidez) = ({c[0]:+.5f}, {c[1]:+.5f}, {c[2]:+.5f}) ; verdaderos con signo cambiado = ({-nc_true[0]:+.5f}, {-nc_true[1]:+.5f}, {-nc_true[2]:+.5f})")
    s1 = strehl(c)
    print(f"Strehl tras la nitidez = {s1:.6f}")
    assert all(abs(c[k] + nc_true[k]) < 1e-3 for k in range(3)) and s1 > 0.9999
    # con ruido en la metrica
    c2 = [0.0, 0.0, 0.0]
    rr = random.Random(20261109)
    for ronda in range(2):
        for k in range(3):
            def f(x, k=k):
                cc = c2[:]; cc[k] = x
                return strehl(cc, 0.003)
            c2[k] = secc_aurea(f, -0.5, 0.5, it=14)
    err = math.sqrt(sum((c2[k] + nc_true[k]) ** 2 for k in range(3)))
    print(f"con ruido de 0,003 en la metrica y 14 iteraciones: error de los coeficientes = {err:.4f} rad ; Strehl residual = {strehl(c2):.5f}")
    assert err < 0.1 and strehl(c2) > s0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
