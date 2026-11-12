# SPDX-License-Identifier: Apache-2.0
"""Utilidades comunes de los talleres: constantes, fórmulas de mecánica orbital y figuras SVG.

UNIDADES: km, s, kg, W; velocidades en km/s salvo que se diga lo contrario.
SISTEMA DE REFERENCIA: los que declare cada función (heliocéntrico eclíptico, geocéntrico, selenocéntrico...).
MODELO: cónicas de dos cuerpos y órbitas circulares y coplanares (diseño preliminar, ±5 %). No sirve para vuelo.
VERSIONES: Python 3.12, solo biblioteca estándar.
"""
from __future__ import annotations

import math

# --- Constantes (km, s) -----------------------------------------------------------------------
MU_SOL = 1.32712440018e11
MU_TIERRA = 3.986004418e5
MU_LUNA = 4.9028e3
MU_MARTE = 4.282837e4
MU_VENUS = 3.24859e5
MU_JUPITER = 1.26687e8
MU_SATURNO = 3.79312e7
UA = 1.495978707e8
R_TIERRA = 6378.137
R_LUNA = 1737.4
R_SOL = 695700.0
C_LUZ = 299792.458
G0 = 9.80665
SIGMA = 5.670374e-8  # W/m^2/K^4
S_1UA = 1361.0       # W/m^2, constante solar a 1 UA


def vis_viva(mu: float, r: float, a: float) -> float:
    return math.sqrt(mu * (2 / r - 1 / a))


def circular(mu: float, r: float) -> float:
    return math.sqrt(mu / r)


def periodo(mu: float, a: float) -> float:
    return 2 * math.pi * math.sqrt(a**3 / mu)


def hohmann(a1: float, a2: float, mu: float = MU_SOL) -> dict:
    v1, v2 = circular(mu, a1), circular(mu, a2)
    at = (a1 + a2) / 2
    vt1, vt2 = vis_viva(mu, a1, at), vis_viva(mu, a2, at)
    return {"v_inf_salida": vt1 - v1, "v_inf_llegada": v2 - vt2, "t_vuelo_s": math.pi * math.sqrt(at**3 / mu),
            "n1": v1 / a1, "n2": v2 / a2, "dv1": vt1 - v1, "dv2": v2 - vt2}


def delta_v_desde_orbita_baja(v_inf: float, mu: float, r: float) -> float:
    """Delta-v de un impulso en el periapsis de una órbita circular de radio r para alcanzar v_inf."""
    return math.sqrt(v_inf**2 + 2 * mu / r) - circular(mu, r)


def velocidad_entrada(v_inf: float, mu: float, r: float) -> float:
    return math.sqrt(v_inf**2 + 2 * mu / r)


def cohete_dv(isp_s: float, m0: float, mf: float) -> float:
    """Delta-v ideal en km/s."""
    return isp_s * G0 * math.log(m0 / mf) / 1000


def masa_propelente(dv_kms: float, isp_s: float, m_final: float) -> float:
    return m_final * (math.exp(dv_kms * 1000 / (isp_s * G0)) - 1)


def luz_min(distancia_km: float) -> float:
    return distancia_km / C_LUZ / 60


def rtg(p0: float, anios: float, vida_media_anios: float = 87.7, degradacion_anual: float = 0.0) -> float:
    """Potencia de un generador de radioisótopos: decaimiento del Pu-238 y degradación de los termopares."""
    return p0 * math.exp(-math.log(2) * anios / vida_media_anios) * (1 - degradacion_anual) ** anios


def flujo_solar(d_ua: float) -> float:
    return S_1UA / d_ua**2


def temperatura_equilibrio(flujo: float, absortividad: float = 0.9, emisividad: float = 0.9, factor: float = 4.0) -> float:
    """Temperatura de equilibrio de una superficie plana al Sol (factor 4 = esfera isoterma, 1 = cara al Sol)."""
    return (absortividad * flujo / (factor * emisividad * SIGMA)) ** 0.25


def serie(p: list[float]) -> float:
    r = 1.0
    for x in p:
        r *= x
    return r


def paralelo(p: list[float]) -> float:
    r = 1.0
    for x in p:
        r *= 1 - x
    return 1 - r


def fmt(x: float, d: int = 2) -> str:
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# --- Figuras SVG -------------------------------------------------------------------------------
FONDO, TINTA, SUAVE = "#ffffff", "#1d2733", "#5b6b7c"
AZUL, ROJO, VERDE, AMBAR, MORADO, GRIS = "#1f77b4", "#c1440e", "#2a7f62", "#e0a800", "#6a4fb0", "#8a96a3"
FUENTE = 'font-family="Segoe UI, Arial, sans-serif"'


