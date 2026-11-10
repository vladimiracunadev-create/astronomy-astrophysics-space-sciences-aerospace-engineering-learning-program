#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C22. Propagacion ionosferica y comunicaciones HF: frecuencia de plasma, frecuencia critica foF2, frecuencia maxima utilizable (MUF)
por la ley de la secante en geometria esferica y efecto de una tormenta (reduccion de la densidad de electrones).
Densidades y alturas SINTETICAS/ILUSTRATIVAS; la relacion f_p = 8.98 sqrt(N) y la ley de la secante son relaciones estandar NO consultadas."""
import math, sys

RE = 6371.0     # km ILUSTRATIVO
HF2 = 300.0     # km, altura de la capa F2, ILUSTRATIVA
A_PLASMA = 8.98  # Hz m^1.5, relacion estandar no consultada

def fplasma(n_m3):
    return A_PLASMA * math.sqrt(n_m3)

def muf_esfera(fo, d_km, h=HF2):
    th = d_km / (2 * RE)       # semiangulo central
    beta = math.atan2(math.cos(th) - RE / (RE + h), math.sin(th))   # elevacion de salida
    sin_phi = RE * math.cos(beta) / (RE + h)
    phi = math.asin(sin_phi)
    return fo / math.cos(phi), math.degrees(beta), math.degrees(phi)

def muf_esfera_2(fo, d_km, h=HF2):
    """Segunda via: angulo de incidencia por ley de los senos en el triangulo centro-estacion-punto de reflexion."""
    th = d_km / (2 * RE)
    # distancia estacion - punto de reflexion
    r1, r2 = RE, RE + h
    L = math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * math.cos(th))
    # angulo en el punto de reflexion entre la vertical (al centro) y la direccion a la estacion
    sin_phi = r1 * math.sin(th) / L
    phi = math.asin(sin_phi)
    return fo / math.cos(phi), math.degrees(phi)

def calcular():
    R = {}
    R["n_dia"], R["n_noche"], R["n_tormenta"] = 1.0e12, 2.0e11, 4.0e11   # m^-3, SINTETICOS
    R["fo"] = {k: fplasma(R[k]) for k in ("n_dia", "n_noche", "n_tormenta")}
    dists = (500.0, 1000.0, 2000.0, 3000.0, 3500.0)
    R["muf"] = {d: {k: muf_esfera(R["fo"][k], d)[0] for k in R["fo"]} for d in dists}
    R["angulos"] = {d: muf_esfera(R["fo"]["n_dia"], d)[1:] for d in dists}
    R["dif"] = max(abs(muf_esfera(R["fo"]["n_dia"], d)[0] - muf_esfera_2(R["fo"]["n_dia"], d)[0]) for d in dists)
    R["plano_1000"] = R["fo"]["n_dia"] / math.cos(math.atan(500.0 / HF2))   # tierra plana a 1000 km
    R["cobertura_dia_hf"] = {d: R["muf"][d]["n_tormenta"] / R["muf"][d]["n_dia"] for d in dists}
    R["salto_max"] = None
    # distancia de salto maxima (elevacion 0) para el dia
    th0 = math.acos(RE / (RE + HF2))
    R["salto_max"] = 2 * RE * th0
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: N_max dia = 1e12 m^-3, noche = 2e11, tormenta = 4e11 ; capa F2 a 300 km (ilustrativo)")
    for k, v in R["fo"].items():
        print(f"  {k:10s}: foF2 = 8.98 sqrt(N) = {v/1e6:6.3f} MHz")
    print(f"{'D [km]':>8s}{'elev. [deg]':>13s}{'inc. [deg]':>12s}{'MUF dia':>10s}{'MUF noche':>11s}{'MUF tormenta':>14s}   [MHz]")
    for d, m in R["muf"].items():
        b, p = R["angulos"][d]
        print(f"{d:8.0f}{b:13.2f}{p:12.2f}{m['n_dia']/1e6:10.2f}{m['n_noche']/1e6:11.2f}{m['n_tormenta']/1e6:14.2f}")
    print(f"Diferencia entre las dos formas de calcular la MUF = {R['dif']:.2e} Hz")
    print(f"Tierra plana a 1000 km: MUF = {R['plano_1000']/1e6:.2f} MHz (esfera: {R['muf'][1000.0]['n_dia']/1e6:.2f} MHz)")
    print(f"Distancia maxima de un salto (elevacion 0) = {R['salto_max']:.0f} km")
    assert R["dif"] < 1.0 and R["salto_max"] > 3000
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
