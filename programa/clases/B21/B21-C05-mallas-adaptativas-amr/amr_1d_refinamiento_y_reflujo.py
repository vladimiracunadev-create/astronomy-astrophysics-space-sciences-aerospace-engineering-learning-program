#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B21-C05: mallas adaptativas en 1D (criterio de gradiente y corrección de flujo).

Datos: SINTETICOS y adimensionales. (a) frente suave u(x) = tanh((x - 0.5)/w), w = 0.01
(un frente delgado, como una capa de choque ablandada); (c) pulso gaussiano
u0(x) = exp(-((x - 0.2)/0.05)^2) transportado con velocidad a = 1 en [0, 1) periodico.
Modelo: (a) representación de una función por valores en el centro de cada celda;
(b) restricción y prolongación conservativas; (c) advección u_t + a u_x = 0.
Método: (a) refinamiento por bisección de las celdas cuyo gradiente por el ancho
de celda supera una fracción C = 0.05 de la amplitud (criterio del tipo de la ecuación 21 de
Teyssier 2002) y de sus vecinas (suavizado de malla); (c) volúmenes finitos
contracorriente en una malla gruesa de 64 celdas con un parche fino (razón 2) sobre
x in [0.25, 0.5), con subciclos temporales (2 pasos finos por paso grueso), y
corrección de flujo en las dos caras de contacto (Berger-Colella).
Supuestos: razón de refinamiento 2; un solo parche estático; interpolación
temporal lineal del dato de frontera del parche.
Validez: número de Courant 0.8 en ambas mallas; régimen lineal y 1D.
Tolerancias (las pruebas detienen la ejecución si fallan): el AMR con lmax = 8 usa < 5 % de las
celdas de la malla uniforme que logra su mismo error, y ese error es <= 1.05 C/2;
restricción(prolongación(u)) = u a 1e-15; con corrección de flujo la masa
se conserva a 1e-13 y sin ella el error es > 1e-6.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()}  NumPy {np.__version__}")

# ---------------------------------------------------------------- (a)
W = 0.01
perfil = lambda x: np.tanh((x - 0.5) / W)


def construir_amr(N0, lmax, C=0.05):
    celdas = [(0, i) for i in range(N0)]  # (nivel, índice dentro del nivel)
    for _ in range(lmax):
        marcas = []
        for (l, i) in celdas:
            dx = 1.0 / (N0 * 2**l)
            xc = (i + 0.5) * dx
            grad_dx = abs(perfil(xc + dx) - perfil(xc - dx)) / 2.0  # |du/dx| * dx, diferencia centrada
            marcas.append(grad_dx >= C * 1.0)
        # suavizado de malla: también las vecinas inmediatas
        marcas = [m or (k > 0 and marcas[k - 1]) or (k < len(marcas) - 1 and marcas[k + 1])
                  for k, m in enumerate(marcas)]
        nuevas = []
        for (l, i), m in zip(celdas, marcas):
            if m and l < lmax:
                nuevas += [(l + 1, 2 * i), (l + 1, 2 * i + 1)]
            else:
                nuevas.append((l, i))
        celdas = nuevas
    return celdas


def error_max(celdas, N0):
    e = 0.0
    for (l, i) in celdas:
        dx = 1.0 / (N0 * 2**l)
        valor = float(perfil((i + 0.5) * dx))
        xs = np.linspace(i * dx, (i + 1) * dx, 9)
        e = max(e, float(np.max(np.abs(perfil(xs) - valor))))
    return e


print("(a) frente tanh((x-0.5)/0.01); malla gruesa N0 = 32, hasta lmax niveles, C = 0.05")
N0 = 32
for lmax in (3, 5, 7, 8):
    cel = construir_amr(N0, lmax)
    ea = error_max(cel, N0)
    # malla uniforme más barata que alcanza el mismo error
    lu = 0
    while error_max([(lu, i) for i in range(N0 * 2**lu)], N0) > ea * 1.001:
        lu += 1
    n_uni = N0 * 2**lu
    print(f"    lmax={lmax}  celdas AMR = {len(cel):4d}  error AMR = {ea:.4f}  |  "
          f"uniforme con ese error: {n_uni:5d} celdas (nivel {lu})  AMR/uniforme = {100*len(cel)/n_uni:5.2f} %")
    if lmax == 8:
        assert len(cel) < 0.05 * n_uni and ea <= 0.05 / 2 * 1.05, "ahorro AMR"

# ---------------------------------------------------------------- (b)
print("(b) restricción y prolongación conservativas")
rng = np.random.default_rng(1)
uc = rng.standard_normal(32)
pend = (np.roll(uc, -1) - np.roll(uc, 1)) / 2.0  # pendiente centrada por celda (en unidades de dx_c)
uf = np.empty(64)
uf[0::2] = uc - pend / 4.0
uf[1::2] = uc + pend / 4.0
uc_ida = 0.5 * (uf[0::2] + uf[1::2])  # promedio ponderado por volumen (volúmenes iguales)
dif = float(np.max(np.abs(uc_ida - uc)))
print(f"    max |restricción(prolongación(u)) - u| = {dif:.2e}   |sum fino*dxf - sum grueso*dxc| = "
      f"{abs(uf.sum()/64 - uc.sum()/32):.2e}")
