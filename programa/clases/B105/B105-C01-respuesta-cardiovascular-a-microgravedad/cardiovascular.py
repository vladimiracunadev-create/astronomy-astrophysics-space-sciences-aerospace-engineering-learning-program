#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C01: presion hidrostatica y tolerancia ortostatica (modelo DIDACTICO, datos SINTETICOS).

Modelo: columna de sangre de densidad rho = 1060 kg/m3; g = 9.81 m/s2 en la Tierra y 0 en caida libre (microgravedad).
Presion media a la altura de la cabeza = presion media en el corazon - rho g h (h = 0.35 m). 1 mmHg = 133.322 Pa.
Ortostasis: gasto GC = FC * VS; VS = VS0 (V_ef / V0)^2 (relacion de llenado simplificada); PAM = GC * RVS.
La reserva barorrefleja eleva FC hasta un maximo y RVS hasta un maximo. Poblacion SINTETICA de 2000 personas, semilla 105.
Todos los parametros son ILUSTRATIVOS; no representan a tripulantes reales. Umbral didactico de PAM en la cabeza: 60 mmHg.
Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

RHO, G, MMHG = 1060.0, 9.81, 133.322
H_CAB, H_PIE = 0.35, 1.30  # m sobre / bajo el corazon
UMBRAL = 60.0  # mmHg en la cabeza (didactico)


def delta_p_mmhg(h, g):
    return RHO * g * h / MMHG


def pam_cabeza(pam_corazon, g=G):
    return pam_corazon - delta_p_mmhg(H_CAB, g)


def simular(n, deficit_plasma, rng):
    """PAM en la cabeza de pie, para n personas, con un deficit de volumen circulante (fraccion)."""
    v0 = rng.normal(5.0, 0.4, n)  # L
    vs0 = rng.normal(0.075, 0.008, n)  # L por latido
    fc0 = rng.normal(70, 6, n)
    rvs0 = rng.normal(18.5, 1.5, n)  # mmHg min/L (PAM = GC*RVS; GC 5 L/min -> 85 mmHg aprox.)
    fc_max_aumento = rng.normal(0.45, 0.10, n)  # fraccion maxima de aumento de FC
    rvs_max_aumento = rng.normal(0.30, 0.08, n)
    pool = rng.normal(0.40, 0.08, n)  # L que se acumulan en las piernas al ponerse de pie
    v_ef = v0 * (1 - deficit_plasma) - pool
    vs = vs0 * np.clip(v_ef / v0, 0.05, None) ** 2  # el llenado de referencia es el del reposo con volumen total v0
    # respuesta barorrefleja proporcional a la caida de VS (saturable)
    caida = 1 - vs / vs0
    fc = fc0 * (1 + np.minimum(fc_max_aumento, 0.8 * caida))
    rvs = rvs0 * (1 + np.minimum(rvs_max_aumento, 0.6 * caida))
    gc = fc * vs  # L/min
    pam = gc * rvs
    return pam_cabeza(pam), pam


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): 2000 personas con parametros ilustrativos; no son datos de tripulantes")
    print(f"Presion hidrostatica rho g h (rho = {RHO:.0f} kg/m3):")
    for nombre, g in (("Tierra (g = 9.81)", G), ("Luna (g = 1.62)", 1.62), ("Marte (g = 3.71)", 3.71), ("Microgravedad (g = 0)", 0.0)):
        print(f"  {nombre:24s} cabeza -{delta_p_mmhg(H_CAB, g):5.1f} mmHg; pies +{delta_p_mmhg(H_PIE, g):5.1f} mmHg")
    rng = np.random.default_rng(105)
    res = {}
    for etiqueta, deficit in (("referencia (sin deficit)", 0.0), ("deficit de volumen 10 %", 0.10), ("deficit de volumen 20 %", 0.20)):
        pc, pm = simular(2000, deficit, rng)
        frac = float(np.mean(pc < UMBRAL))
        res[etiqueta] = frac
        print(f"{etiqueta:26s} PAM corazon {pm.mean():5.1f} +- {pm.std():4.1f} mmHg; PAM cabeza {pc.mean():5.1f} mmHg; fraccion bajo {UMBRAL:.0f} mmHg = {frac:.3f}")
    # comprobaciones
    assert abs(delta_p_mmhg(H_CAB, G) - 27.3) < 0.2
    assert delta_p_mmhg(H_CAB, 0.0) == 0.0
    vals = list(res.values())
    assert vals[0] < vals[1] < vals[2]
    assert vals[0] < 0.25
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
