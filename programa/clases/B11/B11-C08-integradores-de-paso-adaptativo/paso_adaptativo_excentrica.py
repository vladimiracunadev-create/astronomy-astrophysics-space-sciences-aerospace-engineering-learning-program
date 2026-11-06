#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C08: paso adaptativo por duplicación de paso en una órbita excéntrica.

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal IAU 2015, Res. B3).
Órbita ILUSTRATIVA muy excéntrica: a = 26 560 km, e = 0.74 (valores de ejemplo
de orden de magnitud, no de una misión concreta).
Modelo: dos cuerpos; referencia exacta por la ecuación de Kepler M = E - e sin E
resuelta por Newton (tolerancia 1e-15).
Método: RK4 con control de error por duplicación de paso: un paso h frente a
dos pasos h/2; error estimado = |s_2 - s_1| / 15 (extrapolación de Richardson
para orden 4); se acepta si err_norm <= 1 con escala atol + rtol |s|, y el
paso nuevo es h * min(5, max(0.2, 0.9 err_norm^(-1/5))).
Supuestos: sin perturbaciones; doble precisión. Validez: rtol >= 1e-12.
Tolerancia: error de posición tras un periodo < 1 km para rtol = 1e-9; el paso
mínimo debe ocurrir cerca del perigeo y el máximo cerca del apogeo; a igual
número de pasos, el paso fijo debe ser peor que el adaptativo.
"""
import math, platform

GM = 3.986004e14
a, e = 26_560e3, 0.74
b = a * math.sqrt(1 - e * e)
T = 2 * math.pi * math.sqrt(a**3 / GM)
n = 2 * math.pi / T


def F(t, s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -GM * x / r3, -GM * y / r3)


def kepler_exacta(t):
    M = (n * t) % (2 * math.pi)
    E = M if e < 0.8 else math.pi
    for _ in range(100):
        dE = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= dE
        if abs(dE) < 1e-15:
            break
    x, y = a * (math.cos(E) - e), b * math.sin(E)
    Ed = n / (1 - e * math.cos(E))
    return (x, y, -a * math.sin(E) * Ed, b * math.cos(E) * Ed)


def rk4(f, t, s, h):
    c = lambda k, q: tuple(si + h * q * ki for si, ki in zip(s, k))
    k1 = f(t, s); k2 = f(t + h / 2, c(k1, .5)); k3 = f(t + h / 2, c(k2, .5)); k4 = f(t + h, c(k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def adaptativo(s, t_fin, h, rtol, atol=1e-3):
    t, pasos, rech, trazas = 0.0, 0, 0, []
    while t < t_fin:
        h = min(h, t_fin - t)
        s1 = rk4(F, t, s, h)
        sm = rk4(F, t, s, h / 2)
        s2 = rk4(F, t + h / 2, sm, h / 2)
        err = max(abs(u - v) / 15 / (atol + rtol * max(abs(u), abs(v))) for u, v in zip(s2, s1))
        if err <= 1.0:
            t += h
            s = s2
            pasos += 1
            trazas.append((t - h, h))
        else:
            rech += 1
        h *= min(5.0, max(0.2, 0.9 * (err + 1e-30) ** (-0.2)))
    return s, pasos, rech, trazas


def fijo(s, t_fin, N):
    h, t = t_fin / N, 0.0
    for _ in range(N):
        s = rk4(F, t, s, h); t += h
    return s


print(f"Python {platform.python_version()}")
print(f"a = {a/1e3:.0f} km, e = {e}, periodo = {T:.2f} s = {T/3600:.4f} h, perigeo = {a*(1-e)/1e3:.1f} km, apogeo = {a*(1+e)/1e3:.1f} km")
s0 = kepler_exacta(0.0)
print("estado inicial (perigeo):", tuple(round(v, 4) for v in s0))
ex = kepler_exacta(T)
for rtol in (1e-6, 1e-8, 1e-10):
    s, pasos, rech, tr = adaptativo(s0, T, 10.0, rtol)
    err = math.hypot(s[0] - s0[0], s[1] - s0[1])
    hmin = min(tr, key=lambda p: p[1]); hmax = max(tr, key=lambda p: p[1])
    print(f"rtol={rtol:.0e}: pasos={pasos:5d} rechazados={rech:3d} error tras 1 periodo = {err:12.6f} m  "
          f"h_min={hmin[1]:.3f} s (t={hmin[0]/T:.3f} T)  h_max={hmax[1]:.2f} s (t={hmax[0]/T:.3f} T)")
    if rtol == 1e-10:
        ref_pasos, ref_err, ref_min, ref_max, ref_rech = pasos, err, hmin, hmax, rech
        s_ad = s
# prueba a mitad de periodo
s_h, pasos_h, _, _ = adaptativo(s0, T / 2, 10.0, 1e-10)
ex_h = kepler_exacta(T / 2)
err_h = math.hypot(s_h[0] - ex_h[0], s_h[1] - ex_h[1])
print(f"a T/2: error de posición = {err_h:.6f} m (distancia {math.hypot(*ex_h[:2])/1e3:.1f} km, apogeo)")
sf = fijo(s0, T, ref_pasos)
errf = math.hypot(sf[0] - s0[0], sf[1] - s0[1])
print(f"paso FIJO con los mismos {ref_pasos} pasos (h = {T/ref_pasos:.2f} s): error = {errf:.3f} m  (adaptativo: {ref_err:.6f} m)")

ev_ad = (ref_pasos + ref_rech) * 12          # cada intento = 3 pasos RK4 = 12 evaluaciones
N_eq = ev_ad // 4
sq = fijo(s0, T, N_eq)
errq = math.hypot(sq[0] - s0[0], sq[1] - s0[1])
print(f"A IGUAL COSTO ({ev_ad} evaluaciones): paso fijo con {N_eq} pasos (h = {T/N_eq:.2f} s): error = {errq:.3f} m")
assert ref_err < 1.0e3 and err_h < 1.0e3
assert errq > 10 * ref_err
assert ref_min[0] < 0.1 * T or ref_min[0] > 0.9 * T          # paso mínimo cerca del perigeo
assert abs(ref_max[0] / T - 0.5) < 0.2                       # paso máximo cerca del apogeo
assert errf > 100 * ref_err
print("Pruebas superadas.")
