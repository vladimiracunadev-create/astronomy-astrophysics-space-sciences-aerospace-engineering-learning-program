"""B118-C20 · Evaluación de riesgo de conjunción documentada.

Genera un REGISTRO reproducible de una evaluación de riesgo para un evento SINTÉTICO: entradas con unidades, versión del método, Pc por
cuadratura, sensibilidad a la escala de la covarianza, categoría y huella SHA-256 del registro canónico.
Los umbrales de categoría (1e-7 y 1e-4) son ILUSTRATIVOS; NO se tomaron de ninguna política operativa ni se consultó una.
Sistema de referencia: plano de encuentro (x a lo largo del desfase, y perpendicular). Unidades: m, m/s, adimensional.
Tolerancia numérica: cuadratura polar con 300 x 300 puntos (error relativo < 0,2 % frente a la aproximación de disco pequeño con R << sigma).
"""
import hashlib
import json
import math
import sys

VERSION = "lab-b118-c20-1.0"
UMBRAL_ROJO, UMBRAL_AMARILLO = 1e-4, 1e-7  # ILUSTRATIVOS


def validar(ev):
    for k in ("miss_m", "sx_m", "sy_m", "radio_m", "v_rel_ms"):
        if k not in ev:
            raise ValueError(f"falta {k}")
    if ev["sx_m"] <= 0 or ev["sy_m"] <= 0 or ev["radio_m"] <= 0:
        raise ValueError("sigmas y radio deben ser positivos")
    if ev["miss_m"] < 0:
        raise ValueError("miss no puede ser negativo")


def pc(miss, sx, sy, R, n=300):
    tot = 0.0
    dr, dth = R / n, 2 * math.pi / n
    for i in range(n):
        r = (i + 0.5) * dr
        for j in range(n):
            th = (j + 0.5) * dth
            x, y = r * math.cos(th), r * math.sin(th)
            tot += math.exp(-0.5 * (((x - miss) / sx) ** 2 + (y / sy) ** 2)) * r * dr * dth
    return tot / (2 * math.pi * sx * sy)


def categoria(p):
    return "ROJO" if p >= UMBRAL_ROJO else ("AMARILLO" if p >= UMBRAL_AMARILLO else "VERDE")


def evaluar(ev, escalas=(0.5, 1.0, 2.0)):
    validar(ev)
    sens = {}
    for s in escalas:
        sens[f"{s}"] = pc(ev["miss_m"], ev["sx_m"] * s, ev["sy_m"] * s, ev["radio_m"], n=120)
    p0 = pc(ev["miss_m"], ev["sx_m"], ev["sy_m"], ev["radio_m"])
    peor = max(sens.values())
    reg = {
        "version_metodo": VERSION,
        "tipo_datos": "SINTETICO",
        "entradas": ev,
        "unidades": {"miss_m": "m", "sx_m": "m", "sy_m": "m", "radio_m": "m", "v_rel_ms": "m/s"},
        "sistema_referencia": "plano de encuentro (x a lo largo del desfase)",
        "pc": float(f"{p0:.6e}"),
        "sensibilidad_escala_covarianza": {k: float(f"{x:.6e}") for k, x in sens.items()},
        "pc_peor_caso": float(f"{peor:.6e}"),
        "categoria_nominal": categoria(p0),
        "categoria_peor_caso": categoria(peor),
        "umbrales_ilustrativos": {"amarillo": UMBRAL_AMARILLO, "rojo": UMBRAL_ROJO},
        "tolerancia": "cuadratura 300x300; sensibilidad 120x120",
    }
    canon = json.dumps(reg, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    reg_huella = hashlib.sha256(canon.encode()).hexdigest()
    return reg, reg_huella


def compute():
    v = {}
    ev = dict(id_evento="SINT-0001", miss_m=350.0, sx_m=200.0, sy_m=120.0, radio_m=8.0, v_rel_ms=14000.0)
    v["ev"] = ev
    v["reg"], v["hash"] = evaluar(ev)
    v["reg2"], v["hash2"] = evaluar(ev)
    ev3 = dict(ev, miss_m=351.0)
    v["reg3"], v["hash3"] = evaluar(ev3)
    v["aprox"] = ev["radio_m"] ** 2 / (2 * ev["sx_m"] * ev["sy_m"]) * math.exp(-0.5 * (ev["miss_m"] / ev["sx_m"]) ** 2)
    errores = []
    for malo in (dict(ev, sx_m=-1.0), dict(ev, miss_m=-5.0), {k: x for k, x in ev.items() if k != "radio_m"}):
        try:
            validar(malo)
            errores.append("no detectado")
        except ValueError as e:
            errores.append(str(e))
    v["errores"] = errores
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Evento SINTETICO; umbrales de categoria ILUSTRATIVOS (no tomados de ninguna politica); version del metodo " + VERSION)
    v = compute()
    r = v["reg"]
    print(f"Pc nominal = {r['pc']:.4e} (aproximacion de disco pequeno {v['aprox']:.4e}); categoria {r['categoria_nominal']}")
    for k, x in r["sensibilidad_escala_covarianza"].items():
        print(f"  covarianza x{k}: Pc = {x:.4e}")
    print(f"Pc de peor caso = {r['pc_peor_caso']:.4e}; categoria de peor caso {r['categoria_peor_caso']}")
    print(f"Huella SHA-256: {v['hash']}")
    print(f"Repetida:       {v['hash2']} (iguales: {v['hash'] == v['hash2']})")
    print(f"Miss 351 m:     {v['hash3'][:16]}... (distinta: {v['hash'] != v['hash3']})")
    for e in v["errores"]:
        print(f"  validacion: {e}")
    assert v["hash"] == v["hash2"] and v["hash"] != v["hash3"]
    assert abs(r["pc"] / v["aprox"] - 1) < 0.002
    assert all(e != "no detectado" for e in v["errores"])
    print("Pruebas superadas (reproducibilidad por huella, sensibilidad a la entrada, validacion de entradas).")


if __name__ == "__main__":
    main()
