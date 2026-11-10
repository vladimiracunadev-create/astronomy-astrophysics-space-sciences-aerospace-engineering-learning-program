#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C30: correlacion modelo-ensayo: MAC, ortogonalidad cruzada y actualizacion de parametros.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B, 2021-04-28, p. 2.4-7 del PDF): para la encuesta modal, ortogonalidad cruzada con objetivo de al menos 0,9 en la diagonal
y no mayor que 0,1 fuera de la diagonal, y frecuencias de modos de ensayo y de analisis coincidentes dentro de 5 %.
DATOS SINTETICOS (no medidos): el 'ensayo' se fabrica con una copia de la viga en voladizo de B84-C10 (10 elementos, EI = 287,5 N m2, rho A = 1,35 kg/m, L = 1 m) con la rigidez
global multiplicada por sE = 1,06 y la rigidez del elemento 3 reducida a s3 = 0,70, mas ruido: 1 % en frecuencias (gaussiano, semilla 84030) y 2 % en las formas modales medidas en 5 sensores
(desplazamientos de los nodos 2, 4, 6, 8, 10). El MODELO inicial tiene sE = 1 y s3 = 1.
Actualizacion: minimos cuadrados no lineales (Gauss-Newton con Jacobiano por diferencias finitas) de (sE, s3) para igualar las 3 primeras frecuencias; se reevalua el MAC y la
ortogonalidad cruzada con las formas completas del 'ensayo' (disponibles porque es sintetico).
MAC_ij = (phi_i^T psi_j)^2/((phi_i^T phi_i)(psi_j^T psi_j)) en los sensores. Tolerancias: tras actualizar, los errores de frecuencia deben bajar y quedar < 5 %.
"""
from __future__ import annotations
import math, platform, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import viga_ke, viga_me, zeros, gen_eig, reducir, solve, matvec

EI, RHOA, L, N = 287.5, 1.35, 1.0, 10
SENS = [1, 3, 5, 7, 9]  # indices de nodo (0 es el empotramiento) -> nodos 2,4,6,8,10 en numeracion 1..10


def modos(sE, s3):
    le = L / N
    n = 2 * (N + 1)
    K, M = zeros(n), zeros(n)
    me = viga_me(RHOA, le)
    for e in range(N):
        fe = sE * (s3 if e == 2 else 1.0)
        ke = viga_ke(EI * fe, le)
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4):
                K[g[i]][g[j]] += ke[i][j]
                M[g[i]][g[j]] += me[i][j]
    libres = list(range(2, n))
    lam, phi = gen_eig(reducir(K, libres), reducir(M, libres))
    return lam, phi, reducir(M, libres)


def freqs(lam):
    return [math.sqrt(l) / (2 * math.pi) for l in lam]


def sensores(phi, k):
    # GDL libres: indice j corresponde al GDL global j+2; el desplazamiento del nodo i (1..N) es el GDL 2 i -> libre 2 i - 2
    return [phi[2 * (i + 1) - 2][k] for i in SENS]


def mac(a, b):
    num = sum(x * y for x, y in zip(a, b)) ** 2
    return num / (sum(x * x for x in a) * sum(y * y for y in b))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lam_t, phi_t, Mr = modos(1.06, 0.70)
    ft = freqs(lam_t)
    rng = random.Random(84030)
    ft_m = [f * (1 + 0.01 * rng.gauss(0, 1)) for f in ft[:3]]
    psi = [[v * (1 + 0.02 * rng.gauss(0, 1)) for v in sensores(phi_t, k)] for k in range(3)]
    lam0, phi0, _ = modos(1.0, 1.0)
    f0 = freqs(lam0)
    print("'Ensayo' SINTETICO: sE = 1,06 y s3 = 0,70 (desconocidos para el modelo) con ruido de 1 % en frecuencias y 2 % en formas")
    print("Antes de actualizar (modelo sE = 1, s3 = 1):")
    print(" modo  f ensayo [Hz]  f modelo [Hz]  error [%]   MAC")
    for k in range(3):
        print(f"  {k + 1}    {ft_m[k]:11.3f}   {f0[k]:12.3f}   {(f0[k] - ft_m[k]) / ft_m[k] * 100:8.2f}   {mac(sensores(phi0, k), psi[k]):.4f}")
    # Gauss-Newton sobre (sE, s3)
    p = [1.0, 1.0]
    for it in range(12):
        f = freqs(modos(*p)[0])[:3]
        r = [(a - b) / b for a, b in zip(f, ft_m)]
        J = []
        for j in range(2):
            q = p[:]
            q[j] += 1e-6
            fq = freqs(modos(*q)[0])[:3]
            J.append([((a - b) / b - rr) / 1e-6 for a, b, rr in zip(fq, ft_m, r)])
        A = [[sum(J[i][k] * J[j][k] for k in range(3)) for j in range(2)] for i in range(2)]
        g = [-sum(J[i][k] * r[k] for k in range(3)) for i in range(2)]
        d = solve(A, g)
        p = [p[0] + d[0], p[1] + d[1]]
        if abs(d[0]) + abs(d[1]) < 1e-10:
            break
    lam1, phi1, _ = modos(*p)
    f1 = freqs(lam1)
    print(f"Parametros actualizados por Gauss-Newton: sE = {p[0]:.4f}, s3 = {p[1]:.4f} (verdaderos 1,06 y 0,70; 3 frecuencias para 2 parametros)")
    print("Despues de actualizar:")
    print(" modo  f ensayo [Hz]  f modelo [Hz]  error [%]   MAC")
    for k in range(3):
        print(f"  {k + 1}    {ft_m[k]:11.3f}   {f1[k]:12.3f}   {(f1[k] - ft_m[k]) / ft_m[k] * 100:8.2f}   {mac(sensores(phi1, k), psi[k]):.4f}")
    # Ortogonalidad cruzada con las formas completas
    print("Ortogonalidad cruzada phi_modelo^T M psi_ensayo (formas completas del ensayo sintetico, masa del modelo actualizado):")
    for nombre, ph in (("antes", phi0), ("despues", phi1)):
        X = [[sum(ph[i][a] * sum(Mr[i][k] * phi_t[k][b] for k in range(len(Mr))) for i in range(len(Mr))) for b in range(3)] for a in range(3)]
        diag = [abs(X[k][k]) for k in range(3)]
        fuera = max(abs(X[a][b]) for a in range(3) for b in range(3) if a != b)
        print(f"  {nombre:8s} diagonal = {diag[0]:.4f}, {diag[1]:.4f}, {diag[2]:.4f} ; maximo fuera de la diagonal = {fuera:.4f} ; criterio GEVS (>= 0,9 y <= 0,1): {'cumple' if min(diag) >= 0.9 and fuera <= 0.1 else 'NO cumple'}")
    e0 = max(abs(f0[k] - ft_m[k]) / ft_m[k] for k in range(3))
    e1 = max(abs(f1[k] - ft_m[k]) / ft_m[k] for k in range(3))
    print(f"Error maximo de frecuencia: antes = {e0 * 100:.2f} %, despues = {e1 * 100:.2f} % (criterio GEVS: dentro de 5 %)")
    assert e1 < e0 and e1 < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
