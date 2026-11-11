#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C05: desplazamiento hipermetropico por acortamiento axial (modelo DIDACTICO, datos SINTETICOS).

Ojo reducido: potencia P = n / L con n = 1.336 (humor vitreo/acuoso, valor de ensenanza) y longitud axial L = 22.3 mm, es decir ~59.9 dioptrias,
ojo emetrope (la imagen cae en la retina). Si la retina se acerca al cristalino en DL (aplanamiento posterior del globo), la imagen de un
objeto lejano cae detras de la retina y el error refractivo es dD = n DL / L^2 (en dioptrias, DL y L en metros, linealizacion).
Presion del liquido cefalorraquideo: columna rho g h con rho = 1007 kg/m3 y h = 0.20 m entre la cabeza y el nivel de medida (ILUSTRATIVO); 1 mmHg = 133.322 Pa.
Fuente consultada (NASA, 'Human body in space', 2026-11-10): el desplazamiento de liquidos hacia la cabeza puede presionar los ojos y causar problemas
de vision (cualitativo; la pagina no usa el termino SANS). Poblacion SINTETICA de 5000 ojos, semilla 105, DL ~ N(0.15 mm, 0.08 mm). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

N, L0 = 1.336, 22.3e-3


def potencia(l):
    return N / l


def delta_d_lineal(dl, l=L0):
    return N * dl / l ** 2


def delta_d_exacto(dl, l=L0):
    # emetrope con potencia fija: retina desplazada dl hacia el cristalino; error = P - n/(l - dl) cambiado de signo (hipermetropia positiva)
    return N / (l - dl) - N / l


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): modelo de ojo reducido; DL ilustrativo; unica fuente consultada, cualitativa (NASA, 2026-11-10)")
    print(f"Potencia del ojo reducido = {potencia(L0):.2f} D; pendiente dD/dL = {delta_d_lineal(1e-3):.3f} D por mm")
    print("Acortamiento axial DL [mm] -> desplazamiento hipermetropico [D] (lineal / exacto):")
    for dl_mm in (0.05, 0.10, 0.20, 0.37, 0.50):
        dl = dl_mm * 1e-3
        print(f"  {dl_mm:4.2f} mm -> {delta_d_lineal(dl):5.3f} / {delta_d_exacto(dl):5.3f} D")
    rng = np.random.default_rng(105)
    dl = rng.normal(0.15e-3, 0.08e-3, 5000).clip(0, None)
    dd = delta_d_exacto(dl)
    print(f"Poblacion sintetica de 5000 ojos: desplazamiento medio {dd.mean():.3f} D (DE {dd.std():.3f}); fraccion >= +0.50 D = {np.mean(dd >= 0.5):.4f}; fraccion >= +1.00 D = {np.mean(dd >= 1.0):.5f}")
    dl_1d = 1.0 * L0 ** 2 / N
    print(f"Acortamiento necesario para +1.00 D = {dl_1d * 1e3:.3f} mm (lineal)")
    for nombre, g in (("Tierra, vertical", 9.81), ("microgravedad", 0.0)):
        p = 1007 * g * 0.20 / 133.322
        print(f"Presion hidrostatica de la columna de LCR a 0.20 m, {nombre:18s} = {p:5.2f} mmHg")
    assert abs(potencia(L0) - 59.91) < 0.05
    assert abs(delta_d_lineal(1e-3) - 2.686) < 0.01
    assert abs(delta_d_exacto(0.1e-3) - delta_d_lineal(0.1e-3)) < 0.01
    assert abs(dl_1d * 1e3 - 0.372) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
