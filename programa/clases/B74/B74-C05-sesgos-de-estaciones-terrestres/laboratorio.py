#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C05: efecto de errores de posicion de estacion y de sesgos de alcance en un ajuste.

Todo SINTETICO (no observado): seis estaciones repartidas en una esfera de 6 378 137 m (valor ilustrativo), una nave a 20 000 km
de altitud sobre el cenit de la primera. Se miden alcances; el ajuste es Gauss-Newton por minimos cuadrados de la posicion de la nave
(3 incognitas), con una variante que estima ademas un sesgo comun. Monte Carlo de 1000 realizaciones, semilla 13.
Niveles ILUSTRATIVOS: ruido 1 m; error de posicion de estacion 5 m por eje; sesgo de alcance por estacion 3 m (1 sigma).
Tolerancia: sin errores sistematicos el rms 3D debe coincidir con la prediccion lineal sqrt(traza((H^T H)^-1)) sigma dentro del 8 %.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, platform, sys
import numpy as np

RE = 6378137.0


def estaciones():
    ll = [(0, 0), (40, 60), (-35, 120), (10, -100), (-60, -30), (65, 170)]
    s = []
    for la, lo in ll:
        la, lo = np.radians(la), np.radians(lo)
        s.append(RE * np.array([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)]))
    return np.array(s)


def ajusta(est_asum, y, x0, estima_sesgo=False, it=6):
    x = x0.copy(); b = 0.0
    for _ in range(it):
        d = x - est_asum
        r = np.linalg.norm(d, axis=1)
        H = d / r[:, None]
        if estima_sesgo:
            H = np.hstack([H, np.ones((len(r), 1))])
            p = np.concatenate([x, [b]])
        else:
            p = x
        res = y - (r + (b if estima_sesgo else 0.0))
        dp = np.linalg.lstsq(H, res, rcond=None)[0]
        x = x + dp[:3]
        if estima_sesgo:
            b += dp[3]
    return x


def main():
    rng = np.random.default_rng(13)
    S = estaciones()
    x_true = S[0] / RE * (RE + 20e6)
    sn, sp, sb = 1.0, 5.0, 3.0
    d = x_true - S
    r0 = np.linalg.norm(d, axis=1)
    H = d / r0[:, None]
    pred = np.sqrt(np.trace(np.linalg.inv(H.T @ H))) * sn
    casos = {"a) solo ruido": (0, 0, False), "b) + posicion de estacion": (sp, 0, False),
             "c) + sesgo por estacion": (0, sb, False), "d) sesgo comun de 10 m sin estimarlo": (0, "comun", False),
             "f) sesgo comun de 10 m, estimado": (0, "comun", True),
             "e) sesgo por estacion, estimando uno comun": (0, sb, True)}
    Ha = np.hstack([H, np.ones((len(r0), 1))])
    pred_a = np.sqrt(np.trace(np.linalg.inv(Ha.T @ Ha)[:3, :3])) * sn
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (geometria y errores SINTETICOS, semilla 13)",
           f"Prediccion lineal del rms 3D con ruido {sn} m: {pred:.3f} m"]
    res = {"pred": float(pred), "pred_a": float(pred_a)}
    out.append(f"Prediccion lineal con un sesgo comun estimado: {pred_a:.3f} m")
    out.append("caso                                           rms 3D [m]")
    ok = True
    for k, (spos, sbias, est) in casos.items():
        e = []
        for _ in range(1000):
            S_err = S + rng.normal(0, spos, S.shape) if spos else S
            if sbias == "comun":
                bias = np.full(len(S), 10.0)
            else:
                bias = rng.normal(0, sbias, len(S)) if sbias else np.zeros(len(S))
            y = np.linalg.norm(x_true - S_err, axis=1) + bias + rng.normal(0, sn, len(S))
            x = ajusta(S, y, x_true + np.array([1e3, -1e3, 1e3]), estima_sesgo=est)
            e.append(np.linalg.norm(x - x_true))
        rms = float(np.sqrt(np.mean(np.square(e))))
        out.append(f"{k:46s} {rms:9.3f}")
        res["c" + k[0]] = rms
    ok = abs(res["ca"] / pred - 1) < 0.08
    out.append(f"Cociente rms/prediccion en el caso a) = {res['ca']/pred:.3f}")
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res["cociente"] = res["ca"] / pred
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
