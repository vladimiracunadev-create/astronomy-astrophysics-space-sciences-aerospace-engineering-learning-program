#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C17: principios de la desviacion por impactador cinetico: cambio de periodo de un satelite binario y desplazamiento heliocentrico acumulado.

Datos: (A) sistema binario SINTETICO inspirado en la mision DART (pagina de NASA consultada el 2026-11-09): periodo orbital inicial de 11 h 55 min y final de 11 h 23 min (cambio de 32 min) segun la
fuente; el semieje de 1190 m es ILUSTRATIVO (no consultado) y fija GM por la tercera ley de Kepler. La fuente NO da un valor numerico del factor de aumento de momento beta. (B) asteroide SINTETICO
circular a 1.1 au con un impulso tangencial de 0.01 m/s. Constante de Gauss, ua y radio terrestre recordados, no consultados.
Modelo: (A) un impulso retrogrado dv en una orbita circular da a' por vis-viva (exacto) y P' = P (a'/a)^1.5; primer orden dP/P = -3 dv/v; integracion leapfrog con medida del periodo por angulo
acumulado. (B) integracion leapfrog heliocentrica de 10 y 20 anios con paso 0.5 d; desplazamiento a lo largo de la orbita frente a 3 dv T. Unidades SI en (A), au y dia en (B).
Supuestos: orbitas circulares iniciales, impulso instantaneo y tangencial, dos cuerpos. Validez: ilustrativa; no reconstruye DART ni ninguna mision.
Tolerancia: periodo integrado frente a vis-viva 1e-6 relativo; primer orden frente a exacto 5 %; desplazamiento integrado frente a 3 dv T 3 % (10 y 20 anios).
"""
import math, platform

def periodo_integrado(a, GM, v0, dt):
    """Orbita con posicion (a, 0) y velocidad (0, v0); tiempo en que el angulo acumulado llega a 2 pi (interpolacion lineal)."""
    x, y, vx, vy = a, 0.0, 0.0, v0
    def acc(x, y):
        r3 = (x * x + y * y) ** 1.5
        return -GM * x / r3, -GM * y / r3
    ax, ay = acc(x, y)
    th, thp, t = 0.0, 0.0, 0.0
    while True:
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        ax, ay = acc(x, y)
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        t += dt
        ang = math.atan2(y, x)
        d = (ang - thp + math.pi) % (2 * math.pi) - math.pi
        th_prev = th
        th += d; thp = ang
        if th >= 2 * math.pi:
            return t - dt + dt * (2 * math.pi - th_prev) / (th - th_prev)

def periodo_exacto(a, GM, dv):
    v = math.sqrt(GM / a)
    vn = v - dv
    an = 1.0 / (2.0 / a - vn * vn / GM)
    return 2 * math.pi * math.sqrt(an ** 3 / GM)

def parteA():
    P0 = 11 * 3600 + 55 * 60.0
    dP = -32 * 60.0
    a = 1190.0
    GM = 4 * math.pi ** 2 * a ** 3 / P0 ** 2
    v = 2 * math.pi * a / P0
    lo, hi = 0.0, 0.1 * v
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if periodo_exacto(a, GM, mid) - P0 > dP:
            lo = mid
        else:
            hi = mid
    dv = 0.5 * (lo + hi)
    dv1 = abs(dP) / P0 * v / 3.0
    Pint = periodo_integrado(a, GM, v - dv, P0 / 20000)
    return {"v": v, "dv": dv, "dv1": dv1, "Pint": Pint, "Pex": periodo_exacto(a, GM, dv), "P0": P0, "GM": GM, "frac": abs(dP) / P0}

def integrar_helio(a0, dv_aud, dias, dt):
    K = 0.01720209895; GM = K * K
    res = []
    for kick in (0.0, dv_aud):
        x, y, vx, vy = a0, 0.0, 0.0, math.sqrt(GM / a0) + kick
        def acc(x, y):
            r3 = (x * x + y * y) ** 1.5
            return -GM * x / r3, -GM * y / r3
        ax, ay = acc(x, y); th, thp = 0.0, 0.0
        for _ in range(int(round(dias / dt))):
            vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
            x += dt * vx; y += dt * vy
            ax, ay = acc(x, y)
            vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
            ang = math.atan2(y, x)
            th += (ang - thp + math.pi) % (2 * math.pi) - math.pi; thp = ang
        res.append(th)
    return res[0] - res[1]

def calcular():
    A = parteA()
    AU = 1.495978707e11
    dv = 0.01
    dv_aud = dv * 86400.0 / AU
    filas = []
    for anios in (10, 20):
        dias = anios * 365.25
        dth = integrar_helio(1.1, dv_aud, dias, 0.5)
        s_num = abs(dth) * 1.1 * AU
        s_ana = 3 * dv * dias * 86400.0
        filas.append((anios, s_num / 1e3, s_ana / 1e3, abs(s_num / s_ana - 1)))
    b = 1.5 * 6378.137e3
    req = [(T, b / (3 * T * 365.25 * 86400.0) * 1e3) for T in (1, 2, 5, 10, 20)]
    return {"A": A, "filas": filas, "req": req}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular(); A = r["A"]
    print("(A) Binario sintetico: P0 = %.0f s (11 h 55 min) ; a = 1190 m (ilustrativo) ; v circular = %.4f m/s" % (A["P0"], A["v"]))
    print("    dv exacto (vis-viva) para -32 min = %.5f m/s ; primer orden -3 dv/v: %.5f m/s ; cociente = %.3f" % (A["dv"], A["dv1"], A["dv1"] / A["dv"]))
    print("    Periodo tras el impulso: integrado = %.3f s ; vis-viva = %.3f s ; diferencia relativa = %.2e" % (A["Pint"], A["Pex"], abs(A["Pint"] / A["Pex"] - 1)))
    print("(B) Impulso de 0.01 m/s a 1.1 au; desplazamiento a lo largo de la orbita:")
    for an, sn, sa, e in r["filas"]:
        print("    %2d anios : integrado = %.0f km ; 3 dv T = %.0f km ; diferencia = %.2f %%" % (an, sn, sa, 100 * e))
    print("(C) dv necesario para desplazar 1.5 radios terrestres (9567 km) segun el aviso T:")
    for T, d in r["req"]:
        print("    T = %2d anios : dv = %.3f mm/s" % (T, d))
    assert abs(A["Pint"] / A["Pex"] - 1) < 1e-6
    assert abs(A["dv1"] / A["dv"] - 1) < 0.05
    assert all(f[3] < 0.03 for f in r["filas"])
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
