#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C04: mapa de traversabilidad a partir de un modelo digital de elevacion (MDE) SINTETICO con ruido de estereo.

Todo es sintetico (semilla 103): terreno suave de baja frecuencia + 40 rocas hemisfericas, celda de 0.10 m, 200 x 200 celdas
(20 m x 20 m), sensor en el borde y = 0 mirando hacia +y (rango = distancia al borde). Unidades: m y grados. Sistema: x, y en el plano,
z hacia arriba.
Ruido del MDE ILUSTRATIVO: sigma_h(r) = 0.0005 r^2 m (r = rango en m); crece con el cuadrado del rango como en B103-C03, pero
la constante NO viene de una medicion.
Vehiculo ILUSTRATIVO: huella de 1.0 m x 1.0 m (10 x 10 celdas). Umbrales ILUSTRATIVOS: pendiente > 20 grados, escalon (max-min
en la huella) > 0.25 m, rugosidad (desv. tipica del residuo al plano ajustado) > 0.06 m -> celda NO transitable.
Variante con correccion de sesgo: se resta el aporte esperado del ruido a la rugosidad y al escalon.
Metodo: ajuste de plano por minimos cuadrados en cada ventana (formulas cerradas en rejilla regular) y escalon por max-min.
Verificacion: la verdad se calcula con el MDE sin ruido; se mide la matriz de confusion con el MDE ruidoso, sin y con
correccion de sesgo. Tolerancias: sin ruido la confusion es perfecta (0 errores); la correccion reduce las falsas alarmas y
no puede reducir los falsos "seguro" (compromiso). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

N, CELDA, V = 200, 0.10, 10
PEND_MAX, ESC_MAX, RUG_MAX = 20.0, 0.25, 0.06


def terreno(rng):
    ruido = rng.normal(0, 1, (N, N))
    f = np.fft.fft2(ruido)
    kx, ky = np.fft.fftfreq(N)[:, None], np.fft.fftfreq(N)[None, :]
    f *= np.exp(-(kx ** 2 + ky ** 2) / (2 * 0.012 ** 2))
    z = np.real(np.fft.ifft2(f))
    z = (z - z.mean()) / z.std() * 0.4
    yy, xx = np.mgrid[0:N, 0:N] * CELDA
    for _ in range(40):
        cx, cy, r = rng.uniform(0.5, 19.5), rng.uniform(0.5, 19.5), rng.uniform(0.08, 0.35)
        d2 = (xx - cx) ** 2 + (yy - cy) ** 2
        z += np.where(d2 < r * r, np.sqrt(np.maximum(r * r - d2, 0)), 0.0)
    return z


def metricas(z):
    """Pendiente [grados], escalon [m] y rugosidad [m] en ventanas V x V (indexadas por su esquina)."""
    w = sliding_window_view(z, (V, V))
    c = (np.arange(V) - (V - 1) / 2) * CELDA
    sxx = V * np.sum(c ** 2)
    a = np.einsum("ijkl,l->ij", w, c) / sxx  # dz/dx (columnas)
    b = np.einsum("ijkl,k->ij", w, c) / sxx  # dz/dy (filas)
    media = w.mean(axis=(2, 3))
    plano = media[..., None, None] + a[..., None, None] * c[None, None, None, :] + b[..., None, None] * c[None, None, :, None]
    rug = np.sqrt(np.mean((w - plano) ** 2, axis=(2, 3)))
    esc = w.max(axis=(2, 3)) - w.min(axis=(2, 3))
    pend = np.degrees(np.arctan(np.hypot(a, b)))
    return pend, esc, rug


def clasificar(pend, esc, rug, sigma=None):
    """True = NO transitable. Con `sigma` (m, por ventana) se resta el sesgo esperado del ruido: la rugosidad al
    cuadrado se corrige en 0.97 sigma^2 (97 grados de libertad de 100) y el escalon en 5.0 sigma (rango esperado de 100
    normales)."""
    if sigma is not None:
        rug = np.sqrt(np.maximum(rug ** 2 - 0.97 * sigma ** 2, 0.0))
        esc = np.maximum(esc - 5.0 * sigma, 0.0)
    return (pend > PEND_MAX) | (esc > ESC_MAX) | (rug > RUG_MAX)


