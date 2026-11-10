#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C30: asociacion de observaciones a pistas con compuerta de Mahalanobis y asignacion global frente a vecino mas cercano.

Todo SINTETICO: 4 pistas con posiciones predichas en el plano (km) separadas entre si por 1.5 a 3 sigma de la covarianza de innovacion S = sigma^2 I con sigma = 1.0 km (ILUSTRATIVO), 4 observaciones
(una por objeto, ruido gaussiano de sigma) y clutter de Poisson con 2 falsas detecciones por escena en un cuadrado de 20 x 20 km. Compuerta: d^2 = nu^T S^-1 nu < g con g = chi2 de 2 gl al 99 % = -2 ln(0.01).
Metodos: (a) vecino mas cercano voraz (cada pista toma la observacion de menor distancia dentro de la compuerta, en orden de pista; una observacion puede ser tomada solo una vez); (b) asignacion global
de costo minimo (suma de d^2) por busqueda exhaustiva con poda (recursion sobre las pistas; una pista puede quedar sin asociar con una penalizacion de 2 g). Se reporta la fraccion de escenas con las 4 asociaciones correctas, la fraccion de asociaciones
individuales correctas y la fraccion de observaciones verdaderas fuera de compuerta (esperada 1 %). 3000 escenas por configuracion (semilla 103).
Tolerancias: la fraccion de observaciones verdaderas fuera de la compuerta esta entre 0.5 % y 1.5 %; la asignacion global no es peor que el vecino mas cercano en la fraccion de escenas correctas.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

SIG = 1.0
G = -2 * math.log(0.01)


def escena(rng, sep):
    base = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]) * sep * SIG + np.array([10.0, 10.0])
    obs = base + rng.normal(0, SIG, base.shape)
    nc = rng.poisson(2.0)
    clut = rng.uniform(0, 20, (nc, 2))
    todas = np.vstack([obs, clut]) if nc else obs
    perm = rng.permutation(len(todas))
    return base, todas[perm], np.argsort(perm)[:4]  # indice de cada observacion verdadera dentro de 'todas'


def vecino(pred, z):
    usadas = set(); res = []
    for p in pred:
        d2 = np.sum((z - p) ** 2, axis=1) / SIG**2
        orden = np.argsort(d2)
        elegido = -1
        for j in orden:
            if d2[j] < G and j not in usadas:
                elegido = int(j); usadas.add(j); break
        res.append(elegido)
    return res


def global_(pred, z):
    n, m = len(pred), len(z)
    d2 = np.sum((z[None, :, :] - pred[:, None, :]) ** 2, axis=2) / SIG**2
    PEN = 2 * G  # costo de no asociar una pista
    mejor = None; mc = 1e18
    # busqueda por recursion: cada pista elige una observacion no usada o ninguna
    def rec(i, usadas, costo, asig):
        nonlocal mejor, mc
        if costo >= mc:
            return
        if i == n:
            mc, mejor = costo, asig[:]
            return
        for j in range(m):
            if j not in usadas and d2[i, j] < G:
                rec(i + 1, usadas | {j}, costo + d2[i, j], asig + [j])
        rec(i + 1, usadas, costo + PEN, asig + [-1])
    rec(0, frozenset(), 0.0, [])
    return mejor


def main():
    rng = np.random.default_rng(103)
    NE = 3000
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (escenas SINTETICAS, semilla 103)",
           f"compuerta chi2 (2 gl, 99 %) = {G:.3f} ; sigma = {SIG} km ; clutter medio = 2 falsas detecciones por escena"]
    res = {}
    out.append("separacion      vecino mas cercano: escenas OK / asoc. OK      global: escenas OK / asoc. OK      verdaderas fuera de compuerta")
    ok = True
    for sep in (1.5, 3.0, 6.0):
        a_esc = a_as = g_esc = g_as = fuera = tot = 0
        for _ in range(NE):
            base, z, idx = escena(rng, sep)
            va = vecino(base, z); vg = global_(base, z)
            a_as += sum(int(va[k] == idx[k]) for k in range(4)); g_as += sum(int(vg[k] == idx[k]) for k in range(4))
            a_esc += int(all(va[k] == idx[k] for k in range(4))); g_esc += int(all(vg[k] == idx[k] for k in range(4)))
            for k in range(4):
                tot += 1
                fuera += int(np.sum((z[idx[k]] - base[k]) ** 2) / SIG**2 >= G)
        fe = fuera / tot * 100
        out.append(f"{sep:6.1f} sigma     {a_esc/NE*100:12.1f} % / {a_as/(4*NE)*100:5.1f} %              {g_esc/NE*100:10.1f} % / {g_as/(4*NE)*100:5.1f} %            {fe:8.2f} %")
        k = str(sep).replace(".", "")
        res[f"ne_{k}"] = a_esc / NE * 100; res[f"na_{k}"] = a_as / (4 * NE) * 100
        res[f"ge_{k}"] = g_esc / NE * 100; res[f"ga_{k}"] = g_as / (4 * NE) * 100; res[f"fu_{k}"] = fe
        ok &= 0.5 < fe < 1.5 and g_esc >= a_esc
    res["G"] = G
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
