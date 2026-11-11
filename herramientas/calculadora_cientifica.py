#!/usr/bin/env python3
"""Calculadora científica del programa (solo biblioteca estándar de Python).

Sirve para comprobar a mano los cálculos de las clases: constantes con fuente,
conversión de unidades, escalas astronómicas, mecánica orbital, cohetes,
radiación, óptica y evaluación segura de expresiones.

Cada resultado declara unidades y el supuesto del modelo. Es una herramienta
didáctica: no sustituye software validado ni sirve para decisiones de vuelo,
lanzamiento o seguridad.

Uso (ver `--ayuda` o `python herramientas/calculadora_cientifica.py -h`):
  calculadora_cientifica.py const G
  calculadora_cientifica.py convert 1 pc ly
  calculadora_cientifica.py calc "sqrt(2*GM_tierra/(R_tierra+400e3))"
  calculadora_cientifica.py modulo-distancia --m 5 --M 0
  calculadora_cientifica.py orbita --a 6778e3 --cuerpo tierra
  calculadora_cientifica.py hohmann --r1 6678e3 --r2 42164e3 --cuerpo tierra
  calculadora_cientifica.py cohete --isp 450 --m0 1000 --mf 300
  calculadora_cientifica.py autotest
"""
from __future__ import annotations

import argparse
import ast
import math
import operator
import sys

# ---------------------------------------------------------------------------
# Constantes. Cada una: (valor, unidad, fuente / nota)
# ---------------------------------------------------------------------------
PI = math.pi
CONSTANTES = {
    "c": (299_792_458.0, "m/s", "SI 2019, valor exacto"),
    "h": (6.626_070_15e-34, "J s", "SI 2019, valor exacto"),
    "k_B": (1.380_649e-23, "J/K", "SI 2019, valor exacto"),
    "e": (1.602_176_634e-19, "C", "SI 2019, valor exacto"),
    "N_A": (6.022_140_76e23, "1/mol", "SI 2019, valor exacto"),
    "G": (6.674_30e-11, "m^3 kg^-1 s^-2", "CODATA 2018 (incertidumbre relativa ~2,2e-5)"),
    "sigma_SB": (5.670_374_419e-8, "W m^-2 K^-4", "derivada de h, k_B y c (CODATA 2018)"),
    "b_Wien": (2.897_771_955e-3, "m K", "derivada de h, k_B y c (CODATA 2018)"),
    "m_e": (9.109_383_7015e-31, "kg", "CODATA 2018"),
    "m_p": (1.672_621_923_69e-27, "kg", "CODATA 2018"),
    "UA": (149_597_870_700.0, "m", "UAI 2012, definición exacta"),
    "pc": (149_597_870_700.0 * 648_000.0 / PI, "m", "UAI 2015: 648000/pi UA (derivado)"),
    "ly": (299_792_458.0 * 365.25 * 86_400.0, "m", "año luz = c x 365,25 d (año juliano)"),
    "GM_sol": (1.327_124_4e20, "m^3 s^-2", "UAI 2015 Resolución B3, valor nominal"),
    "R_sol": (6.957e8, "m", "UAI 2015 Resolución B3, valor nominal"),
    "L_sol": (3.828e26, "W", "UAI 2015 Resolución B3, valor nominal"),
    "T_sol": (5772.0, "K", "UAI 2015 Resolución B3, temperatura efectiva nominal"),
    "GM_tierra": (3.986_004e14, "m^3 s^-2", "UAI 2015 B3, valor nominal"),
    "R_tierra": (6.378_1e6, "m", "UAI 2015 B3, radio ecuatorial nominal"),
    "GM_luna": (4.902_800_066e12, "m^3 s^-2", "valor de referencia de la literatura (GRAIL); contrastar con la fuente"),
    "R_luna": (1.737_4e6, "m", "radio medio, valor de referencia"),
    "GM_jupiter": (1.266_865_3e17, "m^3 s^-2", "UAI 2015 B3, valor nominal"),
    "R_jupiter": (7.149_2e7, "m", "UAI 2015 B3, radio ecuatorial nominal"),
    "g0": (9.806_65, "m/s^2", "gravedad estándar convencional (definición)"),
    "dia": (86_400.0, "s", "día SI de 86 400 s"),
    "ano_juliano": (365.25 * 86_400.0, "s", "año juliano de 365,25 d"),
}

