#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C19: presupuesto de potencia de mision por fases con reservas de crecimiento segun madurez (satelite SINTETICO).

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC) para el periodo y el eclipse de una orbita de 600 km con beta = 0.
Las reservas por madurez NO se tomaron de una norma: los porcentajes (5 %, 15 %, 30 %) son ILUSTRATIVOS; no se consulto el estandar de masa y potencia de la AIAA ni el manual de ingenieria
de sistemas de la NASA en esta clase.
ILUSTRATIVOS (sinteticos): cargas por subsistema y fase, reserva de sistema 10 % sobre el total con crecimiento, potencia BOL del ala 286.67 W normal al Sol (B86-C14), factor de fin de vida
0.8858 a 5 anos (B86-C14), eficiencias de camino Xd = 0.85 y Xe = 0.65 (B86-C01), fase LEOP con el ala al 50 %, 20000 ensayos Monte Carlo con semilla 20261110.
Modelo: P_modo = suma_i P_i (1 + c_i) (1 + r_sist); P_sa = (P_e T_e / X_e + P_d T_d / X_d) / T_d; margen = (P_gen - P_sa)/P_sa.
Segunda via: Monte Carlo donde cada carga toma un crecimiento uniforme en [0, c_i]; se mide la probabilidad de que la demanda de potencia de ala supere la generacion.
Tolerancia: suma de contribuciones de subsistemas igual al total con residuo < 1e-9 W.
"""
from __future__ import annotations
import math, platform, random

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
TE = math.asin(RE / A) / math.pi * T
TD = T - TE
XD, XE, R_SIST = 0.85, 0.65, 0.10
P_BOL, F_EOL5 = 286.67, 0.8858
CREC = {"comercial": 0.05, "modificado": 0.15, "nuevo": 0.30}
# subsistema: (madurez, {modo: (P_luz, P_eclipse)})
SUBS = {
    "Ordenador de a bordo": ("comercial", {"nominal": (12.0, 12.0), "LEOP": (12.0, 12.0), "seguro": (8.0, 8.0)}),
    "Control de actitud": ("modificado", {"nominal": (20.0, 20.0), "LEOP": (25.0, 25.0), "seguro": (6.0, 6.0)}),
    "Radio": ("modificado", {"nominal": (18.0, 6.0), "LEOP": (10.0, 6.0), "seguro": (4.0, 4.0)}),
    "Carga util": ("nuevo", {"nominal": (30.0, 0.0), "LEOP": (0.0, 0.0), "seguro": (0.0, 0.0)}),
    "Termica": ("comercial", {"nominal": (4.0, 16.0), "LEOP": (6.0, 18.0), "seguro": (8.0, 20.0)}),
    "Despliegue": ("nuevo", {"nominal": (0.0, 0.0), "LEOP": (15.0, 0.0), "seguro": (0.0, 0.0)}),
}
FASES = {  # modo, potencia de ala disponible [W]
    "LEOP": ("LEOP", 0.5 * P_BOL),
    "Nominal inicio de vida": ("nominal", P_BOL),
    "Nominal fin de vida (5 anos)": ("nominal", P_BOL * F_EOL5),
    "Modo seguro fin de vida": ("seguro", P_BOL * F_EOL5),
}


def demanda(modo, luz=True, crecer=True):
    tot = 0.0
    filas = []
    for n, (mad, modos) in SUBS.items():
        p = modos[modo][0 if luz else 1]
        c = CREC[mad] if crecer else 0.0
        v = p * (1.0 + c)
        filas.append((n, mad, p, c, v))
        tot += v
    return filas, tot * (1.0 + R_SIST) if crecer else tot


def p_ala(pd, pe):
    return (pe * TE / XE + pd * TD / XD) / TD


def resultados():
    r = dict(T=T, Te=TE, Td=TD)
    fn, tot_n = demanda("nominal", True)
    r["filas_nom"] = fn
    r["P_d_nom"] = tot_n
    r["P_d_nom_sin"] = demanda("nominal", True, False)[1]
    r["P_e_nom"] = demanda("nominal", False)[1]
    r["P_e_nom_sin"] = demanda("nominal", False, False)[1]
    r["resid"] = abs(sum(f[4] for f in fn) * (1.0 + R_SIST) - tot_n)
    r["crec_total_pct"] = (r["P_d_nom"] / r["P_d_nom_sin"] - 1.0) * 100.0
    fases = []
    for nombre, (modo, pgen) in FASES.items():
        pd, pe = demanda(modo, True)[1], demanda(modo, False)[1]
        psa = p_ala(pd, pe)
        fases.append((nombre, pd, pe, psa, pgen, (pgen - psa) / psa * 100.0))
    r["fases"] = fases
    for k, f in enumerate(fases):
        r[f"fase{k}_psa"], r[f"fase{k}_pgen"], r[f"fase{k}_m"] = f[3], f[4], f[5]
    r["margen_min"] = min(f[5] for f in fases)
    r["fase_min"] = min(fases, key=lambda f: f[5])[0]
    # Monte Carlo del caso nominal fin de vida
    rng = random.Random(20261110)
    n, exc = 20000, 0
    pgen = P_BOL * F_EOL5
    psas = []
    for _ in range(n):
        pd = pe = 0.0
        for nm, (mad, modos) in SUBS.items():
            g = rng.uniform(0.0, CREC[mad])
            pd += modos["nominal"][0] * (1.0 + g)
            pe += modos["nominal"][1] * (1.0 + g)
        psa = p_ala(pd * (1.0 + R_SIST), pe * (1.0 + R_SIST))
        psas.append(psa)
        exc += psa > pgen
    psas.sort()
    r["mc_media"], r["mc_p95"], r["mc_max"] = sum(psas) / n, psas[int(0.95 * n)], psas[-1]
    r["mc_prob_exceso"] = exc / n
    r["psa_det"] = r["fase2_psa"]
    r["pgen_eol"] = pgen
    for k, f in enumerate(fn):
        r[f"c{k+1}"] = f[4]
    r["c4_sys"] = fn[3][4] * (1.0 + R_SIST)
    for k, f in enumerate(fases):
        r[f"f{k}_pd"], r[f"f{k}_pe"] = f[1], f[2]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA 600 km: T = {T:.1f} s ; eclipse = {TE:.1f} s ; luz = {TD:.1f} s")
    print("Modo nominal en luz (crecimiento por madurez = 5 % comercial, 15 % modificado, 30 % nuevo):")
    print(" subsistema              madurez      P [W]  crec.   con crec. [W]")
    for n, mad, p, c, v in r["filas_nom"]:
        print(f" {n:<22} {mad:<11} {p:6.1f}  {c*100:4.0f} %   {v:10.3f}")
    print(f"Suma con crecimiento = {sum(f[4] for f in r['filas_nom']):.3f} W ; con reserva de sistema {R_SIST*100:.0f} % = {r['P_d_nom']:.3f} W (sin reservas {r['P_d_nom_sin']:.1f} W ; +{r['crec_total_pct']:.1f} %) ; eclipse = {r['P_e_nom']:.3f} W")
    print(f"Residuo de la suma de contribuciones = {r['resid']:.1e} W")
    print(" fase                              P_luz [W]  P_ecl [W]  P_ala req. [W]  P_ala disp. [W]  margen [%]")
    for n, pd, pe, psa, pg, m in r["fases"]:
        print(f" {n:<32} {pd:9.2f}  {pe:9.2f}  {psa:13.2f}  {pg:15.2f}  {m:9.1f}")
    print(f"Margen minimo = {r['margen_min']:.1f} % en la fase '{r['fase_min']}'")
    print(f"Monte Carlo (nominal fin de vida): media = {r['mc_media']:.2f} W ; p95 = {r['mc_p95']:.2f} W ; maximo = {r['mc_max']:.2f} W ; P(demanda > generacion) = {r['mc_prob_exceso']:.4f}")
    print(f"Determinista con crecimiento maximo = {r['psa_det']:.2f} W frente a Monte Carlo maximo = {r['mc_max']:.2f} W")
    assert r["resid"] < 1e-9
    assert r["mc_max"] <= r["psa_det"] + 1e-9, "el caso determinista con crecimiento maximo es una cota superior del Monte Carlo"
    assert r["mc_media"] < r["psa_det"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
