#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C04: completitud y coherencia de un expediente regulatorio SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria legal ni regulatoria; los campos NO son el formulario oficial.
CONSULTADO (2026-11-11):
 - «ITU Radio Regulatory Framework for Space Services» (UIT, PDF creado 2018-01-10; hasta CMR-15), seccion 8.2, diligencia debida administrativa:
   informacion de la red (nombre del satelite, administracion notificante, referencia a la publicacion en seccion especial, rango de frecuencias,
   nombre del operador, caracteristicas orbitales); del fabricante (nombre, fecha de ejecucion del contrato, ventana de entrega, numero de satelites);
   y, antes de notificar, del proveedor de lanzamiento (nombre, fecha del contrato, ventana de lanzamiento prevista, vehiculo, nombre y ubicacion del sitio).
   Informacion incompleta a tiempo implica la cancelacion de la red.
 - Diapositivas «A milestone approach for NGSO systems, Resolution 35 (WRC-19)» (UIT, 30.o Seminario Mundial de Radiocomunicaciones, 24-28 octubre 2022):
   campos de la informacion de despliegue (sistema: nombre, administracion notificante, hito; lanzamiento: fecha, pais, instalacion, proveedor, vehiculo;
   estacion espacial: ID de plano orbital, nombre, apogeo, perigeo, inclinacion, argumento del perigeo; bandas: frecuencia minima y maxima).
