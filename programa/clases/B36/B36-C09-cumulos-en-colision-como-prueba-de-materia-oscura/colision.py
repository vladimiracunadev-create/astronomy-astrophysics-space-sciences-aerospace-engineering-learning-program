#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C09: desplazamiento entre masa y gas en un cumulo en colision y lente de esfera isoterma singular (juguete).

Datos: SINTETICOS. Velocidad relativa 3000 km/s, tiempo desde el paso 0,05 Gyr, masa del subcumulo 1e14 Msun dentro de 200 kpc, sigma_v = 1000 km/s, D_ls/D_s = 0,5 y
1000 laminas/particulas por componente son valores ILUSTRATIVOS (no los del cumulo 1E 0657-558). Consultado el 2026-11-09 solo el RESUMEN de Clowe et al. 2006
(arXiv:astro-ph/0608407: z = 0,296; desplazamiento de 8 sigma entre el centro de masa total y el bariónico) y el RESUMEN de Randall et al. 2008 (arXiv:0704.0261: sigma/m < 1,25 cm^2/g
y < 0,7 cm^2/g); sus metodos y datos NO se reproducen aqui. G (NIST CODATA 2022), au (IERS TN36) y GM_sol nominal (UAI 2015 B3) consultados el 2026-11-09.
Modelo: (a) cada particula del subcumulo interacciona con probabilidad f = 1 - exp(-Sigma sigma/m) y, si lo hace, se detiene en el punto del choque; el centroide queda en (1-f) v t;
el gas (colisional) tiene f ~ 1; (b) lente SIS: theta_E = 4 pi (sigma_v/c)^2 D_ls/D_s, gamma_t = theta_E/(2 theta), ruido de forma 0,25 por componente, ajuste por minimos cuadrados con centro libre.
Segunda via: media de la simulacion Monte Carlo frente a la formula cerrada; theta_E y centro ajustados frente a los verdaderos.
Supuestos: sin hidrodinamica, interaccion de detencion total, SIS aislada sin otro cumulo ni lentes fuertes. Validez: solo pedagogica.
Tolerancia: centroides MC dentro de 3 errores estandar de la formula; theta_E dentro de 3 sigma; centro dentro de 3 sigma de posicion.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
G = 6.67430e-11
AU = 149597870700.0
KPC = AU * 648000 / math.pi * 1e3
GMSUN = 1.3271244e20
MSUN = GMSUN / G
GYR = 3.15576e16  # 1 Gyr = 1e9 anos julianos de 365,25 d


def mc_offset(rng, f, n=1000, vt=1.0, sig=0.3):
    xs = []
    for _ in range(n):
        x0 = rng.gauss(0, sig)  # estructura inicial (kpc relativo normalizado)
        if rng.random() < f:
            xs.append(x0)  # se detiene en el choque
        else:
            xs.append(x0 + vt)
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1) / n)
    return m, sd


def E(z, om=0.315):
    return math.sqrt(om * (1 + z) ** 3 + 1 - om)


