#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C01: valor agregado en una cadena de valor espacial SINTETICA con un modelo insumo-producto.

CONTENIDO EDUCATIVO: no es asesoria financiera. Todas las cifras son SINTETICAS (no medidas, no de ninguna empresa real).
Modelo: x = A x + f (producto bruto x, compras intermedias A, demanda final f); x = (I - A)^-1 f.
Valor agregado de la etapa j: VA_j = x_j (1 - sum_i A_ij - e_j), con e_j la fraccion comprada fuera de la cadena.
Unidades: unidades monetarias sinteticas (um) por periodo. Etapas: 0 materiales, 1 fabricacion de satelites,
2 lanzamiento, 3 operacion de infraestructura, 4 servicios y aplicaciones de datos.
Tolerancias: identidad sum(VA) = sum(f) - sum(e x) dentro de 1e-9; solucion directa frente a serie de Neumann < 1e-9.
"""
import platform

NOMBRES = ["materiales", "fabricacion de satelites", "lanzamiento", "operacion de infraestructura", "servicios de datos"]
A = [  # A[i][j]: compra de la etapa j al proveedor i, por unidad de producto de j
    [0.00, 0.20, 0.15, 0.02, 0.00],
    [0.00, 0.00, 0.00, 0.30, 0.05],
    [0.00, 0.00, 0.00, 0.15, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.35],
    [0.00, 0.00, 0.00, 0.00, 0.00],
]
E = [0.30, 0.25, 0.30, 0.20, 0.25]  # fraccion comprada fuera de la cadena
F = [5.0, 30.0, 40.0, 25.0, 100.0]  # demanda final (um)
N = 5


def resolver(M, b):
    n = len(b)
    a = [row[:] + [b[i]] for i, row in enumerate(M)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        for r in range(n):
            if r != c:
                k = a[r][c] / a[c][c]
                a[r] = [x - k * y for x, y in zip(a[r], a[c])]
    return [a[i][n] / a[i][i] for i in range(n)]


def leontief_directo(f):
    I_A = [[(1.0 if i == j else 0.0) - A[i][j] for j in range(N)] for i in range(N)]
    return resolver(I_A, f)


def leontief_neumann(f, terminos=400):
    x = f[:]
    t = f[:]
    for _ in range(terminos):
        t = [sum(A[i][j] * t[j] for j in range(N)) for i in range(N)]
        x = [a + b for a, b in zip(x, t)]
    return x


def run():
    x = leontief_directo(F)
    xn = leontief_neumann(F)
    err_neumann = max(abs(a - b) for a, b in zip(x, xn))
    va = [x[j] * (1 - sum(A[i][j] for i in range(N)) - E[j]) for j in range(N)]
    ext = sum(E[j] * x[j] for j in range(N))
    ident = abs(sum(va) - (sum(F) - ext))
    mult = []  # multiplicador de producto: produccion total por um de demanda final de la etapa j
    for j in range(N):
        e = [1.0 if k == j else 0.0 for k in range(N)]
        mult.append(sum(leontief_directo(e)))
    R = {"vasum": sum(va), "fsum": sum(F), "ext": ext, "ident": ident, "err_neumann": err_neumann,
         "xsum": sum(x), "share4": va[4] / sum(va), "share0": va[0] / sum(va)}
    for j in range(N):
        R[f"x{j}"] = x[j]
        R[f"va{j}"] = va[j]
        R[f"m{j}"] = mult[j]
        R[f"s{j}"] = va[j] / sum(va)
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Cadena de valor SINTETICA (ilustrativa); unidades monetarias sinteticas (um) por periodo.")
    print(f"Demanda final total = {R['fsum']:.1f} um ; compras fuera de la cadena = {R['ext']:.3f} um")
    print(" etapa                          x[um]    VA[um]   VA[%]  multiplicador")
    for j in range(N):
        print(f" {NOMBRES[j]:<29} {R[f'x{j}']:8.3f} {R[f'va{j}']:8.3f} {100 * R[f's{j}']:6.1f} {R[f'm{j}']:9.3f}")
    print(f"Suma de VA = {R['vasum']:.6f} um ; demanda final - compras externas = {R['fsum'] - R['ext']:.6f} um")
    print(f"Identidad (error) = {R['ident']:.2e} ; solucion directa frente a serie de Neumann (error) = {R['err_neumann']:.2e}")
    assert R["ident"] < 1e-9 and R["err_neumann"] < 1e-9
    assert abs(R["vasum"] + R["ext"] - R["fsum"]) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
