#!/usr/bin/env python3
"""B53-C30: radar de subsuelo SINTETICO. eps1 = 3.0 (regolito), eps2 = 7.0 (roca), ilustrativos. c = 299792458 exacta.
Reflector puntual a d = 3 m; trazas -10..10 m cada 0.5 m; ruido de tiempo 0.5 ns; 500 repeticiones; semilla 20261109.
Tolerancias: v a 3 errores tipicos; recuperacion sin ruido 1e-9."""
import math, platform, random

C, E1, E2, D0, SIGT = 299792458.0, 3.0, 7.0, 3.0, 0.5e-9
XS = [-10 + 0.5 * i for i in range(41)]
V0 = C / math.sqrt(E1)

def ajusta(ts):
    x2 = [x * x for x in XS]
    y = [t * t for t in ts]
    n = len(XS); mx, my = sum(x2) / n, sum(y) / n
    pend = sum((a - mx) * (b - my) for a, b in zip(x2, y)) / sum((a - mx) ** 2 for a in x2)
    inter = my - pend * mx
    v = 2 / math.sqrt(pend)
    return v, math.sqrt(inter) * v / 2

def compute():
    rng = random.Random(20261109)
    exacto = [2 * math.sqrt(D0 ** 2 + x * x) / V0 for x in XS]
    v0, d0 = ajusta(exacto)
    vs, ds = [], []
    for _ in range(500):
        v, d = ajusta([t + rng.gauss(0, SIGT) for t in exacto])
        vs.append(v); ds.append(d)
    mean = lambda a: sum(a) / len(a)
    sd = lambda a: math.sqrt(sum((e - mean(a)) ** 2 for e in a) / (len(a) - 1))
    Rc = (math.sqrt(E1) - math.sqrt(E2)) / (math.sqrt(E1) + math.sqrt(E2))
    t0 = 2 * D0 / V0
    vw = C / math.sqrt(4.0)
    dw = vw * t0 / 2
    return dict(Rc=Rc, R2=Rc * Rc, R_dB=10 * math.log10(Rc * Rc), v_true=V0, t0=t0 * 1e9, v_mean=mean(vs), v_sd=sd(vs),
                d_mean=mean(ds), d_sd=sd(ds), err0=max(abs(v0 / V0 - 1), abs(d0 / D0 - 1)), v_wrong=vw, d_wrong=dw,
                d_wrong_pct=100 * (dw / D0 - 1), se=sd(vs) / math.sqrt(500))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"R = {r['Rc']:.5f} ; R^2 = {r['R2']:.5f} ; perdida de reflexion = {r['R_dB']:.3f} dB")
    print(f"v verdadera = {r['v_true']:.5e} m/s ; t0 = {r['t0']:.3f} ns ; error del ajuste sin ruido = {r['err0']:.2e}")
    print(f"500 radargramas: v = {r['v_mean']:.5e} +- {r['v_sd']:.2e} m/s ; d = {r['d_mean']:.4f} +- {r['d_sd']:.4f} m")
    print(f"con eps = 4 supuesto: v = {r['v_wrong']:.4e} m/s ; d = {r['d_wrong']:.4f} m ({r['d_wrong_pct']:+.1f} %)")
    assert r["err0"] < 1e-9 and abs(r["v_mean"] - r["v_true"]) < 3 * r["se"] + 1e4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
