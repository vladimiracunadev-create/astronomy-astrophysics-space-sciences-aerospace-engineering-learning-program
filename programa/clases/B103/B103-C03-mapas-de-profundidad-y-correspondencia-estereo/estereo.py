#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C03: disparidad por bloques (SAD) y profundidad estereo sobre un par SINTETICO rectificado.

Todo es sintetico (semilla 103): imagen izquierda de textura aleatoria, terreno plano visto desde 1.2 m de altura y una
caja a 6 m. Camara ILUSTRATIVA: f = 400 px, punto principal (160, 120), imagen 320 x 240; linea de base B = 0.42 m
(ese orden de magnitud lo cita la ficha de la NASA para las Navcam de Perseverance, pero la camara de aqui NO es esa camara).
Modelo: par rectificado, d = f B / Z; suelo plano: Z = h f / (v - cy). Sistema: pixeles (u a la derecha, v hacia abajo); m.
Metodo: SAD en ventana 9 x 9 con integral de imagen, d entero 0..63, refinamiento subpixel por parabola; Z = f B / d.
Verificacion: error de profundidad frente a la verdad analitica por rango y contraste con sigma_Z = Z^2 sigma_d / (f B), usando
el sigma_d robusto de cada rango. Tolerancias: cociente sigma_Z medido/teorico entre 0.6 y 1.6 en los rangos < 32 m; caja a 6 m +- 0.2 m. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

W, H, F, CX, CY, B, ALT = 320, 240, 400.0, 160.0, 120.0, 0.42, 1.2
V0 = 130
VENT, DMAX = 9, 64
CAJA = (slice(170, 215), slice(120, 200), 6.0)  # filas, columnas, profundidad (m)


def textura(rng):
    base = rng.normal(0, 1, (H, W + 80))
    k = np.array([1, 2, 3, 2, 1], float) / 9
    for ax in (0, 1):
        base = np.apply_along_axis(lambda x: np.convolve(x, k, mode="same"), ax, base)
    base = (base - base.mean()) / base.std()
    return 128 + 40 * base


def escena(rng, ruido=2.0):
    izq = textura(rng)[:, :W].copy()
    # d = f B / Z con Z = h f / (v - cy)  ->  d = B (v - cy) / h
    dv = B * (np.arange(H) - CY)[:, None] / ALT * np.ones((1, W))
    dv[:V0, :] = 0
    drec = F * B / CAJA[2]
    dv[CAJA[0], CAJA[1]] = drec
    der = np.zeros((H, W))
    x = np.arange(W, dtype=float)
    for v in range(V0, H):
        der[v] = np.interp(x + dv[v], x, izq[v])  # derecha(x) = izquierda(x + d)
    # la caja: se pinta con la textura izquierda desplazada d columnas
    fi, co = CAJA[0], CAJA[1]
    d_int = int(round(drec))
    der[fi, co.start - d_int:co.stop - d_int] = izq[fi, co]
    dv[CAJA[0], CAJA[1]] = d_int  # la verdad de la caja es el desplazamiento entero usado
    izq_n = izq + rng.normal(0, ruido, izq.shape)
    der_n = der + rng.normal(0, ruido, der.shape)
    return izq_n, der_n, dv


def caja_filtro(a, n):
    c = np.cumsum(np.cumsum(np.pad(a, ((1, 0), (1, 0))), axis=0), axis=1)
    s = c[n:, n:] - c[:-n, n:] - c[n:, :-n] + c[:-n, :-n]
    r = n // 2
    out = np.full(a.shape, np.inf)
    out[r:r + s.shape[0], r:r + s.shape[1]] = s
    return out