def dm_mpc(z, h0=67.4, om=0.315):
    n = 2000
    hh = z / n
    f = lambda t: 1 / E(t, om)
    s = f(0) + f(z) + sum((4 if i % 2 else 2) * f(i * hh) for i in range(1, n))
    return C / (h0 * 1e3) * s * hh / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    v = 3000e3  # m/s
    t = 0.05 * GYR
    vt_kpc = v * t / KPC
    sigma = 1e14 * MSUN * 1e3 / (math.pi * (200 * KPC * 100) ** 2)  # g / cm^2 : masa en g, radio en cm
    print(f"v t = {vt_kpc:.1f} kpc ; Sigma = {sigma:.3f} g/cm^2 (1e14 Msun en 200 kpc)")
    print(f"{'sigma/m [cm2/g]':>16} {'tau':>7} {'f=1-e^-tau':>11} {'offset DM-gal teo [kpc]':>24} {'MC [kpc]':>10} {'error':>7} {'pull':>6}")
    pulls = []
    for sm in (0.0, 0.5, 1.25, 5.0):
        f = 1 - math.exp(-sigma * sm)
        teo = f * vt_kpc
        # el centroide de las galaxias (f=0) y el de la DM se miden en la misma maqueta
        m_d, s_d = mc_offset(rng, f, vt=vt_kpc, sig=30.0)
        m_g, s_g = mc_offset(rng, 0.0, vt=vt_kpc, sig=30.0)
        off = m_g - m_d
        err = math.hypot(s_d, s_g)
        pull = (off - teo) / err
        pulls.append(pull)
        print(f"{sm:16.2f} {sigma * sm:7.3f} {f:11.3f} {teo:24.1f} {off:10.1f} {err:7.1f} {pull:6.2f}")
    m_gas, s_gas = mc_offset(rng, 0.999, vt=vt_kpc, sig=30.0)
    m_gal, s_gal = mc_offset(rng, 0.0, vt=vt_kpc, sig=30.0)
    print(f"gas (f = 0.999) frente a galaxias: desplazamiento = {m_gal - m_gas:.1f} +/- {math.hypot(s_gas, s_gal):.1f} kpc (teorico {0.999 * vt_kpc:.1f})")
    # lente SIS
    z = 0.296
    da = dm_mpc(z) / (1 + z)  # Mpc
    esc = da * 1e3 * math.pi / 648000  # kpc por arcsec
    print(f"D_A(z = {z}) = {da:.1f} Mpc ; escala = {esc:.3f} kpc/arcsec")
    sv = 1000e3
    th_e = 4 * math.pi * (sv / C) ** 2 * 0.5 * 648000 / math.pi  # arcsec
    print(f"theta_E verdadero = {th_e:.2f} arcsec")
    c_true = (m_gal - m_gas) / esc  # la masa esta en el centroide de las galaxias; el gas queda detras
    half = 240.0  # semicampo (arcsec)
    ng = 600
    gal = []
    for _ in range(ng):
        x = rng.uniform(-half, half)
        y = rng.uniform(-half, half)
        th = math.hypot(x - c_true, y)
        if th < 8:
            continue
        g_t = th_e / (2 * th)
        phi = math.atan2(y, x - c_true)
        e1 = -g_t * math.cos(2 * phi) + rng.gauss(0, 0.25)
        e2 = -g_t * math.sin(2 * phi) + rng.gauss(0, 0.25)
        gal.append((x, y, e1, e2))

    def ajusta(cx, cy):
        num = den = 0.0
        for x, y, e1, e2 in gal:
            dx, dy = x - cx, y - cy
            th = math.hypot(dx, dy)
            if th < 8:
                continue
            phi = math.atan2(dy, dx)
            et = -(e1 * math.cos(2 * phi) + e2 * math.sin(2 * phi))
            g = 1 / (2 * th)
            num += et * g
            den += g * g
        return num / den, den

    best = None
    rejilla = []
    for ix in range(-30, 31):
        for iy in range(-10, 11):
            cx, cy = 2.0 * ix, 2.0 * iy
            th_hat, den = ajusta(cx, cy)
            gain = th_hat ** 2 * den / 0.25 ** 2
            rejilla.append((gain, cx, cy, th_hat, den))
            if best is None or gain > best[0]:
                best = (gain, cx, cy, th_hat, den)
    gain, cx, cy, th_hat, den = best
    sig_th = 0.25 / math.sqrt(den)
    # region Delta chi2 < 2.3 (68 % para 2 parametros)
    reg = [(a, b) for g, a, b, _, _ in rejilla if g >= gain - 2.3]
    rx = (max(a for a, b in reg) - min(a for a, b in reg)) / 2
    ry = (max(b for a, b in reg) - min(b for a, b in reg)) / 2
    sx = max(rx, 1.0)
    print(f"{len(gal)} galaxias de fondo ; centro verdadero ({c_true:.1f}, 0.0) arcsec ; centro ajustado ({cx:.1f}, {cy:.1f}) +/- ({sx:.1f}, {max(ry, 1.0):.1f}) arcsec")
    print(f"theta_E ajustado = {th_hat:.2f} +/- {sig_th:.2f} arcsec (verdadero {th_e:.2f}) ; sigma_v ajustada = {sv / 1e3 * math.sqrt(th_hat / th_e):.0f} km/s")
    nsig = abs(cx - 0.0) / sx
    desp = (m_gal - m_gas)
    print(f"desplazamiento masa-gas: {desp:.1f} kpc = {desp / esc:.1f} arcsec ; el centro de la lente (con gas en el origen) dista {abs(cx):.1f} arcsec = {nsig:.1f} errores de posicion")
    assert all(abs(p) < 3 for p in pulls)
    assert abs(th_hat - th_e) < 3 * sig_th
    assert abs(cx - c_true) < 3 * sx + 2.0
    assert nsig > 3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
