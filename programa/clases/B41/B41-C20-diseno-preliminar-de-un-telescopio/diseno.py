#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C20: presupuesto de diseno preliminar de un Newton de aficionado (apertura, focal, campo, difraccion, coma, secundario, tolerancias).

Datos: sin constantes del NIST. Todo el diseno es ILUSTRATIVO: D = 250 mm, F = 1250 mm (f/5), sensor de 22,3 x 14,9 mm con pixeles de 4,3 micras, lambda = 550 nm,
seeing de 2,0 arcsec, distancia del eje al plano focal q = 165 mm y objetivo de 1 grado de campo. No describe un instrumento real. 648000/pi = definicion geometrica.
Modelo: se reunen las relaciones verificadas en B41-C09, C10, C11, C12, C13, C16 y C19: escala de placa, campo, Airy, Rayleigh, coma 3 theta F/(16 N^2), secundario a = w + (D-w) q/F,
pupila de salida y aumentos. Tolerancias: Strehl de Marechal exp(-(2 pi sigma)^2) frente a una simulacion con semilla 20261109 de una pantalla de fase blanca (Strehl = |<exp(i phi)>|^2 = exp(-sigma^2)),
y la varianza del desenfoque sigma = W20/sqrt(12) frente a una integracion numerica sobre el disco.
Supuestos: paraboloide perfecto, seeing aparte, sin refraccion atmosferica. Validez: preliminar (orden de magnitud con tolerancias).
Tolerancia: Strehl de la pantalla de fase frente a exp(-sigma^2) 0,005; sigma del desenfoque numerico frente a la forma cerrada 1e-4.
"""
from __future__ import annotations
import math, platform, random, sys

ARCSEC = 648000.0 / math.pi


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, F, lam = 250.0, 1250.0, 550e-6
    w_s, h_s, px = 22.3, 14.9, 4.3e-3
    seeing, q = 2.0, 165.0
    N = F / D
    print("== Requisitos y primera cifra ==")
    print(f"relacion focal f/{N:.1f} ; area colectora = {math.pi*(D/2)**2/100:.1f} cm2 ; ganancia sobre un ojo de 7 mm = {5*math.log10(D/7):.2f} mag")
    airy = 2.44 * lam * N * 1e3
    ray = 1.21967 * lam / D * ARCSEC
    print(f"disco de Airy (diametro) = {airy:.2f} micras = {2.44*lam/D*ARCSEC:.3f} arcsec ; Rayleigh = {ray:.3f} arcsec")
    esc = ARCSEC / F * px
    fov_w, fov_h = [2 * math.degrees(math.atan(x / (2 * F))) for x in (w_s, h_s)]
    print(f"escala = {esc:.4f} arcsec/pixel ; campo = {fov_w:.3f} x {fov_h:.3f} deg ; pixel / (seeing/2) = {esc/(seeing/2):.2f}")
    assert esc < seeing / 2 and fov_w >= 1.0
    # rango de focales para muestrear el seeing entre 2 y 3 pixeles
    for npx in (2.0, 3.0):
        print(f"  {npx:.0f} pixeles por FWHM de seeing -> escala {seeing/npx:.3f} arcsec/pixel -> F = {ARCSEC*px/(seeing/npx):.0f} mm")
    print("== Campo y aberraciones ==")
    diag = math.hypot(w_s, h_s)
    th_edge = diag / 2 / F
    coma_edge = 3 * th_edge * F / (16 * N * N) * 1e3
    r_airy = airy / 2
    print(f"semidiagonal del sensor = {diag/2:.2f} mm = {math.degrees(th_edge)*60:.2f} arcmin ; coma en el borde = {coma_edge:.2f} micras ; radio de Airy = {r_airy:.2f} micras ; razon = {coma_edge/r_airy:.2f}")
    th_max = r_airy * 1e-3 * 16 * N * N / (3 * F)
    print(f"campo con coma igual al radio de Airy: semicampo = {math.degrees(th_max)*60:.2f} arcmin = {th_max*F:.2f} mm de altura de imagen")
    print(f"coma en el borde = {coma_edge/(seeing/ARCSEC*F*1e3):.3f} del FWHM del seeing ({seeing/ARCSEC*F*1e3:.1f} micras)")
    print("== Secundario y obstruccion ==")
    w = diag
    a = w + (D - w) * q / F
    print(f"secundario para iluminar todo el sensor: eje menor a = {a:.1f} mm ; obstruccion lineal = {a/D*100:.1f} % ; por area = {(a/D)**2*100:.1f} % ; perdida = {-2.5*math.log10(1-(a/D)**2):.3f} mag")
    sag = (D / 2) ** 2 / (2 * 2 * F)
    print(f"flecha del primario (paraboloide) = {sag:.3f} mm ; radio de curvatura = {2*F:.0f} mm")
    print("== Oculares ==")
    for fe in (32.0, 12.0, 6.0):
        M = F / fe
        pe = D / M
        print(f"ocular {fe:4.0f} mm: aumento {M:5.1f} ; pupila de salida {pe:5.2f} mm ; {'pupila mayor que el ojo (7 mm)' if pe > 7 else 'ok'}")
    print(f"aumento minimo (pupila 7 mm) = {D/7:.1f} ; maximo orientativo 2 D[mm] = {2*D:.0f}")
    print("== Tolerancias (Marechal) ==")
    sig = 1 / 14
    print(f"RMS de frente de onda 1/14 de onda -> Strehl = {math.exp(-(2*math.pi*sig)**2):.3f}")
    # presupuesto
    terms = [("primario (superficie 1/40 RMS, frente x2)", 2 / 40), ("secundario plano (1/60 RMS, frente x1,414)", math.sqrt(2) / 60), ("desenfoque de un cuarto de la zona 2 lambda N^2 (W20)", None)]
    dz = 0.25 * lam * N * N * 2          # un cuarto de la zona de 2 lambda N^2
    w20 = dz / (8 * N * N) / lam
    # integral numerica de la varianza del desenfoque sobre el disco
    n = 20000
    m1 = m2 = 0.0
    for i in range(n):
        rho = (i + 0.5) / n
        wgt = 2 * rho / n
        m1 += wgt * rho * rho
        m2 += wgt * rho ** 4
    sig_def_num = w20 * math.sqrt(m2 - m1 * m1)
    sig_def = w20 / math.sqrt(12)
    print(f"desenfoque dz = {dz*1e3:.2f} micras: W20 = {w20:.4f} ondas ; sigma (numerico) = {sig_def_num:.6f} ; W20/sqrt(12) = {sig_def:.6f}")
    assert abs(sig_def_num - sig_def) < 1e-4
    sigs = [2 / 40, math.sqrt(2) / 60, sig_def]
    tot = math.sqrt(sum(s * s for s in sigs))
    for (nom, _), s in zip(terms, sigs):
        print(f"  {nom}: {s:.4f} ondas RMS")
    st = math.exp(-(2 * math.pi * tot) ** 2)
    print(f"total RSS = {tot:.4f} ondas RMS ; Strehl de Marechal = {st:.3f}")
    rng = random.Random(20261109)
    n = 40000
    sp = 2 * math.pi * tot
    c = sum(math.cos(rng.gauss(0, sp)) for _ in range(n)) / n
    s = sum(math.sin(rng.gauss(0, sp)) for _ in range(n)) / n
    st_mc = c * c + s * s
    print(f"pantalla de fase blanca con la misma sigma ({n} puntos, semilla 20261109): Strehl = {st_mc:.3f} ; exp(-sigma^2) = {st:.3f}")
    assert abs(st_mc - st) < 0.005
    assert st > 0.8
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
