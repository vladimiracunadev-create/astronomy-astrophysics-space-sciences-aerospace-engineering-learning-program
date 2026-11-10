#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C06: astrometria de un objeto menor con proyeccion gnomonica y constantes de placa.

Datos: campo SINTETICO centrado en (RA, Dec) = (150 deg, +20 deg) de 2048 x 2048 pixeles, escala verdadera 1.00 arcsec/pixel, rotacion 12 deg; 40 estrellas de referencia SINTETICAS con
posicion de catalogo con error de 0.02 arcsec y centroide con error de 0.10 pixel (semilla 20261109); un asteroide SINTETICO en el pixel (1500.3, 700.2). No se usa ningun catalogo real.
Modelo: proyeccion gnomonica (coordenadas estandar xi, eta) y modelo lineal de seis constantes de placa xi = a X + b Y + c ; eta = d X + e Y + f, con X, Y el pixel menos el centro (1024, 1024).
El formato de observaciones del MPC no se consulto (pagina no accesible, 403). Unidades: grados, arcsec, pixel. Marco: ecuatorial, equinoccio de la fecha del catalogo (no se especifica una epoca real).
Supuestos: sin distorsion optica, sin refraccion diferencial, sin movimiento propio ni paralaje. Validez: campo pequeno; ilustrativa.
Tolerancia: ida y vuelta pixel -> cielo -> pixel con 1e-9 pixel; ajuste sin ruido recupera escala y rotacion con 1e-9; RMS del residuo entre 0.7 y 1.2 veces el esperado.
"""
import math, platform, random

AS = 206264.80624709636  # arcsec por radian
A0, D0 = math.radians(150.0), math.radians(20.0)

def directa(a, d):
    c = math.sin(d) * math.sin(D0) + math.cos(d) * math.cos(D0) * math.cos(a - A0)
    return (math.cos(d) * math.sin(a - A0) / c, (math.sin(d) * math.cos(D0) - math.cos(d) * math.sin(D0) * math.cos(a - A0)) / c)

def inversa(xi, eta):
    rho = math.hypot(xi, eta)
    if rho == 0:
        return A0, D0
    c = math.atan(rho)
    d = math.asin(math.cos(c) * math.sin(D0) + eta * math.sin(c) * math.cos(D0) / rho)
    a = A0 + math.atan2(xi * math.sin(c), rho * math.cos(D0) * math.cos(c) - eta * math.sin(D0) * math.sin(c))
    return a % (2 * math.pi), d

def placa_verdadera(X, Y, escala=1.0, rot=12.0):
    s, th = escala / AS, math.radians(rot)
    return s * (math.cos(th) * X - math.sin(th) * Y), s * (math.sin(th) * X + math.cos(th) * Y)

def resolver3(A, b):
    n = len(b); M = [A[i][:] + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][k] * x[k] for k in range(i + 1, n))) / M[i][i]
    return x

def ajustar(XY, ST):
    """Minimos cuadrados de xi y eta frente a (X, Y, 1). Devuelve (a, b, c), (d, e, f)."""
    N = [[sum(p[i] * p[j] for p in [(x, y, 1.0) for x, y in XY]) for j in range(3)] for i in range(3)]
    out = []
    for k in (0, 1):
        rhs = [sum(p[i] * s[k] for p, s in zip([(x, y, 1.0) for x, y in XY], ST)) for i in range(3)]
        out.append(resolver3(N, rhs))
    return out[0], out[1]

def escala_rot(pl):
    (a, b, _), (d, e, _) = pl
    return math.sqrt(abs(a * e - b * d)) * AS, math.degrees(math.atan2(d, a))

def simular(ruido_px, ruido_cat_as, rng):
    XY, ST, pix = [], [], []
    for _ in range(40):
        x, y = rng.uniform(0, 2048), rng.uniform(0, 2048)
        xi, eta = placa_verdadera(x - 1024, y - 1024)
        a, d = inversa(xi, eta)
        a += rng.gauss(0, ruido_cat_as) / AS / math.cos(d); d += rng.gauss(0, ruido_cat_as) / AS
        ST.append(directa(a, d))
        XY.append((x - 1024 + rng.gauss(0, ruido_px), y - 1024 + rng.gauss(0, ruido_px)))
    return XY, ST

def calcular():
    rng0 = random.Random(1)
    XY0, ST0 = simular(0.0, 0.0, rng0)
    pl0 = ajustar(XY0, ST0)
    esc0, rot0 = escala_rot(pl0)
    # ida y vuelta de la proyeccion
    a, d = math.radians(150.7), math.radians(20.4)
    xi, eta = directa(a, d); a2, d2 = inversa(xi, eta)
    ida = max(abs(a - a2), abs(d - d2)) * AS
    # caso con ruido
    rng = random.Random(20261109)
    XY, ST = simular(0.10, 0.02, rng)
    pl = ajustar(XY, ST)
    esc, rot = escala_rot(pl)
    res = []
    for (x, y), (xi, eta) in zip(XY, ST):
        mx = pl[0][0] * x + pl[0][1] * y + pl[0][2]; my = pl[1][0] * x + pl[1][1] * y + pl[1][2]
        res += [(mx - xi) * AS, (my - eta) * AS]
    rms = math.sqrt(sum(v * v for v in res) / (len(res) - 6))
    # asteroide
    Xv, Yv = 1500.3 - 1024, 700.2 - 1024
    xi_v, eta_v = placa_verdadera(Xv, Yv); av, dv = inversa(xi_v, eta_v)
    Xm, Ym = Xv + rng.gauss(0, 0.10), Yv + rng.gauss(0, 0.10)
    xi_m = pl[0][0] * Xm + pl[0][1] * Ym + pl[0][2]; eta_m = pl[1][0] * Xm + pl[1][1] * Ym + pl[1][2]
    am, dm = inversa(xi_m, eta_m)
    err = math.hypot((am - av) * math.cos(dv), dm - dv) * AS
    # tasa de movimiento: 10 arcsec/min entre dos exposiciones separadas 20 min
    desplaz = 10.0 * 20.0
    return {"esc0": esc0, "rot0": rot0, "ida": ida, "esc": esc, "rot": rot, "rms": rms, "esperado": math.sqrt(0.10 ** 2 + 0.02 ** 2),
            "err": err, "av": math.degrees(av), "dv": math.degrees(dv), "am": math.degrees(am), "dm": math.degrees(dm), "desplaz": desplaz}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Ida y vuelta de la proyeccion: %.2e arcsec" % r["ida"])
    print("Sin ruido: escala = %.10f arcsec/px ; rotacion = %.10f deg (verdad 1.0 ; 12.0)" % (r["esc0"], r["rot0"]))
    print("Con ruido (40 estrellas): escala = %.5f arcsec/px ; rotacion = %.4f deg" % (r["esc"], r["rot"]))
    print("RMS del residuo = %.4f arcsec ; esperado = %.4f arcsec" % (r["rms"], r["esperado"]))
    print("Asteroide sintetico: verdad (RA, Dec) = (%.6f, %.6f) deg ; medido = (%.6f, %.6f) deg ; error = %.3f arcsec" % (r["av"], r["dv"], r["am"], r["dm"], r["err"]))
    print("Un objeto de 10 arcsec/min recorre %.0f arcsec (%.0f px) en 20 min" % (r["desplaz"], r["desplaz"]))
    assert r["ida"] < 1e-9 * AS
    assert abs(r["esc0"] - 1.0) < 1e-9 and abs(r["rot0"] - 12.0) < 1e-9
    assert 0.7 < r["rms"] / r["esperado"] < 1.2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
