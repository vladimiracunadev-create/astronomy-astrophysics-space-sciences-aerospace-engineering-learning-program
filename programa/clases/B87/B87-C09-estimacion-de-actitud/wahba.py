#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C09: estimacion de actitud con dos vectores (Sol y campo magnetico): TRIAD, SVD (Wahba) y metodo q de Davenport.
Datos SINTETICOS (semilla 20260519): actitud aleatoria; vectores de referencia de EJEMPLO fijos en el sistema inercial;
ruido angular del Sol 0.5 deg y del magnetometro 1.0 deg por eje transversal. Pesos 1/sigma^2."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

SS, SM = 0.5 * D2R, 1.0 * D2R


def par_referencia(sep_deg):
    r1 = unit([0.6, 0.5, 0.62])
    e = unit(np.cross(r1, [0, 0, 1.0]))
    r2 = math.cos(sep_deg * D2R) * r1 + math.sin(sep_deg * D2R) * np.cross(e, r1) / np.linalg.norm(np.cross(e, r1)) * 1.0
    return r1, unit(r2)


def corrida(sep_deg, n, rng):
    r1, r2 = par_referencia(sep_deg)
    w = np.array([1 / SS ** 2, 1 / SM ** 2])
    es = {k: [] for k in ("triad_sol", "triad_mag", "svd", "q", "dsq", "loss")}
    for _ in range(n):
        qt = random_q(rng); At = A_of_q(qt)
        b1 = noisy_unit(At @ r1, SS, rng); b2 = noisy_unit(At @ r2, SM, rng)
        As = wahba_svd([b1, b2], [r1, r2], w)
        qs = q_of_A(As)
        qq = q_method([b1, b2], [r1, r2], w)
        es["triad_sol"].append(ang_between(q_of_A(triad(b1, b2, r1, r2)), qt))
        es["triad_mag"].append(ang_between(q_of_A(triad(b2, b1, r2, r1)), qt))
        es["svd"].append(ang_between(qs, qt))
        es["q"].append(ang_between(qq, qt))
        es["dsq"].append(ang_between(qs, qq))
        es["loss"].append(wahba_loss(As, [b1, b2], [r1, r2], w))
    return {k: (math.sqrt(np.mean(np.square(v))) if k != "dsq" else float(np.max(v))) * (R2D if k not in ("loss",) else 1) for k, v in es.items() if k != "loss"} | {"loss": float(np.mean(es["loss"]))}


def calcular():
    rng = np.random.default_rng(20260519)
    base = corrida(70.0, 3000, rng)
    seps = []
    for sep in (20.0, 45.0, 70.0, 90.0):
        r = corrida(sep, 1500, rng)
        seps.append((sep, r["svd"], r["triad_sol"]))
    return dict(base=base, seps=seps, ss=SS * R2D, sm=SM * R2D)


def main():
    banner("B87-C09 estimacion de actitud con dos vectores | SINTETICO (semilla 20260519): Sol 0.5 deg, campo 1.0 deg, separacion 70 deg")
    d = calcular(); b = d['base']
    print(f"error rms de actitud (3000 casos, separacion de 70 deg):")
    print(f"  TRIAD (Sol primario)   = {b['triad_sol']:.4f} deg")
    print(f"  TRIAD (campo primario) = {b['triad_mag']:.4f} deg")
    print(f"  SVD ponderado (Wahba)  = {b['svd']:.4f} deg")
    print(f"  metodo q ponderado     = {b['q']:.4f} deg")
    print(f"  diferencia maxima SVD - q = {b['dsq']:.2e} deg")
    print(f"  perdida de Wahba media (con pesos 1/sigma^2) = {b['loss']:.3f}")
    print("separacion [deg]  error SVD [deg]  error TRIAD (Sol) [deg]")
    for sep, e, et in d['seps']:
        print(f"{sep:16.0f}  {e:14.4f}  {et:22.4f}")
    assert b['dsq'] < 1e-6 and b['svd'] < b['triad_mag'] and b['svd'] <= b['triad_sol'] * 1.001
    assert d['seps'][0][1] > d['seps'][2][1] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
