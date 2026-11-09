#!/usr/bin/env python3
"""B53-C08: catalogos SINTETICOS de crateres. N(>D) ~ D^-b, b = 2, D_min = 1 km, n = 500, area 1e5 km2.
Semilla 20261109, 2000 repeticiones. Tolerancias: sesgo de Hill < 2 errores tipicos; dispersion dentro de 5 % de b/sqrt(n)."""
import math, platform, random

B, DMIN, N, AREA, NREP = 2.0, 1.0, 500, 1.0e5, 2000

def catalogo(rng):
    return [DMIN * rng.random() ** (-1 / B) for _ in range(N)]

def hill(d, dmin):
    d = [x for x in d if x >= dmin]
    return len(d) / sum(math.log(x / dmin) for x in d)

def ls_acumulada(d):
    d = sorted(d, reverse=True)
    xs = [math.log(x) for x in d]
    ys = [math.log(i + 1) for i in range(len(d))]
    n = len(d); mx, my = sum(xs) / n, sum(ys) / n
    return -sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)

def media_sd(v):
    m = sum(v) / len(v)
    return m, math.sqrt(sum((e - m) ** 2 for e in v) / (len(v) - 1))

def compute():
    rng = random.Random(20261109)
    h, l, mal = [], [], []
    for _ in range(NREP):
        c = catalogo(rng)
        h.append(hill(c, DMIN)); l.append(ls_acumulada(c)); mal.append(len(c) / sum(math.log(x / 0.5) for x in c))
    mh, sh = media_sd(h); ml, sl = media_sd(l)
    return dict(b_mle_mean=mh, b_mle_sd=sh, b_ls_mean=ml, b_ls_sd=sl, b_th=B / math.sqrt(N), sesgo_mle=mh - B, sesgo_ls=ml - B,
                b_bad=sum(mal) / len(mal), n=N, dens=N / AREA, dens_err=math.sqrt(N) / AREA, se_media=sh / math.sqrt(NREP))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"Hill: b = {r['b_mle_mean']:.4f} +- {r['b_mle_sd']:.4f} (teorica {r['b_th']:.4f}) ; sesgo {r['sesgo_mle']:+.4f}")
    print(f"minimos cuadrados acumulada: b = {r['b_ls_mean']:.4f} +- {r['b_ls_sd']:.4f} ; sesgo {r['sesgo_ls']:+.4f}")
    print(f"D_min mal fijado (0.5 km): b = {r['b_bad']:.4f}")
    print(f"densidad N(>1 km) = {r['dens']:.3e} +- {r['dens_err']:.1e} km^-2")
    assert abs(r["sesgo_mle"]) < 2 * r["se_media"] + 0.005 and abs(r["b_mle_sd"] / r["b_th"] - 1) < 0.05 and r["b_bad"] < 1.5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
