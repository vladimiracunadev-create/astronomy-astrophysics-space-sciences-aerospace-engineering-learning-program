#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C12. Telecomandos: deteccion de errores con CRC-16 (polinomio 0x1021, estandar CRC-16/CCITT-FALSE), aceptacion por
ventana deslizante de numeros de secuencia modulo 256 (estilo FARM) y eficiencia de retransmision go-back-N.
Los parametros exactos de los estandares de telecomando CCSDS NO se consultaron; todo es una ilustracion con datos SINTETICOS (semilla 89)."""
import random, sys

def crc16(datos, init=0xFFFF):
    crc = init
    for b in datos:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc

def clasifica(ns, vr, pw, nw, mod=256):
    """Ventana de aceptacion: ns recibido, vr esperado. Devuelve la accion."""
    d = (ns - vr) % mod
    if d == 0:
        return "acepta"
    if d < pw:
        return "retransmitir"       # dentro de la ventana positiva pero fuera de orden
    if d >= mod - nw:
        return "descarta"           # dentro de la ventana negativa (duplicado antiguo)
    return "bloqueo"                # fuera de ambas ventanas

def eficiencia_gbn_teo(p, n):
    return (1 - p) / (1 - p + n * p)

def eficiencia_gbn_sim(p, n, tramas, rng):
    ranuras = 0
    for _ in range(tramas):
        ranuras += 1
        while rng.random() < p:      # intento fallido: se pierden n ranuras antes de reintentar
            ranuras += n
            ranuras += 0
        # el exito consume 1 ranura (ya contada arriba)
    return tramas / ranuras

def calcular():
    R = {}
    R["check"] = crc16(b"123456789")
    rng = random.Random(89)
    trama = bytes(rng.getrandbits(8) for _ in range(64))
    base = crc16(trama)
    # todos los errores de 1 y 2 bits en una trama de 64 octetos
    nbits = 8 * len(trama)
    det1 = det2 = tot2 = 0
    for i in range(nbits):
        t = bytearray(trama)
        t[i // 8] ^= 1 << (i % 8)
        det1 += crc16(bytes(t)) != base
    for i in range(0, nbits, 7):
        for j in range(i + 1, nbits, 11):
            t = bytearray(trama)
            t[i // 8] ^= 1 << (i % 8)
            t[j // 8] ^= 1 << (j % 8)
            det2 += crc16(bytes(t)) != base
            tot2 += 1
    R["det1"], R["n1"], R["det2"], R["n2"] = det1, nbits, det2, tot2
    # rafagas de hasta 16 bits
    detr = totr = 0
    for ini in range(0, nbits - 16, 13):
        for largo in (8, 12, 16):
            t = bytearray(trama)
            for k in range(largo):
                pos = ini + k
                if k in (0, largo - 1) or (k % 2 == 0):
                    t[pos // 8] ^= 1 << (pos % 8)
            detr += crc16(bytes(t)) != base
            totr += 1
    R["detr"], R["totr"] = detr, totr
    # corrupcion fuerte aleatoria: fraccion no detectada ~ 2^-16
    n_sim = 300_000
    nd = 0
    for _ in range(n_sim):
        r = bytes(rng.getrandbits(8) for _ in range(4))
        nd += crc16(r) == crc16(b"\x00\x00\x00\x00")
    R["no_det"], R["n_sim"] = nd, n_sim
    R["teo_no_det"] = 2 ** -16
    # ventana
    cuenta = {}
    for ns in range(256):
        a = clasifica(ns, 10, 10, 10)
        cuenta[a] = cuenta.get(a, 0) + 1
    R["ventana"] = cuenta
    # go-back-N
    R["gbn"] = {}
    for p, n in ((0.01, 8), (0.1, 8), (0.1, 32)):
        R["gbn"][(p, n)] = (eficiencia_gbn_teo(p, n), eficiencia_gbn_sim(p, n, 200_000, rng))
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"CRC-16 (0x1021, init 0xFFFF) de '123456789' = 0x{R['check']:04X} (valor de verificacion publicado de CRC-16/CCITT-FALSE: 0x29B1)")
    print(f"Errores de 1 bit detectados: {R['det1']}/{R['n1']} ; de 2 bits (muestra): {R['det2']}/{R['n2']} ; rafagas <= 16 bits: {R['detr']}/{R['totr']}")
    print(f"Corrupcion aleatoria no detectada: {R['no_det']}/{R['n_sim']} = {R['no_det']/R['n_sim']:.2e} ; teoria 2^-16 = {R['teo_no_det']:.2e}")
    print(f"Ventana (V(R) = 10, positiva 10, negativa 10) sobre 256 numeros: {R['ventana']}")
    for (p, n), (t, s) in R["gbn"].items():
        print(f"Go-back-N p = {p:.2f}, ventana {n:2d}: eficiencia teorica = {t:.4f} ; simulada = {s:.4f}")
    assert R["check"] == 0x29B1 and R["det1"] == R["n1"] and R["det2"] == R["n2"] and R["detr"] == R["totr"]
    assert R["ventana"]["acepta"] == 1 and R["ventana"]["retransmitir"] == 9 and R["ventana"]["descarta"] == 10 and R["ventana"]["bloqueo"] == 236
    for t, s in R["gbn"].values():
        assert abs(t - s) / t < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