# Cuerpos para las funciones orbitales: (GM [m^3/s^2], radio [m])
CUERPOS = {
    "sol": (CONSTANTES["GM_sol"][0], CONSTANTES["R_sol"][0]),
    "tierra": (CONSTANTES["GM_tierra"][0], CONSTANTES["R_tierra"][0]),
    "luna": (CONSTANTES["GM_luna"][0], CONSTANTES["R_luna"][0]),
    "jupiter": (CONSTANTES["GM_jupiter"][0], CONSTANTES["R_jupiter"][0]),
}

# ---------------------------------------------------------------------------
# Conversión de unidades: factor al SI de cada magnitud
# ---------------------------------------------------------------------------
LONGITUD = {"m": 1.0, "km": 1e3, "cm": 1e-2, "mm": 1e-3, "um": 1e-6, "nm": 1e-9, "angstrom": 1e-10,
            "ua": CONSTANTES["UA"][0], "au": CONSTANTES["UA"][0], "ly": CONSTANTES["ly"][0],
            "pc": CONSTANTES["pc"][0], "kpc": CONSTANTES["pc"][0] * 1e3, "mpc": CONSTANTES["pc"][0] * 1e6,
            "R_sol": CONSTANTES["R_sol"][0], "R_tierra": CONSTANTES["R_tierra"][0],
            "mi": 1609.344, "ft": 0.3048, "in": 0.0254, "nmi": 1852.0}
MASA = {"kg": 1.0, "g": 1e-3, "t": 1e3, "lb": 0.45359237,
        "M_sol": CONSTANTES["GM_sol"][0] / CONSTANTES["G"][0],
        "M_tierra": CONSTANTES["GM_tierra"][0] / CONSTANTES["G"][0]}
TIEMPO = {"s": 1.0, "ms": 1e-3, "us": 1e-6, "min": 60.0, "h": 3600.0, "d": 86_400.0,
          "ano": CONSTANTES["ano_juliano"][0], "yr": CONSTANTES["ano_juliano"][0]}
ENERGIA = {"J": 1.0, "kJ": 1e3, "MJ": 1e6, "erg": 1e-7, "cal": 4.184, "kWh": 3.6e6,
           "eV": CONSTANTES["e"][0], "keV": CONSTANTES["e"][0] * 1e3, "MeV": CONSTANTES["e"][0] * 1e6,
           "GeV": CONSTANTES["e"][0] * 1e9, "ton_TNT": 4.184e9}
ANGULO = {"rad": 1.0, "deg": PI / 180.0, "arcmin": PI / 10_800.0, "arcsec": PI / 648_000.0,
          "mas": PI / 648_000_000.0, "uas": PI / 648_000_000_000.0, "hora": PI / 12.0, "rev": 2 * PI}
PRESION = {"Pa": 1.0, "kPa": 1e3, "MPa": 1e6, "bar": 1e5, "mbar": 1e2, "atm": 101_325.0, "mmHg": 133.322_387_415, "psi": 6894.757_293_168}
VELOCIDAD = {"m/s": 1.0, "km/s": 1e3, "km/h": 1 / 3.6, "mph": 0.44704, "kn": 1852 / 3600, "c": CONSTANTES["c"][0]}
POTENCIA = {"W": 1.0, "kW": 1e3, "MW": 1e6, "erg/s": 1e-7, "L_sol": CONSTANTES["L_sol"][0]}
TABLAS = {"longitud": LONGITUD, "masa": MASA, "tiempo": TIEMPO, "energia": ENERGIA, "angulo": ANGULO,
          "presion": PRESION, "velocidad": VELOCIDAD, "potencia": POTENCIA}


