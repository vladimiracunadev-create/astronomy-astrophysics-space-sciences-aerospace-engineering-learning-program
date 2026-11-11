#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C01: radio de la Tierra con dos sombras de gnomon, incertidumbre y propagacion.

CONTENIDO EDUCATIVO. Sin observacion propia: los datos de sombra proceden de una presentacion publicada (consultada 2026-11-11).
CONSULTADOS (presentacion CESAR/ESA 'Eratosthenes experiment', Caude, 21 mar 2018, PDF leido con PyMuPDF):
  - Caude (Madrid): latitud teorica 40.45 deg N; gnomon H = 100 cm; sombras medidas 86.0 cm y 83.9 cm.
  - Granada: latitud teorica 37.17 deg N; gnomon H = 101 cm; sombra medida 76.5 cm.
  - Distancia Caude-Granada 365 km (como figura en la presentacion). El calculo teorico de la presentacion da R = 6376 km.
  - Radio ecuatorial nominal de la Tierra: 6.3781e6 m (IAU 2015, Resolucion B3; PDF leido con PyMuPDF).
Supuestos: equinoccio (declinacion ~0), de modo que el angulo cenital al mediodia solar es igual a la latitud; mismo meridiano; Tierra esferica.
ILUSTRATIVOS (no medidos): incertidumbre de una lectura de sombra sigma_S = 1.0 cm y de la distancia sigma_d = 5 km; el ensayo
Monte Carlo de 20 grupos SINTETICOS (semilla 131) simula lecturas ruidosas alrededor de la sombra teorica.
Unidades: longitudes en cm y km; angulos en grados; radio en km.
Tolerancias: propagacion lineal frente a Monte Carlo (200 000 muestras) dentro del 10 % relativo (la propagacion lineal subestima cuando el error relativo de delta theta es grande); ida y vuelta atan/tan < 1e-12.
"""
from __future__ import annotations
import math, platform, random, statistics

LAT_CAU, LAT_GRA, DIST = 40.45, 37.17, 365.0
H_CAU, H_GRA = 100.0, 101.0
S_CAU = [86.0, 83.9]
S_GRA = [76.5]
R_NOMINAL_KM = 6378.1
SIG_S, SIG_D = 1.0, 5.0


def angulo(s, h):
    return math.degrees(math.atan(s / h))


def radio(theta_cau, theta_gra, dist):
    return dist / math.radians(theta_cau - theta_gra)


def sig_theta(s, h, sig_s):
    # d(atan(s/h))/ds = h/(h^2 + s^2)
    return math.degrees(sig_s * h / (h * h + s * s))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos de sombra CONSULTADOS (CESAR/ESA 2018); incertidumbres ILUSTRATIVAS; el aula SINTETICA es simulada, no observada.")
    # 1) teoria
    sc, sg = H_CAU * math.tan(math.radians(LAT_CAU)), H_GRA * math.tan(math.radians(LAT_GRA))
    print(f"Sombra teorica: Caude {sc:.2f} cm (presentacion 85.25) ; Granada {sg:.2f} cm (presentacion 76.57)")
    r_teo = radio(LAT_CAU, LAT_GRA, DIST)
    print(f"Radio con las latitudes teoricas: {r_teo:.0f} km (presentacion 6376)")
    # 2) datos medidos
    th_c = [angulo(s, H_CAU) for s in S_CAU]
    th_g = [angulo(s, H_GRA) for s in S_GRA]
    tc, tg = statistics.mean(th_c), statistics.mean(th_g)
    print("Angulos de las lecturas: Caude " + ", ".join(f"{t:.4f}" for t in th_c) + f" ; Granada {th_g[0]:.4f} (grados)")
    r_med = radio(tc, tg, DIST)
    print(f"Delta theta = {tc - tg:.4f} deg ; R medido = {r_med:.0f} km ; error frente a nominal = {100 * (r_med - R_NOMINAL_KM) / R_NOMINAL_KM:+.1f} %")
    # 3) propagacion lineal
    st_c = sig_theta(statistics.mean(S_CAU), H_CAU, SIG_S) / math.sqrt(len(S_CAU))
    st_g = sig_theta(S_GRA[0], H_GRA, SIG_S) / math.sqrt(len(S_GRA))
    sd_theta = math.hypot(st_c, st_g)
    rel = math.hypot(sd_theta / (tc - tg), SIG_D / DIST)
    sig_r = r_med * rel
    print(f"sigma(theta_Caude) = {st_c:.3f} deg ; sigma(theta_Granada) = {st_g:.3f} deg ; sigma(R) lineal = {sig_r:.0f} km ({100 * rel:.1f} %)")
    # 4) Monte Carlo de la misma incertidumbre
    rng = random.Random(131)
    muestras = []
    s_c_media, s_g = statistics.mean(S_CAU), S_GRA[0]
    for _ in range(200_000):
        a = angulo(rng.gauss(s_c_media, SIG_S / math.sqrt(len(S_CAU))), H_CAU)
        b = angulo(rng.gauss(s_g, SIG_S), H_GRA)
        d = rng.gauss(DIST, SIG_D)
        muestras.append(radio(a, b, d))
    mc = statistics.pstdev(muestras)
    print(f"Monte Carlo (200000): sigma(R) = {mc:.0f} km ; lineal/MC = {sig_r / mc:.3f}")
    # 5) aula sintetica de 20 grupos: lecturas ruidosas alrededor de la sombra teorica
    est = []
    for _ in range(20):
        a = angulo(rng.gauss(sc, SIG_S), H_CAU)
        b = angulo(rng.gauss(sg, SIG_S), H_GRA)
        est.append(radio(a, b, DIST))
    m, sd = statistics.mean(est), statistics.stdev(est)
    print(f"Aula SINTETICA (20 grupos, 1 lectura por sitio): media {m:.0f} km ; desv. {sd:.0f} km ; error estandar {sd / math.sqrt(20):.0f} km")
    print(f"  mediana {statistics.median(est):.0f} km ; minimo {min(est):.0f} ; maximo {max(est):.0f}")
    # 6) sensibilidad
    print("Sensibilidad: error de R al errar 0.1 deg en Delta theta -> " + f"{100 * 0.1 / (tc - tg):.1f} %")
    # pruebas
    assert abs(math.degrees(math.atan(math.tan(math.radians(33.3)))) - 33.3) < 1e-12
    assert abs(r_teo - 6376) < 5
    assert abs(sig_r / mc - 1) < 0.10
    assert abs(sc - 85.25) < 0.05 and abs(sg - 76.57) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
