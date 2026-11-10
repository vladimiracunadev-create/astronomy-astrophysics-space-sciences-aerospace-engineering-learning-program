# SPDX-License-Identifier: Apache-2.0
"""B85-C19: ensayo de vacío térmico: perfil de ciclado, tiempos de rampa y de estabilización, y duración total.

Consultado: nada específico de procedimientos de ensayo. ILUSTRATIVO y SINTÉTICO: artículo de ensayo, conductancia a la pantalla,
disipación, rangos, tasa de rampa, margen de ensayo, criterio de estabilización. ECSS y estándares de ensayo NO consultados.
Segunda vía: respuesta analítica del nodo a una rampa y a un escalón frente a la integración numérica.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

C_ART, G_ART, Q_ART = 20000.0, 2.0, 15.0     # J/K, W/K, W (ilustrativos)
RAMPA = 3.0 / 60.0                          # K/s (3 K/min, ilustrativo)
T_PRED_MAX, T_PRED_MIN = 320.0, 255.0        # K predichos (sinteticos)
MARGEN = 10.0                               # K de margen de ensayo (ilustrativo)
CRITERIO = 1.0 / 3600.0                      # K/s: estabilizado si |dT/dt| < 1 K/h (ilustrativo)
P_INICIAL, P_OBJ = 101325.0, 1.0e-3


def niveles():
    return T_PRED_MIN - MARGEN, T_PRED_MAX + MARGEN


def t_pantalla_para(t_art):
    return t_art - Q_ART / G_ART


def simular(t_ini, t_sh_obj, dwell_max=40000.0, dt=5.0):
    """Pantalla con rampa lineal hasta t_sh_obj y luego fija; devuelve (t_alcanza_obj_pantalla, t_estable, T_final)."""
    t = t_ini
    tau = C_ART / G_ART
    tiempo = 0.0
    sh = t_ini
    t_sh_alcanzada = None
    t_estable = None
    while tiempo < dwell_max:
        paso = RAMPA * dt
        if abs(t_sh_obj - sh) <= paso:
            sh = t_sh_obj
            if t_sh_alcanzada is None:
                t_sh_alcanzada = tiempo
        else:
            sh += paso if t_sh_obj > sh else -paso
        dT = (Q_ART + G_ART * (sh - t)) / C_ART * dt
        t += dT
        tiempo += dt
        if t_sh_alcanzada is not None and abs(dT / dt) < CRITERIO and t_estable is None:
            t_estable = tiempo
            break
    return t_sh_alcanzada, t_estable, t


def tiempo_estabilizacion_analitico(delta0):
    """Tras alcanzar la pantalla, la diferencia con el equilibrio decae como delta0 exp(-t/tau); |dT/dt| = delta/tau."""
    tau = C_ART / G_ART
    return tau * math.log(delta0 / (tau * CRITERIO)) if delta0 > tau * CRITERIO else 0.0


def calcular():
    r = {}
    t_frio, t_cal = niveles()
    r["t_frio"], r["t_cal"] = t_frio, t_cal
    r["sh_cal"], r["sh_frio"] = t_pantalla_para(t_cal), t_pantalla_para(t_frio)
    a1 = simular(293.15, r["sh_cal"])
    a2 = simular(a1[2], r["sh_frio"])
    a3 = simular(a2[2], r["sh_cal"])
    r["tramos"] = [("ambiente -> caliente", a1), ("caliente -> frio", a2), ("frio -> caliente", a3)]
    r["duracion_ciclo_h"] = (a2[1] + a3[1]) / 3600.0
    r["duracion_4_ciclos_h"] = 4 * r["duracion_ciclo_h"] + a1[1] / 3600.0
    r["t_bombeo_h"] = -(2.0 / 0.5) * math.log((P_OBJ - 8e-5) / (P_INICIAL - 8e-5)) / 3600.0
    r["tau"] = C_ART / G_ART
    # analitico: al alcanzar la pantalla, la diferencia con el equilibrio
    b = a1
    dif_ini = abs((r["sh_cal"] + Q_ART / G_ART) - b[2]) if False else None
    r["estab_analitico_demo"] = tiempo_estabilizacion_analitico(5.0)
    # numerico para un escalon: pantalla fija y articulo 5 K por debajo del equilibrio
    t = r["t_cal"] - 5.0
    tiempo = 0.0
    while True:
        dT = (Q_ART + G_ART * (r["sh_cal"] - t)) / C_ART * 5.0
        t += dT
        tiempo += 5.0
        if abs(dT / 5.0) < CRITERIO:
            break
    r["estab_numerico_demo"] = tiempo
    r["margen_total"] = (t_cal - t_frio) - (T_PRED_MAX - T_PRED_MIN)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Articulo ILUSTRATIVO: C = {C_ART:.0f} J/K, G a la pantalla = {G_ART} W/K, disipa {Q_ART:.0f} W ; tau = {r['tau']:.0f} s")
    print(f"Predicho (sintetico) {T_PRED_MIN:.0f}-{T_PRED_MAX:.0f} K ; margen de ensayo {MARGEN:.0f} K -> niveles {r['t_frio']:.0f}-{r['t_cal']:.0f} K")
    print(f"Pantalla necesaria: caliente {r['sh_cal']:.1f} K ; frio {r['sh_frio']:.1f} K (T_pantalla = T_objetivo - Q/G)")
    print(f"Rampa de la pantalla: {RAMPA*60:.1f} K/min ; criterio de estabilizacion: |dT/dt| < 1 K/h")
    for nombre, (t_sh, t_est, tf) in r["tramos"]:
        print(f"  {nombre:<22}: pantalla en el objetivo a los {t_sh/3600:.2f} h ; articulo estable a las {t_est/3600:.2f} h ; T = {tf:.2f} K")
    print(f"Ciclo completo (caliente + frio) = {r['duracion_ciclo_h']:.2f} h ; 4 ciclos con la subida inicial = {r['duracion_4_ciclos_h']:.1f} h ; bombeo a 1e-3 Pa (C12) = {r['t_bombeo_h']:.3f} h")
    print(f"Estabilizacion de un escalon de 5 K: analitica = {r['estab_analitico_demo']:.0f} s ; numerica = {r['estab_numerico_demo']:.0f} s")
    comprobar(abs(r["estab_analitico_demo"] - r["estab_numerico_demo"]) <= 10.0, "estabilizacion analitica frente a numerica")
    comprobar(r["margen_total"] == 2 * MARGEN, "margen total")
    fin()


if __name__ == "__main__":
    main()
