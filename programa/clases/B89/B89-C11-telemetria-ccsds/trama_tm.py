#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C11. Telemetria CCSDS: marcador ASM 1ACFFC1D, bloque RS(255,223) con entrelazado I, rendimiento de la trama y
sincronizacion de trama por correlacion con tolerancia. ASM e I: CCSDS 131.0-B-5 (consultada). Cabecera de 6 octetos y CRC de 2 octetos:
ILUSTRATIVOS (formato de trama TM no consultado). Datos y errores SINTETICOS, semilla 89."""
import math, random, sys

ASM = 0x1ACFFC1D
ASM_BITS = [(ASM >> (31 - i)) & 1 for i in range(32)]

def estructura(i, cabecera=6, fec=2):
    k_oct = 223 * i                    # octetos de informacion por bloque (tabla 6-1)
    n_oct = 255 * i
    carga = k_oct - cabecera - fec     # octetos de datos de usuario
    return {"k_oct": k_oct, "n_oct": n_oct, "canal_oct": n_oct + 4, "carga": carga,
            "efic": carga / (n_oct + 4), "k_bits": 8 * k_oct}

def p_deteccion(p, t):
    return sum(math.comb(32, k) * p ** k * (1 - p) ** (32 - k) for k in range(t + 1))

def p_falsa(t):
    return sum(math.comb(32, k) for k in range(t + 1)) / 2 ** 32   # patron aleatorio a distancia <= t

def buscar(bits, t):
    n = len(bits)
    hits = []
    for pos in range(n - 32 + 1):
        d = 0
        for j in range(32):
            if bits[pos + j] != ASM_BITS[j]:
                d += 1
                if d > t:
                    break
        else:
            hits.append(pos)
        if d <= t and (not hits or hits[-1] != pos):
            hits.append(pos)
    return hits

def calcular():
    R = {"estr": {i: estructura(i) for i in (1, 2, 3, 4, 5, 8)}}
    rng = random.Random(89)
    i = 5
    e = R["estr"][i]
    nbits_trama = 8 * e["canal_oct"]
    nt, p, t = 20, 0.02, 3
    bits = []
    posiciones = []
    for _ in range(nt):
        posiciones.append(len(bits))
        bits += ASM_BITS + [rng.getrandbits(1) for _ in range(8 * e["n_oct"])]
    ruidoso = [b ^ (rng.random() < p) for b in bits]
    hits = buscar(ruidoso, t)
    R["n_tramas"], R["p"], R["t"] = nt, p, t
    R["detectadas"] = sum(1 for q in posiciones if q in hits)
    R["falsas"] = len(hits) - R["detectadas"]
    R["p_det"] = p_deteccion(p, t)
    R["p_falsa_pos"] = p_falsa(t)
    R["falsas_esp"] = R["p_falsa_pos"] * (len(bits) - 32)
    R["nbits"] = len(bits)
    R["asm_hex"] = f"{ASM:08X}"
    R["asm_bin"] = "".join(map(str, ASM_BITS))
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"ASM = {R['asm_hex']} = {R['asm_bin']} (CCSDS 131.0-B-5, consultada)")
    print("Estructura con RS(255,223) segun profundidad I (cabecera 6 + CRC 2 octetos ILUSTRATIVOS):")
    print(f"{'I':>3s}{'k [oct]':>9s}{'n [oct]':>9s}{'canal [oct]':>13s}{'datos [oct]':>13s}{'eficiencia':>12s}{'k [bits]':>10s}")
    for i, e in R["estr"].items():
        print(f"{i:3d}{e['k_oct']:9d}{e['n_oct']:9d}{e['canal_oct']:13d}{e['carga']:13d}{e['efic']:12.4f}{e['k_bits']:10d}")
    print(f"Sincronizacion de trama: {R['n_tramas']} tramas, p = {R['p']}, tolerancia t = {R['t']} bits, {R['nbits']} bits")
    print(f"  P(deteccion) teorica = {R['p_det']:.5f} ; detectadas = {R['detectadas']}/{R['n_tramas']}")
    print(f"  P(falsa por posicion) = {R['p_falsa_pos']:.3e} ; falsas esperadas = {R['falsas_esp']:.3f} ; falsas observadas = {R['falsas']}")
    assert R["asm_hex"] == "1ACFFC1D" and R["estr"][5]["k_bits"] == 8920 and R["estr"][1]["k_bits"] == 1784
    assert R["detectadas"] >= R["n_tramas"] - 2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
