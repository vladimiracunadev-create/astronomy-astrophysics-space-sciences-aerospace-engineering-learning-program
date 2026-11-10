#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C04: Doppler de dos sentidos, velocidad radial y ruido de la cuenta integrada.

Constante consultada (NIST, 2026-11-10): c = 299 792 458 m/s. Frecuencia de subida ILUSTRATIVA de 7.2 GHz (banda X, valor
redondeado NO tomado de ninguna especificacion consultada). Trayectoria SINTETICA: nave con velocidad radial que cambia
linealmente. Modelo de dos sentidos no relativista: f_D = -2 f_t (rho_dot / c) (positivo si se acerca); con correccion relativista
exacta f_D = f_t [ (1 - b)/(1 + b) - 1 ] para ida y vuelta con b = rho_dot/c (comparacion). Cuenta integrada: N = integral f_D dt.
Tolerancia: la velocidad recuperada del Doppler debe coincidir con la verdadera dentro de 1e-3 m/s de ruido (semilla 3);
el termino relativista debe ser < 1e-6 relativa a 30 km/s.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, platform, sys
import numpy as np

C = 299792458.0
FT = 7.2e9  # Hz, ILUSTRATIVA


def doppler_clasico(v):
    return -2.0 * FT * v / C


def doppler_exacto(v):
    b = v / C
    return FT * ((1 - b) / (1 + b) - 1)


def main():
    rng = np.random.default_rng(3)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (trayectoria SINTETICA, semilla 3)"]
    res = {}
    v = 30e3
    fc, fe = doppler_clasico(v), doppler_exacto(v)
    rel = abs(fe - fc) / abs(fc)
    out.append(f"f_t = {FT/1e9:.1f} GHz (ILUSTRATIVA); para rho_dot = {v/1e3:.0f} km/s: f_D clasica = {fc/1e3:.3f} kHz, exacta = {fe/1e3:.3f} kHz, dif. relativa = {rel:.2e}")
    res.update(fc_khz=fc / 1e3, fe_khz=fe / 1e3, rel=rel)
    # sensibilidad
    sens = 2 * FT / C
    out.append(f"Sensibilidad = 2 f_t / c = {sens:.4f} Hz por (m/s) ; 1 mm/s -> {sens*1e-3*1e3:.2f} mHz")
    res["sens"] = sens
    res["mhz_mm"] = sens * 1e-3 * 1e3
    # trayectoria sintetica
    t = np.arange(0, 600.0, 10.0)
    v_true = 1500.0 - 2.0 * t  # m/s, aceleracion constante ILUSTRATIVA
    sig_v = 0.05e-3  # m/s por muestra de 10 s (ILUSTRATIVO, 0.05 mm/s)
    fd = doppler_clasico(v_true) + rng.normal(0, sig_v * sens, t.size)
    v_rec = -fd * C / (2 * FT)
    err = v_rec - v_true
    out.append(f"Velocidad radial recuperada: rms del error = {np.sqrt(np.mean(err**2))*1e3:.4f} mm/s (entrada {sig_v*1e3:.3f} mm/s por muestra)")
    res["rms_mm"] = float(np.sqrt(np.mean(err**2)) * 1e3)
    # cuenta integrada: rango diferencial
    cuenta = np.cumsum(fd) * 10.0  # ciclos acumulados (regla del rectangulo)
    d_rho = -cuenta * C / (2 * FT)  # variacion de alcance respecto del inicio
    d_true = np.cumsum(v_true) * 10.0
    out.append(f"Variacion de alcance integrada tras {t[-1]:.0f} s = {d_rho[-1]/1e3:.4f} km (verdad {d_true[-1]/1e3:.4f} km)")
    res.update(drho_km=float(d_rho[-1] / 1e3), dtrue_km=float(d_true[-1] / 1e3))
    # el Doppler da la velocidad en la linea de vision, no la posicion: dos trayectorias con el mismo rho_dot pero distinto rho
    ok = rel < 1e-3 and np.sqrt(np.mean(err**2)) < 2 * sig_v and abs(d_rho[-1] - d_true[-1]) < 20.0
    out.append(f"Diferencia relativa clasica/exacta a 30 km/s = {rel:.2e} (termino de orden v/c = {v/C:.1e})")
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res["vc"] = v / C
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
