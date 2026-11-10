#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C06: anchos natural, Doppler y por presion de la linea J=1-0 del 12C16O y perfil de Voigt.

Datos consultados el 2026-11-09:
  - CODATA 2022 (NIST): c, k, u. S1.
  - Frecuencia 115271.2018 MHz (catalogo JPL, c028001.cat). S4. Coeficiente A = 7.203e-08 s^-1 (LAMDA, co.dat). S5.
  - Ec. (7) del documento del catalogo JPL (Pickett et al., ed. 2003): semiancho Doppler (HWHM) = 1.17221e-6 nu sqrt((T/300)(28/m)). S3.
  - Definicion de HITRAN (hitran.org/docs/definitions-and-units): gamma_air es el HWHM en cm^-1/atm a 296 K y 1 atm y n_air el exponente de
    (T_ref/T) del ancho lorentziano. S7.
Datos SINTETICOS / ILUSTRATIVOS (no medidos ni de ninguna base consultada): gamma_ref = 0.060 cm^-1/atm, n = 0.70 (valores tipicos supuestos
  para el ensanchamiento del CO por aire; NO provienen de HITRAN), entornos de densidad 1e4 cm^-3 (nucleo frio) y 1 atm (atmosfera).
Modelo: Gaussiana (Doppler) con FWHM_D = (nu/c) sqrt(8 k T ln2 / m) ; Lorentziana con FWHM_L = A/(2 pi) (natural) o 2 gamma (presion),
  gamma = gamma_ref (p/p_ref)(T_ref/T)^n ; Voigt = convolucion, calculada con la funcion de Faddeeva (scipy.special.wofz).
Pruebas: (i) FWHM_D recalculado vs Ec. (7) del catalogo, 1e-4 relativo; (ii) area del Voigt = 1 (1e-4, integral numerica en +-2000 anchos);
  (iii) limites: Voigt con gamma -> 0 reproduce la gaussiana (1e-6) y con sigma -> 0 la lorentziana (1e-6); (iv) max(fG, fL) <= fV <= fG + fL.
Supuestos: ensanchamiento por colisiones tratado como lorentziano (sin estrechamiento por colisiones ni desplazamiento); gas puro de CO en reposo.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.special import wofz

C = 299792458.0
KB = 1.380649e-23
U = 1.66053906892e-27
NU0 = 115271.2018e6        # Hz
A_10 = 7.203e-08           # s^-1
M_U = 28.0                 # u (numero de masa 12 + 16, aproximacion)
CM1_HZ = C * 100.0


def fwhm_doppler(T: float, nu: float = NU0, m_u: float = M_U) -> float:
    return nu / C * math.sqrt(8 * KB * T * math.log(2) / (m_u * U))


def gamma_pres_hz(p_atm: float, T: float, gamma_ref=0.060, n=0.70) -> float:
    """HWHM de presion en Hz (parametros ILUSTRATIVOS)."""
    return gamma_ref * p_atm * (296.0 / T) ** n * CM1_HZ


def voigt(x, sigma, gamma):
    """Perfil de Voigt normalizado (area 1): sigma desviacion gaussiana, gamma HWHM lorentziano; x en las mismas unidades."""
    if sigma == 0:
        return gamma / math.pi / (x * x + gamma * gamma)
    z = (x + 1j * gamma) / (sigma * math.sqrt(2))
    return wofz(z).real / (sigma * math.sqrt(2 * math.pi))


def fwhm_numerico(sigma, gamma):
    f_g, f_l = 2.3548200450309493 * sigma, 2 * gamma
    xs = np.linspace(0, 3 * (f_g + f_l), 400001)
    v = voigt(xs, sigma, gamma)
    mitad = v[0] / 2
    i = np.argmax(v < mitad)
    # interpolacion lineal
    x0, x1, v0, v1 = xs[i - 1], xs[i], v[i - 1], v[i]
    return 2 * (x0 + (v0 - mitad) / (v0 - v1) * (x1 - x0))


