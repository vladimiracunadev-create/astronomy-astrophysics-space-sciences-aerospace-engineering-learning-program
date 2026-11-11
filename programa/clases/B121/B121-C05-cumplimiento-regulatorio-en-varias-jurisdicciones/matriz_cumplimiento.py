"""B121-C05 - Matriz de cumplimiento multijurisdiccion y envolvente del requisito mas estricto.

DATOS: los requisitos de J1 (IADC Rev. 4, 2025-01, recomendaciones) y J2 (47 CFR 25.114(d)(14)(vii)
y 14 CFR 450.101(a), eCFR) fueron CONSULTADOS el 2026-11-11. J3 es una jurisdiccion HIPOTETICA
SINTETICA inventada para el ejercicio. El diseno de mision y los plazos de tramite son SINTETICOS.
Unidades: anos, probabilidad e bajas esperadas (adimensionales). No es asesoria legal.
Solo biblioteca estandar.
"""
import itertools
import sys

# requisito: (sentido, valores por jurisdiccion). sentido "max": el diseno debe ser <= valor; "min": >= valor
REQ = {
    "plazo de desorbita LEO [a]": ("max", {"J1_IADC": 25.0, "J2_EEUU": 5.0, "J3_hipotetica": 10.0}),
    "P(exito de desorbita)": ("min", {"J1_IADC": 0.90, "J2_EEUU": 0.90, "J3_hipotetica": 0.95}),
    "Ec reentrada": ("max", {"J1_IADC": 1e-4, "J2_EEUU": 1e-4, "J3_hipotetica": 5e-5}),
    "Ec lanzamiento (publico)": ("max", {"J2_EEUU": 1e-4, "J3_hipotetica": 1e-4}),
}
DISENO = {  # SINTETICO
    "plazo de desorbita LEO [a]": 7.56,
    "P(exito de desorbita)": 0.92,
    "Ec reentrada": 5.0e-5,
    "Ec lanzamiento (publico)": 8.0e-5,
}
# dias de tramite por jurisdiccion SINTETICOS: (preparar, evaluar)
TRAMITE = {"J1_IADC": (0, 0), "J2_EEUU": (30, 120), "J3_hipotetica": (45, 150)}


def cumple(sentido, valor, lim):
    return valor <= lim if sentido == "max" else valor >= lim


def envolvente(sentido, vals):
    return min(vals.values()) if sentido == "max" else max(vals.values())


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("J1 y J2: requisitos consultados 2026-11-11. J3: HIPOTETICA y SINTETICA. Diseno y tramites: SINTETICOS.")
    js = ["J1_IADC", "J2_EEUU", "J3_hipotetica"]
    print(f"{'requisito':30s}{'diseno':>10s}" + "".join(f"{j:>15s}" for j in js) + f"{'envolvente':>12s}")
    fallos = []
    for r, (s, vals) in REQ.items():
        d = DISENO[r]
        celdas = []
        for j in js:
            if j in vals:
                ok = cumple(s, d, vals[j])
                celdas.append(f"{vals[j]:g} {'OK' if ok else 'NO'}")
                if not ok:
                    fallos.append((r, j))
            else:
                celdas.append("-")
        env = envolvente(s, vals)
        assert cumple(s, d, env) == all(cumple(s, d, v) for v in vals.values())  # envolvente = todas
        print(f"{r:30s}{d:10g}" + "".join(f"{c:>15s}" for c in celdas) + f"{env:12g}")
    print("Incumplimientos:", fallos if fallos else "ninguno")
    # verificacion por fuerza bruta: el diseno cumple todo <=> no hay celdas fallidas
    todo = all(cumple(s, DISENO[r], v) for r, (s, vals) in REQ.items() for v in vals.values())
    assert todo == (not fallos)
    # camino critico de tramites: en serie vs en paralelo
    tot = {j: sum(t) for j, t in TRAMITE.items()}
    serie = sum(tot.values())
    paralelo = max(tot.values())
    assert paralelo <= serie
    print("Dias por jurisdiccion:", tot, "| en serie:", serie, "d | en paralelo:", paralelo, "d")
    # mejora minima del diseno para cumplir la envolvente: cuanto debe bajar Ec de reentrada
    env = envolvente("max", REQ["Ec reentrada"][1])
    print(f"Ec de reentrada: diseno {DISENO['Ec reentrada']:.1e} frente a envolvente {env:.1e} -> margen {env/DISENO['Ec reentrada']:.2f}x")
    # busqueda: cuantas de las 2^4 combinaciones de 'cambiar o no cambiar' cada parametro cumplen
    mejor = {r: envolvente(s, v) for r, (s, v) in REQ.items()}
    n_ok = 0
    for mask in itertools.product([0, 1], repeat=len(REQ)):
        d = {r: (mejor[r] if m else DISENO[r]) for m, r in zip(mask, REQ)}
        if all(cumple(s, d[r], v) for r, (s, vals) in REQ.items() for v in vals.values()):
            n_ok += 1
    print(f"Combinaciones (de 16) de ajustar o no cada parametro a la envolvente que cumplen todo: {n_ok}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
