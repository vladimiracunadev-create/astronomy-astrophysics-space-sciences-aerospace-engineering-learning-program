"""B96-C06: telemetria operativa SINTETICA: cuentas -> unidades, limites con histeresis."""
import sys, random
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: sensor de temperatura ficticio de 12 bit; semilla 96")
# calibracion polinomica T = a0 + a1*x + a2*x^2 (x = cuentas de 12 bit)
a0, a1, a2 = -50.0, 0.0488, 1.5e-7
def cal(x): return a0 + a1*x + a2*x*x
for x in (0, 1024, 2048, 3072, 4095):
    print(f"cuentas {x:5d} -> {cal(x):8.3f} grados C")
lsb = cal(1) - cal(0)
print(f"Resolucion (1 cuenta) = {lsb:.4f} grados C ; rango = {cal(0):.1f} a {cal(4095):.1f} grados C")
assert all(cal(x+1) > cal(x) for x in range(4095))
random.seed(96)
def inv(T):
    lo, hi = 0.0, 4095.0
    for _ in range(60):
        m = (lo+hi)/2
        if cal(m) < T: lo = m
        else: hi = m
    return round((lo+hi)/2)
n = 600
def base(k): return 20.0 + 18.0*max(0.0, 1 - abs(k-300)/120)
serie = [inv(base(k) + random.gauss(0, 0.4)) for k in range(n)]
T = [cal(x) for x in serie]
def vigilar(T, ama=30.0, rojo=36.0, hist=1.0):
    est = "OK"; out = []; cambios = 0
    for t in T:
        nuevo = est
        if est == "OK" and t >= ama: nuevo = "AMARILLO"
        if est in ("OK", "AMARILLO") and t >= rojo: nuevo = "ROJO"
        if est == "ROJO" and t < rojo - hist: nuevo = "AMARILLO"
        if nuevo == "AMARILLO" and t < ama - hist: nuevo = "OK"
        if nuevo != est: cambios += 1
        est = nuevo; out.append(est)
    return out, cambios
con, c1 = vigilar(T)
sin, c0 = vigilar(T, hist=0.0)
print(f"Muestras = {n} ; max = {max(T):.2f} C ; min = {min(T):.2f} C")
print(f"Cambios de estado con histeresis 1.0 C = {c1} ; sin histeresis = {c0}")
print(f"Muestras con histeresis: ROJO = {con.count('ROJO')} ; AMARILLO = {con.count('AMARILLO')} ; OK = {con.count('OK')}")
assert max(T) > 36.0 and c1 <= c0 and c1 >= 4
Tl = [cal(inv(base(k))) for k in range(n)]
l, cl = vigilar(Tl)
print(f"Serie sin ruido: cambios = {cl} (OK->AMARILLO->ROJO->AMARILLO->OK = 4)")
assert cl == 4
print("Pruebas superadas.")
