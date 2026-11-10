#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C02: modelo de error de un acelerometro (sesgo, factor de escala, ruido) y varianza de Allan.

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80002). Ninguno procede de un sensor real ni de una hoja de datos.
Modelo: f_medida = (1 + s) f + b + n_w + b_rw, con f en m/s2; s = factor de escala (adimensional);
  b = sesgo constante; n_w = ruido blanco de densidad N (m/s2/sqrt(Hz)); b_rw = paseo aleatorio del sesgo (densidad K, m/s2*sqrt(Hz)).
Parametros ilustrativos: s = 200 ppm, b = 2.0e-3 m/s2, N = 5.0e-4 m/s2/sqrt(Hz) (equivale a un paseo aleatorio de velocidad VRW = N m/s/sqrt(s)),
  K = 1.0e-6 m/s2*sqrt(Hz), frecuencia de muestreo 100 Hz, duracion 1 h.
Identidades de referencia (varianza de Allan, definicion IEEE para ruido blanco y paseo aleatorio): sigma_A^2(tau) = N^2/tau + K^2 tau/3.
Segunda via: la formula cerrada frente a la varianza de Allan estimada de la serie simulada. Tolerancia: 15 % en los puntos de ruido blanco puro.
Sistema de referencia: ejes del cuerpo; unidades SI.
"""
from __future__ import annotations
import math, platform, random

FS = 100.0
S_ESC, B0, N_W, K_RW = 200e-6, 2.0e-3, 5.0e-4, 1.0e-6
DUR = 3600.0


def serie(seed=80002, dur=DUR, f_verd=0.0):
    rnd = random.Random(seed)
    dt = 1.0 / FS
    n = int(dur * FS)
    sig_w = N_W / math.sqrt(dt)
    sig_k = K_RW * math.sqrt(dt)
    b = 0.0
    out = []
    for _ in range(n):
        b += rnd.gauss(0.0, sig_k)
        out.append((1.0 + S_ESC) * f_verd + B0 + b + rnd.gauss(0.0, sig_w))
    return out


def allan(x, m):
    """Desviacion de Allan solapada con grupos de m muestras: x son medidas de aceleracion (promedios de grupo)."""
    n = len(x)
    # promedios acumulados para eficiencia
    cs = [0.0]
    for v in x:
        cs.append(cs[-1] + v)
    prom = [(cs[i + m] - cs[i]) / m for i in range(0, n - m + 1)]
    suma = 0.0
    k = 0
    for i in range(0, len(prom) - m):
        d = prom[i + m] - prom[i]
        suma += d * d
        k += 1
    return math.sqrt(suma / (2.0 * k))


def formula(tau):
    return math.sqrt(N_W ** 2 / tau + K_RW ** 2 * tau / 3.0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    x0 = serie()
    prom = sum(x0) / len(x0)
    print(f"Datos SINTETICOS, semilla 80002, {len(x0)} muestras a {FS:.0f} Hz. Fuerza especifica verdadera 0: media medida = {prom:.4e} m/s2 (sesgo fijo {B0:.1e} + paseo)")
    # Efecto del factor de escala: con f = 1 m/s2
    x1 = serie(f_verd=1.0)
    print(f"Con f = 1.000 m/s2 la media medida es {sum(x1) / len(x1):.6f} m/s2 (esperado {1 + S_ESC + B0:.6f} + paseo del sesgo)")
    print(" tau [s]   sigma_A simulada [m/s2]   sigma_A formula [m/s2]   cociente")
    # Quitar el sesgo constante no cambia la varianza de Allan (diferencias de promedios)
    for tau in (0.1, 1.0, 10.0, 100.0, 300.0):
        m = int(round(tau * FS))
        a = allan(x0, m)
        f = formula(tau)
        print(f"{tau:8.1f} {a:25.4e} {f:24.4e} {a / f:10.3f}")
    # Minimo de la curva: tau_min = sqrt(3) N / K
    tau_min = math.sqrt(3.0) * N_W / K_RW
    print(f"Minimo teorico en tau = sqrt(3) N/K = {tau_min:.1f} s, sigma_min = {formula(tau_min):.3e} m/s2")
    # Error de velocidad y posicion tras 60 s con solo el sesgo constante y el ruido blanco
    t = 60.0
    print(f"Tras {t:.0f} s: error de velocidad por sesgo = {B0 * t:.4f} m/s ; error de posicion = {0.5 * B0 * t * t:.3f} m ; por ruido blanco (1 sigma) velocidad = {N_W * math.sqrt(t):.5f} m/s")
    # Comprobaciones
    a1 = allan(x0, int(round(1.0 * FS)))
    a10 = allan(x0, int(round(10.0 * FS)))
    assert abs(a1 / formula(1.0) - 1.0) < 0.15
    assert abs(a10 / formula(10.0) - 1.0) < 0.15
    assert abs(a1 / a10 - math.sqrt(10.0)) / math.sqrt(10.0) < 0.2
    assert abs(sum(x1) / len(x1) - (1 + S_ESC + B0)) < 3e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
