#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C22: estado de tension 3D: tensiones principales, von Mises, cortante maximo, ley de Hooke y energia de deformacion.

DATOS ILUSTRATIVOS (no consultados): tensor de Cauchy en un punto, en MPa, ejes x, y, z:
  [[120, 40, 0], [40, -30, 20], [0, 20, 60]]; material E = 69 GPa, nu = 0,33 (aluminio tipico).
Calculos: tensiones principales por Jacobi (autovalores del tensor); invariantes I1 = tr, I2 = (I1^2 - tr(s^2))/2, I3 = det;
von Mises: sigma_vm = sqrt(1/2[(s1-s2)^2 + (s2-s3)^2 + (s3-s1)^2]) y por componentes sqrt(3 J2) con J2 = 1/2 s_dev:s_dev; cortante maximo (s1 - s3)/2.
Hooke: eps = [(1+nu) s - nu tr(s) I]/E. Energia por volumen u = 1/2 s:eps (componentes) = 1/2 sum s_i eps_i (principales).
Unidades: MPa, GPa. Tolerancias: invariantes 1e-9 relativa; von Mises por dos vias 1e-9; energia por dos vias 1e-12.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import jacobi_eig

S = [[120.0, 40.0, 0.0], [40.0, -30.0, 20.0], [0.0, 20.0, 60.0]]
E, NU = 69e3, 0.33  # MPa


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Tensor ILUSTRATIVO [MPa]: [[120, 40, 0], [40, -30, 20], [0, 20, 60]]")
    vals, vec = jacobi_eig(S)
    s3, s2, s1 = vals
    print(f"Tensiones principales: s1 = {s1:.4f}, s2 = {s2:.4f}, s3 = {s3:.4f} MPa")
    tr = sum(S[i][i] for i in range(3))
    tr2 = sum(S[i][j] * S[j][i] for i in range(3) for j in range(3))
    I1, I2, I3 = tr, (tr ** 2 - tr2) / 2, det3(S)
    print(f"Invariantes: I1 = {I1:.4f}, I2 = {I2:.4f}, I3 = {I3:.4f}")
    e1 = abs(I1 - (s1 + s2 + s3)) / abs(I1)
    e2 = abs(I2 - (s1 * s2 + s2 * s3 + s3 * s1)) / abs(I2)
    e3 = abs(I3 - s1 * s2 * s3) / abs(I3)
    print(f"Diferencias relativas de los invariantes frente a los autovalores: {e1:.1e}, {e2:.1e}, {e3:.1e}")
    vm_p = math.sqrt(0.5 * ((s1 - s2) ** 2 + (s2 - s3) ** 2 + (s3 - s1) ** 2))
    dev = [[S[i][j] - (tr / 3 if i == j else 0.0) for j in range(3)] for i in range(3)]
    j2 = 0.5 * sum(dev[i][j] ** 2 for i in range(3) for j in range(3))
    vm_c = math.sqrt(3 * j2)
    print(f"Von Mises por principales = {vm_p:.6f} MPa ; por componentes sqrt(3 J2) = {vm_c:.6f} MPa ; dif = {abs(vm_p - vm_c):.1e}")
    print(f"Cortante maximo (s1 - s3)/2 = {(s1 - s3) / 2:.4f} MPa ; presion hidrostatica -tr/3 = {-tr / 3:.4f} MPa")
    eps = [[((1 + NU) * S[i][j] - (NU * tr if i == j else 0.0)) / E for j in range(3)] for i in range(3)]
    print("Deformaciones (x 1e-6): " + "; ".join(f"e{'xyz'[i]}{'xyz'[j]} = {eps[i][j] * 1e6:8.2f}" for i in range(3) for j in range(i, 3)))
    u_c = 0.5 * sum(S[i][j] * eps[i][j] for i in range(3) for j in range(3))
    e_pr = [((1 + NU) * s - NU * tr) / E for s in (s1, s2, s3)]
    u_p = 0.5 * sum(s * e for s, e in zip((s1, s2, s3), e_pr))
    print(f"Energia de deformacion por volumen: componentes = {u_c:.6e} MJ/m3 ; principales = {u_p:.6e} MJ/m3 ; dif = {abs(u_c - u_p):.1e}")
    k = E / (3 * (1 - 2 * NU))
    u_vol = tr ** 2 / (18 * k)
    u_dis = u_c - u_vol
    print(f"Parte volumetrica = {u_vol:.6e} ; distorsional = {u_dis:.6e} MJ/m3 ; distorsional con von Mises: (1+nu)/(3E) sigma_vm^2 = {(1 + NU) / (3 * E) * vm_c ** 2:.6e}")
    # Margen de fluencia con von Mises (limite elastico ilustrativo de 275 MPa, FS 1,25)
    print(f"Margen de fluencia con sigma_y = 275 MPa y FS = 1,25 (GEVS): {275 / (1.25 * vm_c) - 1:.3f}")
    assert max(e1, e2, e3) < 1e-9
    assert abs(vm_p - vm_c) < 1e-9
    assert abs(u_c - u_p) < 1e-12
    assert abs(u_dis - (1 + NU) / (3 * E) * vm_c ** 2) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