def convertir(valor: float, de: str, a: str) -> float:
    """Convierte entre dos unidades de la misma magnitud (incluye temperaturas)."""
    temps = {"K", "C", "F", "R"}
    if de in temps and a in temps:
        k = {"K": valor, "C": valor + 273.15, "F": (valor - 32) * 5 / 9 + 273.15, "R": valor * 5 / 9}[de]
        return {"K": k, "C": k - 273.15, "F": (k - 273.15) * 9 / 5 + 32, "R": k * 9 / 5}[a]
    for nombre, tabla in TABLAS.items():
        if de in tabla and a in tabla:
            return valor * tabla[de] / tabla[a]
    raise ValueError(f"No se puede convertir de «{de}» a «{a}» (magnitudes distintas o unidad desconocida).")


# ---------------------------------------------------------------------------
# Fórmulas
# ---------------------------------------------------------------------------
def modulo_distancia(m: float | None = None, M: float | None = None, d_pc: float | None = None) -> dict:
    """m - M = 5 log10(d/10 pc). Dados dos de (m, M, d), calcula el tercero. Sin extinción."""
    if d_pc is not None and M is not None and m is None:
        return {"m": M + 5 * math.log10(d_pc / 10)}
    if d_pc is not None and m is not None and M is None:
        return {"M": m - 5 * math.log10(d_pc / 10)}
    if m is not None and M is not None and d_pc is None:
        return {"d_pc": 10 ** ((m - M + 5) / 5)}
    raise ValueError("Da exactamente dos de: m, M, d_pc.")


def razon_flujos(delta_m: float) -> float:
    """Pogson: F1/F2 = 10^(-0,4 (m1 - m2))."""
    return 10 ** (-0.4 * delta_m)


def kepler_periodo(a: float, gm: float) -> float:
    """T = 2 pi sqrt(a^3 / GM) [s] (problema de dos cuerpos, a = semieje mayor)."""
    return 2 * PI * math.sqrt(a ** 3 / gm)


def vis_viva(r: float, a: float, gm: float) -> float:
    """v = sqrt(GM (2/r - 1/a)) [m/s]."""
    return math.sqrt(gm * (2 / r - 1 / a))


def velocidad_circular(r: float, gm: float) -> float:
    return math.sqrt(gm / r)


def velocidad_escape(r: float, gm: float) -> float:
    return math.sqrt(2 * gm / r)


def hohmann(r1: float, r2: float, gm: float) -> dict:
    """Transferencia de Hohmann entre órbitas circulares coplanares (impulsiva)."""
    a_t = (r1 + r2) / 2
    dv1 = abs(vis_viva(r1, a_t, gm) - velocidad_circular(r1, gm))
    dv2 = abs(velocidad_circular(r2, gm) - vis_viva(r2, a_t, gm))
    return {"dv1": dv1, "dv2": dv2, "dv_total": dv1 + dv2, "tiempo_vuelo": PI * math.sqrt(a_t ** 3 / gm)}


def tsiolkovski(isp: float, m0: float, mf: float) -> float:
    """dv = Isp g0 ln(m0/mf) [m/s]."""
    return isp * CONSTANTES["g0"][0] * math.log(m0 / mf)


def masa_propelente(dv: float, isp: float, m0: float) -> float:
    """Masa de propelente para un dv dado: m0 (1 - exp(-dv/(Isp g0)))."""
    return m0 * (1 - math.exp(-dv / (isp * CONSTANTES["g0"][0])))


def radio_schwarzschild(masa_kg: float) -> float:
    return 2 * CONSTANTES["G"][0] * masa_kg / CONSTANTES["c"][0] ** 2


def luminosidad(radio_m: float, t_k: float) -> float:
    """L = 4 pi R^2 sigma T^4 [W] (cuerpo negro esférico)."""
    return 4 * PI * radio_m ** 2 * CONSTANTES["sigma_SB"][0] * t_k ** 4


def temperatura_equilibrio(l_w: float, d_m: float, albedo: float = 0.3) -> float:
    """T_eq = [L (1-A) / (16 pi sigma d^2)]^(1/4) [K] (rotación rápida, sin efecto invernadero)."""
    return (l_w * (1 - albedo) / (16 * PI * CONSTANTES["sigma_SB"][0] * d_m ** 2)) ** 0.25


def wien_pico(t_k: float) -> float:
    """Longitud de onda del máximo (por unidad de longitud de onda) [m]."""
    return CONSTANTES["b_Wien"][0] / t_k


