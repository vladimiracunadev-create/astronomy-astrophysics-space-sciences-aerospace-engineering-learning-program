#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C06: pruebas de conformidad de un codificador/decodificador de tramas TM, con mutantes y trazabilidad.

Requisitos tomados de lo CONSULTADO el 2026-11-10 en CCSDS 132.0-B-3 (oct. 2021): version '00' en los bits 0-1; SCID de 10 bits; VCID de 3
bits; bandera OCF de 1 bit (1 = presente); contadores de canal maestro y virtual de 8 bits; estado de 16 bits con FHP de 11 bits (11111111111 =
ningun paquete empieza en la trama); FECF de 16 bits con X^16+X^12+X^5+1 y registro inicial a unos, en los dos ultimos octetos.
Esto NO es una suite de conformidad oficial ni cubre todos los "shall" del estandar; el telecomando no se consulto. El empaquetado de paquetes
sinteticos (REQ-11) es una convencion propia del laboratorio, no del estandar.
El IUT (implementation under test) es la implementacion de B94-C03 con una correccion (rechazar version distinta de 0 y longitud distinta de 64)
y variantes defectuosas (mutantes) generadas con banderas. Oraculo independiente: cabecera construida cadena de bits a cadena de bits y CRC
por tabla. Datos SINTETICOS, semilla 94008. Tolerancias: igualdad exacta.
"""
from __future__ import annotations
import platform, random, struct

LT, LD = 64, 52
FHP_NINGUNO = 0x7FF


def crc_tabla(datos, ini=0xFFFF):
    reg = ini
    for b in datos:
        reg ^= b << 8
        for _ in range(8):
            reg = ((reg << 1) ^ 0x1021) & 0xFFFF if reg & 0x8000 else (reg << 1) & 0xFFFF
    return reg


class IUT:
    def __init__(self, m=frozenset(), corregido=True):
        self.m, self.corregido = m, corregido

    def crc(self, datos):
        poly = 0x8005 if "poly" in self.m else 0x1021
        reg = 0 if "init0" in self.m else 0xFFFF
        for b in datos:
            for k in range(7, -1, -1):
                top = (reg >> 15) & 1
                reg = (reg << 1) & 0xFFFF
                if top ^ ((b >> k) & 1):
                    reg ^= poly
        return reg

    def arma(self, scid, vcid, mcfc, vcfc, fhp, datos, ocf=b"\0\0\0\0"):
        m = self.m
        w0 = (scid << (3 if "scid_shift" in m else 4)) | ((vcid & (3 if "vcid_mask" in m else 7)) << 1) | (0 if "ocf0" in m else 1)
        est = ((1 << 13) if "pktorder" in m else 0) | (3 << 11) | fhp
        mc = min(mcfc, 255) if "nowrap" in m else mcfc & 0xFF
        cab = struct.pack("<H" if "little" in m else ">H", w0) + bytes([mc, vcfc & 0xFF]) + struct.pack(">H", est)
        cuerpo = cab + datos + ocf
        base = cuerpo[6:] if "crc_nohdr" in m else cuerpo
        return cuerpo + struct.pack(">H", self.crc(base))

    def lee(self, t):
        m = self.m
        if self.corregido and "nolength" not in m and len(t) != LT:
            return None
        if "nocrc" not in m and self.crc(t[6:] if "crc_nohdr" in m else t) != 0:
            return None
        w0, mc, vc, est = struct.unpack(">HBBH", t[:6])
        if self.corregido and "noversion" not in m and (w0 >> 14) != 0:
            return None
        return {"version": w0 >> 14, "scid": (w0 >> 4) & 0x3FF, "vcid": (w0 >> 1) & 7, "ocf": w0 & 1, "mcfc": mc, "vcfc": vc,
                "fhp": est & 0x7FF, "datos": t[6:6 + LD]}

    def empaqueta(self, paquetes, scid, vcid, mc0, vc0):
        flujo = b"".join(struct.pack(">H", len(p)) + p for p in paquetes)
        inicios, pos = [], 0
        for p in paquetes:
            inicios.append(pos)
            pos += 2 + len(p)
        out, mc, vc = [], mc0, vc0
        relleno = b"\xff" if "pad_ff" in self.m else b"\0"
        ninguno = 0x7FE if "fhp_ninguno" in self.m else FHP_NINGUNO
        for off in range(0, len(flujo), LD):
            trozo = flujo[off:off + LD].ljust(LD, relleno)
            cand = [s - off for s in inicios if off <= s < off + LD]
            out.append(self.arma(scid, vcid, mc, vc, cand[0] if cand else ninguno, trozo))
            mc, vc = mc + 1, vc + 1
        return out

    def reensambla(self, tramas):
        pk, buf, esp, huecos, sinc = [], b"", None, 0, False
        for t in tramas:
            f = self.lee(t)
            if f is None:
                continue
            if esp is not None and f["vcfc"] != esp:
                huecos += (f["vcfc"] - esp) & 0xFF
                buf, sinc = b"", False
            esp = (f["vcfc"] + 1) & 0xFF
            d = f["datos"]
            if not sinc:
                if f["fhp"] >= 0x7FE:
                    continue
                d, sinc = d[f["fhp"]:], True
            buf += d
            while len(buf) >= 2:
                n = struct.unpack(">H", buf[:2])[0]
                if n == 0 or len(buf) < 2 + n:
                    if n == 0:
                        buf = b""
                    break
                pk.append(buf[2:2 + n])
                buf = buf[2 + n:]
        return pk, huecos


def oraculo(scid, vcid, mcfc, vcfc, fhp, datos, ocf=b"\0\0\0\0"):
    bits = "00" + format(scid, "010b") + format(vcid, "03b") + "1" + format(mcfc, "08b") + format(vcfc, "08b") + "000" + "11" + format(fhp, "011b")
    cab = int(bits, 2).to_bytes(6, "big")
    cuerpo = cab + datos + ocf
    return cuerpo + crc_tabla(cuerpo).to_bytes(2, "big")


# ---------------- pruebas ----------------
VEC = [(0x2A5, 1, 255, 7, 10), (0x3FF, 7, 0, 255, 0x7FF), (0x000, 0, 128, 0, 0), (0x155, 5, 1, 2, 51)]
PAQ = [bytes([i % 250 + 1] * (5 + (i * 7) % 40)) for i in range(30)]


def datos52(rng):
    return bytes(rng.randrange(256) for _ in range(LD))


def t01(u):  # cabecera y FECF frente al oraculo
    rng = random.Random(94008)
    return all(u.arma(*v, d) == oraculo(*v, d) for v in VEC for d in [datos52(rng)])


def t02(u):  # valor de comprobacion del CRC
    return u.crc(b"123456789") == 0x29B1


def t03(u):  # recalcular el FECF sobre trama + FECF da cero
    rng = random.Random(94009)
    return all(crc_tabla(u.arma(*v, datos52(rng))) == 0 for v in VEC)


def t04(u):  # ida y vuelta de campos
    rng = random.Random(94010)
    for v in VEC:
        f = u.lee(u.arma(*v, datos52(rng)))
        if f is None or (f["scid"], f["vcid"], f["mcfc"], f["vcfc"], f["fhp"], f["ocf"], f["version"]) != (v[0], v[1], v[2], v[3], v[4], 1, 0):
            return False
    return True


def t05(u):  # negativa: un bit corrupto se rechaza
    rng = random.Random(94011)
    for _ in range(60):
        t = bytearray(u.arma(*VEC[0], datos52(rng)))
        k = rng.randrange(len(t) * 8)
        t[k // 8] ^= 1 << (k % 8)
        if u.lee(bytes(t)) is not None:
            return False
    return True


def t06(u):  # negativa: version distinta de 00 se rechaza (con CRC valido)
    cuerpo = bytearray(oraculo(*VEC[0], bytes(LD)))[:-2]
    cuerpo[0] |= 0x40
    return u.lee(bytes(cuerpo) + crc_tabla(bytes(cuerpo)).to_bytes(2, "big")) is None


def t07(u):  # negativa: longitud distinta de la fija se rechaza (con CRC valido)
    cuerpo = oraculo(*VEC[0], bytes(LD))[:-2] + b"\0\0"
    return u.lee(cuerpo + crc_tabla(cuerpo).to_bytes(2, "big")) is None


def t08(u):  # contadores modulo 256 en una secuencia que da la vuelta
    tr = u.empaqueta(PAQ, 0x2A5, 1, 250, 253)
    cab = [u.lee(t) for t in tr[:12]]
    return all(f is not None for f in cab) and [f["mcfc"] for f in cab] == [(250 + i) & 0xFF for i in range(12)] and [f["vcfc"] for f in cab] == [(253 + i) & 0xFF for i in range(12)]


def t09(u):  # FHP: 0x7FF si ningun paquete empieza, y desplazamiento correcto si empieza
    paq = [b"\x01" * 150, b"\x02" * 10]
    tr = [u.lee(t) for t in u.empaqueta(paq, 0x2A5, 1, 0, 0)]
    return tr[0]["fhp"] == 0 and tr[1]["fhp"] == FHP_NINGUNO and tr[2]["fhp"] == 2 + 150 - 2 * LD


def t10(u):  # reensamblado sin perdidas
    return u.reensambla(u.empaqueta(PAQ, 0x2A5, 1, 250, 250))[0] == PAQ


def t11(u):  # deteccion de huecos y paquetes validos tras ellos
    tr = u.empaqueta(PAQ, 0x2A5, 1, 0, 0)
    pk, huecos = u.reensambla([t for i, t in enumerate(tr) if i not in (3, 4)])
    return huecos == 2 and all(p in PAQ for p in pk) and 0 < len(pk) < len(PAQ)


def t12(u):  # bandera OCF y octetos de OCF en su sitio
    t = u.arma(0x2A5, 1, 0, 0, 0, bytes(LD), ocf=b"\xde\xad\xbe\xef")
    return (t[1] & 1) == 1 and t[58:62] == b"\xde\xad\xbe\xef"


PRUEBAS = [("T01", t01, ["REQ-01", "REQ-02", "REQ-03", "REQ-04", "REQ-05", "REQ-06", "REQ-07", "REQ-08"]),
           ("T02", t02, ["REQ-08"]), ("T03", t03, ["REQ-08", "REQ-09"]), ("T04", t04, ["REQ-01", "REQ-02", "REQ-03", "REQ-05", "REQ-06"]),
           ("T05", t05, ["REQ-10"]), ("T06", t06, ["REQ-01", "REQ-10"]), ("T07", t07, ["REQ-10"]),
           ("T08", t08, ["REQ-05", "REQ-06"]), ("T09", t09, ["REQ-07"]), ("T10", t10, ["REQ-11"]),
           ("T11", t11, ["REQ-06", "REQ-11"]), ("T12", t12, ["REQ-04"])]
REQ = {"REQ-01": "version '00' en bits 0-1", "REQ-02": "SCID de 10 bits (bits 2-11)", "REQ-03": "VCID de 3 bits (bits 12-14)",
       "REQ-04": "bandera OCF (bit 15) = 1 si hay OCF", "REQ-05": "contador de canal maestro de 8 bits, modulo 256",
       "REQ-06": "contador de canal virtual de 8 bits, modulo 256", "REQ-07": "FHP de 11 bits; 11111111111 si ningun paquete empieza",
       "REQ-08": "FECF: X^16+X^12+X^5+1, registro inicial a unos", "REQ-09": "FECF en los dos ultimos octetos; el receptor lo verifica",
       "REQ-10": "rechazar tramas corruptas, de version no valida o de longitud no fija", "REQ-11": "(propio, no del estandar) reensamblado de paquetes sinteticos"}
MUTANTES = [("init0", "FECF con registro inicial a ceros"), ("poly", "FECF con polinomio 0x8005"), ("scid_shift", "SCID desplazado 3 bits en vez de 4"),
            ("vcid_mask", "VCID limitado a 2 bits"), ("ocf0", "bandera OCF siempre 0"), ("nowrap", "contador maestro satura en 255"),
            ("pktorder", "bandera de orden de paquetes a 1"), ("little", "primera palabra en little endian"),
            ("crc_nohdr", "FECF sin cubrir la cabecera"), ("nocrc", "el receptor no verifica el FECF"),
            ("noversion", "el receptor no comprueba la version"), ("nolength", "el receptor no comprueba la longitud"),
            ("fhp_ninguno", "FHP 'ninguno' = 0x7FE (codigo de datos ociosos)"), ("pad_ff", "relleno con 0xFF en vez de 0x00")]


def corre(u, ids=None):
    res = {}
    for pid, f, _ in PRUEBAS:
        if ids is None or pid in ids:
            try:
                res[pid] = bool(f(u))
            except Exception:
                res[pid] = False
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("1) Suite contra la implementacion de B94-C03 sin corregir (IUT v1):")
    r1 = corre(IUT(corregido=False))
    print("   fallan: " + (", ".join(k for k, v in r1.items() if not v) or "ninguna"))
    assert [k for k, v in r1.items() if not v] == ["T06", "T07"]
    print("2) Suite contra el IUT corregido (v2):")
    r2 = corre(IUT())
    print(f"   superadas {sum(r2.values())} de {len(r2)}")
    assert all(r2.values())
    print("3) Trazabilidad requisito -> pruebas:")
    for rid, txt in REQ.items():
        ps = [p for p, _, rs in PRUEBAS if rid in rs]
        print(f"   {rid} {txt}: {', '.join(ps)} ({len(ps)})")
        assert ps
    print("4) Mutantes (cada uno con un defecto, sobre el IUT v2):")
    pos = {"T01", "T02", "T03", "T04", "T08", "T09", "T10", "T11", "T12"}
    muertos = muertos_pos = 0
    for mid, txt in MUTANTES:
        r = corre(IUT(frozenset([mid])))
        caen = [k for k, v in r.items() if not v]
        muertos += bool(caen)
        muertos_pos += any(k in pos for k in caen)
        print(f"   {mid:12s} {txt:55s} -> {'MUERTO por ' + ','.join(caen) if caen else 'SOBREVIVE'}")
    n = len(MUTANTES)
    print(f"Puntuacion de mutantes con la suite completa: {muertos} de {n} = {100 * muertos / n:.1f} %")
    print(f"Puntuacion solo con pruebas positivas (sin T05-T07): {muertos_pos} de {n} = {100 * muertos_pos / n:.1f} %")
    assert muertos < n and muertos_pos < muertos
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