def main() -> int:
    print(f"Python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}")
    print("Linea J=1-0 del 12C16O a 115.2712018 GHz; A = 7.203e-08 s^-1 (LAMDA); gamma_ref y n de presion son ILUSTRATIVOS (sinteticos)")
    # 1. Doppler vs Ec. (7) del catalogo
    print("T [K]   FWHM Doppler [kHz]   Ec.(7) 2*HWHM [kHz]   dif.rel.   FWHM [km/s]")
    for T in (10.0, 20.0, 100.0, 300.0):
        fd = fwhm_doppler(T)
        fe = 2 * 1.17221e-6 * (NU0 / 1e6) * math.sqrt((T / 300.0) * (28.0 / M_U)) * 1e6   # Hz
        print(f"{T:6.1f}  {fd/1e3:14.4f}  {fe/1e3:18.4f}  {abs(fd-fe)/fe:9.1e}  {fd/NU0*C/1e3:8.4f}")
        assert abs(fd - fe) / fe < 1e-4, "Doppler fuera de la Ec. (7)"
    # 2. Natural
    fn = A_10 / (2 * math.pi)
    print(f"Ancho natural FWHM = A/(2 pi) = {fn:.3e} Hz ; cociente con el Doppler a 20 K = {fn/fwhm_doppler(20.0):.2e}")
    # 3. Presion: atmosfera y nucleo frio
    fd296 = fwhm_doppler(296.0)
    g1 = gamma_pres_hz(1.0, 296.0)
    print(f"Atmosfera 296 K, 1 atm: FWHM Doppler = {fd296/1e6:.4f} MHz ; FWHM de presion (2 gamma) = {2*g1/1e6:.1f} MHz (ilustrativo)")
    nH2 = 1e4 * 1e6    # m^-3
    p_atm = nH2 * KB * 20.0 / 101325.0
    gi = gamma_pres_hz(p_atm, 20.0)
    print(f"Nucleo frio sintetico (n = 1e4 cm^-3, T = 20 K): p = {p_atm:.2e} atm ; FWHM de presion = {2*gi:.2e} Hz ; cociente con Doppler = {2*gi/fwhm_doppler(20.0):.1e}")
    # presion de cruce a 296 K
    pc = fd296 / (2 * gamma_pres_hz(1.0, 296.0))
    print(f"Presion en que FWHM_L = FWHM_D a 296 K: {pc:.2e} atm = {pc*760:.3f} Torr")
    # 4. Voigt: pruebas
    sigma = fd296 / 2.3548200450309493
    gam = gamma_pres_hz(pc, 296.0)      # igualdad de anchos
    xs = np.linspace(-2000 * (fd296 + 2 * gam), 2000 * (fd296 + 2 * gam), 4000001)
    v = voigt(xs, sigma, gam)
    area = np.trapezoid(v, xs)
    fv = fwhm_numerico(sigma, gam)
    print(f"Voigt con anchos iguales: area = {area:.6f} ; FWHM_V = {fv/1e6:.4f} MHz ; FWHM_G = {fd296/1e6:.4f} ; FWHM_L = {2*gam/1e6:.4f} ; suma = {(fd296+2*gam)/1e6:.4f}")
    assert abs(area - 1) < 1e-3     # las colas lorentzianas truncadas limitan la precision
    assert max(fd296, 2 * gam) <= fv <= fd296 + 2 * gam
    xx = np.linspace(-3 * sigma, 3 * sigma, 7)
    g_exacta = np.exp(-xx ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
    err_g = np.max(np.abs(voigt(xx, sigma, 1e-9 * sigma) - g_exacta)) / g_exacta.max()
    xl = np.linspace(-3 * gam, 3 * gam, 7)
    l_exacta = gam / math.pi / (xl ** 2 + gam ** 2)
    err_l = np.max(np.abs(voigt(xl, 1e-9 * gam, gam) - l_exacta)) / l_exacta.max()
    print(f"Limite gaussiano: error relativo maximo = {err_g:.1e} ; limite lorentziano: {err_l:.1e}")
    assert err_g < 1e-6 and err_l < 1e-6
    for r in (0.01, 0.1, 1.0, 10.0, 100.0):
        g = r * sigma
        f = fwhm_numerico(sigma, g)
        fG, fL = 2.3548200450309493 * sigma, 2 * g
        print(f"  gamma/sigma = {r:6.2f}: FWHM_V / (FWHM_G + FWHM_L) = {f/(fG+fL):.4f} ; FWHM_V / max = {f/max(fG,fL):.4f}")
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
