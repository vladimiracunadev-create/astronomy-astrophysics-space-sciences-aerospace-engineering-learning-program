# SPDX-License-Identifier: Apache-2.0
"""Genera las efemérides oficiales de los simuladores a partir de NASA/JPL Horizons (2027-01-01 a 2050-12-31).

Qué hace
  1. Lee de Horizons la lista de cuerpos mayores y selecciona los satélites de Marte, Júpiter, Saturno, Urano y Neptuno
     (los números 4xx-8xx más las designaciones provisionales 55xxx, 65xxx, 75xxx y 85xxx) y la Luna.
  2. Descarga posiciones geométricas (eclíptica y equinoccio J2000, ICRF, km, TDB) centradas en el planeta
     (o en el Sol para los planetas) con un paso regular elegido según la frecuencia orbital de cada cuerpo.
  3. Empaqueta cada sistema en `simuladores/datos/<sistema>.bin` + `<sistema>.json` (binario little-endian).
  4. Mide el error de interpolación contra consultas de Horizons en épocas que NO son nodos de la tabla y lo guarda en
     `simuladores/datos/verificacion.json` (lo usa `pruebas/` para reproducirlo en JavaScript sin red).

Uso (necesita red y numpy; la caché evita repetir descargas):
    python herramientas/efemerides/generar_efemerides.py            # todo
    python herramientas/efemerides/generar_efemerides.py --plan     # sólo el plan de tamaños, sin descargar tablas

Interpolación (idéntica en Python y en `simuladores/motor/efemerides.js`): Lagrange de 10 puntos sobre nodos equiespaciados.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horizons as H  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "simuladores" / "datos"

JD_INI = 2461406.5     # 2027-01-01 00:00 TDB
JD_FIN = 2470172.5     # 2051-01-01 00:00 TDB
NODOS = 10             # puntos de Lagrange (4 antes y 5 después del intervalo)
FILAS_POR_PETICION = 40000
N_VERIF = 120          # épocas de verificación por cuerpo

# GM [km^3/s^2] (DE440 / JPL SSD) para estimar periodos orbitales al planificar la tabla
GM = {"399": 398600.435, "499": 42828.375, "599": 126686534.9, "699": 37931207.8, "799": 5793951.3, "899": 6835099.5}

SISTEMAS = {  # clave: (id del planeta, nombre, filtro de ids de satélites)
    "tierra": ("399", "Tierra", lambda i: i == 301),
    "marte": ("499", "Marte", lambda i: i in (401, 402)),
    "jupiter": ("599", "Júpiter", lambda i: 501 <= i <= 598 or 55000 < i < 56000),
    "saturno": ("699", "Saturno", lambda i: 601 <= i <= 698 or 65000 < i < 66000),
    "urano": ("799", "Urano", lambda i: 701 <= i <= 798 or 75000 < i < 76000),
    "neptuno": ("899", "Neptuno", lambda i: 801 <= i <= 898 or 85000 < i < 86000),
}

# Planetas heliocéntricos: (id Horizons, nombre, paso en minutos)
PLANETAS = [
    ("199", "Mercurio", 1440), ("299", "Venus", 2880), ("399", "Tierra", 1440), ("499", "Marte", 2880),
    ("599", "Júpiter", 5760), ("699", "Saturno", 5760), ("799", "Urano", 5760), ("899", "Neptuno", 5760),
    ("9", "Plutón (baricentro del sistema)", 5760), ("2000001", "Ceres", 2880),
]


def lista_cuerpos_mayores() -> list[tuple[int, str, str]]:
    t = H.consulta({"COMMAND": "MB"})
    filas = []
    for l in t.splitlines():
        m = re.match(r"\s+(\d+)\s{2}(.{34})\s(.{11})\s(.*)$", l)
        if m:
            filas.append((int(m[1]), m[2].strip(), m[3].strip()))
    return filas


def catalogo_satelites() -> list[dict]:
    mb = lista_cuerpos_mayores()
    pedidos = []
    for sk, (pid, pnom, filtro) in SISTEMAS.items():
        for (i, nom, desig) in mb:
            if filtro(i):
                pedidos.append((sk, pid, i, nom, desig))

    def estado(p):
        sk, pid, i, nom, desig = p
        try:
            cab, f = H.vectores(str(i), f"500@{pid}", "JD 2461406.5", "JD 2461406.6", "1m", obj_data=True)
        except Exception as e:  # noqa: BLE001
            return {"sistema": sk, "id": i, "nombre": nom or desig, "error": str(e)[:160]}
        x = np.array(f[0][1:4]); v = np.array(f[0][4:7]); mu = GM[pid]
        r = np.linalg.norm(x); a = 1 / (2 / r - v @ v / mu)
        h = np.cross(x, v); e = np.linalg.norm(np.cross(v, h) / mu - x / r)
        return {"sistema": sk, "id": i, "nombre": nom or desig.replace("_", " "), "designacion": desig, "a_km": float(a), "e": float(e),
                "periodo_d": float(2 * math.pi * math.sqrt(abs(a) ** 3 / mu) / 86400) if a > 0 else None,
                "radio_km": H.radio_medio(cab), "centro": pid}

    with ThreadPoolExecutor(4) as ex:
        return list(ex.map(estado, pedidos))


def planificar(c: dict) -> dict:
    """Elige formato y paso de la tabla. Principal (radio >= 190 km o Luna/lunas de Marte): nodos más densos y float32."""
    P = c["periodo_d"]
    principal = (c.get("radio_km") or 0) >= 190 or c["id"] == 301
    if c["id"] == 301:
        nh = 0.15      # la Luna: perturbaciones solares de alta frecuencia
    elif P >= 20 and not principal:
        nh = 0.25      # satélites irregulares: la marea solar añade términos de alta frecuencia; son baratos de tabular
    else:
        nh = 0.6 if principal else 1.0
    n_rad_d = 2 * math.pi / (P * 0.9)
    fe = (1 + c["e"]) ** 2 / (1 - c["e"] ** 2) ** 1.5 if c["e"] < 0.95 else 10.0
    h_d = min(30.0, nh / (n_rad_d * fe))
    h_min = max(5, int(h_d * 1440))
    n_filas = int(math.ceil((JD_FIN - JD_INI) / (h_min / 1440))) + 2 * NODOS + 2
    fmt = "i16" if (not principal and P < 5.0) else "f32"
    c.update({"paso_min": h_min, "nodos_orbita": nh, "fmt": fmt, "n": n_filas,
              "bytes": n_filas * 3 * (2 if fmt == "i16" else 4), "principal": bool(principal)})
    return c


MESES = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def _jd_de_texto(m: re.Match) -> float:
    y, mes, d, hh, mm, ss = int(m[2]), MESES[m[3]], int(m[4]), int(m[5]), int(m[6]), int(m[7])
    a = (14 - mes) // 12; yy = y + 4800 - a; mm_ = mes + 12 * a - 3
    jdn = d + (153 * mm_ + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
    return jdn - 0.5 + (hh + mm / 60 + ss / 3600) / 24


LIMITE = re.compile(r"(after|prior to) A\.D\. (\d{4})-([A-Z]{3})-(\d{2}) (\d{2}):(\d{2}):(\d{2})")


def descargar(cuerpo: str, centro: str, paso_min: int, n: int):
    """Devuelve (tabla[n,3], t0, jd_min, jd_max). Si Horizons no tiene efemérides en todo el intervalo, recorta la tabla
    al tramo disponible (guardando los límites) en lugar de inventar datos."""
    h_d = paso_min / 1440
    base = JD_INI - (NODOS // 2 + 1) * h_d
    k0, k1 = 0, n  # índices [k0, k1) de la rejilla base
    jd_min, jd_max = -1e99, 1e99
    for _ in range(4):
        filas = []
        k = k0
        try:
            while k < k1:
                m = min(FILAS_POR_PETICION, k1 - k)
                ini = base + k * h_d
                fin = ini + (m - 1) * h_d + h_d * 0.01
                _, f = H.vectores(cuerpo, centro, f"JD {ini:.9f}", f"JD {fin:.9f}", f"{paso_min}m", tabla="1")
                if len(f) != m:
                    raise RuntimeError(f"{cuerpo}: se esperaban {m} filas y llegaron {len(f)}")
                if abs(f[0][0] - ini) > 1e-6:
                    raise RuntimeError(f"{cuerpo}: época inicial {f[0][0]} != {ini}")
                filas += [r[1:4] for r in f]
                k += m
            return np.array(filas, dtype=np.float64), base + k0 * h_d, jd_min, jd_max
        except RuntimeError as e:
            m = LIMITE.search(str(e))
            if not m:
                raise
            lim = _jd_de_texto(m)
            if m[1] == "after":
                jd_max = lim
                k1 = min(k1, int(math.floor((lim - base) / h_d)))
            else:
                jd_min = lim
                k0 = max(k0, int(math.ceil((lim - base) / h_d)))
    raise RuntimeError(f"{cuerpo}: no se pudo acotar el intervalo")


def lagrange(tab: np.ndarray, t0: float, h_d: float, jd: float) -> np.ndarray:
    """Misma fórmula que el motor JavaScript."""
    s = (jd - t0) / h_d
    i = int(math.floor(s)); u = s - i
    js = np.arange(-(NODOS // 2 - 1), NODOS // 2 + 1)  # -4..5
    w = np.empty(len(js))
    for a, j in enumerate(js):
        num = 1.0; den = 1.0
        for m in js:
            if m != j:
                num *= (u - m); den *= (j - m)
        w[a] = num / den
    return w @ tab[i + js]


def cuantizar(arr: np.ndarray, fmt: str):
    if fmt == "f64":
        return arr.astype("<f8"), 1.0
    if fmt == "f32":
        return arr.astype("<f4"), 1.0
    esc = float(np.max(np.abs(arr))) / 32760.0
    return np.round(arr / esc).astype("<i2"), esc


def desquantizar(q: np.ndarray, esc: float) -> np.ndarray:
    return q.astype(np.float64) * esc


def construir(plan_solo: bool, solo: list[str] | None = None) -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    cat = catalogo_satelites()
    sats = [planificar(c) for c in cat if "error" not in c]
    fallos = [c for c in cat if "error" in c]
    tot = sum(c["bytes"] for c in sats)
    print(f"satélites con efemérides: {len(sats)} · sin efemérides en Horizons: {[(f['id'], f['nombre']) for f in fallos]} · tamaño ≈ {tot / 1e6:.1f} MB")
    for sk in SISTEMAS:
        s = [c for c in sats if c["sistema"] == sk]
        print(f"  {sk:9s} {len(s):3d} lunas  {sum(c['bytes'] for c in s) / 1e6:6.2f} MB")
    if plan_solo:
        return

    rng = random.Random(2027)
    vf = SALIDA / "verificacion.json"
    verif = json.loads(vf.read_text(encoding="utf-8")) if vf.exists() else {}
    # ---- planetas (heliocéntricos, float64)
    sistemas_def = {"sol": {"centro": "10", "cuerpos": []}}
    bloques = {"sol": []}
    for (cid, nom, paso) in (PLANETAS if (not solo or "sol" in solo) else []):
        n = int(math.ceil((JD_FIN - JD_INI) / (paso / 1440))) + 2 * NODOS + 2
        tab, t0, jmin, jmax = descargar(cid, "500@10", paso, n)
        bloques["sol"].append({"id": cid, "nombre": nom, "paso_min": paso, "fmt": "f64", "n": len(tab), "t0": t0, "tab": tab})
    for sk, (pid, pnom, _) in SISTEMAS.items():
        if solo and sk not in solo:
            continue
        bloques[sk] = []
        for c in [c for c in sats if c["sistema"] == sk]:
            tab, t0, jmin, jmax = descargar(str(c["id"]), f"500@{pid}", c["paso_min"], c["n"])
            bloques[sk].append({**c, "id": str(c["id"]), "t0": t0, "tab": tab, "n": len(tab)})
        print("descargado", sk, len(bloques[sk]))

    centros = {"sol": "500@10", **{sk: f"500@{v[0]}" for sk, v in SISTEMAS.items()}}
    for sk, cuerpos in bloques.items():
        if not cuerpos:
            continue
        meta = {"sistema": sk, "centro_horizons": centros[sk], "marco": "Eclíptica y equinoccio J2000 (ICRF), geométrico",
                "unidades": "km", "escala_tiempo": "TDB", "nodos_lagrange": NODOS,
                "jd_inicio_soporte": JD_INI, "jd_fin_soporte": JD_FIN, "cuerpos": []}
        chunks = []; off = 0
        for c in cuerpos:
            q, esc = cuantizar(c["tab"], c["fmt"])
            b = q.tobytes()
            # verificación fuera de nodos
            h_d = c["paso_min"] / 1440
            lo = max(JD_INI + 1, c["t0"] + 6 * h_d); hi = min(JD_FIN - 1, c["t0"] + (c["n"] - 7) * h_d)
            jds = sorted(rng.uniform(lo, hi) for _ in range(N_VERIF))
            if c["fmt"] == "i16":
                tabq = desquantizar(q, esc)
            else:
                tabq = q.astype(np.float64)
            ref = []
            for k in range(0, len(jds), 60):
                ref += H.vectores_lista(c["id"], centros[sk], jds[k:k + 60], tabla="1")
            errs = []
            muestras = []
            for r in ref:
                p = lagrange(tabq, c["t0"], h_d, r[0])
                e = float(np.linalg.norm(p - np.array(r[1:4])))
                errs.append(e); muestras.append([r[0], r[1], r[2], r[3]])
            entrada = {k: v for k, v in c.items() if k not in ("tab", "bytes", "sistema")}
            entrada.update({"jd_valido_ini": c["t0"] + 5 * h_d, "jd_valido_fin": c["t0"] + (c["n"] - 6) * h_d, "offset": off, "longitud": len(b), "escala_i16": esc,
                            "error_max_km": round(max(errs), 4), "error_rms_km": round(float(np.sqrt(np.mean(np.square(errs)))), 4)})
            meta["cuerpos"].append(entrada)
            verif[f"{sk}/{c['id']}"] = {"nombre": c["nombre"], "epocas": muestras[:12], "error_max_km": entrada["error_max_km"]}
            chunks.append(b); off += len(b)
        (SALIDA / f"{sk}.bin").write_bytes(b"".join(chunks))
        (SALIDA / f"{sk}.json").write_text(json.dumps(meta, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        peor = max(meta["cuerpos"], key=lambda c: c["error_max_km"])
        print(f"{sk}: {off / 1e6:.2f} MB; peor error {peor['nombre']} {peor['error_max_km']} km")
    (SALIDA / "verificacion.json").write_text(json.dumps(verif, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--solo", help="lista separada por comas: sol,tierra,marte,jupiter,saturno,urano,neptuno")
    a = ap.parse_args()
    construir(a.plan, a.solo.split(",") if a.solo else None)
