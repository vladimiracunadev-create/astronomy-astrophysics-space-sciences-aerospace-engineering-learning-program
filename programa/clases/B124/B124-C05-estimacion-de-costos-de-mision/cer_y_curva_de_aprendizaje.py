#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C05: relacion de estimacion de costo (CER) log-log y curva de aprendizaje, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni una estimacion de costo de una mision real. Los datos de 14 misiones son SINTETICOS.
Consultado (2026-11-11): el NASA Cost Estimating Handbook v4.0 (febrero de 2015) y su apendice E describen los CER como ecuaciones que
relacionan costo con atributos medibles y las curvas de aprendizaje; ninguna cifra de este laboratorio sale de el.
Modelo CER: costo = a * m^b * exp(e), e ~ N(0, s^2); ajuste por minimos cuadrados en ln(costo) = ln(a) + b ln(m).
Curva de aprendizaje (Wright): costo de la unidad n = T1 * n^beta, beta = log2(pendiente), pendiente = 0.85.
Unidades: masa en kg; costo en millones de unidades monetarias sinteticas (Mum), base de precios constante e ilustrativa.
Datos sinteticos generados con a = 0.9, b = 0.55, s = 0.20 (semilla 124); intervalo de prediccion al 80 % con z = 1.2816 (aprox. normal).
Tolerancias: sum de residuos y ortogonalidad con ln(m) < 1e-9; parametros dentro de 3 errores estandar de los verdaderos;
suma directa de la curva de aprendizaje frente a su aproximacion integral < 2 %.
"""
import math, platform, random

A_V, B_V, S_V, N = 0.9, 0.55, 0.20, 14
M_NUEVA = 600.0
T1, PEND, UNID = 40.0, 0.85, 10


def datos():
    rng = random.Random(124)
    out = []
    for _ in range(N):
        m = math.exp(rng.uniform(math.log(80), math.log(3000)))
        c = A_V * m ** B_V * math.exp(rng.gauss(0, S_V))
        out.append((m, c))
    return out


def ajustar(d):
    x = [math.log(m) for m, _ in d]
    y = [math.log(c) for _, c in d]
    n = len(d)
    xb, yb = sum(x) / n, sum(y) / n
    sxx = sum((a - xb) ** 2 for a in x)
    sxy = sum((a - xb) * (b - yb) for a, b in zip(x, y))
    b = sxy / sxx
    la = yb - b * xb
    res = [yy - (la + b * xx) for xx, yy in zip(x, y)]
    see = math.sqrt(sum(r * r for r in res) / (n - 2))
    return dict(b=b, la=la, see=see, sxx=sxx, xb=xb, n=n, res=res, x=x)


def run():
    d = datos()
    f = ajustar(d)
    a_hat = math.exp(f["la"])
    se_b = f["see"] / math.sqrt(f["sxx"])
    x0 = math.log(M_NUEVA)
    med = math.exp(f["la"] + f["b"] * x0)
    sd = f["see"] * math.sqrt(1 + 1 / f["n"] + (x0 - f["xb"]) ** 2 / f["sxx"])
    lo, hi = med * math.exp(-1.2816 * sd), med * math.exp(1.2816 * sd)
    verd = A_V * M_NUEVA ** B_V
    beta = math.log(PEND, 2)
    unit = [T1 * n ** beta for n in range(1, UNID + 1)]
    cum = sum(unit)
    cum_aprox = T1 * ((UNID + 0.5) ** (beta + 1) - 0.5 ** (beta + 1)) / (beta + 1)
    R = {"a_hat": a_hat, "b_hat": f["b"], "see": f["see"], "se_b": se_b, "med": med, "lo": lo, "hi": hi, "verd": verd,
         "dentro": 1 if lo <= verd <= hi else 0, "res_sum": abs(sum(f["res"])), "orto": abs(sum(r * xx for r, xx in zip(f["res"], f["x"]))),
         "b_z": abs(f["b"] - B_V) / se_b, "beta": beta, "u2": unit[1] / unit[0], "u4": unit[3] / unit[0], "u10": unit[-1], "cum": cum,
         "cum_aprox": cum_aprox, "err_aprox": abs(cum - cum_aprox) / cum, "prom": cum / UNID, "total": med + cum,
         "m_min": min(m for m, _ in d), "m_max": max(m for m, _ in d), "pend": PEND}
    return R


def main():
    R = run()
    d = datos()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("14 misiones SINTETICAS (masa en kg, costo en Mum sinteticos), a = 0.9, b = 0.55, s = 0.20, semilla 124")
    for m, c in sorted(d):
        print(f"  m = {m:8.1f} kg   costo = {c:7.2f} Mum")
    print(f"Ajuste: a = {R['a_hat']:.3f} ; b = {R['b_hat']:.4f} (error estandar {R['se_b']:.4f}; |b - 0.55| = {R['b_z']:.2f} errores estandar) ; SEE = {R['see']:.4f}")
    print(f"Prediccion para m = {M_NUEVA:.0f} kg: mediana = {R['med']:.2f} Mum ; intervalo 80 % = [{R['lo']:.2f}, {R['hi']:.2f}] ; verdadero = {R['verd']:.2f} ; dentro = {bool(R['dentro'])}")
    print(f"Curva de aprendizaje: pendiente {R['pend']} ; beta = {R['beta']:.4f} ; unidad 2/unidad 1 = {R['u2']:.4f} ; unidad 4/unidad 1 = {R['u4']:.4f}")
    print(f"  unidad {UNID} = {R['u10']:.3f} Mum ; costo acumulado de {UNID} unidades = {R['cum']:.3f} ; aproximacion integral = {R['cum_aprox']:.3f} ; error = {100 * R['err_aprox']:.2f} %")
    print(f"  costo promedio por unidad = {R['prom']:.3f} Mum ; mision (CER mediano + {UNID} unidades) = {R['total']:.2f} Mum")
    print(f"Residuos: |suma| = {R['res_sum']:.1e} ; |ortogonalidad con ln m| = {R['orto']:.1e}")
    assert R["res_sum"] < 1e-9 and R["orto"] < 1e-9 and R["b_z"] < 3
    assert abs(R["u2"] - PEND) < 1e-12 and abs(R["u4"] - PEND ** 2) < 1e-12
    assert R["err_aprox"] < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
