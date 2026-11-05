#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C20: verificador de requisitos de una campaña de observación nocturna.

Trata la campaña como un problema de ingeniería: requisitos con criterio de comprobación, componentes y decisión «go / no-go».
Datos: noches y posiciones lunares de NASA SVS 5415 (JPL DE421, consultada 2026-11-05) y Sol de baja precisión, reutilizados de
B08-C12 (`ventana_oscura.py`, que ya se prueba contra astropy); altura de planetas del 5-6 nov 2025 de la referencia astropy de
B08-C10 (copiada). Salidas CALCULADAS/SIMULADAS. Dominio: las dos noches de noviembre de 2025 para el lugar redondeado lat -30,0
lon -70,7. Criterios de decisión: umbrales de EJEMPLO elegidos por esta clase, no normas.
Prueba independiente: (1) la noche de Luna nueva debe superar a la de Luna llena en horas sin Luna (se contrasta con la fase
publicada); (2) cada requisito del plan debe tener criterio y método de comprobación; (3) el requisito de seguridad solar debe existir.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))


def _cargar(ruta: Path, nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


VO = _cargar(RAIZ / "B08-C12-limitacion-por-contaminacion-luminica" / "ventana_oscura.py", "ventana_oscura_c12")

# Alturas de planetas al crepúsculo astronómico vespertino/matutino (astropy, copiadas de C10) para la noche del 5-6 de noviembre
PLANETAS_5NOV = {"Saturno": (61.6, -8.3), "Jupiter": (-46.4, 35.9), "Mercurio": (2.8, -26.3), "Marte": (-2.6, -26.4), "Venus": (-33.0, -10.9)}

REQUISITOS = [
    ("R1", "Seguridad solar: nadie mira el Sol sin protección certificada verificada", "0 observaciones solares sin plan C16", "revisión del plan por una segunda persona", "NASA, AAS (C16)"),
    ("R2", "Ventana oscura: al menos 4 h de noche astronómica sin Luna", "horas sin Luna >= 4 h", "cálculo con ventana_oscura.py y tabla NASA", "NASA SVS 5415 (C12)"),
    ("R3", "Objeto por encima de 25 grados durante la sesión", "altura >= 25 grados entre inicio y fin", "cálculo de altura (C04) o aplicación", "C04"),
    ("R4", "Tiempos y lugar registrados en UT con procedencia", "100 % de filas válidas", "validación de bitácora (C17)", "C17"),
    ("R5", "Plan de terreno, abrigo y comunicación", "lista completa y un responsable de seguridad", "revisión previa en el sitio de día", "C01, C12"),
    ("R6", "Alternativas por recurso (sin equipo, binoculares, telescopio, datos abiertos)", "una actividad por cada recurso", "revisión de la lista de actividades", "C13-C16"),
    ("R7", "Accesibilidad: una vía no visual para cada actividad", "una alternativa por actividad", "prueba con una persona usuaria", "C07, C12"),
    ("R8", "Criterio de cancelación (nubes, viento, fatiga)", "nubosidad > 50 % o viento fuerte o fatiga -> no-go", "pronóstico y revisión en el sitio", "criterio de ejemplo"),
]


def decidir(nombre_noche: str, nubes_pct: float) -> tuple[str, dict]:
    r = VO.analizar(nombre_noche)
    ok_r2 = r["sin_luna_h"] >= 4.0
    ok_nubes = nubes_pct <= 50.0
    return ("GO" if ok_r2 and ok_nubes else "NO-GO"), r


def pruebas() -> None:
    VO.pruebas()
    assert len(REQUISITOS) >= 8
    for rid, texto, criterio, metodo, fuente in REQUISITOS:
        assert texto and criterio and metodo and fuente, rid
    assert any("Sol" in r[1] for r in REQUISITOS)
    llena, _ = decidir("llena (5-6 nov 2025)", 10.0)
    nueva, _ = decidir("nueva (20-21 nov 2025)", 10.0)
    assert llena == "NO-GO" and nueva == "GO"
    assert decidir("nueva (20-21 nov 2025)", 80.0)[0] == "NO-GO"       # con 80 % de nubes se cancela


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for rid, texto, criterio, metodo, fuente in REQUISITOS:
        print(f"{rid}: {texto} | criterio: {criterio} | comprobación: {metodo} ({fuente})")
    for nombre in VO.NOCHES:
        for nubes in (10.0, 80.0):
            d, r = decidir(nombre, nubes)
            print(f"{nombre}, nubes {nubes:.0f} %: {d} (horas sin Luna {r['sin_luna_h']:.2f} de {r['noche_h']:.2f} h; fase media {r['fase_media']:.1f} %)")
    print("Planetas 5-6 nov 2025 (altura al anochecer / al amanecer astronómicos):")
    for p, (a, b) in PLANETAS_5NOV.items():
        print(f"  {p}: {a:+.1f} / {b:+.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
