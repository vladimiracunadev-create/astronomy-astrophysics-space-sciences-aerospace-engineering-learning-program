#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C25: deteccion de limbo con borde subpixel y ajuste de circulo (Kasa) en imagenes sinteticas de un disco planetario.

Todo SINTETICO: imagen de 200 x 200 px con un disco de radio 80.3 px centrado en (100.4, 99.6) (ILUSTRATIVOS), borde difuminado por una PSF gaussiana de sigma 1.5 px
(perfil radial de error: I = A/2 erfc((r - R)/(sqrt(2) sigma))), amplitud 100, ruido gaussiano de 2 (1 sigma) por pixel, semilla 83. Dos casos: disco completo y disco gibboso
(angulo de fase 90 grados: sombreado de Lambert I = A max(0, n.s) con s = (sin a, 0, cos a)), donde solo la mitad iluminada tiene limbo detectable.
Metodo: 180 rayos desde un centro aproximado (error inicial de 4 px); en cada rayo, perfil con interpolacion bilineal, derivada radial, maximo de |gradiente| con interpolacion
parabolica (subpixel); se descartan rayos con gradiente < 25 % del maximo; ajuste de circulo por minimos cuadrados algebraicos (Kasa: x^2 + y^2 + D x + E y + F = 0). 300 realizaciones de ruido por caso.
Tolerancias: disco completo, error del centro < 0.05 px y del radio < 0.05 px (medias de 300); en el gibboso se reporta el sesgo.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

N = 200
CX, CY, R0 = 100.4, 99.6, 80.3
SIGP, AMP, SIGN = 1.5, 100.0, 2.0


def imagen(rng, fase_deg):
    y, x = np.mgrid[0:N, 0:N].astype(float)
    dx, dy = x - CX, y - CY
    r = np.hypot(dx, dy)
    borde = 0.5 * np.vectorize(math.erfc)((r - R0) / (math.sqrt(2) * SIGP))
    if fase_deg is None:
        I = AMP * borde
    else:
        a = math.radians(fase_deg)
        rr = np.minimum(r, R0 * 0.999) / R0
        nz = np.sqrt(1 - rr**2)
        ndot = (dx / R0) * math.sin(a) + nz * math.cos(a)
        I = AMP * borde * np.clip(ndot, 0, None)
    return I + rng.normal(0, SIGN, I.shape)


def bilineal(img, x, y):
    x0 = np.floor(x).astype(int); y0 = np.floor(y).astype(int)
    fx, fy = x - x0, y - y0
    x0 = np.clip(x0, 0, N - 2); y0 = np.clip(y0, 0, N - 2)
    return (img[y0, x0] * (1 - fx) * (1 - fy) + img[y0, x0 + 1] * fx * (1 - fy) + img[y0 + 1, x0] * (1 - fx) * fy + img[y0 + 1, x0 + 1] * fx * fy)


def limbo(img, c0, nr=180):
    pts = []
    s = np.arange(40.0, 120.0, 0.25)
    gmax = []
    cand = []
    for k in range(nr):
        t = 2 * math.pi * k / nr
        x = c0[0] + s * math.cos(t); y = c0[1] + s * math.sin(t)
        ok = (x > 1) & (x < N - 2) & (y > 1) & (y < N - 2)
        if ok.sum() < 20:
            continue
        p = bilineal(img, x[ok], y[ok])
        # suavizado simple y derivada radial
        p = np.convolve(p, np.ones(9) / 9, mode="same")
        g = -np.gradient(p, s[ok])
        j = int(np.argmax(g[5:-5])) + 5
        if 0 < j < len(g) - 1:
            a, b, c = g[j - 1], g[j], g[j + 1]
            d = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) != 0 else 0.0
        else:
            d = 0.0
        sr = s[ok][j] + d * 0.25
        cand.append((t, sr, g[j], c0[0] + sr * math.cos(t), c0[1] + sr * math.sin(t)))
    gm = max(c[2] for c in cand)
    pts = np.array([[c[3], c[4]] for c in cand if c[2] >= 0.25 * gm])
    return pts


def kasa(pts):
    x, y = pts[:, 0], pts[:, 1]
    A = np.column_stack([x, y, np.ones(len(x))])
    b = -(x**2 + y**2)
    D, E, F = np.linalg.lstsq(A, b, rcond=None)[0]
    cx, cy = -D / 2, -E / 2
    r = math.sqrt(max(cx**2 + cy**2 - F, 0))
    return cx, cy, r


def main():
    rng = np.random.default_rng(83)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (imagen SINTETICA, semilla 83)",
           f"Disco: centro ({CX}, {CY}) px, radio {R0} px, PSF sigma {SIGP} px, ruido {SIGN} (amplitud {AMP}); centro inicial desplazado 4 px"]
    res = {}
    out.append("caso                 puntos de limbo   sesgo centro [px] (x, y)     sesgo radio [px]   sigma centro [px]   sigma radio [px]")
    ok = True
    for nom, fase in (("disco completo", None), ("gibboso (fase 90)", 90.0)):
        e = []
        npts = []
        for _ in range(300):
            img = imagen(rng, fase)
            pts = limbo(img, (CX + 3.0, CY - 2.6))
            cx, cy, r = kasa(pts)
            e.append((cx - CX, cy - CY, r - R0)); npts.append(len(pts))
        e = np.array(e); m = e.mean(axis=0); s = e.std(axis=0, ddof=1)
        out.append(f"{nom:20s} {np.mean(npts):12.1f}   ({m[0]:+.3f}, {m[1]:+.3f})            {m[2]:+.3f}            {math.hypot(s[0], s[1]):.3f}              {s[2]:.3f}")
        k = "c" if fase is None else "g"
        res[f"{k}_n"] = float(np.mean(npts)); res[f"{k}_bx"] = float(m[0]); res[f"{k}_by"] = float(m[1]); res[f"{k}_br"] = float(m[2])
        res[f"{k}_sc"] = float(math.hypot(s[0], s[1])); res[f"{k}_sr"] = float(s[2])
        if fase is None:
            ok &= math.hypot(m[0], m[1]) < 0.05 and abs(m[2]) < 0.05
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
