#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C14: dispersion del vidrio, aberracion cromatica longitudinal y astigmatismo de un espejo esferico fuera de eje.

Datos: coeficientes de Sellmeier de un vidrio tipo crown (B1 = 1,03961212; B2 = 0,231792344; B3 = 1,01046945; C1 = 0,00600069867; C2 = 0,0200179144;
C3 = 103,560653, C en micras^2) escritos de MEMORIA por el autor del laboratorio: NO se consultaron en esta sesion y se tratan como ILUSTRATIVOS (no como
catalogo de un fabricante). Lineas espectrales F 486,1 nm, d 587,6 nm y C 656,3 nm (valores de libro, no consultados). Focal 1000 mm ilustrativa.
Modelo: n(lambda) por Sellmeier; numero de Abbe V = (nd - 1)/(nF - nC); focal de lente delgada con la misma forma f(lambda) = f_d (nd - 1)/(n(lambda) - 1).
Segunda via: la aberracion cromatica longitudinal se compara con la formula f/V. Astigmatismo: se trazan rayos finos (diferencias finitas) en un espejo esferico
a un angulo de campo t y se halla donde se enfocan los planos tangencial y sagital, frente a f_t = (R/2) cos t y f_s = R/(2 cos t).
Supuestos: lente delgada, rayos paraxiales (crom.); haz delgado y espejo esferico (astig.). Validez: tercer orden.
Tolerancia: dispersion f/V 3 % (relacion del segundo orden); focos tangencial y sagital frente a formulas 1e-4 relativo.
"""
from __future__ import annotations
import math, platform, sys

B = (1.03961212, 0.231792344, 1.01046945)
Cc = (0.00600069867, 0.0200179144, 103.560653)


def n_de(lam_nm):
    l2 = (lam_nm / 1000.0) ** 2
    return math.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(B, Cc)))


def foco_espejo(R, t, plano):
    """Intersecciones de un rayo principal con rayos vecinos de un haz fino (esfera de radio R, vertice en 0, concavo hacia +z). Devuelve distancia
    al punto de impacto del rayo principal en el rayo reflejado."""
    # rayo principal con inclinacion t llega al vertice (0,0). Rayos vecinos desplazados dh perpendicularmente en el plano tangencial o fuera del plano (sagital).
    dh = 1e-4
    if plano == "t":
        # dos rayos paralelos en el plano x-z, desplazados +-dh perpendicular a la direccion del rayo
        res = []
        for s in (-dh, dh):
            d = (math.sin(t), -math.cos(t))
            # parametrizar: punto de partida = -5000*d + s*perp, perp = (cos t, sin t)
            p0 = (-5000 * d[0] + s * math.cos(t), -5000 * d[1] + s * math.sin(t))
            # interseccion con la esfera: centro (0, R), |p - c| = R, tomar la raiz del casquete inferior (vertice)
            ox, oz = p0[0], p0[1] - R
            b = ox * d[0] + oz * d[1]
            cc = ox * ox + oz * oz - R * R
            tt = -b + math.sqrt(b * b - cc)
            q = (p0[0] + tt * d[0], p0[1] + tt * d[1])
            n = ((q[0]) / R, (q[1] - R) / R)
            kdn = d[0] * n[0] + d[1] * n[1]
            r = (d[0] - 2 * kdn * n[0], d[1] - 2 * kdn * n[1])
            res.append((q, r))
        (q1, r1), (q2, r2) = res
        # interseccion de los dos rayos reflejados
        det = r1[0] * (-r2[1]) - r1[1] * (-r2[0])
        u = ((q2[0] - q1[0]) * (-r2[1]) - (q2[1] - q1[1]) * (-r2[0])) / det
        punto = (q1[0] + u * r1[0], q1[1] + u * r1[1])
        return math.hypot(punto[0], punto[1])
    else:
        # sagital: dos rayos desplazados +-dh en y (fuera del plano), simetricos; se cortan en el plano x-z del rayo principal
        res = []
        d = (math.sin(t), 0.0, -math.cos(t))
        for s in (-dh, dh):
            p0 = (-5000 * d[0], s, -5000 * d[2])
            ox, oy, oz = p0[0], p0[1], p0[2] - R
            b = ox * d[0] + oy * d[1] + oz * d[2]
            cc = ox * ox + oy * oy + oz * oz - R * R
            tt = -b + math.sqrt(b * b - cc)
            q = (p0[0] + tt * d[0], p0[1] + tt * d[1], p0[2] + tt * d[2])
            n = (q[0] / R, q[1] / R, (q[2] - R) / R)
            kdn = d[0] * n[0] + d[1] * n[1] + d[2] * n[2]
            r = tuple(d[i] - 2 * kdn * n[i] for i in range(3))
            res.append((q, r))
        (q1, r1), (q2, r2) = res
        # corte con y = 0: u tal que q1y + u r1y = 0
        u = -q1[1] / r1[1]
        punto = tuple(q1[i] + u * r1[i] for i in range(3))
        return math.sqrt(punto[0] ** 2 + punto[1] ** 2 + punto[2] ** 2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nF, nd, nC = n_de(486.1), n_de(587.6), n_de(656.3)
    V = (nd - 1) / (nF - nC)
    print(f"nF = {nF:.5f} ; nd = {nd:.5f} ; nC = {nC:.5f} ; V = {V:.2f}")
    assert 60 < V < 68
    fd = 1000.0
    print(f"{'lambda [nm]':>12} {'n':>9} {'f [mm]':>10} {'f - f_d [mm]':>13}")
    focos = {}
    for lam in (400.0, 486.1, 550.0, 587.6, 656.3, 800.0):
        n = n_de(lam)
        f = fd * (nd - 1) / (n - 1)
        focos[lam] = f
        print(f"{lam:12.1f} {n:9.5f} {f:10.3f} {f-fd:13.3f}")
    dF = focos[486.1] - focos[656.3]
    print(f"separacion focal F-C = {-dF:.3f} mm ; f/V = {fd/V:.3f} mm ; razon = {-dF/(fd/V):.4f}")
    assert abs(-dF / (fd / V) - 1) < 0.03
    # tamano del disco cromatico para f/10 (D = 100 mm)
    D = 100.0
    disco = abs(dF) * D / fd
    print(f"disco cromatico (f/10, F-C) = {disco*1e3:.1f} micras ; disco de Airy a 550 nm = {2.44*550e-6*10*1e3:.1f} micras ; razon = {disco/(2.44*550e-6*10):.1f}")
    # criterio de Conrady-like: longitud focal para limitar el error cromatico a 4 lambda N^2 (profundidad de foco ~ 4 lambda N^2)
    print(f"profundidad de enfoque total 4 lambda N^2 (f/10) = {4*550e-6*100:.3f} mm ; dispersion F-C = {abs(dF):.3f} mm")
    # astigmatismo
    R = 2000.0
    print(f"espejo esferico R = {R:.0f} mm : foco paraxial {R/2:.1f} mm")
    print(f"{'t [deg]':>8} {'f_tang [mm]':>12} {'(R/2)cos t':>12} {'f_sag [mm]':>12} {'R/(2cos t)':>12} {'f_s - f_t [mm]':>15}")
    for gd in (1.0, 3.0, 5.0, 8.0):
        t = math.radians(gd)
        ft = foco_espejo(R, t, "t")
        fs = foco_espejo(R, t, "s")
        ft_f, fs_f = R / 2 * math.cos(t), R / (2 * math.cos(t))
        print(f"{gd:8.1f} {ft:12.4f} {ft_f:12.4f} {fs:12.4f} {fs_f:12.4f} {fs-ft:15.4f}")
        assert abs(ft - ft_f) / ft_f < 1e-4 and abs(fs - fs_f) / fs_f < 1e-4
    # aproximacion de tercer orden: separacion ~ R t^2 / 2 (con R/2 foco)
    t = math.radians(5.0)
    print(f"a 5 grados: separacion = {foco_espejo(R,t,'s')-foco_espejo(R,t,'t'):.4f} mm ; (R/2) t^2 = {R/2*t*t:.4f} mm")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
