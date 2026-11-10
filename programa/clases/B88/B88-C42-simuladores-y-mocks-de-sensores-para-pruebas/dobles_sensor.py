"""B88-C42: dobles de sensor con ruido, sesgo, cuantizacion y fallos; varianza de Allan (SINTETICO, semilla 42)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: un sensor de velocidad angular inventado (rad/s)")

class Sensor:
    def __init__(self, sesgo=0.0, ruido=0.01, lsb=0.001, semilla=1):
        self.sesgo = sesgo; self.ruido = ruido; self.lsb = lsb; self.r = random.Random(semilla); self.modo = "ok"; self.ult = 0.0
    def leer(self, verdad):
        if self.modo == "atascado": return self.ult
        if self.modo == "perdida": return None
        v = verdad + self.sesgo + self.r.gauss(0, self.ruido)
        v = round(v / self.lsb) * self.lsb
        self.ult = v; return v
# 1. Propiedades estadisticas
s = Sensor(sesgo=0.005, ruido=0.01, lsb=0.001)
x = [s.leer(0.0) for _ in range(20000)]
m = sum(x) / len(x); sd = math.sqrt(sum((v - m) ** 2 for v in x) / (len(x) - 1))
print(f"Media medida = {m:.5f} (sesgo programado 0.005) ; desviacion = {sd:.5f} (ruido 0.01 + cuantizacion)")
print(f"Desviacion esperada = {math.sqrt(0.01**2 + 0.001**2/12):.5f}")
# 2. Detector de atascado (FDIR): n lecturas identicas
def detector(sensor, verdad, n_ident=5, N=60, t_falla=30):
    hist = []; det = None
    for k in range(N):
        if k == t_falla: sensor.modo = "atascado"
        v = sensor.leer(verdad(k)); hist.append(v)
        if det is None and len(hist) >= n_ident and len(set(hist[-n_ident:])) == 1: det = k
    return det
det = [detector(Sensor(ruido=0.01, lsb=0.001, semilla=i), lambda k: 0.1 * math.sin(0.2 * k)) for i in range(200)]
falsos = sum(1 for d in det if d is not None and d < 30)
lat = [d - 30 for d in det if d is not None and d >= 30]
print(f"Detector de atascado (5 lecturas identicas): detectado en {len(lat)}/200 ; falsas alarmas antes de la falla = {falsos} ; latencia media = {sum(lat)/len(lat):.2f} muestras")
# 3. Dropout
sp = Sensor(); sp.modo = "perdida"
print("Lectura con perdida de dato:", sp.leer(1.0))
# 4. Varianza de Allan de ruido blanco: sigma_A(tau) ~ sigma / sqrt(tau/dt)
random.seed(42)
dt = 0.1; N = 100000
w = [random.gauss(0, 0.01) for _ in range(N)]
def allan(w, m):
    k = len(w) // m
    med = [sum(w[i * m:(i + 1) * m]) / m for i in range(k)]
    return math.sqrt(0.5 * sum((med[i + 1] - med[i]) ** 2 for i in range(k - 1)) / (k - 1))
print("tau [s]   desv. de Allan   teorico 0.01/sqrt(m)")
for m_ in (1, 10, 100, 1000):
    a = allan(w, m_); t = 0.01 / math.sqrt(m_)
    print(f"{m_*dt:7.1f}   {a:14.6f}   {t:14.6f}")
    assert abs(a - t) / t < 0.1
print("Pruebas superadas.")
