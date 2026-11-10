#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C01: Reed-Solomon (255,223) sobre GF(2^8) y un LDPC de juguete.

Consultado (2026-11-10, CCSDS 131.0-B-5, sept. 2023): polinomio del campo F(x) = x^8+x^7+x^2+x+1; generador
g(x) = prod_{j=128-E}^{127+E} (x - alfa^(11 j)); E = 16 -> (255,223), E = 8 -> (255,239); simbolos de 8 bits.
NO implementado: la transformacion de base dual del estandar. Aqui se usa la base convencional (polinomica), de modo
que los octetos NO coinciden con los del estandar; la estructura algebraica y la capacidad de correccion si.
Datos: mensajes y errores SINTETICOS con semilla fija (random.Random(94001)). El LDPC es un codigo de JUGUETE
(Gallager (3,6), n = 120), NO el codigo (8160,7136) del estandar.
Segundas vias: sindromes nulos de la palabra de codigo; cota teorica t = E; el decodificador LDPC se prueba con
palabra de codigo nula (valida para un canal binario simetrico y un decodificador simetrico).
Tolerancias: igualdad exacta (aritmetica entera); tasas con 1e-12.
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


# ---------------- LDPC de juguete ----------------
def gallager(n, wc, wr, rng):
    m = n * wc // wr
    filas = m // wc
    h = []
    base = [[1 if j // wr == i else 0 for j in range(n)] for i in range(filas)]
    h += base
    for _ in range(wc - 1):
        perm = list(range(n))
        rng.shuffle(perm)
        h += [[row[perm[j]] for j in range(n)] for row in base]
    return h


def decodifica_bf(h, rec, itmax=50):
    n = len(rec)
    w = rec[:]
    for it in range(itmax):
        insat = [sum(w[j] for j in fila) % 2 for fila in H_IDX]
        if not any(insat):
            return w, it
        cuenta = [0] * n
        for fi, s in enumerate(insat):
            if s:
                for j in H_IDX[fi]:
                    cuenta[j] += 1
        mx = max(cuenta)
        for j in range(n):
            if cuenta[j] == mx:
                w[j] ^= 1
    return w, itmax


if __name__ == "__main__":
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert len(set(EXP[:255])) == 255 and pow_a(11 * 255) == 1 and len({pow_a(11 * i) for i in range(255)}) == 255
    print("Campo GF(2^8), F(x)=x^8+x^7+x^2+x+1: alfa y alfa^11 son primitivos (orden 255)")
    rng = random.Random(94001)
    for e in (16, 8):
        rs = RS(e)
        msg = [rng.randrange(256) for _ in range(rs.k)]
        cw = rs.encode(msg)
        nulo = not any(rs.syndromes(cw))
        print(f"RS({rs.n},{rs.k}) E={e}: grado g = {len(rs.g) - 1}, simbolos de paridad = {2 * e}, tasa = {rs.k / rs.n:.6f}, sindromes nulos = {nulo}")
        assert len(rs.g) - 1 == 2 * e and nulo and abs(rs.k / rs.n - (255 - 2 * e) / 255) < 1e-12
    rs = RS(16)
    print("RS(255,223), 200 palabras por fila, errores de simbolo en posiciones aleatorias:")
    print(" t errores  corregidas  fallo detectado  miscorreccion")
    res = {}
    for t in (0, 1, 8, 16, 17, 20, 32):
        ok = det = mis = 0
        for _ in range(200):
            msg = [rng.randrange(256) for _ in range(223)]
            cw = rs.encode(msg)
            r = inyectar(cw, t, rng)
            out, info = rs.decode(r)
            if out is None:
                det += 1
            elif out == cw:
                ok += 1
            else:
                mis += 1
        res[t] = (ok, det, mis)
        print(f"  {t:3d}        {ok:4d}          {det:4d}            {mis:4d}")
    assert all(res[t][0] == 200 for t in (0, 1, 8, 16))
    assert all(res[t][0] == 0 for t in (17, 20, 32))
    print("Con t <= E = 16 siempre se corrige; con t > 16 nunca se recupera la palabra (cota teorica).")
    # LDPC
    n, wc, wr = 120, 3, 6
    hrng = random.Random(94002)
    H = gallager(n, wc, wr, hrng)
    H_IDX = [[j for j in range(n) if fila[j]] for fila in H]
    assert all(len(f) == wr for f in H_IDX)
    print(f"LDPC de JUGUETE Gallager (3,6): n = {n}, {len(H)} ecuaciones, tasa de diseno >= {1 - len(H) / n:.2f}")
    print("  p canal   tramas sin error tras decodificar (de 400)   iteraciones medias")
    frs = []
    for p in (0.005, 0.01, 0.02, 0.04):
        buenas = 0
        its = 0
        lrng = random.Random(94003)
        for _ in range(400):
            rec = [1 if lrng.random() < p else 0 for _ in range(n)]
            w, it = decodifica_bf(H, rec)
            its += it
            buenas += (not any(w))
        frs.append(buenas)
        print(f"  {p:6.3f}     {buenas:4d}                                   {its / 400:.2f}")
    assert frs[0] >= frs[-1] and frs[0] > 300
    print("Pruebas superadas.")
