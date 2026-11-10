"""B96-C15: emergencia SINTETICA: tiempo hasta el limite critico frente al tiempo de respuesta tras perder el contacto."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: bateria, cargas y tiempos de respuesta ficticios")
CAP = 40.0             # Wh
SOC0 = 0.80            # estado de carga al perder el contacto
SOC_MIN = 0.20         # limite critico (sintetico)
P_load = 12.0          # W en modo seguro
def t_critico(gen_media):
    neto = P_load - gen_media          # W de descarga neta
    if neto <= 0: return float("inf")
    return (SOC0 - SOC_MIN)*CAP/neto   # horas
print("Generacion media [W]  tiempo hasta SOC critico [h]")
casos = [0.0, 3.0, 6.0, 9.0, 11.0]
for g in casos:
    t = t_critico(g)
    print(f"{g:19.1f} {t:28.2f}")
# comprobacion numerica por integracion con paso de 1 s
def integra(gen_media, dt=1.0):
    soc = SOC0*CAP; t = 0.0
    while soc > SOC_MIN*CAP and t < 1e6:
        soc -= (P_load - gen_media)*dt/3600; t += dt
    return t/3600
for g in (0.0, 6.0):
    a = t_critico(g); b = integra(g)
    print(f"  g = {g:3.1f} W: analitico = {a:.4f} h ; integrado = {b:.4f} h ; dif = {abs(a-b):.2e} h")
    assert abs(a - b) < 1e-3
# cadena de respuesta tras perdida de contacto
detect = 1.5      # h hasta confirmar la perdida (varias pasadas sin senal)
decide = 0.5      # h para decidir y preparar el procedimiento
prep_est = 1.0    # h hasta la siguiente pasada util con otra estacion
resp = detect + decide + prep_est
print(f"Tiempo de respuesta = {detect} + {decide} + {prep_est} = {resp:.2f} h")
print("Generacion  t_critico  margen [h]  veredicto")
res = {}
for g in casos:
    t = t_critico(g); m = t - resp; res[g] = m
    print(f"{g:10.1f} {t:10.2f} {m:11.2f}  {'cabe' if m >= 0 else 'NO cabe'}")
assert res[0.0] < 0 and res[9.0] > 0
# generacion minima para que el tiempo de respuesta quepa
gmin = P_load - (SOC0 - SOC_MIN)*CAP/resp
print(f"Generacion media minima para que la respuesta quepa = {gmin:.2f} W")
assert abs(t_critico(gmin) - resp) < 1e-9
# reduccion de carga: apagar cargas no esenciales
for pl in (12.0, 8.0, 6.0):
    P_load_bak = P_load
    P_load = pl
    print(f"  carga {pl:4.1f} W, sin generacion: t_critico = {t_critico(0.0):.2f} h")
    P_load = P_load_bak
print("Pruebas superadas.")
