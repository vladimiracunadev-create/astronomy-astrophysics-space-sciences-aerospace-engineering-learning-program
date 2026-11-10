#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C03: trama de transferencia de telemetria (TM) con cabecera de 6 octetos, FHP y FECF.

Consultado (2026-11-10, CCSDS 132.0-B-3, oct. 2021): cabecera primaria de 6 octetos = version (2 bits, '00'), identificador de nave
SCID (10 bits), VCID (3 bits), bandera OCF (1 bit), contador de canal maestro (8 bits), contador de canal virtual (8 bits) y estado del
campo de datos (16 bits: bandera de cabecera secundaria 1, sincronia 1, orden de paquetes 1, id de longitud de segmento 2, puntero de
primera cabecera FHP 11); FHP = 11111111111 si ningun paquete empieza en la trama y 11111111110 para datos ociosos;
FECF de 16 bits, polinomio X^16+X^12+X^5+1 con registro inicial a unos.
NO consultado: el telecomando (CCSDS 232.0-B) y el formato de paquete espacial (CCSDS 133.0-B).
Los "paquetes" de este laboratorio son SINTETICOS: 2 octetos de longitud + carga util; no son paquetes CCSDS.
Parametros SINTETICOS: trama de 64 octetos, SCID = 0x2A5, VCID de datos = 1, OCF presente (4 octetos), semilla 94006.
Segundas vias: CRC bit a bit frente a CRC por tabla; valor de comprobacion de la cadena ASCII '123456789' (valor conocido de la
variante CRC-16/CCITT-FALSE, no consultado en una fuente); reensamblado frente a los paquetes originales.
Tolerancias: igualdad exacta; escapes del CRC frente a 2^-16 con intervalo de +-4 sigma.
"""
from __future__ import annotations
import platform, random, struct

LONG_TRAMA, LONG_CAB, LONG_OCF, LONG_FECF = 64, 6, 4, 2
LONG_DATOS = LONG_TRAMA - LONG_CAB - LONG_OCF - LONG_FECF
FHP_SIN_PAQUETE, FHP_OCIOSO = 0x7FF, 0x7FE


def crc16_bits(datos: bytes, ini=0xFFFF) -> int:
    reg = ini
    for b in datos:
        for k in range(7, -1, -1):
            bit = (b >> k) & 1
            top = (reg >> 15) & 1
            reg = (reg << 1) & 0xFFFF
            if top ^ bit:
                reg ^= 0x1021
    return reg


def _tabla():
    t = []
    for i in range(256):
        r = i << 8
        for _ in range(8):
            r = ((r << 1) ^ 0x1021) & 0xFFFF if r & 0x8000 else (r << 1) & 0xFFFF
        t.append(r)
    return t


TAB = _tabla()


def crc16_tabla(datos: bytes, ini=0xFFFF) -> int:
    reg = ini
    for b in datos:
        reg = ((reg << 8) & 0xFFFF) ^ TAB[((reg >> 8) ^ b) & 0xFF]
    return reg


def arma_trama(scid, vcid, mcfc, vcfc, fhp, datos, ocf=b"\x00\x00\x00\x00", sync=0):
    assert len(datos) == LONG_DATOS and len(ocf) == LONG_OCF
    w0 = (0 << 14) | (scid << 4) | (vcid << 1) | 1  # OCF presente
    estado = (0 << 15) | (sync << 14) | (0 << 13) | (3 << 11) | fhp
    cab = struct.pack(">HBBH", w0, mcfc & 0xFF, vcfc & 0xFF, estado)
    cuerpo = cab + datos + ocf
    return cuerpo + struct.pack(">H", crc16_bits(cuerpo))


def lee_trama(trama):
    if crc16_bits(trama) != 0:  # el CRC calculado sobre trama + FECF da cero
        return None
    w0, mcfc, vcfc, estado = struct.unpack(">HBBH", trama[:6])
    return {"version": w0 >> 14, "scid": (w0 >> 4) & 0x3FF, "vcid": (w0 >> 1) & 7, "ocf": w0 & 1, "mcfc": mcfc, "vcfc": vcfc,
            "sync": (estado >> 14) & 1, "fhp": estado & 0x7FF, "datos": trama[6:6 + LONG_DATOS]}


def empaqueta(paquetes, scid, vcid, mc0, vc0):
    """Coloca paquetes (2 octetos de longitud + carga) en tramas de datos; devuelve las tramas."""
    flujo = b"".join(struct.pack(">H", len(p)) + p for p in paquetes)
    inicios, pos = [], 0
    for p in paquetes:
        inicios.append(pos)
        pos += 2 + len(p)
    tramas, mc, vc = [], mc0, vc0
    for off in range(0, len(flujo), LONG_DATOS):
        trozo = flujo[off:off + LONG_DATOS].ljust(LONG_DATOS, b"\x00")
        cand = [s - off for s in inicios if off <= s < off + LONG_DATOS]
        fhp = cand[0] if cand else FHP_SIN_PAQUETE
        tramas.append(arma_trama(scid, vcid, mc, vc, fhp, trozo))
        mc, vc = (mc + 1) & 0xFF, (vc + 1) & 0xFF
    return tramas


def reensambla(tramas):
    """Receptor: valida CRC, detecta huecos con el contador de canal virtual y resincroniza con el FHP."""
    paquetes, buf, esperado, huecos, rechazadas = [], b"", None, 0, 0
    sincronizado = False
    for t in tramas:
        f = lee_trama(t)
        if f is None:
            rechazadas += 1
            continue
        if esperado is not None and f["vcfc"] != esperado:
            huecos += (f["vcfc"] - esperado) & 0xFF
            buf, sincronizado = b"", False
        esperado = (f["vcfc"] + 1) & 0xFF
        datos = f["datos"]
        if not sincronizado:
            if f["fhp"] == FHP_SIN_PAQUETE:
                continue
            datos = datos[f["fhp"]:]
            sincronizado = True
        buf += datos
        while len(buf) >= 2:
            n = struct.unpack(">H", buf[:2])[0]
            if n == 0:
                buf = b""  # relleno de la ultima trama
                break
            if len(buf) < 2 + n:
                break
            paquetes.append(buf[2:2 + n])
            buf = buf[2 + n:]
    return paquetes, huecos, rechazadas


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert crc16_bits(b"123456789") == crc16_tabla(b"123456789") == 0x29B1
    print(f"CRC-16 (poly 0x1021, inicial 0xFFFF) de '123456789': bit a bit = tabla = 0x{crc16_bits(b'123456789'):04X}")
    # a) campos de la cabecera
    t = arma_trama(0x2A5, 1, 255, 7, 0x00A, bytes(range(LONG_DATOS)))
    f = lee_trama(t)
    print(f"Trama de {len(t)} octetos: cabecera = {t[:6].hex()}  campos = version {f['version']}, SCID 0x{f['scid']:03X}, VCID {f['vcid']}, OCF {f['ocf']}, MCFC {f['mcfc']}, VCFC {f['vcfc']}, FHP {f['fhp']}")
    assert (f["version"], f["scid"], f["vcid"], f["mcfc"], f["vcfc"], f["fhp"]) == (0, 0x2A5, 1, 255, 7, 10)
    assert len(t) == LONG_TRAMA and LONG_DATOS == 52
    # b) deteccion de errores
    rng = random.Random(94006)

    def base():
        return arma_trama(0x2A5, 1, rng.randrange(256), rng.randrange(256), 0, bytes(rng.randrange(256) for _ in range(LONG_DATOS)))

    det1 = det2 = 0
    for _ in range(500):
        tr = bytearray(base())
        k = rng.randrange(len(tr) * 8)
        tr[k // 8] ^= 1 << (k % 8)
        det1 += lee_trama(bytes(tr)) is None
        k2 = rng.randrange(len(tr) * 8)
        while k2 == k:
            k2 = rng.randrange(len(tr) * 8)
        tr[k2 // 8] ^= 1 << (k2 % 8)
        det2 += lee_trama(bytes(tr)) is None
    print(f"Errores de 1 bit detectados: {det1} de 500; de 2 bits: {det2} de 500")
    rafaga_ok = 0
    for L in range(1, 17):
        for _ in range(50):
            tr = bytearray(base())
            ini = rng.randrange(len(tr) * 8 - L + 1)
            pat = ([1] + [rng.randrange(2) for _ in range(L - 2)] + [1]) if L > 1 else [1]
            for j, bit in enumerate(pat):
                if bit:
                    k = ini + j
                    tr[k // 8] ^= 1 << (7 - k % 8)
            rafaga_ok += lee_trama(bytes(tr)) is None
    print(f"Rafagas de 1 a 16 bits detectadas: {rafaga_ok} de 800")
    assert det1 == 500 and det2 == 500 and rafaga_ok == 800
    escapes, n = 0, 400000
    for _ in range(n):
        tr = bytes(rng.randrange(256) for _ in range(LONG_TRAMA))
        escapes += crc16_tabla(tr) == 0
    esp = n / 65536
    print(f"Tramas aleatorias que pasan el CRC por azar: {escapes} de {n} (esperado {esp:.2f} +- {esp ** 0.5:.2f})")
    assert abs(escapes - esp) <= 4 * esp ** 0.5
    # c) empaquetado, perdida de tramas y resincronizacion
    paquetes = [bytes([i % 251 + 1] * (5 + (i * 7) % 40)) for i in range(60)]
    tramas = empaqueta(paquetes, 0x2A5, 1, 250, 250)  # los contadores dan la vuelta en 255 -> 0
    rx, huecos, rech = reensambla(tramas)
    print(f"Sin perdidas: {len(tramas)} tramas, {len(rx)} de {len(paquetes)} paquetes recuperados, huecos {huecos}; contador inicial 250 con vuelta modulo 256")
    assert rx == paquetes and huecos == 0
    perdidas = {5, 6, 20}
    rx2, huecos2, _ = reensambla([t for i, t in enumerate(tramas) if i not in perdidas])
    print(f"Con {len(perdidas)} tramas perdidas (indices {sorted(perdidas)}): huecos detectados por el contador = {huecos2}, paquetes recuperados = {len(rx2)} de {len(paquetes)}")
    assert huecos2 == 3 and all(p in paquetes for p in rx2) and len(rx2) < len(paquetes)
    mal = list(tramas)
    b = bytearray(mal[10])
    b[20] ^= 0x40
    mal[10] = bytes(b)
    rx3, huecos3, rech3 = reensambla(mal)
    print(f"Con 1 trama corrupta: rechazadas por CRC = {rech3}, huecos = {huecos3}, paquetes recuperados = {len(rx3)} de {len(paquetes)}")
    assert rech3 == 1 and huecos3 == 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
