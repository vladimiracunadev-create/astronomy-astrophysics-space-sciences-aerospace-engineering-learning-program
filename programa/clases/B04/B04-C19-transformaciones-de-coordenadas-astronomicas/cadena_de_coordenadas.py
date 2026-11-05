#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C19: cadena ecuatorial → eclíptico y ecuatorial → galáctico.

Datos (PUBLICADOS): ESA, Hipparcos Catalogue SP-1200, vol. 1, § 1.5.3: polo norte galáctico
(ICRS) α_G = 192,85948°, δ_G = +27,12825° (ec. 1.5.9); longitud galáctica del nodo
ascendente del plano galáctico sobre el ecuador l_Ω = 32,93192° (ec. 1.5.10); matriz
A_G a 10 decimales (ec. 1.5.11); ε = 23°26′21,448″ (ec. 1.5.7). Dirección de Próxima Cen:
NASA Exoplanet Archive (2026-11-05; ra, dec; marco y época no declarados por la documentación del archivo; su uso como ICRS es una hipótesis didáctica).
Modelo: [x_G y_G z_G] = [x y z] A_G (S1): las componentes galácticas son A_Gᵀ · v_ecuatorial;
las eclípticas, R_x(ε) · v_ecuatorial. Supuestos: matrices constantes (sin precesión, sin
movimiento propio). Validez: direcciones respecto del ICRS. Tolerancia de las pruebas:
2e-9 entre la matriz publicada (10 decimales) y la construida desde los ángulos (1.5.9, 1.5.10),
y 1e-12 en propiedades algebraicas.
"""
from __future__ import annotations
import math, platform, sys

# Matriz A_G publicada (ec. 1.5.11): columnas = ejes galácticos x_G, y_G, z_G escritos en el sistema ecuatorial
A_G = [[-0.0548755604, +0.4941094279, -0.8676661490],
       [-0.8734370902, -0.4448296300, -0.1980763734],
       [-0.4838350155, +0.7469822445, +0.4559837762]]
ALFA_G, DELTA_G, L_NODO = 192.85948, 27.12825, 32.93192
EPS = math.radians(23 + 26 / 60 + 21.448 / 3600)


def T(M):
    return [[M[j][i] for j in range(3)] for i in range(3)]


def mv(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(3)) for i in range(3))


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def vec(lon, lat):
    a, d = math.radians(lon), math.radians(lat)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def ang(v):
    """(longitud, latitud) en grados. La latitud usa atan2(z, hypot(x, y)): arcsen(z) pierde
    cifras cerca de los polos (z ≈ 1), igual que arccos cerca de 1 en C13."""
    return math.degrees(math.atan2(v[1], v[0])) % 360, math.degrees(math.atan2(v[2], math.hypot(v[0], v[1])))


def cruz(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def matriz_desde_angulos():
    """Construye A_G a partir de (α_G, δ_G, l_Ω): z_G = polo, x_G a l = 0°."""
    zg = vec(ALFA_G, DELTA_G)
    n = cruz((0.0, 0.0, 1.0), zg)                       # dirección de la línea de nodos (± )
    m = math.sqrt(sum(c * c for c in n))
    nodo = tuple(c / m for c in n)
    for s in (+1, -1):                                  # el signo se fija con l_Ω y se comprueba abajo
        nd = tuple(s * c for c in nodo)
        w = cruz(zg, nd)
        lo = math.radians(L_NODO)
        xg = tuple(nd[i] * math.cos(lo) - w[i] * math.sin(lo) for i in range(3))
        yg = cruz(zg, xg)
        M = [[xg[i], yg[i], zg[i]] for i in range(3)]
        if all(abs(M[i][j] - A_G[i][j]) < 2e-9 for i in range(3) for j in range(3)):
            return M, s
    raise AssertionError("ninguna elección de signo reproduce la matriz publicada")


def a_galacticas(ra, dec):
    return ang(mv(T(A_G), vec(ra, dec)))


def a_ecuatoriales_desde_galacticas(l, b):
    return ang(mv(A_G, vec(l, b)))


def a_eclipticas(ra, dec):
    c, s = math.cos(EPS), math.sin(EPS)
    Rx = [[1, 0, 0], [0, c, s], [0, -s, c]]
    return ang(mv(Rx, vec(ra, dec)))


def pruebas():
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    P = mm(T(A_G), A_G)
    assert all(abs(P[i][j] - I[i][j]) < 5e-10 for i in range(3) for j in range(3))       # ortogonal (a 10 decimales)
    M, signo = matriz_desde_angulos()                                                  # (1.5.9–1.5.10) ⇒ (1.5.11)
    # El polo galáctico norte cae en b = +90°
    l, b = a_galacticas(ALFA_G, DELTA_G)
    assert abs(b - 90.0) < 1e-8
    # Ida y vuelta
    for ra, dec in ((10.0, 20.0), (217.3934657, -62.6761821), (359.0, -89.0), (180.0, 0.0)):
        l, b = a_galacticas(ra, dec)
        ra2, dec2 = a_ecuatoriales_desde_galacticas(l, b)
        # A_G publicada tiene 10 decimales: ida y vuelta a ~1e-6° (más cerca de los polos)
        assert abs(((ra2 - ra + 180) % 360) - 180) < 1e-6 and abs(dec2 - dec) < 1e-6
        # con la matriz construida desde los ángulos (exactamente ortogonal) la ida y vuelta es exacta
        v_g = mv(T(M), vec(ra, dec))
        v_back = ang(mv(M, v_g))
        assert abs(((v_back[0] - ra + 180) % 360) - 180) < 1e-10 and abs(v_back[1] - dec) < 1e-10
    # El nodo (b = 0, l = l_Ω) está en el ecuador (δ = 0)
    ra_n, dec_n = a_ecuatoriales_desde_galacticas(L_NODO, 0.0)
    assert abs(dec_n) < 1e-8
    # Cadena = composición: ecuatorial → eclíptico → ecuatorial → galáctico
    c, s = math.cos(EPS), math.sin(EPS)
    Rx = [[1, 0, 0], [0, c, s], [0, -s, c]]
    v = vec(100.0, -30.0)
    v_ecl = mv(Rx, v)
    v_gal_directo = mv(T(A_G), v)
    v_gal_cadena = mv(T(A_G), mv(T(Rx), v_ecl))
    assert all(abs(a - b) < 1e-12 for a, b in zip(v_gal_directo, v_gal_cadena))
    return signo


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    signo = pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (A_G ortogonal, A_G reconstruida desde 1.5.9–1.5.10, polo, ida y vuelta, nodo, cadena)")
    M, _ = matriz_desde_angulos()
    d = max(abs(M[i][j] - A_G[i][j]) for i in range(3) for j in range(3))
    print(f"\nA_G publicada frente a A_G construida desde (α_G, δ_G, l_Ω): diferencia máxima = {d:.2e} (signo de nodo elegido: {signo:+d})")
    ra_c, dec_c = a_ecuatoriales_desde_galacticas(0.0, 0.0)
    print(f"Dirección (l, b) = (0°, 0°) → ecuatoriales α = {ra_c:.4f}°, δ = {dec_c:.4f}° (calculado desde A_G)")
    ra, dec = 217.3934657, -62.6761821
    lam, bet = a_eclipticas(ra, dec)
    l, b = a_galacticas(ra, dec)
    print(f"\nPróxima Cen (α={ra}°, δ={dec}°):")
    print(f"  eclípticas   λ = {lam:.4f}°, β = {bet:.4f}°   (R_x(ε), ε = {math.degrees(EPS):.7f}°)")
    print(f"  galácticas   l = {l:.4f}°, b = {b:.4f}°   (A_Gᵀ)")
    print("\nOtras direcciones de prueba (sintéticas):")
    for ra_, dec_ in ((0.0, 0.0), (90.0, 0.0), (192.85948, 27.12825), (266.4, -28.94)):
        l_, b_ = a_galacticas(ra_, dec_)
        lam_, bet_ = a_eclipticas(ra_, dec_)
        print(f"  (α,δ)=({ra_:8.4f},{dec_:8.4f}) → eclíptica ({lam_:8.4f},{bet_:8.4f}); galáctica ({l_:8.4f},{b_:8.4f})")


if __name__ == "__main__":
    main()
