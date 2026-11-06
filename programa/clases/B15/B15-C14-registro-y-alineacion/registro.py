#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C14: registro por correlación de fase y por puntos (Procrustes).

Datos: SINTÉTICOS, semilla fija. Campo de 64 x 64 con 12 estrellas gaussianas
(sigma 2 px); la segunda imagen es la primera desplazada por (dy, dx) mediante
el teorema del desplazamiento de Fourier (exacto para señales de banda limitada).
Modelo 1: correlación de fase R = F1 conj(F2)/|F1 conj(F2)|, pico de su
transformada inversa en el desplazamiento; refinado subpíxel evaluando la
inversa en una rejilla fina alrededor del pico (DFT local).
Modelo 2: con N pares de puntos y rotación + traslación, la solución de
Procrustes (SVD) es exacta sin ruido; con ruido gaussiano de sigma_p por
coordenada en ambos conjuntos, el ángulo estimado tiene desviación ~ sigma_p sqrt(2)/sqrt(S),
S = suma de |P - media|^2.
Convención: el desplazamiento (dy, dx) es el de la imagen 2 respecto de la 1
(im2[y, x] = im1[y - dy, x - dx]).
Tolerancias: 0.01 px (subpíxel sin ruido); 1e-9 (Procrustes sin ruido); 15 % en la desviación del ángulo.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


N = 64
yy, xx = np.mgrid[0:N, 0:N]


def campo(rng):
    im = np.zeros((N, N))
    for _ in range(12):
        cy, cx = rng.uniform(10, N - 10, 2)
        F = rng.uniform(300, 1000)
        im += F * np.exp(-0.5 * (((yy - cy) ** 2 + (xx - cx) ** 2) / 2.0**2))
    return im


def desplazar(im, dy, dx):
    ky = np.fft.fftfreq(N)[:, None]
    kx = np.fft.fftfreq(N)[None, :]
    return np.real(np.fft.ifft2(np.fft.fft2(im) * np.exp(-2j * np.pi * (ky * dy + kx * dx))))


def fase(im1, im2, paso=0.01, rango=1.0):
    F1, F2 = np.fft.fft2(im1), np.fft.fft2(im2)
    # im2 = im1 desplazada por d  =>  F2 = F1 exp(-2 pi i k.d)  =>  conj(F1) F2 / |.| = exp(-2 pi i k d)
    R = np.conj(F1) * F2
    R /= np.maximum(np.abs(R), 1e-12)
    c = np.real(np.fft.ifft2(R))                       # pico en +d
    py, px = np.unravel_index(np.argmax(c), c.shape)
    py = py - N if py > N // 2 else py
    px = px - N if px > N // 2 else px
    g = np.arange(-rango, rango + paso / 2, paso)
    ky = np.fft.fftfreq(N)
    Ey = np.exp(2j * np.pi * np.outer(py + g, ky))
    Ex = np.exp(2j * np.pi * np.outer(px + g, ky))
    fino = np.real(Ey @ R @ Ex.T)
    iy, ix = np.unravel_index(np.argmax(fino), fino.shape)
    return (py, px), (py + g[iy], px + g[ix])


def procrustes(P, Q):
    """Rotación R y traslación t con Q ~ P R^T + t (mínimos cuadrados)."""
    mp, mq = P.mean(0), Q.mean(0)
    U, _, Vt = np.linalg.svd((P - mp).T @ (Q - mq))
    D = np.diag([1, np.sign(np.linalg.det(Vt.T @ U.T))])
    R = Vt.T @ D @ U.T
    return R, mq - R @ mp


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15014)
im1 = campo(rng)

# (1) Desplazamiento entero
im2 = desplazar(im1, 3, -5)
ent, sub = fase(im1, im2)
print(f"(1) desplazamiento entero (3, -5): estimado {ent}")
prueba(ent == (3, -5), "entero")

# (2) Subpíxel sin ruido
for d in ((3.4, -2.7), (-0.25, 6.15)):
    im2 = desplazar(im1, *d)
    _, sub = fase(im1, im2)
    err = max(abs(sub[0] - d[0]), abs(sub[1] - d[1]))
    print(f"(2) desplazamiento {d}: estimado ({sub[0]:.2f}, {sub[1]:.2f}); error máx. {err:.3f} px")
    prueba(err <= 0.0101, "subpíxel sin ruido")

# (3) Con ruido
d = (3.4, -2.7)
base = desplazar(im1, *d)
for sg in (5.0, 50.0, 200.0):
    errs = []
    for _ in range(30):
        a = im1 + sg * rng.standard_normal((N, N))
        b = base + sg * rng.standard_normal((N, N))
        _, s = fase(a, b)
        errs.append((s[0] - d[0], s[1] - d[1]))
    e = np.array(errs)
    print(f"(3) ruido {sg:5.0f} (pico estelar ~ 500): sesgo ({e[:,0].mean():+.3f}, {e[:,1].mean():+.3f}); "
          f"desviación ({e[:,0].std():.3f}, {e[:,1].std():.3f}) px; fallos groseros (>1 px): {int((np.abs(e) > 1).any(1).sum())}/30")

# (4) Procrustes sin ruido
th = np.deg2rad(0.8)
Rv = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
tv = np.array([2.5, -1.25])
P = rng.uniform(0, 1000, (20, 2))
Q = P @ Rv.T + tv
R, t = procrustes(P, Q)
ang = np.degrees(np.arctan2(R[1, 0], R[0, 0]))
print(f"(4) Procrustes sin ruido: ángulo {ang:.6f}° (real 0.8); traslación ({t[0]:.6f}, {t[1]:.6f}) (real {tv.tolist()})")
prueba(np.allclose(R, Rv, atol=1e-9) and np.allclose(t, tv, atol=1e-8), "Procrustes exacto")

# (5) Procrustes con ruido: sigma_theta ~ sigma_p sqrt(2)/sqrt(sum |P - media|^2)
sp, Np = 0.1, 20
ths, ts = [], []
for _ in range(1000):
    Pn = P + sp * rng.standard_normal(P.shape)
    Qn = Q + sp * rng.standard_normal(Q.shape)
    Rn, tn = procrustes(Pn, Qn)
    ths.append(np.arctan2(Rn[1, 0], Rn[0, 0]))
    ts.append(tn)
ths, ts = np.array(ths), np.array(ts)
teo = sp * np.sqrt(2) / np.sqrt(((P - P.mean(0)) ** 2).sum())
print(f"(5) puntos con error {sp} px, N = {Np}: desviación del ángulo {np.degrees(ths.std()):.5f}° "
      f"(teoría {np.degrees(teo):.5f}°); desviación de la traslación en el origen {ts.std(0).round(3).tolist()} px "
      f"(incluye el brazo de palanca |centroide| * sigma_theta)")
prueba(abs(ths.std() / teo - 1) < 0.15, "desviación del ángulo")
print("Pruebas superadas.")
