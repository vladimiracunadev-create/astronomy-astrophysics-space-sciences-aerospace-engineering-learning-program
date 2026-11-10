#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C10: geodesia con GNSS: posicion por pseudodistancias, sesgo de reloj y DOP.

Datos: SINTETICOS e ILUSTRATIVOS. Receptor en una esfera de 6371 km de radio a latitud -33.45 y longitud -70.66 (coordenadas ilustrativas);
satelites en una orbita circular de radio 26 560 km (valor ilustrativo, no consultado) en acimut/elevacion elegidos. Sesgo de reloj del receptor
0.3 ms; ruido de pseudodistancia gaussiano de 1 m (ilustrativo). No se consultaron paginas de GNSS en esta sesion.
Modelo: pseudodistancia P = |r_sat - r_rx| + c b ; minimos cuadrados de Gauss-Newton con 4 incognitas (x, y, z, c b); matriz de geometria G con
filas (-u, 1); DOP desde (G^T G)^-1 en ejes locales ENU; Monte Carlo con semilla fija 57 y 5000 ensayos.
Validez: sin ionosfera, troposfera, multitrayecto ni errores de efemerides. Tolerancia: error sin ruido < 1e-6 m; error rms 3D simulado frente
a PDOP*sigma dentro de 5 %.
Requiere numpy.
"""
import math, platform
import numpy as np

C = 299792458.0
RT, RS = 6371e3, 26560e3
LAT, LON = math.radians(-33.45), math.radians(-70.66)
SIG = 1.0
SESGO = 0.3e-3


def base_enu():
    e = np.array([-math.sin(LON), math.cos(LON), 0.0])
    n = np.array([-math.sin(LAT) * math.cos(LON), -math.sin(LAT) * math.sin(LON), math.cos(LAT)])
    u = np.array([math.cos(LAT) * math.cos(LON), math.cos(LAT) * math.sin(LON), math.sin(LAT)])
    return np.vstack([e, n, u])


def satelites(az_el):
    E = base_enu()
    rx = RT * E[2]
    sats = []
    for az, el in az_el:
        a, h = math.radians(az), math.radians(el)
        d = E.T @ np.array([math.cos(h) * math.sin(a), math.cos(h) * math.cos(a), math.sin(h)])
        b = rx @ d
        rho = -b + math.sqrt(b * b - (rx @ rx - RS**2))
        sats.append(rx + rho * d)
    return rx, np.array(sats)


def resolver(sats, P):
    x = np.zeros(4)
    for it in range(1, 20):
        rho = np.linalg.norm(sats - x[:3], axis=1)
        G = np.hstack([-(sats - x[:3]) / rho[:, None], np.ones((len(P), 1))])
        res = P - (rho + x[3])
        dx = np.linalg.lstsq(G, res, rcond=None)[0]
        x += dx
        if np.linalg.norm(dx) < 1e-6:
            break
    return x, it


def dop(sats, rx):
    E = base_enu()
    rho = np.linalg.norm(sats - rx, axis=1)
    u = (sats - rx) / rho[:, None]
    G = np.hstack([-(u @ E.T), np.ones((len(sats), 1))])
    Q = np.linalg.inv(G.T @ G)
    return dict(hdop=math.sqrt(Q[0, 0] + Q[1, 1]), vdop=math.sqrt(Q[2, 2]), pdop=math.sqrt(Q[0, 0] + Q[1, 1] + Q[2, 2]), tdop=math.sqrt(Q[3, 3]))


def caso(az_el, rng, ensayos=5000):
    rx, sats = satelites(az_el)
    P0 = np.linalg.norm(sats - rx, axis=1) + C * SESGO
    x, it = resolver(sats, P0)
    err0 = float(np.linalg.norm(x[:3] - rx))
    sesgo_rec = float(abs(x[3] / C - SESGO))
    d = dop(sats, rx)
    e = []
    for _ in range(ensayos):
        xs, _ = resolver(sats, P0 + SIG * rng.standard_normal(len(P0)))
        e.append(np.sum((xs[:3] - rx) ** 2))
    d.update(err0=err0, iter=it, sesgo_err=sesgo_rec, rms3d=math.sqrt(np.mean(e)))
    d["razon"] = d["rms3d"] / (d["pdop"] * SIG)
    return d


def calcular():
    rng = np.random.default_rng(57)
    buena = [(0, 20), (45, 35), (90, 50), (135, 65), (180, 80), (225, 30), (270, 45), (315, 25)]
    mala = [(0, 30), (20, 45), (40, 35), (60, 50)]
    return dict(buena=caso(buena, rng), mala=caso(mala, rng), clima_km=C * SESGO / 1e3)


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Un sesgo de reloj de 0.3 ms equivale a {r['clima_km']:.1f} km de pseudodistancia")
    for nombre in ("buena", "mala"):
        d = r[nombre]
        print(f"Geometria {nombre}: iteraciones = {d['iter']} ; error sin ruido = {d['err0']:.2e} m ; error de sesgo = {d['sesgo_err']:.2e} s")
        print(f"   HDOP = {d['hdop']:.2f} ; VDOP = {d['vdop']:.2f} ; PDOP = {d['pdop']:.2f} ; TDOP = {d['tdop']:.2f} ; rms 3D simulado = {d['rms3d']:.2f} m ; razon rms/(PDOP*sigma) = {d['razon']:.3f}")
    for nombre in ("buena", "mala"):
        assert r[nombre]["err0"] < 1e-6
        assert abs(r[nombre]["razon"] - 1) < 0.05
    assert r["mala"]["pdop"] > 3 * r["buena"]["pdop"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
