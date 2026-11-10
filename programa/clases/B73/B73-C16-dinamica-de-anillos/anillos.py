#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C16: dinamica de anillos de Saturno: limite de Roche, cizalla kepleriana, resonancias de Mimas y ensanchamiento viscoso.

Datos consultados (2026-11-10): masa de Saturno 568.32 x 10^24 kg, radio ecuatorial 60 268 km (NASA/NSSDC, Saturn Fact Sheet, 2025-03-18);
G = 6.67430e-11 (CODATA 2018, citada en el registro de cambios de la tabla de planetas del JPL) -> GM_Saturno ~ 3.7931e7 km3/s2;
semiejes y periodos de Mimas 185.52e3 km y 0.9424218 d, Enceladus 238.02e3 km y 1.370218 d, Tethys 294.66e3 km y 1.887802 d
(NASA/NSSDC, Saturnian Satellite Fact Sheet, 2025-07-22).
ILUSTRATIVOS (no consultados): densidad de las particulas del anillo 920 kg/m3 (hielo), viscosidad cinematica nu = 0.01 y 0.1 m2/s,
anchura del anillo W = 100 km. La densidad media de Saturno se ESTIMA con el radio ecuatorial (cota inferior; no es una densidad publicada).
Modelo: limites de Roche rigido 1.26 R (rho_M/rho_m)^(1/3) y fluido 2.456 R (rho_M/rho_m)^(1/3) (formulas estandar, no consultadas);
criterio de la esfera de Hill de la particula (1.442 R (rho_M/rho_m)^(1/3)); cizalla kepleriana Omega = sqrt(GM/r^3); resonancia p:q con una luna exterior
en r = a_luna (q/p)^(2/3).
Segunda via: (a) tercera ley de Kepler con GM_Saturno frente a los periodos publicados; (b) ensanchamiento viscoso: difusion 1D explicita frente a sigma^2 = sigma0^2 + 2 nu t;
(c) el criterio de Hill debe caer entre el limite rigido y el fluido.
Tolerancias: Kepler dentro del 0.5 % ; difusion 1D dentro del 1 % ; 1.26 < 1.442 < 2.456.
"""
from __future__ import annotations
import json, math, platform, sys

G = 6.67430e-11
M_S = 568.32e24
R_S = 60268.0  # km
GM = G * M_S / 1e9  # km3/s2
LUNAS = {"Mimas": (185.52e3, 0.9424218), "Enceladus": (238.02e3, 1.370218), "Tethys": (294.66e3, 1.887802)}
RHO_M = 920.0
SEG_ANIO = 365.25 * 86400.0


def difusion_1d(sigma0, nu, t_fin, n=801, L=12.0):
    # unidades: sigma0 = 1, longitud L en sigma0
    dx = 2 * L / (n - 1)
    dt = 0.2 * dx * dx / nu
    x = [-L + i * dx for i in range(n)]
    u = [math.exp(-xi * xi / (2 * sigma0**2)) for xi in x]
    t = 0.0
    while t < t_fin:
        h = min(dt, t_fin - t)
        un = u[:]
        for i in range(1, n - 1):
            un[i] = u[i] + nu * h / (dx * dx) * (u[i + 1] - 2 * u[i] + u[i - 1])
        u = un
        t += h
    m0 = sum(u) * dx
    m2 = sum(ui * xi * xi for ui, xi in zip(u, x)) * dx
    return math.sqrt(m2 / m0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print(f"GM_Saturno (deducido de la masa de la ficha y G de CODATA 2018) = {GM:.4e} km3/s2 ; R_ecuatorial = {R_S:.0f} km")
    rho_S = M_S / (4 / 3 * math.pi * (R_S * 1e3) ** 3)
    print(f"Densidad media estimada con el radio ecuatorial (cota inferior) = {rho_S:.0f} kg/m3 ; densidad de particula ILUSTRATIVA = {RHO_M:.0f} kg/m3")
    f = (rho_S / RHO_M) ** (1 / 3)
    rig, flu, hill = 1.26 * f * R_S, 2.456 * f * R_S, 1.442 * f * R_S
    print(f"Limite de Roche: rigido = {rig:,.0f} km ({rig / R_S:.2f} R_S) ; fluido = {flu:,.0f} km ({flu / R_S:.2f} R_S) ; criterio de Hill = {hill:,.0f} km ({hill / R_S:.2f} R_S)")
    out.update(gm=GM, rho_S=rho_S, rig=rig, flu=flu, hill=hill, rig_R=rig / R_S, flu_R=flu / R_S, hill_R=hill / R_S)
    assert rig < hill < flu
    print("Tercera ley de Kepler con GM_Saturno frente al periodo publicado de cada luna:")
    kmax = 0.0
    for nom, (a, P) in LUNAS.items():
        Pk = 2 * math.pi * math.sqrt(a**3 / GM) / 86400
        d = abs(Pk / P - 1)
        kmax = max(kmax, d)
        print(f"  {nom:9s}: P_kepler = {Pk:.6f} d ; P_publicado = {P} d ; diferencia = {d:.3%}")
    out["kmax"] = kmax
    assert kmax < 0.005
    print("Cizalla kepleriana: Omega(r) y tasa de cizalla -(3/2) Omega:")
    for r in (74000.0, 100000.0, 117000.0, 136000.0):
        Om = math.sqrt(GM / r**3)
        P = 2 * math.pi / Om / 3600
        print(f"  r = {r:9,.0f} km ({r / R_S:.2f} R_S): periodo = {P:6.2f} h ; velocidad orbital = {Om * r:.2f} km/s ; cizalla = {1.5 * Om:.3e} 1/s")
    Om100, Om117 = math.sqrt(GM / 100000.0**3), math.sqrt(GM / 117000.0**3)
    out.update(P100=2 * math.pi / Om100 / 3600, v100=Om100 * 100000.0, sh100=1.5 * Om100, P117=2 * math.pi / Om117 / 3600)
    print("Resonancias con lunas exteriores: una particula con periodo P_luna * q/p queda en r = a_luna (q/p)^(2/3):")
    for nom, (a, P) in LUNAS.items():
        for p, q in ((2, 1), (3, 2)):
            r = a * (q / p) ** (2 / 3)
            # comprobacion con Kepler: periodo de una orbita en r
            Pr = 2 * math.pi * math.sqrt(r**3 / GM) / 86400
            print(f"  {nom:9s} {p}:{q}: r = {r:9,.0f} km ({r / R_S:.3f} R_S) ; periodo de la particula = {Pr:.5f} d ; P_luna q/p = {P * q / p:.5f} d ; dif. = {abs(Pr / (P * q / p) - 1):.2%}")
            if nom == "Mimas":
                out[f"res_{p}{q}"] = r
                out[f"resR_{p}{q}"] = r / R_S
    # viscosidad
    print("Ensanchamiento viscoso (ILUSTRATIVO): sigma^2 = sigma0^2 + 2 nu t; difusion 1D explicita frente a la formula:")
    W = 100.0e3  # m
    for nu, tag in ((0.01, "a"), (0.1, "b")):
        tau = W**2 / nu / SEG_ANIO
        out[f"tau_{tag}"] = tau
        print(f"  nu = {nu} m2/s, W = 100 km: W^2/nu = {tau:,.0f} anos")
    # prueba numerica: sigma0 = 1 (unidad), nu = 1, t = 4.5 -> sigma^2 = 1 + 9
    sig = difusion_1d(1.0, 1.0, 4.5)
    teo = math.sqrt(1 + 2 * 1.0 * 4.5)
    print(f"  Prueba numerica (sigma0 = 1, nu = 1, t = 4.5 adimensionales): sigma = {sig:.5f} ; teoria = {teo:.5f} ; diferencia = {abs(sig / teo - 1):.2e}")
    out.update(sig=sig, teo=teo, sigdiff=abs(sig / teo - 1))
    assert abs(sig / teo - 1) < 0.01
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
