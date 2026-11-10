#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C12: cocientes, normalizacion y norma mineral de un meteorito SINTETICO.

Datos: SINTETICOS. La composicion modal inyectada (forsterita 30 %, fayalita 10 %, enstatita 60 % en masa) y la composicion de referencia para normalizar son inventadas;
no representan a ningun meteorito. Pesos atomicos estandar del NIST (consultados el 2026-11-09): Mg 24.305 (punto medio de [24.304, 24.307]), Si 28.085 (punto medio de [28.084, 28.086]),
Fe 55.845; O = 15.9994 (de las masas isotopicas del NIST).
Modelo: oxidos MgO, FeO, SiO2 en % en masa -> moles -> sistema lineal 3x3 para los moles de forsterita (Mg2SiO4), fayalita (Fe2SiO4) y enstatita (MgSiO3); resolucion por eliminacion
gaussiana con pivote parcial. Se invierte la direccion directa (modal -> oxidos) y se comprueba la recuperacion.
Supuestos: solo tres oxidos y tres minerales; sin Al, Ca, Ni ni fases opacas. Validez: ilustrativa.
Tolerancia: recuperacion del modal a 1e-10; suma de masas de los minerales igual a la suma de los oxidos a 1e-10.
"""
from __future__ import annotations
import platform

M = {"Mg": 24.305, "Si": 28.085, "Fe": 55.845, "O": 15.9994}
MM = {"MgO": M["Mg"] + M["O"], "FeO": M["Fe"] + M["O"], "SiO2": M["Si"] + 2 * M["O"]}
# minerales: moles de cada oxido por mol de mineral (MgO, FeO, SiO2)
MIN = {"forsterita Mg2SiO4": (2, 0, 1), "fayalita Fe2SiO4": (0, 2, 1), "enstatita MgSiO3": (1, 0, 1)}
MM_MIN = {k: v[0] * MM["MgO"] + v[1] * MM["FeO"] + v[2] * MM["SiO2"] for k, v in MIN.items()}

def directo(modal):
    """modal (% masa) -> oxidos (% masa)"""
    ox = {"MgO": 0.0, "FeO": 0.0, "SiO2": 0.0}
    for k, w in modal.items():
        mol = w / MM_MIN[k]
        a, b, c = MIN[k]
        ox["MgO"] += mol * a * MM["MgO"]; ox["FeO"] += mol * b * MM["FeO"]; ox["SiO2"] += mol * c * MM["SiO2"]
    return ox

def resolver(A, b):
    n = len(b)
    A = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[p] = A[p], A[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n + 1):
                A[r][c] -= f * A[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (A[i][n] - sum(A[i][c] * x[c] for c in range(i + 1, n))) / A[i][i]
    return x

def inverso(ox):
    """oxidos (% masa) -> modal (% masa) """
    mol = [ox["MgO"] / MM["MgO"], ox["FeO"] / MM["FeO"], ox["SiO2"] / MM["SiO2"]]
    nombres = list(MIN)
    A = [[MIN[k][i] for k in nombres] for i in range(3)]
    x = resolver(A, mol)
    return {k: x[j] * MM_MIN[k] for j, k in enumerate(nombres)}

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Masas molares [g/mol]: " + ", ".join(f"{k} {v:.4f}" for k, v in MM.items()) + " ; " + ", ".join(f"{k} {v:.3f}" for k, v in MM_MIN.items()))
    modal = {"forsterita Mg2SiO4": 30.0, "fayalita Fe2SiO4": 10.0, "enstatita MgSiO3": 60.0}
    ox = directo(modal)
    print("A. Meteorito SINTETICO: modal inyectado -> oxidos (% masa)")
    for k, v in ox.items():
        print(f"   {k:5s} {v:8.4f}")
    s_ox = sum(ox.values())
    print(f"   suma de oxidos = {s_ox:.6f} (igual a la suma del modal, 100)")
    assert abs(s_ox - 100.0) < 1e-9
    rec = inverso(ox)
    err = max(abs(rec[k] - modal[k]) for k in modal)
    print("B. Norma mineral recuperada (% masa) frente al modal inyectado")
    for k in modal:
        print(f"   {k:20s} {rec[k]:10.6f}   inyectado {modal[k]:6.2f}")
    print(f"   error maximo = {err:.2e}")
    assert err < 1e-10
    # cocientes molares
    n_mg = ox["MgO"] / MM["MgO"]; n_fe = ox["FeO"] / MM["FeO"]; n_si = ox["SiO2"] / MM["SiO2"]
    print(f"C. Cocientes molares: Mg/Si = {n_mg / n_si:.4f} ; Fe/Si = {n_fe / n_si:.4f} ; Mg# = Mg/(Mg+Fe) = {n_mg / (n_mg + n_fe):.4f}")
    # normalizacion a una referencia SINTETICA
    ref = {"Mg/Si": 0.95, "Fe/Si": 0.60}
    obs = {"Mg/Si": n_mg / n_si, "Fe/Si": n_fe / n_si}
    print("D. Normalizacion a una referencia SINTETICA (valor/referencia)")
    for k in obs:
        print(f"   {k}: {obs[k]:.4f} / {ref[k]:.2f} = {obs[k] / ref[k]:.4f}")
    # olivino: forsterita molar
    fo = rec["forsterita Mg2SiO4"] / MM_MIN["forsterita Mg2SiO4"]
    fa = rec["fayalita Fe2SiO4"] / MM_MIN["fayalita Fe2SiO4"]
    print(f"E. Fo# del olivino = Fo/(Fo+Fa) en moles = {100 * fo / (fo + fa):.2f}")
    # sensibilidad: perturbar FeO en 1 % relativo
    ox2 = dict(ox); ox2["FeO"] *= 1.01
    rec2 = inverso(ox2)
    print(f"F. Sensibilidad: +1 % relativo de FeO cambia la fayalita de {rec['fayalita Fe2SiO4']:.4f} a {rec2['fayalita Fe2SiO4']:.4f} % masa")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