assert dif < 1e-15 and abs(uf.sum() / 64 - uc.sum() / 32) < 1e-15

# ---------------------------------------------------------------- (c)
NC, I0, I1 = 64, 16, 32
A, NU_C = 1.0, 0.8


def simular(corregir, tfin, uniforme_fino=False):
    dxc = 1.0 / NC
    dxf = dxc / 2
    dtc = NU_C * dxc
    xc = (np.arange(NC) + 0.5) * dxc
    uc = np.exp(-(((xc - 0.2) / 0.05) ** 2))
    xf = (np.arange(2 * (I1 - I0)) + 0.5) * dxf + I0 * dxc
    uf = np.exp(-(((xf - 0.2) / 0.05) ** 2))
    masa0 = None
    errores_masa = []
    nsteps = int(round(tfin / dtc))
    for n in range(nsteps + 1):
        cubierta = np.zeros(NC, bool)
        cubierta[I0:I1] = True
        masa = float(np.sum(uc[~cubierta]) * dxc + np.sum(uf) * dxf)
        if masa0 is None:
            masa0 = masa
        errores_masa.append(abs(masa - masa0))
        if n == nsteps:
            break
        uc_old = uc.copy()
        Fc = A * np.roll(uc_old, 1)  # flujo en la cara izquierda de cada celda gruesa
        uc_new = uc - dtc / dxc * (np.roll(Fc, -1) - Fc)
        flujos_izq, flujos_der = [], []
        for s in range(2):
            ghost = uc_old[I0 - 1] if s == 0 else 0.5 * (uc_old[I0 - 1] + uc_new[I0 - 1])
            Ff = A * np.concatenate([[ghost], uf[:-1]])  # caras izquierdas de las celdas finas
            flujos_izq.append(Ff[0])
            flujos_der.append(A * uf[-1])
            uf = uf - (dtc / 2) / dxf * (np.concatenate([Ff[1:], [A * uf[-1]]]) - Ff)
        if corregir:
            uc_new[I0 - 1] += dtc / dxc * (Fc[I0] - 0.5 * (flujos_izq[0] + flujos_izq[1]))
            uc_new[I1] += dtc / dxc * (0.5 * (flujos_der[0] + flujos_der[1]) - Fc[I1])
        uc = uc_new
        uc[I0:I1] = 0.5 * (uf[0::2] + uf[1::2])  # restricción
    return xc, uc, xf, uf, max(errores_masa)


def error_vs_exacta(xc, uc, xf, uf, t):
    ex = lambda x: np.exp(-((((x - t) % 1.0 - 0.2) / 0.05) ** 2))
    return float(np.max(np.abs(uf - ex(xf)))), float(np.max(np.abs(uc - ex(xc))))


print("(c) pulso gaussiano con parche fino sobre [0.25, 0.5): conservación de la masa")
res = {}
for corregir in (True, False):
    xc, uc, xf, uf, dm = simular(corregir, 0.5)
    res[corregir] = dm
    print(f"    corrección de flujo = {str(corregir):5s}  máx |masa - masa inicial| = {dm:.3e}")
assert res[True] < 1e-13 and res[False] > 1e-6

print("    precisión en t = 0.15 (pulso dentro del parche): error máx frente a la solución exacta")
xc, uc, xf, uf, _ = simular(True, 0.15)
ef, ec = error_vs_exacta(xc, uc, xf, uf, 0.15)
# malla gruesa pura de referencia, mismo esquema
uc2 = np.exp(-((((np.arange(NC) + 0.5) / NC) - 0.2) / 0.05) ** 2)
for _ in range(12):
    uc2 = uc2 - NU_C * (uc2 - np.roll(uc2, 1))
e_grueso = float(np.max(np.abs(uc2 - np.exp(-(((((np.arange(NC) + 0.5) / NC) - 0.15 - 0.2) / 0.05) ** 2)))))
# malla fina pura de referencia
NF = 2 * NC
uf2 = np.exp(-((((np.arange(NF) + 0.5) / NF) - 0.2) / 0.05) ** 2)
for _ in range(24):
    uf2 = uf2 - NU_C * (uf2 - np.roll(uf2, 1))
e_fino = float(np.max(np.abs(uf2 - np.exp(-(((((np.arange(NF) + 0.5) / NF) - 0.15 - 0.2) / 0.05) ** 2)))))
print(f"    AMR (parche) = {ef:.4e}   malla gruesa pura = {e_grueso:.4e}   malla fina pura = {e_fino:.4e}")
assert e_fino <= ef < e_grueso
print("Pruebas superadas.")
