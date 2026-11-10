"""B96-C20: simulacion de una jornada de control de mision SINTETICA con eventos discretos."""
import heapq, math, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b96_comun import pasadas
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: satelite de 550 km, estacion 40 N 0 E; telemetria, comandos y anomalia ficticios; semilla 96")
random.seed(96)
ps = pasadas(550.0, 97.6, 40.0, 0.0, 10.0, dt=5.0)
DIA = 86400.0
TM_RATE = 2000.0        # bit/s de generacion continua
DL_RATE = 2.0e6*0.85    # bit/s de bajada util
CMD_T = 12.0            # s por comando (incluye verificacion)
# eventos: (tiempo, orden, tipo, datos)
ev = []
for k, (i, f, em) in enumerate(ps, 1):
    heapq.heappush(ev, (i, 0, "AOS", (k, i, f)))
    heapq.heappush(ev, (f, 9, "LOS", (k, i, f)))
t_anom = random.uniform(2000, 40000)
heapq.heappush(ev, (t_anom, 5, "ANOMALIA", None))
heapq.heappush(ev, (DIA, 10, "FIN", None))
cola_cmd = [f"C{j:02d}" for j in range(1, 13)]      # 12 comandos pendientes
buffer_bits = 0.0; t_ult = 0.0
en_contacto = False; cmds_ok = []; bajado = 0.0; anom_det = None; log = []
t_ant = 0.0
orden_ok = True; t_prev = -1.0
while ev:
    t, _, tipo, d = heapq.heappop(ev)
    if t < t_prev: orden_ok = False
    t_prev = t
    buffer_bits += TM_RATE*(t - t_ant)
    if en_contacto:
        # durante el contacto se baja a DL_RATE hasta vaciar el buffer
        baja = min(buffer_bits, DL_RATE*(t - t_ant)); buffer_bits -= baja; bajado += baja
    t_ant = t
    if tipo == "AOS":
        en_contacto = True; k, i, f = d
        disp = (f - i) - 40.0                        # 20 s de enganche y 20 s de cierre
        n = min(len(cola_cmd), int(disp // CMD_T))
        for _ in range(n): cmds_ok.append((cola_cmd.pop(0), k))
        log.append(f"t={t:8.0f} s AOS pasada {k}: {n} comandos ejecutados ({len(cola_cmd)} pendientes)")
        if t_anom <= t and anom_det is None:
            anom_det = t; log.append(f"t={t:8.0f} s anomalia detectada en la telemetria de la pasada {k}")
    elif tipo == "LOS":
        en_contacto = False; log.append(f"t={t:8.0f} s LOS pasada {d[0]}: buffer pendiente = {buffer_bits/8e6:.3f} MB")
    elif tipo == "ANOMALIA":
        log.append(f"t={t:8.0f} s ANOMALIA a bordo (inicio)")
for l in log: print(l)
gen = TM_RATE*DIA
print(f"Pasadas = {len(ps)} ; comandos ejecutados = {len(cmds_ok)} de 12 ; pendientes = {len(cola_cmd)}")
print(f"Telemetria generada = {gen/8e6:.3f} MB ; bajada = {bajado/8e6:.3f} MB ; en buffer al final = {buffer_bits/8e6:.3f} MB")
print(f"Anomalia en t = {t_anom:.0f} s ; detectada en t = {anom_det:.0f} s ; latencia = {(anom_det - t_anom)/60:.1f} min")
# invariantes
assert orden_ok
assert abs(gen - bajado - buffer_bits) < 1e-6*gen
assert all(ps[j][1] <= ps[j+1][0] for j in range(len(ps)-1))
tot_cmd_t = len(cmds_ok)*CMD_T; tot_cont = sum(f - i for i, f, _ in ps)
print(f"Tiempo de comando = {tot_cmd_t:.0f} s de {tot_cont:.0f} s de contacto ({100*tot_cmd_t/tot_cont:.1f} %)")
assert tot_cmd_t <= tot_cont
print("Pruebas superadas.")
