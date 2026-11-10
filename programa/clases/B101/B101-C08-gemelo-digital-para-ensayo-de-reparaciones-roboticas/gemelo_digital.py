#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C08: gemelo digital: modelo nominal frente a una 'realidad' SINTETICA con errores de parametros; ensayo de una insercion.

La 'realidad' es el mismo brazo de B101-C01 con errores cinematicos inventados (no observados). El gemelo empieza nominal y se
recalibra con 60 mediciones sinteticas (ruido 0.2 mm por eje, semilla 108). Tarea: llevar la herramienta a 40 posiciones objetivo
y exigir un error de posicion menor que 5 mm (umbral ILUSTRATIVO de la insercion). Unidades: m, rad.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: realidad con errores inventados, ruido 0.2 mm, umbral de insercion de 5 mm (ilustrativo)")
rng = np.random.default_rng(108)
sig = 2e-4
p_real = np.concatenate([rng.normal(0, np.radians(0.5), 7), rng.normal(0, 2e-3, 3)])


def ik_pos(objetivo, p, q0):
    """Cinematica inversa de posicion de la herramienta con el modelo p (Newton amortiguado, orientacion libre)."""
    q = q0.copy()
    for _ in range(200):
        e = objetivo - pos_tool(q, p)
        if np.linalg.norm(e) < 1e-10:
            break
        h = 1e-6
        J = np.array([(pos_tool(q + h * np.eye(7)[i], p) - pos_tool(q - h * np.eye(7)[i], p)) / (2 * h) for i in range(7)]).T
        q = q + J.T @ np.linalg.solve(J @ J.T + 1e-4 * np.eye(3), e)
    return q


# 40 objetivos alcanzables
q_ref = [rng.uniform(-1.5, 1.5, 7) for _ in range(40)]
objetivos = [pos_tool(q, np.zeros(NPAR)) for q in q_ref]
UMBRAL = 5e-3


def ensayo(p_gemelo, etiqueta):
    errs = []
    for obj, qr in zip(objetivos, q_ref):
        qc = ik_pos(obj, p_gemelo, qr)           # el gemelo planifica
        errs.append(np.linalg.norm(pos_tool(qc, p_real) - obj))   # la realidad ejecuta
    errs = np.array(errs)
    print(f"{etiqueta}: error mediano = {np.median(errs) * 1000:7.3f} mm ; maximo = {errs.max() * 1000:7.3f} mm ; dentro de 5 mm = {(errs < UMBRAL).sum()}/40")
    return errs


e_nom = ensayo(np.zeros(NPAR), "Gemelo nominal       ")
comprobar((e_nom < UMBRAL).sum() < 30, "el gemelo nominal falla en parte de las inserciones")
# autoverificacion: un gemelo perfecto falla 0
e_per = ensayo(p_real, "Gemelo perfecto      ")
comprobar(e_per.max() < 1e-6, "con el modelo exacto la realidad coincide")

# recalibracion con mediciones de la realidad
q_cal = [rng.uniform(-2, 2, 7) for _ in range(60)]
y = [pos_tool(q, p_real) + rng.normal(0, sig, 3) for q in q_cal]
p_cal = calibrar(q_cal, y)
e_cal = ensayo(p_cal, "Gemelo recalibrado   ")
comprobar((e_cal < UMBRAL).sum() == 40 and np.median(e_cal) < np.median(e_nom) / 10, "la recalibracion devuelve el margen")
print(f"Residuo de modelo (RMS 3D sobre 40 poses nuevas): nominal = {np.sqrt(np.mean([np.sum((pos_tool(q, p_real) - pos_tool(q, np.zeros(NPAR))) ** 2) for q in q_ref])) * 1000:.3f} mm ; recalibrado = {np.sqrt(np.mean([np.sum((pos_tool(q, p_real) - pos_tool(q, p_cal)) ** 2) for q in q_ref])) * 1000:.3f} mm")

# margen de la maniobra: cuanto error de parametros tolera la insercion (Monte Carlo)
print("Margen frente al error cinematico: probabilidad de insercion dentro de 5 mm (300 ensayos por fila)")
print("  sigma angulos [grados]  sigma d [mm]  probabilidad")
prob = []
for sa, sd in ((0.05, 0.2), (0.1, 0.5), (0.25, 1.0), (0.5, 2.0), (1.0, 4.0)):
    ok = 0
    for _ in range(300):
        pr = np.concatenate([rng.normal(0, np.radians(sa), 7), rng.normal(0, sd * 1e-3, 3)])
        q = q_ref[rng.integers(40)]
        obj = pos_tool(q, np.zeros(NPAR))
        qc = ik_pos(obj, np.zeros(NPAR), q)
        ok += np.linalg.norm(pos_tool(qc, pr) - obj) < UMBRAL
    prob.append(ok / 300)
    print(f"  {sa:20.2f}  {sd:12.1f}  {ok / 300:12.3f}")
comprobar(prob[0] > prob[-1] and prob[0] > 0.95, "la probabilidad decrece al empeorar el modelo")
fin()
