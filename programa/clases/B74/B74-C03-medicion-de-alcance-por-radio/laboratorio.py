#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C03: alcance por radio, tiempo de ida y vuelta y precision del retardo.

Constante consultada (NIST, 2026-11-10): c = 299 792 458 m/s (exacta). Distancias de referencia (Luna 384 400 km, 1 au =
1.495978707e11 m) son ILUSTRATIVAS/no consultadas en esta sesion. Senal SINTETICA: pulso gaussiano muestreado con ruido blanco;
estimacion del retardo por Gauss-Newton; 3000 realizaciones, semilla 5.
Modelo: rho = c tau / 2 (ida y vuelta, ignorando el movimiento y la atmosfera). Cota de Cramer-Rao para el retardo:
sigma_tau = sigma_n / sqrt(sum s'(t_k)^2). Tolerancia: sigma empirica dentro del 10 % de la cota.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, platform, sys
import numpy as np

C = 299792458.0


def pulso(t, tau, s):
    return np.exp(-((t - tau) ** 2) / (2 * s**2))


def main():
    rng = np.random.default_rng(5)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (senal SINTETICA, semilla 5)"]
    res = {}
    out.append("Tiempo de ida y vuelta (RTLT) = 2 rho / c:")
    for nombre, rho in (("Luna 384400 km", 384.4e6), ("1 au", 1.495978707e11), ("Marte ~1.5 au", 1.5 * 1.495978707e11)):
        rt = 2 * rho / C
        out.append(f"  {nombre:16s} RTLT = {rt:10.4f} s")
        res["rt_" + nombre.split()[0]] = rt
    # error de alcance por error de retardo
    dt_ns = 1.0
    d_rho = C * dt_ns * 1e-9 / 2
    out.append(f"1 ns de error en el retardo de ida y vuelta = {d_rho*100:.2f} cm de alcance")
    res["d_rho_cm"] = d_rho * 100
    # movimiento durante el RTLT: LEO
    v, rt_leo = 7500.0, 2 * 1.0e6 / C
    out.append(f"LEO (rho = 1000 km, v = 7.5 km/s): RTLT = {rt_leo*1e3:.3f} ms ; la nave se mueve {v*rt_leo:.1f} m durante la medida")
    res["rt_leo_ms"] = rt_leo * 1e3
    res["mov_leo"] = v * rt_leo
    # estimacion de retardo con ruido
    fs, s, tau0, sn = 100e6, 20e-9, 1.234e-6, 0.2  # Hz, s, s, amplitud ILUSTRATIVOS
    t = np.arange(0, 3e-6, 1 / fs)
    ds = (pulso(t, tau0 + 1e-12, s) - pulso(t, tau0 - 1e-12, s)) / 2e-12
    crlb = sn / np.sqrt(np.sum(ds**2))
    est = []
    for _ in range(3000):
        y = pulso(t, tau0, s) + rng.normal(0, sn, t.size)
        tau = t[np.argmax(np.convolve(y, pulso(np.arange(-5 * s, 5 * s, 1 / fs), 0, s), mode="same"))]
        for _ in range(8):
            r = y - pulso(t, tau, s)
            g = (pulso(t, tau + 1e-12, s) - pulso(t, tau - 1e-12, s)) / 2e-12
            tau += float(g @ r / (g @ g))
        est.append(tau)
    est = np.array(est)
    emp = float(np.std(est, ddof=1))
    sesgo = float(np.mean(est) - tau0)
    out.append(f"Pulso gaussiano s = {s*1e9:.0f} ns, muestreo {fs/1e6:.0f} MHz, ruido {sn}")
    out.append(f"sigma_tau empirica = {emp*1e9:.4f} ns ; cota de Cramer-Rao = {crlb*1e9:.4f} ns ; cociente = {emp/crlb:.3f}")
    out.append(f"sesgo medio = {sesgo*1e12:.2f} ps ; sigma de alcance = {C*emp/2*100:.3f} cm")
    ok = abs(emp / crlb - 1) < 0.10
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res.update(emp_ns=emp * 1e9, crlb_ns=crlb * 1e9, cociente=emp / crlb, sesgo_ps=sesgo * 1e12, s_rho_cm=C * emp / 2 * 100)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
