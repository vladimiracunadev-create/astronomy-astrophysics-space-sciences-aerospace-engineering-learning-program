#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C20: triangulación con base y ángulos, y su incertidumbre.

Datos (PUBLICADOS; estimados): NASA NSSDC Moon Fact Sheet (2024-01-11; consulta 2026-11-05):
semieje mayor 384 400 km; NASA Exoplanet Archive (consulta TAP del 2026-11-05; mutable):
Próxima Cen p = 768,5 ± 0,2030 mas; tau Cet 277,516 ± 0,5173; GJ 1061 272,245 ± 0,0661; IAU 2015 B3:
radio ecuatorial nominal 6,3781e6 m; SI: 1 au = 149 597 870 700 m. Base de las estaciones (6000 km),
ruido angular (1′) y semilla del generador aleatorio: SINTÉTICOS.
Modelo: dos estaciones separadas por una base B ven un mismo objeto bajo los ángulos A y B_
medidos entre la base y la visual; la altura del objeto sobre la base es h = B/(cot A + cot B_).
Propagación a primer orden: σ_h = sqrt(2)·(B/4)·(1 + (2h/B)²)·σθ para el caso simétrico (ángulos
independientes con la misma σθ). Paralaje: d = 1 au / tan p, δd/d = δp/p.
Supuestos: plano; ruido gaussiano independiente en los ángulos; sin error en la base.
Validez: σθ pequeña frente al ángulo entre la visual y la base. Tolerancia: 1e-9 relativa en
la triangulación sin ruido; 5 % entre la desviación típica simulada (40 000 casos) y la analítica.
"""
from __future__ import annotations
import math, platform, random, sys

AU = 149_597_870_700.0
PC = 648_000.0 / math.pi * AU
MAS = math.pi / (648_000.0 * 1000.0)


def altura(B, A, Bb):
    return B / (1 / math.tan(A) + 1 / math.tan(Bb))


def angulos_exactos(B, h, x0):
    """Ángulos (en las estaciones en 0 y B) hacia un objeto en (x0, h)."""
    A = math.atan2(h, x0)
    Bb = math.atan2(h, B - x0)
    return A, Bb


def sigma_h(B, h, sig):
    return math.sqrt(2) * (B / 4) * (1 + (2 * h / B) ** 2) * sig


def pruebas():
    # Sin ruido, la triangulación devuelve la altura exacta (sintético)
    for B, h, x0 in ((10.0, 7.5, 5.0), (6000.0, 384400.0, 3000.0), (1.0, 3.0, 0.2)):
        A, Bb = angulos_exactos(B, h, x0)
        assert abs(altura(B, A, Bb) / h - 1) < 1e-9
    # Ley de senos: distancia a la estación 1 = B sen(Bb)/sen(A+Bb) = h/sen A
    B, h, x0 = 10.0, 7.5, 5.0
    A, Bb = angulos_exactos(B, h, x0)
    assert abs(B * math.sin(Bb) / math.sin(A + Bb) - h / math.sin(A)) < 1e-12
    # Paralaje: tan p · d = 1 au y δd/d = δp/p a primer orden
    p = 768.5 * MAS
    d = AU / math.tan(p)
    assert abs(math.tan(p) * d / AU - 1) < 1e-12
    dp = 0.203 * MAS
    d2 = AU / math.tan(p - dp)
    assert abs((d2 - d) / d - dp / p) < 1e-3
    # Monte Carlo frente a la propagación analítica (caso simétrico, sintético)
    rng = random.Random(20261105)
    B, h, sig = 6000.0, 384_400.0, math.radians(1 / 60)
    x0 = B / 2
    A, Bb = angulos_exactos(B, h, x0)
    muestras = [altura(B, A + rng.gauss(0, sig), Bb + rng.gauss(0, sig)) for _ in range(40_000)]
    media = sum(muestras) / len(muestras)
    sd = math.sqrt(sum((m - media) ** 2 for m in muestras) / (len(muestras) - 1))
    assert abs(sd / sigma_h(B, h, sig) - 1) < 0.05, (sd, sigma_h(B, h, sig))
    return sd


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sd = pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (sin ruido exacto, ley de senos, paralaje, Monte Carlo = propagación analítica ±5 %)")
    B, h = 6000.0, 384_400.0
    sig = math.radians(1 / 60)
    print(f"\nLuna (S1) con dos estaciones sintéticas: B = {B:.0f} km, σθ = 1′ = {sig:.3e} rad, h = {h:.0f} km")
    A, Bb = angulos_exactos(B, h, B / 2)
    print(f"  ángulos en las estaciones: {math.degrees(A):.4f}° y {math.degrees(Bb):.4f}° (casi 90°: visuales casi paralelas)")
    print(f"  σ_h analítica = {sigma_h(B, h, sig):.0f} km ({sigma_h(B, h, sig) / h * 100:.2f} %); simulada = {sd:.0f} km")
    print(f"  aproximación h² σθ √2 / B = {math.sqrt(2) * h * h * sig / B:.0f} km")
    print("\nBase necesaria para 10 % de error relativo (σθ = 1′): B ≈ 10·√2·h·σθ =",
          f"{10 * math.sqrt(2) * h * sig:.0f} km (diámetro terrestre: {2 * 6378.1:.0f} km)")
    print("\nCon la base cambiando (Luna, σθ = 1′):")
    for Bi in (1000.0, 6000.0, 12000.0):
        print(f"  B = {Bi:7.0f} km → σ_h/h = {sigma_h(Bi, h, sig) / h * 100:6.2f} %")
    print("\nParalaje estelar (base 1 au): d = 1/p, error relativo = δp/p")
    print(f"{'Estrella':<13}{'p (mas)':>10}{'δp (mas)':>10}{'d (pc)':>10}{'δd (pc)':>10}{'δd/d':>10}")
    for n, p, e in (("Proxima Cen", 768.5, 0.203021), ("tau Cet", 277.516, 0.517309), ("GJ 1061", 272.245, 0.0660788)):
        d_pc = 1000 / p
        print(f"{n:<13}{p:10.3f}{e:10.3f}{d_pc:10.4f}{d_pc * e / p:10.4f}{e / p:10.2e}")
    print(f"\nAlcance con 10 % y δp = 0,2 mas: p ≥ 2 mas → d ≤ {1000 / 2:.0f} pc")
    print(f"Una base de 2 au (extremos de la órbita terrestre) tiene un paralaje de ±p: el ángulo total 2p = {2 * 768.5:.1f} mas para Próxima")


if __name__ == "__main__":
    main()
