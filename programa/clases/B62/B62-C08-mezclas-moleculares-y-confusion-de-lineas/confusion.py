#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C08: mezcla de lineas, probabilidad de coincidencia e identificacion por varias lineas (SINTETICO).

Datos REALES consultados el 2026-11-09: seis frecuencias de reposo del 12C16O del catalogo JPL (c028001.cat), S4; c de CODATA 2022, S1.
Datos SINTETICOS (generados aqui, semilla 20261109; NO son una observacion): un campo de lineas "intrusas" distribuidas al azar (proceso de Poisson)
  con densidad rho = 0.01 lineas/MHz (10 por GHz, valor ilustrativo de una fuente rica en moleculas, no medido), y una "observacion"
  simulada de las seis lineas de CO desplazadas por una velocidad v_lsr = +7.30 km/s, con ruido de 0.05 km/s (1 sigma) en cada frecuencia.
Modelo:
  (1) fraccion de lineas con al menos otra a menos de +-w: analitica 1 - exp(-2 rho w) (Poisson) y exacta 1 - (1 - 2 w / L)^(N-1) para N lineas
      uniformes en una banda L; comparacion con Monte Carlo (500 realizaciones).
  (2) falsa identificacion: una especie ajena con k lineas predichas, cada una con probabilidad p = 2 rho delta de coincidir (delta = tolerancia);
      probabilidad de que coincidan todas p^k; con M especies candidatas, falsas identificaciones esperadas M p^k.
  (3) busqueda de velocidad: se barre v en [-50, +50] km/s (paso 0.02) y se cuentan lineas de CO predichas con una linea observada a menos
      de 0.30 km/s; se compara el maximo en la verdadera velocidad con el maximo en las demas (coincidencias por azar).
Supuestos: lineas puntuales (se ignora la forma), tolerancia constante en velocidad, sin confusion con lineas de CO de otros isotopologos.
Tolerancias: MC vs formula exacta dentro de 3 errores estandar; falsa identificacion k=1,2 dentro de 4 sigma binomiales.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

C_KMS = 299792.458
CO_REPOSO = np.array([115271.2018, 230538.0000, 345795.9899, 461040.7682, 576267.9305, 691473.0763])  # MHz (JPL, consultadas)


