#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C14: reductores y transmisiones: relacion total, rendimiento del tornillo sin fin, holgura y resonancia torsional.

Datos: ILUSTRATIVOS (tornillo de una entrada, diametro primitivo 20 mm, avance 3 mm, coeficiente de friccion 0,1; corona de 144 dientes y radio primitivo 72 mm; etapa previa 1:5; motor de 200 pasos con 16 micropasos;
holgura 0,01 mm; rigidez torsional 2e4 N m/rad; inercia 0,5 kg m^2). Sin datos de fabricantes ni constantes externas (1 vuelta = 1296000", definicion).
Modelo: angulo de avance lambda = atan(L/(pi d)); rendimiento eta = tan(lambda)/tan(lambda + phi) con tan(phi) = mu, autobloqueo si lambda < phi.
Verificacion independiente del rendimiento: equilibrio de fuerzas de un bloque en un plano inclinado con friccion, resolviendo P = W (sin l + mu cos l)/(cos l - mu sin l) y eta = W tan(l)/P.
Resonancia: f = sqrt(k/J)/(2 pi) frente a la integracion numerica (Verlet, dt = 1e-5 s) del oscilador libre medida por cruces por cero.
Supuestos: friccion de Coulomb constante, engranajes rigidos salvo la rigidez torsional global, sin amortiguamiento. Validez: orden de magnitud.
Tolerancia: rendimiento por las dos vias, 1e-12 relativo; frecuencia simulada, 5e-4 relativo.
"""
from __future__ import annotations
import math, platform

D = 0.020; LEAD = 0.003; MU = 0.1
Z = 144; RW = 0.072; ETAPA = 5.0
PASOS = 200; MICRO = 16
HOLG = 1e-5
KT = 2e4; J = 0.5

def calc():
    r = {}
    lam = math.atan(LEAD / (math.pi * D)); phi = math.atan(MU)
    r["lambda_deg"] = math.degrees(lam); r["phi_deg"] = math.degrees(phi)
    r["autobloqueo"] = lam < phi
    eta = math.tan(lam) / math.tan(lam + phi)
    P = (math.sin(lam) + MU * math.cos(lam)) / (math.cos(lam) - MU * math.sin(lam))
    r["eta_trigonometrica"] = eta; r["eta_fuerzas"] = math.tan(lam) / P
    # rendimiento si se arrastra desde la rueda (retroceso): eta' = tan(l - phi)/tan(l) (si l > phi)
    r["ratio_total"] = ETAPA * Z
    r["micropasos_vuelta"] = PASOS * MICRO
    r["arcsec_por_micropaso"] = 1296000.0 / (PASOS * MICRO * r["ratio_total"])
    r["holgura_arcsec"] = HOLG / RW * 206264.806
    f_teo = math.sqrt(KT / J) / (2 * math.pi)
    r["f_resonancia_hz"] = f_teo
    dt = 1e-5; x = 1.0; v = 0.0; t = 0.0
    cruces = []
    a = -KT / J * x
    prev = x
    while len(cruces) < 21:
        v += 0.5 * a * dt; x += v * dt; a = -KT / J * x; v += 0.5 * a * dt; t += dt
        if prev > 0 >= x:
            cruces.append((t - dt) + dt * prev / (prev - x))
        prev = x
    # periodo: media de intervalos entre cruces descendentes
    r["f_simulada_hz"] = (len(cruces) - 1) / (cruces[-1] - cruces[0])
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.8g}" if not isinstance(v, bool) else f"{k} = {v}")
    assert r["autobloqueo"] is True
    assert abs(r["eta_trigonometrica"] - r["eta_fuerzas"]) / r["eta_fuerzas"] < 1e-12
    assert abs(r["f_simulada_hz"] - r["f_resonancia_hz"]) / r["f_resonancia_hz"] < 5e-4
    assert abs(r["ratio_total"] - 720.0) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
