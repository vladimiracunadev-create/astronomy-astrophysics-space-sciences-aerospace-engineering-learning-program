#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C26: correlacion de terreno (correlacion cruzada normalizada, NCC) con desplazamiento subpixel y ambiguedad.

Todo SINTETICO: terreno de 256 x 256 px generado como ruido gaussiano filtrado en Fourier (espectro ~ exp(-k^2 / (2 k0^2)) con k0 = 0.12 ciclos/px, ILUSTRATIVO), normalizado a media 0 y desviacion 1.
La imagen 'actual' es el terreno desplazado por (dx, dy) = (5.37, -3.82) px (desplazamiento de Fourier, subpixel exacto) mas ruido gaussiano de sigma 0.05, 0.2, 0.5 y 1.0.
La plantilla es un recorte de 32 x 32 del terreno original centrado en el pixel (128, 128). Busqueda: NCC en una ventana de +/-12 px; maximo y refinamiento subpixel por parabola independiente
en cada eje. 100 realizaciones por nivel de ruido (semilla 89). Se reporta el error rms del desplazamiento, la altura del pico de NCC y la razon pico/segundo pico.
Segundo caso: terreno periodico (patron repetido cada 16 px) con la misma plantilla, mostrando ambiguedad: la razon pico/segundo pico tiende a 1 y el emparejamiento falla.
Tolerancias: con ruido 0.05, error rms < 0.05 px; el error crece con el ruido; con terreno periodico la razon pico/segundo pico < 1.1.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

N = 256
DX, DY = 5.37, -3.82
T = 32
BUSQ = 12


def terreno(rng):
    k = np.fft.fftfreq(N)
    kx, ky = np.meshgrid(k, k)
    esp = np.exp(-(kx**2 + ky**2) / (2 * 0.12**2))
    z = np.fft.ifft2(np.fft.fft2(rng.normal(size=(N, N))) * esp).real
    return (z - z.mean()) / z.std()


def desplaza(z, dx, dy):
    k = np.fft.fftfreq(N)
    kx, ky = np.meshgrid(k, k)
    return np.fft.ifft2(np.fft.fft2(z) * np.exp(-2j * np.pi * (kx * dx + ky * dy))).real


def ncc_mapa(img, plantilla, cx, cy):
    t = plantilla - plantilla.mean(); tn = np.sqrt((t**2).sum())
    m = np.full((2 * BUSQ + 1, 2 * BUSQ + 1), -1.0)
    h = T // 2
    for j, oy in enumerate(range(-BUSQ, BUSQ + 1)):
        for i, ox in enumerate(range(-BUSQ, BUSQ + 1)):
            w = img[cy + oy - h:cy + oy + h, cx + ox - h:cx + ox + h]
            wz = w - w.mean(); wn = np.sqrt((wz**2).sum())
            m[j, i] = (t * wz).sum() / (tn * wn + 1e-12)
    return m


def pico(m):
    j, i = np.unravel_index(np.argmax(m), m.shape)
    def sub(a, b, c):
        d = a - 2 * b + c
        return 0.5 * (a - c) / d if d != 0 else 0.0
    di = sub(m[j, i - 1], m[j, i], m[j, i + 1]) if 0 < i < m.shape[1] - 1 else 0.0
    dj = sub(m[j - 1, i], m[j, i], m[j + 1, i]) if 0 < j < m.shape[0] - 1 else 0.0
    # segundo pico: maximo fuera de un entorno de 3 px del primero
    mm = m.copy()
    mm[max(j - 3, 0):j + 4, max(i - 3, 0):i + 4] = -2
    return (i - BUSQ + di, j - BUSQ + dj, m[j, i], mm.max())


def main():
    rng = np.random.default_rng(89)
    z = terreno(rng)
    c = N // 2
    h = T // 2
    plantilla = z[c - h:c + h, c - h:c + h]
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (terreno SINTETICO, semilla 89)",
           f"desplazamiento verdadero = ({DX}, {DY}) px ; plantilla {T} x {T} px ; busqueda +/-{BUSQ} px"]
    res = {}
    out.append("ruido    error rms [px]   NCC pico medio   razon pico/segundo pico (media)")
    base = desplaza(z, DX, DY)  # el contenido se mueve +DX, +DY
    prev = 0.0
    ok = True
    for s in (0.05, 0.2, 0.5, 1.0):
        errs = []; pk = []; rz = []
        for _ in range(100):
            img = base + rng.normal(0, s, base.shape)
            m = ncc_mapa(img, plantilla, c, c)
            ex, ey, p1, p2 = pico(m)
            errs.append((ex - DX, ey - DY)); pk.append(p1); rz.append(p1 / max(p2, 1e-9))
        e = np.array(errs); rms = float(np.sqrt(np.mean(np.sum(e**2, axis=1))))
        out.append(f"{s:5.2f}  {rms:14.4f}  {np.mean(pk):15.3f}  {np.mean(rz):25.2f}")
        k = str(s).replace(".", "")
        res[f"rms_{k}"] = rms; res[f"pk_{k}"] = float(np.mean(pk)); res[f"rz_{k}"] = float(np.mean(rz))
        if s == 0.05: ok &= rms < 0.05
        ok &= rms >= prev * 0.9
        prev = rms
    # ambiguedad: terreno periodico
    y, x = np.mgrid[0:N, 0:N]
    zp = np.sin(2 * np.pi * x / 16) * np.sin(2 * np.pi * y / 16)
    zp = (zp - zp.mean()) / zp.std()
    imgp = desplaza(zp, DX, DY) + rng.normal(0, 0.2, zp.shape)
    pl = zp[c - h:c + h, c - h:c + h]
    mp = ncc_mapa(imgp, pl, c, c)
    ex, ey, p1, p2 = pico(mp)
    out.append(f"Terreno periodico (16 px), ruido 0.20: pico NCC = {p1:.3f}, segundo pico = {p2:.3f}, razon = {p1/p2:.2f}; desplazamiento hallado = ({ex:.2f}, {ey:.2f}) px frente a ({DX}, {DY}) verdadero")
    res.update(per_p1=float(p1), per_p2=float(p2), per_rz=float(p1 / p2), per_ex=float(ex), per_ey=float(ey))
    ok &= p1 / p2 < 1.1
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