def main() -> int:
    print(f"Python {platform.python_version()}, numpy {np.__version__}")
    print("Datos SINTETICOS (semilla 20261109): campo de lineas intrusas rho = 0.01 /MHz y observacion simulada del CO; las seis frecuencias de reposo son REALES (JPL, 2026-11-09)")
    rng = np.random.default_rng(20261109)
    # (1) mezcla y bloqueo de lineas
    L, rho = 10000.0, 0.01          # banda de 10 GHz
    N = int(rho * L)
    print(f"(1) Banda de {L/1e3:.0f} GHz con N = {N} lineas intrusas (rho = {rho} /MHz)")
    print("    FWHM [MHz]  velocidad a 225 GHz [km/s]  analitica Poisson  exacta  Monte Carlo (+- error est.)")
    for w in (0.5, 1.5, 3.75, 7.5):
        pa = 1 - math.exp(-2 * rho * w)
        pe = 1 - (1 - 2 * w / L) ** (N - 1)
        fr = []
        for _ in range(500):
            x = np.sort(rng.uniform(0, L, N))
            d = np.diff(x)
            # linea interior bloqueada si el vecino mas cercano esta a menos de w
            vec = np.minimum(np.r_[np.inf, d], np.r_[d, np.inf])
            interior = (x > w) & (x < L - w)
            fr.append(np.mean(vec[interior] < w))
        mc, se = float(np.mean(fr)), float(np.std(fr, ddof=1) / math.sqrt(len(fr)))
        print(f"    {w:8.2f}   {w/225e3*C_KMS:12.3f}            {pa:10.4f}      {pe:7.4f}   {mc:7.4f} +- {se:.4f}")
        assert abs(mc - pe) < 3 * se + 2e-4, "Monte Carlo fuera de la formula exacta"
    # (2) falsas identificaciones
    delta = 0.5     # MHz
    p = 2 * rho * delta
    print(f"(2) Tolerancia +-{delta} MHz: probabilidad de coincidencia por linea p = 2 rho delta = {p:.4f}")
    M = 300
    for k in (1, 2, 3, 4):
        print(f"    k = {k} lineas: P(todas coinciden) = {p**k:.3e} ; con M = {M} especies candidatas, falsas identificaciones esperadas = {M*p**k:.3e}")
    ntr = 400000
    for k in (1, 2):
        # intrusas en una banda de 10 GHz; predichas k lineas ajenas en posiciones al azar
        x = np.sort(rng.uniform(0, L, N))
        pred = rng.uniform(0, L, (ntr, k))
        idx = np.searchsorted(x, pred)
        lo = x[np.clip(idx - 1, 0, N - 1)]
        hi = x[np.clip(idx, 0, N - 1)]
        dmin = np.minimum(np.abs(pred - lo), np.abs(pred - hi))
        ok = (dmin < delta).all(axis=1).mean()
        # cobertura exacta de esta realizacion: cada intrusa cubre 2 delta salvo solapes (se aproxima con la suma de huecos acotados)
        cub = (np.minimum(np.diff(x), 2 * delta).sum() + 2 * delta) / L
        sig = math.sqrt(cub ** k * (1 - cub ** k) / ntr)
        print(f"    MC k = {k}: {ok:.5f} (modelo p^k = {p**k:.5f}; cobertura de esta realizacion^k = {cub**k:.5f}; sigma = {sig:.5f})")
        assert abs(ok - cub ** k) < 4 * sig + 1e-6
    # (3) busqueda de velocidad con el CO
    v_true, sv = 7.30, 0.05
    nu_obs = CO_REPOSO * (1 - v_true / C_KMS) * (1 + rng.normal(0, sv / C_KMS, CO_REPOSO.size))
    band = (60e3, 750e3)
    n_int = int(rho * (band[1] - band[0]))
    intrusas = np.sort(rng.uniform(*band, n_int))
    todas = np.sort(np.r_[intrusas, nu_obs])
    print(f"(3) Observacion SIMULADA: {todas.size} lineas en {band[0]/1e3:.0f}-{band[1]/1e3:.0f} GHz ({n_int} intrusas + 6 del CO con v = {v_true} km/s)")
    vs = np.arange(-50.0, 50.0001, 0.02)
    tol = 0.30     # km/s
    cuentas = np.zeros(vs.size, dtype=int)
    for i, v in enumerate(vs):
        pred = CO_REPOSO * (1 - v / C_KMS)
        tolf = pred * tol / C_KMS
        idx = np.searchsorted(todas, pred)
        lo = todas[np.clip(idx - 1, 0, todas.size - 1)]
        hi = todas[np.clip(idx, 0, todas.size - 1)]
        cuentas[i] = int((np.minimum(np.abs(pred - lo), np.abs(pred - hi)) < tolf).sum())
    plateau = vs[cuentas == cuentas.max()]
    v_est = float(plateau.mean())
    lejos = np.abs(vs - v_true) > 1.0
    print(f"    maximo de coincidencias: {cuentas.max()} de 6 en el intervalo v = {plateau.min():.2f} a {plateau.max():.2f} km/s (centro {v_est:.2f}; verdadera: {v_true})")
    print(f"    fuera de +-1 km/s de la verdad: maximo por azar = {cuentas[lejos].max()} ; velocidades con 3 o mas coincidencias por azar = {(cuentas[lejos]>=3).sum()} de {lejos.sum()}")
    print(f"    histograma de coincidencias por azar (0,1,2,3,4+ lineas): {[int((cuentas[lejos]==j).sum()) for j in range(4)]+[int((cuentas[lejos]>=4).sum())]}")
    assert cuentas.max() == 6 and abs(v_est - v_true) < 0.15
    assert cuentas[lejos].max() <= 3
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
