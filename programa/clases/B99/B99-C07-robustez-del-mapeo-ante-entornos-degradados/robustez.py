#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C07: robustez de la estimacion de movimiento y del emparejamiento ante entornos degradados (SINTETICO).

(a) Registro rigido 2D con una fraccion de correspondencias atipicas (polvo, falsos emparejamientos): minimos cuadrados (LS),
    Huber por minimos cuadrados reponderados (IRLS, delta = 0.05 m) y RANSAC (60 hipotesis, umbral 0.08 m).
(b) Degeneracion: informacion de un ajuste punto-a-linea en un pasillo recto (todas las normales paralelas) frente a una
    esquina en L; el autovalor minimo de J^T J mide si el movimiento esta determinado.
(c) Cambio de iluminacion (ganancia y sesgo) y texturas pobres: tasa de acierto del emparejamiento de parches con SSD y con
    correlacion cruzada normalizada de media cero (ZNCC).
Unidades: m, rad; parches en niveles 0-255 (ruido de parche 4 niveles). Semillas fijas. Todos los datos son SINTETICOS.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import cabecera, comprobar, fin, kabsch2d, rot

cabecera("Datos SINTETICOS: 60 puntos en 10 x 10 m, transformacion verdadera (0.10 rad, 0.5 m, -0.3 m), ruido 0.02 m")
TH, TT = 0.10, np.array([0.5, -0.3])
SIG = 0.02


def caso(rng, frac):
    P = rng.uniform(0, 10, (60, 2))
    Q = (rot(TH) @ P.T).T + TT + rng.normal(0, SIG, P.shape)
    m = int(round(frac * len(P)))
    if m:
        k = rng.choice(len(P), m, replace=False)
        Q[k] = rng.uniform(0, 10, (m, 2))
    return P, Q


def est_ls(P, Q, rng):
    return kabsch2d(P, Q)[1:]


def est_huber(P, Q, rng, delta=0.05, it=30):
    w = np.ones(len(P))
    for _ in range(it):
        _, R, t = kabsch2d(P, Q, w)
        r = np.linalg.norm((R @ P.T).T + t - Q, axis=1)
        w = np.where(r <= delta, 1.0, delta / np.maximum(r, 1e-12))
    return R, t


def est_ransac(P, Q, rng, it=60, umbral=0.08):
    mejor = None
    for _ in range(it):
        idx = rng.choice(len(P), 2, replace=False)
        _, R, t = kabsch2d(P[idx], Q[idx])
        inl = np.linalg.norm((R @ P.T).T + t - Q, axis=1) < umbral
        if mejor is None or inl.sum() > mejor.sum():
            mejor = inl
    _, R, t = kabsch2d(P[mejor], Q[mejor])
    return R, t


def error(R, t):
    th = math.atan2(R[1, 0], R[0, 0])
    return float(np.hypot(*(t - TT))), abs(th - TH)


# (a) estimadores frente a la fraccion de atipicos (media de 30 casos)
print("atipicos  estimador   error de traslacion [m]   error de giro [rad]")
tab = {}
for frac in (0.0, 0.1, 0.3, 0.5):
    for nombre, f in (("LS", est_ls), ("Huber", est_huber), ("RANSAC", est_ransac)):
        e = np.array([error(*f(*caso(np.random.default_rng(700 + s), frac), np.random.default_rng(s))) for s in range(30)])
        tab[(frac, nombre)] = e.mean(axis=0)
        print(f"{frac:8.0%}  {nombre:9s}  {e[:, 0].mean():23.4f}   {e[:, 1].mean():19.4f}")
comprobar(all(tab[(0.0, n)][0] < 0.02 for n in ("LS", "Huber", "RANSAC")), "sin atipicos los tres estimadores deben coincidir con la verdad a 2 cm")
comprobar(tab[(0.3, "LS")][0] > 5 * tab[(0.3, "RANSAC")][0], "con 30 % de atipicos LS debe ser mucho peor que RANSAC")
comprobar(tab[(0.3, "Huber")][0] < tab[(0.3, "LS")][0], "Huber debe mejorar a LS con 30 % de atipicos")
comprobar(tab[(0.5, "LS")][0] > tab[(0.1, "LS")][0], "el error de LS debe crecer con los atipicos")
comprobar(tab[(0.5, "RANSAC")][0] < 0.5, "RANSAC debe aguantar 50 % de atipicos en este caso")

# (b) degeneracion: autovalores de J^T J para restricciones punto-a-linea
print()


def info_pl(puntos, normales):
    J = np.array([[n[0], n[1], n[0] * (-p[1]) + n[1] * p[0]] for p, n in zip(puntos, normales)])
    return J.T @ J


