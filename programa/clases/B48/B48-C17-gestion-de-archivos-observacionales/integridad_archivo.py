"""Integridad de un archivo: vectores de prueba de SHA-256 y CRC-32, detección de errores y colisiones.

Datos: vector de prueba SHA-256 de la cadena "abc" (FIPS 180, valor conocido) y valor de verificación
CRC-32 de "123456789" (0xCBF43926, valor de uso común); NO se consultaron esas fuentes en esta sesión: se
comprueban contra hashlib y zlib de la biblioteca estándar. Bloques y errores SINTÉTICOS.
Modelo: una función hash truncada a b bits deja pasar una corrupción aleatoria con probabilidad 2^-b;
con n archivos, P(alguna colisión) ~ 1 - exp(-n (n - 1) / 2^(b + 1)) (problema del cumpleaños).
Segunda vía: simulación con semilla 20261109.
Supuestos: hash tratado como función aleatoria uniforme; corrupciones independientes del contenido.
Tolerancia: 4 desviaciones binomiales; cambio de un bit detectado siempre por CRC-32 en bloques de 4096 bytes.
"""
import hashlib
import math
import random
import zlib

SHA_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def h(b, bits):
    return int.from_bytes(hashlib.sha256(b).digest(), "big") >> (256 - bits)


def calc():
    rng = random.Random(20261109)
    sha = hashlib.sha256(b"abc").hexdigest()
    crc = zlib.crc32(b"123456789")
    # un bit volteado en bloques de 4096 bytes
    detectados = 0
    pruebas = 3000
    for _ in range(pruebas):
        bloque = bytearray(rng.randbytes(4096))
        c0 = zlib.crc32(bytes(bloque))
        i = rng.randrange(4096 * 8)
        bloque[i // 8] ^= 1 << (i % 8)
        detectados += zlib.crc32(bytes(bloque)) != c0
    # corrupción aleatoria con hash de 10 bits
    bits = 10
    n = 400000
    pasan = 0
    for k in range(n):
        a = rng.randbytes(16)
        b = rng.randbytes(16)
        pasan += h(a, bits) == h(b, bits)
    p = 2.0 ** -bits
    # cumpleaños con 24 bits y 4000 archivos
    nf, bb, reps = 4000, 24, 400
    teo = 1 - math.exp(-nf * (nf - 1) / 2 ** (bb + 1))
    col = 0
    for _ in range(reps):
        vistos = set()
        for _ in range(nf):
            v = rng.getrandbits(bb)
            if v in vistos:
                col += 1
                break
            vistos.add(v)
    return dict(sha=sha, crc=crc, det=detectados, pruebas=pruebas, pasan=pasan, n=n, p=p, teo=teo, col=col / reps, reps=reps)


def main():
    Q = calc()
    print(f"SHA-256('abc') = {Q['sha']}")
    print(f"CRC-32('123456789') = {Q['crc']:#010x}")
    print(f"Un bit volteado en bloques de 4096 bytes: detectados {Q['det']} de {Q['pruebas']}")
    esp = Q["n"] * Q["p"]
    print(f"Hash de 10 bits: pasan {Q['pasan']} de {Q['n']} (esperados {esp:.1f}, sigma {math.sqrt(esp):.1f})")
    print(f"Colisión entre 4000 archivos con 24 bits: analítica {Q['teo']:.4f} | simulada {Q['col']:.4f}")
    assert Q["sha"] == SHA_ABC and Q["crc"] == 0xCBF43926
    assert Q["det"] == Q["pruebas"]
    assert abs(Q["pasan"] - esp) < 4 * math.sqrt(esp)
    sig = math.sqrt(Q["teo"] * (1 - Q["teo"]) / Q["reps"])
    assert abs(Q["col"] - Q["teo"]) < 4 * sig
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
