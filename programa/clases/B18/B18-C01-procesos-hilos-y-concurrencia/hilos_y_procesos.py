#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B18-C01: hilos, procesos y GIL con un lote de órbitas.

Datos: SIMULADOS (sin datos observados). Cada tarea propaga una órbita circular
en unidades canónicas (GM = 1, radio = 1, velocidad = 1, periodo = 2*pi) con el
integrador leapfrog (kick-drift-kick), en Python puro (tarea limitada por CPU).
Modelo: dos cuerpos; solución analítica x(t) = cos t, y(t) = sin t.
Supuestos: masa puntual central, sin perturbaciones; paso dt fijo.
Validez: demostración de ejecución concurrente; no es un propagador orbital.
Tolerancias: posición final contra la analítica, error < 1e-5 (el error del
leapfrog crece como dt^2); la suma protegida con cerrojo debe ser exacta;
los tiempos son medidas de esta máquina y NO se comparan con un umbral fijo
salvo el solapamiento de esperas (hilos con time.sleep), con holgura amplia.
"""
from __future__ import annotations
import math, os, platform, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PASOS = 600_000          # pasos por órbita
PERIODO = 2 * math.pi
DT = PERIODO / PASOS     # una órbita completa en PASOS pasos
N_TAREAS = 8


def propagar(pasos: int = PASOS, dt: float = DT) -> tuple[float, float]:
    """Propaga una órbita circular con leapfrog KDK. Devuelve (x, y) final."""
    x, y, vx, vy = 1.0, 0.0, 0.0, 1.0
    r3 = (x * x + y * y) ** 1.5
    ax, ay = -x / r3, -y / r3
    for _ in range(pasos):
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
        x += dt * vx
        y += dt * vy
        r3 = (x * x + y * y) ** 1.5
        ax, ay = -x / r3, -y / r3
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
    return x, y


def tarea(_k: int) -> tuple[float, float]:
    return propagar()


def esperar(segundos: float) -> float:
    """Tarea limitada por E/S simulada: libera el GIL mientras duerme."""
    time.sleep(segundos)
    return segundos


def medir(f, *a):
    t0 = time.perf_counter()
    r = f(*a)
    return r, time.perf_counter() - t0


def lote_serie():
    return [tarea(k) for k in range(N_TAREAS)]


def lote_hilos():
    with ThreadPoolExecutor(max_workers=N_TAREAS) as ex:
        return list(ex.map(tarea, range(N_TAREAS)))


def lote_procesos():
    with ProcessPoolExecutor(max_workers=min(N_TAREAS, os.cpu_count() or 1)) as ex:
        return list(ex.map(tarea, range(N_TAREAS)))


def contador_con_cerrojo(n_hilos: int, n_inc: int) -> int:
    cuenta = 0
    cerrojo = threading.Lock()

    def trabajo():
        nonlocal cuenta
        for _ in range(n_inc):
            with cerrojo:
                cuenta += 1

    hs = [threading.Thread(target=trabajo) for _ in range(n_hilos)]
    for h in hs: h.start()
    for h in hs: h.join()
    return cuenta


def prueba(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  CPU lógicas={os.cpu_count()}  "
          f"GIL activo={getattr(sys, '_is_gil_enabled', lambda: True)()}")
    print(f"Tarea: {PASOS} pasos leapfrog; lote de {N_TAREAS} órbitas (simuladas)")

    # Corrección: una vuelta completa debe volver a (1, 0) con error ~ dt^2.
    x, y = propagar()
    err = math.hypot(x - 1.0, y - 0.0)
    print(f"error de posición tras una órbita: {err:.2e} (tolerancia 1e-5)")
    prueba(err < 1e-5, "la órbita no cierra dentro de la tolerancia")

    r_s, t_s = medir(lote_serie)
    r_h, t_h = medir(lote_hilos)
    r_p, t_p = medir(lote_procesos)
    prueba(r_s == r_h == r_p, "los tres modos deben dar resultados idénticos")
    print(f"serie    : {t_s:6.2f} s")
    print(f"8 hilos  : {t_h:6.2f} s  (aceleración {t_s / t_h:4.2f}x)")
    print(f"procesos : {t_p:6.2f} s  (aceleración {t_s / t_p:4.2f}x)")

    # Tareas de espera: los hilos SÍ se solapan porque sleep libera el GIL.
    espera = 0.3
    _, t_es = medir(lambda: [esperar(espera) for _ in range(N_TAREAS)])
    def esperas_hilos():
        with ThreadPoolExecutor(max_workers=N_TAREAS) as ex:
            return list(ex.map(esperar, [espera] * N_TAREAS))
    _, t_eh = medir(esperas_hilos)
    print(f"esperas serie={t_es:.2f} s  esperas con hilos={t_eh:.2f} s")
    prueba(t_eh < 0.5 * t_es, "las esperas con hilos deberían solaparse")

    total = contador_con_cerrojo(8, 50_000)
    print(f"contador con cerrojo: {total} (exacto: {8 * 50_000})")
    prueba(total == 8 * 50_000, "el contador protegido debe ser exacto")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
