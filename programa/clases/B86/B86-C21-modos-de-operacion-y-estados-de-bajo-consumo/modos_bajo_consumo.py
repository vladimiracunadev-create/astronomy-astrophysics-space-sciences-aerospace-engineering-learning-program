#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C21: modos de operacion y estados de bajo consumo con umbrales de SOC e histeresis (satelite SINTETICO).

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC) para el periodo y el eclipse de una orbita de 600 km con beta = 0.
ILUSTRATIVOS (sinteticos): tres modos con cargas (luz, eclipse) de nominal (100.8 W, 64.8 W), reducido (60.8 W, 44.8 W; carga util apagada) y seguro (30 W, 30 W);
generacion constante en luz de 125 W (caso de ala degradada o beta alto), bateria de 259.2 Wh, eficiencias 0.97 y 0.95, carga maxima 70 W, SOC inicial 80 %,
umbrales de la politica con histeresis: bajar a reducido si SOC < 40 %, a seguro si SOC < 25 %, volver a nominal si SOC > 60 % y de seguro a reducido si SOC > 45 %;
politica sin histeresis: nominal si SOC >= 50 % y reducido en otro caso. Duracion de la simulacion: 30 dias; paso de 10 s.
Modelo: balance de energia como en B86-C13 con la carga del modo vigente en cada paso.
Segunda via: fraccion de tiempo en nominal predicha del balance de energia por orbita (deficit del modo nominal frente a excedente del reducido) frente a la simulada.
Tolerancia: fraccion nominal simulada frente a la predicha < 8 puntos porcentuales (la prediccion supone modos constantes durante toda la orbita); balance de energia con residuo < 1e-6 Wh.
"""
from __future__ import annotations
import math, platform

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
TE = math.asin(RE / A) / math.pi * T
TD = T - TE
E_NOM, ETA_C, ETA_D, P_CHG, P_GEN = 259.2, 0.97, 0.95, 70.0, 125.0
MODOS = {"nominal": (100.8, 64.8), "reducido": (60.8, 44.8), "seguro": (30.0, 30.0)}
DIAS = 30


def politica_histeresis(modo, soc):
    if modo == "nominal":
        return "seguro" if soc < 0.25 else ("reducido" if soc < 0.40 else "nominal")
    if modo == "reducido":
        return "seguro" if soc < 0.25 else ("nominal" if soc > 0.60 else "reducido")
    return "reducido" if soc > 0.45 else "seguro"


def politica_simple(modo, soc):
    return "nominal" if soc >= 0.50 else "reducido"


def politica_ninguna(modo, soc):
    return "nominal"


def simular(politica, dt=10.0, soc0=0.8):
    e = soc0 * E_NOM
    modo = "nominal"
    t_modo = dict.fromkeys(MODOS, 0.0)
    trans, soc_min, agotada = 0, 1.0, None
    gen = carga = perd = desc = 0.0
    e0 = e
    n_orb = int(DIAS * 86400.0 / T)
    for k in range(n_orb):
        t = 0.0
        while t < T - 1e-9:
            h = min(dt, (TD if t < TD else T) - t)
            hh = h / 3600.0
            nuevo = politica(modo, e / E_NOM)
            if nuevo != modo:
                trans += 1
                modo = nuevo
            luz = t < TD
            pl = MODOS[modo][0 if luz else 1]
            t_modo[modo] += h
            carga += pl * hh
            if luz:
                gen += P_GEN * hh
                s = P_GEN - pl
                if s >= 0.0:
                    pc = min(s, P_CHG, (E_NOM - e) / (ETA_C * hh))
                    e += pc * ETA_C * hh
                    perd += pc * (1.0 - ETA_C) * hh
                    desc += (s - pc) * hh
                else:
                    e -= -s / ETA_D * hh
                    perd += -s * (1.0 / ETA_D - 1.0) * hh
            else:
                e -= pl / ETA_D * hh
                perd += pl * (1.0 / ETA_D - 1.0) * hh
            if e <= 0.0:
                return dict(agotada=(k + 1, k * T / 86400.0), trans=trans, t_modo=t_modo, soc_min=0.0, resid=0.0, n_orb=n_orb)
            soc_min = min(soc_min, e / E_NOM)
            t += h
    resid = abs(gen - (carga + perd + desc + (e - e0)))
    return dict(agotada=None, trans=trans, t_modo=t_modo, soc_min=soc_min, resid=resid, n_orb=n_orb, soc_fin=e / E_NOM, carga=carga, gen=gen)


def resultados():
    r = {}
    ninguna, simple, hist = simular(politica_ninguna), simular(politica_simple), simular(politica_histeresis)
    r["n_orb"] = hist["n_orb"]
    r["ning_orb"], r["ning_dias"] = ninguna["agotada"]
    for pre, x in (("s", simple), ("h", hist)):
        tot = sum(x["t_modo"].values())
        for m in MODOS:
            r[f"{pre}_{m}_pct"] = 100.0 * x["t_modo"][m] / tot
        r[f"{pre}_trans"] = x["trans"]
        r[f"{pre}_soc_min"] = x["soc_min"] * 100.0
        r[f"{pre}_resid"] = x["resid"]
        r[f"{pre}_carga_med"] = x["carga"] / (tot / 3600.0)
    # energia por orbita de cada modo (modo constante) y fraccion nominal predicha
    def delta(modo):
        pl, pe = MODOS[modo]
        ganado = min(P_GEN - pl, P_CHG) * ETA_C * TD / 3600.0 if P_GEN > pl else (P_GEN - pl) / ETA_D * TD / 3600.0
        gastado = pe / ETA_D * TE / 3600.0
        return ganado - gastado
    r["d_nom"], r["d_red"], r["d_seg"] = delta("nominal"), delta("reducido"), delta("seguro")
    f_pred = r["d_red"] / (r["d_red"] - r["d_nom"])
    r["f_pred_pct"] = 100.0 * f_pred
    # el tiempo en "seguro" es nulo: el reparto nominal/reducido define la fraccion
    sim_nom = r["h_nominal_pct"] / (r["h_nominal_pct"] + r["h_reducido_pct"])
    r["f_sim_pct"] = 100.0 * sim_nom
    r["dif_pp"] = abs(r["f_sim_pct"] - r["f_pred_pct"])
    r["P_med_nom_ref"] = (MODOS["nominal"][0] * TD + MODOS["nominal"][1] * TE) / T
    r["P_med_red_ref"] = (MODOS["reducido"][0] * TD + MODOS["reducido"][1] * TE) / T
    r["P_med_seg_ref"] = (MODOS["seguro"][0] * TD + MODOS["seguro"][1] * TE) / T
    r["d_nom_abs"] = abs(r["d_nom"])
    r["ratio_trans"] = r["s_trans"] / max(1, r["h_trans"])
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA 600 km: T = {T:.1f} s ; eclipse = {TE:.1f} s ; generacion en luz = {P_GEN} W ; {r['n_orb']} orbitas en {DIAS} dias")
    print(" modo        P luz [W]  P eclipse [W]  P media por orbita [W]  delta de energia por orbita [Wh]")
    for m, p, d in (("nominal", r["P_med_nom_ref"], r["d_nom"]), ("reducido", r["P_med_red_ref"], r["d_red"]), ("seguro", r["P_med_seg_ref"], r["d_seg"])):
        print(f" {m:<10} {MODOS[m][0]:9.1f}  {MODOS[m][1]:13.1f}  {p:22.2f}  {d:+30.2f}")
    print(f"Sin politica (siempre nominal): la bateria se agota en la orbita {r['ning_orb']} (dia {r['ning_dias']:.2f})")
    print(" politica         transiciones  SOC min [%]  nominal [%]  reducido [%]  seguro [%]  P media [W]  residuo [Wh]")
    for pre, n in (("s", "umbral unico 50 %"), ("h", "histeresis 40/60 %")):
        print(f" {n:<17} {r[pre+'_trans']:10d}  {r[pre+'_soc_min']:11.2f}  {r[pre+'_nominal_pct']:11.2f}  {r[pre+'_reducido_pct']:12.2f}  {r[pre+'_seguro_pct']:10.2f}  {r[pre+'_carga_med']:11.2f}  {r[pre+'_resid']:.1e}")
    print(f"Fraccion nominal/(nominal+reducido) con histeresis: simulada = {r['f_sim_pct']:.2f} % ; predicha del balance = {r['f_pred_pct']:.2f} % ; diferencia = {r['dif_pp']:.2f} puntos")
    print(f"Transiciones sin histeresis / con histeresis = {r['ratio_trans']:.1f}")
    assert r["ning_orb"] is not None
    assert r["h_resid"] < 1e-6 and r["s_resid"] < 1e-6
    assert r["dif_pp"] < 8.0
    assert r["h_trans"] < r["s_trans"]
    assert r["h_soc_min"] > 0.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
