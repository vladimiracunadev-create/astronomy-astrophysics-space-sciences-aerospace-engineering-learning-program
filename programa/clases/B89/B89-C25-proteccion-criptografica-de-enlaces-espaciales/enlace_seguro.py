#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C25. Proteccion criptografica de enlaces espaciales: asociacion de seguridad, autenticacion de tramas, ventana anti-repeticion y sobrecarga.
*** SOLO DIDACTICO: usa HMAC-SHA256 de la biblioteca estandar como sustituto de la autenticacion; NO implementa AES-GCM ni el protocolo SDLS
y no debe usarse como criptografia de produccion. *** La CCSDS 355.0-B-2 (consultada) indica AES-GCM con clave de 256 bits como base de interoperabilidad.
Tamanos de campos ILUSTRATIVOS. Claves, tramas y ataques SINTETICOS (semilla 89)."""
import hashlib, hmac, random, sys

CLAVE = bytes(range(32))            # 256 bits SINTETICA (no usar jamas una clave publicada)
SPI_B, IV_B, MAC_B = 2, 12, 16      # octetos ILUSTRATIVOS
VENTANA = 64

def etiqueta(clave, spi, asn, carga, mac_bytes=MAC_B):
    msg = spi.to_bytes(2, "big") + asn.to_bytes(8, "big") + carga
    return hmac.new(clave, msg, hashlib.sha256).digest()[:mac_bytes]

class Receptor:
    def __init__(self, clave, ventana=VENTANA, mac_bytes=MAC_B):
        self.clave, self.w, self.mac_bytes = clave, ventana, mac_bytes
        self.max_asn = -1
        self.vistos = set()

    def procesar(self, spi, asn, carga, tag):
        if not hmac.compare_digest(tag, etiqueta(self.clave, spi, asn, carga, self.mac_bytes)):
            return "rechazada: autenticacion"
        if asn <= self.max_asn - self.w:
            return "rechazada: fuera de ventana"
        if asn in self.vistos:
            return "rechazada: repeticion"
        self.vistos.add(asn)
        self.max_asn = max(self.max_asn, asn)
        return "aceptada"

def calcular():
    R = {}
    rng = random.Random(89)
    tx = lambda asn, carga=b"TC-CMD": (7, asn, carga, etiqueta(CLAVE, 7, asn, carga))
    rx = Receptor(CLAVE)
    R["escenario"] = []
    def paso(nombre, trama):
        R["escenario"].append((nombre, rx.procesar(*trama)))
    paso("ASN 0 legitima", tx(0))
    paso("ASN 1 legitima", tx(1))
    paso("ASN 1 repetida", tx(1))
    paso("ASN 5 legitima (salto)", tx(5))
    paso("ASN 3 legitima (tarde, dentro de la ventana)", tx(3))
    paso("ASN 3 repetida", tx(3))
    t = tx(6)
    manipulada = (t[0], t[1], b"TC-CMX", t[3])
    paso("ASN 6 con la carga alterada", manipulada)
    paso("ASN 200 legitima", tx(200))
    paso("ASN 100 legitima (fuera de la ventana de 64)", tx(100))
    paso("ASN 7 con etiqueta aleatoria", (7, 7, b"TC-CMD", bytes(rng.getrandbits(8) for _ in range(MAC_B))))
    R["aceptadas"] = sum(1 for _, r in R["escenario"] if r == "aceptada")
    # alteracion de un bit en 1000 tramas
    det = 0
    for i in range(1000):
        carga = bytes(rng.getrandbits(8) for _ in range(32))
        tag = etiqueta(CLAVE, 1, i, carga)
        b = bytearray(carga)
        k = rng.randrange(8 * len(b))
        b[k // 8] ^= 1 << (k % 8)
        det += tag != etiqueta(CLAVE, 1, i, bytes(b))
    R["det_bit"] = det
    # falsificacion con etiqueta de 16 bits: tasa esperada 2^-16
    n = 300_000
    objetivo = etiqueta(CLAVE, 9, 1, b"X", 2)
    aciertos = sum(1 for _ in range(n) if rng.getrandbits(16).to_bytes(2, "big") == objetivo)
    R["forja"] = (aciertos, n)
    R["forja_teo"] = n * 2 ** -16
    # sobrecarga
    k_oct = 223 * 5
    R["sobrecarga"] = SPI_B + IV_B + MAC_B
    R["datos"] = k_oct - 8 - R["sobrecarga"]
    R["efic_antes"] = (k_oct - 8) / k_oct
    R["efic_despues"] = R["datos"] / k_oct
    R["k_oct"] = k_oct
    R["bits_clave"] = 8 * len(CLAVE)
    R["combinaciones"] = 2 ** 128
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("DIDACTICO: HMAC-SHA256 truncado a 16 octetos como sustituto; NO es AES-GCM ni SDLS. Clave sintetica de", R["bits_clave"], "bits")
    for nombre, res in R["escenario"]:
        print(f"  {nombre:50s} -> {res}")
    print(f"Tramas aceptadas = {R['aceptadas']} de {len(R['escenario'])}")
    print(f"Alteracion de 1 bit detectada en {R['det_bit']}/1000 tramas")
    a, n = R["forja"]
    print(f"Falsificacion con etiqueta de 16 bits: {a} aciertos en {n} intentos ; esperados {R['forja_teo']:.2f} (2^-16)")
    print(f"Sobrecarga ilustrativa = {R['sobrecarga']} octetos (SPI {SPI_B} + IV {IV_B} + etiqueta {MAC_B}) en un bloque de {R['k_oct']} octetos")
    print(f"  datos utiles: {R['datos']} octetos ; eficiencia {R['efic_antes']:.4f} -> {R['efic_despues']:.4f}")
    print(f"Etiqueta de 128 bits: 2^128 = {R['combinaciones']:.3e} combinaciones")
    esperado = ["aceptada", "aceptada", "rechazada: repeticion", "aceptada", "aceptada", "rechazada: repeticion",
                "rechazada: autenticacion", "aceptada", "rechazada: fuera de ventana", "rechazada: autenticacion"]
    assert [r for _, r in R["escenario"]] == esperado
    assert R["det_bit"] == 1000 and abs(R["forja"][0] - R["forja_teo"]) < 4 * R["forja_teo"] ** 0.5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
