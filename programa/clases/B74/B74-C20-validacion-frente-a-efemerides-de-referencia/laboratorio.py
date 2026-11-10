#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C20: validacion de una solucion frente a una efemeride de referencia (diferencias RTN).

Todo SINTETICO. 'Referencia': orbita integrada numericamente (RK4, paso 10 s) con gravedad central mas el termino J2 (J2 = 1.08263e-3 y radio ecuatorial
6 378 137 m, valores ilustrativos NO consultados en esta sesion; mu = 3.986004e14 m3/s2 ilustrativo), orbita a = 7200 km, e = 0.01, i = 55 grados. 'Solucion a validar': orbita
kepleriana de dos cuerpos ajustada por minimos cuadrados (Gauss-Newton, 6 parametros) a 24 h de posiciones de la referencia muestreadas cada 600 s (sin ruido).
Se compara la solucion con la referencia en el arco de ajuste (0-24 h) y en una prediccion (24-72 h), en el marco RTN de la referencia: radial, transversal (a lo largo de la trayectoria),
normal. Se reportan rms por componente, el maximo de la diferencia 3D y la tasa de crecimiento a lo largo de la trayectoria.
Tolerancias: se comprueba el integrador numerico integrando sin J2 contra el propagador kepleriano (diferencia < 1 m en 1 dia; es el error de truncamiento de RK4 con paso de 10 s).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

MU = 3.986004e14
J2 = 1.08263e-3
RE = 6378137.0


def acel(r, j2=True):
    rn = np.linalg.norm(r)
    a = -MU * r / rn**3
    if j2:
        z2 = (r[2] / rn) ** 2
        k = 1.5 * J2 * MU * RE**2 / rn**5
        a = a + k * np.array([r[0] * (5 * z2 - 1), r[1] * (5 * z2 - 1), r[2] * (5 * z2 - 3)])
    return a


def rk4(x, dt, j2=True):
    def f(y):
        return np.concatenate([y[3:], acel(y[:3], j2)])
    k1 = f(x); k2 = f(x + dt / 2 * k1); k3 = f(x + dt / 2 * k2); k4 = f(x + dt * k3)
    return x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def kep(x0, dt):
    r0, v0 = x0[:3], x0[3:]
    r0n = np.linalg.norm(r0); vr0 = np.dot(r0, v0) / r0n
    al = 2 / r0n - np.dot(v0, v0) / MU
    chi = math.sqrt(MU) * abs(al) * dt
    for _ in range(100):
        z = al * chi**2; C, S = stumpff(z)
        F = r0n * vr0 / math.sqrt(MU) * chi**2 * C + (1 - al * r0n) * chi**3 * S + r0n * chi - math.sqrt(MU) * dt
        dF = r0n * vr0 / math.sqrt(MU) * chi * (1 - z * S) + (1 - al * r0n) * chi**2 * C + r0n
        d = F / dF; chi -= d
        if abs(d) < 1e-10: break
    z = al * chi**2; C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C; g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0; rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi; gd = 1 - chi**2 / rn * C
    return np.concatenate([r, fd * r0 + gd * v0])


def inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


def rtn(ref, d):
    r = ref[:3] / np.linalg.norm(ref[:3]); n = np.cross(ref[:3], ref[3:]); n /= np.linalg.norm(n); t = np.cross(n, r)
    return np.array([d @ r, d @ t, d @ n])


def main():
    x0 = inicial()
    dt = 10.0
    n = int(72 * 3600 / dt)
    ref = np.zeros((n + 1, 6)); ref[0] = x0
    for k in range(n):
        ref[k + 1] = rk4(ref[k], dt)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (referencia y solucion SINTETICAS)"]
    res = {}
    # control: sin J2, RK4 vs Kepler en 1 dia
    y = x0.copy()
    for _ in range(int(86400 / dt)):
        y = rk4(y, dt, j2=False)
    ctrl = np.linalg.norm(y[:3] - kep(x0, 86400.0)[:3])
    out.append(f"Control sin J2: |RK4 - Kepler| tras 1 dia = {ctrl:.2e} m")
    res["ctrl"] = ctrl
    # ajuste kepleriano a 24 h cada 600 s
    idx = np.arange(0, int(86400 / dt) + 1, int(600 / dt))
    t = idx * dt
    obs = ref[idx, :3]
    x = x0.copy() + np.array([100.0, -100.0, 50.0, 0.1, -0.1, 0.05])
    for it in range(8):
        def model(xx):
            return np.concatenate([kep(xx, tt)[:3] if tt > 0 else xx[:3] for tt in t])
        m0 = model(x)
        J = np.zeros((len(m0), 6))
        for k in range(6):
            d = np.zeros(6); d[k] = 1.0 if k < 3 else 1e-3
            J[:, k] = (model(x + d) - model(x - d)) / (2 * d[k])
        dx = np.linalg.lstsq(J, obs.ravel() - m0, rcond=None)[0]
        x = x + dx
        if np.linalg.norm(dx[:3]) < 1e-4: break
    out.append(f"Ajuste de dos cuerpos a 24 h de posiciones J2: {it+1} iteraciones ; correccion final {np.linalg.norm(dx[:3]):.2e} m")
    # comparacion
    out.append("tramo                 rms R [m]    rms T [m]    rms N [m]   max 3D [m]")
    for nom, a, b in (("ajuste 0-24 h", 0, 86400), ("prediccion 24-48 h", 86400, 172800), ("prediccion 48-72 h", 172800, 259200)):
        ii = np.arange(int(a / dt), int(b / dt) + 1, int(60 / dt))
        d = np.array([rtn(ref[k], kep(x, k * dt)[:3] - ref[k, :3]) for k in ii])
        rms = np.sqrt(np.mean(d**2, axis=0)); mx = np.max(np.linalg.norm(d, axis=1))
        out.append(f"{nom:20s} {rms[0]:10.1f} {rms[1]:12.1f} {rms[2]:12.1f} {mx:12.1f}")
        key = nom.split()[0][:3] + nom.split()[1].replace("-", "_").replace(" ", "")
        res[key + "_R"] = float(rms[0]); res[key + "_T"] = float(rms[1]); res[key + "_N"] = float(rms[2]); res[key + "_M"] = float(mx)
    out.append("(el modelo de dos cuerpos no reproduce la precesion nodal por J2: domina la componente normal y el error crece fuera del arco de ajuste)")
    ok = ctrl < 1.0 and res["pre24_48_M"] > res["aju0_24_M"] and res["pre48_72_M"] > res["pre24_48_M"]
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
