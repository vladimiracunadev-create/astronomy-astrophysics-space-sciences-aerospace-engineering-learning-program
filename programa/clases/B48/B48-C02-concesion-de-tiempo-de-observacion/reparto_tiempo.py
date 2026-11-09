"""Reparto de horas de telescopio por cuotas y horas efectivas tras el clima.

Datos: solicitudes y cuotas SINTÉTICAS (cuatro instituciones ficticias); no corresponden a ningún
comité real. No se consultó ninguna fuente externa.
Modelo: reparto de 620 horas con el método de Hamilton (mayor resto) y con el de D'Hondt (divisores);
horas efectivas = horas asignadas por la probabilidad de noche despejada (binomial).
Supuestos: horas enteras; clima independiente entre noches con p = 0,72 (ilustrativo).
Tolerancia: las sumas deben ser exactas; la simulación a menos de 4 sigmas de la media analítica.
"""
import math
import random

CUOTAS = {"Instituto A": 0.38, "Instituto B": 0.27, "Instituto C": 0.21, "Instituto D": 0.14}
HORAS = 620
SOLICITADO = {"Instituto A": 410, "Instituto B": 300, "Instituto C": 150, "Instituto D": 190}
P_CLARO = 0.72
NOCHES = 62
SEMILLA = 20261109


def hamilton(cuotas, total):
    exactas = {k: v * total for k, v in cuotas.items()}
    base = {k: math.floor(v) for k, v in exactas.items()}
    resto = total - sum(base.values())
    orden = sorted(exactas, key=lambda k: exactas[k] - base[k], reverse=True)
    for k in orden[:resto]:
        base[k] += 1
    return base


def dhondt(cuotas, total):
    out = {k: 0 for k in cuotas}
    for _ in range(total):
        k = max(cuotas, key=lambda x: cuotas[x] / (out[x] + 1))
        out[k] += 1
    return out


def calc():
    h = hamilton(CUOTAS, HORAS)
    d = dhondt(CUOTAS, HORAS)
    presion = {k: SOLICITADO[k] / h[k] for k in h}
    total_pres = sum(SOLICITADO.values()) / HORAS
    # horas efectivas: 10 h por noche, 62 noches; cada noche despejada con p
    esp = NOCHES * 10 * P_CLARO
    sig = 10 * math.sqrt(NOCHES * P_CLARO * (1 - P_CLARO))
    rng = random.Random(SEMILLA)
    reps = 20000
    suma = 0.0
    suma2 = 0.0
    for _ in range(reps):
        x = 10 * sum(1 for _ in range(NOCHES) if rng.random() < P_CLARO)
        suma += x
        suma2 += x * x
    media = suma / reps
    var = suma2 / reps - media ** 2
    return dict(h=h, d=d, presion=presion, total_pres=total_pres, esp=esp, sig=sig, media=media, sd=math.sqrt(var),
                z=(media - esp) / (sig / math.sqrt(reps)))


def main():
    R = calc()
    for k in CUOTAS:
        print(f"{k}: Hamilton {R['h'][k]:4d} h | D'Hondt {R['d'][k]:4d} h | presión {R['presion'][k]:.2f}")
    print(f"Presión global = {R['total_pres']:.3f}")
    print(f"Horas efectivas esperadas = {R['esp']:.1f} h (sigma {R['sig']:.2f} h)")
    print(f"Simulación: media {R['media']:.2f} h, desviación {R['sd']:.2f} h, z = {R['z']:+.2f}")
    assert sum(R["h"].values()) == HORAS and sum(R["d"].values()) == HORAS
    for k, v in CUOTAS.items():
        assert abs(R["h"][k] - v * HORAS) < 1 and abs(R["d"][k] - v * HORAS) < 2
    assert abs(R["z"]) < 4 and abs(R["sd"] - R["sig"]) < 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
