#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C09. Codificacion correctora de errores: Hamming(7,4) simulado y Reed-Solomon (255,223) analitico,
con la tabla de bloques/entrelazado de CCSDS 131.0-B-5 (consultada). Canal SINTETICO, semilla fija."""
import math, random, sys

def comb(n, k):
    return math.comb(n, k)

def hamming_enc(d):
    d1, d2, d3, d4 = d
    p1, p2, p3 = d1 ^ d2 ^ d4, d1 ^ d3 ^ d4, d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]   # posiciones 1..7

def hamming_dec(c):
    s1 = c[0] ^ c[2] ^ c[4] ^ c[6]
    s2 = c[1] ^ c[2] ^ c[5] ^ c[6]
    s3 = c[3] ^ c[4] ^ c[5] ^ c[6]
    pos = s1 + 2 * s2 + 4 * s3
    c = c[:]
    if pos:
        c[pos - 1] ^= 1
    return [c[2], c[4], c[5], c[6]]

def sim_hamming(p, n, rng):
    err_bloque = err_bits = 0
    for _ in range(n):
        d = [rng.getrandbits(1) for _ in range(4)]
        c = hamming_enc(d)
        r = [b ^ (rng.random() < p) for b in c]
        o = hamming_dec(r)
        e = sum(a != b for a, b in zip(d, o))
        err_bits += e
        err_bloque += e > 0
    return err_bloque / n, err_bits / (4 * n)

def p_bloque_hamming(p):
    return 1 - (1 - p) ** 7 - 7 * p * (1 - p) ** 6

def p_bloque_rs(ps, n=255, t=16):
    return sum(comb(n, i) * ps ** i * (1 - ps) ** (n - i) for i in range(t + 1, n + 1))

def ber_rs(ps, n=255, t=16, m=8):
    """BER de salida aproximada: tasa de error de simbolo decodificada x 2^(m-1)/(2^m-1)."""
    pse = sum((i / n) * comb(n, i) * ps ** i * (1 - ps) ** (n - i) for i in range(t + 1, n + 1))
    return pse * 2 ** (m - 1) / (2 ** m - 1)

def q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))

def ebn0_req(ber_obj, codificado):
    lo, hi = 0.0, 200.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if codificado:
            pb = q(math.sqrt(2 * (223 / 255) * mid))     # BPSK sobre el simbolo codificado, Eb -> r Eb
            ps = 1 - (1 - pb) ** 8
            ber = ber_rs(ps)
        else:
            ber = q(math.sqrt(2 * mid))
        if ber > ber_obj:
            lo = mid
        else:
            hi = mid
    return 10 * math.log10(lo)

def calcular():
    R = {}
    rng = random.Random(89)
    R["p_canal"] = 0.02
    R["n_sim"] = 100_000
    R["sim_bloque"], R["sim_bit"] = sim_hamming(R["p_canal"], R["n_sim"], rng)
    R["teo_bloque"] = p_bloque_hamming(R["p_canal"])
    R["z"] = abs(R["sim_bloque"] - R["teo_bloque"]) / math.sqrt(R["teo_bloque"] * (1 - R["teo_bloque"]) / R["n_sim"])
    R["sin_codigo_bit"] = R["p_canal"]
    R["rs"] = {ps: p_bloque_rs(ps) for ps in (0.01, 0.05, 0.0627, 0.08, 0.10)}
    R["rs_umbral"] = 16 / 255
    R["req_sin"], R["req_con"] = ebn0_req(1e-5, False), ebn0_req(1e-5, True)
    R["ganancia"] = R["req_sin"] - R["req_con"]
    R["ccsds_k"] = {i: 223 * 8 * i for i in (1, 2, 3, 4, 5, 8)}
    R["ccsds_n"] = {i: 255 * 8 * i for i in (1, 2, 3, 4, 5, 8)}
    R["tasa_rs"] = 223 / 255
    R["chk_hamming_n"] = all(hamming_dec(hamming_enc([a, b, c, d])) == [a, b, c, d]
                              for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1))
    # un error en cualquier posicion siempre se corrige
    R["chk_un_error"] = True
    for dd in range(16):
        d = [(dd >> i) & 1 for i in range(4)]
        c = hamming_enc(d)
        for pos in range(7):
            r = c[:]
            r[pos] ^= 1
            R["chk_un_error"] &= hamming_dec(r) == d
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print("Hamming(7,4) sobre canal binario simetrico SINTETICO p = 0.02 (100000 bloques)")
    print(f"  P(bloque erroneo) simulada = {R['sim_bloque']:.5f} ; teorica = {R['teo_bloque']:.5f} ; z = {R['z']:.2f}")
    print(f"  BER de informacion = {R['sim_bit']:.5f} frente a {R['sin_codigo_bit']:.5f} sin codigo")
    print("Reed-Solomon (255,223), t = 16 simbolos: probabilidad de bloque no corregido segun p_simbolo")
    for ps, v in R["rs"].items():
        print(f"  p_s = {ps:.4f} -> P_bloque = {v:.3e}")
    print(f"  umbral t/n = {R['rs_umbral']:.4f} ; tasa del codigo = {R['tasa_rs']:.4f}")
    print(f"Eb/N0 para BER 1e-5: sin codigo = {R['req_sin']:.2f} dB ; con RS(255,223) = {R['req_con']:.2f} dB ; ganancia = {R['ganancia']:.2f} dB")
    print("CCSDS 131.0-B-5, tabla 6-1: profundidad I -> k bits (223 octetos x I) / n bits (255 octetos x I)")
    for i in R["ccsds_k"]:
        print(f"  I = {i}: k = {R['ccsds_k'][i]} ; n = {R['ccsds_n'][i]}")
    assert R["chk_hamming_n"] and R["chk_un_error"] and R["z"] < 4
    assert [R["ccsds_k"][i] for i in (1, 2, 4, 5)] == [1784, 3568, 7136, 8920]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
