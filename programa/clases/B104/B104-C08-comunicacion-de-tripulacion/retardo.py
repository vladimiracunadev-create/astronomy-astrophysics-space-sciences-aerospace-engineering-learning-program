#!/usr/bin/env python3
"""B104-C08: retardo de luz y repeticion de lectura (read-back) en un canal con ruido.
Distancias estandar (no consultadas en una fuente concreta); tasa de error y mensajes SINTETICOS (semilla 104)."""
import sys
import numpy as np

C = 299_792.458   # km/s
print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: distancias estandar no consultadas; mensajes SINTETICOS (semilla 104)")

# (a) Retardo de luz
dist = [("ISS (400 km, ilustrativo)", 400.0), ("Luna (media 384 400 km)", 384_400.0),
        ("Marte, minimo (~54,6 millones de km)", 54.6e6), ("Marte, maximo (~401 millones de km)", 401e6)]
print("\nDestino | ida [s] | ida y vuelta [s]")
ret = {}
for n, d in dist:
    ret[n] = d / C
    print(f"{n:42s} {d/C:10.3f} {2*d/C:12.3f}")
assert abs(ret[dist[1][0]] - 1.282) < 0.001
assert abs(ret[dist[3][0]] / 60 - 22.3) < 0.1

# (b) Una pregunta y su respuesta en una conversacion con turnos de 5 s
turno = 5.0
print("\nTiempo de un intercambio (pregunta + respuesta, 5 s por mensaje) y de 10 intercambios")
for n, _ in dist:
    t = 2 * ret[n] + 2 * turno
    print(f"{n:42s} {t:10.1f} s por intercambio; {10*t/60:8.1f} min por 10")

# (c) Repeticion de lectura en un canal con errores por palabra
rng = np.random.default_rng(104)
P_PAL, PALABRAS, C_DET, N = 0.01, 20, 0.95, 200_000


def residual(read_back):
    uplink_err = (rng.random((N, PALABRAS)) < P_PAL).any(axis=1)
    if not read_back:
        return uplink_err.mean(), 0.0
    downlink_err = (rng.random((N, PALABRAS)) < P_PAL).any(axis=1)
    discrepancia = uplink_err | downlink_err
    detectada = discrepancia & (rng.random(N) < C_DET)
    # si se detecta, se repite el mensaje; un error residual queda solo si hubo error de subida no detectado
    residuo = (uplink_err & ~detectada).mean()
    return residuo, detectada.mean()


e_sin, _ = residual(False)
e_con, falsas = residual(True)
e_teo = (1 - (1 - P_PAL) ** PALABRAS)
print(f"\nError por mensaje de {PALABRAS} palabras con p = {P_PAL} por palabra: teorico {e_teo:.4f}")
print(f"  sin repeticion de lectura: error residual {e_sin:.4f}")
print(f"  con repeticion de lectura (deteccion {C_DET:.2f}): error residual {e_con:.4f}; mensajes repetidos {falsas:.4f}")
print("Costo en tiempo de la repeticion: 2 mensajes extra por intercambio -> en Marte (minimo) +%.0f s" % (2 * ret[dist[2][0]]))

assert abs(e_sin - e_teo) < 0.003
assert e_con < e_sin / 5
print("Pruebas superadas.")
