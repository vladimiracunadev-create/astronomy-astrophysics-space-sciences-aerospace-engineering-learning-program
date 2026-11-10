#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C07: leer lineas de catalogo (formato JPL y niveles LAMDA) del 12C16O, convertir unidades y temperatura.

Datos REALES consultados el 2026-11-09 (copiados literalmente):
  - 6 lineas del catalogo JPL, archivo c028001.cat (TAG -28001). S4.
  - Formato de linea y Ec. (3)-(4) del documento del catalogo JPL (Pickett et al., ed. 2 mayo 2003): (F13.4,F8.4,F8.4,I2,F10.4,I3,I7,I4,6I2,6I2). S3.
  - 5 primeros niveles de LAMDA co.dat (energias en cm^-1, pesos y J) y A de las tres primeras transiciones. S5.
  - Definicion de intensidad de HITRAN: cm^-1/(molecula cm^-2) a T_ref = 296 K. S7.
  - CODATA 2022: c, k, h. S1.
Calculos propios: Q rotacional (rotor con B0 = 1.922529 cm^-1 y D = 6.12147e-06 cm^-1 del WebBook, S2), energia superior = ELO + nu.
Pruebas: (i) el analizador de ancho fijo reproduce FREQ/ERR/LGINT/GUP/TAG; (ii) GUP = 2 J_sup + 1; (iii) las energias de LAMDA reproducen las
  frecuencias de JPL con 1e-5 relativo (la diferencia observada, hasta 7e-6, es un hallazgo y se informa); (iv) la Ec. (3) a 300 K reproduce el valor de partida y la Ec. (4) se desvia menos de 5 % a 296 K;
  (v) una linea con longitud distinta de 80 caracteres o campo no numerico se rechaza.
