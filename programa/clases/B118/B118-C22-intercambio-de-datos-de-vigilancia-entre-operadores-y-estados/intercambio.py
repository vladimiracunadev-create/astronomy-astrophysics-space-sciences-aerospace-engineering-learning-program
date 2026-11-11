"""B118-C22 · Intercambio de datos de vigilancia entre operadores y Estados.

Mensaje SINTÉTICO de conjunción en texto clave = valor [unidad], INSPIRADO en el estilo KVN de los mensajes CCSDS pero NO conforme a
CCSDS 508.0-B-1 (de ese documento solo se consultó su ficha: título «Conjunction Data Message», Issue 1, junio de 2013, con correcciones técnicas
hasta octubre de 2021; la sintaxis no se consultó). Se implementan serialización, análisis, validación de unidades y reconciliación entre dos
operadores.
Unidades: m, m/s, adimensional (SI en el mensaje). Tolerancias: ida y vuelta exacta; reconciliación a 1 % relativo.
"""
import sys

CAMPOS = [
    ("MESSAGE_ID", str, None),
    ("ORIGINATOR", str, None),
    ("CREATION_DATE", str, None),
    ("TCA", str, None),
    ("OBJECT1", str, None),
    ("OBJECT2", str, None),
    ("MISS_DISTANCE", float, "m"),
    ("RELATIVE_SPEED", float, "m/s"),
    ("COLLISION_PROBABILITY", float, None),
]
A_SI = {"m": 1.0, "km": 1000.0, "m/s": 1.0, "km/s": 1000.0}


def serializar(d):
    lineas = []
    for k, tipo, u in CAMPOS:
        if k not in d:
            raise ValueError(f"falta {k}")
        val = repr(d[k]) if tipo is float else d[k]
        lineas.append(f"{k} = {val}" + (f" [{u}]" if u else ""))
    return "\n".join(lineas) + "\n"


def analizar(texto):
    d, vistos = {}, set()
    for ln in texto.strip().splitlines():
        if "=" not in ln:
            raise ValueError(f"linea sin '=': {ln!r}")
        k, v = [x.strip() for x in ln.split("=", 1)]
        if k in vistos:
            raise ValueError(f"campo repetido {k}")
        vistos.add(k)
        unidad = None
        if v.endswith("]") and "[" in v:
            v, u = v[:-1].rsplit("[", 1)
            unidad, v = u.strip(), v.strip()
        spec = {c[0]: c for c in CAMPOS}.get(k)
        if spec is None:
            raise ValueError(f"campo desconocido {k}")
        _, tipo, u_esp = spec
        if tipo is float:
            x = float(v)
            if u_esp:
                if unidad is None:
                    raise ValueError(f"{k} sin unidad")
                if unidad not in A_SI:
                    raise ValueError(f"unidad no reconocida {unidad}")
                x *= A_SI[unidad]
            d[k] = x
        else:
            d[k] = v
    faltan = [c[0] for c in CAMPOS if c[0] not in d]
    if faltan:
        raise ValueError("faltan " + ",".join(faltan))
    return d


def reconciliar(a, b, tol=0.01):
    """Compara dos mensajes del mismo evento; devuelve lista de discrepancias."""
    dis = []
    for k in ("MISS_DISTANCE", "RELATIVE_SPEED"):
        ra = abs(a[k] - b[k]) / max(abs(a[k]), abs(b[k]), 1e-30)
        if ra > tol:
            dis.append((k, a[k], b[k], ra))
    if a["TCA"] != b["TCA"]:
        dis.append(("TCA", a["TCA"], b["TCA"], None))
    return dis


def compute():
    v = {}
    d = dict(MESSAGE_ID="SINT-A-0001", ORIGINATOR="OPERADOR_SINTETICO_A", CREATION_DATE="2026-11-11T00:00:00",
             TCA="2026-11-12T03:04:05.000", OBJECT1="SINT-90001", OBJECT2="SINT-90002",
             MISS_DISTANCE=350.0, RELATIVE_SPEED=14000.0, COLLISION_PROBABILITY=2.88e-4)
    v["texto"] = serializar(d)
    v["ida_vuelta"] = analizar(v["texto"]) == d
    # el mismo evento en km (otro operador): tras convertir debe coincidir
    otro = v["texto"].replace("MISS_DISTANCE = 350.0 [m]", "MISS_DISTANCE = 0.35 [km]").replace("RELATIVE_SPEED = 14000.0 [m/s]", "RELATIVE_SPEED = 14.0 [km/s]")
    v["conv_ok"] = analizar(otro)
    v["dis_km"] = reconciliar(analizar(v["texto"]), v["conv_ok"])
    # un operador que escribe 350 en 'km' por error
    malo = v["texto"].replace("MISS_DISTANCE = 350.0 [m]", "MISS_DISTANCE = 350.0 [km]")
    v["dis_malo"] = reconciliar(analizar(v["texto"]), analizar(malo))
    errores = []
    for t in (v["texto"].replace(" [m]", "", 1), v["texto"].replace("[m/s]", "[mph]"), v["texto"] + "TCA = x\n",
              v["texto"].replace("ORIGINATOR", "ORIGEN"), "MESSAGE_ID SINT"):
        try:
            analizar(t)
            errores.append("aceptado")
        except ValueError as e:
            errores.append(str(e))
    v["errores"] = errores
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Mensaje SINTETICO tipo clave = valor [unidad], inspirado en KVN pero NO conforme a CCSDS 508.0-B-1 (solo se consulto su ficha).")
    v = compute()
    print(v["texto"], end="")
    print(f"Ida y vuelta exacta: {v['ida_vuelta']}")
    print(f"Mismo evento en km (0.35 km, 14 km/s): discrepancias tras convertir a SI: {v['dis_km']}")
    print(f"Operador que escribe 350 [km] por error: {len(v['dis_malo'])} discrepancia(s): " +
          "; ".join(f"{k} {a:.4g} vs {b:.4g}" for k, a, b, r in v["dis_malo"]))
    for e in v["errores"]:
        print(f"  rechazo: {e}")
    assert v["ida_vuelta"] and v["dis_km"] == []
    assert len(v["dis_malo"]) == 1
    assert all(e != "aceptado" for e in v["errores"])
    print("Pruebas superadas (ida y vuelta, conversion de unidades, deteccion de unidad erronea, 5 rechazos).")


if __name__ == "__main__":
    main()
