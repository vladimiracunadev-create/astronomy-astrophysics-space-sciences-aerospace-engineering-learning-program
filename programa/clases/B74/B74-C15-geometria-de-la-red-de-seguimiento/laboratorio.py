#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C15: geometria de la red de seguimiento y dilucion de la precision con alcance simultaneo.

Todo SINTETICO: tres estaciones SINTETICAS en una esfera de 6 378 137 m (valor ilustrativo del radio) en dos configuraciones:
'amplia' (longitudes 0, 120, 240 grados; latitudes 35, -35, 40) y 'agrupada' (tres estaciones a menos de 1 000 km entre si).
Nave a 1.0e9 m (1 millon de km) en 1000 direcciones aleatorias (semilla 53). Medidas: alcances simultaneos con sigma 1 m
(ILUSTRATIVO). Para cada direccion: (HtH)^-1 sigma^2 -> sigma 3D (raiz de la traza) con la descomposicion en componentes a lo largo de la linea de vision
y transversal. Sin mascara de horizonte (geometria pura: en la practica las estaciones ven a la nave en pases sucesivos y la rotacion terrestre aporta la geometria; aqui se supone alcance simultaneo). Se descartan matrices mal condicionadas (cond > 1e12).
Prediccion: sigma_transversal ~ sigma_alcance * rho / B para dos estaciones con linea de base B (la mitad del rango de B a rho 1e9).
Tolerancia: la sigma transversal simulada (mediana) coincide con sigma*rho/B_efectiva entre 0.5 y 4 veces la prediccion (aproximacion de orden de magnitud); la red agrupada debe ser mas de 5 veces peor.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

RE = 6378137.0


def est(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return RE * np.array([math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la)])


REDES = {
    "amplia": [est(35, 0), est(-35, 120), est(40, 240)],
    "agrupada": [est(35, 0), est(35.5, 5), est(36, 10)],
}


def visible(p, s):
    return np.dot(p - s, s) > 0


def main():
    rng = np.random.default_rng(53)
    rho = 1.0e9
    N = 1000
    D = rng.normal(size=(N, 3)); D /= np.linalg.norm(D, axis=1)[:, None]
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (estaciones y direcciones SINTETICAS, semilla 53)",
           f"nave a {rho:.1e} m ; alcance sigma = 1 m ; {N} direcciones"]
    res = {}
    out.append("red       dir. validas   sigma 3D mediana [m]  p95 [m]   sigma transversal mediana [m]   linea de base [km]")
    ok = True
    for nom, S in REDES.items():
        v3 = []; tr = []; ln = []
        for u in D:
            x = rho * u
            H = np.array([(x - s) / np.linalg.norm(x - s) for s in S])
            A = H.T @ H
            if np.linalg.cond(A) > 1e12:
                continue
            P = np.linalg.inv(A)
            v3.append(math.sqrt(np.trace(P)))
            # componente a lo largo de la linea de vision
            sl = math.sqrt(u @ P @ u)
            ln.append(sl)
            tr.append(math.sqrt(max(np.trace(P) - sl**2, 0.0) / 2))
        v3, tr, ln = map(np.array, (v3, tr, ln))
        B = max(np.linalg.norm(S[i] - S[j]) for i in range(3) for j in range(i + 1, 3))
        out.append(f"{nom:9s} {len(v3):10d}   {np.median(v3):18.1f}  {np.percentile(v3,95):8.1f}   {np.median(tr):18.1f}   {B/1e3:14.0f}")
        res[f"{nom}_n"] = int(len(v3)); res[f"{nom}_med"] = float(np.median(v3)); res[f"{nom}_p95"] = float(np.percentile(v3, 95))
        res[f"{nom}_tr"] = float(np.median(tr)); res[f"{nom}_B"] = float(B / 1e3); res[f"{nom}_ln"] = float(np.median(ln))
        pred = rho / B
        res[f"{nom}_pred"] = float(pred)
        ok &= 0.5 < np.median(tr) / pred < 4.0 if nom == "amplia" else True
    ratio = res["agrupada_med"] / res["amplia_med"]
    res["ratio"] = float(ratio)
    out.append(f"sigma 3D agrupada / amplia (medianas) = {ratio:.1f}")
    out.append(f"Prediccion sigma_alcance*rho/B: amplia = {res['amplia_pred']:.1f} m, agrupada = {res['agrupada_pred']:.1f} m")
    ok &= ratio > 5
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
