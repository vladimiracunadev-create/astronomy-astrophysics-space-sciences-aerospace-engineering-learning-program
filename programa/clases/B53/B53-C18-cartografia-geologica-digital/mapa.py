#!/usr/bin/env python3
"""B53-C18: areas en proyecciones sobre una esfera SINTETICA (R = 1000 km). Region lat 60-70, lon 0-10 grados.
Tolerancia: proyecciones equivalentes dentro de 1e-5 relativo."""
import math, platform

R = 1000.0
LAT1, LAT2, LON1, LON2 = 60.0, 70.0, 0.0, 10.0

def borde(n=400):
    pts = []
    for i in range(n): pts.append((LAT1, LON1 + (LON2 - LON1) * i / n))
    for i in range(n): pts.append((LAT1 + (LAT2 - LAT1) * i / n, LON2))
    for i in range(n): pts.append((LAT2, LON2 - (LON2 - LON1) * i / n))
    for i in range(n): pts.append((LAT2 - (LAT2 - LAT1) * i / n, LON1))
    return pts

def lazada(xy):
    s = 0.0
    for (x1, y1), (x2, y2) in zip(xy, xy[1:] + xy[:1]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2

def sinusoidal(p, l):
    p, l = math.radians(p), math.radians(l)
    return R * l * math.cos(p), R * p

def lambert(p, l, p0=65.0, l0=5.0):
    p, l, p0, l0 = map(math.radians, (p, l, p0, l0))
    k = math.sqrt(2 / (1 + math.sin(p0) * math.sin(p) + math.cos(p0) * math.cos(p) * math.cos(l - l0)))
    return R * k * math.cos(p) * math.sin(l - l0), R * k * (math.cos(p0) * math.sin(p) - math.sin(p0) * math.cos(p) * math.cos(l - l0))

def equirect(p, l):
    return R * math.radians(l) * math.cos(math.radians(65.0)), R * math.radians(p)

def cubrir(unidades, paso=0.1):
    gap = ov = 0
    for i in range(100):
        for j in range(100):
            lat, lon = LAT1 + (i + 0.5) * paso, LON1 + (j + 0.5) * paso
            n = sum(1 for (a, b) in unidades if a <= lon < b)
            gap += n == 0; ov += n > 1
    return gap, ov

def compute():
    ex = R * R * math.radians(LON2 - LON1) * (math.sin(math.radians(LAT2)) - math.sin(math.radians(LAT1)))
    b = borde()
    si = lazada([sinusoidal(p, l) for p, l in b])
    la = lazada([lambert(p, l) for p, l in b])
    pc = lazada([equirect(p, l) for p, l in b])
    pc_naive = R * R * math.radians(LON2 - LON1) * math.radians(LAT2 - LAT1)
    g0, o0 = cubrir([(0.0, 5.0), (5.0, 10.0)])
    g1, o1 = cubrir([(0.0, 5.0), (5.1, 10.0)])
    g2, o2 = cubrir([(0.0, 5.1), (5.0, 10.0)])
    return dict(A_ex=ex, A_si=si, A_la=la, A_pc=pc_naive, err_si=(si - ex) / ex, err_la=(la - ex) / ex,
                err_pc=100 * (pc_naive - ex) / ex, gap0=g0, ov0=o0, gap=g1, ov1=o1, gap2=g2, ov=o2)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"area exacta = {r['A_ex']:.3f} km2")
    print(f"sinusoidal = {r['A_si']:.3f} ({r['err_si']:+.2e}) ; Lambert = {r['A_la']:.3f} ({r['err_la']:+.2e}) ; equirrectangular R^2 dl dphi = {r['A_pc']:.3f} ({r['err_pc']:+.2f} %)")
    print(f"topologia: contiguas -> huecos {r['gap0']}, solapes {r['ov0']} ; con hueco -> huecos {r['gap']}, solapes {r['ov1']} ; con solape -> huecos {r['gap2']}, solapes {r['ov']}")
    assert abs(r["err_si"]) < 1e-5 and abs(r["err_la"]) < 1e-5 and r["gap0"] == 0 and r["ov0"] == 0 and r["gap"] > 0 and r["ov"] > 0 and r["ov1"] == 0 and r["gap2"] == 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