def disparidad(izq, der):
    costes = np.full((DMAX, H, W), np.inf)
    for d in range(DMAX):
        diff = np.full((H, W), np.inf)
        diff[:, d:] = np.abs(izq[:, d:] - der[:, :W - d]) if d else np.abs(izq - der)
        # derecha(x) = izquierda(x + d): el pixel izquierdo u se compara con derecha(u - d)
        costes[d] = caja_filtro(np.where(np.isfinite(diff), diff, 255.0), VENT)
    d0 = np.argmin(costes, axis=0)
    sub = d0.astype(float)
    ii, jj = np.indices(d0.shape)
    ok = (d0 > 0) & (d0 < DMAX - 1)
    cm, c0, cp = costes[np.clip(d0 - 1, 0, DMAX - 1), ii, jj], costes[d0, ii, jj], costes[np.clip(d0 + 1, 0, DMAX - 1), ii, jj]
    with np.errstate(invalid="ignore"):
        den = cm - 2 * c0 + cp
    with np.errstate(invalid="ignore", divide="ignore"):
        corr = np.where(ok & (den > 0), 0.5 * (cm - cp) / den, 0.0)
    return sub + np.clip(corr, -0.5, 0.5)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    rng = np.random.default_rng(103)
    print(f"DATOS SINTETICOS (semilla 103): par rectificado {W}x{H}, f = {F:.0f} px, B = {B} m (ilustrativa), altura {ALT} m, caja a {CAJA[2]} m")
    izq, der, dv = escena(rng)
    d = disparidad(izq, der)
    r = VENT // 2
    mascara = np.zeros((H, W), bool)
    mascara[V0 + r:H - r, DMAX + r:W - r] = True
    suelo = mascara.copy()
    suelo[CAJA[0].start - 12:CAJA[0].stop + 12, CAJA[1].start - DMAX - 12:CAJA[1].stop + 12] = False
    err = d - dv
    print(f"Disparidad del suelo: de {dv[H-1, 0]:.2f} px (fila inferior, Z = {F*B/dv[H-1,0]:.2f} m) a {dv[V0+r,0]:.2f} px (fila {V0+r}, Z = {F*B/dv[V0+r,0]:.1f} m)")
    sd = err[suelo].std()
    print(f"Error de disparidad en el suelo (global): media = {err[suelo].mean():+.3f} px, sigma_d = {sd:.3f} px")
    malos = np.mean(np.abs(err[suelo]) > 1.0) * 100
    print(f"Pixeles del suelo con |error| > 1 px (umbral ilustrativo): {malos:.2f} %")
    print("Por rango (sigma robusta = 1.4826 MAD respecto de la mediana):")
    print("Rango Z [m]    n    sigma_d [px]  malos [%]  RMSE_Z [m]  sigma_Z rob. [m]  sigma_Z teor. [m]  cociente")
    z_v = np.where(dv > 0.5, F * B / np.maximum(dv, 1e-9), np.nan)
    z_e = F * B / np.maximum(d, 1e-3)
    rangos = [(4, 8), (8, 16), (16, 32), (32, 60)]
    cocientes = []
    for lo, hi in rangos:
        m = suelo & (z_v >= lo) & (z_v < hi)
        if m.sum() < 50:
            continue
        e = z_e[m] - z_v[m]
        ed = err[m]
        sdr = 1.4826 * np.median(np.abs(ed - np.median(ed)))
        zc = np.median(z_v[m])
        teo = zc ** 2 * sdr / (F * B)
        sz = 1.4826 * np.median(np.abs(e - np.median(e)))
        cocientes.append((lo, sz / teo))
        print(f" {lo:3d} - {hi:3d}  {m.sum():6d}  {sdr:11.3f}  {np.mean(np.abs(ed) > 1) * 100:9.2f}  {np.sqrt(np.mean(e ** 2)):10.3f}  {sz:15.3f}  {teo:16.3f}  {sz / teo:8.2f}")
    # Caja
    cj = np.zeros((H, W), bool)
    cj[CAJA[0].start + r:CAJA[0].stop - r, CAJA[1].start + r:CAJA[1].stop - r] = True
    zc = z_e[cj]
    print(f"Caja a {CAJA[2]} m (interior): Z estimada = {np.median(zc):.3f} m (mediana), error de disparidad medio {err[cj].mean():+.3f} px")
    # Sensibilidad a la linea de base
    ed = err[suelo]
    sdg = 1.4826 * np.median(np.abs(ed - np.median(ed)))
    print(f"Sensibilidad: sigma_Z a Z = 20 m con sigma_d robusto global = {sdg:.3f} px, segun la linea de base B:")
    for b in (0.1, 0.2, 0.42, 0.84):
        print(f"  B = {b:4.2f} m: sigma_Z = {20.0**2 * sdg / (F * b):6.2f} m")
    for lo, c in cocientes:
        if lo < 32:
            assert 0.6 < c < 1.6, (lo, c)
    assert abs(np.median(zc) - CAJA[2]) < 0.2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
