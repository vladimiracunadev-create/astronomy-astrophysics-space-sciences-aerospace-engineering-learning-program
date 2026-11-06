#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B18-C02: paso de mensajes con MPI (mpi4py).

Ejecutar con:  mpiexec -n 4 python mensajes_mpi.py
Datos: SIMULADOS/ANALÍTICOS. (1) pi = integral de 0 a 1 de 4/(1+x^2) dx por la
regla del punto medio, repartida por rangos; (2) un lote de órbitas circulares
sintéticas (unidades canónicas GM = r = 1) repartido con scatter.
Modelo: SPMD (todos los procesos ejecutan este mismo programa; cada uno tiene
su rango). Comunicación: sendrecv en anillo, bcast, scatter, reduce/allreduce,
gather y Send/Recv con buffers frente a send/recv con pickle.
Supuestos: comunicador MPI.COMM_WORLD; N de intervalos divisible por el tamaño
solo para el reparto del lote (el reparto de la integral admite resto).
Validez: demostración didáctica; los tiempos dependen de la implementación MPI
y de la máquina (aquí, memoria compartida en un solo equipo).
Tolerancias: |pi_calculado - math.pi| < 1e-9; sumas exactas de enteros.
"""
from __future__ import annotations
import math, platform, sys, time
import numpy as np

try:
    from mpi4py import MPI
except ImportError:  # pragma: no cover
    raise SystemExit("Falta mpi4py y un entorno MPI (ver sección 17 de la clase).")

comm = MPI.COMM_WORLD
rango, tam = comm.Get_rank(), comm.Get_size()


def decir(*a):
    if rango == 0:
        print(*a, flush=True)


def prueba(cond: bool, msg: str) -> None:
    """Prueba colectiva: si falla en cualquier rango, todos se detienen."""
    ok = comm.allreduce(bool(cond), op=MPI.LAND)
    if not ok:
        if rango == 0:
            print(f"PRUEBA FALLIDA: {msg}", flush=True)
        comm.Abort(1)


def propagar(pasos: int, dt: float) -> tuple[float, float]:
    x, y, vx, vy = 1.0, 0.0, 0.0, 1.0
    r3 = (x * x + y * y) ** 1.5
    ax, ay = -x / r3, -y / r3
    for _ in range(pasos):
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        r3 = (x * x + y * y) ** 1.5
        ax, ay = -x / r3, -y / r3
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
    return x, y


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    decir(f"Python {platform.python_version()}  NumPy {np.__version__}  "
          f"{MPI.Get_library_version().splitlines()[0]}  procesos={tam}")

    # 1) Punto a punto: anillo. Cada rango envía su rango al siguiente.
    vecino_der, vecino_izq = (rango + 1) % tam, (rango - 1) % tam
    recibido = comm.sendrecv(rango, dest=vecino_der, source=vecino_izq)
    prueba(recibido == vecino_izq, "el anillo debe entregar el rango del vecino izquierdo")
    decir(f"anillo: cada rango recibió el rango de su vecino izquierdo (rango 0 recibió {recibido})")

    # 2) Difusión de parámetros (bcast) desde el rango 0.
    par = {"n": 1_000_000} if rango == 0 else None
    par = comm.bcast(par, root=0)
    n = par["n"]

    # 3) Integral repartida: pi con punto medio; cada rango suma sus intervalos.
    t0 = MPI.Wtime()
    h = 1.0 / n
    local = 0.0
    for i in range(rango, n, tam):          # reparto cíclico
        x = (i + 0.5) * h
        local += 4.0 / (1.0 + x * x)
    local *= h
    pi_reduce = comm.reduce(local, op=MPI.SUM, root=0)   # solo el rango 0 lo recibe
    pi_todos = comm.allreduce(local, op=MPI.SUM)         # todos lo reciben
    t_int = MPI.Wtime() - t0
    err = abs(pi_todos - math.pi)
    decir(f"pi = {pi_todos:.12f}  error = {err:.2e}  (n = {n}, {t_int:.3f} s)")
    prueba(err < 1e-9, "pi fuera de tolerancia")
    if rango == 0:
        prueba(abs(pi_reduce - pi_todos) < 1e-12, "reduce y allreduce deben coincidir")
    else:
        prueba(True, "")

    # 4) Lote de órbitas con scatter / gather (versión con objetos).
    pasos_por_orbita, n_orb = 20_000, 4 * tam
    dt = 2 * math.pi / pasos_por_orbita
    lote = [pasos_por_orbita] * n_orb if rango == 0 else None
    trozos = None
    if rango == 0:
        trozos = [lote[i::tam] for i in range(tam)]
    mios = comm.scatter(trozos, root=0)
    finales = [propagar(p, dt) for p in mios]
    todos = comm.gather(finales, root=0)
    if rango == 0:
        planos = [f for g in todos for f in g]
        peor = max(math.hypot(x - 1.0, y) for x, y in planos)
        decir(f"órbitas: {len(planos)} propagadas; peor error de cierre = {peor:.2e}")
        prueba(len(planos) == n_orb and peor < 1e-5, "órbitas fuera de tolerancia")
    else:
        prueba(True, "")

    # 5) Eco (ida y vuelta) entre los rangos 0 y 1: objetos (pickle) frente a buffers.
    if tam >= 2:
        datos = np.arange(2_000_000, dtype="f8")
        t_obj = t_buf = 0.0
        ok = True
        if rango == 0:
            t0 = MPI.Wtime()
            comm.send(datos, dest=1, tag=7); a = comm.recv(source=1, tag=7)
            t_obj = MPI.Wtime() - t0
            b = np.empty_like(datos)
            t0 = MPI.Wtime()
            comm.Send([datos, MPI.DOUBLE], dest=1, tag=8)
            comm.Recv([b, MPI.DOUBLE], source=1, tag=8)
            t_buf = MPI.Wtime() - t0
            ok = bool(np.array_equal(a, datos) and np.array_equal(b, datos))
        elif rango == 1:
            a = comm.recv(source=0, tag=7); comm.send(a, dest=0, tag=7)
            b = np.empty_like(datos)
            comm.Recv([b, MPI.DOUBLE], source=0, tag=8); comm.Send([b, MPI.DOUBLE], dest=0, tag=8)
        decir(f"eco de 2 x 10^6 doubles (16 MB, ida y vuelta): pickle = {t_obj:.4f} s ; buffer = {t_buf:.4f} s ; datos íntegros = {ok}")
        prueba(ok, "los datos recibidos deben ser idénticos")
    decir("Pruebas superadas.")


if __name__ == "__main__":
    main()