def svg(ancho: int, alto: int, titulo: str, desc: str, cuerpo: str) -> str:
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" role="img" '
            f'aria-labelledby="t d"><title id="t">{esc(titulo)}</title><desc id="d">{esc(desc)}</desc>'
            f'<rect width="{ancho}" height="{alto}" fill="{FONDO}"/>{cuerpo}</svg>')


def t(x: float, y: float, s: str, tam: int = 14, color: str = TINTA, anchor: str = "start", peso: str = "normal") -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{tam}" fill="{color}" text-anchor="{anchor}" font-weight="{peso}" {FUENTE}>{s}</text>'


def encabezado(titulo: str, sub: str) -> str:
    return t(24, 36, titulo, 20, TINTA, "start", "bold") + t(24, 58, sub, 13, SUAVE)


def barra_apilada(titulo: str, sub: str, datos: list[tuple[str, float, str]], unidad: str, nota: str, desc: str) -> str:
    total = sum(d[1] for d in datos)
    x0, y0, w = 40.0, 110.0, 900.0
    c = [encabezado(titulo, sub)]
    x = x0
    for i, (n, v, col) in enumerate(datos):
        ancho = w * v / total
        c.append(f'<rect x="{x:.1f}" y="{y0}" width="{ancho:.1f}" height="70" fill="{col}"/>')
        c.append(f'<line x1="{x + ancho / 2:.1f}" y1="{y0 + 70}" x2="{x + ancho / 2:.1f}" y2="{y0 + 90 + (i % 2) * 44}" stroke="{SUAVE}"/>')
        c.append(t(x + ancho / 2, y0 + 106 + (i % 2) * 44, n, 13, TINTA, "middle", "bold"))
        c.append(t(x + ancho / 2, y0 + 123 + (i % 2) * 44, f"{fmt(v, 0)} {unidad} · {100 * v / total:.0f} %", 13, SUAVE, "middle"))
        x += ancho
    c.append(t(24, 330, nota, 13, TINTA))
    return svg(980, 360, titulo, desc, "".join(c))


def barras(titulo: str, sub: str, datos: list[tuple[str, float, str]], unidad: str, nota: str, desc: str, formato: int = 0) -> str:
    """Barras horizontales; la etiqueta va a la izquierda y el valor al final de la barra."""
    n = len(datos)
    alto = 110 + 40 * n + 50
    vmax = max(d[1] for d in datos)
    x0, w = 330.0, 560.0
    c = [encabezado(titulo, sub)]
    for i, (nombre, v, col) in enumerate(datos):
        y = 90 + 40 * i
        ancho = max(2.0, w * v / vmax)
        c.append(t(x0 - 12, y + 19, nombre, 13, TINTA, "end"))
        c.append(f'<rect x="{x0}" y="{y}" width="{ancho:.1f}" height="26" fill="{col}"/>')
        c.append(t(x0 + ancho + 8, y + 19, f"{fmt(v, formato)} {unidad}", 13, SUAVE))
    c.append(t(24, alto - 18, nota, 13, TINTA))
    return svg(980, alto, titulo, desc, "".join(c))


