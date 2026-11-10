#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C08: propagacion lineal de la covarianza orbital a la posicion en el cielo, contrastada con Monte Carlo.

Datos: el mismo asteroide SINTETICO de C07 (a = 1.8 au, e = 0.35, i = 7 deg) con 41 observaciones sinteticas (ruido 0.5 arcsec, semilla 20261109). Tierra circular de 1 au; constante de Gauss
no consultada. Modelo: covarianza formal C = (J^T W J)^-1 de los seis elementos; para cada fecha futura t, la covarianza del cielo (longitud*cos b, latitud) es G C G^T con G = d(cielo)/d(elementos)
por diferencias centrales; Monte Carlo con 3000 muestras gaussianas de los elementos (factor de Cholesky) propagadas con el modelo no lineal. Unidades: arcsec, dia, rad.
Supuestos: ruido gaussiano independiente, modelo de dos cuerpos, sin perturbaciones; la covarianza es la formal. Validez: ilustrativa.
Tolerancia: en las cuatro fechas, semieje mayor lineal y Monte Carlo con 5 % (a 300 dias, 10 % y fraccion en 3 sigma); fraccion de muestras dentro de la elipse lineal de 3 sigma entre 0.97 y 1.0 (esperado 0.9889).
"""
import math, platform, random

# ---- Propagador kepleriano de dos cuerpos (biblioteca estandar). Unidades: au, dia, radian. Marco: eclíptico heliocéntrico. ----
K_GAUSS = 0.01720209895          # constante gravitacional de Gauss [au^1.5 / dia] (definicion historica; GM_sol = K^2 au^3/dia^2)
GM = K_GAUSS ** 2
TWO_PI = 2.0 * math.pi
AU_KM = 149597870.7              # km, valor exacto adoptado por la IAU en 2012

def kepler_E(M, e):
    """Resuelve E - e sin E = M por Newton (tolerancia 1e-14)."""
    M = math.fmod(M, TWO_PI)
    E = M if e < 0.8 else math.pi
    for _ in range(60):
        d = (E - e * math.sin(E) - M) / (1.0 - e * math.cos(E))
        E -= d
        if abs(d) < 1e-14:
            break
    return E

def rot3(Om, i, w, v):
    """Rota del plano orbital al ecliptico (Rz(Om) Rx(i) Rz(w))."""
    cw, sw, ci, si, cO, sO = math.cos(w), math.sin(w), math.cos(i), math.sin(i), math.cos(Om), math.sin(Om)
    x1, y1 = cw * v[0] - sw * v[1], sw * v[0] + cw * v[1]
    x2, y2, z2 = x1, ci * y1, si * y1
    return (cO * x2 - sO * y2, sO * x2 + cO * y2, z2)

def pos_kepler(el, t):
    """Posicion heliocentrica [au] en el dia t (medido desde la epoca) para elementos el = (a, e, i, Om, w, M0) en radianes."""
    a, e, i, Om, w, M0 = el
    n = K_GAUSS / a ** 1.5
    E = kepler_E(M0 + n * t, e)
    xp, yp = a * (math.cos(E) - e), a * math.sqrt(1.0 - e * e) * math.sin(E)
    return rot3(Om, i, w, (xp, yp))

def tierra(t, L0=1.7):
    """Tierra en orbita circular de 1 au en el plano eclíptico (aproximacion didactica); periodo 365.2568983 d; L0 en rad."""
    L = L0 + TWO_PI * t / 365.2568983
    return (math.cos(L), math.sin(L), 0.0)

def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def norm(a): return math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
def lon_lat(v):
    """Longitud y latitud eclípticas [rad] de un vector geocentrico."""
    return math.atan2(v[1], v[0]) % TWO_PI, math.asin(v[2] / norm(v))


# ---- Ajuste de elementos por Levenberg-Marquardt a observaciones (longitud, latitud) eclípticas geocentricas (biblioteca estandar) ----
def observables(el, ts, L0=1.7):
    return [lon_lat(sub(pos_kepler(el, t), tierra(t, L0))) for t in ts]

def resid(el, obs, ts):
    """obs - modelo; la longitud se multiplica por cos(latitud). Unidades: radian."""
    r = []
    for (l, b), (lo, bo) in zip(observables(el, ts), obs):
        dl = (lo - l + math.pi) % TWO_PI - math.pi
        r += [dl * math.cos(bo), bo - b]
    return r

def jacobiano(el, obs, ts, h=1e-6):
    """d(modelo)/d(elemento) por diferencias centrales; filas = observaciones, columnas = 6 elementos."""
    cols = []
    for k in range(6):
        ep, em = list(el), list(el)
        ep[k] += h; em[k] -= h
        rp, rm = resid(ep, obs, ts), resid(em, obs, ts)
        cols.append([-(a - b) / (2 * h) for a, b in zip(rp, rm)])
    return [[cols[k][j] for k in range(6)] for j in range(len(cols[0]))]

def resolver(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][k] * x[k] for k in range(i + 1, n))) / M[i][i]
    return x

def inversa(A):
    n = len(A)
    cols = [resolver(A, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def ajustar(el0, obs, ts, sig, itmax=200):
    """Levenberg-Marquardt. sig: desviacion de cada medida [rad]. Devuelve (elementos, chi2, covarianza, iteraciones)."""
    el = list(el0); lam = 1e-3
    r = resid(el, obs, ts); chi = sum(x * x for x in r) / sig ** 2
    it = 0
    for it in range(1, itmax + 1):
        J = jacobiano(el, obs, ts)
        A = [[sum(J[k][i] * J[k][j] for k in range(len(r))) / sig ** 2 for j in range(6)] for i in range(6)]
        g = [sum(J[k][i] * r[k] for k in range(len(r))) / sig ** 2 for i in range(6)]
        mejora = False
        for _ in range(30):
            Al = [[A[i][j] * (1 + lam if i == j else 1.0) for j in range(6)] for i in range(6)]
            d = resolver(Al, g)
            nuevo = [el[i] + d[i] for i in range(6)]
            if not (0.0 <= nuevo[1] < 0.99 and nuevo[0] > 0.1):
                lam *= 10; continue
            rn = resid(nuevo, obs, ts); cn = sum(x * x for x in rn) / sig ** 2
            if cn < chi:
                dchi = chi - cn
                el, r, chi = nuevo, rn, cn
                lam = max(lam / 10, 1e-12); mejora = True
                break
            lam *= 10
        if not mejora or dchi < 1e-10 * max(chi, 1e-30) + 1e-18:
            break
    J = jacobiano(el, obs, ts)
    A = [[sum(J[k][i] * J[k][j] for k in range(len(r))) / sig ** 2 for j in range(6)] for i in range(6)]
    return el, chi, inversa(A), it


D = math.radians
VERDAD = (1.8, 0.35, D(7), D(40), D(120), D(60))
GUESS = (1.88, 0.39, D(8), D(42), D(123), D(57))
SIG = 0.5 / 206264.80624709636
AS = 206264.80624709636

def cielo(el, t):
    l, b = lon_lat(sub(pos_kepler(el, t), tierra(t)))
    return l, b

def desplazamiento(el, el_nom, t):
    l, b = cielo(el, t); ln, bn = cielo(el_nom, t)
    dl = (l - ln + math.pi) % TWO_PI - math.pi
    return dl * math.cos(bn) * AS, (b - bn) * AS

def cholesky(C):
    n = len(C); L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = C[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            L[i][j] = math.sqrt(s) if i == j else s / L[j][j]
    return L

def eig2(S):
    a, b, c = S[0][0], S[0][1], S[1][1]
    m, d = 0.5 * (a + c), math.sqrt(0.25 * (a - c) ** 2 + b * b)
    return m + d, m - d

def calcular():
    ts = [6 * k for k in range(41)]
    limpio = observables(VERDAD, ts)
    rng = random.Random(20261109)
    obs = [(l + rng.gauss(0, SIG) / math.cos(b), b + rng.gauss(0, SIG)) for l, b in limpio]
    el, chi, C, it = ajustar(GUESS, obs, ts, SIG)
    L = cholesky(C)
    N = 3000
    muestras = []
    for _ in range(N):
        z = [rng.gauss(0, 1) for _ in range(6)]
        muestras.append([el[i] + sum(L[i][k] * z[k] for k in range(i + 1)) for i in range(6)])
    filas = []
    for t in (300, 600, 1200, 2400):
        G = [[0.0] * 6 for _ in range(2)]
        for k in range(6):
            h = 1e-6
            ep, em = list(el), list(el)
            ep[k] += h; em[k] -= h
            dp, dm = desplazamiento(ep, el, t), desplazamiento(em, el, t)
            for j in range(2):
                G[j][k] = (dp[j] - dm[j]) / (2 * h)
        S = [[sum(G[a][i] * C[i][j] * G[b][j] for i in range(6) for j in range(6)) for b in range(2)] for a in range(2)]
        l1, l2 = eig2(S)
        pts = [desplazamiento(m, el, t) for m in muestras]
        mx = sum(p[0] for p in pts) / N; my = sum(p[1] for p in pts) / N
        Sm = [[sum((p[a] - (mx, my)[a]) * (p[b] - (mx, my)[b]) for p in pts) / (N - 1) for b in range(2)] for a in range(2)]
        m1, m2 = eig2(Sm)
        det = S[0][0] * S[1][1] - S[0][1] ** 2
        dentro = 0
        for p in pts:
            q = (S[1][1] * p[0] ** 2 - 2 * S[0][1] * p[0] * p[1] + S[0][0] * p[1] ** 2) / det
            dentro += q <= 9.0
        filas.append((t, math.sqrt(l1), math.sqrt(m1), math.sqrt(m1) / math.sqrt(l1), math.sqrt(l2), dentro / N))
    return {"filas": filas, "sa": math.sqrt(C[0][0]), "chi": chi, "esperado": 1 - math.exp(-4.5)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Elementos ajustados con 41 observaciones: sigma(a) = %.2e au ; chi2 = %.1f" % (r["sa"], r["chi"]))
    print("%6s %16s %16s %10s %14s %18s" % ("t[d]", "sigma mayor lin", "sigma mayor MC", "MC/lin", "sigma menor", "dentro 3 sigma lin"))
    for t, sl, sm, q, smin, dentro in r["filas"]:
        print("%6d %14.2f\" %14.2f\" %10.3f %12.2f\" %18.4f" % (t, sl, sm, q, smin, dentro))
    print("Fraccion esperada dentro de la elipse de 3 sigma (2D, gaussiana) = %.4f" % r["esperado"])
    f300 = r["filas"][0]
    assert abs(f300[3] - 1) < 0.10
    assert 0.97 < f300[5] <= 1.0
    assert all(abs(f[3] - 1) < 0.05 for f in r["filas"])
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
