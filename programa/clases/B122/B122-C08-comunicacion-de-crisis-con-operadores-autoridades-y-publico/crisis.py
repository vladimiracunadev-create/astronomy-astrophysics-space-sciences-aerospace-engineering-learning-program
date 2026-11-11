#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C08: plazos de notificacion y plan de mensajes de una crisis SIMULADA.

CONTENIDO EDUCATIVO: no es asesoria legal ni regulatoria; no determina si una entidad esta sujeta a una norma ni sus plazos reales. Datos SINTETICOS.
Texto normativo consultado el 2026-11-11: Directiva (UE) 2022/2555 (NIS 2), EUR-Lex (version en ingles del Diario Oficial), articulo 23(4):
alerta temprana en 24 horas desde que se tiene conocimiento de un incidente significativo; notificacion del incidente en 72 horas; informe final
a mas tardar un mes despues de presentar la notificacion. Anexo I, sector 11 (Espacio): operadores de infraestructura terrestre que apoya
la prestacion de servicios espaciales (se leyo el texto; la fecha de publicacion y la transposicion nacional NO se consultaron).
Los plazos pueden cambiar o tener matices (p. ej. 'incidente significativo'): este laboratorio solo hace aritmetica de fechas.
Sistema de referencia: UTC. Unidades: horas y fechas. Tolerancias: aritmetica exacta; mes = mismo dia del mes siguiente (recortado al ultimo dia).
"""
from __future__ import annotations
import calendar, platform
from datetime import datetime, timedelta, timezone

CONOCIMIENTO = datetime(2026, 3, 5, 22, 30, tzinfo=timezone.utc)   # sintetico
NOTIFICACION_ENVIADA = datetime(2026, 3, 8, 20, 0, tzinfo=timezone.utc)  # sintetico


def mas_un_mes(dt):
    y, m = (dt.year + (dt.month == 12), 1 if dt.month == 12 else dt.month + 1)
    d = min(dt.day, calendar.monthrange(y, m)[1])
    return dt.replace(year=y, month=m, day=d)


# audiencia -> (que necesita saber, canal, aprobador, minutos de preparacion/aprobacion) (sintetico)
AUDIENCIAS = [
    ("Autoridad competente", "hechos, alcance, medidas", "formulario oficial", "direccion + juridico", 90),
    ("Operadores de servicios dependientes", "impacto y hora estimada de recuperacion", "canal operativo", "direccion de operaciones", 45),
    ("Personal interno", "que hacer y que no hacer", "intranet/aviso", "direccion de operaciones", 30),
    ("Publico y medios", "hechos verificados y proximo aviso", "comunicado", "direccion + comunicaciones", 120),
]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: fechas y audiencias inventadas. Plazos: art. 23(4) de la Directiva (UE) 2022/2555 (texto consultado 2026-11-11).")
    alerta = CONOCIMIENTO + timedelta(hours=24)
    notif = CONOCIMIENTO + timedelta(hours=72)
    final = mas_un_mes(NOTIFICACION_ENVIADA)
    print(f"Conocimiento del incidente : {CONOCIMIENTO:%Y-%m-%d %H:%M} UTC")
    print(f"Alerta temprana (24 h)     : {alerta:%Y-%m-%d %H:%M} UTC")
    print(f"Notificacion (72 h)        : {notif:%Y-%m-%d %H:%M} UTC ; enviada {NOTIFICACION_ENVIADA:%Y-%m-%d %H:%M} UTC -> a tiempo: {NOTIFICACION_ENVIADA <= notif}")
    print(f"Informe final (1 mes tras la notificacion): {final:%Y-%m-%d %H:%M} UTC")
    assert (alerta - CONOCIMIENTO) == timedelta(hours=24) and (notif - alerta) == timedelta(hours=48)
    assert mas_un_mes(datetime(2026, 1, 31, tzinfo=timezone.utc)).day == 28
    margen = (notif - NOTIFICACION_ENVIADA).total_seconds() / 3600
    print(f"Margen de la notificacion = {margen:.1f} h")
    print("Matriz de audiencias y tiempo de mensajes en secuencia (un solo equipo) o en paralelo:")
    t_seq = 0
    for nom, que, canal, apr, mins in AUDIENCIAS:
        t_seq += mins
        print(f"  {nom:36s} | {canal:18s} | {apr:28s} | {mins:3d} min | acumulado secuencial {t_seq:3d} min")
    t_par = max(a[4] for a in AUDIENCIAS)
    print(f"Tiempo total en secuencia = {t_seq} min ; en paralelo = {t_par} min ; la alerta temprana a la autoridad cabe en {24 * 60} min: {t_seq <= 24 * 60}")
    campos = {"hechos confirmados": 5, "hechos no confirmados": 3, "medidas en curso": 4, "proxima actualizacion": 1}
    conf = campos["hechos confirmados"] / (campos["hechos confirmados"] + campos["hechos no confirmados"])
    print(f"Fraccion de hechos confirmados en el mensaje sintetico = {conf:.3f}; regla del curso: rotular los no confirmados como tales")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
