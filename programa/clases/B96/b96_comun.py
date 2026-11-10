"""Utilidad comun SINTETICA: orbita circular kepleriana, Tierra esferica que rota; ECI -> ECEF; elevacion."""
import math
MU = 398600.4418; RE = 6378.137; WE = 7.2921159e-5   # km3/s2, km, rad/s
def sat_eci(t, h, inc_deg, raan_deg=0.0, u0_deg=0.0):
    a = RE + h; n = math.sqrt(MU/a**3)
    u = math.radians(u0_deg) + n*t; i = math.radians(inc_deg); O = math.radians(raan_deg)
    x = a*(math.cos(O)*math.cos(u) - math.sin(O)*math.sin(u)*math.cos(i))
    y = a*(math.sin(O)*math.cos(u) + math.cos(O)*math.sin(u)*math.cos(i))
    z = a*math.sin(u)*math.sin(i)
    return (x, y, z)
def eci_to_ecef(p, t):
    th = WE*t; c, s = math.cos(th), math.sin(th)
    return (c*p[0] + s*p[1], -s*p[0] + c*p[1], p[2])
def estacion(lat_deg, lon_deg):
    la, lo = math.radians(lat_deg), math.radians(lon_deg)
    return (RE*math.cos(la)*math.cos(lo), RE*math.cos(la)*math.sin(lo), RE*math.sin(la))
def az_el_rng(sat, st, lat_deg, lon_deg):
    la, lo = math.radians(lat_deg), math.radians(lon_deg)
    d = [sat[k]-st[k] for k in range(3)]
    e = (-math.sin(lo), math.cos(lo), 0.0)
    nn = (-math.sin(la)*math.cos(lo), -math.sin(la)*math.sin(lo), math.cos(la))
    u = (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))
    E_ = sum(d[k]*e[k] for k in range(3)); N_ = sum(d[k]*nn[k] for k in range(3)); U_ = sum(d[k]*u[k] for k in range(3))
    r = math.sqrt(E_**2 + N_**2 + U_**2)
    return math.degrees(math.atan2(E_, N_)) % 360.0, math.degrees(math.asin(U_/r)), r
def pasadas(h, inc, lat, lon, el_min, dt=5.0, T=86400.0, raan=0.0, u0=0.0):
    st = estacion(lat, lon); out = []; dentro = False
    t = 0.0
    while t <= T:
        az, el, r = az_el_rng(eci_to_ecef(sat_eci(t, h, inc, raan, u0), t), st, lat, lon)
        if el >= el_min and not dentro:
            dentro = True; ini = t; elmax = el
        if dentro:
            elmax = max(elmax, el)
        if el < el_min and dentro:
            dentro = False; out.append((ini, t, elmax))
        t += dt
    if dentro: out.append((ini, T, elmax))
    return out
