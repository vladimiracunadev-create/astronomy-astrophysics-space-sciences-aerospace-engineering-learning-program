#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C22: informe de navegacion verificable (procedencia, huellas SHA-256, completitud y reproducibilidad).

Todo SINTETICO: se generan en un directorio temporal dos archivos de entrada (observaciones de alcance de 4 estaciones sinteticas y una lista de estaciones, semilla 71),
se resuelve una posicion por minimos cuadrados (Gauss-Newton), y se produce un informe en JSON con: identificador, sistema de referencia, escala de tiempo, unidades,
versiones (Python, NumPy), semilla, huellas SHA-256 de las entradas, estado estimado con covarianza y metricas. Un verificador independiente comprueba:
(1) campos obligatorios presentes y con unidades; (2) huellas de las entradas recalculadas; (3) covarianza simetrica y definida positiva; (4) reproducibilidad (se recalcula el
estado desde las entradas y debe coincidir dentro de 1e-6 m); (5) deteccion de manipulacion: se altera un byte de una entrada y el verificador debe fallar en la huella.
SHA-256 es el algoritmo estandar (hashlib de Python; no se consulto una norma). Tolerancias: reproducibilidad 1e-6 m.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import hashlib, json, math, os, platform, sys, tempfile
import numpy as np

CAMPOS = ["id_informe", "sistema_de_referencia", "escala_de_tiempo", "unidades", "versiones", "semilla", "entradas", "estado", "covarianza", "metricas", "limites"]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def resuelve(est, rho):
    x = np.mean(est, axis=0) * 0.0 + np.array([1.0e6, 2.0e6, 3.0e6])  # inicio fijo
    for _ in range(10):
        d = x - est
        r = np.linalg.norm(d, axis=1)
        H = d / r[:, None]
        dx = np.linalg.lstsq(H, rho - r, rcond=None)[0]
        x = x + dx
    P = np.linalg.inv(H.T @ H) * 1.0**2
    return x, P


def lee_entradas(base):
    est = np.loadtxt(os.path.join(base, "estaciones.csv"), delimiter=",")
    rho = np.loadtxt(os.path.join(base, "alcances.csv"), delimiter=",")
    return est, rho


def verifica(inf, base):
    fallos = []
    for c in CAMPOS:
        if c not in inf:
            fallos.append(f"falta el campo {c}")
    if fallos:
        return fallos
    for k in ("posicion", "covarianza"):
        if k not in inf["unidades"]:
            fallos.append(f"falta la unidad de {k}")
    for nom, h in inf["entradas"].items():
        if sha(os.path.join(base, nom)) != h:
            fallos.append(f"huella distinta en {nom}")
    P = np.array(inf["covarianza"])
    if np.max(np.abs(P - P.T)) > 1e-9 * np.max(np.abs(P)) or np.min(np.linalg.eigvalsh((P + P.T) / 2)) <= 0:
        fallos.append("covarianza no valida")
    if not fallos:
        est, rho = lee_entradas(base)
        x, _ = resuelve(est, rho)
        if np.linalg.norm(x - np.array(inf["estado"])) > 1e-6:
            fallos.append("no reproducible")
    return fallos


def main():
    rng = np.random.default_rng(71)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (datos SINTETICOS, semilla 71)"]
    res = {}
    est = np.array([[6.4e6, 0, 0], [0, 6.4e6, 0], [0, 0, 6.4e6], [-4.5e6, -4.5e6, 0]])
    x_true = np.array([1.2e7, 8.0e6, 6.0e6])
    rho = np.linalg.norm(x_true - est, axis=1) + rng.normal(0, 1.0, 4)
    with tempfile.TemporaryDirectory() as base:
        np.savetxt(os.path.join(base, "estaciones.csv"), est, delimiter=",", fmt="%.6f")
        np.savetxt(os.path.join(base, "alcances.csv"), rho, delimiter=",", fmt="%.6f")
        e2, r2 = lee_entradas(base)
        x, P = resuelve(e2, r2)
        informe = {
            "id_informe": "B74-C22-demo-sintetico",
            "sistema_de_referencia": "marco terrestre fijo simplificado (SINTETICO)",
            "escala_de_tiempo": "no aplica (alcances simultaneos sinteticos)",
            "unidades": {"posicion": "m", "covarianza": "m^2", "alcance": "m"},
            "versiones": {"python": platform.python_version(), "numpy": np.__version__},
            "semilla": 71,
            "entradas": {n: sha(os.path.join(base, n)) for n in ("estaciones.csv", "alcances.csv")},
            "estado": [float(v) for v in x],
            "covarianza": [[float(v) for v in f] for f in P],
            "metricas": {"error_vs_verdad_sintetica_m": float(np.linalg.norm(x - x_true)), "sigma_3d_formal_m": float(math.sqrt(np.trace(P)))},
            "limites": "datos sinteticos; sin troposfera, sesgos ni relatividad; no describe ninguna nave real",
        }
        texto = json.dumps(informe, indent=1, sort_keys=True)
        out.append(f"Informe: {len(texto)} bytes ; campos = {len(informe)} ; huella de estaciones.csv = {informe['entradas']['estaciones.csv'][:16]}...; huella de alcances.csv = {informe['entradas']['alcances.csv'][:16]}...")
        out.append(f"Estado = ({x[0]:.3f}, {x[1]:.3f}, {x[2]:.3f}) m ; error frente a la verdad sintetica = {informe['metricas']['error_vs_verdad_sintetica_m']:.3f} m ; sigma 3D formal = {informe['metricas']['sigma_3d_formal_m']:.3f} m")
        f_ok = verifica(informe, base)
        out.append(f"Verificacion del informe integro: {'APROBADA' if not f_ok else 'FALLA ' + str(f_ok)}")
        # manipulacion
        p = os.path.join(base, "alcances.csv")
        b = bytearray(open(p, "rb").read()); b[0] = ord("9") if b[0] != ord("9") else ord("1")
        open(p, "wb").write(bytes(b))
        f_t = verifica(informe, base)
        out.append(f"Verificacion tras alterar un byte de alcances.csv: {'APROBADA (inesperado)' if not f_t else 'RECHAZADA: ' + '; '.join(f_t)}")
        # informe incompleto
        inc = dict(informe); del inc["sistema_de_referencia"]
        f_i = verifica(inc, base)
        out.append(f"Verificacion de un informe sin sistema de referencia: {'APROBADA (inesperado)' if not f_i else 'RECHAZADA: ' + '; '.join(f_i)}")
        res.update(bytes=len(texto), campos=len(informe), err=informe["metricas"]["error_vs_verdad_sintetica_m"], sig=informe["metricas"]["sigma_3d_formal_m"],
                   h1=informe["entradas"]["estaciones.csv"][:12], h2=informe["entradas"]["alcances.csv"][:12], ok_int=int(not f_ok), ok_man=int(bool(f_t)), ok_inc=int(bool(f_i)))
        ok = (not f_ok) and bool(f_t) and bool(f_i)
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
