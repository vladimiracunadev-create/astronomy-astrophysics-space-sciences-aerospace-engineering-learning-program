#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C08: limpieza reproducible de una bitácora con pandas.

Datos: SINTÉTICOS. Bitácora de 200 filas (con identificador único id_obs; sin él, dos observaciones distintas con los mismos valores parecerían duplicadas) generada con semilla fija 20261105:
nombre de objeto con mayúsculas y espacios inconsistentes, magnitud (escala de
magnitudes, adimensional) con 7 valores centinela -99.0, 5 valores ausentes
(NaN), 4 filas duplicadas y 3 valores atípicos de +5 mag inyectados a
propósito, y tiempo de exposición en segundos. Las cantidades de cada defecto
SE CONOCEN de antemano, de modo que la limpieza se comprueba contra ellas.
Modelo: normalizar texto, convertir centinelas en NaN, eliminar duplicados
exactos, marcar (no borrar) atípicos con la mediana y la MAD (desviación
absoluta mediana; criterio |x - med| > 5 * 1.4826 * MAD).
Supuestos: los defectos son los conocidos; los atípicos son errores de
captura, no variaciones reales.
Validez: demostración; el umbral de 5 MAD no es universal.
Tolerancia: los recuentos deben coincidir exactamente con los planeados.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import pandas as pd


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def generar(rng):
    n = 196
    objetos = rng.choice(["OBJ-A", "OBJ-B", "OBJ-C"], n)
    mag = rng.normal(15.0, 0.1, n)
    t_exp = rng.choice([30.0, 60.0, 120.0], n)
    df = pd.DataFrame({"id_obs": np.arange(n), "objeto": objetos, "mag": mag, "t_exp_s": t_exp})
    df.loc[5:11, "mag"] = -99.0
    df.loc[[20, 40, 60, 80, 100], "mag"] = np.nan
    df.loc[[130, 150, 170], "mag"] = df.loc[[130, 150, 170], "mag"] + 5.0
    # suciedad de texto: variantes de mayúsculas y espacios del PROPIO nombre
    df.loc[0, "objeto"] = "  " + df.loc[0, "objeto"].lower() + " "
    df.loc[1, "objeto"] = df.loc[1, "objeto"].title()
    df.loc[2, "objeto"] = df.loc[2, "objeto"].lower()
    df.loc[3, "objeto"] = " " + df.loc[3, "objeto"]
    # 4 duplicados que repiten las filas 0-3 tal cual (misma id_obs)
    df = pd.concat([df, df.iloc[[0, 1, 2, 3]]], ignore_index=True)
    return df


def limpiar(df):
    out = df.copy()
    out["objeto"] = out["objeto"].str.strip().str.upper()
    out["mag"] = out["mag"].mask(out["mag"] == -99.0)
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  pandas {pd.__version__}")
    rng = np.random.default_rng(20261105)
    sucio = generar(rng)
    print(f"filas = {len(sucio)}; nombres distintos antes = {sucio['objeto'].nunique()}")
    prueba(len(sucio) == 200, "200 filas")
    prueba(int((sucio["mag"] == -99.0).sum()) == 7, "7 centinelas")
    prueba(int(sucio["mag"].isna().sum()) == 5, "5 ausentes")

    tmp = limpiar(sucio)
    n_nom = tmp["objeto"].nunique()
    print(f"nombres distintos tras normalizar = {n_nom}")
    prueba(n_nom == 3, "3 nombres tras normalizar")
    prueba(int(tmp["mag"].isna().sum()) == 12, "12 NaN (5 + 7 centinelas)")

    ndup = int(tmp.duplicated().sum())
    print(f"duplicados exactos = {ndup}")
    prueba(ndup == 4, "4 duplicados")
    limpio = tmp.drop_duplicates().reset_index(drop=True)
    prueba(len(limpio) == 196, "196 filas sin duplicados")

    med = limpio["mag"].median()
    mad = (limpio["mag"] - med).abs().median()
    sigma_robusta = 1.4826 * mad
    limpio["atipico"] = (limpio["mag"] - med).abs() > 5 * sigma_robusta
    n_at = int(limpio["atipico"].sum())
    print(f"mediana = {med:.4f}, sigma robusta = {sigma_robusta:.4f}, atípicos marcados = {n_at}")
    prueba(n_at == 3, "3 atípicos inyectados")
    prueba(not bool(limpio.loc[limpio["mag"].isna(), "atipico"].any()), "NaN no es atípico")
    media_sucia = sucio["mag"].mean()
    media_limpia = limpio.loc[~limpio["atipico"], "mag"].mean()
    print(f"media sucia (con -99 y atípicos) = {media_sucia:.3f}; media limpia = {media_limpia:.4f}")
    prueba(abs(media_limpia - 15.0) < 0.05, "media limpia cerca de 15")
    print("recuento por objeto:", limpio["objeto"].value_counts().sort_index().to_dict())
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
