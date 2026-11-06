#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C24: una bitácora de decisiones encadenada por hashes.

Datos: SINTÉTICOS. Un análisis ficticio de un tránsito con una hipótesis
preregistrada, tres decisiones y una desviación; los textos están escritos en
el script. Las fechas son ficticias y FIJAS para que el resultado sea
reproducible (no se usa el reloj).
Modelo: cada entrada lleva (índice, fecha, tipo, texto, huella_previa) y su
huella = SHA-256 de esos campos; la huella de cada entrada incluye la de la
anterior, de modo que cambiar, borrar o reordenar una entrada rompe la cadena
desde ese punto. La primera entrada fija la huella del protocolo.
Supuestos: una sola persona escribe; la cadena detecta cambios, no impide que
alguien reescriba TODA la cadena y su huella final.
Validez: demostración; no sustituye a un sistema de control de versiones.
Tolerancia: la verificación debe señalar el índice exacto donde se rompió.
"""
from __future__ import annotations
import hashlib, json, platform, sys


def huella(entrada: dict) -> str:
    base = {k: entrada[k] for k in ("indice", "fecha", "tipo", "texto", "huella_previa")}
    return hashlib.sha256(json.dumps(base, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


class Bitacora:
    def __init__(self):
        self.entradas = []

    def anotar(self, fecha, tipo, texto):
        previa = self.entradas[-1]["huella"] if self.entradas else "0" * 64
        e = {"indice": len(self.entradas), "fecha": fecha, "tipo": tipo, "texto": texto, "huella_previa": previa}
        e["huella"] = huella(e)
        self.entradas.append(e)


def verificar(entradas):
    """Devuelve None si la cadena es íntegra, o el índice del primer fallo."""
    previa = "0" * 64
    for i, e in enumerate(entradas):
        if e["indice"] != i or e["huella_previa"] != previa or huella(e) != e["huella"]:
            return i
        previa = e["huella"]
    return None


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    b = Bitacora()
    proto_hash = hashlib.sha256(b"protocolo v1 (sintetico)").hexdigest()
    b.anotar("2026-01-01", "protocolo", f"hipótesis: la profundidad del tránsito es mayor que cero; prueba z; alfa 0,05; huella del protocolo {proto_hash[:16]}")
    b.anotar("2026-01-02", "decision", "se usa el modelo trapezoidal con ingreso fijo de 1000 s (justificación: geometría esperada)")
    b.anotar("2026-01-03", "desviacion", "se excluyen 3 muestras con flujo atípico (más de 5 MAD); NO estaba en el protocolo; se declara exploratorio")
    b.anotar("2026-01-04", "decision", "se reporta el resultado con y sin la exclusión")
    print(f"entradas: {len(b.entradas)}; tipos: {[e['tipo'] for e in b.entradas]}")
    prueba(verificar(b.entradas) is None, "cadena íntegra")
    print("cadena íntegra: verificación aprobada")

    # 1) modificar el texto de la entrada 1
    copia = json.loads(json.dumps(b.entradas))
    copia[1]["texto"] = "se usa el modelo sin ingreso"
    print(f"texto de la entrada 1 modificado: se rompe en el índice {verificar(copia)}")
    prueba(verificar(copia) == 1, "rotura en 1")
    # 2) recalcular la huella de la entrada alterada no basta: la siguiente apunta a la antigua
    copia[1]["huella"] = huella(copia[1])
    print(f"recalcular solo la huella de la entrada 1: se rompe en el índice {verificar(copia)} (la entrada 2 apunta a la huella anterior)")
    prueba(verificar(copia) == 2, "rotura en 2")
    # 3) borrar una entrada
    copia = json.loads(json.dumps(b.entradas))
    del copia[2]
    print(f"entrada 2 borrada: se rompe en el índice {verificar(copia)}")
    prueba(verificar(copia) == 2, "borrado detectado")
    # 4) reordenar
    copia = json.loads(json.dumps(b.entradas))
    copia[1], copia[2] = copia[2], copia[1]
    print(f"entradas 1 y 2 intercambiadas: se rompe en el índice {verificar(copia)}")
    prueba(verificar(copia) == 1, "reordenado detectado")
    # 5) añadir al final es válido
    b.anotar("2026-01-05", "decision", "se publica el informe con la lista de desviaciones")
    prueba(verificar(b.entradas) is None, "añadir mantiene la cadena")
    print(f"añadir una entrada válida: cadena íntegra con {len(b.entradas)} entradas; huella final = {b.entradas[-1]['huella'][:16]}...")
    # 6) límite: reescribir toda la cadena produce otra cadena válida
    rehecha = Bitacora()
    for e in b.entradas:
        rehecha.anotar(e["fecha"], e["tipo"], e["texto"].replace("trapezoidal", "gaussiano"))
    prueba(verificar(rehecha.entradas) is None and rehecha.entradas[-1]["huella"] != b.entradas[-1]["huella"],
           "una cadena reescrita entera es válida pero tiene otra huella final")
    print("límite: una cadena reescrita entera también verifica, pero su huella final es distinta; por eso la huella final debe publicarse o registrarse aparte")
    n_desv = sum(1 for e in b.entradas if e["tipo"] == "desviacion")
    print(f"desviaciones del protocolo registradas: {n_desv}")
    prueba(n_desv == 1, "una desviación registrada")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
