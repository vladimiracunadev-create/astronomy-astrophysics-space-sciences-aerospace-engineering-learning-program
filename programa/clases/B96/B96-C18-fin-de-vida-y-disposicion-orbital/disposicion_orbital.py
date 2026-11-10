"""B96-C18: fin de vida SINTETICO: delta-v de retiro y decaimiento por arrastre con atmosfera exponencial ficticia."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: atmosfera exponencial ficticia (rho = 3.0e-12 kg/m3 a 400 km, H = 60 km); satelite de 50 kg, Cd = 2.2, A = 0.1 m2")
MU = 398600.4418; RE = 6378.137      # km3/s2, km
# --- delta-v de retiro: bajar el perigeo desde orbita circular de 550 km
h0 = 550.0; a0 = RE + h0
vc = math.sqrt(MU/a0)
for hp in (400.0, 300.0, 200.0, 100.0):
    at = (a0 + RE + hp)/2
    va = math.sqrt(MU*(2/a0 - 1/at))
    print(f"Perigeo {hp:5.0f} km: delta-v = {(vc - va)*1000:7.2f} m/s")
# comprobacion por energia: v^2/2 - mu/r conservada en la elipse
hp = 100.0; at = (a0 + RE + hp)/2; va = math.sqrt(MU*(2/a0 - 1/at))
E1 = va*va/2 - MU/a0; E2 = -MU/(2*at)
print(f"Energia especifica: vis-viva = {E1:.6f} ; -mu/2a = {E2:.6f} km2/s2")
assert abs(E1 - E2) < 1e-9
# --- decaimiento por arrastre de una orbita circular
rho0, H, hbase = 3.0e-12, 60.0, 400.0
B = 50.0/(2.2*0.1)                         # kg/m2
def rho(h): return rho0*math.exp(-(h - hbase)/H)
def dadt(a):                               # km/s ; da/dt = -rho a v / B
    h = a - RE
    am = a*1000.0; v = math.sqrt(MU*1e9/am)
    return -rho(h)*am*v/B/1000.0
def decae(h_ini, dt, h_fin=150.0, tmax=500*365.25*86400):
    a = RE + h_ini; t = 0.0
    while a - RE > h_fin and t < tmax:
        k1 = dadt(a); k2 = dadt(a + 0.5*dt*k1); k3 = dadt(a + 0.5*dt*k2); k4 = dadt(a + dt*k3)
        a += dt*(k1 + 2*k2 + 2*k3 + k4)/6; t += dt
    return t/(365.25*86400)
print("h0 [km]  vida RK4 dt=1 d [anios]  RK4 dt=0.5 d  aproximacion B H/(rho a v)  [anios]")
res = {}
for h in (400.0, 450.0, 500.0, 550.0):
    t1 = decae(h, 86400.0); t2 = decae(h, 43200.0)
    a = (RE + h)*1000; v = math.sqrt(MU*1e9/a)
    ap = B*H*1000/(rho(h)*a*v)/(365.25*86400)
    res[h] = (t1, t2, ap)
    print(f"{h:7.0f} {t1:20.3f} {t2:14.3f} {ap:26.3f}")
    assert abs(t1 - t2)/t2 < 0.01
    assert abs(ap - t2)/t2 < 0.25
assert res[400.0][0] < res[450.0][0] < res[500.0][0] < res[550.0][0]
crit = 25.0
print(f"Vida natural desde 550 km = {res[550.0][1]:.1f} anios ; supera {crit} anios: {'SI' if res[550.0][1] > crit else 'NO'} (umbral usado solo como referencia de lectura)")
print("Pruebas superadas.")
