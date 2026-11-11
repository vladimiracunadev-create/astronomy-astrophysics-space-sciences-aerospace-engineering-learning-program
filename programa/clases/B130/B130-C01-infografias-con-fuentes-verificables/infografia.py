#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C01: auditoria de procedencia de una infografia de datos planetarios.

Datos CONSULTADOS (2026-11-11, fichas NASA/NSSDC de la Tierra y de Marte): gravedad media, radio medio
volumetrico, densidad media. La ficha no informa incertidumbres: aqui se rotula "no informada".
SINTETICOS / ILUSTRATIVOS: las afirmaciones defectuosas de la lista de prueba (sin fuente, sin fecha, sin estado)
y la incertidumbre del ejemplo de cifras significativas (0.05 m/s2) NO son mediciones.
Definicion adoptada aqui (no consultada en Tufte): factor de mentira LF = efecto_en_el_grafico / efecto_en_los_datos,
con efecto = (B - A) / A; para circulos, el area (no el diametro) debe ser proporcional al dato.
Color representativo: orden cromatico (longitud de onda menor -> azul, mayor -> rojo), segun el explicador de NASA/ESA-Webb;
las longitudes de onda de la prueba son ILUSTRATIVAS.
Tolerancias: LF con area proporcional = 1 dentro de 1e-12; reglas de redondeo verificadas por casos.
"""
from __future__ import annotations
import math
import platform

REQUERIDOS = ("valor", "unidad", "fuente", "fecha", "estado", "incertidumbre")
ESTADOS = {"observado", "modelado", "ilustrativo", "consultado"}

AFIRMACIONES = [
    {"id": "g_tierra", "valor": 9.820, "unidad": "m/s2", "fuente": "NASA/NSSDC Earth Fact Sheet", "fecha": "2026-11-11",
     "estado": "consultado", "incertidumbre": "no informada"},
    {"id": "g_marte", "valor": 3.73, "unidad": "m/s2", "fuente": "NASA/NSSDC Mars Fact Sheet", "fecha": "2026-11-11",
     "estado": "consultado", "incertidumbre": "no informada"},
    {"id": "rho_tierra", "valor": 5513, "unidad": "kg/m3", "fuente": "NASA/NSSDC Earth Fact Sheet", "fecha": "2026-11-11",
     "estado": "consultado", "incertidumbre": "no informada"},
    {"id": "rho_marte", "valor": 3934, "unidad": "kg/m3", "fuente": "NASA/NSSDC Mars Fact Sheet", "fecha": "2026-11-11",
     "estado": "consultado", "incertidumbre": "no informada"},
    # Defectuosas SINTETICAS para probar la auditoria:
    {"id": "defecto_sin_fuente", "valor": 42, "unidad": "m", "fuente": "", "fecha": "2026-11-11",
     "estado": "ilustrativo", "incertidumbre": "no informada"},
    {"id": "defecto_sin_fecha", "valor": 7, "unidad": "K", "fuente": "fuente X", "fecha": "",
     "estado": "modelado", "incertidumbre": "no informada"},
    {"id": "defecto_estado_invalido", "valor": 1, "unidad": "kg", "fuente": "fuente Y", "fecha": "2026-11-11",
     "estado": "real", "incertidumbre": "no informada"},
]


def auditar(afirm):
    """Devuelve la lista de problemas de una afirmacion."""
    problemas = []
    for campo in REQUERIDOS:
        if campo not in afirm or afirm[campo] in ("", None):
            problemas.append("falta " + campo)
    if afirm.get("estado") not in ESTADOS:
        problemas.append("estado no admitido")
    return problemas


def factor_mentira(a, b, modo):
    """LF de un par de circulos (A, B). modo = 'diametro' o 'area' proporcional al dato."""
    efecto_datos = (b - a) / a
    if modo == "diametro":
        efecto_grafico = (b / a) ** 2 - 1.0  # area ~ diametro^2
    else:
        efecto_grafico = (b / a) - 1.0
    return efecto_grafico / efecto_datos


def formatear(valor, incert):
    """Redondea valor a la cifra de la incertidumbre (1 cifra significativa) y devuelve texto."""
    if incert <= 0:
        raise ValueError("incertidumbre positiva")
    exp = math.floor(math.log10(incert))
    inc_r = round(incert, -exp)
    dec = max(0, -exp)
    return f"{round(valor, -exp):.{dec}f} +/- {inc_r:.{dec}f}"


def color_representativo(longitudes_um):
    """Asigna colores por orden cromatico; devuelve {longitud: color}."""
    orden = sorted(longitudes_um)
    paleta = {1: ["rojo"], 2: ["azul", "rojo"], 3: ["azul", "verde", "rojo"], 4: ["azul", "cian", "naranja", "rojo"]}
    return dict(zip(orden, paleta[len(orden)]))


def credito_cc_by(titulo, autor, fuente_url, licencia, modificado):
    elementos = {"autor": autor, "enlace": fuente_url, "licencia": licencia}
    faltan = [k for k, v in elementos.items() if not v]
    texto = f"{titulo} - {autor} ({fuente_url}), {licencia}"
    texto += "; modificada" if modificado else "; sin cambios"
    return texto, faltan


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Auditoria de procedencia (datos NASA/NSSDC consultados 2026-11-11; defectos SINTETICOS):")
    buenas = 0
    for a in AFIRMACIONES:
        p = auditar(a)
        buenas += not p
        print(f"  {a['id']:<24} {'OK' if not p else 'FALLA: ' + ', '.join(p)}")
    print(f"Afirmaciones completas: {buenas}/{len(AFIRMACIONES)}")
    assert buenas == 4 and sum(1 for a in AFIRMACIONES if auditar(a)) == 3

    print("Factor de mentira (circulos Tierra frente a Marte):")
    for nombre, (vt, vm) in {"gravedad": (9.820, 3.73), "densidad": (5513, 3934), "radio": (6371.0, 3389.5)}.items():
        lf_d = factor_mentira(vm, vt, "diametro")
        lf_a = factor_mentira(vm, vt, "area")
        print(f"  {nombre:<9} razon {vt/vm:.4f}  LF diametro = {lf_d:.3f}  LF area = {lf_a:.3f}")
        assert abs(lf_a - 1.0) < 1e-12 and lf_d > 1.0

    print("Cifras significativas con incertidumbre ILUSTRATIVA 0.05 m/s2:")
    t = formatear(3.7342, 0.05)
    print("  3.7342 +/- 0.05  ->", t)
    assert t == "3.73 +/- 0.05"
    t2 = formatear(9.8201, 0.3)
    print("  9.8201 +/- 0.3   ->", t2)
    assert t2 == "9.8 +/- 0.3"

    filtros = [4.44, 1.15, 2.00]  # micrometros, ILUSTRATIVOS
    col = color_representativo(filtros)
    print("Color representativo (orden cromatico, longitudes ILUSTRATIVAS en um):", col)
    assert col[1.15] == "azul" and col[4.44] == "rojo"

    cred, faltan = credito_cc_by("Imagen de ejemplo", "ESO/Autor", "https://www.eso.org/public/", "CC BY 4.0", True)
    print("Credito CC BY:", cred, "| faltan:", faltan)
    assert not faltan
    _, faltan2 = credito_cc_by("Imagen", "", "", "CC BY 4.0", False)
    assert faltan2 == ["autor", "enlace"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
