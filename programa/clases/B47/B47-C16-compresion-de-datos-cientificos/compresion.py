#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C16: compresion de datos cientificos, entropia de Shannon, codigo de Rice sin perdida y cuantizacion con perdida acotada.

Datos: ninguna constante fisica. La imagen es SINTETICA (semilla 20261109) e ILUSTRATIVA: 128 x 128 pixeles, fondo suave 400 + 150 sin(x/20) cos(y/25) cuentas mas ruido gaussiano
de varianza igual a la senal (aproximacion del ruido de fotones). No es una imagen de ningun instrumento. El estandar CCSDS de compresion sin perdida no se consulto: aqui se implementa solo
un codigo de Rice con parametro k adaptativo por bloque de 32 muestras, no el estandar.
Modelo: (1) prediccion horizontal d[i] = x[i] - x[i-1] y plegado a enteros no negativos n = 2d (d >= 0) o -2d - 1; (2) entropia empirica H = -sum p log2 p de los residuos;
(3) longitud de Rice (n >> k) + 1 + k con k optimo por bloque mas 4 bits de cabecera; (4) decodificacion bit a bit y comprobacion de que la ida y vuelta es identica;
(5) cuantizacion con paso entero impar q: error maximo (q-1)/2 y RMS sqrt((q^2-1)/12) (uniforme discreta) frente al medido, y razon de compresion.
Supuestos: residuos independientes y estacionarios por bloque; imagen de 16 bit sin saturacion. Validez: ilustrativa.
Tolerancia: ida y vuelta exacta; H <= bits por pixel de Rice <= H + 0,6; RMS de cuantizacion a 3 % de sqrt((q^2-1)/12).
"""
from __future__ import annotations
import math, platform, random

N = 128
BLOQ = 32


def imagen():
    rng = random.Random(20261109)
    img = []
    for y in range(N):
        fila = []
        for x in range(N):
            mu = 400 + 150 * math.sin(x / 20) * math.cos(y / 25)
            fila.append(int(round(rng.gauss(mu, math.sqrt(mu)))))
        img.append(fila)
    return img


def residuos(img):
    out = []
    for fila in img:
        prev = fila[0]
        out.append(prev)
        for v in fila[1:]:
            out.append(v - prev)
            prev = v
    return out


def plegar(d):
    return 2 * d if d >= 0 else -2 * d - 1


def desplegar(n):
    return n // 2 if n % 2 == 0 else -(n + 1) // 2


def entropia(xs):
    cnt = {}
    for v in xs:
        cnt[v] = cnt.get(v, 0) + 1
    n = len(xs)
    return -sum(c / n * math.log2(c / n) for c in cnt.values())


def rice_len(bloque, k):
    return sum((v >> k) + 1 + k for v in bloque)


def codificar(ns):
    bits = []
    for i in range(0, len(ns), BLOQ):
        b = ns[i:i + BLOQ]
        k = min(range(16), key=lambda kk: rice_len(b, kk))
        bits.append(format(k, "04b"))
        for v in b:
            bits.append("1" * (v >> k) + "0" + (format(v & ((1 << k) - 1), f"0{k}b") if k else ""))
    return "".join(bits)


def decodificar(s, total):
    ns, pos = [], 0
    while len(ns) < total:
        k = int(s[pos:pos + 4], 2)
        pos += 4
        for _ in range(min(BLOQ, total - len(ns))):
            q = 0
            while s[pos] == "1":
                q += 1
                pos += 1
            pos += 1
            r = int(s[pos:pos + k], 2) if k else 0
            pos += k
            ns.append((q << k) | r)
    return ns


def calc():
    img = imagen()
    flat = [v for f in img for v in f]
    res = residuos(img)
    # los primeros pixeles de cada fila se guardan con su valor; se pliegan igual (son positivos grandes)
    ns = [plegar(d) for d in res]
    r = {"npix": len(flat)}
    r["H_res"] = entropia(ns)
    r["H_crudo"] = entropia(flat)
    bits = codificar(ns)
    r["bpp"] = len(bits) / len(ns)
    dec = decodificar(bits, len(ns))
    r["ida_vuelta"] = dec == ns
    rec = []
    for i in range(0, len(dec), N):
        fila = [desplegar(dec[i])]
        for n in dec[i + 1:i + N]:
            fila.append(fila[-1] + desplegar(n))
        rec.append(fila)
    r["identica"] = rec == img
    r["razon"] = 16 / r["bpp"]
    r["q"] = {}
    for q in (3, 5, 9):
        cu = [round(v / q) for v in flat]
        err = [c * q - v for c, v in zip(cu, flat)]
        rms = math.sqrt(sum(e * e for e in err) / len(err))
        h = entropia(cu)
        r["q"][q] = (max(abs(e) for e in err), rms, math.sqrt((q * q - 1) / 12), h)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"pixeles = {r['npix']} ; entropia de los pixeles crudos = {r['H_crudo']:.4f} bit ; entropia de los residuos = {r['H_res']:.4f} bit")
    print(f"Rice adaptativo (con cabecera): {r['bpp']:.4f} bit/pixel ; razon de compresion frente a 16 bit = {r['razon']:.3f}")
    print(f"ida y vuelta identica: {r['identica']}")
    print(f"{'q':>3} {'error max':>10} {'RMS medido':>11} {'teorico':>9} {'H cuantizada [bit]':>19}")
    for q, (em, rms, teo, h) in r["q"].items():
        print(f"{q:3d} {em:10.1f} {rms:11.4f} {teo:9.4f} {h:19.4f}")
        assert em <= (q - 1) / 2
        assert abs(rms - teo) / teo < 0.03
    assert r["identica"] and r["ida_vuelta"]
    assert r["H_res"] <= r["bpp"] <= r["H_res"] + 0.6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
