#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C12: oceanografia desde orbita: velocidad geostrofica y tendencia del nivel del mar.

Datos: SINTETICOS e ILUSTRATIVOS. Remolino gaussiano eta = eta0 exp(-r^2/(2 L^2)), eta0 = 0.20 m, L = 50 km, latitud -33 grados;
g = 9.80665 m s^-2 y Omega = 7.2921159e-5 rad/s (valores de referencia, no consultados en la sesion). Serie mensual de 30 anios con tendencia
de 3.0 mm/anio (VALOR ILUSTRATIVO, no es una medicion), ciclo anual de 40 mm y ruido de 20 mm. Semilla fija 57.
Modelo: v_theta = (g/f) d eta/dr con f = 2 Omega sen(lat); derivada numerica centrada en malla de 5 km frente a la solucion analitica;
tendencia por minimos cuadrados con terminos anual y semianual; incertidumbre de la pendiente = sigma sqrt([(A^T A)^-1]_11).
Validez: balance geostrofico (numero de Rossby pequeno), sin mareas ni correcciones. Tolerancia: derivada numerica frente a analitica < 1 %;
desviacion de la pendiente simulada frente a la analitica < 15 %.
Requiere numpy.
"""
import math, platform
import numpy as np

G, OM = 9.80665, 7.2921159e-5
ETA0, L = 0.20, 50e3
LAT = math.radians(-33.0)


def calcular():
    r = {}
    f = 2 * OM * math.sin(LAT)
    r["f"] = f
    h = 5e3
    x = np.arange(-200e3, 200e3 + h, h)
    eta = ETA0 * np.exp(-x**2 / (2 * L**2))
    v_num = (G / f) * np.gradient(eta, h)  # perfil que pasa por el centro: componente transversal
    v_ana = (G / f) * (-x / L**2) * eta
    sel = np.abs(x) <= 150e3
    r["v_max_ana"] = float(np.max(np.abs(v_ana)))
    r["v_max_num"] = float(np.max(np.abs(v_num[sel])))
    r["err_rel"] = float(np.max(np.abs(v_num[sel] - v_ana[sel])) / r["v_max_ana"])
    r["r_vmax_km"] = L / 1e3
    r["rossby"] = r["v_max_ana"] / (abs(f) * L)
    # serie temporal sintetica
    rng = np.random.default_rng(57)
    t = np.arange(360) / 12.0
    A = np.column_stack([np.ones_like(t), t, np.cos(2 * math.pi * t), np.sin(2 * math.pi * t), np.cos(4 * math.pi * t), np.sin(4 * math.pi * t)])
    sig = 0.020
    cov = np.linalg.inv(A.T @ A)
    r["sig_pend_ana"] = sig * math.sqrt(cov[1, 1]) * 1e3
    pend = []
    for _ in range(2000):
        y = 0.003 * t + 0.040 * np.cos(2 * math.pi * t + 0.7) + sig * rng.standard_normal(t.size)
        c = np.linalg.lstsq(A, y, rcond=None)[0]
        pend.append(c[1])
    pend = np.array(pend)
    r["pend_media"] = float(pend.mean() * 1e3)
    r["sig_pend_sim"] = float(pend.std() * 1e3)
    r["razon_sig"] = r["sig_pend_sim"] / r["sig_pend_ana"]
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Parametro de Coriolis f = {r['f']:.4e} s^-1 (lat -33 grados)")
    print(f"Velocidad geostrofica maxima: analitica = {r['v_max_ana']:.4f} m/s (en r = {r['r_vmax_km']:.0f} km) ; numerica = {r['v_max_num']:.4f} m/s ; error relativo = {r['err_rel']:.2e}")
    print(f"Numero de Rossby = v/(f L) = {r['rossby']:.3f}")
    print(f"Tendencia sintetica recuperada = {r['pend_media']:.3f} mm/anio (impuesta: 3.000) ; sigma analitica = {r['sig_pend_ana']:.3f} mm/anio ; sigma simulada = {r['sig_pend_sim']:.3f} mm/anio ; razon = {r['razon_sig']:.3f}")
    assert r["err_rel"] < 0.01
    assert abs(r["razon_sig"] - 1) < 0.15
    assert abs(r["pend_media"] - 3.0) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
