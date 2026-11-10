#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C04: reconocimiento de lugares, verificacion geometrica y daño de un cierre de bucle falso (SINTETICO).

Trayectoria: dos vueltas a un cuadrado de 80 m (321 poses; la pose k+160 coincide con la k). Cada pose tiene un descriptor
de lugar de 64 componentes: un vector base unico por lugar mas ruido; tres pares de lugares distintos (30-110, 55-95, 15-75) comparten el 90 % de su
vector (aliasing perceptual). Candidato de cierre = mejor similitud coseno con una pose anterior (separada > 30 poses) que supere
un umbral. Verificacion geometrica: la pose relativa medida debe concordar con la que predice la odometria dentro de
3 sigma (sigma crece con la raiz del numero de pasos). Se compara el ATE del grafo con distintas politicas.
Unidades: m y rad; ruido de odometria sigma_t = 0.02 m, sigma_r = 0.005 rad por paso. Semillas fijas. Datos SINTETICOS.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import (cabecera, comprobar, fin, lazo_cuadrado, odometria_ruidosa, integrar, entre, info_diag, optimizar_grafo,
                       ate_rmse, wrap)

cabecera("Datos SINTETICOS: 2 vueltas a un cuadrado de 80 m, 321 poses, descriptores de 64 componentes, semilla 21")
SIG_T, SIG_R = 0.02, 0.005
V1, rel1 = lazo_cuadrado(40, 0.5)
rel = np.vstack([rel1, rel1])
gt = integrar(rel)
n = len(gt)
VUELTA = len(rel1)                    # 160
rng = np.random.default_rng(21)
z_odo = odometria_ruidosa(rel, rng, SIG_T, SIG_R)
x0 = integrar(z_odo)
Om = info_diag(SIG_T, SIG_R)
aristas_odo = [(i, i + 1, z_odo[i], Om) for i in range(n - 1)]

# descriptores de lugar: un vector base por lugar (indice mod 160), aliasing entre los lugares 30 y 110
D0 = rng.normal(0, 1, (VUELTA, 64))
D0 /= np.linalg.norm(D0, axis=1, keepdims=True)
ALIAS = [(30, 110), (55, 95), (15, 75)]       # pares de lugares distintos con aspecto casi igual
for a_, b_ in ALIAS:
    otro = rng.normal(0, 1, 64)
    otro -= (otro @ D0[a_]) * D0[a_]
    otro /= np.linalg.norm(otro)
    D0[b_] = 0.9 * D0[a_] + np.sqrt(1 - 0.81) * otro
RUIDO = 0.5
desc = np.array([D0[k % VUELTA] + RUIDO * rng.normal(0, 1, 64) / np.sqrt(64) for k in range(n)])
desc /= np.linalg.norm(desc, axis=1, keepdims=True)
S = desc @ desc.T
print(f"Similitud coseno: mismo lugar (mediana) = {np.median([S[k, k + VUELTA] for k in range(VUELTA + 1)]):.2f} ; "
      f"lugares con aliasing 30-110 = {S[30, 110]:.2f} ; lugares distintos (mediana) = {np.median(S[np.triu_indices(n, 60)]):.2f}")


def es_verdadero(i, j):
    return abs(abs(i - j) - VUELTA) <= 2          # misma ubicacion (hasta 2 poses de diferencia)


def candidatos(tau, paso=1):
    c = []
    for i in range(0, n, paso):
        if i - 30 < 1:
            continue
        j = int(np.argmax(S[i, :i - 30]))
        if S[i, j] > tau:
            c.append((i, j))
    return c


# 1) Barrido del umbral: precision y exhaustividad de los candidatos (solo reconocimiento de lugares)
posibles = sum(1 for i in range(0, n, 1) if i - VUELTA >= 0)
print("umbral  candidatos  verdaderos  falsos  precision  exhaustividad")
tab = {}
for tau in (0.4, 0.55, 0.7, 0.85):
    c = candidatos(tau)
    tp = sum(es_verdadero(i, j) for i, j in c)
    fp = len(c) - tp
    pr = tp / len(c) if c else float("nan")
    ex = tp / posibles
    tab[tau] = (len(c), tp, fp, pr, ex)
    print(f"{tau:6.2f}  {len(c):10d}  {tp:10d}  {fp:6d}  {pr:9.0%}  {ex:13.0%}")
