#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C30: una cadena automática con orden de dependencias, idempotencia y control de calidad.

Datos: SINTÉTICOS. Cada «lote» es un arreglo de 1000 flujos relativos
(media 1.0, desviación 0.01, semilla = 20261105 + número de lote); el lote 3
se corrompe a propósito (200 valores NaN) para probar el control de calidad.
Modelo: etapas con dependencias (ingestar -> validar -> procesar -> publicar),
ordenadas con graphlib.TopologicalSorter; cada etapa guarda su resultado en un
almacén con clave = SHA-256 de (nombre de etapa + huella de la entrada); si la
clave existe, la etapa se SALTA (idempotencia). El control de calidad detiene
la cadena de ese lote si hay más de 1 % de NaN o si la media sale de [0.99, 1.01].
Un fallo transitorio inyectado (2 fallos y luego éxito) se reintenta hasta 3 veces.
Supuestos: ejecución en un solo proceso; sin planificador ni reloj.
Validez: demostración del patrón; una cadena operativa añade registros, alertas y
recuperación que aquí no existen.
Tolerancia: conteos exactos de etapas ejecutadas y saltadas; la cadena de dependencias
debe respetar el orden; un ciclo debe detectarse.
"""
from __future__ import annotations
import hashlib, platform, sys
from graphlib import CycleError, TopologicalSorter
import numpy as np

DEPENDENCIAS = {"validar": {"ingestar"}, "procesar": {"validar"}, "publicar": {"procesar"}}


def huella(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


class Cadena:
    def __init__(self):
        self.almacen = {}
        self.registro = []
        self.fallos_pendientes = {}      # (lote, etapa) -> número de fallos transitorios por inyectar

    def ejecutar_lote(self, n):
        orden = list(TopologicalSorter(DEPENDENCIAS).static_order())
        estado = {"lote": n}
        for etapa in orden:
            clave = huella(f"{etapa}|{n}|{estado.get('huella', '')}".encode())
            if clave in self.almacen:
                self.registro.append((n, etapa, "saltada"))
                estado.update(self.almacen[clave])
                continue
            for intento in range(1, 4):
                try:
                    if self.fallos_pendientes.get((n, etapa), 0) > 0:
                        self.fallos_pendientes[(n, etapa)] -= 1
                        raise ConnectionError("fallo transitorio inyectado")
                    resultado = getattr(self, "_" + etapa)(n, estado)
                    break
                except ConnectionError:
                    self.registro.append((n, etapa, f"reintento {intento}"))
                    if intento == 3:
                        self.registro.append((n, etapa, "falló definitivamente"))
                        return False
            if resultado is None:                      # el control de calidad detuvo el lote
                self.registro.append((n, etapa, "detenida por calidad"))
                return False
            self.almacen[clave] = resultado
            estado.update(resultado)
            self.registro.append((n, etapa, "ejecutada"))
        return True

    # --- etapas ---
    def _ingestar(self, n, estado):
        rng = np.random.default_rng(20261105 + n)
        x = rng.normal(1.0, 0.01, 1000)
        if n == 3:
            x[:200] = np.nan
        estado["datos"] = x
        return {"datos": x, "huella": huella(x.tobytes())}

    def _validar(self, n, estado):
        x = estado["datos"]
        frac_nan = float(np.isnan(x).mean())
        media = float(np.nanmean(x))
        if frac_nan > 0.01 or not (0.99 <= media <= 1.01):
            return None
        return {"media_validada": media, "huella": huella(x.tobytes() + b"validado")}

    def _procesar(self, n, estado):
        x = estado["datos"]
        return {"producto": float(np.mean(x)), "huella": huella(x.tobytes() + b"procesado")}

    def _publicar(self, n, estado):
        return {"publicado": f"lote-{n}:{estado['producto']:.6f}", "huella": huella(f"pub{n}".encode())}


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def contar(reg, lote=None):
    c = {}
    for n, e, s in reg:
        if lote is None or n == lote:
            c[s] = c.get(s, 0) + 1
    return c


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    orden = list(TopologicalSorter(DEPENDENCIAS).static_order())
    print(f"orden topológico de las etapas: {orden}")
    prueba(orden == ["ingestar", "validar", "procesar", "publicar"], "orden")
    try:
        list(TopologicalSorter({"a": {"b"}, "b": {"a"}}).static_order())
        prueba(False, "debía detectar el ciclo")
    except CycleError:
        print("un ciclo de dependencias se detecta (CycleError)")

    c = Cadena()
    ok = [c.ejecutar_lote(n) for n in range(5)]
    print(f"primera pasada, lotes 0-4: aprobados = {ok}")
    prueba(ok == [True, True, True, False, True], "solo el lote 3 es detenido")
    print(f"  resumen lote 3: {contar(c.registro, 3)}")
    prueba(contar(c.registro, 3) == {"ejecutada": 1, "detenida por calidad": 1}, "lote 3: ingesta ejecutada y validación detenida")
    print(f"  etapas ejecutadas en total: {contar(c.registro)['ejecutada']} (4 lotes completos x 4 + 1 de ingesta del lote 3 = 17)")
    prueba(contar(c.registro)["ejecutada"] == 17, "17 etapas ejecutadas")

    n0 = len(c.registro)
    ok2 = [c.ejecutar_lote(n) for n in range(5)]
    nuevo = c.registro[n0:]
    cuentas = contar(nuevo)
    print(f"segunda pasada: aprobados = {ok2}; {cuentas}")
    prueba(ok2 == ok, "mismo resultado")
    prueba(cuentas.get("ejecutada", 0) == 0 and cuentas["saltada"] == 17 and cuentas["detenida por calidad"] == 1,
           "segunda pasada: nada se recalcula (17 etapas saltadas) y el lote 3 vuelve a ser detenido por calidad")

    # fallo transitorio con reintentos
    c2 = Cadena()
    c2.fallos_pendientes[(0, "procesar")] = 2
    prueba(c2.ejecutar_lote(0), "con 2 fallos transitorios y 3 intentos debe terminar")
    print(f"fallo transitorio (2 fallos): {contar(c2.registro, 0)}")
    prueba(contar(c2.registro, 0).get("reintento 1", 0) == 1 and contar(c2.registro, 0).get("reintento 2", 0) == 1, "dos reintentos")
    c3 = Cadena()
    c3.fallos_pendientes[(0, "procesar")] = 5
    prueba(not c3.ejecutar_lote(0), "con 5 fallos y 3 intentos debe fallar")
    print(f"fallo persistente (5 fallos): {contar(c3.registro, 0)}")
    prueba("falló definitivamente" in contar(c3.registro, 0), "registro del fallo definitivo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
