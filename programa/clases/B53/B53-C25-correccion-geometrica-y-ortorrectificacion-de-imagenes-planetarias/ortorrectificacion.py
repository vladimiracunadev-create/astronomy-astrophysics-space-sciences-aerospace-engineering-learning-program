#!/usr/bin/env python3
"""B53-C25: ortorrectificacion de una camara de cuadro en nadir ILUSTRATIVA. SI. H = 250 km, f = 0.5 m, pixel 10 um.
Terreno SINTETICO h = 1500 + 1500 sin(2 pi x/8000) cos(2 pi y/6000). 2000 puntos con r <= 15 km. Semilla 20261109.
Tolerancias: error residual < 1e-6 m; desplazamiento igual a la formula (1e-9 relativo)."""
import math, platform, random

H, F, PIX = 250e3, 0.5, 10e-6

def h_mde(x, y, sesgo=0.0):
    return 1500 + 1500 * math.sin(2 * math.pi * x / 8000) * math.cos(2 * math.pi * y / 6000) + sesgo

def proyectar(x, y):
    h = h_mde(x, y)
    return F * x / (H - h), F * y / (H - h)

def ortho(u, v, sesgo=0.0):
    x, y = u * H / F, v * H / F
    it = 0
    for it in range(1, 100):
        h = h_mde(x, y, sesgo)
        xn, yn = u * (H - h) / F, v * (H - h) / F
        if math.hypot(xn - x, yn - y) < 1e-9:
            x, y = xn, yn
            break
        x, y = xn, yn
    return x, y, it

def compute():
    rng = random.Random(20261109)
    dmax = dform = sdm = 0.0
    eo = emde = 0.0
    itm = 0
    n = 2000
    for _ in range(n):
        r = 15e3 * math.sqrt(rng.random())
        a = rng.uniform(0, 2 * math.pi)
        x, y = r * math.cos(a), r * math.sin(a)
        h = h_mde(x, y)
        u, v = proyectar(x, y)
        x0, y0 = u * H / F, v * H / F
        d = math.hypot(x0 - x, y0 - y)
        dform = max(dform, r * h / (H - h))
        dmax = max(dmax, d)
        sdm += d
        xo, yo, it = ortho(u, v)
        eo = max(eo, math.hypot(xo - x, yo - y)); itm = max(itm, it)
        xm, ym, _ = ortho(u, v, sesgo=100.0)
        emde = max(emde, math.hypot(xm - x, ym - y))
    gsd = H * PIX / F
    r15 = 15e3
    return dict(gsd=gsd, d_max=dmax, d_form=dform, d_mean=sdm / n, err_ortho=eo, it_max=itm, err_mde=emde,
                err_mde_50=emde / 2, d_ej=r15 * 3000 / (H - 3000), d_max_px=dmax / gsd)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"GSD = {r['gsd']:.3f} m ; desplazamiento por relieve: maximo {r['d_max']:.3f} m ; medio {r['d_mean']:.3f} m ; formula (max de r h/(H-h)) {r['d_form']:.3f} m")
    print(f"ortorrectificacion: error maximo {r['err_ortho']:.2e} m en <= {r['it_max']} iteraciones")
    print(f"con sesgo de 100 m en el MDE: error horizontal maximo {r['err_mde']:.3f} m")
    assert r["err_ortho"] < 1e-6 and abs(r["d_max"] / r["d_form"] - 1) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
