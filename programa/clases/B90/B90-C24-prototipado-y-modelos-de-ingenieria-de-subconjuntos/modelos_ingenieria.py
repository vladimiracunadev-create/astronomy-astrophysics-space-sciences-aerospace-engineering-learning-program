#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C24: filosofias de modelos (solo vuelo, protovuelo, modelo de ingenieria + vuelo) con costo esperado y riesgo residual (SINTETICO).

Un defecto de diseno existe con probabilidad q. Cada modelo de prueba lo detecta con probabilidad d_i (ensayos distintos). Un defecto que escapa
al vuelo cuesta F_perdida. Costo esperado = costo de modelos + costo de correccion si se detecta + q P(escapa) F_perdida.
Comparacion analitica y Monte Carlo (semilla fija). Todas las probabilidades y costos (en unidades de costo, uc) son SINTETICOS.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: costos en unidades de costo (uc); q = 0.30 de defecto de diseno")
q = 0.30
F = 1000.0                                   # uc: perdida de la mision si el defecto llega a orbita
corr_ing, corr_vuelo = 20.0, 120.0           # uc: corregir un defecto hallado en el modelo de ingenieria o en el de vuelo
filos = {
    "A: solo vuelo": dict(costo=100.0, etapas=[("vuelo", 0.70, corr_vuelo)]),
    "B: protovuelo": dict(costo=130.0, etapas=[("protovuelo", 0.85, corr_vuelo)]),
    "C: ingenieria + vuelo": dict(costo=100.0 + 60.0, etapas=[("ingenieria", 0.80, corr_ing), ("vuelo", 0.70, corr_vuelo)]),
}
def analitico(f):
    c = f["costo"]
    p_no = 1.0
    c_corr = 0.0
    for _, d, k in f["etapas"]:
        c_corr += q * p_no * d * k
        p_no *= (1 - d)
    return c + c_corr + q * p_no * F, q * p_no

rng = np.random.default_rng(90)
N = 2_000_000
print("filosofia               costo modelos  P(escapa)  costo esperado (uc)  MC (uc)")
res = {}
for nombre, f in filos.items():
    ce, resid = analitico(f)
    defecto = rng.random(N) < q
    costo = np.full(N, f["costo"])
    vivo = defecto.copy()
    for _, d, k in f["etapas"]:
        det = vivo & (rng.random(N) < d)
        costo += np.where(det, k, 0.0)
        vivo = vivo & ~det
    costo += np.where(vivo, F, 0.0)
    mc = costo.mean()
    se = costo.std() / math.sqrt(N)
    res[nombre] = (ce, resid)
    print(f"{nombre:22s} {f['costo']:12.0f} {resid:10.4f} {ce:19.2f} {mc:9.2f}")
    comprobar(abs(mc - ce) < 4 * se, "el Monte Carlo debe coincidir con el costo analitico")
mejor = min(res, key=lambda k: res[k][0])
print("Menor costo esperado:", mejor)
comprobar(res["C: ingenieria + vuelo"][1] < res["A: solo vuelo"][1], "agregar un modelo de ingenieria debe bajar el riesgo residual")
print("Sensibilidad: F (uc) -> menor costo esperado")
for FF in (200.0, 500.0, 1000.0, 5000.0):
    F = FF
    r = {k: analitico(v)[0] for k, v in filos.items()}
    print(f"   {FF:6.0f} -> {min(r, key=r.get)} ({min(r.values()):.1f})")
fin()
