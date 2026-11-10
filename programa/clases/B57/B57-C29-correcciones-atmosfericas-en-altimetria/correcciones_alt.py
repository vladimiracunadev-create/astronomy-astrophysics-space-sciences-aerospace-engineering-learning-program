#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C29: correcciones atmosfericas en altimetria: retardo troposferico seco y ionosferico de dos frecuencias.

Datos: SINTETICOS / ILUSTRATIVOS. Frecuencias de 13.575 y 5.41 GHz (valores ilustrativos de un altimetro de doble frecuencia), contenido electronico total 20 y 50 TECU
(1 TECU = 1e16 electrones/m^2), presion de superficie 1013.25, 1000 y 700 hPa, latitud -33 grados, altura 0 y 3 km, ruido de distancia de 2 cm por frecuencia, semilla 57.
Las formulas del retardo ionosferico (40.3 TEC/f^2) y del retardo hidrostatico (tipo Saastamoinen: 0.0022768 P / (1 - 0.00266 cos 2 phi - 0.00028 h_km)) son conocimiento
general NO CONSULTADO en esta sesion; se usan para contrastar con el laboratorio y no como valores de referencia de una mision. La barometria inversa (1 hPa ~ 1 cm de nivel) se calcula
con densidad 1025 kg/m^3 y g = 9.80665.
Modelo: R_i = R + d_ion(f_i) con d_ion = 40.3e16 TECU /f^2 ; combinacion libre de ionosfera R_if = (f1^2 R1 - f2^2 R2)/(f1^2 - f2^2) ; amplificacion del ruido sqrt((f1^4+f2^4))/(f1^2-f2^2).
Validez: ionosfera de primer orden. Tolerancia: la combinacion recupera la distancia exacta a 1e-9 m sin ruido; la amplificacion simulada frente a la analitica < 3 %.
Requiere numpy.
"""
import math, platform
import numpy as np

F1, F2 = 13.575e9, 5.41e9


def d_ion(tecu, f):
    return 40.3 * tecu * 1e16 / f**2


def d_hid(P, lat_deg, h_km):
    return 0.0022768 * P / (1 - 0.00266 * math.cos(2 * math.radians(lat_deg)) - 0.00028 * h_km)


def combinar(R1, R2):
    return (F1**2 * R1 - F2**2 * R2) / (F1**2 - F2**2)


def calcular():
    r = {}
    for tec in (20, 50):
        r[f"ion_ku_{tec}"] = d_ion(tec, F1)
        r[f"ion_c_{tec}"] = d_ion(tec, F2)
    for P in (1013.25, 1000.0, 700.0):
        r[f"hid_{int(P)}"] = d_hid(P, -33.0, 0.0)
    r["hid_3km_700"] = d_hid(700.0, -33.0, 3.0)
    R = 1336000.123
    R1, R2 = R + d_ion(50, F1), R + d_ion(50, F2)
    r["err_if"] = abs(combinar(R1, R2) - R)
    amp = math.sqrt(F1**4 + F2**4) / (F1**2 - F2**2)
    r["amp_ana"] = amp
    rng = np.random.default_rng(57)
    n1 = 0.02 * rng.standard_normal(200000)
    n2 = 0.02 * rng.standard_normal(200000)
    rif = combinar(R + n1, R + n2) - R
    r["sig_if"] = float(rif.std())
    r["amp_sim"] = r["sig_if"] / 0.02
    r["razon_amp"] = r["amp_sim"] / amp
    r["inv_baro_mm_hpa"] = 100.0 / (1025.0 * 9.80665) * 1e3
    r["efecto_30hpa_cm"] = 30 * r["inv_baro_mm_hpa"] / 10
    r["d30"] = d_hid(30.0, -33.0, 0.0) * 100
    r["ruido_if_cm"] = r["sig_if"] * 100
    r["ion_ku_5"] = d_ion(5, F1) * 100
    r["dif_ion_ku_c_50"] = r["ion_c_50"] - r["ion_ku_50"]
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Retardo ionosferico 50 TECU: Ku (13.575 GHz) = {r['ion_ku_50']*100:.2f} cm ; C (5.41 GHz) = {r['ion_c_50']*100:.2f} cm ; 20 TECU: Ku = {r['ion_ku_20']*100:.2f} cm ; C = {r['ion_c_20']*100:.2f} cm")
    print(f"Retardo hidrostatico (lat -33, nivel del mar): 1013.25 hPa = {r['hid_1013']:.4f} m ; 1000 hPa = {r['hid_1000']:.4f} m ; 700 hPa = {r['hid_700']:.4f} m ; 700 hPa a 3 km = {r['hid_3km_700']:.4f} m")
    print(f"Combinacion libre de ionosfera: error sin ruido = {r['err_if']:.1e} m")
    print(f"Amplificacion del ruido: analitica = {r['amp_ana']:.4f} ; simulada = {r['amp_sim']:.4f} ; razon = {r['razon_amp']:.4f} ; ruido de 2 cm -> {r['sig_if']*100:.2f} cm")
    print(f"Barometria inversa: 1 hPa = {r['inv_baro_mm_hpa']:.2f} mm de nivel del mar ; 30 hPa = {r['efecto_30hpa_cm']:.1f} cm")
    assert r["err_if"] < 1e-9
    assert abs(r["razon_amp"] - 1) < 0.03
    assert r["ion_ku_50"] < r["ion_c_50"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
