#!/usr/bin/env python3
"""B53-C28: inversion gravimetrica de una esfera enterrada SINTETICA. SI. G = 6.67430e-11 (NIST). a = 2 km, drho = 300, z = 5 km.
Perfil -20..20 km cada 1 km, ruido 2e-7 m/s2, 300 repeticiones, semilla 20261109. Tolerancias: z a 3 errores tipicos; razon de ancho 1e-6."""
import math, platform, random

G = 6.67430e-11
XS = [float(i) * 1000 for i in range(-20, 21)]
Z0, A0, DR = 5000.0, 2000.0, 300.0
M0 = DR * 4 / 3 * math.pi * A0 ** 3
SIG = 2e-7

def gz(m, z, x):
    return G * m * z / (x * x + z * z) ** 1.5

def forma(z):
    return [z / (x * x + z * z) ** 1.5 for x in XS]

def resid(d, z):
    f = forma(z)
    m = sum(a * b for a, b in zip(d, f)) / (G * sum(a * a for a in f))
    return sum((a - G * m * b) ** 2 for a, b in zip(d, f)), m

def invierte(d):
    zs = [500.0 * k for k in range(1, 41)]
    zb = min(zs, key=lambda z: resid(d, z)[0])
    a, b = zb - 500.0, zb + 500.0
    g = (math.sqrt(5) - 1) / 2
    c, e = b - g * (b - a), a + g * (b - a)
    for _ in range(60):
        if resid(d, c)[0] < resid(d, e)[0]:
            b, e = e, c
            c = b - g * (b - a)
        else:
            a, c = c, e
            e = a + g * (b - a)
    z = 0.5 * (a + b)
    return z, resid(d, z)[1]

def compute():
    rng = random.Random(20261109)
    zs, ms = [], []
    for _ in range(300):
        d = [gz(M0, Z0, x) + rng.gauss(0, SIG) for x in XS]
        z, m = invierte(d)
        zs.append(z); ms.append(m)
    mean = lambda v: sum(v) / len(v)
    sd = lambda v: math.sqrt(sum((e - mean(v)) ** 2 for e in v) / (len(v) - 1))
    lo, hi = 0.0, 5 * Z0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gz(M0, Z0, mid) > 0.5 * gz(M0, Z0, 0.0):
            lo = mid
        else:
            hi = mid
    m2 = 2400.0 * 4 / 3 * math.pi * 1000.0 ** 3
    deg = max(abs(gz(M0, Z0, x) - gz(m2, Z0, x)) for x in XS)
    return dict(m_true=M0, peak=gz(M0, Z0, 0.0) * 1e5, peak_ms2=gz(M0, Z0, 0.0), z_mean=mean(zs) / 1e3, z_sd=sd(zs) / 1e3,
                m_mean=mean(ms), m_sd=sd(ms), xh_r=0.5 * (lo + hi) / Z0, xh_a=math.sqrt(2 ** (2 / 3) - 1), deg=deg,
                z_rel=sd(zs) / Z0, se=sd(zs) / math.sqrt(300) / 1e3)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"m = {r['m_true']:.4e} kg ; maximo = {r['peak']:.4f} mGal")
    print(f"inversion (300 perfiles): z = {r['z_mean']:.4f} +- {r['z_sd']:.4f} km (verdadero 5) ; m = {r['m_mean']:.4e} +- {r['m_sd']:.2e} kg")
    print(f"ancho a media altura / profundidad: numerico {r['xh_r']:.6f} ; teorico {r['xh_a']:.6f}")
    print(f"degeneracion (a = 1 km, drho = 2400): diferencia maxima {r['deg']:.2e} m/s2")
    assert abs(r["z_mean"] - 5.0) < 3 * r["se"] + 0.01 and abs(r["xh_r"] / r["xh_a"] - 1) < 1e-6 and r["deg"] < 1e-18
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
