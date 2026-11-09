#!/usr/bin/env python3
"""B53-C05: coordenadas lunares sobre una ESFERA ilustrativa (R = 1737.4 km, no consultado).
Latitud planetocentrica, longitud este positiva. Desfase de marcos ILUSTRATIVO (0.02, 0.03, 0.01 grados).
Semilla 20261109. Tolerancias: ida y vuelta 1e-9 km; escala de proyeccion 1e-4."""
import math, platform, random

R = 1737.4

def a_xyz(lat, lon):
    p, l = math.radians(lat), math.radians(lon)
    return (R * math.cos(p) * math.cos(l), R * math.cos(p) * math.sin(l), R * math.sin(p))

def a_latlon(v):
    x, y, z = v
    return (math.degrees(math.asin(z / math.sqrt(x * x + y * y + z * z))), math.degrees(math.atan2(y, x)))

def rot(ax, ay, az):
    ax, ay, az = map(math.radians, (ax, ay, az))
    cx, sx, cy, sy, cz, sz = math.cos(ax), math.sin(ax), math.cos(ay), math.sin(ay), math.cos(az), math.sin(az)
    rx = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    ry = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    rz = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]
    mm = lambda a, b: [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return mm(rz, mm(ry, rx))

def apply(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))

def haversine(p, q):
    f1, f2 = math.radians(p[0]), math.radians(q[0])
    dl = math.radians(q[1] - p[1])
    h = math.sin((f2 - f1) / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

def estereo_sur(lat, lon):
    rho = 2 * R * math.tan(math.radians(90 - abs(lat)) / 2)
    l = math.radians(lon)
    return (rho * math.sin(l), rho * math.cos(l))

def compute():
    rng = random.Random(20261109)
    m = rot(0.02, 0.03, 0.01)
    th = math.radians(math.sqrt(0.02 ** 2 + 0.03 ** 2 + 0.01 ** 2))
    rt = nm = dmax = 0.0
    for _ in range(2000):
        lat = math.degrees(math.asin(rng.uniform(-1, 1)))
        lon = rng.uniform(-180, 180)
        v = a_xyz(lat, lon)
        l2 = a_latlon(v)
        dl = (l2[1] - lon + 180) % 360 - 180
        rt = max(rt, abs(l2[0] - lat) * math.pi / 180 * R, abs(dl) * math.pi / 180 * R * math.cos(math.radians(lat)))
        w = apply(m, v)
        nm = max(nm, abs(math.sqrt(sum(c * c for c in w)) - R))
        dmax = max(dmax, math.sqrt(sum((a - b) ** 2 for a, b in zip(v, w))))
    lat0, lon0, dd = -85.0, 40.0, 1e-4
    a = estereo_sur(lat0, lon0)
    b = estereo_sur(lat0, lon0 + dd)
    arco = R * math.cos(math.radians(lat0)) * math.radians(dd)
    k_num = math.dist(a, b) / arco
    k_ana = 2 / (1 + math.sin(math.radians(85)))
    return dict(rt_err=rt, norm_err=nm, disp_max=dmax, disp_bound=R * th,
                d_gc=haversine((-20.0, 10.0), (35.0, 80.0)), k_ana=k_ana, k_num=k_num)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"ida y vuelta lat/lon (2000 puntos): error maximo {r['rt_err']:.2e} km")
    print(f"norma tras rotar: error maximo {r['norm_err']:.2e} km")
    print(f"desplazamiento por el desfase: maximo {r['disp_max']:.5f} km ; cota R*|theta| = {r['disp_bound']:.5f} km")
    print(f"distancia haversine (20S,10E)-(35N,80E): {r['d_gc']:.3f} km")
    print(f"escala de la estereografica a 85S: analitica {r['k_ana']:.6f} ; numerica {r['k_num']:.6f}")
    assert r["rt_err"] < 1e-9 and r["disp_max"] <= r["disp_bound"] * (1 + 1e-9) and abs(r["k_num"] / r["k_ana"] - 1) < 1e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
