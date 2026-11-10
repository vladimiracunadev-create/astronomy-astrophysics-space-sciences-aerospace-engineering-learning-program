#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C09: probabilidad de impacto como integral de una gaussiana en el plano B.

Datos: escenario SINTETICO. Radio terrestre ecuatorial 6378.137 km y velocidad de escape en superficie 11.186 km/s: valores del autor, no consultados en esta sesion. Velocidad de aproximacion v_inf =
12 km/s, desviaciones (12000, 3000) km y centro (15000, 4000) km: ILUSTRATIVOS. No describe ningun objeto real.
Modelo: el plano B es el plano perpendicular a la velocidad relativa en el infinito; el blanco es un disco de radio b = R sqrt(1 + v_esc^2 / v_inf^2) (enfoque gravitatorio); la distribucion de la posicion
del objeto es gaussiana bidimensional con ejes alineados. P = integral de la densidad sobre el disco. Tres vias: cuadratura polar (400 x 720), aproximacion P ~ pi b^2 f(centro) y Monte Carlo (1 500 000
muestras, semilla 20261109). Caso de control: centro 0 y sigma igual: P = 1 - exp(-b^2 / 2 sigma^2). Unidades: km, adimensional.
Supuestos: aproximacion de encuentro rapido (el plano B resume la geometria), gaussiana exacta, sin correlaciones. Validez: ilustrativa.
Tolerancia: cuadratura frente a caso exacto 1e-5 relativo; cuadratura frente a Monte Carlo dentro de 3 errores binomiales; aproximacion frente a cuadratura 1 % para un disco pequeno (b = 500 km).
"""
import math, platform, random

R_E, V_ESC, V_INF = 6378.137, 11.186, 12.0

def b_efectivo(r=R_E, vesc=V_ESC, vinf=V_INF):
    return r * math.sqrt(1.0 + (vesc / vinf) ** 2)

def pdf(x, y, c, s):
    return math.exp(-0.5 * (((x - c[0]) / s[0]) ** 2 + ((y - c[1]) / s[1]) ** 2)) / (2 * math.pi * s[0] * s[1])

def cuadratura(b, c, s, nr=400, nt=720):
    tot = 0.0
    dr, dt = b / nr, 2 * math.pi / nt
    for i in range(nr):
        r = (i + 0.5) * dr
        for j in range(nt):
            t = (j + 0.5) * dt
            tot += pdf(r * math.cos(t), r * math.sin(t), c, s) * r
    return tot * dr * dt

def aproximacion(b, c, s):
    return math.pi * b * b * pdf(0.0, 0.0, c, s)

def montecarlo(b, c, s, N, rng):
    k = 0
    for _ in range(N):
        x, y = rng.gauss(c[0], s[0]), rng.gauss(c[1], s[1])
        if x * x + y * y <= b * b:
            k += 1
    return k / N

def calcular():
    b = b_efectivo()
    # control: centro 0 y sigma igual
    ctrl_exacto = 1 - math.exp(-b * b / (2 * 4000.0 ** 2))
    ctrl_cuad = cuadratura(b, (0.0, 0.0), (4000.0, 4000.0))
    c, s = (15000.0, 4000.0), (12000.0, 3000.0)
    Pq = cuadratura(b, c, s)
    Pa = aproximacion(b, c, s)
    N = 1500000
    rng = random.Random(20261109)
    Pm = montecarlo(b, c, s, N, rng)
    err = math.sqrt(Pq * (1 - Pq) / N)
    # disco pequeno
    bp = 500.0
    Pq2 = cuadratura(bp, c, s); Pa2 = aproximacion(bp, c, s)
    # P frente al desplazamiento del centro
    curva = [(d1, cuadratura(b, (d1, 0.0), s)) for d1 in (0.0, 6000.0, 12000.0, 24000.0, 36000.0)]
    return {"b": b, "ctrl_exacto": ctrl_exacto, "ctrl_cuad": ctrl_cuad, "Pq": Pq, "Pa": Pa, "Pm": Pm, "err": err, "N": N,
            "Pq2": Pq2, "Pa2": Pa2, "curva": curva, "foco": (b / R_E) ** 2}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Radio efectivo del blanco b = %.1f km (R = %.3f km ; factor de enfoque b^2/R^2 = %.4f)" % (r["b"], R_E, r["foco"]))
    print("Control (centro 0, sigma 4000 km): exacto = %.8f ; cuadratura = %.8f" % (r["ctrl_exacto"], r["ctrl_cuad"]))
    print("Escenario: cuadratura = %.6e ; aproximacion pi b^2 f(centro) = %.6e ; Monte Carlo (%d) = %.6e +- %.1e" % (r["Pq"], r["Pa"], r["N"], r["Pm"], r["err"]))
    print("Diferencia Monte Carlo - cuadratura = %+.2f errores binomiales ; aproximacion / cuadratura = %.4f" % ((r["Pm"] - r["Pq"]) / r["err"], r["Pa"] / r["Pq"]))
    print("Disco pequeno b = 500 km: cuadratura = %.6e ; aproximacion = %.6e ; cociente = %.5f" % (r["Pq2"], r["Pa2"], r["Pa2"] / r["Pq2"]))
    print("P frente al desplazamiento del centro en el eje 1 (sigma1 = 12000 km):")
    for d, p in r["curva"]:
        print("  d1 = %6.0f km  ->  P = %.4e" % (d, p))
    assert abs(r["ctrl_cuad"] / r["ctrl_exacto"] - 1) < 1e-5
    assert abs(r["Pm"] - r["Pq"]) < 3 * r["err"]
    assert abs(r["Pa2"] / r["Pq2"] - 1) < 0.01
    ps = [p for _, p in r["curva"]]
    assert all(ps[i] > ps[i + 1] for i in range(len(ps) - 1))
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
