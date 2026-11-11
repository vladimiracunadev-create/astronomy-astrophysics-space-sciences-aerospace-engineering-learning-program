#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C07: pendulo invertido controlado con ruido sensorial y re-ponderacion de la informacion vestibular.

TODO SINTETICO/ILUSTRATIVO: cuerpo de masa m = 70 kg, centro de masa a h = 1.0 m, momento I = m h^2; constantes de control inventadas; no describe a
una persona ni a un astronauta. Sistema: angulo th (rad) respecto de la vertical, positivo hacia delante; g = 9.80665 m/s2.
Dinamica linealizada: I th'' = m g h th - Kp th - Kd th' + ruido de par. Estabilidad (analitica): Kp > m g h = 686.5 N m/rad.
Control con estimacion sensorial: th_est = w_v * th_vest + (1 - w_v) * th_otro, cada fuente con su ruido (vestibular 0.20 deg, otras 0.35 deg,
ilustrativos); w_v es el peso vestibular. Una condicion degradada (simula superficie inestable) multiplica el ruido de las otras fuentes por 4.
Verificacion: (a) con Kp < m g h el pendulo diverge; con Kp > m g h el balanceo es acotado; (b) la desviacion del estimador ponderado medida por Monte Carlo
coincide con sqrt(w^2 s_v^2 + (1-w)^2 s_o^2) y su minimo esta en w* = s_o^2/(s_v^2 + s_o^2); (c) el balanceo RMS simulado
con la condicion degradada es menor con w_v = 1 que con w_v = 0. Semilla 107. Euler explicito, dt = 0.005 s. Numpy.
Tolerancias: desviacion del estimador a +-2 % de la analitica; minimo en la malla = w* redondeado a +-0.05; RMS(w=1) < RMS(w=0) con degradacion.
"""
from __future__ import annotations
import platform
import numpy as np

G, M, H = 9.80665, 70.0, 1.0
I = M * H**2
KP, KD = 900.0, 250.0
SV, SO = np.radians(0.20), np.radians(0.35)


def simula(kp, wv, so_mult, rng, T=60.0, dt=0.005, ruido_par=8.0):
    n = int(T / dt)
    th, om = 0.001, 0.0
    sv, so = SV, SO * so_mult
    thr = np.zeros(n)
    for i in range(n):
        est = wv * (th + rng.normal(0, sv)) + (1 - wv) * (th + rng.normal(0, so))
        par = -kp * est - KD * om + rng.normal(0, ruido_par)
        acc = (M * G * H * th + par) / I
        om += acc * dt
        th += om * dt
        thr[i] = th
        if abs(th) > 0.5:
            return thr[: i + 1], True
    return thr, False


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): masa 70 kg, h 1.0 m, g 9.80665 m/s2; ruidos 0.20 y 0.35 deg")
    mgh = M * G * H
    print(f"Umbral de rigidez para estabilidad: m g h = {mgh:.1f} N m/rad; Kp usado = {KP:.0f}")
    for kp in (500.0, 900.0):
        thr, cae = simula(kp, 0.5, 1.0, rng)
        print(f"Kp = {kp:.0f}: {'diverge (cae antes de 60 s)' if cae else 'balanceo acotado'}; RMS = {np.degrees(np.sqrt(np.mean(thr**2))):.3f} deg")
        assert cae == (kp < mgh)
    ws = np.linspace(0, 1, 11)
    for mult, nombre in ((1.0, "superficie firme"), (4.0, "otras fuentes degradadas x4")):
        so = SO * mult
        est = []
        for w in ws:
            x = w * rng.normal(0, SV, 200000) + (1 - w) * rng.normal(0, so, 200000)
            teo = np.sqrt(w**2 * SV**2 + (1 - w) ** 2 * so**2)
            assert abs(x.std() - teo) / teo <= 0.02
            est.append(np.degrees(x.std()))
        wopt = so**2 / (SV**2 + so**2)
        wsim = float(ws[int(np.argmin(est))])
        print(f"{nombre}: desviacion del estimador (deg) por w_v 0..1 paso 0.1 = " + ", ".join(f"{e:.3f}" for e in est))
        print(f"  w* analitico = {wopt:.2f}; minimo en la malla = {wsim:.1f}")
        assert abs(wsim - wopt) <= 0.05 + 1e-9
        rms = []
        for w in (0.0, 1.0):
            thr, _ = simula(KP, w, mult, np.random.default_rng(107))
            rms.append(np.degrees(np.sqrt(np.mean(thr**2))))
        print(f"  balanceo RMS simulado (60 s): w_v = 0 -> {rms[0]:.3f} deg; w_v = 1 -> {rms[1]:.3f} deg")
        if mult > 1:
            assert rms[1] < rms[0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
