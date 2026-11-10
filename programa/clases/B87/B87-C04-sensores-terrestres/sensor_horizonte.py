#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C04: sensor de horizonte (Tierra esferica): radio angular, nadir por ajuste de puntos del limbo, error vs altitud.
Modelo SINTETICO: K puntos del limbo equiespaciados en azimut medidos con error angular gaussiano sigma (por eje transversal).
Tierra esferica de radio 6378137 m (valor adoptado de ejemplo; sin achatamiento, sin atmosfera). Semilla 20260514."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *


def rho(alt_m):
    return math.asin(RE / (RE + alt_m))


def estimar_nadir(n, alt_m, sigma, K, rng, alt_supuesta_m=None):
    r = rho(alt_m)
    e1 = unit(np.cross(n, [0.3, 0.5, 0.8])); e2 = np.cross(n, e1)
    H = []
    for k in range(K):
        phi = 2 * math.pi * k / K
        h = math.cos(r) * n + math.sin(r) * (math.cos(phi) * e1 + math.sin(phi) * e2)
        H.append(noisy_unit(h, sigma, rng))
    H = np.array(H)
    rs = rho(alt_m if alt_supuesta_m is None else alt_supuesta_m)
    nh = np.linalg.lstsq(H, math.cos(rs) * np.ones(K), rcond=None)[0]
    nh = unit(nh)
    rho_est = math.acos(max(-1, min(1, float(np.mean(H @ nh)))))
    return nh, rho_est


def mc(alt_m, sigma, K, n=2000, seed=20260514, alt_supuesta_m=None):
    rng = np.random.default_rng(seed)
    errs, rhos = [], []
    for _ in range(n):
        nt = unit(rng.standard_normal(3))
        nh, re_ = estimar_nadir(nt, alt_m, sigma, K, rng, alt_supuesta_m)
        errs.append(math.acos(max(-1, min(1, nh @ nt)))); rhos.append(re_)
    return math.sqrt(np.mean(np.square(errs))) * R2D, np.std(rhos) * R2D


def calcular():
    sig = 0.05 * D2R
    tabla = []
    for h_km in (400, 500, 800, 1500, 35786):
        r = rho(h_km * 1e3)
        e, sr = mc(h_km * 1e3, sig, 4)
        dhdr = RE * math.cos(r) / math.sin(r) ** 2 / 1e3 * D2R  # km por grado
        tabla.append((h_km, r * R2D, e, sr, dhdr))
    e4, _ = mc(500e3, sig, 4)
    e8, _ = mc(500e3, sig, 8)
    e16, _ = mc(500e3, sig, 16)
    e_mal, _ = mc(500e3, sig, 4, alt_supuesta_m=450e3)
    return dict(tabla=tabla, sig_deg=0.05, e4=e4, e8=e8, e16=e16, teo4=2 * 0.05 / math.sqrt(4),
                teo8=2 * 0.05 / math.sqrt(8), teo16=2 * 0.05 / math.sqrt(16), e_mal=e_mal,
                rho500=rho(500e3) * R2D, drho_mal=(rho(450e3) - rho(500e3)) * R2D)


def main():
    banner("B87-C04 sensor de horizonte | Tierra esferica; limbo medido con sigma = 0.05 deg por eje (SINTETICO, semilla 20260514)")
    d = calcular()
    print("alt [km]  rho [deg]  error nadir rms [deg]  desv. de rho [deg]  km de altitud por grado de rho")
    for h, r, e, sr, dh in d['tabla']:
        print(f"{h:8d}  {r:9.4f}  {e:20.4f}  {sr:17.4f}  {dh:12.1f}")
    print(f"K = 4 puntos: error rms = {d['e4']:.4f} deg (teoria 2*sigma/sqrt(K) = {d['teo4']:.4f})")
    print(f"K = 8 puntos: error rms = {d['e8']:.4f} deg (teoria {d['teo8']:.4f})")
    print(f"K = 16 puntos: error rms = {d['e16']:.4f} deg (teoria {d['teo16']:.4f})")
    print(f"altitud supuesta 450 km en lugar de 500 km (rho cambia {d['drho_mal']:.3f} deg): error de nadir = {d['e_mal']:.4f} deg")
    for _, _, e, _, _ in d['tabla']:
        assert abs(e - d['e4']) / d['e4'] < 0.1
    assert abs(d['e4'] - d['teo4']) / d['teo4'] < 0.08 and abs(d['e16'] - d['teo16']) / d['teo16'] < 0.08
    assert abs(d['e_mal'] - d['e4']) / d['e4'] < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