def confusion(verdad, est):
    tp = int(np.sum(verdad & est))
    fn = int(np.sum(verdad & ~est))  # peligroso declarado seguro
    fp = int(np.sum(~verdad & est))
    tn = int(np.sum(~verdad & ~est))
    return tp, fn, fp, tn


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    rng = np.random.default_rng(103)
    z = terreno(rng)
    print(f"DATOS SINTETICOS (semilla 103): MDE {N}x{N} celdas de {CELDA} m, 40 rocas, huella {V*CELDA:.1f} m, umbrales ILUSTRATIVOS "
          f"(pendiente {PEND_MAX} grados, escalon {ESC_MAX} m, rugosidad {RUG_MAX} m)")
    pv, ev, rv = metricas(z)
    verdad = clasificar(pv, ev, rv)
    print(f"Verdad: {verdad.mean()*100:.1f} % de las ventanas NO transitables; pendiente maxima {pv.max():.1f} grados, escalon maximo {ev.max():.2f} m")
    sig = lambda r: 0.0005 * r ** 2
    yy = (np.arange(N - V + 1) + (V - 1) / 2) * CELDA  # rango del centro de cada ventana
    sig_w = sig(yy)[:, None] * np.ones((1, N - V + 1))
    zr = z + rng.normal(0, 1, z.shape) * sig(np.arange(N) * CELDA)[:, None]
    pe, ee, re = metricas(zr)
    print("Sin ruido (control): errores de clasificacion =", int(np.sum(clasificar(*metricas(z)) != verdad)))
    print("Ruido del MDE por rango: sigma_h = " + ", ".join(f"{sig(r)*100:.1f} cm a {r:.0f} m" for r in (2, 5, 10, 20)))
    print("Banda de rango [m]   n   falsos 'seguro' sin correccion   con correccion de sesgo    falsas alarmas sin / con")
    bandas = [(0, 5), (5, 10), (10, 15), (15, 20)]
    est0 = clasificar(pe, ee, re)
    est1 = clasificar(pe, ee, re, sigma=sig_w)
    tot = {}
    for lo, hi in bandas:
        m = (yy >= lo) & (yy < hi)
        vm = verdad[m, :]
        r0, r1 = confusion(vm, est0[m, :]), confusion(vm, est1[m, :])
        neg = max(int(np.sum(~vm)), 1)
        pos = max(int(np.sum(vm)), 1)
        print(f"  {lo:2d} - {hi:2d}   {vm.size:6d}   {r0[1]:5d} ({r0[1]/pos*100:5.1f} % de peligro)   {r1[1]:5d} ({r1[1]/pos*100:5.1f} %)"
              f"   {r0[2]/neg*100:5.1f} % / {r1[2]/neg*100:5.1f} %")
        for k, v in zip(("tp0", "fn0", "fp0", "tn0"), r0):
            tot[k] = tot.get(k, 0) + v
        for k, v in zip(("tp1", "fn1", "fp1", "tn1"), r1):
            tot[k] = tot.get(k, 0) + v
    print(f"Total sin correccion:  TP={tot['tp0']} FN={tot['fn0']} FP={tot['fp0']} TN={tot['tn0']} ; exhaustividad de peligro = {tot['tp0']/(tot['tp0']+tot['fn0']):.4f}")
    print(f"Total con correccion:  TP={tot['tp1']} FN={tot['fn1']} FP={tot['fp1']} TN={tot['tn1']} ; exhaustividad de peligro = {tot['tp1']/(tot['tp1']+tot['fn1']):.4f}")
    # Mapa de coste simple: transitables / dudosas / bloqueadas
    print("Fraccion transitable del MDE ruidoso (sin / con correccion): "
          f"{(~est0).mean()*100:.1f} % / {(~est1).mean()*100:.1f} % ; verdad: {(~verdad).mean()*100:.1f} %")
    assert np.sum(clasificar(*metricas(z)) != verdad) == 0
    assert tot["fn1"] >= tot["fn0"]
    assert tot["fp1"] <= tot["fp0"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
