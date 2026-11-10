#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C26: correccion atmosferica: reflectancia en el tope de la atmosfera, inversion y objeto oscuro.

Datos: SINTETICOS / ILUSTRATIVOS. Espesores opticos 0.35 (rojo, 0.66 um) y 0.15 (infrarrojo cercano, 0.86 um) como ejemplo, albedo de dispersion simple 0.95,
funcion de fase 0.2, albedo esferico 0.08, geometria con cenital solar 30 grados y vista al nadir, superficies sinteticas (rojo 0.05, NIR 0.45 para vegetacion).
La definicion de reflectancia de superficie es la del producto de USGS (consultada 2026-11-09), que no daba el algoritmo ni los factores de escala.
Modelo: rho_toa = rho_p + Td Tu rho_s/(1 - s rho_s), con rho_p = w0 tau P/(4 mu_s mu_v), Td = exp(-tau/mu_s), Tu = exp(-tau/mu_v); inversion
rho_s = (rho_toa - rho_p)/(Td Tu + s (rho_toa - rho_p)) ; objeto oscuro: se supone que el pixel mas oscuro tiene rho_s = 0.01.
Validez: atmosfera de una capa, superficie lambertiana. Tolerancia: ida y vuelta exacta a 1e-12.
"""
import math, platform

W0, P, S_ALB = 0.95, 0.2, 0.08
MUS, MUV = math.cos(math.radians(30.0)), 1.0
TAU = {"rojo": 0.35, "nir": 0.15}


def toa(rho_s, tau):
    rp = W0 * tau * P / (4 * MUS * MUV)
    td, tu = math.exp(-tau / MUS), math.exp(-tau / MUV)
    return rp + td * tu * rho_s / (1 - S_ALB * rho_s), rp, td * tu


def invertir(rho_toa, tau):
    _, rp, t = toa(0.0, tau)
    x = rho_toa - rp
    return x / (t + S_ALB * x)


def ndvi(n, r):
    return (n - r) / (n + r)


def calcular():
    r = {}
    rs = {"rojo": 0.05, "nir": 0.45}
    t = {b: toa(rs[b], TAU[b])[0] for b in rs}
    r["toa_rojo"], r["toa_nir"] = t["rojo"], t["nir"]
    rec = {b: invertir(t[b], TAU[b]) for b in rs}
    r["err_ida_vuelta"] = max(abs(rec[b] - rs[b]) for b in rs)
    r["ndvi_sup"] = ndvi(rs["nir"], rs["rojo"])
    r["ndvi_toa"] = ndvi(t["nir"], t["rojo"])
    r["ndvi_corr"] = ndvi(rec["nir"], rec["rojo"])
    r["ndvi_sesgo"] = r["ndvi_toa"] - r["ndvi_sup"]
    # objeto oscuro: el pixel mas oscuro (rho_s verdadero 0.02) se supone 0.01
    dark_toa = toa(0.02, TAU["rojo"])[0]
    rp_est = dark_toa - toa(0.0, TAU["rojo"])[2] * 0.01
    rec_dos = (t["rojo"] - rp_est) / (toa(0.0, TAU["rojo"])[2])
    r["rojo_dos"] = rec_dos
    r["err_dos"] = rec_dos - rs["rojo"]
    rp_ok = toa(0.01, TAU["rojo"])[0] - toa(0.0, TAU["rojo"])[2] * 0.01
    r["err_dos_ok"] = (t["rojo"] - rp_ok) / toa(0.0, TAU["rojo"])[2] - rs["rojo"]
    r["rojo_sin_corr_err"] = t["rojo"] - rs["rojo"]
    # sensibilidad a un error de 0.1 en tau
    r["err_tau"] = invertir(t["rojo"], TAU["rojo"] + 0.10) - rs["rojo"]
    r["Td_Tu_rojo"] = toa(0.0, TAU["rojo"])[2]
    r["rp_rojo"] = toa(0.0, TAU["rojo"])[1]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Superficie rojo 0.05 / NIR 0.45 -> TOA: rojo = {r['toa_rojo']:.5f} ; NIR = {r['toa_nir']:.5f}")
    print(f"Trayectoria Td*Tu (rojo) = {r['Td_Tu_rojo']:.4f} ; reflectancia de trayectoria (rojo) = {r['rp_rojo']:.5f}")
    print(f"Ida y vuelta (inversion): error maximo = {r['err_ida_vuelta']:.1e}")
    print(f"NDVI de superficie = {r['ndvi_sup']:.4f} ; NDVI en el TOA = {r['ndvi_toa']:.4f} (sesgo {r['ndvi_sesgo']:+.4f}) ; NDVI corregido = {r['ndvi_corr']:.4f}")
    print(f"Objeto oscuro: rojo recuperado = {r['rojo_dos']:.5f} (error {r['err_dos']:+.5f}) ; sin corregir el error del rojo en el TOA = {r['rojo_sin_corr_err']:+.5f}")
    print(f"Objeto oscuro con el supuesto correcto (0.01): error = {r['err_dos_ok']:+.5f}")
    print(f"Error de tau de +0.10 en el rojo: error de reflectancia = {r['err_tau']:+.5f}")
    assert r["err_ida_vuelta"] < 1e-12
    assert abs(r["ndvi_corr"] - r["ndvi_sup"]) < 1e-12
    assert abs(r["ndvi_sesgo"]) > 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
