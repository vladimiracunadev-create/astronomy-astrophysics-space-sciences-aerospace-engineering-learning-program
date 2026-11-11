#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C01: dimensionamiento de un canal hidroponico de pelicula de nutrientes (NFT) SINTETICO.

Todo es sintetico o ilustrativo: la geometria del canal, el caudal, las plantas y su respiracion no describen ningun
hardware real. Unidades: m, L, min, h, mg/L, kPa. Sistema: canal rectangular inclinado, flujo en una direccion.
Metodo: (1) profundidad de la pelicula con Manning (n ilustrativo, canal ancho) resuelta por biseccion; (2) velocidad,
numero de Froude y tiempo de residencia; (3) oxigeno disuelto en la entrada (saturacion empirica, no consultada) y
caida por respiracion de raices; (4) balance de agua del deposito con valvula de reposicion: simulacion numerica frente
a la solucion analitica. Verificacion: el caudal reconstruido con la profundidad coincide con el dato (tolerancia 1e-6)
y el deposito simulado coincide con la solucion analitica (tolerancia 1 %). Solo numpy y la biblioteca estandar.
"""
from __future__ import annotations
import math
import platform
import numpy as np

ANCHO, LARGO, PENDIENTE, MANNING_N = 0.10, 2.0, 0.01, 0.030   # m, m, m/m, s/m^(1/3) (ilustrativo)
CAUDAL_LMIN = 1.0                                              # L/min por canal
G = 9.81                                                       # m/s2 (Tierra; en otro cuerpo cambia solo el Froude)


def caudal_manning(h, w=ANCHO, s=PENDIENTE, n=MANNING_N):
    area = w * h
    radio = area / (w + 2 * h)
    return area * radio ** (2 / 3) * math.sqrt(s) / n


def profundidad(q_m3s):
    lo, hi = 1e-6, 0.05
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if caudal_manning(mid) < q_m3s:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def do_saturacion(t_c):
    """Saturacion de O2 en agua dulce a nivel del mar (relacion empirica estandar, NO consultada), mg/L."""
    return 14.652 - 0.41022 * t_c + 0.007991 * t_c ** 2 - 0.000077774 * t_c ** 3


def deposito(v0, plantas, uso_l_dia_planta, dias, dt_h=0.5, repone=True):
    """Deposito con valvula de flotador: la transpiracion saca agua y la valvula la repone con un retardo."""
    v, serie = v0, []
    consumo = plantas * uso_l_dia_planta / 24.0   # L/h
    for k in range(int(dias * 24 / dt_h)):
        v -= consumo * dt_h
        if repone and v < v0 - 1.0:               # la valvula repone cuando el nivel baja 1 L
            v = v0
        serie.append(v)
    return np.array(serie)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: canal 0.10 m x 2.0 m, pendiente 1 %, n de Manning 0.030, 1.0 L/min")
    q = CAUDAL_LMIN / 1000 / 60
    h = profundidad(q)
    area = ANCHO * h
    v = q / area
    fr = v / math.sqrt(G * h)
    t_res = LARGO / v
    vol_pelicula = area * LARGO * 1000
    print(f"Profundidad de pelicula h = {h*1000:.3f} mm; velocidad = {v*100:.2f} cm/s; Froude = {fr:.3f}")
    print(f"Tiempo de residencia = {t_res:.1f} s; volumen retenido en el canal = {vol_pelicula*1000:.1f} mL")
    err_q = abs(caudal_manning(h) - q) / q
    print(f"Comprobacion: caudal reconstruido, error relativo = {err_q:.2e}")
    assert err_q < 1e-6 and fr < 1.0, "caudal o regimen fuera de tolerancia"

    print("Oxigeno disuelto en la entrada (saturacion empirica, nivel del mar, aire 20.9 % O2)")
    print("   T[C]   DOsat[mg/L]   caida con 12 plantas a 6 mg/h  DOsal[mg/L]")
    n_pl, resp = 12, 6.0                           # plantas por canal; mg O2/h por planta (sintetico)
    caida = n_pl * resp / (CAUDAL_LMIN * 60)       # mg/L = (mg/h) / (L/h)
    for t in (18, 22, 26, 30):
        s = do_saturacion(t)
        print(f"   {t:3d}   {s:10.2f}   {caida:26.2f}   {s - caida:12.2f}")
    s22 = do_saturacion(22)
    assert 8.5 < s22 < 9.1, "saturacion a 22 C fuera de lo esperado"
    print("Efecto de la atmosfera del habitat sobre la saturacion (ley de Henry, T = 22 C)")
    for nombre, p, x in (("aire a 101.3 kPa, 20.9 % O2", 101.325, 0.209), ("ilustrativo 70.3 kPa, 26.5 % O2", 70.3, 0.265)):
        f = p * x / (101.325 * 0.209)
        print(f"   {nombre:34s} factor = {f:.3f}  DOsat = {s22 * f:.2f} mg/L")

    print("Deposito de 40 L con 6 canales x 12 plantas, 0.12 L/dia/planta (sintetico), 7 dias")
    plantas = 6 * n_pl
    sin = deposito(40.0, plantas, 0.12, 7, repone=False)
    con = deposito(40.0, plantas, 0.12, 7, repone=True)
    analitico = 40.0 - plantas * 0.12 * 7
    err = abs(sin[-1] - analitico) / 40.0
    print(f"   Consumo = {plantas*0.12:.2f} L/dia; sin reposicion V(7 d) = {sin[-1]:.2f} L (analitico {analitico:.2f} L, error {err:.1e})")
    t_vacio = 40.0 / (plantas * 0.12)
    print(f"   Con valvula: V minimo = {con.min():.2f} L, V maximo = {con.max():.2f} L; sin reposicion se vacia en {t_vacio:.1f} dias")
    assert err < 0.01 and con.min() > 38.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
