#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C04: respuesta de banda con pendiente de fase (retardo residual) y ondulacion por reflexion.

Datos: ninguna constante fisica. Banda de 128 MHz con 256 canales, retardo residual de 3,0 ns, reflexion de amplitud 0,05 y retardo 40 ns, ruido de fase por canal: todo
SINTETICO e ILUSTRATIVO (semilla 20261109).
Modelo: B(nu) = (1 + r exp(2 pi i nu tau_r)) exp(2 pi i nu tau_0) con caida de bordes. El retardo se ajusta con una recta a la fase desenvuelta; el retardo de la reflexion se halla con
la transformada de Fourier discreta de la amplitud.
Segunda via: desviacion tipica del retardo ajustado frente a sigma_fase / (2 pi sigma_nu sqrt(N)) y un Monte Carlo; pico de la transformada frente al retardo inyectado.
Supuestos: ruido de fase gaussiano e igual en todos los canales; r pequeno. Validez: ilustrativa.
Tolerancia: retardo ajustado dentro de 0,05 ns sin ruido; desviacion Monte Carlo dentro de 10 % de la formula; pico de ondulacion dentro de una celda de retardo.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def compute():
    rng = random.Random(20261109)
    N, bw = 256, 128.0e6
    nu = [(k - (N - 1) / 2) * bw / N for k in range(N)]       # frecuencia relativa al centro (Hz)
    tau0, r, taur = 3.0e-9, 0.05, 40.0e-9
    def B(k):
        return (1 + r * cmath.exp(2j * math.pi * nu[k] * taur)) * cmath.exp(2j * math.pi * nu[k] * tau0)
    def fit_delay(ph):
        mx = sum(nu) / N; my = sum(ph) / N
        sxy = sum((a - mx) * (b - my) for a, b in zip(nu, ph)); sxx = sum((a - mx) ** 2 for a in nu)
        return sxy / sxx / (2 * math.pi)
    def unwrap(p):
        out = [p[0]]
        for x in p[1:]:
            d = x - out[-1]
            d -= 2 * math.pi * round(d / (2 * math.pi))
            out.append(out[-1] + d)
        return out
    R = dict(N=N, bw=bw, tau0=tau0, r=r, taur=taur)
    ph = unwrap([cmath.phase(B(k)) for k in range(N)])
    R["fit0"] = fit_delay(ph)
    sphi = 0.05
    snu = math.sqrt(sum(x * x for x in nu) / N)
    R["sphi"] = sphi; R["pred"] = sphi / (2 * math.pi * snu * math.sqrt(N))
    est = []
    for _ in range(2000):
        p = unwrap([cmath.phase(B(k)) + rng.gauss(0, sphi) for k in range(N)])
        est.append(fit_delay(p))
    mu = sum(est) / len(est)
    R["mc_mu"] = mu; R["mc_sd"] = math.sqrt(sum((e - mu) ** 2 for e in est) / (len(est) - 1))
    # ondulacion: DFT de la amplitud
    amp = [abs(B(k)) for k in range(N)]
    m = sum(amp) / N
    best = (0, 0)
    dtau = 1.0 / bw / 4
    for q in range(1, 400):
        t = q * dtau
        s = abs(sum((a - m) * cmath.exp(-2j * math.pi * nu[k] * t) for k, a in enumerate(amp)))
        if s > best[0]:
            best = (s, t)
    R["rip_tau"] = best[1]; R["cell"] = 1.0 / bw; R["rip_amp"] = 2 * best[0] / N; R["period_mhz"] = 1e-6 / taur
    R["amp_pp"] = max(amp) - min(amp)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"canales = {R['N']} ; ancho de banda = {R['bw'] / 1e6:.0f} MHz ; retardo inyectado = {R['tau0'] * 1e9:.3f} ns")
    print(f"sin ruido: retardo ajustado = {R['fit0'] * 1e9:.4f} ns")
    assert abs(R["fit0"] - R["tau0"]) < 0.05e-9
    print(f"ruido de fase {R['sphi']} rad por canal: formula sigma_tau = {R['pred'] * 1e12:.2f} ps ; Monte Carlo (2000) = {R['mc_sd'] * 1e12:.2f} ps ; media = {R['mc_mu'] * 1e9:.4f} ns")
    assert abs(R["mc_sd"] / R["pred"] - 1) < 0.10
    print(f"ondulacion: periodo esperado = {R['period_mhz']:.1f} MHz ; pico en tau = {R['rip_tau'] * 1e9:.2f} ns (inyectado {R['taur'] * 1e9:.1f}) ; amplitud pico a pico de |B| = {R['amp_pp']:.4f}")
    assert abs(R["rip_tau"] - R["taur"]) < R["cell"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
