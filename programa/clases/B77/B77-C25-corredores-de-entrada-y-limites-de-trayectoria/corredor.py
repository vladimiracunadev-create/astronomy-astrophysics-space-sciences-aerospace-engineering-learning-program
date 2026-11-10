#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C25: corredor de entrada (limites de angulo de trayectoria por captura y por carga) de un vehiculo SINTETICO.

Datos consultados (2026-11-10): resumen del NACA Report 1381 (Allen y Eggers): la desaceleracion maxima de una entrada balistica no depende de la masa, el tamano ni Cd (solo el resumen);
rho0 = 1.217 kg/m3, H = 8.5 km y radio 6378.137 km (NASA/NSSDC Earth Fact Sheet); g0 = 9.80665 m/s2 (NIST); D = Cd q A (NASA Glenn).
NO CONSULTADO (valor estandar rotulado): mu = 3.986004418e14 m3/s2. Los criterios de corredor de misiones reales NO se consultaron.
ILUSTRATIVOS (sinteticos, inventados): entrada a h = 122 km con v = 11 000 m/s (retorno lunar de orden de magnitud), beta = m/(Cd A) = 400 kg/m2, relaciones sustentacion/arrastre L/D = 0 (balistico) y 0.3,
limite de desaceleracion 12 g, la sustentacion se supone siempre 'arriba' (+) para el limite de carga y 'abajo' (-) para el de captura (inclinacion total del vector de sustentacion, idealizacion de la rotacion en balanceo),
atmosfera exponencial, Tierra esferica NO rotante, plano de la trayectoria, sin ablacion.
Sistema: plano orbital, coordenadas (r, theta), gamma = angulo de la velocidad sobre el horizonte local (negativo al entrar); angulo de entrada |gamma_E| positivo hacia abajo; SI.
Modelo: r' = v sin g; theta' = v cos g/r; v' = -D/m - mu sin g/r^2; g' = (L/m)/v - (mu/r^2 - v^2/r) cos g/v con L = (L/D) D (+/-); D/m = rho v^2/(2 beta). RK4, dt = 0.5 s.
Criterios: limite de carga = |gamma_E| maximo con a_max <= 12 g (sustentacion arriba); limite de captura = |gamma_E| minimo para que, al salir de la atmosfera, el apogeo de la orbita keplieriana de salida sea <= 20 000 km (criterio ilustrativo; sustentacion abajo). Corredor = diferencia en grados y en altitud del perigeo kepleriano (sin atmosfera) de las dos entradas.
Segunda via: estimacion de Allen-Eggers para el limite de carga balistico: sin gamma_E = 2 e H a_lim/v_E^2 (sin gravedad ni curvatura).
Tolerancias: bisecciones con ancho final < 1e-4 grados; monotonia de la desaceleracion maxima con el angulo comprobada en 6 puntos.
"""
import math, platform

MU, RE, G0 = 3.986004418e14, 6378137.0, 9.80665
RHO0, H = 1.217, 8500.0
H0, V0, BETA, ALIM = 122e3, 11000.0, 400.0, 12.0 * G0
APO_MAX = 20000e3  # apogeo maximo admisible tras el salto, ilustrativo


def trayectoria(gam_deg, ld, signo, dt=0.5):
    """signo = +1 sustentacion arriba, -1 abajo. Devuelve (a_max, energia_salida|None, h_min)."""
    r, th, v, g = RE + H0, 0.0, V0, -math.radians(gam_deg)
    amax, hmin = 0.0, 1e9
    t = 0.0

    def f(s):
        r_, th_, v_, g_ = s
        h = r_ - RE
        d = RHO0 * math.exp(-h / H) * v_ * v_ / (2 * BETA)
        gr = MU / (r_ * r_)
        return (v_ * math.sin(g_), v_ * math.cos(g_) / r_, -d - gr * math.sin(g_), signo * ld * d / v_ - (gr - v_ * v_ / r_) * math.cos(g_) / v_)
    s = [r, th, v, g]
    en_atm = False
    while t < 3000.0:
        k1 = f(s)
        k2 = f([a + dt / 2 * b for a, b in zip(s, k1)])
        k3 = f([a + dt / 2 * b for a, b in zip(s, k2)])
        k4 = f([a + dt * b for a, b in zip(s, k3)])
        s = [a + dt * (p + 2 * q + 2 * w + e) / 6 for a, p, q, w, e in zip(s, k1, k2, k3, k4)]
        t += dt
        h = s[0] - RE
        d = RHO0 * math.exp(-h / H) * s[2] ** 2 / (2 * BETA)
        a = math.sqrt(d * d * (1 + ld * ld))
        amax = max(amax, a)
        hmin = min(hmin, h)
        if h < 25e3 or s[2] < 2000.0:
            return amax, None, hmin  # entrada directa
        if s[3] > 0 and s[0] > RE + H0 and t > 20.0:
            return amax, apogeo_salida(s), hmin
    return amax, apogeo_salida(s), hmin


def apogeo_salida(s):
    """Altitud del apogeo [m] de la orbita keplieriana de salida; infinito si la energia no es negativa."""
    r, th, v, g = s
    eps = 0.5 * v * v - MU / r
    if eps >= 0:
        return float("inf")
    a = -MU / (2 * eps)
    h = r * v * math.cos(g)
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU ** 2))
    return a * (1 + e) - RE


def perigeo_kepleriano(gam_deg):
    r0, v, g = RE + H0, V0, -math.radians(gam_deg)
    eps = 0.5 * v * v - MU / r0
    h = r0 * v * math.cos(g)
    e = math.sqrt(1 + 2 * eps * h * h / MU ** 2)
    a = -MU / (2 * eps)
    return a * (1 - e) - RE  # a < 0 para hiperbola: a(1-e) > 0


def limite_carga(ld):
    lo, hi = 1.0, 40.0  # carga crece con el angulo
    for _ in range(36):
        mid = 0.5 * (lo + hi)
        if trayectoria(mid, ld, +1)[0] > ALIM:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def limite_captura(ld):
    lo, hi = 1.0, 40.0
    for _ in range(36):
        mid = 0.5 * (lo + hi)
        _, ap, _ = trayectoria(mid, ld, -1)
        capturado = (ap is None) or (ap <= APO_MAX)
        if capturado:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def calcular():
    r = {"casos": []}
    for ld in (0.0, 0.3):
        gc, gp = limite_carga(ld), limite_captura(ld)
        r["casos"].append(dict(ld=ld, steep=gc, shallow=gp, ancho=gc - gp, h_steep=perigeo_kepleriano(gc), h_shallow=perigeo_kepleriano(gp)))
    r["ae_steep"] = math.degrees(math.asin(2 * math.e * H * ALIM / V0 ** 2))
    r["mono"] = [trayectoria(g, 0.0, +1)[0] / G0 for g in (3.0, 5.0, 7.0, 9.0, 12.0, 16.0)]
    r["ok_mono"] = all(b > a for a, b in zip(r["mono"], r["mono"][1:]))
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Entrada SINTETICA: h = {H0/1e3:.0f} km, v = {V0:.0f} m/s, beta = {BETA:.0f} kg/m2, limite de carga = {ALIM/G0:.0f} g")
    print(" L/D   limite de carga (steep) [grados]  limite de captura (shallow) [grados]  ancho [grados]  perigeo kepleriano steep/shallow [km]")
    for c in r["casos"]:
        print(f" {c['ld']:.1f}   {c['steep']:12.4f}   {c['shallow']:18.4f}   {c['ancho']:12.4f}   {c['h_steep']/1e3:9.1f} / {c['h_shallow']/1e3:9.1f}")
    print(f"Estimacion de Allen-Eggers para el limite de carga balistico (sin gravedad ni curvatura): {r['ae_steep']:.3f} grados")
    print("Desaceleracion maxima balistica [g] para gamma_E = 3, 5, 7, 9, 12, 16 grados: " + ", ".join(f"{x:.1f}" for x in r["mono"]))
    assert r["ok_mono"]
    assert r["casos"][1]["ancho"] > r["casos"][0]["ancho"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
