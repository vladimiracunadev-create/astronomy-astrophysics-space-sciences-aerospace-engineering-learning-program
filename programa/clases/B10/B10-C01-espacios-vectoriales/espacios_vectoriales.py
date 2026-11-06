#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C01: espacios vectoriales y subespacios con estados orbitales.

Datos: GM de la Tierra = 3.986005e14 m3/s2 (IERS, TN36, tabla 1.2, valor
GRS80). Estados orbitales: SINTETICOS (orbita circular de radio 7000 km).
Modelo: R^n con suma y producto por escalar; un subconjunto es subespacio si
contiene al 0 y es cerrado bajo suma y producto por escalar.
Supuestos: comprobacion por muestreo aleatorio (no es una demostracion).
Validez: solo detecta fallos; pasar el muestreo no demuestra la propiedad.
Tolerancia: 1e-9 en las igualdades; semilla fija.
"""
from __future__ import annotations
import platform
import numpy as np

GM = 3.986005e5          # km^3/s^2
TOL = 1e-9
rng = np.random.default_rng(10)


def axiomas(n=6, muestras=200):
    """Comprueba 8 axiomas de espacio vectorial para R^n con muestras al azar."""
    ok = True
    for _ in range(muestras):
        u, v, w = rng.normal(size=(3, n))
        a, b = rng.normal(size=2)
        ok &= np.allclose(u + v, v + u, atol=TOL)
        ok &= np.allclose((u + v) + w, u + (v + w), atol=TOL)
        ok &= np.allclose(u + np.zeros(n), u, atol=TOL)
        ok &= np.allclose(u + (-u), 0, atol=TOL)
        ok &= np.allclose(a * (u + v), a * u + a * v, atol=TOL)
        ok &= np.allclose((a + b) * u, a * u + b * u, atol=TOL)
        ok &= np.allclose((a * b) * u, a * (b * u), atol=TOL)
        ok &= np.allclose(1.0 * u, u, atol=TOL)
    return bool(ok)


def es_subespacio(pertenece, generador, n=3, muestras=300):
    """Prueba 0 en W y cierre bajo suma y producto con muestras de W."""
    if not pertenece(np.zeros(n)):
        return False, "no contiene al 0"
    for _ in range(muestras):
        u, v = generador(), generador()
        a = rng.normal()
        if not pertenece(u + v):
            return False, "no es cerrado bajo la suma"
        if not pertenece(a * u):
            return False, "no es cerrado bajo el producto por escalar"
    return True, "pasa el muestreo"


def estado_circular(theta, r=7000.0):
    """Estado (r, v) de una orbita circular en el plano xy, en km y km/s."""
    v = np.sqrt(GM / r)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([r * c, r * s, 0.0, -v * s, v * c, 0.0])


def es_circular(x, tol=1e-6):
    """Orbita circular: r.v = 0 y |r||v|^2 = GM."""
    r, v = x[:3], x[3:]
    return (abs(r @ v) < tol * np.linalg.norm(r) * np.linalg.norm(v)
            and abs(np.linalg.norm(r) * (v @ v) / GM - 1.0) < tol)


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    assert axiomas(), "fallan los axiomas en R^6"
    print("R^6: 8 axiomas superados en 200 muestras")

    s0, s1 = estado_circular(0.0), estado_circular(np.pi / 2)
    assert es_circular(s0) and es_circular(s1)
    h = np.cross(s0[:3], s0[3:])
    print("h = r x v =", h.round(3), "km2/s")

    def gen_plano():
        a, b = rng.normal(size=2)
        return np.array([a, b, 0.0])

    ok, msg = es_subespacio(lambda x: abs(x[2]) < TOL, gen_plano)
    print("plano z=0            :", ok, "-", msg)
    assert ok
    ok2, msg2 = es_subespacio(
        lambda x: abs(x @ h) < 1e-6 * np.linalg.norm(h) * max(1, np.linalg.norm(x)),
        lambda: (lambda a, b: a * s0[:3] + b * s1[:3])(*rng.normal(size=2)))
    print("plano orbital (x.h=0):", ok2, "-", msg2)
    assert ok2
    ok3, msg3 = es_subespacio(lambda x: abs(x[2] - 1) < TOL,
                              lambda: np.array([*rng.normal(size=2), 1.0]))
    print("plano z=1            :", ok3, "-", msg3)
    assert not ok3
    ok4, msg4 = es_subespacio(
        lambda x: abs(np.linalg.norm(x) - 1) < TOL,
        lambda: (lambda g: g / np.linalg.norm(g))(rng.normal(size=3)))
    print("esfera unidad        :", ok4, "-", msg4)
    assert not ok4

    suma = s0 + s1
    razon = np.linalg.norm(suma[:3]) * (suma[3:] @ suma[3:]) / GM
    print("s0+s1 es orbita circular?", es_circular(suma), "| |r||v|^2/GM =", round(razon, 4))
    assert not es_circular(suma)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
