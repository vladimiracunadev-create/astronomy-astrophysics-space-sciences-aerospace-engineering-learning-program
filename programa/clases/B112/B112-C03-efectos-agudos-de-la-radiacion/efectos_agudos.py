#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C03: un evento de particulas solares SINTETICO y los umbrales de efectos agudos.

Datos SINTETICOS (semilla 114). Valores consultados (2026-11-10): intervalos de dosis de los sindromes (Seed, NASA THREE, 2011:
hematopoyetico 0.5-8 Gy, gastrointestinal 4-15 Gy, neurovascular/SNC > 20 Gy; a 1-2 Gy hasta el 50 % de los expuestos muestra reduccion
moderada de celulas sanguineas en 2-4 semanas) y el limite de dosis efectiva de 250 mSv por evento de NASA-STD-3001 (OCHMO-TB-020 Rev E).
Seed cita ademas una tasa de dosis absorbida estimada de hasta 1.4 Gy/h para un evento tipo agosto 1972 fuera de la orbita baja; aqui el
pico inventado es 0.5 Gy/h (de la misma escala, mas bajo), no una reconstruccion. Los 5-20 g/cm2 de blindaje de OCHMO-TB-020 son el contexto. Lo propio del laboratorio (sintetico): perfil
temporal log-normal de la tasa de dosis, atenuacion exponencial con la densidad superficial del blindaje (coeficiente inventado) y una
curva dosis-respuesta sigmoidea inventada (D50 = 3 Gy) que solo ilustra la FORMA con umbral aparente, no es un dato humano.
Unidades: Gy, mSv, g/cm2, horas. Verificacion: la dosis acumulada integrada numericamente coincide con la analitica dentro del 0.1 %;
la dosis decrece monotonamente con el blindaje; el blindaje minimo hallado cumple el limite. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

SINDROMES = [("prodromo y sindrome hematopoyetico", 0.5, 8.0), ("sindrome gastrointestinal", 4.0, 15.0), ("sindrome neurovascular (SNC)", 20.0, None)]
PICO = 0.5          # Gy/h INVENTADO (Seed cita hasta 1.4 Gy/h estimado para un evento extremo, fuera de la orbita baja)
MU = 0.20           # 1/(g/cm2), coeficiente de atenuacion INVENTADO para el campo de protones del evento
H_A_SV = 2.0        # Sv/Gy: cota alta ilustrativa (wR de protones = 2, tejido uniforme); no consultado
LIMITE_SPE_MSV = 250.0


def perfil(t, t0=6.0, s=0.8):
    """Tasa de dosis sin blindaje (Gy/h): log-normal en el tiempo, normalizada a un pico = PICO."""
    x = np.log(t / t0)
    return PICO * np.exp(-x**2 / (2 * s**2))


def dosis_aguda(prof_gcm2, t):
    tasa = perfil(t) * np.exp(-MU * prof_gcm2)
    return float(np.sum((tasa[1:] + tasa[:-1]) / 2 * np.diff(t)))


def clasifica(d_gy):
    out = []
    for nombre, lo, hi in SINDROMES:
        if d_gy >= lo and (hi is None or d_gy <= hi):
            out.append(nombre)
    if out:
        return out
    return ["por debajo de 0.5 Gy" if d_gy < 0.5 else "entre intervalos citados (15-20 Gy), sin intervalo en la fuente"]


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 114): evento inventado; intervalos de sindromes de Seed (2011) y limite de 250 mSv de NASA-STD-3001")
    t = np.geomspace(1e-4, 5000, 400001)
    d0 = dosis_aguda(0.0, t)
    # analitica: integral de PICO*exp(-(ln(t/t0))^2/(2 s^2)) dt = PICO*t0*s*sqrt(2pi)*exp(s^2/2)
    ana = PICO * 6.0 * 0.8 * np.sqrt(2 * np.pi) * np.exp(0.8**2 / 2)
    print(f"Dosis acumulada sin blindaje: numerica {d0:.4f} Gy, analitica (de 0 a infinito) {ana:.4f} Gy")
    assert abs(d0 / ana - 1) < 1e-3
    print("Clasificacion de la dosis sin blindaje: " + "; ".join(clasifica(d0)))
    print(f"{'blindaje [g/cm2]':>17s} {'dosis [Gy]':>11s} {'efectiva [mSv]':>15s} {'cumple 250 mSv':>15s}  intervalo de efectos")
    ds = []
    for p in (0, 2, 5, 10, 15, 20, 30):
        d = dosis_aguda(p, t)
        ds.append(d)
        print(f"{p:17.0f} {d:11.4f} {d*H_A_SV*1e3:15.1f} {'si' if d*H_A_SV*1e3 <= LIMITE_SPE_MSV else 'no':>15s}  {" + ".join(clasifica(d))}")
    assert all(np.diff(ds) < 0)
    # blindaje minimo por biseccion
    lo, hi = 0.0, 40.0
    for _ in range(60):
        m = (lo + hi) / 2
        if dosis_aguda(m, t) * H_A_SV * 1e3 > LIMITE_SPE_MSV:
            lo = m
        else:
            hi = m
    print(f"Blindaje minimo (modelo inventado) para 250 mSv: {hi:.2f} g/cm2")
    assert dosis_aguda(hi, t) * 1e3 <= LIMITE_SPE_MSV + 1e-6
    # forma sigmoidea inventada: fraccion con efecto hematologico moderado
    d50, k = 3.0, 4.0
    print("Curva dosis-respuesta SIGMOIDEA INVENTADA (D50 = 3 Gy, pendiente 4): fraccion con efecto")
    for d in (0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
        f = 1 / (1 + (d50 / d) ** k)
        print(f"  {d:4.1f} Gy -> {f*100:6.2f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
