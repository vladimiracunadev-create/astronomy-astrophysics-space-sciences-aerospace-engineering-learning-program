#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C27: navegacion por pulsares de rayos X (TECNICA DE INVESTIGACION, simulacion): precision del tiempo de llegada y del fijado de posicion.

Todo SINTETICO y SIMULADO; no se uso ningun dato de pulsares reales ni de detectores. Pulsar ILUSTRATIVO: periodo P = 33 ms, perfil gaussiano de anchura w = 0.03 ciclos (1 sigma) sobre un
fondo constante; tasa pulsada 8 fotones/s y tasa de fondo 20 fotones/s (promediadas; ILUSTRATIVAS). Observaciones de T = 1e3, 1e4 y 1e5 s. Se simula el perfil plegado en 64 casillas
con recuentos de Poisson, se estima el desfase por minimos cuadrados ponderados de la desviacion de Poisson sobre una malla fina (1e-4 ciclos) con refinamiento parabolico y se compara
la dispersion con la cota de Cramer-Rao: sigma_t = P / sqrt(T sum_b (lambda_b')^2 / lambda_b dphi), con lambda(phi) en fotones/s por ciclo. 150 realizaciones por duracion (semilla 97).
Fijado de posicion: con tres pulsares en direcciones SINTETICAS no coplanares n_i, el retraso de llegada es dt_i = n_i . dr / c, luego sigma_r(3D) = c sigma_t sqrt(tr[(N^T N)^-1]) con N = filas n_i.
Tolerancias: sigma empirica dentro del 25 % de la cota; el error de posicion escala como 1/sqrt(T).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

C = 299792458.0
P = 0.033
W = 0.03
RP, RB = 8.0, 20.0  # fotones/s pulsados y de fondo
NB = 64


def perfil_tasa(phi):
    """tasa en fotones/s por ciclo (integral sobre el ciclo = RP + RB)."""
    d = (phi + 0.5) % 1.0 - 0.5
    g = np.exp(-0.5 * (d / W) ** 2) / (W * math.sqrt(2 * math.pi))
    return RB + RP * g


def tasa_bin(shift):
    ph = (np.arange(NB) + 0.5) / NB - shift
    return perfil_tasa(ph)


def estima(cuentas, T):
    grid = np.arange(-0.05, 0.05, 1e-4)
    base = np.array([np.sum(cuentas * np.log(np.maximum(tasa_bin(s) * T / NB, 1e-12)) - tasa_bin(s) * T / NB) for s in grid])
    j = int(np.argmax(base))
    if 0 < j < len(grid) - 1:
        a, b, c = base[j - 1], base[j], base[j + 1]
        d = 0.5 * (a - c) / (a - 2 * b + c)
    else:
        d = 0.0
    return grid[j] + d * 1e-4


def main():
    rng = np.random.default_rng(97)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (SIMULACION con pulsar y detector ILUSTRATIVOS, semilla 97)",
           f"P = {P*1e3:.0f} ms ; anchura = {W} ciclos ; tasa pulsada = {RP} fot/s ; fondo = {RB} fot/s"]
    res = {}
    phi = (np.arange(NB) + 0.5) / NB
    lam = perfil_tasa(phi)
    dl = (perfil_tasa(phi + 1e-6) - perfil_tasa(phi - 1e-6)) / 2e-6
    info_por_s = np.sum(dl**2 / lam) / NB  # (1/s) * (1/ciclo^2)
    out.append("T [s]        sigma_t emp [us]   cota CR [us]   cociente   sigma alcance equivalente c sigma_t [m]")
    ok = True
    sig = {}
    for T in (1e3, 1e4, 1e5):
        est = []
        for _ in range(150):
            cuentas = rng.poisson(tasa_bin(0.0) * T / NB)
            est.append(estima(cuentas, T))
        s_emp = float(np.std(est, ddof=1) * P)
        s_cr = P / math.sqrt(T * info_por_s)
        out.append(f"{T:9.0e}    {s_emp*1e6:14.3f}   {s_cr*1e6:12.3f}   {s_emp/s_cr:8.3f}   {C*s_emp:14.1f}")
        k = f"{int(math.log10(T))}"
        res[f"emp{k}"] = s_emp * 1e6; res[f"cr{k}"] = s_cr * 1e6; res[f"raz{k}"] = s_emp / s_cr; res[f"m{k}"] = C * s_emp
        sig[T] = s_emp
        ok &= abs(s_emp / s_cr - 1) < 0.25
    # posicion con tres pulsares
    Nn = np.array([[1, 0, 0], [0.2, 0.9, 0.3], [-0.3, 0.2, 0.9]], dtype=float)
    Nn /= np.linalg.norm(Nn, axis=1)[:, None]
    dop = math.sqrt(np.trace(np.linalg.inv(Nn.T @ Nn)))
    out.append(f"Geometria de tres pulsares sinteticos: factor de dilucion = {dop:.2f}")
    for T in (1e3, 1e4, 1e5):
        sr = C * sig[T] * dop
        out.append(f"T = {T:7.0e} s: sigma de posicion 3D = {sr/1e3:.2f} km")
        res[f"pos{int(math.log10(T))}"] = sr / 1e3
    res["dop"] = dop
    r13 = res["pos3"] / res["pos5"]
    out.append(f"Cociente sigma(1e3 s)/sigma(1e5 s) = {r13:.2f} (esperado 10)")
    res["r13"] = r13
    ok &= 7 < r13 < 14
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
