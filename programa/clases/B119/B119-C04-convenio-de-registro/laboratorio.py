#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C04: registro de objetos espaciales: campos del art. IV y periodo calculado desde apogeo y perigeo. Registros SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, pagina de UNOOSA del Convenio de Registro; WebFetch): art. II (registro del Estado de lanzamiento y aviso al Secretario General),
art. III (registro central abierto), art. IV (nombre del Estado de lanzamiento, designador, fecha y lugar de lanzamiento, parametros orbitales basicos:
periodo nodal, inclinacion, apogeo, perigeo; funcion general), art. VI (ayuda para identificar objetos). Adoptado el 12-11-1974 (res. 3235 (XXIX)); abierto a firma el 14-01-1975.
Constantes (no consultadas en esta sesion; valores estandar): radio ecuatorial R = 6378.137 km, GM = 398600.4418 km^3/s^2.
SINTETICO: los cinco registros. Modelo: periodo kepleriano T = 2 pi sqrt(a^3/GM), a = R + (hp + ha)/2 con alturas sobre el elipsoide;
el periodo nodal real difiere por J2 (no modelado). Tolerancia: T de la orbita circular de 400 km == 92.57 min a 0.05 min.
"""
import json, math, platform

R, GM = 6378.137, 398600.4418
CAMPOS = ["estado", "designador", "fecha_lanzamiento", "lugar", "periodo_min", "inclinacion_deg", "apogeo_km", "perigeo_km", "funcion"]

def periodo_min(ha, hp):
    a = R + (ha + hp) / 2.0
    return 2 * math.pi * math.sqrt(a ** 3 / GM) / 60.0

REG = [
    dict(estado="Pais-A", designador="2026-001A", fecha_lanzamiento="2026-01-10", lugar="Sitio-1", inclinacion_deg=97.4, apogeo_km=540.0, perigeo_km=520.0, funcion="observacion de la Tierra"),
    dict(estado="Pais-A", designador="2026-001B", fecha_lanzamiento="2026-01-10", lugar="Sitio-1", inclinacion_deg=97.4, apogeo_km=545.0, perigeo_km=525.0, funcion="observacion de la Tierra"),
    dict(estado="Pais-B", designador="2026-014A", fecha_lanzamiento="2026-03-02", lugar="Sitio-2", inclinacion_deg=53.0, apogeo_km=560.0, perigeo_km=555.0, funcion="comunicaciones"),
    dict(estado="Pais-B", designador="", fecha_lanzamiento="2026-03-02", lugar="Sitio-2", inclinacion_deg=53.0, apogeo_km=560.0, perigeo_km=555.0, funcion="comunicaciones"),
    dict(estado="Pais-C", designador="2026-030A", fecha_lanzamiento="2026-06-21", lugar="Sitio-3", inclinacion_deg=28.5, apogeo_km=35790.0, perigeo_km=250.0, funcion=""),
]
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Registros SINTETICOS; campos del art. IV segun la pagina de UNOOSA consultada el 2026-11-11.")
completos = 0
for r in REG:
    r["periodo_min"] = periodo_min(r["apogeo_km"], r["perigeo_km"])
    faltan = [c for c in CAMPOS if r.get(c) in (None, "")]
    ok = not faltan
    completos += ok
    print(f"{r['designador'] or '(vacio)':10s} T = {r['periodo_min']:8.2f} min  {'completo' if ok else 'FALTA ' + ','.join(faltan)}")
duplicados = len({r["designador"] for r in REG if r["designador"]}) != len([r for r in REG if r["designador"]])
frac = completos / len(REG)
print(f"Completitud: {completos} de {len(REG)} = {frac:.2f}; designadores repetidos: {duplicados}")
t400 = periodo_min(400.0, 400.0)
print(f"Control: orbita circular a 400 km -> T = {t400:.2f} min (esperado 92.57)")
assert abs(t400 - 92.57) < 0.05
assert completos == 3 and not duplicados
# periodo de la orbita de transferencia geoestacionaria (perigeo 250, apogeo 35790): ~10.5 h
tgto = periodo_min(35790.0, 250.0)
print(f"Control: GTO -> T = {tgto:.1f} min = {tgto / 60:.2f} h")
assert 10.3 < tgto / 60 < 10.7
print("CLAVES " + json.dumps({"t540": "%.2f" % REG[0]["periodo_min"], "t400": "%.2f" % t400, "frac": "%.2f" % frac, "gto": "%.2f" % (tgto / 60), "tleo2": "%.2f" % REG[2]["periodo_min"]}))
print("Pruebas superadas.")