def lineas(titulo: str, sub: str, series: list[tuple[str, list[tuple[float, float]], str]], xlab: str, ylab: str,
           xt: list[float], yt: list[float], marcas: list[tuple[float, float, str]] | None = None, logy: bool = False,
           nota: str = "", desc: str = "") -> str:
    x0, y0, w, h = 100.0, 90.0, 790.0, 300.0
    xs = [p[0] for s in series for p in s[1]]
    ys = [p[1] for s in series for p in s[1]]
    xmin, xmax = min(xt), max(xt)
    ymin, ymax = min(yt), max(yt)

    def X(x):
        return x0 + (x - xmin) / (xmax - xmin) * w

    def Y(y):
        if logy:
            return y0 + h - (math.log10(y) - math.log10(ymin)) / (math.log10(ymax) - math.log10(ymin)) * h
        return y0 + h - (y - ymin) / (ymax - ymin) * h

    c = [encabezado(titulo, sub), f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="{SUAVE}"/>']
    for v in yt:
        c.append(f'<line x1="{x0}" y1="{Y(v):.1f}" x2="{x0 + w}" y2="{Y(v):.1f}" stroke="#e3e8ee"/>')
        c.append(t(x0 - 10, Y(v) + 4, fmt(v, 0 if v >= 10 else 1), 12, SUAVE, "end"))
    for v in xt:
        c.append(t(X(v), y0 + h + 20, fmt(v, 0 if float(v).is_integer() else 1), 12, SUAVE, "middle"))
    for nombre, pts, col in series:
        c.append('<polyline points="' + " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts) + f'" fill="none" stroke="{col}" stroke-width="3.5"/>')
    if len(series) > 1:
        for i, (nombre, pts, col) in enumerate(series):
            c.append(f'<rect x="{x0 + 16 + i * 230}" y="{y0 + 12}" width="14" height="14" fill="{col}"/>')
            c.append(t(x0 + 36 + i * 230, y0 + 24, nombre, 13, TINTA))
    for (a, b, etq) in marcas or []:
        c.append(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="5" fill="{TINTA}" stroke="#fff" stroke-width="1.5"/>')
        c.append(t(X(a), Y(b) - 12, etq, 13, TINTA, "middle", "bold"))
    c.append(t(x0 + w / 2, y0 + h + 44, xlab, 13, TINTA, "middle"))
    c.append(t(24, y0 + h / 2, ylab, 13, TINTA, "start"))
    if nota:
        c.append(t(24, 464, nota, 13, SUAVE))
    return svg(980, 480, titulo, desc or titulo, "".join(c))


def linea_tiempo(titulo: str, sub: str, eventos: list[tuple[str, str, str]], tramo: tuple[int, str] | None, nota: str, desc: str) -> str:
    n = len(eventos)
    x0, x1, y = 90.0, 910.0, 250.0
    paso = (x1 - x0) / (n - 1)
    c = [encabezado(titulo, sub), f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{TINTA}" stroke-width="3"/>']
    if tramo:
        i0, texto = tramo
        c.append(f'<rect x="{x0 + i0 * paso:.1f}" y="{y - 10}" width="{x1 - x0 - i0 * paso:.1f}" height="20" fill="{ROJO}" opacity="0.18"/>')
        c.append(t((x0 + i0 * paso + x1) / 2, y + 150, texto, 14, ROJO, "middle", "bold"))
    for i, (tt, nombre, det) in enumerate(eventos):
        x = x0 + i * paso
        arriba = i % 2 == 0
        y_txt = y - 70 if arriba else y + 62
        c.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y_txt + (6 if arriba else -16):.1f}" stroke="{SUAVE}"/>')
        c.append(f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="{VERDE if i < n - 1 else ROJO}" stroke="#fff" stroke-width="2"/>')
        ancla = "start" if i == 0 else ("end" if i == n - 1 else "middle")
        c.append(t(x, y_txt - 20 if arriba else y_txt - 2, tt, 12, SUAVE, ancla))
        c.append(t(x, y_txt if arriba else y_txt + 16, nombre, 13, TINTA, ancla, "bold"))
        c.append(t(x, y_txt + 17 if arriba else y_txt + 33, det, 12, SUAVE, ancla))
    c.append(t(24, 430, nota, 13, TINTA))
    return svg(980, 460, titulo, desc, "".join(c))


def mapa_orbital(titulo: str, sub: str, orbitas: list[tuple[str, float, str]], rutas: list[tuple[list[tuple[float, float]], str, float]],
                 marcas: list[tuple[float, float, str, str, int, int, str]], esc: float, notas: list[str], desc: str,
                 centro: str = "Sol", color_centro: str = AMBAR, rcentro: int = 12, alto: int = 660) -> str:
    """Órbitas circulares (radio en unidades del mapa) vistas desde el norte. rutas: puntos (ángulo_rad, radio).
    marcas: (ángulo_rad, radio, etiqueta, color, dx, dy, ancla)."""
    cx, cy = 490.0, 330.0

    def P(a, r):
        return cx + esc * r * math.cos(a), cy - esc * r * math.sin(a)

    c = [encabezado(titulo, sub)]
    for nombre, r, col in orbitas:
        c.append(f'<circle cx="{cx}" cy="{cy}" r="{esc * r:.1f}" fill="none" stroke="{col}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    for pts, col, ancho in rutas:
        c.append('<path d="M' + " L".join("%.1f,%.1f" % P(a, r) for a, r in pts) + f'" fill="none" stroke="{col}" stroke-width="{ancho}"/>')
    c.append(f'<circle cx="{cx}" cy="{cy}" r="{rcentro}" fill="{color_centro}"/>')
    c.append(t(cx, cy + rcentro + 18, centro, 13, TINTA, "middle"))
    for a, r, etq, col, dx, dy, anc in marcas:
        x, y = P(a, r)
        c.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{col}" stroke="#fff" stroke-width="1.5"/>')
        c.append(t(x + dx, y + dy, etq, 13, col, anc, "bold"))
    for i, s in enumerate(notas):
        c.append(t(24, alto - 22 * (len(notas) - i) - 4, s, 13, TINTA if i == 0 else SUAVE))
    return svg(980, alto, titulo, desc, "".join(c))
