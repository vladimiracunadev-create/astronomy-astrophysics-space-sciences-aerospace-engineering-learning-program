#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C19: imagen sucia y deconvolucion CLEAN de Hogbom con tres fuentes puntuales sinteticas (semilla fija).

Datos: ninguno externo. El conjunto de 6 antenas este-oeste (0, 60, 150, 270, 420, 600 m), lambda = 0,21 m, declinacion +40 grados, 12 h de
rotacion, las tres fuentes (1,0; 0,5 y 0,3 Jy) y el ruido (0,05 Jy por parte y visibilidad) son SINTETICOS (semilla 20261109).
Modelo: V_k = suma_s S_s exp(-2 pi i (u_k l_s + v_k m_s)) + ruido; imagen sucia I_D(l, m) = (1/N) suma_k Re(V_k exp(2 pi i (u_k l + v_k m))).
Sin ruido, I_D es la suma de haces sucios desplazados (comprobacion por dos vias). CLEAN de Hogbom: ganancia 0,1, se resta el haz desplazado
del pico del residuo hasta llegar a 3 veces el ruido medido; flujo total de componentes frente al verdadero.
Supuestos: plano del cielo, fuentes en centros de pixel (sin discretizacion), ponderacion uniforme. Validez: orientativa.
Tolerancia: imagen sucia por visibilidades frente a suma de haces a 1e-9; flujo de cada fuente dentro del 5 %; pico residual < 4 sigma.
"""
from __future__ import annotations
import math, platform, random

LAM, DEC = 0.21, math.radians(40.0)
POS = [0.0, 60.0, 150.0, 270.0, 420.0, 600.0]
ARC = math.pi / 180 / 3600
NPIX, PIX = 48, 20 * ARC
FUENTES = [(1.0, 24, 24), (0.5, 30, 20), (0.3, 16, 32)]       # (Jy, x, y) en pixeles

def uv():
    out = []
    for t in range(37):
        H = math.radians(15 * (-6 + t * 20 / 60))
        for i in range(len(POS)):
            for j in range(i + 1, len(POS)):
                B = (POS[j] - POS[i]) / LAM
                u, v = B * math.cos(H), B * math.sin(DEC) * math.sin(H)
                out.append((u, v))
                out.append((-u, -v))
    return out

def calc():
    rng = random.Random(20261109)
    S = uv()
    N = len(S)
    # haz sucio en desplazamientos
    haz = {}
    for dy in range(-NPIX + 1, NPIX):
        for dx in range(-NPIX + 1, NPIX):
            l, m = dx * PIX, dy * PIX
            haz[(dx, dy)] = sum(math.cos(2 * math.pi * (u * l + v * m)) for u, v in S) / N
    # visibilidades
    def vis(ruido):
        out = []
        for u, v in S:
            z = sum(f * complex(math.cos(2 * math.pi * (u * (x - 24) * PIX + v * (y - 24) * PIX)), -math.sin(2 * math.pi * (u * (x - 24) * PIX + v * (y - 24) * PIX))) for f, x, y in FUENTES)
            if ruido:
                z += complex(rng.gauss(0, ruido), rng.gauss(0, ruido))
            out.append(z)
        return out
    def sucia(V):
        im = [[0.0] * NPIX for _ in range(NPIX)]
        for y in range(NPIX):
            for x in range(NPIX):
                l, m = (x - 24) * PIX, (y - 24) * PIX
                im[y][x] = sum((z * complex(math.cos(2 * math.pi * (u * l + v * m)), math.sin(2 * math.pi * (u * l + v * m)))).real for z, (u, v) in zip(V, S)) / N
        return im
    sg = 0.05
    D0 = sucia(vis(0.0))
    dif = 0.0
    for y in range(NPIX):
        for x in range(NPIX):
            suma = sum(f * haz[(x - xs, y - ys)] for f, xs, ys in FUENTES)
            dif = max(dif, abs(D0[y][x] - suma))
    Vn = vis(sg)
    D = sucia(Vn)
    # ruido teorico en la imagen: sigma_visibilidad / sqrt(N) (parte real, ponderacion uniforme)
    sigma_im = sg / math.sqrt(N)
    R = [fila[:] for fila in D]
    comp = {}
    it = 0
    while it < 3000:
        pk, px, py = 0.0, 0, 0
        for y in range(NPIX):
            for x in range(NPIX):
                if abs(R[y][x]) > abs(pk):
                    pk, px, py = R[y][x], x, y
        if abs(pk) < 3 * sigma_im:
            break
        g = 0.1 * pk
        comp[(px, py)] = comp.get((px, py), 0.0) + g
        for y in range(NPIX):
            for x in range(NPIX):
                R[y][x] -= g * haz[(x - px, y - py)]
        it += 1
    rec = []
    for f, xs, ys in FUENTES:
        s = sum(v for (x, y), v in comp.items() if abs(x - xs) <= 2 and abs(y - ys) <= 2)
        rec.append((f, xs, ys, s))
    pico_res = max(abs(v) for fila in R for v in fila)
    return dict(dif=dif, sigma_im=sigma_im, it=it, rec=rec, tot=sum(comp.values()), pico_dirty=max(max(f) for f in D),
                pico_res=pico_res, ncomp=len(comp), N=N)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{r['N']} muestras uv ; imagen sucia por visibilidades frente a suma de haces: diferencia maxima = {r['dif']:.2e} Jy/haz")
    print(f"ruido teorico de la imagen = {r['sigma_im']*1e3:.2f} mJy/haz ; pico de la imagen sucia = {r['pico_dirty']:.3f} Jy/haz")
    print(f"CLEAN: {r['it']} iteraciones, {r['ncomp']} pixeles con componentes, flujo total = {r['tot']:.3f} Jy (verdadero 1.800)")
    print(f"{'S verdadero [Jy]':>17} {'pixel':>9} {'S recuperado [Jy]':>18} {'error [%]':>10}")
    for f, x, y, s in r["rec"]:
        print(f"{f:17.3f} ({x:2d},{y:2d}) {s:18.3f} {100*(s/f-1):10.2f}")
    print(f"pico residual = {r['pico_res']*1e3:.2f} mJy/haz = {r['pico_res']/r['sigma_im']:.2f} sigma")
    assert r["dif"] < 1e-9
    for f, x, y, s in r["rec"]:
        assert abs(s / f - 1) < 0.05
    assert r["pico_res"] < 4 * r["sigma_im"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
