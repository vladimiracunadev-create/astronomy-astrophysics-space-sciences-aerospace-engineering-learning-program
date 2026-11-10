#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C16: modelo de reloj, estabilidad (desviacion de Allan) y efecto de un error de tiempo en la medida.

Constante consultada (NIST, 2026-11-10): c = 299 792 458 m/s. Todo lo demas SINTETICO: reloj con desfase inicial 2 us, deriva de frecuencia
(fraccional) 1e-9, ruido blanco de frecuencia de 1e-11 a tau = 1 s (ILUSTRATIVO) y paseo aleatorio de frecuencia 1e-13 por raiz de segundo; semilla 59.
Se simulan 20 000 s con paso de 1 s. Se ajusta un polinomio de grado 1 (desfase y deriva) a una ventana de 600 s y se mide el residuo; se calcula la
desviacion de Allan (no solapada) para tau = 1, 10, 100, 1000 s; se convierte un error de tiempo de 1 us en error de alcance (c dt/2 para ida y vuelta,
c dt para una via) y en posicion de una nave a 7.5 km/s. Transferencia de tiempo de dos sentidos: error = asimetria/2.
Tolerancias: la pendiente ajustada coincide con la deriva verdadera dentro del 5 %; Allan(1 s) cercano al ruido blanco de frecuencia inyectado (dentro del 25 %).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

C = 299792458.0


def allan(x, tau0, m):
    """Desviacion de Allan no solapada a partir de la fase x (s) para tau = m tau0."""
    xs = x[::m]
    d2 = xs[2:] - 2 * xs[1:-1] + xs[:-2]
    return math.sqrt(0.5 * np.mean(d2**2)) / (m * tau0)


def main():
    rng = np.random.default_rng(59)
    n, tau0 = 20000, 1.0
    t = np.arange(n) * tau0
    x0, y0, D = 2e-6, 1e-9, 1e-14  # s, adim, 1/s  (desfase, deriva inicial de frecuencia, deriva lineal)
    wfm = 1e-11  # ruido blanco de frecuencia a tau0
    rw = 1e-13 * math.sqrt(tau0)  # paseo aleatorio de frecuencia por paso
    y_noise = rng.normal(0, wfm, n)
    y_rw = np.cumsum(rng.normal(0, rw, n))
    y = y0 + D * t + y_noise + y_rw
    x = x0 + np.cumsum(y) * tau0
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (reloj SINTETICO, semilla 59)"]
    res = {}
    # ajuste lineal en ventana de 600 s
    w = slice(0, 600)
    p = np.polyfit(t[w], x[w], 1)
    resid = x[w] - np.polyval(p, t[w])
    out.append(f"Ajuste lineal en 600 s: desfase = {p[1]*1e6:.4f} us ; frecuencia = {p[0]:.4e} (verdadera media {np.mean(y[w]):.4e}) ; residuo rms = {np.std(resid)*1e9:.2f} ns")
    out.append(f"Residuo extrapolado 1 h despues: error de prediccion = {abs(x[3600]-np.polyval(p, t[3600]))*1e6:.3f} us")
    res.update(off_us=float(p[1] * 1e6), freq=float(p[0]), freq_true=float(np.mean(y[w])), res_ns=float(np.std(resid) * 1e9),
               pred_us=float(abs(x[3600] - np.polyval(p, t[3600])) * 1e6))
    out.append("tau [s]   Allan")
    ad = {}
    for m in (1, 10, 100, 1000):
        a = allan(x, tau0, m)
        out.append(f"{m*tau0:7.0f}   {a:.3e}")
        ad[m] = a
        res[f"adev{m}"] = a
    out.append(f"Ruido blanco de frecuencia inyectado = {wfm:.1e} a 1 s (Allan(1 s) / inyectado = {ad[1]/wfm:.3f})")
    dt = 1e-6
    out.append(f"Un error de tiempo de {dt*1e6:.0f} us equivale a: alcance de ida y vuelta c dt / 2 = {C*dt/2:.1f} m ; a una via c dt = {C*dt:.1f} m ; posicion de una nave a 7.5 km/s = {7.5e3*dt*1e3:.2f} mm")
    res.update(c_dt2=C * dt / 2, c_dt=C * dt, pos_mm=7.5e3 * dt * 1e3)
    asim = 20e-9
    out.append(f"Transferencia de tiempo de dos sentidos: asimetria de trayecto de {asim*1e9:.0f} ns -> error de desfase = {asim/2*1e9:.1f} ns")
    res["tt_ns"] = asim / 2 * 1e9
    ok = abs(p[0] / np.mean(y[w]) - 1) < 0.05 and abs(ad[1] / wfm - 1) < 0.25
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
