#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C15: varianza cosmica del espectro angular y precision maxima de una amplitud.

Datos: ninguna constante fisica ni dato observado. Todo es SINTETICO con semilla 20261109: el espectro verdadero entra solo como factor de escala (se trabaja con cocientes C^_l / C_l) y
l_max, f_sky y el numero de repeticiones son ilustrativos. No se cita ninguna medicion del cuadrupolo real.
Modelo: para un campo gaussiano y cielo completo, (2l+1) C^_l / C_l sigue una distribucion chi^2 con 2l+1 grados de libertad: media 1, varianza 2/(2l+1). La probabilidad acumulada de chi^2_5
se calcula con la serie de la gamma incompleta regularizada. La amplitud A de un espectro de forma conocida se estima con A^/A = sum (2l+1) x_l / sum (2l+1), con varianza 2 / sum (2l+1);
con mascara se anota la correccion de primer orden f_sky (no simulada).
Supuestos: campo gaussiano e isotropo, sin ruido, sin mascara en la simulacion, modos l independientes. Validez: ilustrativa.
Tolerancia: desviacion simulada frente a sqrt(2/(2l+1)) a 3 % (20000 repeticiones); probabilidad simulada del cuadrupolo bajo frente a la analitica a 0,01; precision de la amplitud a 3 %.
"""
from __future__ import annotations
import math, platform, random, sys

def gamma_inc_reg(a, x):
    # P(a, x) por serie: x^a e^-x / Gamma(a+1) * suma x^k / ((a+1)...(a+k))
    s = t = 1.0 / a
    for k in range(1, 400):
        t *= x / (a + k)
        s += t
        if abs(t) < 1e-16 * abs(s):
            break
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))

def chi2_cdf(x, nu):
    return gamma_inc_reg(nu / 2.0, x / 2.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    nrep = 20000
    print(f"{'l':>5} {'sigma simulada':>15} {'sqrt(2/(2l+1))':>15} {'cociente':>9} {'p5 %':>8} {'p95 %':>8} {'metodo':>8}")
    for l in (2, 5, 10, 30, 100, 1000):
        nu = 2 * l + 1
        xs = []
        for _ in range(nrep):
            if l <= 30:
                s = sum(rng.gauss(0, 1) ** 2 for _ in range(nu))
            else:
                s = 2 * rng.gammavariate(nu / 2.0, 1.0)
            xs.append(s / nu)
        m = sum(xs) / nrep
        sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (nrep - 1))
        xs.sort()
        teo = math.sqrt(2.0 / nu)
        print(f"{l:5d} {sd:15.5f} {teo:15.5f} {sd / teo:9.3f} {xs[int(0.05 * nrep)]:8.3f} {xs[int(0.95 * nrep)]:8.3f} {'directo' if l <= 30 else 'gamma':>8}")
        assert abs(sd / teo - 1) < 0.03
    # cuadrupolo: probabilidad de C^_2 < 0.5 C_2
    nu = 5
    p_teo = chi2_cdf(0.5 * nu, nu)
    cnt = 0
    for _ in range(nrep):
        if sum(rng.gauss(0, 1) ** 2 for _ in range(nu)) < 0.5 * nu:
            cnt += 1
    print(f"P(C^_2 < 0,5 C_2): analitica (chi^2 con 5 gl) = {p_teo:.4f} ; simulada = {cnt / nrep:.4f}")
    assert abs(cnt / nrep - p_teo) < 0.01
    # precision de la amplitud
    print(f"{'l_max':>6} {'f_sky':>6} {'modos (2l+1) f_sky':>20} {'sigma(A)/A = sqrt(2/modos)':>28}")
    for lm in (30, 200, 1000, 2000):
        for fs in (1.0, 0.6):
            modos = ((lm + 1) ** 2 - 4) * fs
            print(f"{lm:6d} {fs:6.1f} {modos:20.0f} {math.sqrt(2 / modos):28.5f}")
    lm = 200
    pesos = [2 * l + 1 for l in range(2, lm + 1)]
    ests = []
    for _ in range(5000):
        tot = 0.0
        for l, w in zip(range(2, lm + 1), pesos):
            tot += 2 * rng.gammavariate(w / 2.0, 1.0)      # = w * x_l
        ests.append(tot / sum(pesos))
    m = sum(ests) / len(ests)
    sd = math.sqrt(sum((e - m) ** 2 for e in ests) / (len(ests) - 1))
    teo = math.sqrt(2.0 / sum(pesos))
    print(f"l_max = {lm}, cielo completo: sigma(A)/A simulada = {sd:.5f} ; teorica = {teo:.5f} ; cociente = {sd / teo:.3f}")
    assert abs(sd / teo - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
