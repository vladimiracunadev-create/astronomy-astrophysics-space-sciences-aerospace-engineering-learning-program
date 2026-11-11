#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C10: precio fijo frente a costo mas incentivo (CPIF) para el comprador y el contratista, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria legal ni de contratacion publica. Costos, precios y tasas de reparto son SINTETICOS.
Consultado (2026-11-11), NASA OIG IG-20-005 (2019): el programa de tripulacion comercial se contrato con empresas bajo contratos de precio fijo
(la NASA paga un precio fijo por el servicio, como en los servicios de carga). Ademas, la NASA acordo pagar 287.2 millones de USD sobre los precios fijos de Boeing (misiones 3 a 6); son datos cualitativos para el modelo.
Modelo: costo real c = 100 exp(N(0.05, 0.20^2)) (um). Precio fijo (FFP): pago = 110; ganancia del contratista = 110 - c.
CPIF: pago = min(c + honorario, 125); honorario = clamp(8 + 0.2 (100 - c), 2, 14); ganancia = pago - c.
Esperanza e integracion: Simpson sobre z en [-6, 6] (4001 puntos) frente a Monte Carlo (200000 muestras, semilla 124).
Tolerancias: esperanzas por Simpson frente a Monte Carlo < 0.3 um; probabilidades < 0.005.
"""
import math, platform, random

MU, SIG, CT = 0.05, 0.20, 100.0
PRECIO, TECHO = 110.0, 125.0
FEE0, SHARE, FMIN, FMAX = 8.0, 0.2, 2.0, 14.0


def costo(z):
    return CT * math.exp(MU + SIG * z)


def pago_ffp(c):
    return PRECIO


def pago_cpif(c):
    fee = min(max(FEE0 + SHARE * (CT - c), FMIN), FMAX)
    return min(c + fee, TECHO)


def pdf(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def esperanza(f, n=4000, zmax=6.0):
    h = 2 * zmax / n
    s = 0.0
    for i in range(n + 1):
        z = -zmax + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * f(z) * pdf(z)
    return s * h / 3


def momentos(pago):
    e = esperanza(lambda z: pago(costo(z)))
    e2 = esperanza(lambda z: pago(costo(z)) ** 2)
    g = esperanza(lambda z: pago(costo(z)) - costo(z))
    p_perd = esperanza(lambda z: 1.0 if pago(costo(z)) - costo(z) < 0 else 0.0, n=40000)
    return e, math.sqrt(max(e2 - e * e, 0.0)), g, p_perd


def mc(pago, rng, n=200000):
    pagos, gan, perd = [], [], 0
    for _ in range(n):
        c = costo(rng.gauss(0, 1))
        p = pago(c)
        pagos.append(p)
        gan.append(p - c)
        if p - c < 0:
            perd += 1
    m = sum(pagos) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in pagos) / n)
    return m, sd, sum(gan) / n, perd / n


def run():
    ffp, cpif = momentos(pago_ffp), momentos(pago_cpif)
    rng = random.Random(124)
    mf, mcp = mc(pago_ffp, rng), mc(pago_cpif, rng)
    p_techo = esperanza(lambda z: 1.0 if costo(z) + min(max(FEE0 + SHARE * (CT - costo(z)), FMIN), FMAX) > TECHO else 0.0, n=40000)
    mediana = CT * math.exp(MU)
    R = {"e_ffp": ffp[0], "sd_ffp": ffp[1], "g_ffp": ffp[2], "pl_ffp": ffp[3], "e_cpif": cpif[0], "sd_cpif": cpif[1], "g_cpif": cpif[2], "pl_cpif": cpif[3],
         "mc_e_ffp": mf[0], "mc_e_cpif": mcp[0], "mc_g_ffp": mf[2], "mc_g_cpif": mcp[2], "mc_pl_ffp": mf[3], "mc_pl_cpif": mcp[3],
         "dif_e": max(abs(ffp[0] - mf[0]), abs(cpif[0] - mcp[0])), "dif_g": max(abs(ffp[2] - mf[2]), abs(cpif[2] - mcp[2])),
         "dif_p": max(abs(ffp[3] - mf[3]), abs(cpif[3] - mcp[3])), "p_techo": p_techo, "mediana": mediana,
         "fee_mediana": min(max(FEE0 + SHARE * (CT - mediana), FMIN), FMAX), "pago_mediana": pago_cpif(mediana)}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Contratos SINTETICOS (um): costo real c = 100 exp(N(0.05, 0.20^2)); mediana =", f"{R['mediana']:.2f}")
    print("Dato consultado (NASA OIG IG-20-005, 2019): el programa de tripulacion comercial uso contratos de precio fijo (cualitativo)")
    print(" contrato  E[pago]  DE[pago]  E[ganancia contratista]  P(contratista pierde)   Monte Carlo: E[pago] E[gan] P(pierde)")
    print(f" FFP    {R['e_ffp']:9.3f} {R['sd_ffp']:9.3f} {R['g_ffp']:15.3f} {R['pl_ffp']:20.4f} {R['mc_e_ffp']:15.3f} {R['mc_g_ffp']:7.3f} {R['mc_pl_ffp']:8.4f}")
    print(f" CPIF   {R['e_cpif']:9.3f} {R['sd_cpif']:9.3f} {R['g_cpif']:15.3f} {R['pl_cpif']:20.4f} {R['mc_e_cpif']:15.3f} {R['mc_g_cpif']:7.3f} {R['mc_pl_cpif']:8.4f}")
    print(f"CPIF con costo mediano: honorario = {R['fee_mediana']:.3f} ; pago = {R['pago_mediana']:.3f} ; P(c + honorario > techo) = {R['p_techo']:.4f}")
    print(f"Diferencias Simpson - Monte Carlo: esperanza del pago {R['dif_e']:.3f} ; ganancia {R['dif_g']:.3f} ; probabilidades {R['dif_p']:.4f}")
    assert R["dif_e"] < 0.3 and R["dif_g"] < 0.3 and R["dif_p"] < 0.005
    assert R["sd_ffp"] < 0.05 and R["sd_cpif"] > 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
