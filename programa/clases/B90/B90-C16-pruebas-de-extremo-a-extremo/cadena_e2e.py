#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C16: cadena de telecomando/telemetria de extremo a extremo con CRC-16 y canal con errores (SINTETICO).

CRC-16/CCITT-FALSE (polinomio 0x1021, valor inicial 0xFFFF, sin reflexion): el codigo de verificacion estandar de "123456789" es 0x29B1
(valor de uso general; NO consultado en una fuente). Canal binario simetrico con BER p: tasa de error de trama FER = 1 - (1-p)^n.
Se comprueba por Monte Carlo y se mide la deteccion de errores del CRC. Unidades: bits, s, adimensional. Tolerancia: 4 errores estandar.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: trama de 1024 bits de datos + CRC de 16 bits; enlace de 9600 bit/s")

def _tabla():
    tb = []
    for i in range(256):
        c = i << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
        tb.append(c)
    return tb

TB = _tabla()

def crc16(data: bytes, crc=0xFFFF) -> int:
    for b in data:
        crc = ((crc << 8) & 0xFFFF) ^ TB[(crc >> 8) ^ b]
    return crc

chk = crc16(b"123456789")
print(f"CRC-16/CCITT-FALSE de '123456789' = 0x{chk:04X} (valor de verificacion habitual: 0x29B1)")
comprobar(chk == 0x29B1, "el CRC debe dar el valor de verificacion")
rng = np.random.default_rng(90)
datos = bytes(rng.integers(0, 256, 128, dtype=np.uint8))
trama = datos + crc16(datos).to_bytes(2, "big")
n = len(trama) * 8
print(f"Trama = {len(trama)} bytes = {n} bits ; CRC de los datos = 0x{crc16(datos):04X} ; CRC de la trama completa = 0x{crc16(trama):04X} (0 si es valida)")
comprobar(crc16(trama) == 0, "la trama sin errores debe verificar")

def voltea(t: bytes, bits):
    a = bytearray(t)
    for b in bits:
        a[b // 8] ^= 1 << (7 - b % 8)
    return bytes(a)

simples = sum(1 for b in range(n) if crc16(voltea(trama, [b])) != 0)
print(f"Errores de 1 bit: detectados {simples} de {n}")
comprobar(simples == n, "el CRC debe detectar todos los errores de un bit")
rr = np.random.default_rng(91)
doble = sum(1 for _ in range(20000) if crc16(voltea(trama, list(rr.choice(n, 2, replace=False)))) != 0)
print(f"Errores de 2 bits (20 000 al azar): detectados {doble}")
comprobar(doble == 20000, "los errores dobles deben detectarse")
rafaga = 0
for _ in range(20000):
    L = int(rr.integers(1, 17))
    ini = int(rr.integers(0, n - L))
    bits = [ini, ini + L - 1] + [b for b in range(ini + 1, ini + L - 1) if rr.random() < 0.5] if L > 1 else [ini]
    rafaga += crc16(voltea(trama, bits)) != 0
print(f"Rafagas de hasta 16 bits (20 000 al azar): detectadas {rafaga}")
comprobar(rafaga == 20000, "las rafagas de hasta 16 bits deben detectarse")
sin_det = 0
M = 2_000_000
blk = rr.integers(0, 256, (M, 4), dtype=np.uint8)
for row in blk:
    sin_det += crc16(bytes(row)) == 0
print(f"Palabras al azar de 4 bytes con CRC valido: {sin_det} de {M} = {sin_det / M:.2e} (teoria 2^-16 = {2.0**-16:.2e})")
comprobar(sin_det <= 4 * math.sqrt(M * 2.0**-16) + M * 2.0**-16 + 3, "la fraccion no detectada debe ser cercana a 2^-16")

print("BER p -> FER teorico -> FER Monte Carlo (200 000 tramas) -> reintentos medios 1/(1-FER)")
N = 200_000
for p in (1e-6, 1e-5, 1e-4, 1e-3):
    fer = 1 - (1 - p) ** n
    errs = rng.binomial(n, p, N) > 0
    fm = errs.mean()
    se = math.sqrt(fer * (1 - fer) / N)
    print(f"  {p:7.0e} -> {fer:.5f} -> {fm:.5f} -> {1 / (1 - fer):.3f}")
    comprobar(abs(fm - fer) <= 4 * se + 1e-6, "Monte Carlo debe coincidir con la FER teorica")

rate = 9600.0
t_trama = n / rate
c = 299792458.0
rango = 1.5e6
lat = {"serializacion de la trama": t_trama, "propagacion (1500 km, un sentido)": rango / c, "proceso en a bordo (ejemplo)": 0.020, "respuesta de telemetria (serializacion)": t_trama}
print("Presupuesto de latencia de un telecomando con acuse [s]:")
for k_, v_ in lat.items():
    print(f"   {k_:42s} {v_:8.4f}")
tot = sum(lat.values()) + rango / c
print(f"   total (ida y vuelta, con propagacion de regreso) = {tot:.4f} s")
comprobar(0.2 < tot < 0.3, "el total del ejemplo debe estar entre 0.2 y 0.3 s")
fin()
