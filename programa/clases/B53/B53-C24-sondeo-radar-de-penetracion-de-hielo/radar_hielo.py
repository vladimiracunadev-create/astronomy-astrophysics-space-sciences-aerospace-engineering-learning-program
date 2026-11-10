#!/usr/bin/env python3
"""B53-C24: sondeo radar de hielo ILUSTRATIVO. eps_r = 3.15 (uso comun, no consultado), B = 10 MHz, chirp de 10 us, fs = 100 MHz.
c = 299792458 m/s exacta. Sin ruido. Tolerancia: ancho comprimido dentro de 10 % del teorico."""
import cmath, math, platform

C, EPS, B, T, FS = 299792458.0, 3.15, 10e6, 10e-6, 100e6
NS = int(T * FS)
V = C / math.sqrt(EPS)
S = [cmath.exp(1j * math.pi * (B / T) * (k / FS - T / 2) ** 2) for k in range(NS)]

def eco(retardos_muestras, L=1600):
    r = [0j] * L
    for m in retardos_muestras:
        for k in range(NS):
            r[m + k] += S[k]
    return r

def comprimir(r):
    out = []
    for m in range(len(r) - NS + 1):
        out.append(abs(sum(r[m + k] * S[k].conjugate() for k in range(NS))))
    return out

def picos(y):
    mx = max(y)
    return [i for i in range(1, len(y) - 1) if y[i] > y[i - 1] and y[i] >= y[i + 1] and y[i] > 0.5 * mx]

def fwhm_muestras(y):
    i = max(range(len(y)), key=lambda k: y[k])
    nivel = y[i] * math.sqrt(0.5)
    a = i
    while y[a] > nivel: a -= 1
    b = i
    while y[b] > nivel: b += 1
    xa = a + (nivel - y[a]) / (y[a + 1] - y[a])
    xb = b - 1 + (y[b - 1] - nivel) / (y[b - 1] - y[b])
    return xb - xa

def compute():
    res = C / (2 * B * math.sqrt(EPS))
    y1 = comprimir(eco([100]))
    w = fwhm_muestras(y1) / FS
    paso = res / (C / (2 * math.sqrt(EPS)) / FS)  # muestras por resolucion
    y05 = comprimir(eco([100, 100 + round(0.5 * paso)]))
    y2 = comprimir(eco([100, 100 + round(2 * paso)]))
    return dict(v=V, d_2us=V * 2e-6 / 2, d_5us=V * 5e-6 / 2, res=res, fwhm_num=w * C / (2 * math.sqrt(EPS)),
                fwhm_th=0.886 * res, n05=len(picos(y05)), n2=len(picos(y2)), loss=2 * 10 * 3.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"v = {r['v']:.5e} m/s ; profundidad a 2 us = {r['d_2us']:.3f} m ; a 5 us = {r['d_5us']:.3f} m ; resolucion = {r['res']:.4f} m")
    print(f"ancho a mitad de potencia: numerico {r['fwhm_num']:.4f} m ; 0.886*res = {r['fwhm_th']:.4f} m")
    print(f"picos a 0.5 resoluciones: {r['n05']} ; a 2 resoluciones: {r['n2']} ; perdida bidireccional en 3 km = {r['loss']:.0f} dB")
    assert abs(r["fwhm_num"] / r["fwhm_th"] - 1) < 0.10 and r["n05"] == 1 and r["n2"] == 2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
