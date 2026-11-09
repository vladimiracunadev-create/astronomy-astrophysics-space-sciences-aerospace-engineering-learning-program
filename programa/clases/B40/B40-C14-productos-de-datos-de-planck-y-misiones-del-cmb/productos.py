#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C14: lectura de un producto de mapa tipo FITS, conversion de unidades K_CMB -> MJy/sr y verosimilitud gaussiana de espectros por bandas.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, k_B, c (exactas). T_0 = 2,7255 K (Fixsen 2009, solo resumen). Del resumen de Planck 2018 I (arXiv:1807.06205, solo
resumen, consultado el 2026-11-09): nueve bandas de frecuencia de 30 a 857 GHz. NO se descargo ningun producto de Planck ni de otra mision: el archivo FITS de este laboratorio lo
escribe el propio script con 12 valores SINTETICOS (N_side = 1, orden anillo) y sus palabras clave son las que el autor del laboratorio eligio como ejemplo; el valor centinela
-1,6375e30 es un ejemplo (se recuerda como convencion de HEALPix, sin haberla consultado). Los espectros por bandas y la semilla 20261109 son ILUSTRATIVOS.
Modelo: bloques de 2880 bytes con tarjetas de 80 caracteres; tabla binaria de flotantes de 32 bits big-endian; conversion I = (dB/dT) T con dB/dT = (2 k nu^2 / c^2) x^2 e^x / (e^x - 1)^2,
x = h nu / (k T_0); verosimilitud -2 ln L = (d - m)^T M^-1 (d - m) con M diagonal de varianzas 2 C^2/nu.
Supuestos: verosimilitud gaussiana y covarianza diagonal (sin mascara). Validez: educativa; las verosimilitudes publicadas usan covarianzas completas, nuisance y bandas propias.
Tolerancia: ida y vuelta del FITS exacta en float32; dB/dT analitico frente a diferencias finitas, 1e-6 relativo; media de chi^2 simulada dentro de 3 errores estandar del numero de bandas y desviacion mayor que la gaussiana pura.
"""
from __future__ import annotations
import math, platform, random, struct, sys

H = 6.62607015e-34; KB = 1.380649e-23; C = 299792458.0; T0 = 2.7255
CENTINELA = -1.6375e30

def tarjeta(k, v, com=""):
    if isinstance(v, bool):
        s = "T" if v else "F"; vs = f"{s:>20}"
    elif isinstance(v, int):
        vs = f"{v:>20d}"
    else:
        vs = f"'{v:<8}'"
    return (f"{k:<8}= {vs}" + (f" / {com}" if com else "")).ljust(80)[:80]

def cabecera(tarjs):
    txt = "".join(tarjs) + "END".ljust(80)
    n = (len(txt) + 2879) // 2880 * 2880
    return txt.ljust(n).encode("ascii")

def escribir(vals, nside):
    prim = cabecera([tarjeta("SIMPLE", True), tarjeta("BITPIX", 8), tarjeta("NAXIS", 0), tarjeta("EXTEND", True)])
    datos = b"".join(struct.pack(">f", v) for v in vals)
    ext = cabecera([tarjeta("XTENSION", "BINTABLE"), tarjeta("BITPIX", 8), tarjeta("NAXIS", 2), tarjeta("NAXIS1", 4), tarjeta("NAXIS2", len(vals)),
                    tarjeta("PCOUNT", 0), tarjeta("GCOUNT", 1), tarjeta("TFIELDS", 1), tarjeta("TFORM1", "1E"), tarjeta("TTYPE1", "I_STOKES"),
                    tarjeta("TUNIT1", "K_CMB"), tarjeta("PIXTYPE", "HEALPIX"), tarjeta("ORDERING", "RING"), tarjeta("NSIDE", nside)])
    cuerpo = datos.ljust((len(datos) + 2879) // 2880 * 2880, b"\0")
    return prim + ext + cuerpo

def leer(b):
    pos = 0
    hdus = []
    while pos < len(b):
        kv = {}
        fin = False
        while not fin:
            bloque = b[pos:pos + 2880]; pos += 2880
            for i in range(0, 2880, 80):
                t = bloque[i:i + 80].decode("ascii")
                if t.startswith("END"):
                    fin = True; break
                if "=" in t[:9]:
                    k = t[:8].strip(); v = t[10:].split(" / ")[0].strip()
                    kv[k] = v.strip("'").strip() if v.startswith("'") else v
        n = 0
        if int(kv.get("NAXIS", 0)) == 2:
            n = int(kv["NAXIS1"]) * int(kv["NAXIS2"])
        datos = b[pos:pos + n]
        pos += (n + 2879) // 2880 * 2880
        hdus.append((kv, datos))
    return hdus

def planck(nu, t):
    x = H * nu / (KB * t)
    return 2 * H * nu ** 3 / C ** 2 / math.expm1(x)

def dbdt(nu):
    x = H * nu / (KB * T0)
    return 2 * KB * nu ** 2 / C ** 2 * x * x * math.exp(x) / math.expm1(x) ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    vals = [struct.unpack(">f", struct.pack(">f", rng.gauss(0, 100e-6)))[0] for _ in range(12)]
    vals[3] = struct.unpack(">f", struct.pack(">f", CENTINELA))[0]
    b = escribir(vals, 1)
    hd = leer(b)
    kv, datos = hd[1]
    rec = list(struct.unpack(f">{len(datos) // 4}f", datos))
    print(f"archivo de {len(b)} bytes = {len(b) // 2880} bloques de 2880 ; HDU: {len(hd)} ; tabla: TTYPE1={kv['TTYPE1']}, TUNIT1={kv['TUNIT1']}, ORDERING={kv['ORDERING']}, NSIDE={kv['NSIDE']}, NAXIS2={kv['NAXIS2']}")
    assert len(b) % 2880 == 0 and rec == vals and kv["NSIDE"] == "1"
    buenos = [v for v in rec if v > -1e29]
    print(f"valores: {len(rec)} ; marcados como sin dato: {len(rec) - len(buenos)} ; media de los validos = {sum(buenos) / len(buenos) * 1e6:+.3f} uK ; rms = {math.sqrt(sum(v * v for v in buenos) / len(buenos)) * 1e6:.3f} uK")
    assert len(buenos) == 11
    print(f"{'nu [GHz]':>9} {'dB/dT [MJy/sr/K_CMB] analitico':>32} {'diferencias finitas':>20}")
    for nu in (100, 143, 217, 353, 545):
        a = dbdt(nu * 1e9) * 1e20
        h = 1e-4
        n = (planck(nu * 1e9, T0 + h) - planck(nu * 1e9, T0 - h)) / (2 * h) * 1e20
        print(f"{nu:9d} {a:32.4f} {n:20.4f}")
        assert abs(a / n - 1) < 1e-6
    print("(las conversiones no se compararon con la tabla de ninguna mision)")
    # verosimilitud gaussiana por bandas
    D0 = 1000.0
    bandas = [(2, 4), (5, 29), (30, 99), (100, 299), (300, 599), (600, 999), (1000, 1499)]
    nu_b = [sum(2 * l + 1 for l in range(a, b + 1)) for a, b in bandas]
    cb = [sum(2 * math.pi * D0 / (l * (l + 1)) for l in range(a, b + 1)) / (b - a + 1) for a, b in bandas]
    print(f"{'banda':>12} {'grados de libertad':>19} {'C medio [uK^2]':>15} {'sigma/C = sqrt(2/nu)':>21} {'asimetria 2 sqrt(2/nu)':>23}")
    for (a, bb), v, c in zip(bandas, nu_b, cb):
        print(f"{str(a) + '-' + str(bb):>12} {v:19d} {c:15.4e} {math.sqrt(2 / v):21.4f} {2 * math.sqrt(2 / v):23.4f}")
    nrep = 5000
    chis = []
    for _ in range(nrep):
        chi = 0.0
        for v, c in zip(nu_b, cb):
            d = c * (2 * rng.gammavariate(v / 2.0, 1.0)) / v
            chi += (d - c) ** 2 / (2 * c * c / v)
        chis.append(chi)
    m = sum(chis) / nrep
    sd = math.sqrt(sum((x - m) ** 2 for x in chis) / (nrep - 1))
    print(f"chi^2 con {len(nu_b)} bandas: media = {m:.3f} (exacta {len(nu_b)}: la media de la forma cuadratica no depende de la asimetria) ; desviacion = {sd:.3f} (gaussiano puro: {math.sqrt(2 * len(nu_b)):.3f}; la asimetria de la banda l = 2-4 la aumenta)")
    assert sd > math.sqrt(2 * len(nu_b))
    e_m = sd / math.sqrt(nrep)
    esp = float(len(nu_b))      # E[(x/nu - 1)^2 nu/2] = 1 para x ~ chi^2_nu
    assert abs(m - esp) < 3 * e_m + 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
