#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C18: deformacion volcanica con una fuente de Mogi: perfil, inversion de profundidad y volumen.

Datos: SINTETICOS. Fuente de Mogi (esfera presurizada en un semiespacio elastico) de profundidad 5 km y cambio de volumen 1e7 m^3 (ILUSTRATIVOS),
razon de Poisson 0.25, ruido de 5 mm por componente, semilla fija 57, 2000 ensayos. La formula de Mogi es conocida y NO se consulto una fuente.
Modelo: u_z = (1 - nu) dV d / (pi (r^2 + d^2)^(3/2)) ; u_r = (1 - nu) dV r / (pi (r^2 + d^2)^(3/2)) ; maximo de u_r en r = d/sqrt(2);
inversion por busqueda en d (1-15 km, paso 25 m) con dV por minimos cuadrados lineales.
Validez: fuente puntual en semiespacio homogeneo. Tolerancia: sin ruido, d recuperada con error < 25 m; maximo de u_r en d/sqrt(2) con 1 %.
Requiere numpy.
"""
import math, platform
import numpy as np

NU = 0.25
D_V, DV = 5e3, 1e7


def campo(r, d, dv):
    k = (1 - NU) * dv / math.pi / (r**2 + d**2) ** 1.5
    return k * d, k * r  # u_z, u_r


def invertir(r, uz, ur):
    mejor = (1e99, None, None)
    for d in np.arange(1e3, 15e3 + 1, 25.0):
        g = np.concatenate([(1 - NU) / math.pi * d / (r**2 + d**2) ** 1.5, (1 - NU) / math.pi * r / (r**2 + d**2) ** 1.5])
        y = np.concatenate([uz, ur])
        dv = float(g @ y / (g @ g))
        c = float(np.sum((y - dv * g) ** 2))
        if c < mejor[0]:
            mejor = (c, d, dv)
    return mejor[1], mejor[2]


def calcular():
    r = {}
    rr = np.arange(0.0, 20e3 + 1, 1e3)
    uz, ur = campo(rr, D_V, DV)
    r["uz0"] = float(uz[0])
    r["ur_max"] = float(ur.max())
    fino = np.arange(0.0, 20e3, 10.0)
    _, urf = campo(fino, D_V, DV)
    r["r_ur_max"] = float(fino[np.argmax(urf)])
    r["r_ur_max_teo"] = D_V / math.sqrt(2)
    r["uz_a_10km"] = float(campo(10e3, D_V, DV)[0])
    d0, dv0 = invertir(rr, uz, ur)
    r["d_rec0"], r["dv_rec0"] = d0, dv0
    rng = np.random.default_rng(57)
    ds, dvs = [], []
    for _ in range(300):
        d, dv = invertir(rr, uz + 0.005 * rng.standard_normal(rr.size), ur + 0.005 * rng.standard_normal(rr.size))
        ds.append(d); dvs.append(dv)
    ds, dvs = np.array(ds), np.array(dvs)
    r["d_media"], r["d_std"] = float(ds.mean()), float(ds.std())
    r["dv_media"], r["dv_std"] = float(dvs.mean()), float(dvs.std())
    r["corr"] = float(np.corrcoef(ds, dvs)[0, 1])
    r["uz0_mm"] = r["uz0"] * 1e3
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Fuente d = 5 km, dV = 1e7 m3: u_z(0) = {r['uz0']*1e3:.1f} mm ; u_z(10 km) = {r['uz_a_10km']*1e3:.2f} mm ; max u_r = {r['ur_max']*1e3:.1f} mm")
    print(f"Maximo de u_r: numerico r = {r['r_ur_max']:.0f} m ; teoria d/sqrt(2) = {r['r_ur_max_teo']:.0f} m")
    print(f"Inversion sin ruido: d = {r['d_rec0']:.0f} m ; dV = {r['dv_rec0']:.4e} m3")
    print(f"Inversion con 5 mm de ruido (300 ensayos): d = {r['d_media']:.0f} +- {r['d_std']:.0f} m ; dV = {r['dv_media']:.3e} +- {r['dv_std']:.2e} m3 ; correlacion d-dV = {r['corr']:.2f}")
    assert abs(r["d_rec0"] - D_V) < 25
    assert abs(r["r_ur_max"] / r["r_ur_max_teo"] - 1) < 0.01
    assert r["corr"] > 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
