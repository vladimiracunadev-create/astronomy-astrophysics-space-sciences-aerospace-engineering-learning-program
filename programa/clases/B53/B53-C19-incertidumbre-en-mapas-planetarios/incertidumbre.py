#!/usr/bin/env python3
"""B53-C19: incertidumbre SINTETICA. Errores por eje: referencia 20 m, punteria 15 m, relieve 5 m * tan(30 grados), en cuadratura.
Semilla 20261109, 200000 sorteos. Tolerancias: RMS 1 %, CE90 1 % de 2.146 sigma, sigma_A (D = 3000 m) 2 %."""
import math, platform, random

N = 200000
SIGD = 15.0

def compute():
    rng = random.Random(20261109)
    sig = math.sqrt(20.0 ** 2 + 15.0 ** 2 + (5.0 * math.tan(math.radians(30))) ** 2)
    rad = sorted(math.hypot(rng.gauss(0, sig), rng.gauss(0, sig)) for _ in range(N))
    rms = math.sqrt(sum(r * r for r in rad) / N)
    r = dict(sig=sig, rms_ana=math.sqrt(2) * sig, rms_mc=rms, ce90_ana=2.146 * sig, ce90_mc=rad[int(0.9 * N)])
    r["ce90_r"] = r["ce90_mc"] / sig
    for D in (300.0, 3000.0):
        a = [math.pi * rng.gauss(D, SIGD) ** 2 / 4 for _ in range(N)]
        m = sum(a) / N
        s = math.sqrt(sum((x - m) ** 2 for x in a) / (N - 1))
        k = int(D)
        r[f"sA_ana{k}"] = math.pi * D / 2 * SIGD
        r[f"sA_mc{k}"] = s
        r[f"bias{k}"] = (m - math.pi * D * D / 4) / (math.pi * D * D / 4)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"sigma por eje = {r['sig']:.3f} m ; RMS radial: analitica {r['rms_ana']:.3f} ; MC {r['rms_mc']:.3f} m")
    print(f"CE90: 2.146 sigma = {r['ce90_ana']:.3f} m ; MC = {r['ce90_mc']:.3f} m ({r['ce90_r']:.4f} sigma)")
    for k in (300, 3000):
        print(f"D = {k} m: sigma_A lineal = {r['sA_ana%d' % k]:.1f} m2 ; MC = {r['sA_mc%d' % k]:.1f} m2 ; sesgo relativo de A = {r['bias%d' % k]:+.5f}")
    assert abs(r["rms_mc"] / r["rms_ana"] - 1) < 0.01 and abs(r["ce90_mc"] / r["ce90_ana"] - 1) < 0.01 and abs(r["sA_mc3000"] / r["sA_ana3000"] - 1) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