NO CONSULTADO: el contenido del Apendice 4 del Reglamento (datos de la publicacion anticipada y de la coordinacion); por eso aqui solo hay una casilla
«apendice4_adjunto» como marcador, sin sus campos. Las reglas de coherencia (perigeo <= apogeo, fmin < fmax, etc.) son del autor, no del Reglamento.
El expediente SINTETICO «SINT-B» no corresponde a ninguna red real. Unidades: km, grados, MHz; fechas AAAA-MM-DD.
Tolerancia: la prueba de mutacion debe detectar el 100 % de las omisiones introducidas (0 omisiones sin detectar).
"""
from __future__ import annotations
import copy, platform

ESQUEMA = {
    "diligencia_red": ["nombre_satelite", "administracion_notificante", "ref_seccion_especial", "frecuencia_min_mhz", "frecuencia_max_mhz", "operador", "perigeo_km", "apogeo_km", "inclinacion_deg"],
    "fabricante": ["nombre", "fecha_contrato", "ventana_entrega_inicio", "ventana_entrega_fin", "n_satelites"],
    "lanzador": ["proveedor", "fecha_contrato", "ventana_lanzamiento_inicio", "ventana_lanzamiento_fin", "vehiculo", "sitio_nombre", "sitio_ubicacion"],
    "despliegue_res35": ["hito", "fecha_lanzamiento", "pais_lanzamiento", "instalacion", "plano_orbital", "n_desplegados"],
    "marcadores": ["apendice4_adjunto"],
}

EXPEDIENTE = {
    "diligencia_red": {"nombre_satelite": "SINT-B-1", "administracion_notificante": "ADM-X", "ref_seccion_especial": "CR/C/9999 (sintetica)", "frecuencia_min_mhz": 10700.0, "frecuencia_max_mhz": 12700.0,
                       "operador": "Operadora Sintetica S.A.", "perigeo_km": 550.0, "apogeo_km": 560.0, "inclinacion_deg": 53.0},
    "fabricante": {"nombre": "Fabrica Sintetica", "fecha_contrato": "2028-02-01", "ventana_entrega_inicio": "2030-06-01", "ventana_entrega_fin": "2030-12-01", "n_satelites": 120},
    "lanzador": {"proveedor": "Lanzadora Sintetica", "fecha_contrato": "2028-09-15", "ventana_lanzamiento_inicio": "2031-01-10", "ventana_lanzamiento_fin": "2031-03-10",
                 "vehiculo": "VL-1 (sintetico)", "sitio_nombre": "Base Sintetica", "sitio_ubicacion": "0.0N 0.0E"},
    "despliegue_res35": {"hito": "M1", "fecha_lanzamiento": "2031-02-01", "pais_lanzamiento": "PAIS-S", "instalacion": "Base Sintetica", "plano_orbital": "P1", "n_desplegados": 12},
    "marcadores": {"apendice4_adjunto": True},
}


def faltantes(exp):
    """Via A: recorre el esquema y devuelve (grupo, campo) ausentes o vacios."""
    out = []
    for g, campos in ESQUEMA.items():
        for c in campos:
            v = exp.get(g, {}).get(c)
            if v is None or v == "" or v is False:
                out.append((g, c))
    return out


def faltantes_conjuntos(exp):
    """Via B: diferencia de conjuntos entre los campos exigidos y los presentes no vacios."""
    exigidos = {(g, c) for g, cs in ESQUEMA.items() for c in cs}
    presentes = {(g, c) for g, d in exp.items() for c, v in d.items() if v not in (None, "", False)}
    return sorted(exigidos - presentes)


def coherencia(exp):
    e = []
    r, f, l, d = exp["diligencia_red"], exp["fabricante"], exp["lanzador"], exp["despliegue_res35"]
    try:
        if r["perigeo_km"] > r["apogeo_km"]:
            e.append("perigeo mayor que apogeo")
        if r["frecuencia_min_mhz"] >= r["frecuencia_max_mhz"]:
            e.append("frecuencia minima >= maxima")
        if not 0 <= r["inclinacion_deg"] <= 180:
            e.append("inclinacion fuera de 0-180")
        if f["ventana_entrega_inicio"] > f["ventana_entrega_fin"]:
            e.append("ventana de entrega invertida")
        if l["ventana_lanzamiento_inicio"] < f["ventana_entrega_inicio"]:
            e.append("lanzamiento previsto antes de la entrega")
        if f["fecha_contrato"] > f["ventana_entrega_inicio"] or l["fecha_contrato"] > l["ventana_lanzamiento_inicio"]:
            e.append("contrato posterior a su ventana")
        if d["n_desplegados"] > f["n_satelites"]:
            e.append("desplegados mas que los fabricados")
        if not (l["ventana_lanzamiento_inicio"] <= d["fecha_lanzamiento"] <= l["ventana_lanzamiento_fin"]):
            e.append("fecha de lanzamiento fuera de la ventana")
    except (KeyError, TypeError):
        e.append("coherencia no evaluable por campos ausentes")
    return e


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("EXPEDIENTE SINTETICO; campos de diligencia debida (UIT 2018-01-10) y de Res. 35 (WRS-22), consulta 2026-11-11; no es el formulario oficial ni asesoria.")
    total = sum(len(c) for c in ESQUEMA.values())
    print(f"Campos exigidos en el esquema: {total} (grupos: " + ", ".join(f"{g}={len(c)}" for g, c in ESQUEMA.items()) + ")")
    base = faltantes(EXPEDIENTE)
    print(f"Expediente base: faltantes = {len(base)} ; incoherencias = {coherencia(EXPEDIENTE)}")
    # prueba de mutacion: quitar cada campo debe detectarse exactamente una vez
    sin_detectar = 0
    for g, cs in ESQUEMA.items():
        for c in cs:
            m = copy.deepcopy(EXPEDIENTE)
            m[g][c] = None
            a, b = faltantes(m), faltantes_conjuntos(m)
            if a != [(g, c)] or b != [(g, c)]:
                sin_detectar += 1
    print(f"Prueba de mutacion: {total} omisiones introducidas, {sin_detectar} sin detectar por alguna de las dos vias")
    casos = {
        "falta contrato del lanzador": ("lanzador", "fecha_contrato", None),
        "falta nombre del operador": ("diligencia_red", "operador", ""),
        "perigeo > apogeo": ("diligencia_red", "perigeo_km", 600.0),
        "lanzamiento antes de la entrega": ("lanzador", "ventana_lanzamiento_inicio", "2030-01-01"),
        "mas desplegados que fabricados": ("despliegue_res35", "n_desplegados", 130),
    }
    print("Caso                               faltantes  incoherencias")
    for nombre, (g, c, v) in casos.items():
        m = copy.deepcopy(EXPEDIENTE)
        m[g][c] = v
        fa = faltantes(m)
        co = coherencia(m)
        print(f"{nombre:34s} {len(fa):6d}  {'; '.join(co) if co else '-'}" + (f"  (falta {fa[0][0]}.{fa[0][1]})" if fa else ""))
    comp = 100 * (total - len(base)) / total
    print(f"Completitud del expediente base: {comp:.1f} %")
    assert base == [] and coherencia(EXPEDIENTE) == [] and sin_detectar == 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
