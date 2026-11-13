# SPDX-License-Identifier: Apache-2.0
"""Genera simuladores/documentacion/TABLA_DE_PRECISION.md a partir de `simuladores/datos/*.json`.

Uso: python herramientas/efemerides/tabla_precision.py [--check]
Con --check falla si el archivo versionado no coincide con los datos (para que la documentación no quede desfasada).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DATOS = RAIZ / "simuladores" / "datos"
SALIDA = RAIZ / "simuladores" / "documentacion" / "TABLA_DE_PRECISION.md"
ORDEN = ["sol", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno"]
TITULO = {"sol": "Sistema Solar (heliocéntrico)", "tierra": "Tierra: la Luna", "marte": "Marte", "jupiter": "Júpiter", "saturno": "Saturno",
          "urano": "Urano", "neptuno": "Neptuno"}


RADIO_PLANETAS = {"199": 2439.4, "299": 6051.8, "399": 6378.1366, "499": 3396.19, "599": 71492, "699": 60268, "799": 25559, "899": 24764, "9": 1188.3, "2000001": 469.7}
PERIODO_PLANETAS = {"199": 87.969, "299": 224.701, "399": 365.256, "499": 686.98, "599": 4332.59, "699": 10759.22, "799": 30688.5, "899": 60182, "9": 90560, "2000001": 1680}


def fmt(x, d=2):
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",")


def fecha(jd: float) -> str:
    z = int(jd + 0.5); f = jd + 0.5 - z
    a = z + 32044; b = (4 * a + 3) // 146097; c = a - 146097 * b // 4; d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    dia = e - (153 * m + 2) // 5 + 1; mes = m + 3 - 12 * (m // 10); anio = 100 * b + d - 4800 + m // 10
    return f"{anio:04d}-{mes:02d}-{dia:02d}"


def construir() -> str:
    L = ["# Tabla de precisión de las efemérides", "",
         "Generada automáticamente por `herramientas/efemerides/tabla_precision.py` a partir de `simuladores/datos/*.json`; no se edita a mano.", "",
         "El **error** es la distancia entre la posición interpolada y la que entrega JPL Horizons en 120 épocas aleatorias que no son nodos de la tabla "
         "(máximo y valor cuadrático medio, en km). «Nodos/órbita» es el número aproximado de nodos por revolución. «Cobertura» sólo aparece cuando "
         "Horizons no publica efemérides hasta el 31-12-2050 (el cuerpo se oculta después). Método: [Datos y efemérides](DATOS_Y_EFEMERIDES.md).", ""]
    for n in ORDEN:
        j = DATOS / f"{n}.json"
        if not j.exists():
            continue
        m = json.loads(j.read_text(encoding="utf-8"))
        cs = m["cuerpos"]
        peor = max(cs, key=lambda c: c["error_max_km"])
        L += [f"## {TITULO[n]}", "", f"{len(cs)} cuerpos · peor error máximo: {peor['nombre']} ({fmt(peor['error_max_km'])} km). Marco: {m['marco']}; centro `{m['centro_horizons']}`.", "",
              "| ID | Cuerpo | Radio (km) | Paso | Nodos/órbita | Formato | Err. máx. (km) | Err. rms (km) | Cobertura |", "|---:|---|---:|---:|---:|---|---:|---:|---|"]
        for c in cs:
            radio = c.get("radio_km") or (RADIO_PLANETAS.get(str(c["id"])) if n == "sol" else (1737.4 if str(c["id"]) == "301" else None))
            P = c.get("periodo_d") or (PERIODO_PLANETAS.get(str(c["id"])) if n == "sol" else None)
            paso = (f"{c['paso_min'] / 1440:.4g} d" if c["paso_min"] >= 1440 else f"{c['paso_min']} min").replace(".", ",")
            nodos = (f"{P * 1440 / c['paso_min']:.1f}".replace('.', ',') if P else "—")
            cob = "" if c["jd_valido_fin"] >= 2470172 else f"hasta {fecha(c['jd_valido_fin'])}"
            L.append(f"| {c['id']} | {c['nombre'].replace('|', '/')} | {fmt(radio, 1) if radio else '—'} | {paso} | {nodos} | {c['fmt']} | {fmt(c['error_max_km'], 3)} | {fmt(c['error_rms_km'], 3)} | {cob} |")
        L.append("")
    return "\n".join(L)


def main() -> int:
    t = construir()
    if "--check" in sys.argv:
        if not SALIDA.exists() or SALIDA.read_text(encoding="utf-8") != t:
            print("TABLA_DE_PRECISION.md desfasada: ejecute herramientas/efemerides/tabla_precision.py")
            return 1
        print("TABLA_DE_PRECISION.md al día")
        return 0
    SALIDA.write_text(t, encoding="utf-8")
    print("escrito", SALIDA.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