x = np.linspace(0, 20, 80)
pasillo_p = np.vstack([np.column_stack([x, np.full_like(x, 1.5)]), np.column_stack([x, np.full_like(x, -1.5)])])
pasillo_n = np.array([[0.0, -1.0]] * 80 + [[0.0, 1.0]] * 80)
y = np.linspace(0, 6, 40)
esq_p = np.vstack([np.column_stack([x[:40] * 0.3, np.zeros(40)]), np.column_stack([np.zeros(40), y])])
esq_n = np.array([[0.0, 1.0]] * 40 + [[1.0, 0.0]] * 40)
for nombre, (p, nrm) in (("pasillo recto (2 paredes)", (pasillo_p, pasillo_n)), ("esquina en L", (esq_p, esq_n))):
    Hh = info_pl(p, nrm)
    w, V = np.linalg.eigh(Hh)
    print(f"{nombre:26s} autovalores de J^T J = {w[0]:.3e}, {w[1]:.3e}, {w[2]:.3e} ; direccion debil = ({V[0, 0]:+.2f}, {V[1, 0]:+.2f}, {V[2, 0]:+.2f}) en (dx, dy, dtheta)")
w_pas = np.linalg.eigvalsh(info_pl(pasillo_p, pasillo_n))
w_esq = np.linalg.eigvalsh(info_pl(esq_p, esq_n))
comprobar(w_pas[0] < 1e-9 * w_pas[-1], "el pasillo recto debe tener un autovalor casi nulo")
comprobar(w_esq[0] > 1e-3 * w_esq[-1], "la esquina en L debe tener informacion en todas las direcciones")
Vp = np.linalg.eigh(info_pl(pasillo_p, pasillo_n))[1][:, 0]
comprobar(abs(abs(Vp[0]) - 1.0) < 1e-6, "la direccion indeterminada del pasillo debe ser la traslacion a lo largo del eje x")
print(f"Razon de condicion: pasillo = infinita (autovalor minimo nulo) ; esquina = {w_esq[-1] / w_esq[0]:.1f}")

# (c) iluminacion y texturas pobres: SSD frente a ZNCC
print("\ncontraste  ganancia  sesgo  acierto SSD  acierto ZNCC")
rng = np.random.default_rng(88)


def parches(n, contraste, rng_local):
    base = rng_local.normal(0, 1, (n, 13, 13))
    # suavizado simple para que parezcan texturas y no ruido blanco
    s = (base + np.roll(base, 1, 1) + np.roll(base, 1, 2) + np.roll(np.roll(base, 1, 1), 1, 2)) / 2
    s = s[:, 1:12, 1:12]
    s = s / s.std(axis=(1, 2), keepdims=True)
    return 120 + contraste * s


def acierto(contraste, gan, sesgo, metodo, semilla):
    r = np.random.default_rng(semilla)
    A = parches(100, contraste, r)
    B = np.clip(gan * A + sesgo + r.normal(0, 4.0, A.shape), 0, 255)
    a, b = A.reshape(100, -1), B.reshape(100, -1)
    if metodo == "ssd":
        d = ((a[:, None, :] - b[None, :, :]) ** 2).sum(axis=2)
    else:
        az = a - a.mean(axis=1, keepdims=True)
        bz = b - b.mean(axis=1, keepdims=True)
        az /= np.linalg.norm(az, axis=1, keepdims=True)
        bz /= np.linalg.norm(bz, axis=1, keepdims=True)
        d = -(az @ bz.T)
    return float(np.mean(np.argmin(d, axis=1) == np.arange(100)))


res = {}
for c, g, s in ((40, 1.0, 0.0), (40, 1.5, 25.0), (10, 1.5, 25.0), (2, 1.5, 25.0), (1, 1.0, 0.0), (1, 1.5, 25.0)):
    a1 = np.mean([acierto(c, g, s, "ssd", k) for k in range(10)])
    a2 = np.mean([acierto(c, g, s, "zncc", k) for k in range(10)])
    res[(c, g, s)] = (a1, a2)
    print(f"{c:9d}  {g:8.1f}  {s:5.0f}  {a1:11.0%}  {a2:12.0%}")
comprobar(res[(40, 1.0, 0.0)][0] > 0.95 and res[(40, 1.0, 0.0)][1] > 0.95, "con buen contraste y sin cambio de luz ambos aciertan")
comprobar(res[(40, 1.5, 25.0)][1] > res[(40, 1.5, 25.0)][0], "ZNCC debe superar a SSD con cambio de ganancia y sesgo")
comprobar(res[(1, 1.5, 25.0)][1] < res[(40, 1.5, 25.0)][1], "con textura pobre el acierto de ZNCC debe bajar")
fin()
