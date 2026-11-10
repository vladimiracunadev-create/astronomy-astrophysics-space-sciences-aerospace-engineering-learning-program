#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C02: entrelazado de profundidad I y concatenacion convolucional + Reed-Solomon.

Consultado (2026-11-10, CCSDS 131.0-B-5): profundidades de entrelazado permitidas I = 1, 2, 3, 4, 5, 8; RS(255,223) E = 16;
codigo convolucional de tasa 1/2 y longitud de restriccion 7 con G1 = 171 (octal) y G2 = 133 (octal), con inversion de la salida de G2.
Convencion de orden de bits del registro: propia de este laboratorio (no se verifico contra los octetos del estandar).
Entrelazado: el octeto i de la corriente transmitida es el simbolo i // I de la palabra i % I (reparto simbolo a simbolo).
Datos SINTETICOS: mensajes, rafagas y errores de canal con random.Random(94004..94005). Canal binario simetrico con
decision dura; el canal real del estandar (AWGN con decision blanda) no se simula.
Segunda via: umbral teorico exacto de rafaga = E*I octetos (cada palabra recibe como maximo ceil(B/I) simbolos erroneos).
Tolerancias: igualdad exacta (aritmetica entera).
"""
from __future__ import annotations
import platform, random

PRIM = 0x187  # x^8 + x^7 + x^2 + x + 1
EXP = [0] * 512
LOG = [0] * 256
x = 1
for i in range(255):
    EXP[i] = x
    LOG[x] = i
    x <<= 1
    if x & 0x100:
        x ^= PRIM
for i in range(255, 512):
    EXP[i] = EXP[i - 255]


def mul(a, b):
    return 0 if a == 0 or b == 0 else EXP[LOG[a] + LOG[b]]


def inv(a):
    return EXP[255 - LOG[a]]


def pow_a(e):
    return EXP[e % 255]


def poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] ^= mul(a, b)
    return r


def poly_eval(p, x):  # p[0] = coeficiente de mayor grado
    y = 0
    for c in p:
        y = mul(y, x) ^ c
    return y


class RS:
    def __init__(self, e, step=11):
        self.e, self.step = e, step
        self.fcr = 128 - e
        g = [1]
        for j in range(128 - e, 128 + e):
            g = poly_mul(g, [1, pow_a(step * j)])
        self.g = g
        self.n, self.k = 255, 255 - 2 * e

    def encode(self, msg):
        assert len(msg) == self.k
        buf = list(msg) + [0] * (2 * self.e)
        for i in range(self.k):
            c = buf[i]
            if c:
                for j in range(1, len(self.g)):
                    buf[i + j] ^= mul(self.g[j], c)
        return list(msg) + buf[self.k:]

    def syndromes(self, r):
        return [poly_eval(r, pow_a(self.step * (self.fcr + i))) for i in range(2 * self.e)]

    def decode(self, r):
        """Devuelve (palabra corregida, nerr) o (None, motivo)."""
        s = self.syndromes(r)
        if not any(s):
            return list(r), 0
        # Berlekamp-Massey
        lam, b, L, m, bb = [1], [1], 0, 1, 1
        for nn in range(2 * self.e):
            d = s[nn]
            for i in range(1, L + 1):
                if i < len(lam):
                    d ^= mul(lam[i], s[nn - i])
            if d == 0:
                m += 1
            else:
                t = lam[:]
                coef = mul(d, inv(bb))
                lam = lam + [0] * (len(b) + m - len(lam))
                for i, bi in enumerate(b):
                    lam[i + m] ^= mul(coef, bi)
                if 2 * L <= nn:
                    L, b, bb, m = nn + 1 - L, t, d, 1
                else:
                    m += 1
        if L > self.e:
            return None, "fallo: grado del localizador mayor que E"
        # Chien: posicion p (potencia de x) es error si lam(X^-1) = 0 con X = beta^p
        pos = []
        for p in range(255):
            xi = pow_a(-self.step * p)
            y = 0
            for i, c in enumerate(lam):
                y ^= mul(c, pow_a(-self.step * p * i)) if c else 0
            if y == 0:
                pos.append(p)
        if len(pos) != L:
            return None, "fallo: raices del localizador distintas de su grado"
        # Omega = S(x) lam(x) mod x^(2E); S(x) = sum s_i x^i
        omega = [0] * (2 * self.e)
        for i in range(2 * self.e):
            for j, c in enumerate(lam):
                if i + j < 2 * self.e:
                    omega[i + j] ^= mul(s[i], c)
        out = list(r)
        for p in pos:
            xinv = pow_a(-self.step * p)
            om = 0
            for i, c in enumerate(omega):
                om ^= mul(c, pow_a(-self.step * p * i)) if c else 0
            dl = 0
            for i in range(1, len(lam), 2):
                dl ^= mul(lam[i], pow_a(-self.step * p * (i - 1))) if lam[i] else 0
            if dl == 0:
                return None, "fallo: derivada nula"
            xk = pow_a(self.step * p)
            val = mul(mul(pow_a(self.step * p * (1 - self.fcr)), om), inv(dl))
            out[255 - 1 - p] ^= val
        if any(self.syndromes(out)):
            return None, "fallo: sindromes no nulos tras corregir"
        return out, len(pos)


def inyectar(r, t, rng):
    r = list(r)
    for p in rng.sample(range(255), t):
        r[p] ^= rng.randrange(1, 256)
    return r




def entrelazar(cws):
    i = len(cws)
    return [cws[j % i][j // i] for j in range(255 * i)]


def desentrelazar(flujo, i):
    cws = [[0] * 255 for _ in range(i)]
    for j, b in enumerate(flujo):
        cws[j % i][j // i] = b
    return cws


def decodifica_bloque(rs, flujo, i):
    """Cuenta palabras recuperadas tras desentrelazar y decodificar."""
    ok = 0
    for cw in desentrelazar(flujo, i):
        out, _ = rs.decode(cw)
        ok += out is not None
    return ok


# ---- codigo convolucional K = 7, r = 1/2 ----
G1, G2 = 0o171, 0o133


def par(x):
    return bin(x).count("1") & 1


SAL = [[(par(((u << 6) | s) & G1) << 1) | (par(((u << 6) | s) & G2) ^ 1) for u in (0, 1)] for s in range(64)]


def conv_codifica(bits):
    s, out = 0, []
    for u in bits + [0] * 6:
        v = SAL[s][u]
        out += [v >> 1, v & 1]
        s = (u << 5) | (s >> 1)
    return out


def viterbi(rx):
    n = len(rx) // 2
    INF = 10 ** 9
    met = [INF] * 64
    met[0] = 0
    dec = []
    for t in range(n):
        r = (rx[2 * t] << 1) | rx[2 * t + 1]
        nm = [INF] * 64
        d = bytearray(64)
        for sp in range(64):
            m0 = met[sp]
            if m0 >= INF:
                continue
            for u in (0, 1):
                ns = (u << 5) | (sp >> 1)
                c = m0 + bin(SAL[sp][u] ^ r).count("1")
                if c < nm[ns]:
                    nm[ns] = c
                    d[ns] = sp & 1
        met = nm
        dec.append(d)
    s, bits = 0, []
    for t in range(n - 1, -1, -1):
        u = s >> 5
        bits.append(u)
        s = ((s & 31) << 1) | dec[t][s]
    bits.reverse()
    return bits[: n - 6]


def a_bits(octetos):
    return [(b >> (7 - k)) & 1 for b in octetos for k in range(8)]


def a_octetos(bits):
    return [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]


if __name__ == "__main__":
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rs = RS(16)
    rng = random.Random(94004)
    # A) rafaga contigua de B octetos en un bloque de I palabras
    print("A) Rafaga de B octetos consecutivos (valores aleatorios) en un bloque de I palabras RS(255,223); 10 inicios por caso")
    print("   I   umbral E*I   B=E*I: palabras recuperadas   B=E*I+1: palabras recuperadas")
    for i in (1, 2, 3, 4, 5, 8):
        fila = []
        for b in (16 * i, 16 * i + 1):
            tot = rec = 0
            for _ in range(10):
                cws = [rs.encode([rng.randrange(256) for _ in range(223)]) for _ in range(i)]
                fl = entrelazar(cws)
                ini = rng.randrange(0, len(fl) - b + 1)
                for k in range(ini, ini + b):
                    fl[k] ^= rng.randrange(1, 256)
                rec += decodifica_bloque(rs, fl, i)
                tot += i
            fila.append((rec, tot))
        print(f"  {i:2d}    {16 * i:4d}        {fila[0][0]:3d} de {fila[0][1]:3d}                  {fila[1][0]:3d} de {fila[1][1]:3d}")
        assert fila[0][0] == fila[0][1]
        assert fila[1][0] < fila[1][1]
    # B) concatenacion convolucional + RS
    print("B) Concatenacion: RS(255,223) externo + convolucional K=7 r=1/2 (Viterbi duro) interno, canal binario simetrico")
    print("   bloque = 5 palabras RS; el mismo patron de errores de canal se aplica a I=1 y a I=5; 6 bloques por p")
    print("   p canal  octetos erroneos tras Viterbi (por bloque)  palabras recuperadas I=1   palabras recuperadas I=5")
    crng = random.Random(94005)
    for p in (0.05, 0.07, 0.09):
        suma_err = 0
        r1 = r5 = 0
        for _ in range(6):
            cws = [rs.encode([crng.randrange(256) for _ in range(223)]) for _ in range(5)]
            patron = None
            res = {}
            for i in (1, 5):
                fl = entrelazar(cws) if i == 5 else [b for cw in cws for b in cw]
                tx = conv_codifica(a_bits(fl))
                if patron is None:
                    patron = [1 if crng.random() < p else 0 for _ in tx]
                rx = [a ^ b for a, b in zip(tx, patron)]
                dec = a_octetos(viterbi(rx))
                if i == 1:
                    suma_err += sum(a != b for a, b in zip(dec, fl))
                    # I = 1: palabras consecutivas, sin entrelazar
                    cwr = [dec[255 * k:255 * (k + 1)] for k in range(5)]
                    res[1] = sum(rs.decode(c)[0] is not None for c in cwr)
                else:
                    res[5] = decodifica_bloque(rs, dec, 5)
            r1 += res[1]
            r5 += res[5]
        print(f"   {p:5.2f}            {suma_err / 6:8.1f}                          {r1:3d} de 30                {r5:3d} de 30")
    print("Pruebas superadas.")
