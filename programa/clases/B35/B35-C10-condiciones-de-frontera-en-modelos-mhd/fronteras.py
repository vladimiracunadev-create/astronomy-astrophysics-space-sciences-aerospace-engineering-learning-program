#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C10: reflexion de una onda de Alfven en tres condiciones de frontera de una malla escalonada.

Datos: ninguna constante fisica ni dato observado. El problema esta normalizado (v_A = 1, dominio de longitud 1) y la forma del pulso, la resolucion y el tiempo son ILUSTRATIVOS (sinteticos).
Modelo: ondas de Alfven transversales 1D con velocidad v y campo b (en unidades de velocidad): dv/dt = db/dx, db/dt = dv/dx. Un pulso gaussiano que viaja hacia +x cumple b = -v. Malla escalonada
(v en los nodos, b en los puntos medios) con salto de rana y CFL = 0.5. Fronteras derechas: (a) pared rigida v = 0 (analitica: v reflejado = -v incidente); (b) gradiente nulo v_N = v_(N-1)
(analitica: v reflejado = +v incidente); (c) caracteristica saliente v_N = -b_(N-1/2) (la onda entrante se anula; reflexion nula en el limite continuo).
Medida: coeficiente de reflexion R = max|v| (en x < 0.93, donde solo esta la onda reflejada) / max|v| del pulso incidente, y fraccion de energia que queda en el dominio.
Supuestos: lineal, 1D, vA uniforme; la frontera de caracteristicas es de primer orden. Validez: ilustrativa.
Tolerancia: R de (a) y (b) igual a 1 con error < 2 %; signo del pulso reflejado correcto; R de (c) < 0.02 para la anchura de 12 celdas y decreciente al ensanchar el pulso.
"""
from __future__ import annotations
import math, platform, sys

def correr(tipo, ancho, N=400, tf=0.5, x0=0.7):
    L = 1.0; dx = L / N; dt = 0.5 * dx; c = dt / dx
    g = lambda x: math.exp(-0.5 * ((x - x0) / ancho) ** 2)
    v = [g(i * dx) for i in range(N + 1)]
    b = [-g((i + 0.5) * dx - dt / 2) for i in range(N)]  # b en t = dt/2
    pasos = int(round(tf / dt))
    for _ in range(pasos):
        for i in range(1, N):
            v[i] += c * (b[i] - b[i - 1])
        # fronteras en el nuevo tiempo
        v[0] = b[0]  # la izquierda es saliente para ondas que van a -x: v = b
        if tipo == "pared":
            v[N] = 0.0
        elif tipo == "gradiente":
            v[N] = v[N - 1]
        else:
            v[N] = -b[N - 1]
        for i in range(N):
            b[i] += c * (v[i + 1] - v[i])
    vmax_ini = 1.0
    imax = max(range(int(0.93 * N)), key=lambda i: abs(v[i]))
    signo = 1 if v[imax] > 0 else -1
    R = abs(v[imax]) / vmax_ini
    en = 0.5 * dx * (sum(x * x for x in v) + sum(y * y for y in b))
    en0 = ancho * math.sqrt(math.pi)  # integral de (v^2 + b^2)/2 = integral de v^2 del pulso gaussiano
    return R, signo, en / en0, imax * dx

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'frontera':>10} {'ancho':>7} {'R':>8} {'signo de v reflejado':>21} {'energia restante':>17} {'posicion del pulso':>19}")
    res = {}
    for tipo in ("pared", "gradiente", "caracteristica"):
        for ancho in (0.06, 0.03, 0.015):
            R, sg, en, xp = correr(tipo, ancho)
            res[(tipo, ancho)] = (R, sg, en)
            print(f"{tipo:>10} {ancho:7.3f} {R:8.5f} {sg:21d} {en:17.5f} {xp:19.4f}")
    for ancho in (0.06, 0.03):
        assert abs(res[("pared", ancho)][0] - 1) < 0.02 and res[("pared", ancho)][1] == -1
        assert abs(res[("gradiente", ancho)][0] - 1) < 0.02 and res[("gradiente", ancho)][1] == +1
    r = [res[("caracteristica", a)][0] for a in (0.06, 0.03, 0.015)]
    assert r[1] < 0.02 and r[0] < r[1] < r[2]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
