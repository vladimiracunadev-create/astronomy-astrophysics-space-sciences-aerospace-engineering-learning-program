#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C09: retardo geometrico, tasa de franjas y fringe stopping en una linea de base este-oeste.

Datos: c de NIST CODATA 2022 (exacta, consultada el 2026-11-09). La velocidad de rotacion terrestre (7,292115e-5 rad/s, valor sideral convencional) es un valor estandar NO consultado
en esta sesion. La linea de base (1000 m), la declinacion (30 grados), la frecuencia (1,4 GHz) y los tiempos de integracion son ILUSTRATIVOS.
Modelo: tau_g(t) = -(B/c) cos(dec) sin(H), H = H0 + omega t; fase = 2 pi nu tau_g; tasa de franjas f = d(fase)/dt / (2 pi) = -(nu B omega / c) cos(dec) cos(H).
Segunda via: la tasa analitica frente a la derivada numerica de la fase; la perdida de coherencia por promediar sin detener las franjas frente a |sinc(f T)|; el error residual por un
retardo de modelo equivocado.
Supuestos: linea de base fija, fuente puntual en el infinito, sin refraccion atmosferica. Validez: ilustrativa.
Tolerancia: derivada numerica a 1e-6 relativo de la tasa analitica; coherencia numerica dentro de 1e-4 de |sinc|.
"""
from __future__ import annotations
import cmath, math, platform, sys

C = 299792458.0
OMEGA = 7.292115e-5

def sinc(x):
    return 1.0 if x == 0 else math.sin(math.pi * x) / (math.pi * x)

def compute():
    B, dec, nu = 1000.0, math.radians(30), 1.4e9
    H0 = 0.0
    tau = lambda t: -(B / C) * math.cos(dec) * math.sin(H0 + OMEGA * t)
    phase = lambda t: 2 * math.pi * nu * tau(t)
    f_an = lambda t: -(nu * B * OMEGA / C) * math.cos(dec) * math.cos(H0 + OMEGA * t)
    R = dict(B=B, dec=math.degrees(dec), nu=nu, tau_max=B / C * math.cos(dec), f0=f_an(0.0))
    h = 0.01
    R["f_num"] = (phase(h) - phase(-h)) / (2 * h) / (2 * math.pi)
    R["rows"] = []
    for T in (0.5, 1.0, 3.39, 10.0):
        n = 20000
        s = sum(cmath.exp(1j * phase(-T / 2 + T * (k + 0.5) / n)) for k in range(n)) / n
        R["rows"].append((T, abs(s), abs(sinc(R["f0"] * T))))
    # error de retardo de modelo
    dt = 10e-12
    R["dphi"] = 2 * math.pi * nu * dt
    R["coh_dt"] = math.cos(R["dphi"])
    # actualizacion del modelo cada Tu segundos
    Tu = 2.0
    Tm = 20000
    s = sum(cmath.exp(1j * (phase(Tu * ((k + 0.5) / Tm - 0.5)) - phase(0) - 2 * math.pi * R["f0"] * Tu * ((k + 0.5) / Tm - 0.5))) for k in range(Tm)) / Tm
    R["coh_upd"] = abs(s)
    R["Tcoh"] = 1.0 / (4 * abs(R["f0"]))      # tiempo para que la fase cambie un cuarto de ciclo
    R["tau_rate_ps_s"] = abs(R["f0"]) / nu * 1e12
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"B = {R['B']:.0f} m ; dec = {R['dec']:.0f} grados ; nu = {R['nu'] / 1e9:.1f} GHz ; retardo geometrico maximo = {R['tau_max'] * 1e6:.4f} us")
    print(f"tasa de franjas en H = 0: analitica = {R['f0']:.6f} Hz ; derivada numerica = {R['f_num']:.6f} Hz ; la tasa de retardo es {R['tau_rate_ps_s']:.1f} ps/s")
    assert abs(R["f_num"] / R["f0"] - 1) < 1e-6
    print("   T [s]   |<exp(i fase)>| numerico   |sinc(f T)|")
    for T, a, b in R["rows"]:
        print(f"{T:8.2f} {a:20.5f} {b:14.5f}")
        assert abs(a - b) < 1e-4
    print(f"error de retardo de 10 ps -> error de fase = {R['dphi']:.4f} rad ; coherencia cos = {R['coh_dt']:.5f}")
    print(f"con el modelo actualizado cada 2 s: coherencia residual = {R['coh_upd']:.5f} ; un cuarto de ciclo en {R['Tcoh']:.3f} s sin detener las franjas")
    assert R["coh_upd"] > 0.99 and R["rows"][-1][1] < 0.2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
