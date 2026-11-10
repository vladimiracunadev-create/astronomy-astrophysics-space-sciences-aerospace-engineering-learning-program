"""B96-C24: ejecutor automatico de pasada SINTETICO con tiempos limite, reintentos y cancelacion manual; prueba exhaustiva de fallos."""
import itertools, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: pasos y tiempos ficticios; el ejecutor es una maquina de estados de banco")
# paso: (nombre, duracion nominal s, tiempo limite s, reintentos, es_comando)
PASOS = [("Pre-chequeo de equipos", 20, 40, 1, False), ("Apuntar antena", 30, 60, 1, False),
         ("Enganchar portadora", 25, 50, 2, False), ("Enviar comando", 12, 24, 1, True), ("Cerrar pasada", 15, 30, 0, False)]
RESULT = ("ok", "falla", "timeout")
def ejecuta(resultados, cancela_en=None):
    """resultados: dict paso -> lista de resultados por intento (se repite el ultimo). cancela_en: indice de paso en que el operador cancela."""
    t = 0.0; estado = "EN_CURSO"; log = []; enganchado = False; cmd_enviado = False; seguro = False
    for i, (n, dur, lim, rein, es_cmd) in enumerate(PASOS):
        if cancela_en == i:
            estado = "CANCELADO"; seguro = True; log.append((t, n, "cancelado por operador")); break
        intentos = 0
        while True:
            res = resultados[i][min(intentos, len(resultados[i]) - 1)]
            intentos += 1
            if res == "ok": t += dur
            elif res == "falla": t += dur
            else: t += lim
            if es_cmd and not enganchado:
                estado = "ABORTADO"; log.append((t, n, "comando sin enganche: BLOQUEADO")); seguro = True; break
            if res == "ok":
                if n.startswith("Enganchar"): enganchado = True
                if es_cmd: cmd_enviado = True
                log.append((t, n, f"ok (intento {intentos})")); break
            if intentos > rein:
                estado = "ABORTADO"; seguro = True; log.append((t, n, f"{res}: agotados los reintentos")); break
        if estado != "EN_CURSO": break
    else:
        estado = "COMPLETADO"; seguro = True
    return estado, t, log, cmd_enviado, enganchado, seguro
# prueba exhaustiva: cada paso con primer resultado en {ok, falla, timeout} y segundo intento ok o igual que el primero
casos = 0; estados = {"COMPLETADO": 0, "ABORTADO": 0, "CANCELADO": 0}; violaciones = 0; tmax = 0.0
for primeros in itertools.product(RESULT, repeat=len(PASOS)):
    for reint_ok in (True, False):
        res = {i: ([p, "ok"] if reint_ok else [p]) for i, p in enumerate(primeros)}
        for canc in [None] + list(range(len(PASOS))):
            est, t, log, cmd, enc, seg = ejecuta(res, canc)
            casos += 1; estados[est] += 1; tmax = max(tmax, t)
            # propiedades
            if est == "EN_CURSO": violaciones += 1
            if cmd and not enc: violaciones += 1       # nunca comandar sin enganche
            if not seg: violaciones += 1               # siempre termina en estado seguro
            if canc is not None and est == "COMPLETADO": violaciones += 1
print(f"Escenarios probados = {casos} ; estados finales = {estados} ; violaciones de propiedad = {violaciones}")
print(f"Duracion maxima observada = {tmax:.0f} s ; nominal = {sum(p[1] for p in PASOS)} s")
assert violaciones == 0 and casos == 3**5*2*6
nom = ejecuta({i: ["ok"] for i in range(len(PASOS))})
print("Pasada nominal:", nom[0], f"en {nom[1]:.0f} s")
for l in nom[2]: print(f"  t={l[0]:5.0f} s  {l[1]:25s} {l[2]}")
assert nom[0] == "COMPLETADO" and nom[1] == sum(p[1] for p in PASOS)
f = ejecuta({0: ["ok"], 1: ["ok"], 2: ["timeout", "timeout", "timeout"], 3: ["ok"], 4: ["ok"]})
print("Falla de enganche con reintentos agotados:", f[0], f"en {f[1]:.0f} s ; comando enviado = {f[3]}")
assert f[0] == "ABORTADO" and not f[3]
print("Pruebas superadas.")
