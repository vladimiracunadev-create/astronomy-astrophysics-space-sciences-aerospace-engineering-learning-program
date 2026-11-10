#!/usr/bin/env python3
"""B53-C22: maduracion del regolito SINTETICA. S(t) = 0.10 + 0.40 (1 - exp(-t/0.30)), 12 edades (ua), ruido 0.01.
Mezcla: caminata gaussiana con reflexion, 400 pasos de 0.5 cm, 20000 particulas. Semilla 20261109.
Tolerancias: tau a 3 errores tipicos; varianza de la mezcla a 2 %."""
import math, platform, random

TS = [0.05, 0.1, 0.2, 0.3, 0.45, 0.6, 0.8, 1.0, 1.3, 1.6, 2.0, 2.5]
S0, DS, TAU, SIGN = 0.10, 0.40, 0.30, 0.01

def ajusta(ys):
    mejor = None
    for k in range(600):
        tau = 0.05 + k * (1.5 - 0.05) / 599
        x = [1 - math.exp(-t / tau) for t in TS]
        n = len(TS); mx, my = sum(x) / n, sum(ys) / n
        sxx = sum((a - mx) ** 2 for a in x)
        ds = sum((a - mx) * (b - my) for a, b in zip(x, ys)) / sxx
        s0 = my - ds * mx
        rss = sum((b - s0 - ds * a) ** 2 for a, b in zip(x, ys))
        if mejor is None or rss < mejor[0]:
            mejor = (rss, tau, s0, ds)
    return mejor[1:]

def compute():
    rng = random.Random(20261109)
    taus, dss, s0s = [], [], []
    for _ in range(500):
        ys = [S0 + DS * (1 - math.exp(-t / TAU)) + rng.gauss(0, SIGN) for t in TS]
        tau, s0, ds = ajusta(ys)
        taus.append(tau); dss.append(ds); s0s.append(s0)
    m = lambda v: sum(v) / len(v)
    sd = lambda v: math.sqrt(sum((e - m(v)) ** 2 for e in v) / (len(v) - 1))
    n, paso, z = 20000, 0.5, 10.0
    prof = []
    for _ in range(n):
        x = 0.0
        for _ in range(400):
            x = abs(x + rng.gauss(0, paso))
        prof.append(x)
    sig = paso * math.sqrt(400)
    var_mc = sum(p * p for p in prof) / n   # E[|x|^2] = sigma^2 con reflexion
    frac_mc = sum(1 for p in prof if p > z) / n
    return dict(tau_mean=m(taus), tau_sd=sd(taus), dS_mean=m(dss), dS_sd=sd(dss), S0_mean=m(s0s), S0_sd=sd(s0s),
                sig=sig, var_mc=var_mc, var_ana=sig ** 2, frac_mc=frac_mc, frac_ana=math.erfc(z / (math.sqrt(2) * sig)),
                se_tau=sd(taus) / math.sqrt(500))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"tau = {r['tau_mean']:.4f} +- {r['tau_sd']:.4f} (verdadero 0.3) ; dS = {r['dS_mean']:.4f} +- {r['dS_sd']:.4f} (0.4) ; S0 = {r['S0_mean']:.4f} +- {r['S0_sd']:.4f} (0.1)")
    print(f"mezcla: sigma = {r['sig']:.2f} cm ; varianza simulada {r['var_mc']:.3f} ; analitica {r['var_ana']:.3f} cm2")
    print(f"fraccion bajo 10 cm: simulada {r['frac_mc']:.4f} ; erfc {r['frac_ana']:.4f}")
    assert abs(r["tau_mean"] - 0.3) < 3 * r["tau_sd"] and abs(r["var_mc"] / r["var_ana"] - 1) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
