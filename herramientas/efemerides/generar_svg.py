# SPDX-License-Identifier: Apache-2.0
"""Genera las figuras SVG de `simuladores/img/` a partir de las efemérides de `simuladores/datos/` (misma interpolación que el motor JS).

Cada figura es un esquema A ESCALA, visto desde el polo norte de la eclíptica, de una época fija. No son capturas: son
dibujos calculados con los datos oficiales, para el README y la documentación. Sólo se generan los sistemas cuyos datos existen.

Uso: python herramientas/efemerides/generar_svg.py [--check]
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lectura  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "simuladores" / "img"
W, H = 1200, 675
UA = 149597870.7
DELTA = 69.184 / 86400
JD_UTC_2027 = 2461406.5
FONDO, TEXTO, SUAVE, ACENTO = "#070a14", "#e6ecf8", "#9fb0cf", "#ffd45e"

RADIO_PLANETA = {"199": 2439.4, "299": 6051.8, "399": 6378.1366, "499": 3396.19, "599": 71492, "699": 60268, "799": 25559, "899": 24764, "9": 1188.3, "2000001": 469.7}
COLOR_PLANETA = {"199": "#a8a29e", "299": "#e6c88b", "399": "#3b82c4", "499": "#c8643c", "599": "#d8b48a", "699": "#e3cf9f", "799": "#9fd8e0", "899": "#4b70dd", "9": "#c9b79c", "2000001": "#9a948c"}
NOMBRE_PLANETA = {"199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno", "9": "Plutón", "2000001": "Ceres"}
PERIODO_PLANETA = {"199": 87.969, "299": 224.701, "399": 365.256, "499": 686.98, "599": 4332.59, "699": 10759.22, "799": 30688.5, "899": 60182, "9": 90560, "2000001": 1680}
COLOR_LUNA = {"301": "#cfcfc8", "401": "#8d8174", "402": "#a89a88", "501": "#e8d36a", "502": "#c9b79a", "503": "#9d9488", "504": "#6f685f", "505": "#a35c3c", "606": "#d9a441", "602": "#f1f3f5",
              "601": "#c8c4bd", "603": "#d7d3cc", "604": "#c3b9ae", "605": "#cdc6bb", "607": "#9a8f82", "608": "#6c6256", "701": "#b9b6b0", "702": "#7d7a76", "703": "#a8a5a0", "704": "#9b9893", "705": "#bdb8b0", "801": "#d9cfc6"}
ANILLOS = {
    "599": [(122500, 129000, 0.35), (129000, 226000, 0.1)],
    "699": [(74658, 92000, 0.3), (92000, 117580, 0.9), (122170, 136775, 0.65), (140180, 140280, 0.6)],
    "799": [(41837, 41840, 0.6), (42234, 42237, 0.6), (44718, 44724, 0.6), (45661, 45667, 0.6), (47627, 47631, 0.5), (50024, 50026, 0.4), (51149, 51159, 0.8)],
    "899": [(53200, 53250, 0.5), (62900, 62960, 0.6)],
}
# Sistemas: clave -> (id del planeta, título, radio del panel 1 [km], descripción del panel 1)
SISTEMAS = {
    "marte": ("499", "Marte y sus dos lunas", 25000, "Fobos y Deimos"),
    "jupiter": ("599", "Júpiter y sus lunas", 2.2e6, "lunas galileanas y Amaltea"),
    "saturno": ("699", "Saturno y sus lunas", 3.9e6, "Titán, Encélado, Jápeto y las demás lunas regulares"),
    "urano": ("799", "Urano y sus lunas", 6.4e5, "las cinco lunas mayores y las internas"),
    "neptuno": ("899", "Neptuno y sus lunas", 4.2e5, "Tritón y las lunas internas"),
}
ids_texto: list[str] = []


def f1(x: float) -> str:
    return f"{x:.1f}"


def jd_tdb(jd_utc: float) -> float:
    return jd_utc + DELTA


def formato_fecha(jd_utc: float) -> str:
    z = int(jd_utc + 0.5); fr = jd_utc + 0.5 - z
    a = z + 32044; b = (4 * a + 3) // 146097; c = a - 146097 * b // 4; d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    dia = e - (153 * m + 2) // 5 + 1; mes = m + 3 - 12 * (m // 10); anio = 100 * b + d - 4800 + m // 10
    h = int(fr * 24 + 1e-9); mi = int(round((fr * 24 - h) * 60))
    return f"{anio:04d}-{mes:02d}-{dia:02d} {h:02d}:{mi:02d} UTC"


def abrir(titulo: str, desc: str) -> list[str]:
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">',
            f'<title id="t">{escape(titulo)}</title>', f'<desc id="d">{escape(desc)}</desc>',
            f'<rect width="{W}" height="{H}" fill="{FONDO}"/>']


def texto(x, y, s, tam=14, color=TEXTO, ancla="start", peso="normal") -> str:
    s = re.sub(r"(\d)\.(\d)", r"\1,\2", s)  # coma decimal (español)
    ids_texto.append(s)
    return f'<text x="{f1(x)}" y="{f1(y)}" font-size="{tam}" fill="{color}" text-anchor="{ancla}" font-weight="{peso}">{escape(s)}</text>'


def encabezado(titulo: str, sub: str) -> list[str]:
    return [texto(32, 44, titulo, 28, TEXTO, peso="600"), texto(32, 70, sub, 14, SUAVE),
            texto(W - 32, H - 10, "Datos: NASA/JPL Horizons (DE441 y efemérides de satélites) · esquema a escala, vista desde el polo norte eclíptico", 11, SUAVE, "end")]


def barra_escala(x, y, km_por_px, etiqueta_km) -> list[str]:
    w = etiqueta_km / km_por_px
    return [f'<path d="M{f1(x)} {f1(y - 5)}V{f1(y)}H{f1(x + w)}V{f1(y - 5)}" fill="none" stroke="{TEXTO}" stroke-width="2"/>',
            texto(x, y - 10, f"{etiqueta_km:,.0f} km".replace(",", " ") if etiqueta_km < 1e7 else f"{etiqueta_km / UA:.2f} UA", 12, TEXTO)]


def elegir_escala(km: float, px: float) -> float:
    e = 10 ** math.floor(math.log10(km))
    for m in (5, 2, 1):
        if m * e / (km / px) <= px * 0.34:
            return m * e
    return e


def planeta_disco(cx, cy, r_km, km_px, color) -> str:
    return f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{max(1.5, r_km / km_px):.1f}" fill="{color}"/>'


def anillos(cx, cy, id_, km_px) -> list[str]:
    out = []
    for a, b, o in ANILLOS.get(id_, []):
        ra, rb = a / km_px, b / km_px
        if rb - ra < 0.8:
            out.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{(ra + rb) / 2:.1f}" fill="none" stroke="#e2cea0" stroke-opacity="{o}" stroke-width="1"/>')
        else:
            out.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{(ra + rb) / 2:.1f}" fill="none" stroke="#e2cea0" stroke-opacity="{o}" stroke-width="{rb - ra:.1f}"/>')
    return out


def trazar_orbita(c, jd0: float, cx, cy, km_px, clip) -> str | None:
    P = c.meta.get("periodo_d")
    if not P or P > 0.95 * (c.meta["jd_valido_fin"] - c.meta["jd_valido_ini"]):
        return None
    N = 90
    pts = []
    for i in range(N + 1):
        p = c.pos(jd0 - P / 2 + P * i / N)
        pts.append((cx + p[0] / km_px, cy - p[1] / km_px))
    return "M" + "L".join(f"{f1(x)} {f1(y)}" for x, y in pts)


def panel(sis, pid, centro, R_km, lado, jd0, nombre_panel, rotular, solo_regulares=None, orbitas=True):
    """Dibuja un panel cuadrado `lado` px con centro en `centro` y radio `R_km`."""
    cx, cy = centro
    km_px = R_km / (lado / 2 - 12)
    out = [f'<rect x="{f1(cx - lado / 2)}" y="{f1(cy - lado / 2)}" width="{lado}" height="{lado}" rx="10" fill="#0b1020" stroke="#26314f"/>',
           f'<clipPath id="cp{int(cx)}"><rect x="{f1(cx - lado / 2)}" y="{f1(cy - lado / 2)}" width="{lado}" height="{lado}" rx="10"/></clipPath>', f'<g clip-path="url(#cp{int(cx)})">']
    out += anillos(cx, cy, pid, km_px)
    out.append(planeta_disco(cx, cy, RADIO_PLANETA[pid], km_px, COLOR_PLANETA[pid]))
    pts = []
    for c in sis.cuerpos.values():
        a = c.meta.get("a_km") or 0
        if a > R_km * 1.02 or (solo_regulares is not None and a > solo_regulares):
            continue
        if not (c.meta["jd_valido_ini"] <= jd0 <= c.meta["jd_valido_fin"]):
            continue
        p = c.pos(jd0)
        if math.hypot(p[0], p[1]) > R_km * 1.02:
            continue
        pts.append((c, p))
    for c, p in pts:
        o = trazar_orbita(c, jd0, cx, cy, km_px, None) if orbitas else None
        if o and (c.meta.get("a_km") or 0) / km_px > 6:
            out.append(f'<path d="{o}" fill="none" stroke="#7d93c0" stroke-opacity="{0.55 if c.meta.get("principal") else 0.25}" stroke-width="0.8"/>')
    ocupado = []
    pts.sort(key=lambda t: -(t[0].meta.get("radio_km") or 0))
    for c, p in pts:
        x, y = cx + p[0] / km_px, cy - p[1] / km_px
        r = max(1.6, (c.meta.get("radio_km") or 0) / km_px)
        out.append(f'<circle cx="{f1(x)}" cy="{f1(y)}" r="{r:.1f}" fill="{COLOR_LUNA.get(str(c.id), "#b9b4aa")}"/>')
    n_rot = 0
    for c, p in pts:
        if n_rot >= rotular:
            break
        x, y = cx + p[0] / km_px, cy - p[1] / km_px
        w = 6.4 * len(c.nombre)
        caja = (x + 6, y - 14, x + 6 + w, y + 2)
        if caja[2] > cx + lado / 2 - 6 or any(not (caja[2] < o[0] or caja[0] > o[2] or caja[3] < o[1] or caja[1] > o[3]) for o in ocupado):
            continue
        ocupado.append(caja); n_rot += 1
        out.append(texto(x + 6, y - 3, c.nombre, 11, TEXTO))
    out.append("</g>")
    out += barra_escala(cx - lado / 2 + 16, cy + lado / 2 - 14, km_px, elegir_escala(R_km, lado / 2))
    out.append(texto(cx - lado / 2 + 16, cy - lado / 2 + 24, nombre_panel, 13, ACENTO, peso="600"))
    return out, len(pts)


def fig_sistema(clave: str) -> str:
    pid, titulo, R1, desc1 = SISTEMAS[clave]
    sis = lectura.Sistema(clave)
    jd0 = jd_tdb(JD_UTC_2027)
    todas = list(sis.cuerpos.values())
    R2 = max((c.meta.get("a_km") or 0) for c in todas) * 1.1
    n_ef = sum(1 for c in todas if c.meta["jd_valido_ini"] <= jd0 <= c.meta["jd_valido_fin"])
    lado = 520
    L = abrir(titulo, f"Esquema a escala de {titulo} el {formato_fecha(JD_UTC_2027)}: {len(todas)} lunas con efemérides oficiales de JPL.")
    L += encabezado(titulo, f"{len(todas)} lunas con efemérides oficiales · época {formato_fecha(JD_UTC_2027)}")
    p1, n1 = panel(sis, pid, (32 + lado / 2, 100 + lado / 2 + 8), R1, lado, jd0, f"Panel 1 · {desc1} (radio {R1 / 1e3:,.0f} mil km)".replace(",", " "), 14)
    p2, n2 = panel(sis, pid, (W - 32 - lado / 2, 100 + lado / 2 + 8), R2, lado, jd0, f"Panel 2 · todas las lunas ({n_ef} visibles)", 0, orbitas=False)
    L += p1 + p2
    L.append(texto(W / 2, 100 + lado + 4 + 20, "El planeta, sus anillos y las lunas están dibujados con su tamaño real en la misma escala del panel (las lunas pequeñas se marcan con puntos de 3 px).", 11, SUAVE, "middle"))
    L.append("</svg>")
    return "\n".join(L)


def fig_tierra() -> str:
    sol, tierra = lectura.Sistema("sol"), lectura.Sistema("tierra")
    jd_utc = 2461619.5 + 10.1167 / 24  # 2027-08-02 10:07 UTC (eclipse total)
    jd0 = jd_tdb(jd_utc)
    m = tierra.cuerpos["301"]
    e = sol.cuerpos["399"].pos(jd0)
    sx, sy = -e[0], -e[1]
    dsol = math.hypot(*[-q for q in e])
    mp = m.pos(jd0)
    L = abrir("Tierra · Sol · Luna", f"Esquema a escala de la órbita lunar y la dirección del Sol el {formato_fecha(jd_utc)} (eclipse total de Sol).")
    L += encabezado("Tierra · Sol · Luna", f"época {formato_fecha(jd_utc)} · eclipse total de Sol")
    cx, cy, lado = 32 + 260, 100 + 260 + 8, 520
    km_px = 420000 / (lado / 2 - 20)
    L += [f'<rect x="32" y="100" width="{lado}" height="{lado}" rx="10" fill="#0b1020" stroke="#26314f"/>']
    P = m.meta["periodo_d"] if m.meta.get("periodo_d") else 27.32
    N = 120
    pts = []
    for i in range(N + 1):
        p = m.pos(jd0 - P / 2 + P * i / N)
        pts.append((cx + p[0] / km_px, cy - p[1] / km_px))
    L.append(f'<path d="M{"L".join(f"{f1(x)} {f1(y)}" for x, y in pts)}" fill="none" stroke="#7d93c0" stroke-opacity="0.6" stroke-width="1"/>')
    L.append(f'<circle cx="{cx}" cy="{cy}" r="{max(2.0, 6378.1366 / km_px):.1f}" fill="#3b82c4"/>')
    L.append(f'<circle cx="{f1(cx + mp[0] / km_px)}" cy="{f1(cy - mp[1] / km_px)}" r="{max(1.6, 1737.4 / km_px):.1f}" fill="#cfcfc8"/>')
    L.append(f'<circle cx="{f1(cx + mp[0] / km_px)}" cy="{f1(cy - mp[1] / km_px)}" r="9" fill="none" stroke="{ACENTO}" stroke-width="1"/>')
    L.append(texto(cx + mp[0] / km_px + 14, cy - mp[1] / km_px - 6, "Luna", 12, ACENTO))
    L.append(texto(cx + 8, cy + 20, "Tierra", 12, TEXTO))
    ang = math.atan2(sy, sx)
    ax, ay = cx + math.cos(ang) * 236, cy - math.sin(ang) * 236
    L.append(f'<path d="M{f1(cx + math.cos(ang) * 120)} {f1(cy - math.sin(ang) * 120)}L{f1(ax)} {f1(ay)}" stroke="{ACENTO}" stroke-width="2" stroke-dasharray="6 5"/>')
    tx = ax + (-120 if math.cos(ang) > 0 else 8)
    L.append(texto(min(max(tx, 60), 400), ay - 8, f"hacia el Sol: {dsol / UA:.3f} UA", 12, ACENTO))
    L += barra_escala(48, 100 + lado - 14, km_px, 100000)
    L.append(texto(48, 100 + 24, "Órbita lunar (un mes sidéreo) a escala", 13, ACENTO, peso="600"))
    L.append(texto(48, 100 + 44, "Tierra: radio 6 378 km = 4 px · Luna: radio 1 737 km = 1,2 px", 11, SUAVE))
    # panel derecho: distancia Tierra-Luna 2027-2050 calculada de los datos
    x0, y0, w, h = 640, 100, 528, 330
    L.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10" fill="#0b1020" stroke="#26314f"/>')
    L.append(texto(x0 + 16, y0 + 26, "Distancia Tierra–Luna, 2027–2050 (km)", 13, ACENTO, peso="600"))
    dmin, dmax = 350000, 410000
    puntos = []
    t = 2461406.5
    while t < 2470172.5:
        p = m.pos(jd_tdb(t)); d = math.hypot(*p)
        puntos.append((x0 + 48 + (t - 2461406.5) / 8766 * (w - 72), y0 + h - 40 - (d - dmin) / (dmax - dmin) * (h - 90)))
        t += 2.0
    for k in range(350000, 410001, 20000):
        yy = y0 + h - 40 - (k - dmin) / (dmax - dmin) * (h - 90)
        L.append(f'<path d="M{x0 + 48} {f1(yy)}H{x0 + w - 24}" stroke="#26314f"/>')
        L.append(texto(x0 + 42, yy + 4, f"{k // 1000} mil", 10, SUAVE, "end"))
    L.append(f'<path d="M{"L".join(f"{f1(x)} {f1(y)}" for x, y in puntos)}" fill="none" stroke="#6cb4ff" stroke-width="0.6"/>')
    for a in range(2027, 2051, 4):
        xx = x0 + 48 + (a - 2027) / 24 * (w - 72)
        L.append(texto(xx, y0 + h - 20, str(a), 10, SUAVE, "middle"))
    L.append(texto(x0 + 16, y0 + 46, "Perigeos y apogeos reales: la órbita no es un círculo (356 400–406 700 km en el periodo)", 11, SUAVE))
    # panel derecho inferior: tamaños angulares
    y1 = y0 + h + 16
    L.append(f'<rect x="{x0}" y="{y1}" width="{w}" height="{100 + lado - (y1)}" rx="10" fill="#0b1020" stroke="#26314f"/>')
    dm = math.hypot(*mp)
    am = 2 * math.asin(1737.4 / dm) * 180 / math.pi * 60
    as_ = 2 * math.asin(695700 / (dsol)) * 180 / math.pi * 60
    L.append(texto(x0 + 16, y1 + 26, "Tamaños angulares en esta época", 13, ACENTO, peso="600"))
    L.append(texto(x0 + 16, y1 + 52, f"Luna: {am:.2f}′ a {dm:,.0f} km".replace(",", " "), 13, TEXTO))
    L.append(texto(x0 + 16, y1 + 74, f"Sol: {as_:.2f}′ a {dsol / 1e6:.1f} millones de km", 13, TEXTO))
    L.append(texto(x0 + 16, y1 + 96, "La Luna cubre al Sol: eclipse total (γ = 0,142 en el catálogo de la NASA).", 12, SUAVE))
    L.append("</svg>")
    return "\n".join(L)


def fig_sol() -> str:
    sol = lectura.Sistema("sol")
    jd_utc = JD_UTC_2027
    jd0 = jd_tdb(jd_utc)
    L = abrir("Sistema Solar", f"Esquema a escala de las órbitas planetarias el {formato_fecha(jd_utc)} visto desde el polo norte eclíptico.")
    L += encabezado("Sistema Solar", f"planetas, Plutón y Ceres · época {formato_fecha(jd_utc)}")
    lado = 520
    paneles = [(32 + lado / 2, 3.0 * UA, "Sistema interior (hasta 3 UA)", ["199", "299", "399", "499", "2000001"]),
               (W - 32 - lado / 2, 52 * UA, "Todo el sistema (hasta 52 UA)", ["199", "299", "399", "499", "599", "699", "799", "899", "9", "2000001"])]
    cy = 100 + lado / 2 + 8
    for cx, R, nombre, ids in paneles:
        km_px = R / (lado / 2 - 12)
        L.append(f'<rect x="{f1(cx - lado / 2)}" y="{f1(cy - lado / 2)}" width="{lado}" height="{lado}" rx="10" fill="#0b1020" stroke="#26314f"/>')
        L.append(f'<clipPath id="c{int(cx)}"><rect x="{f1(cx - lado / 2)}" y="{f1(cy - lado / 2)}" width="{lado}" height="{lado}" rx="10"/></clipPath><g clip-path="url(#c{int(cx)})">')
        L.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{max(2.5, 695700 / km_px):.1f}" fill="#ffd45e"/>')
        ocupado = []
        for i in ids:
            c = sol.cuerpos[i]
            P = PERIODO_PLANETA[i]
            # órbita: arco real 2027-2050 (grueso) y elipse osculadora (fina)
            pts = []
            n = 160
            for k in range(n + 1):
                jd = 2461406.5 + (8766 * k / n if P > 8766 * 0.9 else P * k / n)
                p = c.pos(jd_tdb(jd))
                pts.append((cx + p[0] / km_px, cy - p[1] / km_px))
            if P <= 8766 * 0.9:
                L.append(f'<path d="M{"L".join(f"{f1(x)} {f1(y)}" for x, y in pts)}" fill="none" stroke="#7d93c0" stroke-opacity="0.45" stroke-width="0.9"/>')
            else:
                L.append(f'<path d="M{"L".join(f"{f1(x)} {f1(y)}" for x, y in pts)}" fill="none" stroke="#6cb4ff" stroke-opacity="0.9" stroke-width="2"/>')
                # el resto de la órbita se aproxima con un círculo del radio actual (sólo guía)
                p = c.pos(jd0); r = math.hypot(p[0], p[1]) / km_px
                L.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{r:.1f}" fill="none" stroke="#7d93c0" stroke-opacity="0.22" stroke-dasharray="3 4"/>')
            p = c.pos(jd0)
            x, y = cx + p[0] / km_px, cy - p[1] / km_px
            L.append(f'<circle cx="{f1(x)}" cy="{f1(y)}" r="{max(3.0, RADIO_PLANETA[i] / km_px):.1f}" fill="{COLOR_PLANETA[i]}"/>')
            w = 6.4 * len(NOMBRE_PLANETA[i])
            caja = (x + 6, y - 14, x + 6 + w, y + 2)
            if caja[2] < cx + lado / 2 - 4 and not any(not (caja[2] < o[0] or caja[0] > o[2] or caja[3] < o[1] or caja[1] > o[3]) for o in ocupado):
                ocupado.append(caja)
                L.append(texto(x + 6, y - 3, NOMBRE_PLANETA[i], 11, TEXTO))
        L.append("</g>")
        L += barra_escala(cx - lado / 2 + 16, cy + lado / 2 - 14, km_px, elegir_escala(R, lado / 2))
        L.append(texto(cx - lado / 2 + 16, cy - lado / 2 + 24, nombre, 13, ACENTO, peso="600"))
    L.append(texto(W / 2, 100 + lado + 28, "Línea gruesa azul: arco recorrido entre 2027 y 2050 (planetas exteriores); línea fina: órbita completa. Los planetas se dibujan con su tamaño real: son puntos.", 11, SUAVE, "middle"))
    L.append("</svg>")
    return "\n".join(L)


def todas() -> dict[str, str]:
    out = {}
    d = lectura.DATOS
    if (d / "sol.bin").exists():
        out["sistema-solar.svg"] = fig_sol()
    if (d / "sol.bin").exists() and (d / "tierra.bin").exists():
        out["tierra.svg"] = fig_tierra()
    for k in SISTEMAS:
        if (d / f"{k}.bin").exists() and (d / "sol.bin").exists():
            out[f"{k}.svg"] = fig_sistema(k)
    return out


def verificar(nombre: str, svg: str) -> list[str]:
    import re
    errs = []
    for m in re.finditer(r"<text ([^>]*)>(.*?)</text>", svg):
        at = dict(re.findall(r'([\w-]+)="([^"]*)"', m[1]))
        x, y, tam, anc, t = float(at["x"]), float(at["y"]), float(at["font-size"]), at.get("text-anchor", "start"), m[2]
        w = len(t) * tam * 0.55
        x0 = x if anc == "start" else x - w if anc == "end" else x - w / 2
        if x0 < 0 or x0 + w > W + 1 or y < 0 or y > H:
            errs.append(f"{nombre}: texto fuera del lienzo: {t[:50]!r}")
    return errs


def main() -> int:
    figs = todas()
    SALIDA.mkdir(parents=True, exist_ok=True)
    mal = []
    for nombre, svg in figs.items():
        mal += verificar(nombre, svg)
        f = SALIDA / nombre
        if "--check" in sys.argv:
            if not f.exists() or f.read_text(encoding="utf-8") != svg + "\n":
                mal.append(f"{nombre}: desfasada respecto de los datos (ejecute herramientas/efemerides/generar_svg.py)")
        else:
            f.write_text(svg + "\n", encoding="utf-8")
    if "--check" in sys.argv:
        previas = {p.name for p in SALIDA.glob("*.svg")}
        mal += [f"{n}: figura sin datos de origen" for n in sorted(previas - set(figs))]
    for m in mal:
        print("ERROR", m)
    print(f"{len(figs)} figuras {'comprobadas' if '--check' in sys.argv else 'generadas'}, {len(mal)} problemas")
    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(main())
