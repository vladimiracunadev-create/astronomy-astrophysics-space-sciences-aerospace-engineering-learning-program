#!/usr/bin/env python3
"""B53-C03: campo gravitatorio SINTETICO (masa central + anillo ecuatorial). Adimensional: G*M0 = 1, a = 1.
Marco principal del cuerpo, z por el eje. Suma directa con 720 masas. Tolerancia: pendiente en [-4.5, -3.5]."""
import math, platform

N = 720
MU = 0.02  # m / M0

def v_directo(r, lat):
    x, z = r * math.cos(lat), r * math.sin(lat)
    v = -1.0 / r
    for k in range(N):
        t = 2 * math.pi * k / N
        d = math.sqrt((x - math.cos(t)) ** 2 + (0 - math.sin(t)) ** 2 + z * z)
        v += -MU / N / d
    return v

def v_serie(r, lat):
    m_tot = 1.0 + MU
    j2 = MU / (2 * m_tot)
    p2 = (3 * math.sin(lat) ** 2 - 1) / 2
    return -m_tot / r * (1 - j2 / r ** 2 * p2)

def compute():
    rs = [2, 3, 5, 10]
    R = {"J2": MU / (2 * (1 + MU))}
    xs, ys = [], []
    for r in rs:
        vd, vs = v_directo(r, 0.0), v_serie(r, 0.0)
        e = abs(vs - vd) / abs(vd)
        R[f"V{r}"], R[f"e{r}"] = vd, e
        xs.append(math.log(r)); ys.append(math.log(e))
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n
    R["pend"] = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    R["dV"] = v_directo(3, 0.0) - v_directo(3, math.pi / 2)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"J2 = m/(2M) = {R['J2']:.6f}")
    for r in (2, 3, 5, 10):
        print(f"r = {r:2d} a: V directo = {R['V%d' % r]:.8f} ; error relativo de la serie con J2 = {R['e%d' % r]:.3e}")
    print(f"pendiente de log(error) frente a log(r/a) = {R['pend']:.3f}")
    print(f"V(ecuador) - V(polo) a r=3a = {R['dV']:.4e} (GM0/a)")
    assert -4.5 < R["pend"] < -3.5 and R["dV"] < 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
