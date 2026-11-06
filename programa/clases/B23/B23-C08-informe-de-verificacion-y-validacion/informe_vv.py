#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C08: generación de un informe de verificación y validación (V&V).

Datos: SINTÉTICOS para la verificación (órbita a = 1 au, e = 0.0167, inicio en el perihelio) y
EFEMÉRIDE oficial para la validación (NASA/JPL Horizons API v1.2, Tierra 399, centro Sol, DE441,
eclíptica J2000, au y au/d, TDB), tres épocas copiadas a mano de B23-C05 (JD 2460676.5, 2460767.5,
2461041.5).
Modelo bajo prueba: dos cuerpos con Sol fijo; integradores Verlet (orden 2) y RK4 (orden 4).
Constantes: GM_sol nominal IAU 2015 B3 y 1 au = 149597870700 m (IAU 2012 B2).
Supuestos: sin otros cuerpos; plano; el centro es el Sol y el objeto es el geocentro.
Validez: órbitas de e ≈ 0.0167, arcos de hasta 1 año, pasos de 0.25 a 2 d.
Tolerancias: cada criterio declara su umbral ANTES de calcularse (lista CRITERIOS).
Uso previsto del informe: propagar la Tierra hasta 91 d con error <= 1e-3 au (educativo).
Regla de decisión: «APTO para el uso previsto» solo si todos los criterios marcados «uso» se cumplen;
los demás se reportan como advertencias.
"""
from __future__ import annotations
import hashlib, math, platform, sys
from pathlib import Path
import numpy as np
import scipy

AU = 149597870700.0
MU = 1.3271244e20*86400.0**2/AU**3
A, E = 1.0, 0.0167
N_MED = math.sqrt(MU/A**3)
T_ORB = 2*math.pi/N_MED

HORIZONS = {  # JD TDB: (x, y, z, vx, vy, vz) en au y au/d
    2460676.5: (-1.786834409731047E-01, 9.669827953774551E-01, -5.109423915082682E-05,
                -1.720473858166942E-02, -3.193533189307208E-03, 5.457174067040888E-09),
    2460767.5: (-9.771032044732010E-01, -2.104323089919837E-01, 1.556486123938526E-05,
                3.348948088761836E-03, -1.688703398173705E-02, 6.503050694285350E-07),
    2461041.5: (-1.742814809205833E-01, 9.677589202546031E-01, -5.944511017526243E-05,
                -1.720454736868129E-02, -3.116607022544302E-03, 2.371782782240443E-07),
}


def kepler_E(M, e):
    E_ = M if e < 0.8 else math.pi
    for _ in range(60):
        d = (E_ - e*math.sin(E_) - M)/(1 - e*math.cos(E_))
        E_ -= d
        if abs(d) < 1e-15:
            break
    return E_


def exacto(t):
    M = math.fmod(N_MED*t, 2*math.pi)
    Ex = kepler_E(M, E)
    s, c = math.sin(Ex), math.cos(Ex)
    q, d = math.sqrt(1 - E*E), 1 - E*c
    return (np.array([A*(c - E), A*q*s]), np.array([-A*N_MED*s/d, A*N_MED*q*c/d]))


def acel(r):
    return -MU*r/np.hypot(r[0], r[1])**3


def verlet(r, v, h):
    vm = v + 0.5*h*acel(r)
    rn = r + h*vm
    return rn, vm + 0.5*h*acel(rn)


def rk4(r, v, h):
    k1r, k1v = v, acel(r)
    k2r, k2v = v + 0.5*h*k1v, acel(r + 0.5*h*k1r)
    k3r, k3v = v + 0.5*h*k2v, acel(r + 0.5*h*k2r)
    k4r, k4v = v + h*k3v, acel(r + h*k3r)
    return (r + h/6*(k1r + 2*k2r + 2*k3r + k4r), v + h/6*(k1v + 2*k2v + 2*k3v + k4v))


def err_final(paso, N):
    h = T_ORB/N
    r, v = exacto(0.0)
    for _ in range(N):
        r, v = paso(r, v, h)
    return float(np.hypot(*(r - exacto(T_ORB)[0])))


def orden_obs(paso, Ns=(200, 400)):
    e1, e2 = err_final(paso, Ns[0]), err_final(paso, Ns[1])
    return math.log(e1/e2)/math.log(2)


def energia_max(paso, h, dias):
    r, v = exacto(0.0)
    e0 = 0.5*(v @ v) - MU/np.hypot(*r)
    m = 0.0
    for _ in range(round(dias/h)):
        r, v = paso(r, v, h)
        m = max(m, abs((0.5*(v @ v) - MU/np.hypot(*r) - e0)/e0))
    return m


def kepler3d_error(jd_fin):
    from scipy.integrate import solve_ivp
    j0 = 2460676.5
    s0 = np.array(HORIZONS[j0])

    def f(t, y):
        return np.concatenate([y[3:], -MU*y[:3]/np.linalg.norm(y[:3])**3])
    s = solve_ivp(f, (0, jd_fin - j0), s0, method="DOP853", rtol=1e-12, atol=1e-14)
    return float(np.linalg.norm(s.y[:3, -1] - np.array(HORIZONS[jd_fin])[:3]))


def sha_script():
    return hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def evaluar():
    """Cada criterio: (id, tipo, descripción, valor, umbral, operador, ¿cuenta para el uso previsto?)."""
    c_energia = energia_max(verlet, 2.0, 3652.5)/2.0**2           # constante c estimada en h = 2 d
    crit = [
        ("V1", "verificación", "solución exacta: retorno tras un período [au]",
         float(np.hypot(*(exacto(T_ORB)[0] - exacto(0.0)[0]))), 1e-12, "<=", True),
        ("V2", "verificación", "orden observado de Verlet (N 200→400), abs(p-2)",
         abs(orden_obs(verlet) - 2), 0.15, "<=", True),
        ("V3", "verificación", "orden observado de RK4 (N 200→400), abs(p-4)",
         abs(orden_obs(rk4) - 4), 0.15, "<=", True),
        ("V4", "verificación", "energía Verlet h=1 d, 10 años, error / (1.5·c·h²)",
         energia_max(verlet, 1.0, 3652.5)/(1.5*c_energia*1.0**2), 1.0, "<=", True),
        ("D1", "validación", "posición a +91 d frente a Horizons [au]",
         kepler3d_error(2460767.5), 1e-3, "<=", True),
        ("D2", "validación", "posición a +365 d frente a Horizons [au]",
         kepler3d_error(2461041.5), 5e-3, "<=", False),
    ]
    return crit


def veredicto(valor, umbral, op):
    return valor <= umbral if op == "<=" else valor >= umbral


def informe(crit) -> str:
    L = []
    L.append("# Informe de verificación y validación — propagador de dos cuerpos (ejemplo)")
    L.append("")
    L.append("## 1. Uso previsto y alcance")
    L.append("Propagar la posición de la Tierra hasta 91 d desde un estado inicial, con error ≤ 1e-3 au (uso educativo; no operativo).")
    L.append("")
    L.append("## 2. Modelo, supuestos y dominio")
    L.append("Dos cuerpos con Sol fijo; GM☉ nominal IAU 2015 B3; 1 au = 149 597 870 700 m; Verlet y RK4. "
             "Dominio: e ≈ 0,0167, arcos ≤ 1 año, pasos 0,25–2 d. Datos de verificación: sintéticos. Datos de validación: efeméride oficial (JPL Horizons, DE441).")
    L.append("")
    L.append("## 3. Criterios, resultados y veredictos")
    L.append("| ID | Tipo | Criterio | Valor | Umbral | Uso previsto | Veredicto |")
    L.append("|---|---|---|---|---|---|---|")
    for cid, tipo, desc, val, um, op, uso in crit:
        ok = veredicto(val, um, op)
        L.append(f"| {cid} | {tipo} | {desc} | {val:.3e} | {op} {um:g} | {'sí' if uso else 'no'} | {'CUMPLE' if ok else 'NO CUMPLE'} |")
    L.append("")
    fallos_uso = [c for c in crit if c[6] and not veredicto(c[3], c[4], c[5])]
    fallos_otros = [c for c in crit if not c[6] and not veredicto(c[3], c[4], c[5])]
    L.append("## 4. Advertencias")
    if not fallos_uso and not fallos_otros:
        L.append("Ninguna.")
    for c in fallos_uso + fallos_otros:
        L.append(f"- Criterio {c[0]} no cumplido ({c[2]}): valor {c[3]:.3e} frente a umbral {c[5]} {c[4]:g}"
                 + (" — afecta al uso previsto." if c[6] else " — fuera del uso previsto; limita la extrapolación."))
    L.append("")
    L.append("## 5. Decisión")
    L.append("**APTO para el uso previsto**" if not fallos_uso else "**NO APTO para el uso previsto**")
    L.append("")
    L.append("## 6. Incertidumbre y límites")
    L.append("Sin estimación estadística de incertidumbre; los valores son diferencias deterministas con una sola efeméride y un solo estado inicial. "
             "No validado frente a observaciones. No usar para navegación, predicción de encuentros ni decisiones de operación.")
    L.append("")
    L.append("## 7. Procedencia")
    L.append(f"Python {platform.python_version()}, NumPy {np.__version__}, SciPy {scipy.__version__}; huella del script (SHA-256, LF): {sha_script()[:16]}…")
    return "\n".join(L)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    crit = evaluar()
    texto = informe(crit)
    print(texto)
    print("\n--- pruebas del generador ---")
    # Estructura: siete secciones numeradas
    for k in range(1, 8):
        prueba(f"## {k}. " in texto, f"falta la sección {k}")
    # Cada criterio tiene valor, umbral y veredicto en el informe
    for c in crit:
        prueba(f"| {c[0]} |" in texto, f"falta el criterio {c[0]}")
    # Consistencia de la decisión con los criterios
    fallos_uso = [c for c in crit if c[6] and not veredicto(c[3], c[4], c[5])]
    prueba(("APTO para el uso previsto" in texto and "NO APTO" not in texto) == (not fallos_uso),
           "la decisión coincide con los criterios del uso previsto")
    # Cada criterio no cumplido produce una advertencia
    nc = [c for c in crit if not veredicto(c[3], c[4], c[5])]
    prueba(all(f"Criterio {c[0]} no cumplido" in texto for c in nc), "toda falla aparece como advertencia")
    # Control negativo: un valor corrompido cambia la decisión
    malo = [list(c) for c in crit]
    malo[4][3] = 5e-3
    texto2 = informe([tuple(c) for c in malo])
    prueba("NO APTO" in texto2, "un criterio de uso que falla cambia la decisión")
    print("Pruebas del informe superadas.")


if __name__ == "__main__":
    main()
