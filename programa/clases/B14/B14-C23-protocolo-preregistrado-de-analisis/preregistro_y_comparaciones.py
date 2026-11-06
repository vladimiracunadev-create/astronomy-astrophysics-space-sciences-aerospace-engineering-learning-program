#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C23: por qué se preregistra, con una simulación, y cómo se congela un protocolo.

AVISO: no se registra nada en ningún registro externo (OSF u otro). El
«protocolo» se congela solo con una huella SHA-256 local.
Datos: SINTÉTICOS. 20 000 repeticiones de un estudio ficticio con 20 hipótesis
nulas independientes (no hay efecto real en ninguna), cada una con 50 muestras
gaussianas N(0,1); prueba z bilateral con sigma conocida = 1 (semilla 20261105).
Modelo: con nivel alfa = 0.05 por prueba y 20 pruebas independientes, la
probabilidad de al menos un «positivo» es 1 - 0.95^20 = 0.6415. Con la
corrección de Bonferroni (alfa/20) es 1 - (1 - 0.0025)^20 = 0.0488.
Supuestos: independencia entre pruebas; datos gaussianos con varianza conocida.
Validez: demostración de la inflación de falsos positivos; no es un estudio.
Tolerancia: las frecuencias simuladas deben coincidir con las teóricas dentro
de 4 errores estándar binomiales.
"""
from __future__ import annotations
import hashlib, json, math, platform, sys
import numpy as np
from scipy.stats import norm


def huella(protocolo: dict) -> str:
    return hashlib.sha256(json.dumps(protocolo, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def desviaciones(protocolo: dict, ejecutado: dict):
    return sorted(k for k in set(protocolo) | set(ejecutado) if protocolo.get(k) != ejecutado.get(k))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  (sin registro externo)")
    rng = np.random.default_rng(20261105)
    reps, k, n, alfa = 20_000, 20, 50, 0.05
    z = rng.normal(0.0, 1.0, (reps, k, n)).mean(axis=2) * math.sqrt(n)     # estadístico z bajo la nula
    p = 2 * (1 - norm.cdf(np.abs(z)))
    f_una = float((p[:, 0] < alfa).mean())
    f_alguna = float((p < alfa).any(axis=1).mean())
    f_bonf = float((p < alfa / k).any(axis=1).mean())
    t_una, t_alguna, t_bonf = alfa, 1 - (1 - alfa) ** k, 1 - (1 - alfa / k) ** k
    ee = lambda q: math.sqrt(q * (1 - q) / reps)
    print(f"una sola prueba (preregistrada): falsos positivos = {f_una:.4f} (teórico {t_una:.4f})")
    print(f"20 pruebas, se reporta si alguna sale (sin preregistrar): {f_alguna:.4f} (teórico {t_alguna:.4f})")
    print(f"20 pruebas con Bonferroni (alfa/20): {f_bonf:.4f} (teórico {t_bonf:.4f})")
    prueba(abs(f_una - t_una) < 4 * ee(t_una), "una prueba")
    prueba(abs(f_alguna - t_alguna) < 4 * ee(t_alguna), "alguna de 20")
    prueba(abs(f_bonf - t_bonf) < 4 * ee(t_bonf), "Bonferroni")
    prueba(abs(t_alguna - 0.6415) < 5e-4 and abs(t_bonf - 0.0488) < 5e-4, "valores teóricos")

    # protocolo congelado y detección de desviaciones
    proto = {"hipotesis": "profundidad > 0", "prueba": "z bilateral", "alfa": 0.05, "n_pruebas": 1,
             "exclusiones": "ninguna", "version_datos_sha256": "0e61b27879ae2e80"}
    h = huella(proto)
    print(f"huella del protocolo congelado: {h[:16]}...")
    ejec = dict(proto)
    prueba(desviaciones(proto, ejec) == [] and huella(ejec) == h, "ejecución conforme")
    ejec2 = dict(proto, alfa=0.10, exclusiones="se quitaron 3 puntos")
    d = desviaciones(proto, ejec2)
    print(f"desviaciones detectadas: {d}; la huella cambia: {huella(ejec2) != h}")
    prueba(d == ["alfa", "exclusiones"] and huella(ejec2) != h, "desviaciones detectadas")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
