#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C19: metricas de precision de navegacion (RMS, percentiles, CEP, SEP) y su incertidumbre muestral.

Todo SINTETICO: errores de posicion gaussianos de media cero con sigma = (3.0, 1.2, 2.0) m en (x, y, z) (ILUSTRATIVOS), muestra de verdad de 2 000 000 puntos
(semilla 67) para valores 'exactos' de referencia, y 400 conjuntos de 50 muestras para medir cuanto varian las estimaciones. Metricas: RMS 3D = sqrt(sum sigma^2);
percentil 95 de la norma 3D; CEP (radio del circulo horizontal con 50 % de probabilidad) y su aproximacion 0.589 (sigma_x + sigma_y) (valida cuando sigma_min/sigma_max > 0.3,
relacion estandar NO consultada); 2DRMS = 2 sqrt(sigma_x^2 + sigma_y^2) (aprox. 95-98 %); SEP (radio esferico con 50 %). Intervalo de confianza del percentil 95 con N = 50 por
bootstrap (1000 remuestreos) para un conjunto.
Tolerancias: RMS 3D muestral con 2e6 puntos dentro del 0.1 % del teorico; la aproximacion 0.589(sx+sy) dentro del 3 % del CEP de la muestra grande.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np


def main():
    rng = np.random.default_rng(67)
    s = np.array([3.0, 1.2, 2.0])
    X = rng.normal(0, s, (2_000_000, 3))
    n3 = np.linalg.norm(X, axis=1); n2 = np.linalg.norm(X[:, :2], axis=1)
    rms_t = math.sqrt((s**2).sum()); rms_m = math.sqrt(np.mean(n3**2))
    p95 = float(np.percentile(n3, 95)); cep = float(np.percentile(n2, 50)); sep = float(np.percentile(n3, 50))
    cep_ap = 0.589 * (s[0] + s[1]); d2 = 2 * math.sqrt(s[0]**2 + s[1]**2)
    frac2d = float(np.mean(n2 < d2))
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (errores SINTETICOS, semilla 67)",
           f"sigma (x, y, z) = {s[0]}, {s[1]}, {s[2]} m ; muestra de referencia: {len(X):_} puntos".replace("_", " ")]
    out.append(f"RMS 3D teorico = {rms_t:.4f} m ; muestral = {rms_m:.4f} m (dif. relativa {abs(rms_m/rms_t-1):.2e})")
    out.append(f"Percentil 95 de la norma 3D = {p95:.3f} m ; SEP (50 %) = {sep:.3f} m")
    out.append(f"CEP (50 % horizontal) = {cep:.3f} m ; aproximacion 0.589(sx+sy) = {cep_ap:.3f} m (dif. {abs(cep_ap/cep-1)*100:.2f} %)")
    out.append(f"2DRMS = {d2:.3f} m contiene el {frac2d*100:.2f} % de los puntos horizontales")
    res = dict(rms_t=rms_t, rms_m=rms_m, p95=p95, sep=sep, cep=cep, cep_ap=cep_ap, d2=d2, frac2d=frac2d, dif_cep=abs(cep_ap / cep - 1) * 100)
    # variabilidad con N = 50
    est95 = []; estc = []; estr = []
    for _ in range(400):
        Y = rng.normal(0, s, (50, 3))
        n = np.linalg.norm(Y, axis=1)
        est95.append(np.percentile(n, 95)); estc.append(np.percentile(np.linalg.norm(Y[:, :2], axis=1), 50)); estr.append(math.sqrt(np.mean(n**2)))
    est95, estc, estr = map(np.array, (est95, estc, estr))
    out.append(f"Con N = 50 (400 conjuntos): RMS 3D = {estr.mean():.3f} +/- {estr.std(ddof=1):.3f} m ; P95 = {est95.mean():.3f} +/- {est95.std(ddof=1):.3f} m ; CEP = {estc.mean():.3f} +/- {estc.std(ddof=1):.3f} m")
    res.update(r50=float(estr.mean()), r50s=float(estr.std(ddof=1)), p50m=float(est95.mean()), p50s=float(est95.std(ddof=1)), c50=float(estc.mean()), c50s=float(estc.std(ddof=1)))
    # bootstrap para un conjunto
    Y = rng.normal(0, s, (50, 3)); n = np.linalg.norm(Y, axis=1)
    bs = [np.percentile(rng.choice(n, 50, replace=True), 95) for _ in range(1000)]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    out.append(f"Un conjunto de N = 50: P95 = {np.percentile(n,95):.3f} m ; intervalo bootstrap 95 % = [{lo:.3f}, {hi:.3f}] m ; valor de referencia {p95:.3f} m {'dentro' if lo <= p95 <= hi else 'fuera'} del intervalo")
    res.update(b95=float(np.percentile(n, 95)), lo=float(lo), hi=float(hi), dentro=int(lo <= p95 <= hi))
    ok = abs(rms_m / rms_t - 1) < 1e-3 and abs(cep_ap / cep - 1) < 0.03
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
