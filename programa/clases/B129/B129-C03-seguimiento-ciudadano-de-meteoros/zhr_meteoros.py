#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C03: tasa horaria cenital (ZHR) desde recuentos de meteoros SINTETICOS.

Todo SINTETICO: lluvia con ZHR verdadera = 100 /h e indice de poblacion r = 2.2; 40 observadores inventados con magnitud
limite lm, altura del radiante h, fraccion de nubes k y tiempo efectivo T. NO es ninguna lluvia ni observacion real.
Relacion usada (estandar; NO consultada en una fuente concreta, la pagina de la IMO no la da):
  recuentos esperados  E = ZHR * sin(h) * r^(lm - 6.5) * (1 - k) * T   (h: altura del radiante; lm: magnitud limite; T en horas)
  => ZHR_i = N_i / (sin(h) * r^(lm-6.5) * (1-k) * T)  con incertidumbre sqrt(N_i)/factor (Poisson).
Estimador combinado de maxima verosimilitud: ZHR = sum(N_i) / sum(f_i), f_i = sin(h) r^(lm-6.5) (1-k) T; var = ZHR / sum(f_i).
Segunda via: repeticiones de Monte Carlo (semilla 129, 4000) para media y desviacion; tolerancias: media dentro de 3 errores
estandar, desviacion MC dentro del 5 % de sqrt(ZHR/sum f).
Contador de Poisson: suma de Poisson(<=30) (algoritmo de Knuth), exacta porque la suma de Poisson es Poisson.
"""
from __future__ import annotations
import math, platform, random, statistics

ZHR_VERDAD, R = 100.0, 2.2


def poisson(lam, rng):
    total = 0
    while lam > 0:
        l = min(lam, 30.0)
        lam -= l
        L, k, p = math.exp(-l), 0, 1.0
        while True:
            p *= rng.random()
            if p <= L:
                break
            k += 1
        total += k
    return total


def factor(lm, h_deg, k, T):
    return math.sin(math.radians(h_deg)) * R ** (lm - 6.5) * (1 - k) * T


def observadores(rng, n=40):
    lst = []
    for i in range(n):
        lm = rng.choice([5.0, 5.5, 6.0, 6.5])
        h = rng.uniform(25, 75)
        k = rng.choice([0.0, 0.0, 0.1, 0.25])
        T = rng.choice([0.5, 1.0, 1.0, 2.0])
        lst.append((f"O{i+1:02d}", lm, h, k, T))
    return lst


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    print("DATOS SINTETICOS: ZHR verdadera = 100 /h, r = 2.2; 40 observadores inventados")
    obs = observadores(rng)
    F = [factor(lm, h, k, T) for _, lm, h, k, T in obs]
    suma_f = sum(F)
    # una realizacion
    N = [poisson(ZHR_VERDAD * f, rng) for f in F]
    z_i = [n / f for n, f in zip(N, F)]
    zhr = sum(N) / suma_f
    sig = math.sqrt(sum(N)) / suma_f
    sig_teo = math.sqrt(ZHR_VERDAD / suma_f)
    print(f"Una realizacion: recuentos totales = {sum(N)}, suma de factores = {suma_f:.3f} h")
    print(f"  ZHR combinada = {zhr:.2f} +/- {sig:.2f} /h (verdad 100; sigma teorica {sig_teo:.2f})")
    print("  ejemplos individuales (ZHR_i = N/f):")
    for (nom, lm, h, k, T), n, f, z in list(zip(obs, N, F, z_i))[:5]:
        e = math.sqrt(max(n, 1)) / f
        print(f"   {nom}: lm={lm:.1f} h={h:4.1f} k={k:.2f} T={T:.1f} h  N={n:3d}  f={f:6.3f}  ZHR_i={z:7.1f} +/- {e:6.1f}")
    # ingenuo: ignorar lm, h y k
    ingenuo = sum(N) / sum(T for *_, T in obs)
    print(f"  Estimador ingenuo (solo N/T, sin corregir lm, h ni nubes) = {ingenuo:.1f} /h (sesgado)")
    # Monte Carlo
    reps = 4000
    zs = []
    for _ in range(reps):
        zs.append(sum(poisson(ZHR_VERDAD * f, rng) for f in F) / suma_f)
    media, desv = statistics.fmean(zs), statistics.pstdev(zs)
    ee = sig_teo / math.sqrt(reps)
    print(f"Monte Carlo ({reps} repeticiones): media = {media:.3f}, desviacion = {desv:.3f}; teorica {sig_teo:.3f}")
    assert abs(media - ZHR_VERDAD) < 3 * ee, "el estimador esta sesgado"
    assert abs(desv - sig_teo) / sig_teo < 0.05, "la desviacion MC no coincide con la teorica"
    # sensibilidad a un error de 0.5 mag en la magnitud limite
    print(f"Sensibilidad: un error de +0.5 mag en lm cambia el factor en r^0.5 = {R ** 0.5:.3f} ({(R ** 0.5 - 1) * 100:.1f} %)")
    # numero de observadores para una incertidumbre relativa del 5 %
    f_med = suma_f / len(F)
    n_obs = math.ceil(ZHR_VERDAD / (0.05 ** 2 * ZHR_VERDAD ** 2 * f_med))
    print(f"Para 5 % de incertidumbre relativa hacen falta sum(f) = {1 / (0.05 ** 2 * ZHR_VERDAD):.1f} h; con f medio {f_med:.3f} h son {n_obs} observadores")
    # comprobacion algebraica independiente
    z_alt = sum(n * f for n, f in zip(N, F)) / sum(f * f for f in F)
    print(f"Segunda via (minimos cuadrados sin peso) = {z_alt:.2f} /h (distinta de la de maxima verosimilitud, {zhr:.2f})")
    assert abs(zhr - ZHR_VERDAD) < 4 * sig_teo
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
