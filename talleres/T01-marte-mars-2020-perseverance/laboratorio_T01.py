# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T01 (Marte, Mars 2020 / Perseverance).

Calcula, con modelos simples y declarados, las cifras que el taller discute:
  1. Transferencia de Hohmann Tierra-Marte (delta-v, C3, tiempo de vuelo, ventana).
  2. Velocidad de entrada en la atmósfera de Marte.
  3. Retardo de comunicación Tierra-Marte.
  4. Presupuesto de masa con la ecuación del cohete.
  5. Potencia del MMRTG a lo largo de la misión.
  6. Confiabilidad de una cadena de eventos críticos (entrada, descenso y aterrizaje).
  7. Costo con reservas.

UNIDADES: km, s, kg, W, km/s, años; masas en kg; costos en millones de USD (MUSD).
SISTEMA DE REFERENCIA: heliocéntrico eclíptico (órbitas circulares y coplanares) para la transferencia;
areocéntrico para la entrada. MODELO: cónicas de dos cuerpos, órbitas planetarias circulares y coplanares.
TOLERANCIA: los resultados son de orden de diseño preliminar (±5 % frente a un diseño real con órbitas
elípticas e inclinadas); no sirven para diseñar una trayectoria de vuelo.
DATOS: constantes planetarias de la NASA/JPL (valores redondeados); cifras de la misión redondeadas.
VERSIONES: Python 3.12, solo biblioteca estándar.
"""
from __future__ import annotations

import math

# --- Constantes (km, s) ------------------------------------------------------------------------
MU_SOL = 1.32712440018e11      # km^3/s^2
MU_TIERRA = 3.986004418e5      # km^3/s^2
MU_MARTE = 4.282837e4          # km^3/s^2
UA = 1.495978707e8             # km
A_TIERRA = 1.000 * UA          # semieje de la órbita de la Tierra (circular)
A_MARTE = 1.524 * UA           # semieje de la órbita de Marte (circular)
R_TIERRA = 6378.137            # km, radio ecuatorial
R_MARTE = 3396.19              # km, radio ecuatorial
C_LUZ = 299792.458             # km/s
G0 = 9.80665                   # m/s^2


def hohmann(a1: float, a2: float, mu: float = MU_SOL) -> dict:
    """Transferencia de Hohmann entre dos órbitas circulares coplanares alrededor de mu."""
    v1 = math.sqrt(mu / a1)
    v2 = math.sqrt(mu / a2)
    at = (a1 + a2) / 2
    vt1 = math.sqrt(mu * (2 / a1 - 1 / at))
    vt2 = math.sqrt(mu * (2 / a2 - 1 / at))
    t_vuelo = math.pi * math.sqrt(at**3 / mu)
    return {"v_inf_salida": vt1 - v1, "v_inf_llegada": v2 - vt2, "t_vuelo_s": t_vuelo,
            "n1": v1 / a1, "n2": v2 / a2}


def periodo_sinodico(a1: float, a2: float, mu: float = MU_SOL) -> float:
    t1 = 2 * math.pi * math.sqrt(a1**3 / mu)
    t2 = 2 * math.pi * math.sqrt(a2**3 / mu)
    return 1 / abs(1 / t1 - 1 / t2)


def capitulo_trayectoria() -> None:
    h = hohmann(A_TIERRA, A_MARTE)
    c3 = h["v_inf_salida"] ** 2
    dias = h["t_vuelo_s"] / 86400
    # delta-v de salida desde una órbita circular baja de 200 km (impulso en el perigeo)
    r0 = R_TIERRA + 200
    v_circ = math.sqrt(MU_TIERRA / r0)
    v_perigeo = math.sqrt(h["v_inf_salida"] ** 2 + 2 * MU_TIERRA / r0)
    dv_leo = v_perigeo - v_circ
    # ángulo de fase de Marte respecto a la Tierra al salir: Marte debe ir adelantado
    fase = math.degrees(math.pi - h["n2"] * h["t_vuelo_s"])
    sin = periodo_sinodico(A_TIERRA, A_MARTE) / 86400
    print("1. TRANSFERENCIA TIERRA-MARTE (Hohmann, órbitas circulares y coplanares)")
    print(f"   v_inf de salida       : {h['v_inf_salida']:.3f} km/s")
    print(f"   C3 = v_inf^2          : {c3:.2f} km^2/s^2   (la misión real usó más, ≈ 14-15: ver capítulo 2)")
    print(f"   delta-v desde LEO 200 : {dv_leo:.3f} km/s")
    print(f"   v_inf de llegada      : {h['v_inf_llegada']:.3f} km/s")
    print(f"   tiempo de vuelo       : {dias:.1f} días  (la misión real tardó ≈ 203 días)")
    print(f"   ángulo de fase        : {fase:.1f}° (Marte adelantado de la Tierra al partir)")
    print(f"   período sinódico      : {sin:.1f} días ≈ {sin / 30.4375:.1f} meses entre ventanas")
    return h


def entrada(v_inf: float, altitud_km: float = 125.0) -> float:
    """Velocidad areocéntrica en la interfaz de entrada (conservación de la energía en la hipérbola)."""
    r = R_MARTE + altitud_km
    return math.sqrt(v_inf**2 + 2 * MU_MARTE / r)


def capitulo_entrada(h: dict) -> None:
    v = entrada(h["v_inf_llegada"])
    v_real = entrada(2.9)
    print("2. ENTRADA EN LA ATMÓSFERA DE MARTE (interfaz a 125 km)")
    print(f"   v de entrada con v_inf de Hohmann ({h['v_inf_llegada']:.2f} km/s): {v:.2f} km/s")
    print(f"   v de entrada con v_inf = 2.9 km/s                          : {v_real:.2f} km/s  (≈ {v_real * 3600:,.0f} km/h)".replace(",", "."))
    print("   (la misión real entró a ≈ 5.4-5.6 km/s)")


def capitulo_comunicaciones() -> None:
    print("3. RETARDO DE LUZ TIERRA-MARTE")
    for nombre, d_ua in (("mínima (oposición)", 0.37), ("al aterrizaje de 2021", 1.32), ("máxima (conjunción)", 2.67)):
        d = d_ua * UA
        t = d / C_LUZ
        print(f"   distancia {nombre:<22}: {d_ua:4.2f} UA  -> {t / 60:5.1f} min en un sentido, {2 * t / 60:5.1f} min ida y vuelta")
    print("   la entrada dura ≈ 7 min: cuando llega la señal de 'entrada', el vehículo ya aterrizó o ya falló")


def cohete(isp_s: float, m0: float, mf: float) -> float:
    """Delta-v ideal de la ecuación del cohete, en km/s."""
    return isp_s * G0 * math.log(m0 / mf) / 1000


def capitulo_masas() -> None:
    print("4. ECUACIÓN DEL COHETE Y PRESUPUESTO DE MASA (cifras redondeadas)")
    # Etapa de crucero del Mars 2020 ≈ 540 kg (estructura + combustible de correcciones)
    dv_tcm = 0.020  # km/s, presupuesto ilustrativo de correcciones de trayectoria en el crucero
    isp_hidrazina = 220.0
    m_final = 4050.0
    m_ini = m_final * math.exp(dv_tcm * 1000 / (isp_hidrazina * G0))
    print(f"   corrección de {dv_tcm * 1000:.0f} m/s con hidrazina (Isp {isp_hidrazina:.0f} s) sobre una nave de {m_final:.0f} kg")
    print(f"   combustible necesario  : {m_ini - m_final:.1f} kg")
    # Descenso propulsado: 8 motores MLE, empuje ~ 3 kN cada uno (ilustrativo)
    m_desc = 2300.0
    dv_desc = cohete(215.0, m_desc, m_desc - 400.0)
    print(f"   etapa de descenso: con 400 kg de combustible y Isp 215 s, delta-v ideal = {dv_desc:.3f} km/s")
    masas = {"rover": 1025, "etapa de descenso": 2070, "etapa de crucero": 540, "escudo/cápsula": 410}
    print("   reparto aproximado (kg):", ", ".join(f"{k} {v}" for k, v in masas.items()), f"-> total ≈ {sum(masas.values())} kg")


def mmrtg(anios: float, p0: float = 110.0, degradacion_anual: float = 0.048) -> float:
    """Potencia eléctrica del MMRTG tras 'anios' años (modelo exponencial de degradación total)."""
    return p0 * math.exp(-degradacion_anual * anios)


def capitulo_potencia() -> None:
    print("5. POTENCIA DEL MMRTG (110 W al inicio; degradación ≈ 4.8 % anual, modelo exponencial)")
    for a in (0, 1, 2, 5, 10, 14):
        print(f"   año {a:>2}: {mmrtg(a):6.1f} W")


def confiabilidad_serie(probabilidades: list[float]) -> float:
    p = 1.0
    for x in probabilidades:
        p *= x
    return p


def capitulo_confiabilidad() -> None:
    print("6. CONFIABILIDAD DE LA ENTRADA, DESCENSO Y ATERRIZAJE (cadena en serie, valores ilustrativos)")
    eventos = {"separación de la etapa de crucero": 0.999, "entrada atmosférica y escudo térmico": 0.995,
               "apertura del paracaídas": 0.990, "navegación relativa al terreno": 0.990,
               "descenso propulsado": 0.990, "grúa aérea y contacto": 0.990}
    p = confiabilidad_serie(list(eventos.values()))
    for k, v in eventos.items():
        print(f"   {k:<42}: {v:.3f}")
    print(f"   probabilidad de éxito de la cadena: {p:.4f}  ({(1 - p) * 100:.1f} % de riesgo)")
    mejor = confiabilidad_serie([1 - (1 - v) ** 2 if k.startswith("separación") else v for k, v in eventos.items()])
    print(f"   con un respaldo independiente solo en la separación: {mejor:.4f}  (mejora pequeña: el riesgo está repartido)")
    print("   lección: en una cadena en serie manda el producto; no hay un eslabón 'seguro'")


def capitulo_costos() -> None:
    print("7. COSTO CON RESERVAS (MUSD, reparto ilustrativo)")
    # Reparto ILUSTRATIVO: solo el lanzamiento (243) y el total (≈ 2700) son cifras públicas; el resto se
    # calibró para que base + reserva dé el orden del costo publicado. El estudiante lo reemplaza con su fuente.
    base = {"rover y etapas (diseño, construcción, pruebas)": 1300.0, "instrumentos": 250.0,
            "lanzamiento": 243.0, "operaciones de la misión primaria": 300.0}
    subtotal = sum(base.values())
    for k, v in base.items():
        print(f"   {k:<48}: {v:7.0f}")
    for reserva in (0.20, 0.30):
        print(f"   subtotal {subtotal:.0f} + reserva {reserva:.0%} = {subtotal * (1 + reserva):,.0f}".replace(",", "."))
    print("   referencia publicada: ≈ 2700 MUSD de costo total del ciclo de vida (NASA); el costo real ya incluye sus reservas")


def main() -> None:
    print("TALLER T01 - Marte (Mars 2020 / Perseverance): laboratorio de diseño preliminar")
    print("Modelos simples; resultados de orden de diseño (±5 %), no de vuelo.\n")
    h = capitulo_trayectoria()
    print()
    capitulo_entrada(h)
    print()
    capitulo_comunicaciones()
    print()
    capitulo_masas()
    print()
    capitulo_potencia()
    print()
    capitulo_confiabilidad()
    print()
    capitulo_costos()


if __name__ == "__main__":
    main()
