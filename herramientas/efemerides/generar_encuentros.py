# SPDX-License-Identifier: Apache-2.0
"""Genera simuladores/datos/encuentros.json: los sobrevuelos, asistencias gravitatorias e inserciones en órbita de las naves del simulador de misiones.

1. Detección: mínimos de la distancia nave–planeta DENTRO de la esfera de influencia del planeta (tablas heliocéntricas de `misiones`).
2. Precisión: el instante y la distancia del mayor acercamiento y la trayectoria planetocéntrica salen de JPL Horizons con centro en el
   planeta (paso de 5 a 20 min y 2×36 épocas con espaciado geométrico, denso cerca del acercamiento), no de las tablas de 1–3 días.
3. Asistencia: velocidad heliocéntrica al entrar y al salir de la esfera de influencia (método de las cónicas empalmadas) y desvío.
Uso: python -X utf8 herramientas/efemerides/generar_encuentros.py
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horizons as H  # noqa: E402
import lectura as L  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "simuladores" / "datos" / "encuentros.json"
# esfera de influencia a·(m/M☉)^(2/5) [km]; GM [km³/s²]; radio ecuatorial [km]
SOI = {"199": 1.12e5, "299": 6.16e5, "399": 9.25e5, "499": 5.77e5, "599": 4.82e7, "699": 5.45e7, "799": 5.18e7, "899": 8.68e7, "9": 3.1e6}
GM = {"199": 22031.86, "299": 324858.59, "399": 398600.44, "499": 42828.37, "599": 126686534.0, "699": 37931207.0, "799": 5793951.0, "899": 6835100.0, "9": 869.6}
RADIO = {"199": 2439.4, "299": 6051.8, "399": 6378.137, "499": 3396.19, "599": 71492.0, "699": 60268.0, "799": 25559.0, "899": 24764.0, "9": 1188.3}
CENTRO = {"199": "500@199", "299": "500@299", "399": "500@399", "499": "500@499", "599": "500@599", "699": "500@699", "799": "500@799", "899": "500@899", "9": "500@999"}
NOMBRE = {"199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno", "9": "Plutón"}
N_LADO = 36


def norma(v) -> float:
    return float(math.sqrt(sum(x * x for x in v)))


def resta(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vel(c, jd: float, h: float = 0.05):
    a, b = c.pos(jd - h), c.pos(jd + h)
    k = 1 / (2 * h * 86400)
    return ((b[0] - a[0]) * k, (b[1] - a[1]) * k, (b[2] - a[2]) * k)


def candidatos(nave, planeta, pid: str) -> list[float]:
    """Mínimos locales de la distancia (día juliano TDB aproximado) dentro de la esfera de influencia; un orbitador sólo conserva la llegada."""
    h = nave.h
    ini = max(nave.meta["jd_valido_ini"], planeta.meta["jd_valido_ini"])
    fin = min(nave.meta["jd_valido_fin"], planeta.meta["jd_valido_fin"])
    if pid == "9" and not ini < 2470000:
        return []
    f = lambda jd: norma(resta(nave.pos(jd), planeta.pos(jd)))  # noqa: E731
    out = []
    d0, d1 = f(ini), f(ini + h)
    jd = ini + h
    while jd < fin - h:
        d2 = f(jd + h)
        if d1 < d0 and d1 <= d2 and d1 < SOI[pid] + h * 86400 * 25:   # un sobrevuelo rápido puede caer entre dos muestras
            out.append(jd)
        d0, d1 = d1, d2
        jd += h
    return out


def refinar(nid: str, pid: str, jd0: float, h: float):
    """Instante y distancia mínimos con Horizons (centro en el planeta)."""
    w = 1.5 * h + 1.0
    paso = max(5, math.ceil(2 * w * 1440 / 1500))
    cab, filas = H.vectores(nid, CENTRO[pid], f"JD {jd0 - w:.5f}", f"JD {jd0 + w:.5f}", f"{paso} m", tabla="2")
    a = np.array(filas)
    d = np.linalg.norm(a[:, 1:4], axis=1)
    i = int(np.argmin(d))
    i = min(max(i, 1), len(d) - 2)
    den = d[i - 1] - 2 * d[i] + d[i + 1]
    off = 0.5 * (d[i - 1] - d[i + 1]) / den if den else 0.0
    jd_ca = a[i, 0] + off * (a[i + 1, 0] - a[i, 0])
    # velocidad relativa interpolada
    v = np.linalg.norm(a[i, 4:7])
    return float(jd_ca), float(d[i] - 0.25 * (d[i - 1] - d[i + 1]) * off), float(v)


def cruces_soi(nave, planeta, pid: str, jd_ca: float):
    """Entrada y salida de la esfera de influencia (de las tablas). `orbita` es verdadero si la nave sigue dentro 150 d después (queda en órbita);
    entonces `salida_real` es el instante en que por fin sale (o el final de los datos)."""
    ini = max(nave.meta["jd_valido_ini"], planeta.meta["jd_valido_ini"])
    fin = min(nave.meta["jd_valido_fin"], planeta.meta["jd_valido_fin"])
    f = lambda jd: norma(resta(nave.pos(jd), planeta.pos(jd))) - SOI[pid]  # noqa: E731

    def barrer(sent: int, lim: float):
        t = jd_ca
        while abs(t - jd_ca) < lim and ini < t < fin:
            if f(t) > 0:
                a, b = sorted((t, t - sent * nave.h))
                for _ in range(40):
                    m = (a + b) / 2
                    if (f(m) > 0) == (f(a) > 0):
                        a = m
                    else:
                        b = m
                return (a + b) / 2, True
            t += sent * nave.h
        return t, False
    ent, _ = barrer(-1, 200.0)
    sal, salio = barrer(1, 150.0)
    if salio:
        return ent, sal, False, sal
    real, _ = barrer(1, 1e5)
    return ent, sal, True, real


def main() -> None:
    mis, ph = L.Sistema("misiones"), L.Sistema("planetas_hist")
    enc = []
    for nid, nave in mis.cuerpos.items():
        for pid in SOI:
            hasta = -1.0
            for jd_aprox in candidatos(nave, ph.cuerpos[pid], pid):
                if jd_aprox < hasta:
                    continue          # pericentro de una órbita ya registrada
                jd_ca, d_ca, v_ca = refinar(nid, pid, jd_aprox, nave.h)
                if d_ca >= SOI[pid]:
                    continue
                ent, sal, orbita, real = cruces_soi(nave, ph.cuerpos[pid], pid, jd_ca)
                if orbita:
                    hasta = real
                    sal = jd_ca + 0.3          # tras el periastro la nave queda en una órbita cerrada que no se muestrea en el detalle
                # trayectoria planetocéntrica: 2·N épocas con espaciado geométrico
                dmin = 0.002
                lado = lambda T: [dmin * (T / dmin) ** (k / N_LADO) for k in range(1, N_LADO + 1)]  # noqa: E731
                dts = sorted([-x for x in lado(max(dmin * 4, jd_ca - ent))] + [0.0] + lado(max(dmin * 4, sal - jd_ca)))
                jds = [jd_ca + x for x in dts]
                filas = []
                for k in range(0, len(jds), 40):
                    filas += H.vectores_lista(nid, CENTRO[pid], jds[k:k + 40], tabla="2")
                traza = [[round(r[0] - jd_ca, 6), round(r[1]), round(r[2]), round(r[3]), round(r[4], 4), round(r[5], 4), round(r[6], 4)] for r in filas]
                e = {"nave": nid, "nombre": nave.nombre, "planeta": pid, "jd_ca": round(jd_ca, 6), "dist_km": round(d_ca, 1), "alt_km": round(d_ca - RADIO[pid], 1),
                     "vrel_kms": round(v_ca, 3), "jd_in": round(ent, 4), "jd_out": round(sal, 4), "orbita": bool(orbita), "traza": traza}
                # estado en el mayor acercamiento (época dt = 0) y elementos de la hipérbola
                r0 = next(t for t in traza if abs(t[0]) < 1e-9)
                r = np.array(r0[1:4], float); v = np.array(r0[4:7], float); mu = GM[pid]
                h = np.cross(r, v); ev = np.cross(v, h) / mu - r / np.linalg.norm(r); ecc = float(np.linalg.norm(ev))
                e["excentricidad"] = round(ecc, 4)
                if ecc <= 1.0:
                    e["orbita"] = orbita = True     # capturada: elipse alrededor del planeta
                else:
                    # la distancia mínima exacta sale de la hipérbola del estado (el ajuste parabólico de una malla de minutos se desvía en los pasos rápidos y bajos)
                    a_h = mu / (float(v @ v) - 2 * mu / float(np.linalg.norm(r)))     # |a| = μ/v∞²; el periastro es |a|·(e − 1)
                    rp = a_h * (ecc - 1.0)
                    e["dist_km"] = round(rp, 1); e["alt_km"] = round(rp - RADIO[pid], 1); e["vrel_kms"] = round(math.sqrt(float(v @ v) - 2 * mu / float(np.linalg.norm(r)) + 2 * mu / rp), 3)
                if ecc > 1.0 and not orbita:
                    ph_, hh = ev / ecc, h / np.linalg.norm(h)
                    qh = np.cross(hh, ph_); th = math.acos(-1 / ecc); k = mu / np.linalg.norm(h)
                    v_out = k * (-math.sin(th) * ph_ + (ecc - 1 / ecc) * qh); v_in = k * (math.sin(th) * ph_ + (ecc - 1 / ecc) * qh)
                    vp = np.array(vel(ph.cuerpos[pid], jd_ca))
                    vh_in, vh_out = float(np.linalg.norm(vp + v_in)), float(np.linalg.norm(vp + v_out))
                    e.update({"vinf_kms": round(float(np.linalg.norm(v_in)), 3), "vh_in": round(vh_in, 3), "vh_out": round(vh_out, 3), "dv_helio": round(vh_out - vh_in, 3),
                              "desvio_deg": round(math.degrees(math.acos(max(-1.0, min(1.0, float(v_in @ v_out) / float(np.linalg.norm(v_in) * np.linalg.norm(v_out)))))), 2)})
                enc.append(e)
                print(f"  {nave.nombre} · {NOMBRE[pid]}: {e['jd_ca']:.3f} d={d_ca:.0f} km alt={e['alt_km']:.0f}" + (" (órbita)" if orbita else f" v∞={e.get('vinf_kms')} Δv={e.get('dv_helio')} desvío {e.get('desvio_deg')}°"))
    enc.sort(key=lambda e: e["jd_ca"])
    meta = {"fuente": "NASA/JPL Horizons (SPICE): vectores planetocéntricos de las naves; esfera de influencia a·(m/M☉)^0,4", "unidades": "km, km/s, días TDB; ejes eclíptica J2000",
            "radio_km": RADIO, "gm_km3_s2": GM, "soi_km": SOI, "encuentros": enc}
    SALIDA.write_text(json.dumps(meta, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(enc), "encuentros;", round(SALIDA.stat().st_size / 1024), "KB")


if __name__ == "__main__":
    main()