def corrimiento_rojo_velocidad(z: float) -> float:
    """Velocidad radial relativista v/c = ((1+z)^2 - 1)/((1+z)^2 + 1)."""
    s = (1 + z) ** 2
    return (s - 1) / (s + 1)


def rayleigh(diametro_m: float, lam_m: float) -> float:
    """Límite de difracción de una apertura circular: 1,22 lambda / D [rad]."""
    return 1.22 * lam_m / diametro_m


def escala_de_placa(focal_m: float) -> float:
    """Escala de placa en segundos de arco por milímetro: 206265 / f[mm]."""
    return 206_264.806 / (focal_m * 1e3)


def esfera_de_hill(a: float, m_sec: float, m_prim: float, e: float = 0.0) -> float:
    return a * (1 - e) * (m_sec / (3 * m_prim)) ** (1 / 3)


def energia_sismica_mw(mw: float) -> float:
    """Energía sísmica radiada aproximada [J]: log10 E = 1,5 Mw + 4,8 (Gutenberg–Richter, orden de magnitud)."""
    return 10 ** (1.5 * mw + 4.8)


def kardashev(potencia_w: float) -> float:
    """Escala de Kardashev continua de Sagan: K = (log10 P - 6) / 10."""
    return (math.log10(potencia_w) - 6) / 10


def flujo_clase_goes(clase: str) -> float:
    """Flujo de rayos X (0,1–0,8 nm) de una clase GOES, p. ej. 'M5.2' -> 5,2e-5 W/m^2."""
    base = {"A": 1e-8, "B": 1e-7, "C": 1e-6, "M": 1e-5, "X": 1e-4}
    return base[clase[0].upper()] * float(clase[1:] or 1)


def fecha_juliana(anio: int, mes: int, dia: float) -> float:
    """Día juliano (calendario gregoriano; Meeus). `dia` puede ser fraccionario (0,5 = mediodía)."""
    if mes <= 2:
        anio -= 1
        mes += 12
    a = anio // 100
    b = 2 - a + a // 4
    return int(365.25 * (anio + 4716)) + int(30.6001 * (mes + 1)) + dia + b - 1524.5


# ---------------------------------------------------------------------------
# Evaluador seguro de expresiones
# ---------------------------------------------------------------------------
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos, ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv}
_FUN = {n: getattr(math, n) for n in ("sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "exp",
                                       "log", "log10", "log2", "sinh", "cosh", "tanh", "radians", "degrees",
                                       "floor", "ceil", "fabs", "hypot", "factorial", "gamma")}
_FUN.update({"abs": abs, "min": min, "max": max, "round": round})
_NOMBRES = {"pi": PI, "tau": 2 * PI, "e_euler": math.e, "inf": math.inf}
_NOMBRES.update({k: v[0] for k, v in CONSTANTES.items()})


def evaluar(expr: str) -> float:
    """Evalúa una expresión matemática sin usar eval(): solo números, operadores, funciones de `math` y constantes."""
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.operand))
        if isinstance(n, ast.Name) and n.id in _NOMBRES:
            return _NOMBRES[n.id]
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in _FUN and not n.keywords:
            return _FUN[n.func.id](*[ev(a) for a in n.args])
        raise ValueError(f"Expresión no permitida: {ast.dump(n)[:60]}")
    return ev(ast.parse(expr.strip(), mode="eval"))


# ---------------------------------------------------------------------------
# Interfaz de línea de órdenes
# ---------------------------------------------------------------------------
def fmt(x: float) -> str:
    if x == 0:
        return "0"
    return f"{x:.6g}" if 1e-3 <= abs(x) < 1e6 else f"{x:.6e}"


