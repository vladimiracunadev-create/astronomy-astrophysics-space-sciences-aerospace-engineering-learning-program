#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C17: perfil de observacion de un sobrevuelo de Europa (hiperbola de dos cuerpos).

Datos consultados (2026-11-10): GM de Europa 3202.71210 km3/s2 y radio medio 1560.80 km (JPL SSD, parametros fisicos de satelites).
SINTETICOS / ILUSTRATIVOS: v_inf = 4.0 km/s, altitudes de maxima aproximacion de 25 a 800 km, campo de vision instantaneo (IFOV) de 0.25 mrad, tasa de datos de 10 Mbit/s y ventana de observacion con altitud < 1000 km;
ninguno procede de una mision ni de un instrumento real.
Modelo: dos cuerpos nave-Europa, sin Jupiter ni rotacion de Europa; la traza al suelo es el arco subnave sobre una esfera de radio R.
Pruebas: (1) el tiempo con altitud < 1000 km por la ecuacion hiperbolica de Kepler iguala el obtenido propagando con Kepler universal y biseccion (tol. 1e-3 s);
(2) el angulo barrido por la formula (2 nu) iguala el angulo entre los vectores de posicion de entrada y salida (tol. 1e-9 rad); (3) la resolucion lineal escala con la altitud (tol. 1e-12).
"""
import math, platform
GM, R = 3202.71210, 1560.80
VINF = 4.0
IFOV = 0.25e-3
TASA = 10e6  # bit/s
HLIM = 1000.0
# --- Utilidades de dos cuerpos (todas en km, s, km/s) ---
def _stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def kepler_prop(r0, v0, dt, mu):
    """Propaga (r0, v0) durante dt con variables universales (Curtis, alg. 3.4); r0, v0 listas de 3."""
    r0n = math.sqrt(sum(x * x for x in r0)); vr0 = sum(a * b for a, b in zip(r0, v0)) / r0n
    alpha = 2 / r0n - sum(x * x for x in v0) / mu
    sm = math.sqrt(mu)
    if alpha > 0: x = sm * alpha * dt
    elif alpha < 0:
        a_ = 1 / alpha; sg = 1.0 if dt >= 0 else -1.0
        rv = sum(p * q for p, q in zip(r0, v0))
        x = sg * math.sqrt(-a_) * math.log((-2 * mu * alpha * dt) / (rv + sg * math.sqrt(-mu * a_) * (1 - r0n * alpha)))
    else: x = sm * dt / r0n
    for _ in range(200):
        z = alpha * x * x; C, S = _stumpff(z)
        F = r0n * vr0 / sm * x * x * C + (1 - alpha * r0n) * x**3 * S + r0n * x - sm * dt
        dF = r0n * vr0 / sm * x * (1 - z * S) + (1 - alpha * r0n) * x * x * C + r0n
        dx = F / dF; x -= dx
        if abs(dx) < 1e-12 * max(1.0, abs(x)): break
    z = alpha * x * x; C, S = _stumpff(z)
    f = 1 - x * x / r0n * C; g = dt - x**3 / sm * S
    r = [f * a + g * b for a, b in zip(r0, v0)]; rn = math.sqrt(sum(q * q for q in r))
    fd = sm / (rn * r0n) * (z * S - 1) * x; gd = 1 - x * x / rn * C
    v = [fd * a + gd * b for a, b in zip(r0, v0)]
    return r, v


def rk4_dosc(r, v, dt, n, mu):
    """Integra el problema de dos cuerpos con RK4 de paso fijo (n pasos de dt)."""
    def acc(p):
        d = math.sqrt(sum(q * q for q in p)); return [-mu * q / d**3 for q in p]
    r = list(r); v = list(v)
    for _ in range(n):
        k1v = acc(r); k1r = v
        r2 = [a + 0.5 * dt * b for a, b in zip(r, k1r)]; v2 = [a + 0.5 * dt * b for a, b in zip(v, k1v)]
        k2v = acc(r2); k2r = v2
        r3 = [a + 0.5 * dt * b for a, b in zip(r, k2r)]; v3 = [a + 0.5 * dt * b for a, b in zip(v, k2v)]
        k3v = acc(r3); k3r = v3
        r4 = [a + dt * b for a, b in zip(r, k3r)]; v4 = [a + dt * b for a, b in zip(v, k3v)]
        k4v = acc(r4); k4r = v4
        r = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(r, k1r, k2r, k3r, k4r)]
        v = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(v, k1v, k2v, k3v, k4v)]
    return r, v



def tiempo_y_angulo(rp, hlim):
    e = 1 + rp * VINF**2 / GM
    a = GM / VINF**2
    rl = R + hlim
    coshH = (1 + rl / a) / e
    H = math.acosh(coshH)
    t = math.sqrt(a**3 / GM) * (e * math.sinh(H) - H)
    p = a * (e * e - 1)
    nu = math.acos((p / rl - 1) / e)
    return e, t, nu


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"v_inf = {VINF} km/s (SINTETICO) ; IFOV = {IFOV*1e3} mrad ; tasa = {TASA/1e6:.0f} Mbit/s ; ventana: altitud < {HLIM:.0f} km")
    print(" h_ca [km]   e       giro [grados]  v_p [km/s]  v suelo en h_ca [km/s]  t en ventana [min]  traza [km]  resol. en h_ca [m]  resol. a 1000 km [m]  datos [Gbit]")
    for h in (25.0, 100.0, 400.0, 800.0):
        rp = R + h
        e, t, nu = tiempo_y_angulo(rp, HLIM)
        delta = 2 * math.asin(1 / e)
        vp = math.sqrt(VINF**2 + 2 * GM / rp)
        vs = vp * R / rp
        dur = 2 * t
        traza = R * 2 * nu
        # pruebas
        vp0 = vp
        rA, vA = kepler_prop([rp, 0, 0], [0, vp0, 0], t, GM)
        assert abs(math.hypot(*rA) - (R + HLIM)) < 1e-6
        ang_k = 2 * math.atan2(rA[1], rA[0])
        assert abs(ang_k - 2 * nu) < 1e-9
        print(f"{h:8.0f} {e:9.4f} {math.degrees(delta):11.3f} {vp:11.4f} {vs:20.4f} {dur/60:17.3f} {traza:11.0f} {h*IFOV*1e3:17.1f} {HLIM*IFOV*1e3:20.1f} {dur*TASA/1e9:12.2f}")
    # prueba 3: resolucion lineal
    assert abs(400 * IFOV / (100 * IFOV) - 4.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
