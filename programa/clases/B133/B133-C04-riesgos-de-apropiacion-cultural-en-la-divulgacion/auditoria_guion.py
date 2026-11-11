#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B133-C04: auditoria de riesgos de apropiacion en guiones de divulgacion SINTETICOS.

Todo es SINTETICO: la comunidad (Alfa-Tul), los tres guiones y los permisos estan inventados. Ninguno describe a un pueblo real.
El script aplica reglas de texto (palabras y patrones) que reflejan riesgos que senalan las fuentes consultadas: generalizar
a «los pueblos indigenas», tratar los saberes solo como historia antigua o con palabras jerarquicas (Neilson et al. 2019),
afirmar sin atribuir, contenido con protocolo sin permiso (Lee et al. 2020; art. 31 de la Declaracion de la ONU) y uso
comercial sin beneficio para la comunidad. LAS REGLAS NO PUEDEN DECIDIR SI HAY APROPIACION: eso lo decide la comunidad.
Un guion que pasa las reglas puede ser inaceptable (guion Z lo demuestra con un permiso ausente que ningun texto revela).
Segunda via: la regla de generalizacion se implementa con expresiones regulares y con un recorrido de palabras, y se comparan.
Tolerancias: hallazgos esperados fijados de antemano (defectos plantados); acuerdo entre las dos vias = 100 %.
"""
from __future__ import annotations
import platform, re

GUIONES = {
    "X (cuidado)": {
        "autorizacion_comunidad": True,
        "texto": (
            "En colaboracion con la comunidad ficticia de Alfa-Tul, presentamos lo que su Consejo de Mayores autorizo mostrar. "
            "Segun el Consejo de Mayores de Alfa-Tul, la salida de una estrella indica el inicio de la siembra. "
            "La comunidad Alfa-Tul sigue usando este calendario hoy. "
            "El relato completo se cuenta solo en la comunidad y aqui no se reproduce. "
            "La entrada a esta funcion es gratuita y parte de la recaudacion se entrega a la escuela de Alfa-Tul, segun el acuerdo firmado. "
            "Agradecemos a la comunidad ficticia de Alfa-Tul por su colaboracion."
        ),
    },
    "Y (defectuoso)": {
        "autorizacion_comunidad": False,
        "texto": (
            "Los indigenas creian que las estrellas eran dioses. "
            "Los pueblos originarios antiguos pensaban que el cielo era un animal. "
            "Este mito primitivo es una leyenda pintoresca. "
            "La ceremonia sagrada del solsticio se cuenta aqui completa. "
            "Venta de entradas y de nuestra marca de camisetas con el diseño estelar."
        ),
    },
    "Z (pasa las reglas)": {
        "autorizacion_comunidad": False,
        "texto": (
            "Segun el Consejo de Mayores de Alfa-Tul, la salida de una estrella indica el inicio de la siembra. "
            "La comunidad Alfa-Tul sigue usando este calendario hoy. "
            "Recogimos este relato en una visita y lo mostramos en nuestra sala con la comunidad ficticia de Alfa-Tul como referencia. "
            "Agradecemos a la comunidad ficticia de Alfa-Tul por su colaboracion."
        ),
    },
}

ESPERADO = {
    "X (cuidado)": set(),
    "Y (defectuoso)": {"R1-generalizacion", "R2-solo-pasado", "R3-sin-atribucion", "R4-protocolo-sin-permiso",
                       "R5-comercial-sin-beneficio", "R6-jerarquia", "R7-sin-credito"},
    "Z (pasa las reglas)": set(),
}

GENERICOS = ("los indigenas", "los pueblos originarios", "los nativos", "los aborigenes")
JERARQUIA = ("mito", "leyenda", "primitivo", "pintoresco", "supersticion")
PASADO = ("creian", "pensaban", "antiguos", "antiguo", "ancestrales")
PROTOCOLO = ("sagrada", "sagrado", "ceremonia", "secreto")
COMERCIAL = ("venta", "marca", "entradas", "camisetas")
ATRIBUCION = ("segun", "en colaboracion con", "agradecemos", "consejo de mayores")
BENEFICIO = ("beneficio", "recaudacion", "acuerdo firmado", "gratuita")
PERMISO = ("autorizo", "autorizado", "con permiso", "no se reproduce")


def oraciones(t: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]


def contiene(s: str, palabras) -> bool:
    low = s.lower()
    return any(p in low for p in palabras)


def r1_regex(t: str) -> bool:
    return re.search(r"\b(" + "|".join(GENERICOS) + r")\b", t.lower()) is not None


def r1_tokens(t: str) -> bool:
    toks = re.findall(r"[a-zñ]+", t.lower())
    gen = [g.split() for g in GENERICOS]
    for i in range(len(toks)):
        for g in gen:
            if toks[i:i + len(g)] == g:
                return True
    return False


def auditar(g: dict) -> tuple[set[str], dict]:
    t = g["texto"]
    ors = oraciones(t)
    h: set[str] = set()
    if r1_regex(t):
        h.add("R1-generalizacion")
    if contiene(t, PASADO) and not contiene(t, ("hoy", "sigue usando", "actual")):
        h.add("R2-solo-pasado")
    con_atr = sum(contiene(s, ATRIBUCION) for s in ors)
    frac = con_atr / len(ors)
    if frac < 0.5:
        h.add("R3-sin-atribucion")
    if contiene(t, PROTOCOLO) and not contiene(t, PERMISO):
        h.add("R4-protocolo-sin-permiso")
    if contiene(t, COMERCIAL) and not contiene(t, BENEFICIO):
        h.add("R5-comercial-sin-beneficio")
    if contiene(t, JERARQUIA):
        h.add("R6-jerarquia")
    if not contiene(t, ("agradecemos", "en colaboracion con")):
        h.add("R7-sin-credito")
    return h, {"oraciones": len(ors), "con_atribucion": con_atr, "fraccion": frac}


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Guiones y comunidad SINTETICOS (Alfa-Tul es ficticia). Las reglas no deciden si hay apropiacion.")
    acuerdos = 0
    for nombre, g in GUIONES.items():
        h, m = auditar(g)
        a, b = r1_regex(g["texto"]), r1_tokens(g["texto"])
        acuerdos += (a == b)
        print(f"\nGuion {nombre}: oraciones = {m['oraciones']}, con atribucion = {m['con_atribucion']} ({m['fraccion']:.2f})")
        print(f"   hallazgos de texto: {len(h)}")
        for x in sorted(h):
            print(f"   {x}")
        print(f"   autorizacion de la comunidad (dato externo al texto): {g['autorizacion_comunidad']}")
        veredicto = "puede difundirse" if (not h and g["autorizacion_comunidad"]) else "NO puede difundirse"
        print(f"   -> {veredicto}")
        assert h == ESPERADO[nombre], (nombre, h ^ ESPERADO[nombre])
    print(f"\nAcuerdo entre regex y recorrido de palabras en R1: {acuerdos}/{len(GUIONES)}")
    assert acuerdos == len(GUIONES)
    print("Los guiones X, Y y Z reproducen los hallazgos plantados; la comprobacion es circular por diseño.")
    print("El guion Z no tiene hallazgos de texto y aun asi no puede difundirse: falta la autorizacion de la comunidad.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
