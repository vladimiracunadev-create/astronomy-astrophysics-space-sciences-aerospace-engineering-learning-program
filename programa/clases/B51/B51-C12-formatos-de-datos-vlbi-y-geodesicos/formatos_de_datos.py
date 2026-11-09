#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C12: cuantizacion de 1 y 2 bits, correccion de Van Vleck, empaquetado de bits y tarjetas de cabecera tipo FITS.

Datos: ninguna constante fisica. Todo es SINTETICO e ILUSTRATIVO (semilla 20261109): senales gaussianas, tasa de 2 GHz de ancho de banda, 2 polarizaciones. El formato de empaquetado
de 2 bits por muestra (4 muestras por byte) y las tarjetas de 80 caracteres en bloques de 2880 bytes son un EJEMPLO DIDACTICO inspirado en convenciones conocidas; no implementa VDIF,
Mark 5 ni FITS-IDI y la norma de ninguno de ellos NO fue consultada.
Modelo: eficiencia de muestreo eta = (E[x q(x)])^2 / (E[q^2] E[x^2]) para un cuantizador de 2 bits con niveles +-1, +-3 (unidades de v0) y umbrales 0, +-t; 1 bit: eta = 2/pi.
Para 1 bit la correlacion medida rho_q = (2/pi) arcsin(rho) (Van Vleck), de donde rho = sin(pi rho_q / 2).
Segunda via: eta analitica por erf frente a un Monte Carlo; correlacion recuperada frente a la inyectada; ida y vuelta de empaquetado y de tarjetas.
Supuestos: muestras gaussianas de media cero e independientes, umbrales fijos. Validez: ilustrativa.
Tolerancia: eta de 1 bit exacta a 1e-9; eta de 2 bits Monte Carlo dentro de 0,01 de la analitica; rho recuperada dentro de 3 errores estandar; ida y vuelta exacta.
"""
from __future__ import annotations
import math, platform, random, sys

def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)

def cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def eta2(t, v0):
    """eficiencia con niveles +-1*v0 y +-3*v0 y umbrales 0, +-t*v0 ... (t en unidades de sigma, v0 en sigma)."""
    ex = 2 * (1 * (phi(0) - phi(t)) + 3 * phi(t)) * v0
    eq2 = 2 * ((cdf(t) - 0.5) * 1 + (1 - cdf(t)) * 9) * v0 * v0
    return ex * ex / eq2

def quant2(x, t, v0):
    a = abs(x)
    m = 1 if a < t else 3
    return (m if x >= 0 else -m)

def pack2(codes):
    out = bytearray()
    for i in range(0, len(codes), 4):
        b = 0
        for k, c in enumerate(codes[i:i + 4]):
            b |= c << (2 * k)
        out.append(b)
    return bytes(out)

def unpack2(data, n):
    return [(data[i // 4] >> (2 * (i % 4))) & 3 for i in range(n)]

LEV = {0: -3, 1: -1, 2: 1, 3: 3}
INV = {v: k for k, v in LEV.items()}

def card(key, val, com=""):
    s = f"{key:<8}= {val:>20}" + (f" / {com}" if com else "")
    return s.ljust(80)

def parse_card(c):
    k = c[:8].strip(); rest = c[10:]
    v = rest.split(" / ")[0].strip()
    return k, v

def compute():
    rng = random.Random(20261109)
    R = dict(eta1=2 / math.pi)
    best = (0, 0, 0)
    for it in range(1, 400):
        t = it * 0.01
        for jv in range(1, 400):
            v0 = jv * 0.01
            e = eta2(t, v0)
            if e > best[0]:
                best = (e, t, v0)
    R["eta2"], R["t_opt"], R["v0_opt"] = best
    # Monte Carlo
    n = 200000
    xs = [rng.gauss(0, 1) for _ in range(n)]
    q = [quant2(x, R["t_opt"], 1.0) * R["v0_opt"] for x in xs]
    sxq = sum(a * b for a, b in zip(xs, q)) / n
    sqq = sum(b * b for b in q) / n
    R["eta2_mc"] = sxq ** 2 / (sqq * (sum(x * x for x in xs) / n))
    R["eta1_mc"] = (sum(abs(x) for x in xs) / n) ** 2 / (sum(x * x for x in xs) / n)
    # Van Vleck (1 bit)
    rows = []
    nn = 400000
    for rho in (0.05, 0.3, 0.7):
        s = 0
        for _ in range(nn):
            a = rng.gauss(0, 1); b = rho * a + math.sqrt(1 - rho * rho) * rng.gauss(0, 1)
            s += (1 if a >= 0 else -1) * (1 if b >= 0 else -1)
        rq = s / nn
        se = math.sqrt((1 - rq * rq) / nn)
        rho_est = math.sin(math.pi * rq / 2)
        se_rho = se * math.pi / 2 * math.cos(math.pi * rq / 2)
        rows.append((rho, rq, 2 / math.pi * math.asin(rho), rho_est, se_rho))
    R["vv"] = rows
    # empaquetado
    codes = [INV[quant2(rng.gauss(0, 1), R["t_opt"], 1.0)] for _ in range(1003)]
    data = pack2(codes)
    R["pack_ok"] = unpack2(data, len(codes)) == codes
    R["nbytes"] = len(data); R["nsamp"] = len(codes)
    # tasa de datos
    bw, pol, bits = 2.0e9, 2, 2
    R["rate_gbps"] = 2 * bw * pol * bits / 1e9
    R["TB_h"] = R["rate_gbps"] * 1e9 / 8 * 3600 / 1e12
    # tarjetas
    cards = [card("SIMPLE", "T", "didactico"), card("BITPIX", "8"), card("NAXIS", "1"), card("NAXIS1", str(len(data)), "bytes"), card("CHANBW", "2.0E9", "Hz")]
    cards.append("END".ljust(80))
    header = "".join(cards).ljust(2880)
    R["hdr_len"] = len(header)
    back = [parse_card(header[i:i + 80]) for i in range(0, 80 * 5, 80)]
    R["cards_ok"] = (dict(back)["NAXIS1"] == str(len(data)) and dict(back)["SIMPLE"] == "T")
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"1 bit: eta = 2/pi = {R['eta1']:.6f} ; Monte Carlo = {R['eta1_mc']:.4f}")
    print(f"2 bits: eta optima analitica = {R['eta2']:.4f} con umbral t = {R['t_opt']:.2f} sigma y nivel v0 = {R['v0_opt']:.2f} sigma ; Monte Carlo = {R['eta2_mc']:.4f}")
    assert abs(R["eta1_mc"] - R["eta1"]) < 0.01 and abs(R["eta2_mc"] - R["eta2"]) < 0.01
    print("Van Vleck (1 bit): rho_inyectada, rho_q medida, (2/pi) asin(rho), rho recuperada, error estandar")
    for rho, rq, th, re, se in R["vv"]:
        print(f"  {rho:.2f} {rq:+.4f} {th:+.4f} {re:.4f} {se:.4f}")
        assert abs(re - rho) < 3 * se
    print(f"empaquetado: {R['nsamp']} muestras de 2 bits -> {R['nbytes']} bytes ; ida y vuelta exacta = {R['pack_ok']}")
    assert R["pack_ok"] and R["nbytes"] == (R["nsamp"] + 3) // 4
    print(f"tasa de datos: 2 x 2 GHz x 2 pol x 2 bits = {R['rate_gbps']:.1f} Gbit/s = {R['TB_h']:.2f} TB por hora")
    print(f"cabecera tipo FITS: {R['hdr_len']} bytes (multiplo de 2880: {R['hdr_len'] % 2880 == 0}) ; ida y vuelta de tarjetas = {R['cards_ok']}")
    assert R["cards_ok"] and R["hdr_len"] % 2880 == 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
