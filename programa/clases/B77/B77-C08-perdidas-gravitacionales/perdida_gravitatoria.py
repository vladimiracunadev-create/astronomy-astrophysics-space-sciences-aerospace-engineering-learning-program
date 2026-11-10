#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C08: perdidas gravitacionales en un ascenso SINTETICO.

Datos consultados (2026-11-10): Delta_v = V_eq ln(MR) - g0 t_b para ascenso vertical (NASA Glenn); g0 = 9.80665 m/s2 (NIST CODATA 2022).
ILUSTRATIVOS (sinteticos): Isp = 350 s, MR = 8 (masa inicial 100 000 kg), empuje constante variable segun T/W inicial (1.2 a 3.0),
programa de cabeceo lineal en el tiempo de 90 a 30 grados sobre el horizonte local.
Sistema: plano vertical local (Tierra plana, g = g0 constante, sin aire), gamma = angulo de la trayectoria sobre el horizonte, SI.
Modelo: dv/dt = F/m - g sin(gamma) (aceleracion a lo largo de la velocidad); perdida gravitacional L_g = integral g sin(gamma) dt.
Segunda via: para gamma constante L_g = g sin(gamma) t_b; para cabeceo lineal L_g = g t_b (cos g0 - cos gf)/(gf - g0) con angulos en rad.
Tolerancias: integral numerica frente a analitica 1e-9 relativa (regla de Simpson compuesta).
"""
import math, platform

G0, ISP, MR, M0 = 9.80665, 350.0, 8.0, 100000.0


def perdida_numerica(tb, gam0, gamf, n=2000):
    h = tb / n
    s = 0.0
    for i in range(n + 1):
        t = i * h
        gam = gam0 + (gamf - gam0) * t / tb
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * G0 * math.sin(gam)
    return s * h / 3.0


def perdida_analitica(tb, gam0, gamf):
    if abs(gamf - gam0) < 1e-15:
        return G0 * math.sin(gam0) * tb
    return G0 * tb * (math.cos(gam0) - math.cos(gamf)) / (gamf - gam0)


def tiempo_combustion(tw0):
    c = ISP * G0
    mprop = M0 * (1 - 1 / MR)
    f = tw0 * M0 * G0
    return mprop * c / f


def calcular():
    c = ISP * G0
    r = {"c": c, "dv_ideal": c * math.log(MR)}
    filas = []
    for tw in (1.2, 1.5, 2.0, 3.0):
        tb = tiempo_combustion(tw)
        lv = perdida_analitica(tb, math.pi / 2, math.pi / 2)
        lp = perdida_analitica(tb, math.pi / 2, math.radians(30))
        lpn = perdida_numerica(tb, math.pi / 2, math.radians(30))
        filas.append(dict(tw=tw, tb=tb, lv=lv, lp=lp, lpn=lpn, ganancia_v=r["dv_ideal"] - lv, ganancia_p=r["dv_ideal"] - lp))
    r["filas"] = filas
    r["err"] = max(abs(f["lpn"] - f["lp"]) / f["lp"] for f in filas)
    r["err_vert"] = max(abs(perdida_numerica(f["tb"], math.pi / 2, math.pi / 2) - f["lv"]) / f["lv"] for f in filas)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cohete SINTETICO: Isp = {ISP} s (c = {r['c']:.2f} m/s), MR = {MR}, DV ideal = {r['dv_ideal']:.1f} m/s, m0 = {M0:.0f} kg")
    print(" T/W0   t_b [s]  perdida vertical  perdida cabeceo 90->30  (numerica)   DV neto vertical  DV neto cabeceo")
    for f in r["filas"]:
        print(f" {f['tw']:4.1f}  {f['tb']:7.2f}  {f['lv']:12.1f}  {f['lp']:16.1f}  {f['lpn']:16.1f}  {f['ganancia_v']:12.1f}  {f['ganancia_p']:12.1f}")
    print(f"Error relativo maximo de la integral (cabeceo): {r['err']:.2e}; (vertical): {r['err_vert']:.2e}")
    assert r["err"] < 1e-9 and r["err_vert"] < 1e-9
    assert r["filas"][0]["lv"] > r["filas"][-1]["lv"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
