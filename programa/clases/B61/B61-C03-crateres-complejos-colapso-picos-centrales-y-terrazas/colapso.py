#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C03: transicion simple-compleja por gravedad y relajacion de pendientes.

Datos: transicion aproximada Luna ~16 km y Marte ~8 km tomada de una entrada de divulgacion (CosmoQuest, 2017),
  consultada el 2026-11-09 como orden de magnitud, NO como valor revisado. g Luna 1.62 y g Marte 3.71 m/s2 (redondeados,
  no consultados). Densidad 2800 kg/m3 y perfiles de bol son ILUSTRATIVOS/SINTETICOS.
Modelo A (calibrar y contrastar): el bol transitorio colapsa si la presion litostatica rho g d_t supera una resistencia
  efectiva Y: D_sc = k Y/(rho g) -> D_sc proporcional a 1/g. Se calibra k*Y con la Luna y se PREDICE Marte; el
  desacuerdo con ~8 km se informa, no se oculta. Tambien se ajusta el exponente libre entre ambos cuerpos.
Modelo B (numerico): relajacion de un perfil 1D de bol (d/D=0.25 sintetico) con regla de pendiente critica: donde la
  pendiente |dh/dx| supera tan(phi), el material se transfiere hacia abajo conservando volumen. Se verifica conservacion
  de masa (1e-9 relativo) y que la pendiente maxima final no excede tan(phi)+1e-3.
Tolerancias: ajuste del exponente a 1e-12 por construccion; masa 1e-9; pendiente 1e-3.
Limites: no se modelan picos centrales ni terrazas; la regla de pendiente no es reologia de fluidizacion acustica.
"""
from __future__ import annotations
import math, platform

G_MOON, G_MARS = 1.62, 3.71
D_MOON, D_MARS = 16.0, 8.0  # km, divulgacion


def relajar(h, dx, tan_phi, iters=200000):
    h = h[:]
    n = len(h)
    for _ in range(iters):
        movido = False
        for i in range(n - 1):
            s = (h[i + 1] - h[i]) / dx
            if abs(s) > tan_phi + 1e-4:
                # transferir 25 % del exceso entre la celda alta y la baja
                exceso = (abs(s) - tan_phi) * dx
                t = 0.25 * exceso
                if s > 0:
                    h[i + 1] -= t
                    h[i] += t
                else:
                    h[i] -= t
                    h[i + 1] += t
                movido = True
        if not movido:
            break
    return h


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ky = D_MOON * G_MOON  # D_sc * g = const (k Y / rho)
    pred = ky / G_MARS
    print(f"Modelo A: D_sc * g = {ky:.3f} km m/s2 (calibrado con la Luna: 16 km)")
    print(f"Prediccion para Marte = {pred:.2f} km ; divulgacion ~ {D_MARS:.0f} km ; razon pred/ref = {pred/D_MARS:.3f}")
    alpha = math.log(D_MOON / D_MARS) / math.log(G_MARS / G_MOON)
    print(f"Exponente libre entre ambos cuerpos: D_sc ~ g^(-{alpha:.3f}) (el modelo ingenuo usa -1)")
    # sanidad: con alpha, reproduce Marte exactamente
    assert abs(D_MOON * (G_MARS / G_MOON) ** (-alpha) - D_MARS) < 1e-12
    for nombre, g in (("Luna", G_MOON), ("Marte", G_MARS), ("g=9.81 (cuerpo de prueba)", 9.81)):
        print(f"  D_sc(modelo A, {nombre}) = {ky/g:.2f} km")
    # Modelo B
    n = 400
    D = 20.0  # km, sintetico
    dx = D / n
    d = 0.25 * D
    # perfil: parabola de profundidad d en [-D/2, D/2] mas planicie
    h = []
    for i in range(n):
        x = (i + 0.5) * dx - D / 2
        h.append(-d * (1 - (2 * x / D) ** 2))
    m0 = sum(h) * dx
    tan_phi = math.tan(math.radians(20.0))
    smax0 = max(abs(h[i + 1] - h[i]) / dx for i in range(n - 1))
    h2 = relajar(h, dx, tan_phi)
    m1 = sum(h2) * dx
    smax1 = max(abs(h2[i + 1] - h2[i]) / dx for i in range(n - 1))
    print(f"Perfil sintetico D={D:.0f} km, d={d:.1f} km (d/D=0.25), angulo critico 20 grados (tan={tan_phi:.4f})")
    print(f"Pendiente maxima inicial = {smax0:.4f} ; final = {smax1:.4f}")
    print(f"Profundidad inicial = {-min(h):.3f} km ; final = {-min(h2):.3f} km")
    print(f"Conservacion de area (volumen 2D): inicial {m0:.9f} ; final {m1:.9f} ; dif. relativa {abs(m1/m0-1):.2e}")
    assert abs(m1 / m0 - 1) < 1e-9
    assert smax1 <= tan_phi + 1e-3
    ancho0 = dx * sum(1 for v in h if v < -0.9 * d)
    ancho1 = dx * sum(1 for v in h2 if v < -0.9 * d)
    print(f"Ancho del suelo a >90 % de la profundidad: inicial {ancho0:.2f} km ; final {ancho1:.2f} km")
    print("Hallazgo: la regla de pendiente NO levanta el suelo (profundidad intacta); el pico central requiere rebote/colapso con fluidizacion, fuera de este modelo.")
    assert abs(min(h2) - min(h)) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
