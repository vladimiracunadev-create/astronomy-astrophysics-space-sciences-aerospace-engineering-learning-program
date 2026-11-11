#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C03: canal semicircular como filtro paso alto, ambiguedad inclinacion-traslacion y aprendizaje del entrenamiento.

TODO SINTETICO/ILUSTRATIVO: constantes inventadas de orden de magnitud plausible; no son mediciones de personas.
Sistema: velocidad angular de la cabeza w (deg/s) y aceleracion lineal a (m/s2) en el eje interaural; g = 9.80665 m/s2 (valor convencional).
Modelo 1 (canal): w_percibida' = -w_percibida/tau + w', con tau = 6 s (ilustrativo); en giro constante la sensacion decae como exp(-t/tau).
Modelo 2 (otolito): la fuerza especifica medida es f = g_vector - a; inclinar la cabeza un angulo th produce f_x = g sin(th), igual a una traslacion
a = g sin(th) (ambiguedad). Modelo 3 (entrenamiento): el error de orientacion estimada decae por sesion como e_k = e_inf + (e_0 - e_inf) r^k.
Verificacion: Euler del canal frente a la solucion analitica; ajuste log-lineal de la curva de aprendizaje (semilla 107, ruido 0.5 deg).
Tolerancias: error maximo del canal <= 0.5 %; r ajustado dentro de +-0.03 de 0.85. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

G = 9.80665
TAU = 6.0


def canal(w, dt):
    y = np.zeros_like(w)
    for i in range(1, len(w)):
        y[i] = y[i - 1] + (w[i] - w[i - 1]) - dt * y[i - 1] / TAU
    return y


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): tau = 6 s, g = 9.80665 m/s2 (convencional)")
    dt = 0.01
    t = np.arange(0, 30, dt)
    w = np.where(t >= 1.0, 60.0, 0.0)  # escalon a 60 deg/s en t = 1 s
    y = canal(w, dt)
    ana = np.where(t >= 1.0, 60.0 * np.exp(-(t - 1.0) / TAU), 0.0)
    err = float(np.max(np.abs(y - ana)) / 60.0 * 100)
    print(f"Giro constante 60 deg/s: sensacion a 10 s del inicio = {y[int(10/dt)]:.2f} deg/s (analitico {60*np.exp(-9/TAU):.2f}); error maximo = {err:.3f} % del escalon")
    assert err <= 0.5
    print(f"Tiempo en que la sensacion cae al 37 % (tau) = {TAU:.1f} s; al 10 % = {TAU*np.log(10):.1f} s")
    # ambiguedad inclinacion-traslacion
    for th in (5, 10, 20):
        a = G * np.sin(np.radians(th))
        print(f"Inclinacion de {th:2d} deg = traslacion equivalente a = {a:.3f} m/s2 ({a/G:.3f} g)")
    # curva de aprendizaje: 20 sesiones
    e0, einf, r = 20.0, 4.0, 0.85
    k = np.arange(20)
    e = einf + (e0 - einf) * r**k + rng.normal(0, 0.5, 20)
    A = np.vstack([np.ones(20), k]).T
    # ajuste log-lineal de (e - einf) conocido einf
    ok = (e - einf) > 0.3
    pend = np.polyfit(k[ok], np.log(e[ok] - einf), 1)
    r_aj = float(np.exp(pend[0]))
    print(f"Aprendizaje: error 20.0 -> {e[-1]:.2f} deg en 20 sesiones; r verdadero = {r}; r ajustado = {r_aj:.3f}")
    assert abs(r_aj - r) <= 0.03
    n95 = int(np.ceil(np.log(0.05) / np.log(r)))
    print(f"Sesiones para cerrar el 95 % de la brecha (e0 - einf): {n95} (= ln 0.05 / ln r)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
