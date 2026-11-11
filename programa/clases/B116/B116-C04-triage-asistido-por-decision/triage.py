#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C04: puntaje de triage ILUSTRATIVO sobre casos SINTETICOS, sub-triage con ruido y efecto del retardo.

Todo es sintetico (semilla 119) y NO describe a ninguna persona. El puntaje por parametro (0 a 3) usa bandas PROPIAS del laboratorio,
que NO son las de NEWS2 ni las de ninguna guia clinica. De NEWS2 (cuadro de umbrales del Royal College of Physicians, consultado
2026-11-10) solo se toma la estructura de las bandas agregadas: 0-4 bajo, 5-6 medio, 7 o mas alto, y el disparador de un 3 en un solo
parametro (respuesta urgente aunque el total sea bajo). Estados verdaderos latentes del caso: 0 estable, 1 en deterioro, 2 critico
(prevalencias 80 %, 15 %, 5 %, ilustrativas). Retardo de comunicaciones: de 4 a 24 minutos en un sentido entre Marte y la Tierra segun
la pagina del Centro Goddard de la NASA (consultada 2026-11-10); retardo = ida y vuelta (2 x unidireccional) mas 10 min de revision en
tierra (ilustrativo). Tiempo hasta el evento de un caso critico: exponencial de media 60 min (ilustrativo). Solo numpy.
"""
from __future__ import annotations
import platform
import numpy as np

MEDIAS = {  # por estado latente: (FC lpm, FR resp/min, SpO2 %, T C, PAS mmHg)
    0: (72, 14, 97.5, 36.8, 118),
    1: (104, 22, 93.5, 38.2, 98),
    2: (128, 29, 89.0, 38.9, 84),
}
SIGMAS = (9.0, 2.5, 1.8, 0.35, 10.0)


def puntos(fc, fr, spo2, t, pas):
    """Puntos 0-3 por parametro con bandas ILUSTRATIVAS (no NEWS2)."""
    p = np.zeros(fc.shape + (5,), dtype=int)
    p[..., 0] = np.select([(fc >= 130) | (fc <= 40), fc >= 110, (fc >= 95) | (fc <= 45)], [3, 2, 1], 0)
    p[..., 1] = np.select([(fr >= 25) | (fr <= 8), fr >= 21], [3, 2], 0)
    p[..., 2] = np.select([spo2 <= 91, spo2 <= 93, spo2 <= 95], [3, 2, 1], 0)
    p[..., 3] = np.select([(t >= 39.1) | (t <= 35.0), t >= 38.1], [3, 1], 0)
    p[..., 4] = np.select([pas <= 90, pas <= 100, pas <= 110], [3, 2, 1], 0)
    return np.minimum(p, 3)


def categoria(p):
    tot = p.sum(axis=-1)
    rojo = (p == 3).any(axis=-1)
    cat = np.where(tot >= 7, 2, np.where(tot >= 5, 1, 0))
    cat = np.where(rojo & (cat == 0), 1, cat)  # un 3 en un parametro: al menos respuesta urgente
    return cat


def simular(n, ruido, rng):
    est = rng.choice(3, size=n, p=[0.80, 0.15, 0.05])
    v = np.zeros((n, 5))
    for e in range(3):
        m = est == e
        mu = np.array(MEDIAS[e])
        sd = np.array(SIGMAS)
        v[m] = mu + rng.normal(0, 1, (m.sum(), 5)) * sd
    medido = v + rng.normal(0, 1, v.shape) * np.array(SIGMAS) * 0.5 * ruido
    return est, medido


def evaluar(est, cat):
    cm = np.zeros((3, 3), dtype=int)
    for e, c in zip(est, cat):
        cm[e, c] += 1
    sens = cm[1:, 1:].sum() / cm[1:, :].sum()
    esp = cm[0, 0] / cm[0, :].sum()
    sub = float(np.mean(cat < est))
    return cm, float(sens), float(esp), sub


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 119): casos simulados; el puntaje es ILUSTRATIVO y no es NEWS2 ni una guia clinica")
    rng = np.random.default_rng(119)
    # control de monotonia
    base = np.array([[72.0, 14.0, 97.5, 36.8, 118.0]])
    prev = -1
    ok = True
    for k in range(0, 11):
        v = base + k * np.array([[5.0, 1.5, -0.8, 0.25, -4.0]])
        s = int(puntos(*[v[:, i] for i in range(5)]).sum())
        ok &= s >= prev
        prev = s
    print(f"Control: el puntaje total no baja cuando todos los signos empeoran (11 pasos): {ok}")
    assert ok
    print("Desempeno del triage segun el ruido del sensor (n = 20000; matriz: filas = estado verdadero 0/1/2, columnas = categoria 0/1/2):")
    sub0 = None
    for ruido in (0.0, 1.0, 2.0):
        est, med = simular(20000, ruido, rng)
        cat = categoria(puntos(*[med[:, i] for i in range(5)]))
        cm, sens, esp, sub = evaluar(est, cat)
        if ruido == 0.0:
            sub0 = sub
        print(f"  ruido = {ruido:3.1f} x: sensibilidad (estado >=1 -> categoria >=1) = {sens:.3f}; especificidad = {esp:.3f}; sub-triage = {100 * sub:5.2f} %")
        print(f"      matriz = {cm.tolist()}")
    est, med = simular(20000, 1.0, rng)
    cat = categoria(puntos(*[med[:, i] for i in range(5)]))
    print(f"  con ruido 1.0 x: criticos (n = {int((est == 2).sum())}) con categoria alta: {100 * np.mean(cat[est == 2] == 2):.1f} %; con baja: {100 * np.mean(cat[est == 2] == 0):.1f} %")
    print("Efecto del retardo de comunicaciones en la decision remota (un caso con categoria alta; tiempo hasta el evento ~ exp, media 60 min):")
    print("  retardo unidireccional [min]   ida y vuelta + revision [min]   P(respuesta de tierra llega antes del evento)   decision a bordo (0 min)")
    for d in (0, 4, 12, 24):
        t_resp = 2 * d + 10
        print(f"            {d:3d}                     {t_resp:5.0f}                     {np.exp(-t_resp / 60):6.3f}                        {np.exp(0):6.3f}")
    assert np.exp(-58 / 60) < np.exp(-10 / 60)
    print("  regla de autonomia (ilustrativa): categoria alta -> la tripulacion actua de inmediato y avisa; categoria media -> consulta a tierra")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
