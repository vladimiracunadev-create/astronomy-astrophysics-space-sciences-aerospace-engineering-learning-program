#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C07: determinacion de la orbita de un asteroide sintetico por minimos cuadrados (Levenberg-Marquardt) a observaciones sinteticas.

Datos: asteroide SINTETICO con a = 1.8 au, e = 0.35, i = 7 deg, Omega = 40 deg, omega = 120 deg, M0 = 60 deg a la epoca t = 0. 41 observaciones (longitud y latitud eclipticas geocentricas)
cada 6 dias, con ruido gaussiano de 0.5 arcsec (semilla 20261109). La Tierra es una orbita circular de 1 au en el plano de la eclíptica (simplificacion didactica). Constante de Gauss no consultada.
Modelo: elementos keplerianos (a, e, i, Omega, omega, M0) -> posicion heliocentrica -> vector geocentrico -> (longitud, latitud). Ajuste de seis parametros con diferencias centrales y
amortiguamiento; covarianza (J^T W J)^-1. Unidades: au, radian, dia. Marco: eclíptico.
Supuestos: dos cuerpos, sin perturbaciones, sin aberracion ni retardo de luz, ruido gaussiano independiente. Validez: ilustrativa; no es un determinador de orbitas operativo.
Tolerancia: sin ruido, elementos recuperados con 1e-8 (au o rad); con ruido, chi2 por grado de libertad entre 0.6 y 1.5 y cada elemento dentro de 4 sigma formales.
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
NOMBRES = ["a [au]", "e", "i [rad]", "Omega [rad]", "omega [rad]", "M0 [rad]"]

def calcular():
    ts = [6 * k for k in range(41)]
    limpio = observables(VERDAD, ts)
    el0, chi0, _, it0 = ajustar(GUESS, limpio, ts, SIG)
    err0 = max(abs(x - y) for x, y in zip(el0, VERDAD))
    rng = random.Random(20261109)
    obs = [(l + rng.gauss(0, SIG) / math.cos(b), b + rng.gauss(0, SIG)) for l, b in limpio]
    arcos = []
    for n in (10, 16, 24, 41):
        el, chi, cov, it = ajustar(GUESS, obs[:n], ts[:n], SIG)
        sd = [math.sqrt(cov[i][i]) for i in range(6)]
        arcos.append((n, ts[n - 1], it, chi, 2 * n - 6, el, sd))
    return {"err0": err0, "chi0": chi0, "it0": it0, "arcos": arcos}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Sin ruido: iteraciones = %d ; chi2 final = %.2e ; error maximo de elementos = %.2e" % (r["it0"], r["chi0"], r["err0"]))
    print("%4s %7s %5s %9s %5s %12s %12s %12s" % ("n", "arco[d]", "iter", "chi2", "gl", "sigma(a)[au]", "sigma(e)", "sigma(i)[rad]"))
    for n, arco, it, chi, gl, el, sd in r["arcos"]:
        print("%4d %7d %5d %9.2f %5d %12.2e %12.2e %12.2e" % (n, arco, it, chi, gl, sd[0], sd[1], sd[2]))
    n, arco, it, chi, gl, el, sd = r["arcos"][-1]
    print("Arco completo (41 observaciones): elementos ajustados frente a la verdad sintetica")
    for k in range(6):
        print("  %-12s ajuste = %.7f ; verdad = %.7f ; diferencia = %+.2e = %+.2f sigma" % (NOMBRES[k], el[k], VERDAD[k], el[k] - VERDAD[k], (el[k] - VERDAD[k]) / sd[k]))
    assert r["err0"] < 1e-8
    assert 0.6 < chi / gl < 1.5
    assert all(abs(el[k] - VERDAD[k]) < 4 * sd[k] for k in range(6))
    sa = [x[6][0] for x in r["arcos"]]
    assert all(sa[i] > sa[i + 1] for i in range(len(sa) - 1))
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
