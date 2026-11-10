#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C21: infrarrojo termico: temperatura de brillo, emisividad y ventana dividida.

Datos: bandas termicas 10 (10.6-11.19 um) y 11 (11.5-12.51 um) de Landsat 8, pixel de 100 m (USGS, consultada 2026-11-09), y resolucion de 70 m de ECOSTRESS
(JPL, consultada 2026-11-09). ILUSTRATIVOS / SINTETICOS: longitudes de onda efectivas 10.9 y 12.0 um, emisividades 0.98 y 0.97, atmosfera de temperatura 270 K
con transmitancias exp(-k_i w) (k = 0.10 y 0.17 por unidad de vapor w), semilla 57, 4000 escenas. No se usa ninguna imagen real.
Modelo: L_i = tau_i eps_i B_i(Ts) + (1 - tau_i) B_i(Ta) ; temperatura de brillo T_b = B^-1(L) ; correccion de emisividad Ts = B^-1((L - (1-eps) L_abajo)/eps) ;
ventana dividida: Ts = T11 + c1 (T11 - T12) + c0 ajustada por minimos cuadrados.
Validez: atmosfera de una capa, emisividad conocida. Tolerancia: inversion de Planck 1e-9 K; el error rms de la ventana dividida debe ser < 1.5 K y menor que el de T11 sola.
Requiere numpy.
"""
import math, platform
import numpy as np

H, C, KB = 6.62607015e-34, 299792458.0, 1.380649e-23
L1, L2 = 10.9e-6, 12.0e-6
E1, E2 = 0.98, 0.97


def B(lam, T):
    return 2 * H * C**2 / lam**5 / np.expm1(H * C / (lam * KB * T))


def Binv(lam, L):
    return H * C / (lam * KB * np.log1p(2 * H * C**2 / lam**5 / L))


def escenas(rng, n):
    Ts = rng.uniform(280, 320, n)
    Ta = rng.uniform(260, 285, n)
    w = rng.uniform(0.5, 4.0, n)
    t1, t2 = np.exp(-0.10 * w), np.exp(-0.17 * w)
    La1 = t1 * E1 * B(L1, Ts) + (1 - t1) * B(L1, Ta)
    La2 = t2 * E2 * B(L2, Ts) + (1 - t2) * B(L2, Ta)
    return Ts, Binv(L1, La1), Binv(L2, La2)


def calcular():
    r = {}
    r["err_planck"] = float(abs(Binv(L1, B(L1, 300.0)) - 300.0))
    # correccion de emisividad (sin atmosfera): suelo a 310 K con cielo de 250 K
    Ts, Tcielo = 310.0, 250.0
    for eps in (0.98, 0.92):
        L = eps * B(L1, Ts) + (1 - eps) * B(L1, Tcielo)
        r[f"Tb_eps{int(eps*100)}"] = float(Binv(L1, L))
        r[f"Ts_corr_eps{int(eps*100)}"] = float(Binv(L1, (L - (1 - eps) * B(L1, Tcielo)) / eps))
    r["dT_sin_corr_92"] = Ts - r["Tb_eps92"]
    r["dT_eps_mal"] = float(Binv(L1, (0.92 * B(L1, Ts) + 0.08 * B(L1, Tcielo) - 0.02 * B(L1, Tcielo)) / 0.98) - Ts)
    rng = np.random.default_rng(57)
    Ts, T1, T2 = escenas(rng, 4000)
    r["rms_T11"] = float(np.sqrt(np.mean((T1 - Ts) ** 2)))
    A = np.column_stack([np.ones_like(Ts), T1 - T2])
    c = np.linalg.lstsq(A, Ts - T1, rcond=None)[0]
    r["c0"], r["c1"] = float(c[0]), float(c[1])
    Ts_est = T1 + A @ c
    r["rms_sw"] = float(np.sqrt(np.mean((Ts_est - Ts) ** 2)))
    r["sesgo_T11"] = float(np.mean(T1 - Ts))
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Inversion de Planck: error = {r['err_planck']:.1e} K")
    print(f"Suelo a 310 K con cielo a 250 K: T_brillo (eps 0.98) = {r['Tb_eps98']:.3f} K ; T_brillo (eps 0.92) = {r['Tb_eps92']:.3f} K ; subestimacion por eps 0.92 = {r['dT_sin_corr_92']:.3f} K")
    print(f"Con correccion de emisividad: eps 0.98 -> {r['Ts_corr_eps98']:.4f} K ; eps 0.92 -> {r['Ts_corr_eps92']:.4f} K ; error si se usa eps 0.98 con un suelo de 0.92 = {r['dT_eps_mal']:.3f} K")
    print(f"Ventana dividida (4000 escenas): sesgo de T11 = {r['sesgo_T11']:.2f} K ; rms T11 sola = {r['rms_T11']:.2f} K ; rms ventana dividida = {r['rms_sw']:.2f} K ; c0 = {r['c0']:.3f} ; c1 = {r['c1']:.3f}")
    assert r["err_planck"] < 1e-6
    assert abs(r["Ts_corr_eps92"] - 310.0) < 1e-6 and abs(r["Ts_corr_eps98"] - 310.0) < 1e-6
    assert r["rms_sw"] < 1.5 and r["rms_sw"] < r["rms_T11"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
