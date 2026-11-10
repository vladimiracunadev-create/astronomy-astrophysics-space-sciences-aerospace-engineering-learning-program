"""B96-C28: control y seguimiento de antena SINTETICO: velocidades az/el, paso por el cenit y perdida por error de apuntamiento."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: orbita circular de 550 km, Tierra esferica sin rotacion, estacion en (R, 0, 0); antena con haz de 4 grados y limite de 3 grados/s")
MU = 398600.4418; RE = 6378.137
h = 550.0; a = RE + h; n = math.sqrt(MU/a**3)       # rad/s
HAZ = 4.0; LIM = 3.0; LAT = 0.5                      # grados, grados/s, s de latencia de seguimiento
def az_el(theta, delta):
    A = (math.cos(delta), math.sin(delta), 0.0); B = (0.0, 0.0, 1.0)
    s = [a*(A[i]*math.cos(theta) + B[i]*math.sin(theta)) for i in range(3)]
    d = (s[0] - RE, s[1], s[2])
    E, N, U = d[1], d[2], d[0]
    r = math.sqrt(E*E + N*N + U*U)
    return math.degrees(math.atan2(E, N)), math.degrees(math.asin(U/r)), r
def pasada(delta_deg, dt=0.25, el_min=10.0):
    delta = math.radians(delta_deg); th = -0.5; out = []
    t = 0.0
    while th <= 0.5:
        th = -0.5 + n*t
        az, el, r = az_el(th, delta)
        out.append((t, az, el)); t += dt
    out = [p for p in out if p[2] >= el_min]
    return out
def tasas(p):
    azr = []; elr = []
    for i in range(1, len(p) - 1):
        d_az = p[i+1][1] - p[i-1][1]
        d_az = (d_az + 180.0) % 360.0 - 180.0
        dt = p[i+1][0] - p[i-1][0]
        azr.append(abs(d_az/dt)); elr.append(abs((p[i+1][2] - p[i-1][2])/dt))
    return max(azr), max(elr)
print("delta[gr] el_max[gr] az_rate_max[gr/s] el_rate_max[gr/s] error_lag[gr] perdida[dB] veredicto")
res = []
for dd in (0.2, 1.0, 3.0, 8.0, 12.0):
    p = pasada(dd)
    elm = max(q[2] for q in p)
    azmax, elmax_r = tasas(p)
    err = max(azmax, elmax_r)*LAT
    loss = 12*(err/HAZ)**2
    ok = azmax <= LIM and loss < 1.0
    res.append((dd, elm, azmax, elmax_r, err, loss, ok))
    print(f"{dd:8.1f} {elm:10.2f} {azmax:17.2f} {elmax_r:17.2f} {err:13.2f} {loss:11.3f} {'SIGUE' if ok else 'NO SIGUE'}")
    # comprobacion analitica de la elevacion maxima: tan(el) = (cos d - RE/a)/sin d
    d = math.radians(dd)
    el_a = math.degrees(math.atan2(math.cos(d) - RE/a, math.sin(d)))
    assert abs(elm - el_a) < 0.2, (elm, el_a)
# el azimut maximo crece al acercarse al cenit
assert res[0][2] > res[1][2] > res[2][2] > res[3][2] > res[4][2]
# la pasada casi cenital supera el limite de velocidad
assert not res[0][6] and res[3][6]
# comprobacion de la derivada con paso fino
p2 = pasada(3.0, dt=0.05); a1, e1 = tasas(pasada(3.0, dt=0.25)); a2, e2 = tasas(p2)
print(f"Control del paso: az_rate dt=0.25 s = {a1:.3f} ; dt=0.05 s = {a2:.3f} grados/s")
assert abs(a1 - a2)/a2 < 0.03
print(f"Velocidad angular orbital n = {math.degrees(n):.4f} grados/s")
print("Pruebas superadas.")
