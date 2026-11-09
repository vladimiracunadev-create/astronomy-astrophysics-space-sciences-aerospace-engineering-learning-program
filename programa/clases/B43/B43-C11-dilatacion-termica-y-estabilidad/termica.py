#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C11: dilatacion termica y estabilidad: deriva de foco, compensacion con dos materiales y constante de tiempo de un espejo.

Datos: ILUSTRATIVOS (coeficientes de dilatacion acero 12, aluminio 23,6, fibra de carbono 0,5 en 1e-6/K; vidrio borosilicato k = 1,14 W/m/K, rho = 2230 kg/m^3, c = 830 J/kg/K; coeficiente de conveccion 5 W/m^2/K;
espejo f/5 de 200 mm, espesor 33,3 mm). Valores de orden de magnitud, NO consultados en una hoja de fabricante.
Modelo: dL = alpha L dT; profundidad de foco +-2 lambda N^2; compensacion alpha_1 L_1 = alpha_2 L_2 con L_1 - L_2 = F.
Tiempo de ecualizacion de una placa con conveccion en ambas caras: ecuacion transcendente zeta tan(zeta) = Bi (Bi = h L/k, L = semiespesor), tau = L^2/(kappa zeta^2),
contrastada con una simulacion de diferencias finitas explicita 1D (semiespesor, simetria en el centro, condicion de Robin en la cara), dt = 0,1 s.
Supuestos: 1D, propiedades constantes, h constante, sin radiacion. Validez: mediciones tipo orden de magnitud.
Tolerancia: tau de la simulacion frente a la raiz de la ecuacion transcendente, 2 % relativo; compensacion, 1e-9 mm.
"""
from __future__ import annotations
import math, platform

LAM = 550e-9; NF = 5.0

def raiz_biot(Bi):
    lo, hi = 1e-6, math.pi / 2 - 1e-9
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid * math.tan(mid) > Bi:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def simular(Bi_h, k, rho, c, Lh, nx=24, dt=0.1, tmax=20000.0):
    kap = k / (rho * c); dx = Lh / nx
    assert kap * dt / dx ** 2 < 0.5
    T = [1.0] * (nx + 1)
    reg = []
    t = 0.0; paso = 0
    while t < tmax:
        Tn = T[:]
        for i in range(1, nx):
            Tn[i] = T[i] + kap * dt / dx ** 2 * (T[i + 1] - 2 * T[i] + T[i - 1])
        Tn[0] = T[0] + kap * dt / dx ** 2 * 2 * (T[1] - T[0])
        # nodo de superficie con flujo conductivo y convectivo (balance de semivolumen)
        Tn[nx] = T[nx] + 2 * dt / (rho * c * dx) * (k * (T[nx - 1] - T[nx]) / dx - Bi_h * T[nx])
        T = Tn; t += dt; paso += 1
        if paso % 500 == 0:
            reg.append((t, sum(T) / len(T)))
    return reg

def calc():
    r = {}
    al = {"acero": 12.0, "aluminio": 23.6, "carbono": 0.5}
    L = 1.0; dT = 10.0
    r["dL_um"] = {k: v * 1e-6 * L * dT * 1e6 for k, v in al.items()}
    r["prof_foco_um"] = 2 * LAM * NF ** 2 * 1e6
    r["dT_max_K"] = {k: r["prof_foco_um"] / (v * 1e-6 * L * 1e6) for k, v in al.items()}
    F = 1000.0
    a1, a2 = al["acero"], al["aluminio"]
    L1 = F * a2 / (a2 - a1); L2 = F * a1 / (a2 - a1)
    r["L_acero_mm"] = L1; r["L_aluminio_mm"] = L2
    r["neto_mm"] = L1 - L2
    r["deriva_compensada_mm"] = (a1 * L1 - a2 * L2) * 1e-6 * dT
    k, rho, c, h = 1.14, 2230.0, 830.0, 5.0
    Lh = 0.0333 / 2
    Bi = h * Lh / k
    zeta = raiz_biot(Bi)
    kap = k / (rho * c)
    r["Bi"] = Bi; r["tau_exacto_s"] = Lh ** 2 / (kap * zeta ** 2)
    r["tau_agrupado_s"] = rho * c * Lh / h
    reg = simular(h, k, rho, c, Lh)
    # tasa entre 2000 s y 12000 s
    (t1, m1), (t2, m2) = [x for x in reg if x[0] >= 2000][0], [x for x in reg if x[0] >= 12000][0]
    r["tau_sim_s"] = (t2 - t1) / math.log(m1 / m2)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k in ("dL_um", "dT_max_K"):
        print(k, {a: round(b, 3) for a, b in r[k].items()})
    for k in ("prof_foco_um", "L_acero_mm", "L_aluminio_mm", "neto_mm", "deriva_compensada_mm", "Bi", "tau_exacto_s", "tau_agrupado_s", "tau_sim_s"):
        print(f"{k} = {r[k]:.6g}")
    assert abs(r["neto_mm"] - 1000.0) < 1e-9 and abs(r["deriva_compensada_mm"]) < 1e-9
    assert abs(r["tau_sim_s"] - r["tau_exacto_s"]) / r["tau_exacto_s"] < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
