#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C13: dispersion de la orbita de inyeccion (Monte Carlo frente a propagacion lineal).

Datos consultados (2026-11-10): radio ecuatorial 6378.137 km (NASA/NSSDC Earth Fact Sheet).
NO CONSULTADO (valor estandar rotulado): mu = 3.986004418e14 m3/s2.
SINTETICOS / ILUSTRATIVOS (inventados): orbita nominal de inyeccion con perigeo a 200 km y apogeo a 600 km, inyectada en el perigeo (gamma = 0);
errores de inyeccion independientes y gaussianos: sigma_r = 1 km, sigma_v = 3 m/s, sigma_gamma = 0.05 grados; N = 200 000 muestras con semilla 11.
Sistema: plano orbital, Tierra esferica, dos cuerpos (sin J2 ni arrastre); gamma = angulo de la velocidad sobre el horizonte local.
Modelo: de (r, v, gamma) se obtienen a = -mu/(2 eps), h = r v cos(gamma), e = sqrt(1 + 2 eps h^2/mu^2), rp = a(1-e), ra = a(1+e).
Segunda via: propagacion lineal con el jacobiano por diferencias centrales: Sigma_y = J Sigma_x J^T (errores independientes).
Tolerancias: desviacion estandar de Monte Carlo frente a la lineal, 3 % relativo (error estadistico de ~0.2 % con N = 200 000); el sesgo medio de rp coincide con el de segundo orden (0.5 d2rp/dx2 sigma^2) dentro de 4 errores estandar de la media.
"""
import math, platform, random

MU, RE = 3.986004418e14, 6378137.0
RP0, RA0 = RE + 200e3, RE + 600e3
SIG = (1000.0, 3.0, math.radians(0.05))
N, SEMILLA = 200000, 11


def elementos(r, v, g):
    eps = 0.5 * v * v - MU / r
    a = -MU / (2 * eps)
    h = r * v * math.cos(g)
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU ** 2))
    return a, e, a * (1 - e) - RE, a * (1 + e) - RE


def nominal():
    a = 0.5 * (RP0 + RA0)
    return RP0, math.sqrt(MU * (2 / RP0 - 1 / a)), 0.0


def jacobiano(x0):
    J = [[0.0] * 3 for _ in range(4)]
    for j in range(3):
        d = [abs(x0[j]) * 1e-6 + 1e-9, 1e-4, 1e-8][j]
        xp, xm = list(x0), list(x0)
        xp[j] += d
        xm[j] -= d
        yp, ym = elementos(*xp), elementos(*xm)
        for i in range(4):
            J[i][j] = (yp[i] - ym[i]) / (2 * d)
    return J


def sesgo_segundo_orden(x0, i):
    """0.5 * sum_j d2y_i/dx_j2 * sigma_j^2 por diferencias centrales de segundo orden (terminos cruzados despreciados)."""
    y0 = elementos(*x0)[i]
    tot = 0.0
    for j, d in enumerate((10.0, 0.05, 1e-4)):
        xp, xm = list(x0), list(x0)
        xp[j] += d
        xm[j] -= d
        h2 = (elementos(*xp)[i] - 2 * y0 + elementos(*xm)[i]) / (d * d)
        tot += 0.5 * h2 * SIG[j] ** 2
    return tot


def calcular():
    x0 = nominal()
    y0 = elementos(*x0)
    J = jacobiano(x0)
    nombres = ("a", "e", "perigeo", "apogeo")
    lin = [math.sqrt(sum((J[i][j] * SIG[j]) ** 2 for j in range(3))) for i in range(4)]
    rnd = random.Random(SEMILLA)
    s1 = [0.0] * 4
    s2 = [0.0] * 4
    bajo = 0
    for _ in range(N):
        x = (x0[0] + rnd.gauss(0, SIG[0]), x0[1] + rnd.gauss(0, SIG[1]), x0[2] + rnd.gauss(0, SIG[2]))
        y = elementos(*x)
        for i in range(4):
            s1[i] += y[i]
            s2[i] += y[i] * y[i]
        if y[2] < 150e3:
            bajo += 1
    media = [s / N for s in s1]
    mc = [math.sqrt(max(0.0, s2[i] / N - media[i] ** 2)) for i in range(4)]
    return dict(nombres=nombres, y0=y0, v0=x0[1], J=J, lin=lin, mc=mc, media=media,
                dif=[abs(mc[i] - lin[i]) / lin[i] for i in range(4)],
                sesgo_rp=media[2] - y0[2], sesgo_pred=sesgo_segundo_orden(x0, 2), err_est_rp=mc[2] / math.sqrt(N), p_bajo=bajo / N)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    y0 = r["y0"]
    print(f"Inyeccion SINTETICA en el perigeo: r = {RP0/1e3:.3f} km, v = {r['v0']:.3f} m/s; a = {y0[0]/1e3:.3f} km, e = {y0[1]:.5f}, perigeo = {y0[2]/1e3:.3f} km, apogeo = {y0[3]/1e3:.3f} km")
    print(f"Errores 1-sigma INVENTADOS: r {SIG[0]:.0f} m, v {SIG[1]:.1f} m/s, gamma {math.degrees(SIG[2]):.3f} grados; N = {N}, semilla {SEMILLA}")
    print("Jacobiano d(a, e, perigeo, apogeo)/d(r, v, gamma) [m/m, m/(m/s), m/rad]:")
    for nom, fila in zip(r["nombres"], r["J"]):
        print(f"  {nom:8s} " + "  ".join(f"{x:14.6g}" for x in fila))
    print("  magnitud  sigma lineal   sigma Monte Carlo   dif. relativa")
    for i, nom in enumerate(r["nombres"]):
        u = 1.0 if nom == "e" else 1e3
        print(f"  {nom:8s}  {r['lin'][i]/u:12.6g}  {r['mc'][i]/u:14.6g}  {r['dif'][i]*100:10.3f} %   ({'adimensional' if nom == 'e' else 'km'})")
    print(f"Sesgo medio del perigeo = {r['sesgo_rp']:.3f} m (error estandar de la media = {r['err_est_rp']:.3f} m)")
    print(f"Sesgo previsto por la curvatura de segundo orden (0.5 H sigma^2) = {r['sesgo_pred']:.3f} m")
    print(f"Fraccion de muestras con perigeo < 150 km = {r['p_bajo']:.3e}")
    assert all(d < 0.03 for d in r["dif"])
    assert abs(r["sesgo_rp"] - r["sesgo_pred"]) < 4 * r["err_est_rp"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
