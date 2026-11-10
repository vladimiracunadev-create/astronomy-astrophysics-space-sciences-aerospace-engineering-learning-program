"""B88-C44: pronostico de salud: degradacion exponencial, vida util restante e intervalo por remuestreo (SINTETICO, semilla 44)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: par de friccion de una rueda de reaccion inventado (mN m), NO telemetria real")

random.seed(44)
a_real, b_real = 2.0, 0.0006      # f(t) = a exp(b t), t en horas
umbral = 60.0
dias = 150
t_obs = [24.0 * d for d in range(0, dias, 2)]
y = [a_real * math.exp(b_real * t) * (1 + random.gauss(0, 0.03)) for t in t_obs]
def ajuste(ts, ys):
    ly = [math.log(v) for v in ys]
    n = len(ts); mx = sum(ts) / n; my = sum(ly) / n
    b = sum((x - mx) * (v - my) for x, v in zip(ts, ly)) / sum((x - mx) ** 2 for x in ts)
    a = math.exp(my - b * mx); return a, b
a, b = ajuste(t_obs, y)
t_cruce = math.log(umbral / a) / b
t_ahora = t_obs[-1]
print(f"Observaciones: {len(t_obs)} en {dias} dias ; ultimo valor = {y[-1]:.3f} mN m")
print(f"Ajuste: a = {a:.4f} (real {a_real}) ; b = {b:.6f} /h (real {b_real})")
rul = t_cruce - t_ahora
rul_real = math.log(umbral / a_real) / b_real - t_ahora
print(f"Cruce del umbral {umbral} en t = {t_cruce:.0f} h ; vida util restante = {rul:.0f} h = {rul/24:.1f} dias (real {rul_real/24:.1f} dias)")
# Remuestreo de residuos
res = [math.log(v) - (math.log(a) + b * t) for v, t in zip(y, t_obs)]
ruls = []
for _ in range(2000):
    ys = [a * math.exp(b * t + random.choice(res)) for t in t_obs]
    a2, b2 = ajuste(t_obs, ys)
    ruls.append((math.log(umbral / a2) / b2 - t_ahora) / 24)
ruls.sort()
lo, hi = ruls[int(0.025 * 2000)], ruls[int(0.975 * 2000)]
print(f"Intervalo de remuestreo 95 % de la vida restante: [{lo:.1f}, {hi:.1f}] dias ; ancho = {hi-lo:.1f}")
print(f"El valor real ({rul_real/24:.1f} dias) cae dentro: {lo <= rul_real/24 <= hi}")
# Efecto de menos datos
for n in (15, 30, 75):
    ts = t_obs[:n]; ys = y[:n]
    a3, b3 = ajuste(ts, ys)
    r = (math.log(umbral / a3) / b3 - ts[-1]) / 24
    print(f"Con los primeros {n:3d} puntos ({ts[-1]/24:5.0f} dias): vida util estimada = {r:7.1f} dias")
# Decision: alerta si el limite inferior < horizonte
horiz = 100
print(f"Politica: alertar si el limite inferior < {horiz} dias -> {'ALERTAR' if lo < horiz else 'sin alerta'} (limite inferior = {lo:.1f})")
assert lo <= rul_real / 24 <= hi
print("Pruebas superadas.")
