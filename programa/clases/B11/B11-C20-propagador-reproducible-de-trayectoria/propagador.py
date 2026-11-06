#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C20: propagador reproducible de trayectoria con pruebas.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m (valores
nominales IAU 2015, Res. B3). Órbita circular a 400 km de altitud y órbita
elíptica a = 26 560 km, e = 0.30 son ILUSTRATIVAS (no de una misión concreta).
Modelo: dos cuerpos, plano inercial, masa del satélite despreciable; opcionalmente
una aceleración constante SINTÉTICA de perturbación (para probar que la huella
cambia). Referencia independiente: solución de Kepler (Newton sobre M = E - e sin E).
Métodos: RK4 de paso fijo y leapfrog (kick-drift-kick), seleccionables.
Reproducibilidad: toda la entrada vive en una configuración declarada; el programa
imprime versiones de Python y plataforma y una huella SHA-256 de la trayectoria
redondeada a 1e-6 m (el redondeo evita diferencias de la última cifra entre
plataformas; no garantiza igualdad bit a bit entre máquinas distintas).
Supuestos: sin atmósfera, achatamiento ni terceros cuerpos. Validez: n h << 1.
Tolerancia: error de posición frente a Kepler < 1 m en una vuelta circular y
< 100 m en 5 vueltas elípticas con RK4; deriva de energía de RK4 < 1e-7 por vuelta;
orden observado de RK4 en [3.5, 4.5]; huella idéntica en dos corridas y distinta si
cambia la configuración; leapfrog reversible a 1e-4 m.
"""
from __future__ import annotations
import hashlib, json, math, platform, sys
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Config:
    gm: float = 3.986004e14            # m3/s2, valor nominal IAU 2015
    x0: float = 6.7781e6
    y0: float = 0.0
    vx0: float = 0.0
    vy0: float = 7668.578703685696
    t_final: float = 5553.579089
    n_pasos: int = 400
    metodo: str = "rk4"                # "rk4" | "leapfrog"
    pert_ax: float = 0.0               # aceleración constante sintética, m/s2
    pert_ay: float = 0.0


def aceleracion(c: Config, x: float, y: float):
    r3 = (x * x + y * y) ** 1.5
    return -c.gm * x / r3 + c.pert_ax, -c.gm * y / r3 + c.pert_ay


def paso_rk4(c: Config, s, h):
    def F(u):
        ax, ay = aceleracion(c, u[0], u[1])
        return (u[2], u[3], ax, ay)
    cmb = lambda k, q: tuple(si + h * q * ki for si, ki in zip(s, k))
    k1 = F(s); k2 = F(cmb(k1, .5)); k3 = F(cmb(k2, .5)); k4 = F(cmb(k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def paso_leapfrog(c: Config, s, h):
    x, y, vx, vy = s
    ax, ay = aceleracion(c, x, y)
    vx += 0.5 * h * ax; vy += 0.5 * h * ay
    x += h * vx; y += h * vy
    ax, ay = aceleracion(c, x, y)
    vx += 0.5 * h * ax; vy += 0.5 * h * ay
    return (x, y, vx, vy)


def propagar(c: Config):
    paso = {"rk4": paso_rk4, "leapfrog": paso_leapfrog}[c.metodo]
    h = c.t_final / c.n_pasos
    s = (c.x0, c.y0, c.vx0, c.vy0)
    tray = [s]
    for _ in range(c.n_pasos):
        s = paso(c, s, h)
        tray.append(s)
    return tray


def energia(c: Config, s):
    return 0.5 * (s[2] ** 2 + s[3] ** 2) - c.gm / math.hypot(s[0], s[1])


def huella(c: Config, tray):
    txt = json.dumps(asdict(c), sort_keys=True) + "\n" + "\n".join(
        " ".join(f"{v:.6f}" for v in s) for s in tray)
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()


def kepler(c: Config, t):
    """Referencia independiente (sin perturbación), para estado inicial en el perigeo."""
    r0 = math.hypot(c.x0, c.y0)
    v2 = c.vx0**2 + c.vy0**2
    a = 1 / (2 / r0 - v2 / c.gm)
    h = c.x0 * c.vy0 - c.y0 * c.vx0
    e = math.sqrt(max(0.0, 1 - h * h / (c.gm * a)))
    b = a * math.sqrt(1 - e * e)
    n = math.sqrt(c.gm / a**3)
    M = n * t
    E = M
    for _ in range(100):
        dE = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= dE
        if abs(dE) < 1e-15:
            break
    Ed = n / (1 - e * math.cos(E))
    return (a * (math.cos(E) - e), b * math.sin(E), -a * math.sin(E) * Ed, b * math.cos(E) * Ed), 2 * math.pi / n


def error_pos(c: Config, tray):
    h = c.t_final / c.n_pasos
    return max(math.hypot(s[0] - kepler(c, i * h)[0][0], s[1] - kepler(c, i * h)[0][1]) for i, s in enumerate(tray))


if __name__ == "__main__":
    print(f"Python {platform.python_version()} en {platform.system()} ({platform.machine()})")
    GM = 3.986004e14
    # caso circular de 400 km, una vuelta
    a = 6.3781e6 + 4e5
    T = 2 * math.pi * math.sqrt(a**3 / GM)
    cc = Config(x0=a, vy0=math.sqrt(GM / a), t_final=T, n_pasos=400)
    tray = propagar(cc)
    e1 = error_pos(cc, tray)
    de = (energia(cc, tray[-1]) - energia(cc, tray[0])) / abs(energia(cc, tray[0]))
    h1 = huella(cc, tray)
    print(f"[circular, RK4, 400 pasos, 1 vuelta] error máx de posición = {e1:.4e} m ; d(energía)/|e0| = {de:+.3e}")
    print(f"  huella SHA-256: {h1}")
    assert e1 < 1.0 and abs(de) < 1e-7

    # determinismo y sensibilidad a la configuración
    assert huella(cc, propagar(cc)) == h1
    from dataclasses import replace
    h2 = huella(replace(cc, n_pasos=401), propagar(replace(cc, n_pasos=401)))
    h3 = huella(replace(cc, pert_ax=1e-9), propagar(replace(cc, pert_ax=1e-9)))
    assert h2 != h1 and h3 != h1
    print("  determinismo: dos corridas dan la misma huella; cambiar pasos o añadir 1e-9 m/s2 la cambia")

    # orden observado de RK4
    errs = []
    for N in (100, 200, 400, 800):
        c2 = replace(cc, n_pasos=N)
        errs.append(error_pos(c2, propagar(c2)))
    ordenes = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
    print("  error máx por N=100,200,400,800: " + ", ".join(f"{x:.3e}" for x in errs) + " m ; órdenes " + " ".join(f"{p:.2f}" for p in ordenes))
    assert all(3.5 < p < 4.5 for p in ordenes)

    # elíptica, 5 vueltas
    aE, eE = 26_560e3, 0.30
    TE = 2 * math.pi * math.sqrt(aE**3 / GM)
    ce = Config(x0=aE * (1 - eE), vy0=math.sqrt(GM * (1 + eE) / (aE * (1 - eE))), t_final=5 * TE, n_pasos=5 * 1000)
    trayE = propagar(ce)
    eE_ = error_pos(ce, trayE)
    dE = (energia(ce, trayE[-1]) - energia(ce, trayE[0])) / abs(energia(ce, trayE[0]))
    print(f"[elíptica e=0.30, RK4, 1000 pasos/vuelta, 5 vueltas] error máx = {eE_:.4e} m ; d(energía)/|e0| = {dE:+.3e}")
    print(f"  huella SHA-256: {huella(ce, trayE)}")
    assert eE_ < 100.0

    # leapfrog: reversibilidad
    cl = replace(cc, metodo="leapfrog", n_pasos=200, t_final=10 * T)
    tr = propagar(cl)
    s = tr[-1]
    inv = replace(cl, x0=s[0], y0=s[1], vx0=-s[2], vy0=-s[3])
    tb = propagar(inv)
    rev = math.hypot(tb[-1][0] - cc.x0, tb[-1][1] - cc.y0)
    print(f"[leapfrog, 10 vueltas, 200 pasos] vuelta atrás: error de retorno = {rev:.2e} m")
    assert rev < 1e-4

    manifest = {"programa": "propagador.py", "python": platform.python_version(), "plataforma": platform.platform(),
                "configuracion": asdict(cc), "huella_sha256": h1, "datos": "simulados; GM nominal IAU 2015; órbita ilustrativa"}
    print("manifiesto de resultado:", json.dumps(manifest, sort_keys=True)[:200] + "...")
    print("Pruebas superadas.")
