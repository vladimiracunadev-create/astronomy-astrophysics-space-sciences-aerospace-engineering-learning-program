#!/usr/bin/env python3
"""B53-C06: geodesia sobre un ELIPSOIDE ILUSTRATIVO (a = 3396.2 km, f = 1/170; no consultados).
Longitud este positiva. Tolerancias: Delta_max 1e-6 grados; altura 1e-9 km."""
import math, platform

A = 3396.2
F = 1 / 170
C = A * (1 - F)
E2 = 1 - (C / A) ** 2

def gc_a_gg(lat):
    return math.degrees(math.atan((A / C) ** 2 * math.tan(math.radians(lat))))

def xyz(lat_g, lon, h):
    p = math.radians(lat_g)
    n = A / math.sqrt(1 - E2 * math.sin(p) ** 2)
    return ((n + h) * math.cos(p) * math.cos(math.radians(lon)), (n + h) * math.cos(p) * math.sin(math.radians(lon)), (n * (1 - E2) + h) * math.sin(p))

def lat_h(x, y, z):
    pp = math.hypot(x, y)
    p = math.atan2(z, pp * (1 - E2))
    for _ in range(100):
        n = A / math.sqrt(1 - E2 * math.sin(p) ** 2)
        h = pp / math.cos(p) - n
        pn = math.atan2(z, pp * (1 - E2 * n / (n + h)))
        if abs(pn - p) < 1e-12:
            p = pn
            break
        p = pn
    n = A / math.sqrt(1 - E2 * math.sin(p) ** 2)
    return math.degrees(p), pp / math.cos(p) - n

def compute():
    best, arg = 0.0, 0.0
    for i in range(1, 90000):
        lat = i * 0.001
        d = gc_a_gg(lat) - lat
        if d > best:
            best, arg = d, lat
    dana = math.degrees(math.asin((A * A - C * C) / (A * A + C * C)))
    v = xyz(30.0, 77.0, 100.0)
    lat, h = lat_h(*v)
    d45 = gc_a_gg(45.0) - 45.0
    return dict(c=C, dmax_num=best, dmax_ana=dana, lat_max=arg, h_rec=h, h_err=abs(h - 100.0), lat_err=abs(lat - 30.0),
                d45=d45, d45_km=math.radians(d45) * A, ac2=(A / C) ** 2, lon_este=360 - 250)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"c = {r['c']:.4f} km ; (a/c)^2 = {r['ac2']:.7f}")
    print(f"diferencia maxima de latitudes: barrido {r['dmax_num']:.6f} grados en {r['lat_max']:.3f} ; formula {r['dmax_ana']:.6f} grados")
    print(f"a 45 grados: diferencia {r['d45']:.6f} grados = {r['d45_km']:.3f} km")
    print(f"altura recuperada = {r['h_rec']:.10f} km (error {r['h_err']:.2e}) ; error de latitud {r['lat_err']:.2e} grados")
    print(f"longitud oeste 250 -> este {r['lon_este']}")
    assert abs(r["dmax_num"] - r["dmax_ana"]) < 1e-6 and r["h_err"] < 1e-9 and r["lon_este"] == 110
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
