#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C07: trazabilidad de una cifra (código, datos, parámetros, versión).

Datos: horizons_tierra.csv, EFEMÉRIDE oficial (NASA/JPL Horizons, DE441), la misma de B23-C05.
Cifra trazada: error de posición (au) de un modelo de dos cuerpos frente a la efeméride a +91 d.
Modelo: dos cuerpos, Sol fijo, mu = GM_sol nominal IAU 2015 B3, 1 au = 149597870700 m,
integración DOP853 con rtol dada.
Supuestos: los de B23-C05. Validez: solo para esta cifra; el script demuestra el REGISTRO,
no el modelo.
Tolerancia de reproducción: una cifra se acepta «dentro de tolerancia» si coincide a 1e-9 relativo;
«bit a bit» si el valor es idéntico.
Huella: SHA-256 del JSON canónico de {datos, código, parámetros, versiones, valor}; la fecha de
ejecución NO entra (se registra aparte). Los archivos se normalizan a fin de línea LF antes de
calcular su hash, para que no dependa del sistema operativo.
"""
from __future__ import annotations
import csv, hashlib, json, platform, subprocess, sys, datetime
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp

AQUI = Path(__file__).resolve().parent
AU = 149597870700.0
MU = 1.3271244e20*86400.0**2/AU**3


def sha256_normalizado(ruta: Path) -> str:
    datos = ruta.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(datos).hexdigest()


def leer_datos(ruta: Path):
    with ruta.open(encoding="utf-8", newline="") as f:
        filas = [l for l in f if not l.startswith("#")]
    return np.array([[float(x) for x in fila] for fila in list(csv.reader(filas))[1:]])


def calcular(ruta_datos: Path, rtol: float, indice: int = 1) -> float:
    D = leer_datos(ruta_datos)
    r0, v0 = D[0, 1:4], D[0, 4:7]

    def f(t, y):
        return np.concatenate([y[3:], -MU*y[:3]/np.linalg.norm(y[:3])**3])
    dt = D[indice, 0] - D[0, 0]
    s = solve_ivp(f, (0, dt), np.concatenate([r0, v0]), method="DOP853", rtol=rtol, atol=1e-14)
    return float(np.linalg.norm(s.y[:3, -1] - D[indice, 1:4]))


def commit_git():
    try:
        out = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=AQUI, capture_output=True,
                             text=True, timeout=10)
        return out.stdout.strip() or "no disponible"
    except Exception:
        return "no disponible"


def huella(nucleo: dict) -> str:
    canon = json.dumps(nucleo, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def registrar(ruta_datos: Path, rtol: float = 1e-12) -> dict:
    valor = calcular(ruta_datos, rtol)
    nucleo = {
        "cifra": "error_posicion_91d_au",
        "valor": valor,
        "unidad": "au",
        "parametros": {"rtol": rtol, "mu_au3_d2": MU, "indice_epoca": 1},
        "datos": {"archivo": ruta_datos.name, "sha256": sha256_normalizado(ruta_datos),
                  "tipo": "efemeride (modelo DE441)"},
        "codigo": {"archivo": Path(__file__).name, "sha256": sha256_normalizado(Path(__file__))},
        "versiones": {"python": platform.python_version(), "numpy": np.__version__,
                      "scipy": scipy.__version__},
    }
    ahora = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return {"nucleo": nucleo, "huella": huella(nucleo),
            "contexto": {"commit_git": commit_git(), "plataforma": platform.system(),
                         "ejecutado_utc": ahora}}


def verificar(reg: dict, ruta_datos: Path, tol_rel: float = 1e-9) -> dict:
    """Reconstruye lo que puede y dice qué cambió y si la cifra se reproduce."""
    n = reg["nucleo"]
    cambios = []
    if sha256_normalizado(ruta_datos) != n["datos"]["sha256"]:
        cambios.append("datos")
    if sha256_normalizado(Path(__file__)) != n["codigo"]["sha256"]:
        cambios.append("código")
    v_act = {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}
    if v_act != n["versiones"]:
        cambios.append("versiones")
    valor = calcular(ruta_datos, n["parametros"]["rtol"], n["parametros"]["indice_epoca"])
    if valor == n["valor"]:
        estado = "reproducida bit a bit"
    elif abs(valor - n["valor"]) <= tol_rel*abs(n["valor"]):
        estado = "reproducida dentro de tolerancia"
    else:
        estado = "NO reproducida"
    return {"estado": estado, "cambios_detectados": cambios, "valor_nuevo": valor}


def citar(reg: dict) -> str:
    n = reg["nucleo"]
    return (f"{n['valor']:.3e} {n['unidad']} [reg:{reg['huella'][:12]}; "
            f"datos:{n['datos']['sha256'][:8]}; código:{n['codigo']['sha256'][:8]}]")


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    datos = AQUI/"horizons_tierra.csv"
    reg = registrar(datos)
    n = reg["nucleo"]
    print(f"cifra: {citar(reg)}")
    print(f"huella completa: {reg['huella']}")
    print(f"commit git: {reg['contexto']['commit_git']}  plataforma: {reg['contexto']['plataforma']}")

    # 1. Reproducción: misma entrada, misma huella y mismo valor
    reg2 = registrar(datos)
    prueba(reg2["huella"] == reg["huella"], "la huella no depende de la fecha de ejecución")
    prueba(reg2["nucleo"]["valor"] == n["valor"], "el cálculo es determinista (bit a bit)")
    print("reproducción: misma huella y mismo valor bit a bit (la fecha UTC no entra en la huella)")

    # 2. Round-trip JSON del registro
    texto = json.dumps(reg, sort_keys=True)
    prueba(json.loads(texto)["nucleo"]["valor"] == n["valor"], "el valor sobrevive a JSON sin pérdida")
    v = verificar(json.loads(texto), datos)
    print(f"verificación del registro guardado: {v['estado']}; cambios: {v['cambios_detectados'] or 'ninguno'}")
    prueba(v["estado"] == "reproducida bit a bit" and not v["cambios_detectados"], "verificación limpia")

    # 3. Cambiar UN dígito de los datos: la huella y la verificación lo delatan
    tmp = AQUI/"_horizons_alterado.csv"
    try:
        contenido = datos.read_bytes()
        tmp.write_bytes(contenido.replace(b"9.669827953774551E-01", b"9.669827953774552E-01", 1))
        v2 = verificar(json.loads(texto), tmp)
        r3 = registrar(tmp)
    finally:
        tmp.unlink(missing_ok=True)
    print(f"un dígito alterado en los datos: cambios={v2['cambios_detectados']}; estado={v2['estado']}; "
          f"huella distinta: {r3['huella'] != reg['huella']}")
    prueba("datos" in v2["cambios_detectados"] and r3["huella"] != reg["huella"], "el cambio de datos se detecta")

    # 4. Cambiar un parámetro numérico
    r4 = registrar(datos, rtol=1e-10)
    dif = abs(r4["nucleo"]["valor"] - n["valor"])/n["valor"]
    print(f"rtol 1e-12 -> 1e-10: huella distinta: {r4['huella'] != reg['huella']}; "
          f"diferencia relativa de la cifra: {dif:.1e}")
    prueba(r4["huella"] != reg["huella"], "un parámetro distinto cambia la huella")

    # 5. Fin de línea CRLF no cambia el hash normalizado
    tmp2 = AQUI/"_horizons_crlf.csv"
    try:
        tmp2.write_bytes(datos.read_bytes().replace(b"\n", b"\r\n"))
        igual = sha256_normalizado(tmp2) == sha256_normalizado(datos)
        crudo = hashlib.sha256(tmp2.read_bytes()).hexdigest() == hashlib.sha256(datos.read_bytes()).hexdigest()
    finally:
        tmp2.unlink(missing_ok=True)
    print(f"CRLF vs LF: hash normalizado igual={igual}; hash crudo igual={crudo}")
    prueba(igual and not crudo, "la normalización evita falsas alarmas por fin de línea")

    # 6. Versión alterada: se informa
    reg_viejo = json.loads(texto)
    reg_viejo["nucleo"]["versiones"]["numpy"] = "0.0.0"
    v6 = verificar(reg_viejo, datos)
    print(f"registro con otra versión de NumPy: cambios={v6['cambios_detectados']}; estado={v6['estado']}")
    prueba("versiones" in v6["cambios_detectados"], "el cambio de versión se informa")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
