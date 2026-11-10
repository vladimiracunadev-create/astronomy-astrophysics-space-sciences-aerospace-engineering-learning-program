#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C05: distancia minima de interseccion orbital (MOID) con la orbita terrestre y criterio de objeto potencialmente peligroso.

Datos: cinco orbitas SINTETICAS. Criterio PHA (MOID <= 0.05 au y H <= 22) y definicion de MOID de la pagina NEO Groups de CNEOS/JPL (consultada el 2026-11-09). La orbita de la Tierra se aproxima
por una circunferencia de 1 au en el plano eclíptico (simplificacion didactica, no la orbita real).
Modelo: distancia entre la circunferencia terrestre (radio 1) y la elipse del asteroide d(f)^2 = (rho(f) - 1)^2 + z(f)^2, con rho el radio cilindrico y z la altura; minimo por barrido de 7200
anomalias verdaderas y refinamiento por seccion aurea. Unidades: au, radian. Marco: eclíptico heliocentrico.
Supuestos: orbitas keplerianas fijas; Tierra circular y coplanar con la eclíptica. Validez: ilustrativa; el MOID real usa las dos elipses y se calcula con mas cuidado.
Tolerancia: casos analiticos con 1e-6 au: (i) coplanar exterior MOID = q - 1, (ii) coplanar interior MOID = 1 - Q, (iii) circular inclinada MOID = |a - 1|.
"""
import math, platform

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


def punto(el, f):
    a, e, i, Om, w = el[0], el[1], el[2], el[3], el[4]
    r = a * (1 - e * e) / (1 + e * math.cos(f))
    return rot3(Om, i, w, (r * math.cos(f), r * math.sin(f)))

def dist(el, f):
    x, y, z = punto(el, f)
    return math.sqrt((math.hypot(x, y) - 1.0) ** 2 + z * z)

def moid(el, N=7200):
    ds = [dist(el, TWO_PI * k / N) for k in range(N)]
    mejores = sorted(range(N), key=lambda k: ds[k])[:6]
    mejor = min(ds)
    for k in mejores:
        lo, hi = TWO_PI * (k - 1) / N, TWO_PI * (k + 1) / N
        g = (math.sqrt(5) - 1) / 2
        c, d = hi - g * (hi - lo), lo + g * (hi - lo)
        for _ in range(80):
            if dist(el, c) < dist(el, d):
                hi = d
            else:
                lo = c
            c, d = hi - g * (hi - lo), lo + g * (hi - lo)
        mejor = min(mejor, dist(el, 0.5 * (lo + hi)))
    return mejor

D = math.radians
OBJ = [  # nombre, (a, e, i, Om, w), H
    ("SINT-A", (1.50, 0.28, D(0.0), D(0), D(0)), 21.0),     # coplanar exterior: q = 1.08
    ("SINT-B", (0.80, 0.10, D(0.0), D(0), D(0)), 23.0),     # coplanar interior: Q = 0.88
    ("SINT-C", (1.20, 0.00, D(30.0), D(40), D(0)), 20.0),   # circular inclinada: MOID = 0.2
    ("SINT-D", (1.50, 0.50, D(20.0), D(60), D(100)), 21.5), # cruza el plano; q = 0.75
    ("SINT-E", (1.80, 0.45, D(5.0), D(120), D(250)), 24.0), # q = 0.99, Q = 2.61
]

def calcular():
    filas = []
    for n, el, H in OBJ:
        m = moid(el + (0.0,))
        pha = (m <= 0.05) and (H <= 22.0)
        filas.append((n, el[0] * (1 - el[1]), el[0] * (1 + el[1]), math.degrees(el[2]), H, m, pha))
    return {"filas": filas, "moid_km": [f[5] * AU_KM for f in filas]}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%-7s %7s %7s %7s %6s %10s %10s %5s" % ("objeto", "q", "Q", "i[deg]", "H", "MOID[au]", "MOID[km]", "PHA"))
    for f, km in zip(r["filas"], r["moid_km"]):
        print("%-7s %7.3f %7.3f %7.1f %6.1f %10.6f %10.0f %5s" % (f[0], f[1], f[2], f[3], f[4], f[5], km, "si" if f[6] else "no"))
    A, B, C = r["filas"][0], r["filas"][1], r["filas"][2]
    assert abs(A[5] - (A[1] - 1.0)) < 1e-6
    assert abs(B[5] - (1.0 - B[2])) < 1e-6
    assert abs(C[5] - 0.2) < 1e-6
    print("Casos analiticos: coplanar exterior q-1 = %.6f ; coplanar interior 1-Q = %.6f ; circular inclinada |a-1| = 0.200000" % (A[1] - 1.0, 1.0 - B[2]))
    # estabilidad: duplicar la resolucion no cambia el resultado
    el = OBJ[3][1] + (0.0,)
    assert abs(moid(el, 3600) - moid(el, 14400)) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
