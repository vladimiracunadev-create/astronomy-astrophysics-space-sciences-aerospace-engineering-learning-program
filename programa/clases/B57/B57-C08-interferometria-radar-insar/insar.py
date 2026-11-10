#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C08: interferometria radar (InSAR): fase, franjas y desenrollado.

Datos: banda C a 5.405 GHz y ciclo de repeticion de 12 dias (6 con dos satelites) de Sentinel-1 (SentiWiki, consultada 2026-11-09).
Deformacion SINTETICA: cubeta gaussiana de hundimiento en la linea de visita (LOS) d(x) = -d0 exp(-x^2/(2 w^2)), d0 = 0.15 m;
ruido de fase gaussiano de 0.3 rad, semilla 57. No hay datos observados.
Modelo: fase interferometrica phi = 4 pi d / lambda (ida y vuelta), envuelta a (-pi, pi]; desenrollado 1D con numpy.unwrap; una franja = lambda/2.
Validez: sin contribucion topografica ni atmosferica; coherencia constante. Tolerancia: error rms tras desenrollar < 3 sigma_d en el caso
de pendiente suave; el caso de pendiente excesiva DEBE fallar (> 1 cm).
Requiere numpy.
"""
import math, platform
import numpy as np

C = 299792458.0
LAM = C / 5.405e9
SIG_FASE = 0.3
D0 = 0.15


def caso(w, dx, seed=57):
    rng = np.random.default_rng(seed)
    x = np.arange(-6 * w, 6 * w + dx, dx)
    d = -D0 * np.exp(-x**2 / (2 * w**2))
    fase = 4 * math.pi * d / LAM + SIG_FASE * rng.standard_normal(x.size)
    env = np.angle(np.exp(1j * fase))
    des = np.unwrap(env)
    des -= des[0]
    d_rec = des * LAM / (4 * math.pi)
    d_rec -= d_rec[0] - d[0]
    err = d_rec - d
    pend = np.max(np.abs(np.diff(4 * math.pi * d / LAM)))
    return dict(rms=float(np.sqrt(np.mean(err**2))), rms_mm=float(np.sqrt(np.mean(err**2))) * 1e3, max_pend=float(pend), franjas=float(D0 / (LAM / 2)),
                n_franjas_obs=int(np.sum(np.abs(np.diff(env)) > math.pi)))


def calcular():
    r = {"lambda_cm": LAM * 100, "franja_cm": LAM / 2 * 100, "sig_d_mm": SIG_FASE * LAM / (4 * math.pi) * 1e3}
    r["suave"] = caso(3000.0, 20.0)
    r["empinado"] = caso(100.0, 20.0)
    r["fase_pico_rad"] = 4 * math.pi * D0 / LAM
    r["ciclos_ref"] = 12.0
    r["limite_pendiente_mm"] = LAM / 4 * 1e3
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"lambda = {r['lambda_cm']:.3f} cm ; una franja = lambda/2 = {r['franja_cm']:.3f} cm en la LOS ; sigma_d del ruido de fase (0.3 rad) = {r['sig_d_mm']:.2f} mm")
    print(f"Fase del pico (d0 = 0.15 m) = {r['fase_pico_rad']:.1f} rad = {r['suave']['franjas']:.2f} franjas")
    for nombre in ("suave", "empinado"):
        c = r[nombre]
        print(f"Caso {nombre}: salto maximo de fase entre pixeles = {c['max_pend']:.2f} rad ; saltos de envoltura observados = {c['n_franjas_obs']} ; rms tras desenrollar = {c['rms']*1e3:.2f} mm")
    print(f"Limite de desenrollado: deformacion maxima entre pixeles contiguos = lambda/4 = {r['limite_pendiente_mm']:.2f} mm")
    assert r["suave"]["max_pend"] < math.pi
    assert r["suave"]["rms"] < 3 * r["sig_d_mm"] * 1e-3
    assert r["empinado"]["max_pend"] > math.pi
    assert r["empinado"]["rms"] > 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