def autotest() -> int:
    """Comprueba valores conocidos (tolerancia relativa declarada en cada caso)."""
    casos = [
        ("1 UA / c = 499,00 s", CONSTANTES["UA"][0] / CONSTANTES["c"][0], 499.004_784, 1e-6),
        ("1 pc en años luz = 3,2616", convertir(1, "pc", "ly"), 3.261_564, 1e-5),
        ("1 pc en UA = 206 264,8", convertir(1, "pc", "ua"), 206_264.806, 1e-6),
        ("0 °C en K", convertir(0, "C", "K"), 273.15, 1e-12),
        ("100 °C en °F", convertir(100, "C", "F"), 212.0, 1e-12),
        ("1 arcsec en rad", convertir(1, "arcsec", "rad"), 4.848_137e-6, 1e-6),
        ("Periodo de ISS (a=6778 km) ~ 92,6 min", kepler_periodo(6_778e3, CONSTANTES["GM_tierra"][0]) / 60, 92.56, 2e-3),
        ("Velocidad circular a 400 km ~ 7,67 km/s", velocidad_circular(6_778e3 + 0, CONSTANTES["GM_tierra"][0]) / 1e3, 7.669, 2e-3),
        ("Escape en superficie de la Tierra ~ 11,19 km/s", velocidad_escape(CONSTANTES["R_tierra"][0], CONSTANTES["GM_tierra"][0]) / 1e3, 11.186, 2e-3),
        ("Hohmann LEO(6678 km)->GEO(42164 km) dv total ~ 3,89 km/s", hohmann(6_678e3, 42_164e3, CONSTANTES["GM_tierra"][0])["dv_total"] / 1e3, 3.89, 1e-2),
        ("Tsiolkovski Isp 450 s, m0/mf=10/3 ~ 5,31 km/s", tsiolkovski(450, 1000, 300) / 1e3, 5.314, 2e-3),
        ("Radio de Schwarzschild del Sol ~ 2,95 km", radio_schwarzschild(CONSTANTES["GM_sol"][0] / CONSTANTES["G"][0]) / 1e3, 2.953, 2e-3),
        ("Luminosidad del Sol (R, T nominales) ~ 3,83e26 W", luminosidad(CONSTANTES["R_sol"][0], CONSTANTES["T_sol"][0]), 3.828e26, 3e-3),
        ("Wien: T=5772 K -> 502 nm", wien_pico(5772) * 1e9, 502.0, 2e-3),
        ("Módulo de distancia: m-M=5 -> 100 pc", modulo_distancia(m=5, M=0)["d_pc"], 100.0, 1e-9),
        ("Pogson: 5 mag = factor 100", razon_flujos(-5), 100.0, 1e-9),
        ("Día juliano 2000-01-01 12:00 TT = 2451545,0", fecha_juliana(2000, 1, 1.5), 2451545.0, 1e-12),
        ("GOES M5.2 = 5,2e-5 W/m²", flujo_clase_goes("M5.2"), 5.2e-5, 1e-12),
        ("Rayleigh 1 m a 550 nm ~ 0,138 arcsec", rayleigh(1, 550e-9) / ANGULO["arcsec"], 0.1384, 5e-3),
        ("Evaluador: sqrt(2)*sqrt(2) = 2", evaluar("sqrt(2)*sqrt(2)"), 2.0, 1e-12),
    ]
    malos = 0
    for nombre, obtenido, esperado, tol in casos:
        err = abs(obtenido - esperado) / abs(esperado)
        ok = err <= tol
        malos += not ok
        print(("OK  " if ok else "FALLA"), nombre, f"→ {fmt(obtenido)} (esperado {fmt(esperado)}, error rel. {err:.1e}, tol. {tol:g})")
    print(f"\n{len(casos) - malos} de {len(casos)} comprobaciones correctas.")
    return 1 if malos else 0


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):  # consolas de Windows con cp1252
        sys.stdout.reconfigure(encoding="utf-8")
    p =argparse.ArgumentParser(description="Calculadora científica del programa (didáctica, solo biblioteca estándar).")
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("const", help="Muestra una constante con su unidad y fuente (o todas).")
    s.add_argument("nombre", nargs="?")
    s = sp.add_parser("convert", help="Convierte unidades: VALOR DE A (p. ej. 1 pc ly).")
    s.add_argument("valor", type=float); s.add_argument("de"); s.add_argument("a")
    s = sp.add_parser("calc", help="Evalúa una expresión con constantes y funciones de math.")
    s.add_argument("expresion")
    s = sp.add_parser("modulo-distancia", help="m - M = 5 log10(d/10 pc): da dos de --m --M --d-pc.")
    s.add_argument("--m", type=float); s.add_argument("--M", type=float); s.add_argument("--d-pc", type=float, dest="d")
    s = sp.add_parser("flujos", help="Razón de flujos entre dos estrellas con diferencia de magnitud.")
    s.add_argument("delta_m", type=float, help="m1 - m2")
    s = sp.add_parser("orbita", help="Periodo, velocidad circular y de escape.")
    s.add_argument("--a", type=float, required=True, help="semieje mayor o radio [m]")
    s.add_argument("--cuerpo", choices=CUERPOS, default="tierra")
    s = sp.add_parser("hohmann", help="Transferencia de Hohmann entre dos radios circulares [m].")
    s.add_argument("--r1", type=float, required=True); s.add_argument("--r2", type=float, required=True)
    s.add_argument("--cuerpo", choices=CUERPOS, default="tierra")
    s = sp.add_parser("cohete", help="Ecuación de Tsiolkovski: --isp [s] --m0 --mf.")
    s.add_argument("--isp", type=float, required=True); s.add_argument("--m0", type=float, required=True); s.add_argument("--mf", type=float, required=True)
    s = sp.add_parser("estrella", help="Luminosidad, T de equilibrio y pico de Wien de una estrella o planeta.")
    s.add_argument("--radio", type=float, required=True, help="[m]"); s.add_argument("--temp", type=float, required=True, help="[K]")
    s = sp.add_parser("fecha-juliana", help="Día juliano de AAAA MM DD.fracción (calendario gregoriano).")
    s.add_argument("anio", type=int); s.add_argument("mes", type=int); s.add_argument("dia", type=float)
    sp.add_parser("autotest", help="Comprueba la calculadora contra valores conocidos.")
    a = p.parse_args(argv)

    if a.cmd == "const":
        items = [a.nombre] if a.nombre else sorted(CONSTANTES)
        for n in items:
            if n not in CONSTANTES:
                print(f"Constante desconocida: {n}. Disponibles: {', '.join(sorted(CONSTANTES))}")
                return 2
            v, u, f = CONSTANTES[n]
            print(f"{n} = {v:.12g} {u}   [{f}]")
    elif a.cmd == "convert":
        print(f"{fmt(a.valor)} {a.de} = {fmt(convertir(a.valor, a.de, a.a))} {a.a}")
    elif a.cmd == "calc":
        print(fmt(evaluar(a.expresion)))
    elif a.cmd == "modulo-distancia":
        print(modulo_distancia(a.m, a.M, a.d))
    elif a.cmd == "flujos":
        print(f"F1/F2 = {fmt(razon_flujos(a.delta_m))}")
    elif a.cmd == "orbita":
        gm, rad = CUERPOS[a.cuerpo]
        print(f"Periodo = {fmt(kepler_periodo(a.a, gm))} s ({fmt(kepler_periodo(a.a, gm) / 60)} min)")
        print(f"Velocidad circular = {fmt(velocidad_circular(a.a, gm))} m/s")
        print(f"Velocidad de escape = {fmt(velocidad_escape(a.a, gm))} m/s")
        print(f"Altura sobre el radio de referencia = {fmt(a.a - rad)} m (supuesto: órbita circular, a = r)")
    elif a.cmd == "hohmann":
        r = hohmann(a.r1, a.r2, CUERPOS[a.cuerpo][0])
        for k, v in r.items():
            print(f"{k} = {fmt(v)}", "s" if k == "tiempo_vuelo" else "m/s")
        print("Supuestos: órbitas circulares coplanares, impulsos instantáneos, problema de dos cuerpos.")
    elif a.cmd == "cohete":
        print(f"dv = {fmt(tsiolkovski(a.isp, a.m0, a.mf))} m/s (sin pérdidas por gravedad ni arrastre)")
    elif a.cmd == "estrella":
        L = luminosidad(a.radio, a.temp)
        print(f"L = {fmt(L)} W = {fmt(L / CONSTANTES['L_sol'][0])} L_sol")
        print(f"Pico de Wien = {fmt(wien_pico(a.temp) * 1e9)} nm")
    elif a.cmd == "fecha-juliana":
        jd = fecha_juliana(a.anio, a.mes, a.dia)
        print(f"JD = {jd}   MJD = {jd - 2400000.5}")
    elif a.cmd == "autotest":
        return autotest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
