#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C31: lista de verificacion automatica para la revision de un analisis de elementos finitos.

DATOS ILUSTRATIVOS (no consultados): viga en voladizo de aluminio L = 1,0 m, b = 50 mm, h = 10 mm, E = 69 GPa, rho = 2700 kg/m3, 10 elementos de Euler-Bernoulli.
Se revisan cuatro modelos: el CORRECTO (SI: m, kg, N, Pa), y tres con errores inyectados a proposito:
  (B) error de unidades: E en MPa (69 000) con longitudes en metros y masa en kg;
  (C) error de densidad: rho en g/cm3 (2,7) en vez de kg/m3;
  (D) falta la restriccion de empotramiento (modelo libre).
Comprobaciones (con tolerancia): (1) simetria de K y M (1e-12); (2) masa total = rho A L (1e-9 relativa); (3) numero de modos de solido rigido del modelo libre = 2 (autovalor < 1e-10 del maximo);
(4) K restringida definida positiva (Cholesky); (6) flecha en el extremo con carga unitaria frente a P L^3/(3 E I) (1e-6);
(7) primera frecuencia frente a la analitica 1,875104^2/(2 pi) sqrt(EI/(rho A L^4)) (1 %).
Cada comprobacion da PASA/FALLA; el resultado final es un registro de revision.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import ensamblar_viga, reducir, jacobi_eig, solve, cholesky, gen_eig, matvec

B, H, L, N = 0.05, 0.01, 1.0, 10
A = B * H
I = B * H ** 3 / 12
E0, RHO0 = 69e9, 2700.0


def revisar(nombre, E, rho, restringido=True):
    n = 2 * (N + 1)
    K, M = ensamblar_viga(N, L, E * I, rho * A)
    out = []
    sim = max(abs(K[i][j] - K[j][i]) for i in range(n) for j in range(n)) / max(abs(K[i][i]) for i in range(n))
    out.append(("1 simetria de K", sim < 1e-12, f"{sim:.1e}"))
    rw = [1.0 if i % 2 == 0 else 0.0 for i in range(n)]
    m_tot = sum(rw[i] * v for i, v in enumerate(matvec(M, rw)))
    m_esp = RHO0 * A * L
    out.append(("2 masa total", abs(m_tot - m_esp) / m_esp < 1e-9, f"{m_tot:.4f} kg (esperada {m_esp:.4f})"))
    lam, _ = jacobi_eig(K)
    nul = sum(1 for l in lam if abs(l) / max(abs(x) for x in lam) < 1e-10)
    out.append(("3 modos de solido rigido libres = 2", nul == 2, f"{nul}"))
    libres = list(range(2, n)) if restringido else list(range(n))
    Kr = reducir(K, libres)
    try:
        cholesky(Kr)
        pd = True
    except ValueError:
        pd = False
    out.append(("4 K restringida definida positiva", pd, "si" if pd else "no"))
    if pd:
        f = [0.0] * len(libres)
        f[len(libres) - 2] = 1.0
        u = solve(Kr, f)
        w_tip = u[len(libres) - 2]
        w_ex = 1.0 * L ** 3 / (3 * E0 * I)
        out.append(("6 flecha con carga unitaria", abs(w_tip - w_ex) / w_ex < 1e-6, f"{w_tip * 1e3:.5f} mm (esperada {w_ex * 1e3:.5f})"))
        Mr = reducir(M, libres)
        l2, _ = gen_eig(Kr, Mr)
        f1 = math.sqrt(l2[0]) / (2 * math.pi)
        f1a = 1.875104 ** 2 / (2 * math.pi) * math.sqrt(E0 * I / (RHO0 * A * L ** 4))
        out.append(("7 primera frecuencia", abs(f1 - f1a) / f1a < 0.01, f"{f1:.3f} Hz (esperada {f1a:.3f})"))
    else:
        out.append(("6 flecha con carga unitaria", False, "no calculable (singular)"))
        out.append(("7 primera frecuencia", False, "no calculable (singular)"))
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Viga ILUSTRATIVA: 10 elementos, L = 1 m, 50 x 10 mm, aluminio")
    modelos = (("A correcto (SI)", E0, RHO0, True), ("B error de unidades (E en MPa)", 69e3, RHO0, True),
               ("C error de densidad (g/cm3)", E0, 2.7, True), ("D sin restriccion", E0, RHO0, False))
    resumen = {}
    for nombre, E, rho, restr in modelos:
        res = revisar(nombre, E, rho, restr)
        print(f"Modelo {nombre}:")
        for c, ok, det in res:
            print(f"   {'PASA ' if ok else 'FALLA'}  {c:38s} {det}")
        resumen[nombre] = sum(1 for _, ok, _ in res if not ok)
    print("Resumen de fallas por modelo: " + "; ".join(f"{k}: {v}" for k, v in resumen.items()))
    assert resumen["A correcto (SI)"] == 0
    assert all(resumen[k] > 0 for k in resumen if not k.startswith("A"))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
