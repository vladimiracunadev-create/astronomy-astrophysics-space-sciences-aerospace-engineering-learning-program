#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C15: rotaciones de ejes y de puntos, contra valores publicados.

Datos (PUBLICADOS): ESA, Hipparcos Catalogue SP-1200, vol. 1, ec. (1.5.7): para
ε = 23°26′21,448″ = 23,4392911°, cos ε = +0,9174820621 y sen ε = +0,3977771559 (matriz
A_K, equatorial → eclíptico); IERS Conventions 2010 (TN36): ε0 = 84381,406″ (IAU 2006).
Dirección de Próxima Cen (NASA Exoplanet Archive, 2026-11-05; marco y época no declarados por la documentación del archivo):
α = 217,3934657°, δ = −62,6761821°. Ángulos de otras pruebas: SINTÉTICOS.
Modelo: rotación de ejes (pasiva) alrededor del eje x por el ángulo ε: las componentes
eclípticas son v_ecl = R_x(ε) v_eq con R_x(ε) = [[1,0,0],[0,cos ε, sen ε],[0,-sen ε, cos ε]].
Supuestos: se usa solo la inclinación entre ecuador y eclíptica (sin precesión ni nutación).
Validez: direcciones respecto del equinoccio y la eclíptica de la época J2000. Tolerancia:
1e-9 frente a los dígitos publicados (10 cifras) y 1e-12 en propiedades algebraicas.
"""
from __future__ import annotations
import math, platform, sys

EPS_HIP = math.radians(23 + 26 / 60 + 21.448 / 3600)       # Hipparcos
EPS_IAU2006 = math.radians(84381.406 / 3600)               # IERS TN36


def Rx(a):
    c, s = math.cos(a), math.sin(a)
    return [[1, 0, 0], [0, c, s], [0, -s, c]]


def Rz(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, s, 0], [-s, c, 0], [0, 0, 1]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def mv(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))


def T(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def vec(ra, dec):
    a, d = math.radians(ra), math.radians(dec)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def esf(v):
    return math.degrees(math.atan2(v[1], v[0])) % 360, math.degrees(math.asin(v[2]))


def casi(A, B, tol):
    return all(abs(A[i][j] - B[i][j]) < tol for i in range(3) for j in range(3))


def pruebas():
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    R = Rx(0.7)
    assert casi(mm(R, T(R)), I, 1e-12) and abs(det(R) - 1) < 1e-12           # ortogonal, det +1
    assert casi(mm(Rx(0.3), Rx(0.4)), Rx(0.7), 1e-12)                          # composición mismo eje
    assert casi(Rx(-0.7), T(R), 1e-12)                                         # inversa = traspuesta
    assert casi(mm(Rz(0.3), Rx(0.4)), mm(Rx(0.4), Rz(0.3)), 1e-3) is False    # no conmutan
    v = (0.3, -0.5, 0.8)
    assert abs(sum(a * a for a in mv(R, v)) - sum(a * a for a in v)) < 1e-12   # conserva el módulo
    # Valores publicados (Hipparcos, ec. 1.5.7)
    A = Rx(EPS_HIP)
    assert abs(A[1][1] - 0.9174820621) < 1e-9 and abs(A[1][2] - 0.3977771559) < 1e-9
    # Polo norte celeste en coordenadas eclípticas: latitud 90° − ε, longitud 90°
    lon, lat = esf(mv(Rx(EPS_HIP), (0.0, 0.0, 1.0)))
    assert abs(lon - 90.0) < 1e-9 and abs(lat - (90 - math.degrees(EPS_HIP))) < 1e-9


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (ortogonalidad, det=1, composición, inversa, no conmutatividad, módulo, valores Hipparcos, polo)")
    print(f"\nε (Hipparcos) = {math.degrees(EPS_HIP):.7f}°;  ε0 (IAU 2006) = {math.degrees(EPS_IAU2006):.8f}°;  "
          f"diferencia = {(math.degrees(EPS_HIP) - math.degrees(EPS_IAU2006)) * 3600 * 1000:.2f} mas")
    A1, A2 = Rx(EPS_HIP), Rx(EPS_IAU2006)
    print(f"cos ε (Hipparcos) = {A1[1][1]:.10f};  cos ε (IAU 2006) = {A2[1][1]:.10f}")
    print(f"sen ε (Hipparcos) = {A1[1][2]:.10f};  sen ε (IAU 2006) = {A2[1][2]:.10f}")
    # Solsticio de junio: Sol en la eclíptica con λ=90°, β=0°. Matriz inversa (eclíptico → ecuatorial) = traspuesta
    sol_ecl = (0.0, 1.0, 0.0)
    sol_eq = mv(T(Rx(EPS_HIP)), sol_ecl)
    ra, dec = esf(sol_eq)
    print(f"\nSol en λ=90°, β=0° → ecuatoriales α = {ra:.4f}°, δ = {dec:.4f}° (δ debe ser +ε)")
    # Próxima Cen: ecuatorial → eclíptico
    v = vec(217.3934657, -62.6761821)
    lon, lat = esf(mv(Rx(EPS_HIP), v))
    print(f"Próxima Cen (α={217.3934657}°, δ={-62.6761821}°) → eclípticas λ = {lon:.4f}°, β = {lat:.4f}°")
    lon2, lat2 = esf(mv(Rx(EPS_IAU2006), v))
    print(f"   con ε IAU 2006: λ = {lon2:.6f}°, β = {lat2:.6f}°; diferencia en β = {(lat - lat2) * 3600 * 1000:.2f} mas")
    # Pasiva frente a activa: rotar el vector +ε equivale a rotar los ejes −ε
    vact = mv(T(Rx(0.5)), (1.0, 1.0, 0.0))
    vpas = mv(Rx(-0.5), (1.0, 1.0, 0.0))
    print(f"\nActiva (vector +0,5 rad) = ({vact[0]:.5f}, {vact[1]:.5f}, {vact[2]:.5f}); pasiva (ejes −0,5 rad) = "
          f"({vpas[0]:.5f}, {vpas[1]:.5f}, {vpas[2]:.5f})")
    # Composición: Rz(30°) tras Rx(ε)
    M = mm(Rz(math.radians(30)), Rx(EPS_HIP))
    print(f"det(Rz·Rx) = {det(M):.12f}; Rz·Rx ≠ Rx·Rz: máx diferencia = {max(abs(M[i][j] - mm(Rx(EPS_HIP), Rz(math.radians(30)))[i][j]) for i in range(3) for j in range(3)):.4f}")


if __name__ == "__main__":
    main()
