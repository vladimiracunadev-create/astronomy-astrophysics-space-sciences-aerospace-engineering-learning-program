#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C05: calibracion cinematica por Gauss-Newton con mediciones SINTETICAS de posicion de la herramienta.

Parametros (10): desfases de las 7 articulaciones y errores de d1, d3, d5. Ruido sintetico de 0.2 mm por eje (gaussiano, semilla 105).
Unidades: m, rad. 60 poses de calibracion y 40 de validacion distintas. Tolerancia: error de parametro dentro de 4 sigma.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: mediciones con ruido de 0.2 mm por eje; errores verdaderos inventados")
rng = np.random.default_rng(105)
sig = 2e-4
p_ver = np.concatenate([rng.normal(0, np.radians(0.5), 7), rng.normal(0, 2e-3, 3)])
q_cal = [rng.uniform(-2, 2, 7) for _ in range(60)]
q_val = [rng.uniform(-2, 2, 7) for _ in range(40)]
y_cal = [pos_tool(q, p_ver) + rng.normal(0, sig, 3) for q in q_cal]
y_val = [pos_tool(q, p_ver) + rng.normal(0, sig, 3) for q in q_val]


def rms(qs, ys, p):
    e = np.array([pos_tool(q, p) - y for q, y in zip(qs, ys)])
    return float(np.sqrt((e**2).sum(1).mean()))


p0 = np.zeros(NPAR)
J0 = jac_param(q_cal, p0)
s = np.linalg.svd(J0, compute_uv=False)
print(f"Identificabilidad: rango de J (180x10) = {np.linalg.matrix_rank(J0)} ; sigma_min = {s[-1]:.3f}, sigma_max = {s[0]:.3f}")
comprobar(np.linalg.matrix_rank(J0) == NPAR, "los 10 parametros deben ser identificables")
print(f"Antes de calibrar: RMS 3D en validacion = {rms(q_val, y_val, p0) * 1000:.3f} mm")
p_est = calibrar(q_cal, y_cal)
r_cal, r_val = rms(q_cal, y_cal, p_est), rms(q_val, y_val, p_est)
piso = sig * np.sqrt(3)
print(f"Despues: RMS en calibracion = {r_cal * 1000:.3f} mm ; en validacion = {r_val * 1000:.3f} mm ; piso de ruido = {piso * 1000:.3f} mm")
comprobar(r_val < 1.3 * piso, "la validacion debe acercarse al piso de ruido")
J = jac_param(q_cal, p_est)
cov = sig**2 * np.linalg.inv(J.T @ J)
sd = np.sqrt(np.diag(cov))
nombres = [f"dtheta{i + 1}" for i in range(7)] + ["dd1", "dd3", "dd5"]
print("parametro   verdadero   estimado    error      sigma     |err|/sigma")
dentro = 0
for k in range(NPAR):
    u = 1000 if k >= 7 else 180 / np.pi
    unidad = "mm" if k >= 7 else "gr"
    e = p_est[k] - p_ver[k]
    dentro += abs(e) < 4 * sd[k]
    print(f"{nombres[k]:8s}  {p_ver[k] * u:9.4f}  {p_est[k] * u:9.4f}  {e * u:9.4f}  {sd[k] * u:8.4f}   {abs(e) / sd[k]:5.2f}   [{unidad}]")
comprobar(dentro == NPAR, "cada error de parametro debe estar dentro de 4 sigma")
# Monte Carlo de la covarianza: 100 repeticiones del ruido
errs = []
for _ in range(100):
    yy = [pos_tool(q, p_ver) + rng.normal(0, sig, 3) for q in q_cal]
    errs.append(calibrar(q_cal, yy, p0=p_est, iteraciones=3) - p_ver)
errs = np.array(errs)
razon = errs.std(0) / sd
print(f"Monte Carlo de 100 repeticiones: desviacion observada / sigma teorica: min = {razon.min():.2f}, max = {razon.max():.2f}")
comprobar(0.7 < razon.min() and razon.max() < 1.4, "la covarianza teorica debe coincidir con el Monte Carlo")
# parametro no identificable si la herramienta esta en el eje: demostracion
TOOL_ejemplo = np.array([0.0, 0.0, 0.15])
cols = []
for k in (6,):
    h = 1e-6
    dp = np.zeros(NPAR)
    dp[k] = h
    cambio = []
    for q in q_cal[:20]:
        T1 = fk(q, th0=THETA0_NOM + dp[:7])
        T0 = fk(q)
        cambio.append(np.linalg.norm(T1[:3, :3] @ TOOL_ejemplo + T1[:3, 3] - (T0[:3, :3] @ TOOL_ejemplo + T0[:3, 3])))
print(f"Con la herramienta sobre el eje z7, el efecto de dtheta7 en la posicion es {max(cambio):.1e} m: no es identificable")
comprobar(max(cambio) < 1e-9, "dtheta7 no se ve con una herramienta en el eje")
fin()