comprobar(tab[0.7][4] > 0.9, "con umbral 0.7 deben recuperarse casi todos los cierres verdaderos")
comprobar(tab[0.4][2] > tab[0.7][2], "un umbral bajo debe dejar pasar mas falsos")
comprobar(tab[0.85][1] <= tab[0.7][1], "un umbral alto no puede aceptar mas verdaderos")


def arista_bucle(i, j, rng_local):
    """Pose relativa medida por un emparejador de escaneos. Verdadero: la pose real con ruido. Falso (alias): el
    emparejador fuerza un ajuste y devuelve una pose casi coincidente, ya que el descriptor dijo que era el mismo lugar."""
    if es_verdadero(i, j):
        z = entre(gt[i], gt[j])
    else:
        z = np.array([0.0, 0.0, 0.0])
    z = z + np.array([rng_local.normal(0, 0.02), rng_local.normal(0, 0.02), rng_local.normal(0, 0.005)])
    return (i, j, z, info_diag(0.02, 0.005))


def compuerta(i, j, z):
    """Acepta si la pose relativa medida (j visto desde i) difiere de la predicha por la odometria menos de 3 sigma."""
    k = abs(i - j)
    pred = entre(x0[i], x0[j])
    d_xy = float(np.linalg.norm(z[:2] - pred[:2]))
    d_th = abs(float(wrap(z[2] - pred[2])))
    sig_pos = np.sqrt(k) * SIG_T + np.sqrt(k) * SIG_R * 0.25 * 0.5 * k
    sig_th = np.sqrt(k) * SIG_R
    return d_xy < 3 * sig_pos and d_th < 3 * sig_th


def evaluar(politica, tau=0.4, huber=None):
    rl = np.random.default_rng(77)
    aristas = list(aristas_odo)
    aceptados = rechazados_fp = 0
    for i, j in candidatos(tau):
        a = arista_bucle(j, i, rl) if j < i else arista_bucle(i, j, rl)
        a_i, a_j, z, Om_l = a
        if politica == "oraculo" and not es_verdadero(i, j):
            continue
        if politica == "compuerta" and not compuerta(a_i, a_j, z):
            rechazados_fp += 0 if es_verdadero(i, j) else 1
            continue
        aristas.append(a)
        aceptados += 1
    xo, h = optimizar_grafo(x0, aristas, iteraciones=15, huber=huber)
    return ate_rmse(xo[:, :2], gt[:, :2])[0], aceptados, rechazados_fp, h[-1]


ate_odo = ate_rmse(x0[:, :2], gt[:, :2])[0]
print(f"\nPoliticas con umbral de reconocimiento 0.4 (permisivo); ATE de la odometria sola = {ate_odo:.3f} m")
print("politica               aristas_de_bucle  falsos_rechazados  chi2_final       ATE [m]")
res = {}
for nombre, pol, hub in [("solo odometria", "ninguno", None), ("oraculo (solo verdaderos)", "oraculo", None),
                         ("todos los candidatos", "todos", None), ("compuerta geometrica", "compuerta", None)]:
    if pol == "ninguno":
        ate, ac, rf, chi = ate_odo, 0, 0, 0.0
    else:
        ate, ac, rf, chi = evaluar(pol, 0.4, hub)
    res[pol] = ate
    print(f"{nombre:24s} {ac:14d}  {rf:17d}  {chi:11.1f}  {ate:12.3f}")
comprobar(res["oraculo"] < ate_odo, "los cierres verdaderos deben reducir el ATE")
comprobar(res["todos"] > res["oraculo"], "los cierres falsos deben empeorar el mapa")
comprobar(res["compuerta"] < res["todos"], "la compuerta debe proteger el mapa de los cierres falsos")
comprobar(res["compuerta"] < 1.5 * res["oraculo"] + 0.05, "con la compuerta el ATE debe quedar cerca del oraculo")
fin()
