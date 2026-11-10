#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C18: matriz requisito-verificacion y cadena de resumenes SHA-256 de evidencias (SINTETICO).

Cobertura = requisitos con al menos una verificacion cerrada / total. Cada registro de evidencia incluye el resumen del anterior;
alterar un registro rompe la cadena desde ese punto. Se usa hashlib.sha256 (FIPS 180-4; NO consultada la norma, funcion de la biblioteca estandar).
Comprobacion: la cadena se recalcula por una segunda implementacion independiente. Tolerancia: igualdad exacta.
"""
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: 8 requisitos y 7 registros de evidencia de una unidad de ejemplo")
reqs = {f"R{i}": t for i, t in enumerate([
    "Masa menor de 4 kg", "CG dentro de limites", "Vibracion aleatoria sin danio", "Termovacio sin falla funcional",
    "EMC con margen de 6 dB", "Despliegue de antena", "Tres inhibidores independientes", "Telecomando de extremo a extremo"], start=1)}
matriz = {  # requisito: [(metodo, id de evidencia, estado)]
    "R1": [("inspeccion", "E1", "cerrada")], "R2": [("analisis", "E2", "cerrada")], "R3": [("prueba", "E3", "cerrada")],
    "R4": [("prueba", "E4", "abierta")], "R5": [("prueba", "E5", "cerrada")], "R6": [("demostracion", "E6", "cerrada")],
    "R7": [], "R8": [("prueba", "E7", "cerrada")],
}
cerrados = [r for r, v in matriz.items() if any(e[2] == "cerrada" for e in v)]
print("req  metodo        evidencia  estado")
for r in reqs:
    v = matriz[r]
    print(f"{r:3s}  {', '.join(e[0] for e in v) or '-':12s}  {', '.join(e[1] for e in v) or '-':9s}  {', '.join(e[2] for e in v) or 'SIN VERIFICACION'}")
cob = len(cerrados) / len(reqs)
print(f"Cobertura cerrada = {len(cerrados)} de {len(reqs)} = {cob * 100:.1f} % ; sin verificacion: {[r for r, v in matriz.items() if not v]} ; abiertas: {[r for r, v in matriz.items() if v and not any(e[2] == 'cerrada' for e in v)]}")
comprobar(len(cerrados) == 6, "deben estar cerrados 6 de 8")
ev_ids = {e[1] for v in matriz.values() for e in v}
huerfanas = {"E7", "E8"} - ev_ids
print("Evidencias sin requisito (huerfanas):", sorted(huerfanas))

registros = [{"id": f"E{i}", "fecha": f"2026-10-{10 + i:02d}", "contenido": c} for i, c in enumerate(
    ["Informe de inspeccion de masa", "Calculo de CG", "Informe de vibracion", "Registro de termovacio", "Informe de EMC", "Video de despliegue", "Registro E2E"], start=1)]

def cadena(registros):
    prev, salida = "0" * 64, []
    for r in registros:
        cuerpo = json.dumps(r, sort_keys=True, ensure_ascii=True)
        h = hashlib.sha256((prev + cuerpo).encode()).hexdigest()
        salida.append(h)
        prev = h
    return salida

def cadena_alt(registros):
    h = hashlib.sha256()
    prev = b"0" * 64
    out = []
    for r in registros:
        h = hashlib.sha256(prev + json.dumps(r, sort_keys=True, ensure_ascii=True).encode())
        prev = h.hexdigest().encode()
        out.append(h.hexdigest())
    return out

c1 = cadena(registros)
print("Cadena de resumenes (8 primeros hex):", " ".join(x[:8] for x in c1))
comprobar(c1 == cadena_alt(registros), "las dos implementaciones deben coincidir")
alterado = [dict(r) for r in registros]
alterado[2]["contenido"] = "Informe de vibracion (editado)"
c2 = cadena(alterado)
primero = next(i for i, (a, b) in enumerate(zip(c1, c2)) if a != b)
print(f"Tras editar el registro E3 la cadena cambia desde la posicion {primero + 1}: {sum(a != b for a, b in zip(c1, c2))} de {len(c1)} resumenes distintos")
comprobar(primero == 2 and c1[:2] == c2[:2], "la edicion debe romper la cadena desde E3")
print("Longitud del resumen =", len(c1[0]) * 4, "bits")
fin()
