#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C03: sensor solar de seis fotodiodos (ley del coseno) y vector solar por minimos cuadrados.
Modelo SINTETICO: corriente I_i = I0 max(0, n_i . s) + ruido gaussiano; I0 = 1 (unidades arbitrarias, normalizadas).
Sin albedo; sin eclipse. Semilla 20260512."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

N = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)


def estimar(s, sigma, rng, fov_deg=80.0):
    cosfov = math.cos(fov_deg * D2R)
    c = N @ s
    I = np.where(c > cosfov, c, 0.0) + sigma * rng.standard_normal(6)
    usar = np.where(c > cosfov)[0]
    if len(usar) < 3:
        return None
    sh = np.linalg.lstsq(N[usar], I[usar], rcond=None)[0]
    return unit(sh)


def error_rms(sigma, n=3000, seed=20260512):
    rng = np.random.default_rng(seed)
    errs = []
    for _ in range(n):
        s = unit(rng.standard_normal(3))
        e = estimar(s, sigma, rng)
        if e is not None:
            errs.append(math.acos(max(-1, min(1, e @ s))))
    return math.sqrt(np.mean(np.square(errs))) * R2D, len(errs) / n


def calcular():
    out = {}
    out['curva'] = [(sg, *error_rms(sg)) for sg in (0.001, 0.003, 0.01, 0.03, 0.1)]
    # caso conductor sin ruido
    rng = np.random.default_rng(1)
    s = unit([0.6, 0.5, 0.62])
    e = estimar(s, 0.0, rng)
    out['s'] = s; out['e0'] = math.acos(min(1, e @ s)) * R2D
    # una sola celda a 80 grados: sensibilidad angular d(cos)/dtheta
    th = 80 * D2R
    out['sens_80'] = math.sin(th)
    out['sens_5'] = math.sin(5 * D2R)
    out['pendiente_lineal'] = 0.01 / math.sin(th) * R2D  # deg por 0.01 de ruido de corriente a 80 grados
    return out


def main():
    banner("B87-C03 sensor solar de 6 fotodiodos | datos SINTETICOS (semilla 20260512), ruido en unidades de I0")
    d = calcular()
    print(f"Sol de ejemplo s = [{d['s'][0]:.4f} {d['s'][1]:.4f} {d['s'][2]:.4f}] ; error sin ruido = {d['e0']:.2e} deg")
    print("sigma_I   error rms [deg]   fraccion con >= 3 celdas iluminadas")
    for sg, e, f in d['curva']:
        print(f"{sg:7.3f}   {e:14.4f}   {f:8.3f}")
    print(f"sensibilidad d(cos)/d(theta) = sin(theta): a 80 deg = {d['sens_80']:.4f} ; a 5 deg = {d['sens_5']:.4f}")
    print(f"error angular de una celda a 80 deg por 0.01 de ruido: {d['pendiente_lineal']:.3f} deg")
    assert d['e0'] < 1e-6
    ers = [e for _, e, _ in d['curva']]
    assert all(a < b for a, b in zip(ers, ers[1:]))
    assert abs(ers[-1] / ers[0] - 100) / 100 < 0.25
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
