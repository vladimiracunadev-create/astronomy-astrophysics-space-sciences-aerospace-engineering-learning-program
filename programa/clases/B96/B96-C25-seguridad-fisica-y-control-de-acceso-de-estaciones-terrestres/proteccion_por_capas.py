"""B96-C25: proteccion fisica por capas de una estacion terrestre SINTETICA (analisis DEFENSIVO): probabilidad de interrupcion y margen de tiempo."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: capas, probabilidades y tiempos de retardo ficticios; analisis defensivo abstracto; semilla 96")
# capas desde el exterior: (nombre, prob. de deteccion, retardo s)
capas = [("Cerco perimetral con sensores", 0.80, 30), ("Control de acceso del recinto", 0.90, 20), ("Camaras con analisis", 0.70, 10),
         ("Puerta de la sala de equipos", 0.85, 60), ("Rack cerrado con alarma", 0.95, 90)]
T_RESP = 180.0     # s hasta la llegada de la respuesta, medido desde la primera deteccion fiable (sintetico)
def p_interrupcion(capas, t_resp):
    """Exito defensivo si la primera deteccion ocurre en una capa tal que el retardo restante (incluida la capa) >= t_resp."""
    n = len(capas); p_no_det = 1.0; p = 0.0
    restante = [sum(c[2] for c in capas[i:]) for i in range(n)]   # retardo desde la capa i hasta el final
    for i, (_, pd, d) in enumerate(capas):
        # se detecta por primera vez en la capa i
        if restante[i] >= t_resp: p += p_no_det*pd
        p_no_det *= (1 - pd)
    return p
P_total_det = 1.0
for _, pd, _ in capas: P_total_det *= (1 - pd)
P_total_det = 1 - P_total_det
P_int = p_interrupcion(capas, T_RESP)
print(f"Retardo total = {sum(c[2] for c in capas)} s ; respuesta = {T_RESP:.0f} s")
print(f"Probabilidad de detectar en alguna capa = {P_total_det:.6f}")
print(f"Probabilidad de interrupcion a tiempo = {P_int:.6f}")
for i in range(len(capas)):
    print(f"  retardo restante desde '{capas[i][0]}' = {sum(c[2] for c in capas[i:])} s")
# comprobacion por Monte Carlo
rng = random.Random(96); M = 400000; ok = 0
for _ in range(M):
    for i, (_, pd, d) in enumerate(capas):
        if rng.random() < pd:
            if sum(c[2] for c in capas[i:]) >= T_RESP: ok += 1
            break
esp = P_int*M
print(f"Monte Carlo ({M}): interrupcion = {ok/M:.6f} ; analitica = {P_int:.6f}")
assert abs(ok - esp) < 4*(esp*(1 - P_int))**0.5 + 1
# sensibilidad: reducir el tiempo de respuesta y agregar una capa
for tr in (300.0, 240.0, 180.0, 120.0, 60.0):
    print(f"  respuesta {tr:5.0f} s -> P(interrupcion) = {p_interrupcion(capas, tr):.6f}")
capas2 = capas + [("Guardia en sitio (detecta y retrasa)", 0.60, 45)]
print(f"Con una capa adicional: P(interrupcion) = {p_interrupcion(capas2, T_RESP):.6f}")
assert p_interrupcion(capas, 60.0) >= p_interrupcion(capas, 300.0)
assert P_int <= P_total_det
print("Pruebas superadas.")
