#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C05: roturas dobles del ADN agrupadas a lo largo de una traza y su reparacion (modelo SINTETICO).

Valores consultados (2026-11-10, solo resumen en Europe PMC): Hagiwara et al., J Radiat Res 60:69-79 (2019): la radiacion de alto LET
deposita la energia de forma densa a lo largo de la traza, produce mas aberraciones cromosomicas (dicentricos, translocaciones) y
deleciones mayores de 1000 pb que los rayos X, y se observaron roturas dobles agrupadas a lo largo de la traza. Todo lo demas es
SINTETICO e ILUSTRATIVO (semilla 116) y NO esta calibrado con datos: rendimiento de roturas dobles de 35 por Gy y por nucleo para
radiacion dispersa, fraccion agrupada que crece con el LET, constantes de reparacion rapida (0.5/h) y lenta (0.05/h) y distancia de
interaccion de 0.5 um. Geometria: nucleo esferico de 10 um; una traza es una recta con cuerda aleatoria; las roturas de una traza se
colocan en posiciones uniformes a lo largo de la cuerda. Reparacion: cada rotura se repara con tasa exponencial segun su tipo (simple o
agrupada); una rotura no reparada en 24 h cuenta como residual; un error de reunion se cuenta por cada par de roturas no reparadas
aun a menos de 0.5 um cuando una de ellas se repara. Unidades: Gy, keV/um, um, h. Verificacion: a dosis fija el rendimiento total de
roturas es el mismo; la media de la cinetica simulada sigue la analitica dentro del 3 %; los residuales crecen con el LET.
Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

D_NUC = 10.0       # um
YIELD = 35.0       # roturas dobles por Gy por nucleo (INVENTADO, orden de magnitud ilustrativo)
K_RAP, K_LEN = 0.5, 0.05   # 1/h
R_INT = 0.5        # um
DOSIS = 1.0        # Gy
IONES = [("fotones", 0.3), ("proton", 0.5), ("helio", 2.0), ("carbono", 40.0), ("hierro", 150.0)]


def agrupada(let):
    """Probabilidad inventada de que una rotura de una traza sea 'agrupada' (compleja): sube con el LET."""
    return let / (let + 40.0)


def simula(let, rng, n=3000):
    cuerda = 2 * D_NUC / 3
    area = np.pi * D_NUC**2 / 4
    # impactos por nucleo para DOSIS: nu = D*rho/LET * area (LET en J/m): en unidades de Gy, um y keV
    # D [Gy] = Phi*LET/rho -> Phi*area = D*rho*area/LET ; rho = 1000 kg/m3 ; LET en J/m = keV/um*1.602e-16/1e-6
    let_si = let * 1.602176634e-16 / 1e-6
    nu = DOSIS * 1000.0 * (area * 1e-12) / let_si
    res_total, res_resid, res_miss, res_cinet = [], [], [], []
    t_grid = np.array([0, 2, 6, 24.0])
    for _ in range(n):
        k = rng.poisson(nu)
        nrot = rng.poisson(YIELD * DOSIS)           # numero total de roturas con el rendimiento fijo
        # reparto de roturas en trazas: si hay k impactos, las roturas se reparten entre ellos; k=0 con roturas -> disperso (delta)
        pos = []
        tipo = []
        if k == 0:
            k_eff = 1
        else:
            k_eff = k
        traza = rng.integers(0, k_eff, nrot)
        centro = rng.uniform(-3, 3, (k_eff, 3))
        dirs = rng.normal(size=(k_eff, 3))
        dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
        s = rng.uniform(-cuerda / 2, cuerda / 2, nrot)
        for i in range(nrot):
            pos.append(centro[traza[i]] + dirs[traza[i]] * s[i])
            tipo.append(rng.uniform() < agrupada(let))
        pos = np.array(pos) if nrot else np.zeros((0, 3))
        tipo = np.array(tipo, dtype=bool)
        kk = np.where(tipo, K_LEN, K_RAP)
        t_rep = rng.exponential(1 / kk) if nrot else np.zeros(0)
        res_total.append(nrot)
        res_resid.append(int(np.sum(t_rep > 24.0)))
        res_cinet.append([int(np.sum(t_rep > tt)) for tt in t_grid])
        # errores de reunion: pares a < R_INT; cuenta uno si en el momento en que se repara la primera, la otra sigue sin reparar
        miss = 0
        for a in range(nrot):
            for b in range(a + 1, nrot):
                if np.linalg.norm(pos[a] - pos[b]) < R_INT and min(t_rep[a], t_rep[b]) < 24.0 and max(t_rep[a], t_rep[b]) > min(t_rep[a], t_rep[b]):
                    miss += 1
        res_miss.append(miss)
    return nu, np.mean(res_total), np.mean(res_resid), np.mean(res_miss), np.mean(res_cinet, axis=0)


def analitica(let):
    pa = agrupada(let)
    t = np.array([0, 2, 6, 24.0])
    return YIELD * DOSIS * ((1 - pa) * np.exp(-K_RAP * t) + pa * np.exp(-K_LEN * t))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 116): sin calibracion con datos; solo cualitativamente apoyado en Hagiwara et al. (2019), resumen")
    rng = np.random.default_rng(116)
    print(f"Dosis {DOSIS} Gy, rendimiento inventado {YIELD:.0f} roturas dobles/Gy/nucleo; reparacion rapida {K_RAP}/h, lenta {K_LEN}/h; interaccion {R_INT} um")
    print(f"{'radiacion':10s} {'LET':>6s} {'impactos/nuc':>12s} {'prob.agrup.':>11s} {'roturas':>8s} {'sin reparar 2h':>15s} {'6h':>6s} {'24h':>6s} {'errores reunion':>16s}")
    out = []
    for nombre, let in IONES:
        nu, tot, resid, miss, cin = simula(let, rng, n=1500 if let > 5 else 600)
        ana = analitica(let)
        out.append((nombre, let, tot, resid, miss, cin, ana))
        print(f"{nombre:10s} {let:6.1f} {nu:12.2f} {agrupada(let):11.3f} {tot:8.2f} {cin[1]:15.2f} {cin[2]:6.2f} {resid:6.2f} {miss:16.3f}")
    print("Control analitico de la cinetica (roturas sin reparar a 0, 2, 6, 24 h): simulado frente a analitico")
    for nombre, let, tot, resid, miss, cin, ana in out:
        print(f"  {nombre:10s} sim {np.round(cin,2)}  ana {np.round(ana,2)}")
        assert abs(cin[3] - ana[3]) < 0.03 * ana[0] + 0.3
        assert abs(tot - YIELD * DOSIS) < 0.04 * YIELD * DOSIS
    resid_list = [o[3] for o in out]
    assert all(np.diff(resid_list) > -0.3), "los residuales deben crecer con el LET"
    print(f"Residuales a 24 h: {', '.join(f'{o[0]} {o[3]:.2f}' for o in out)} ; razon hierro / fotones = {resid_list[-1]/resid_list[0]:.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