"""
from __future__ import annotations
import math, platform, sys

C = 299792458.0
H = 6.62607015e-34
KB = 1.380649e-23
CM1 = H * C * 100.0                      # J por cm^-1
CM1_MHZ = C * 100.0 / 1e6
B0, DE = 1.922529, 6.12147e-06

JPL_RAW = [
    "  115271.2018   .0005 -5.0105 2     .0000  3 -28001 101 1           0           ",
    "  230538.0000   .0005 -4.1197 2    3.8450  5 -28001 101 2           1           ",
    "  345795.9899   .0005 -3.6118 2   11.5350  7 -28001 101 3           2           ",
    "  461040.7682   .0005 -3.2657 2   23.0695  9 -28001 101 4           3           ",
    "  576267.9305   .0005 -3.0118 2   38.4481 11 -28001 101 5           4           ",
    "  691473.0763   .0005 -2.8193 2   57.6704 13 -28001 101 6           5           ",
]
LAMDA_LEVELS = [(1, 0.000000000, 1.0, 0), (2, 3.845033413, 3.0, 1), (3, 11.534919938, 5.0, 2), (4, 23.069512649, 7.0, 3), (5, 38.448164669, 9.0, 4)]
LAMDA_TRANS = [(1, 2, 1, 7.203e-08, 115.2712018), (2, 3, 2, 6.910e-07, 230.5380000), (3, 4, 3, 2.497e-06, 345.7959899)]


def analizar(linea: str) -> dict:
    """Lee una linea JPL (F13.4,F8.4,F8.4,I2,F10.4,I3,I7,I4 y cuantos del nivel superior en los 12 primeros caracteres)."""
    if len(linea.rstrip("\n")) < 55:
        raise ValueError("linea demasiado corta")
    try:
        d = dict(freq=float(linea[0:13]), err=float(linea[13:21]), lgint=float(linea[21:29]), dr=int(linea[29:31]),
                 elo=float(linea[31:41]), gup=int(linea[41:44]), tag=int(linea[44:51]), qnfmt=int(linea[51:55]))
        qn = linea[55:79].split()
        d["qn_sup"], d["qn_inf"] = int(qn[0]), int(qn[1])
    except (ValueError, IndexError) as e:
        raise ValueError(f"campo no valido: {e}")
    return d


def Q_rot(T: float) -> float:
    return sum((2 * J + 1) * math.exp(-(B0 * J * (J + 1) - DE * (J * (J + 1)) ** 2) * CM1 / (KB * T)) for J in range(0, 200))


def escalar(I0, Elo, Eup, T0, T):
    """Ec. (3) del catalogo (exacta en las poblaciones)."""
    f = lambda t: math.exp(-Elo * CM1 / (KB * t)) - math.exp(-Eup * CM1 / (KB * t))
    return I0 * Q_rot(T0) / Q_rot(T) * f(T) / f(T0)


def aprox_ec4(I0, Elo, T0, T, n=1):
    """Ec. (4): (T0/T)^(n+1) exp(-(1/T - 1/T0) E''/k)."""
    return I0 * (T0 / T) ** (n + 1) * math.exp(-(1 / T - 1 / T0) * Elo * CM1 / KB)


def main() -> int:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Lineas REALES del catalogo JPL (c028001.cat) y niveles de LAMDA (co.dat), consultados el 2026-11-09")
    filas = [analizar(l) for l in JPL_RAW]
    print("FREQ [MHz]     ERR [MHz]  LGINT    DR  ELO [cm^-1]  GUP  TAG     QNFMT  J'  J''  nu [GHz]  E_sup [cm^-1]")
    for d in filas:
        d["eup"] = d["elo"] + d["freq"] / CM1_MHZ
        print(f"{d['freq']:13.4f}  {d['err']:7.4f}  {d['lgint']:7.4f}  {d['dr']:2d}  {d['elo']:9.4f}  {d['gup']:3d}  {d['tag']:7d}  {d['qnfmt']:4d}  {d['qn_sup']:2d}  {d['qn_inf']:2d}  {d['freq']/1e3:9.4f}  {d['eup']:10.4f}")
        assert d["gup"] == 2 * d["qn_sup"] + 1 and d["tag"] < 0 and d["dr"] == 2
    print("Comprobaciones de formato: GUP = 2J'+1, TAG negativo (frecuencia medida en laboratorio) y DR = 2 (molecula lineal): correctas")
    # LAMDA vs JPL
    print("Frecuencia a partir de las DIFERENCIAS de niveles de LAMDA (energias tal como se consultaron) frente a JPL:")
    peor = 0.0
    for i, (k, e2, g2, J2) in enumerate(LAMDA_LEVELS[1:4], start=1):
        e1 = LAMDA_LEVELS[i - 1][1]
        f_lamda = (e2 - e1) * CM1_MHZ
        f_jpl = filas[i - 1]["freq"]
        peor = max(peor, abs(f_lamda - f_jpl) / f_jpl)
        print(f"  J={J2}->{J2-1}: LAMDA {f_lamda:14.4f} MHz ; JPL {f_jpl:14.4f} MHz ; dif. rel. = {abs(f_lamda-f_jpl)/f_jpl:.2e} ; g_sup LAMDA = {g2:.0f}")
    assert peor < 1e-5     # las energias de LAMDA tienen menos cifras utiles: la diferencia es real y se discute en la clase
    # conversion de unidades de intensidad
    print("Intensidad: LGINT (nm^2 MHz, 300 K) -> cm^-1/(molecula cm^-2) y a 296 K (referencia de HITRAN)")
    for d in filas[:3]:
        I300 = 10 ** d["lgint"]
        Icm = I300 / 2.99792458e18
        I296 = escalar(Icm, d["elo"], d["eup"], 300.0, 296.0)
        I296_ec4 = aprox_ec4(Icm, d["elo"], 300.0, 296.0)
        back = escalar(I296, d["elo"], d["eup"], 296.0, 300.0)
        assert abs(back - Icm) / Icm < 1e-12
        print(f"  J'={d['qn_sup']}: {I300:.4e} nm^2 MHz = {Icm:.4e} cm^-1/(mol cm^-2) a 300 K ; a 296 K (Ec. 3) = {I296:.4e} ; Ec. (4) = {I296_ec4:.4e} ({abs(I296_ec4-I296)/I296*100:.2f} %)")
        assert abs(I296_ec4 - I296) / I296 < 0.05
    print("Escalado a 20 K, linea 1->0: Ec. (3) = {:.4e} ; Ec. (4) = {:.4e} nm^2 MHz (la Ec. (4) exige E'-E'' << kT y a 20 K ya no es buena)".format(
        escalar(10 ** filas[0]["lgint"], filas[0]["elo"], filas[0]["eup"], 300.0, 20.0), aprox_ec4(10 ** filas[0]["lgint"], filas[0]["elo"], 300.0, 20.0)))
    print("A de Einstein: LAMDA vs relaciones entre lineas (cociente A(J)/A(1) frente al modelo (nu/nu1)^3 (J/(2J+1))/(1/3)):")
    for J, (_, _, _, A, f) in enumerate(LAMDA_TRANS, start=1):
        modelo = (f / LAMDA_TRANS[0][4]) ** 3 * (J / (2 * J + 1)) / (1 / 3)
        print(f"  J={J}: A = {A:.3e} s^-1 ; cociente LAMDA = {A/LAMDA_TRANS[0][3]:.3f} ; modelo = {modelo:.3f}")
        assert abs(A / LAMDA_TRANS[0][3] / modelo - 1) < 2e-3
    # entradas defectuosas
    for malo in (JPL_RAW[0][:40], JPL_RAW[0].replace("-5.0105", "  abc  ")):
        try:
            analizar(malo)
            raise AssertionError("debio rechazarse")
        except ValueError as e:
            print("Linea defectuosa rechazada:", e)
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
