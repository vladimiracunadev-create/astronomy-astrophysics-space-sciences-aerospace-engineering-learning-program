"""B67-C06: onda termica en regolito seco y perdida de hielo enterrado (SINTETICO).

1) Conduccion 1D:  dT/dt = kappa d2T/dz2, z hacia abajo [m], T [K], kappa [m2/s].
   Frontera superior T(0,t) = Tm + dT cos(w t) ; inferior sin flujo.
   Solucion analitica de estado periodico:  T = Tm + dT exp(-z/delta) cos(w t - z/delta),
   delta = sqrt(2 kappa / w).  Se resuelve con Crank-Nicolson y se compara.
2) Hielo enterrado a profundidad d bajo regolito seco. Flujo maximo de vapor de la
   superficie del hielo (Hertz-Knudsen, alpha=1) multiplicado por una transmision
   W = 1/(1 + 3 d / (8 r_p)) de poro cilindrico largo (relacion de ingenieria,
   NO consultada; r_p = radio efectivo de poro, ilustrativo).
   Presion de vapor: Murphy y Koop (2005), ec. (7), T > 110 K.
kappa = 1e-8 m2/s, Tm = 140 K, dT = 80 K, periodo 29,53 d: valores ILUSTRATIVOS.
Requiere solo numpy.
"""
import sys
import numpy as np

KB = 1.380649e-23
M = 18.01528 * 1.66053907e-27   # valor de referencia estandar, no consultado
KAPPA = 1.0e-8
TM, DT = 140.0, 80.0
PERIODO = 29.53 * 86400.0
W_ANG = 2 * np.pi / PERIODO
DELTA = np.sqrt(2 * KAPPA / W_ANG)
RP = 50e-6
ANIO = 365.25 * 86400.0


def p_hielo(T):
    T = np.asarray(T, float)
    return np.exp(9.550426 - 5723.265 / T + 3.53068 * np.log(T) - 0.00728332 * T)


def flujo(T):
    return M * p_hielo(T) / np.sqrt(2 * np.pi * M * KB * T)


def transmision(d):
    return 1.0 / (1.0 + 3.0 * d / (8.0 * RP))


def crank_nicolson(nz=150, dz=0.01, pasos_por_periodo=720, periodos=6):
    z = np.arange(nz) * dz
    dt = PERIODO / pasos_por_periodo
    r = KAPPA * dt / dz ** 2
    A = np.zeros((nz, nz))
    B = np.zeros((nz, nz))
    for i in range(1, nz - 1):
        A[i, i - 1:i + 2] = [-r / 2, 1 + r, -r / 2]
        B[i, i - 1:i + 2] = [r / 2, 1 - r, r / 2]
    A[0, 0] = B[0, 0] = 1.0
    A[-1, -1], A[-1, -2] = 1 + r, -r      # sin flujo (nodo fantasma)
    B[-1, -1], B[-1, -2] = 1 - r, r
    Ainv = np.linalg.inv(A)
    T = np.full(nz, TM)
    hist = []
    total = pasos_por_periodo * periodos
    for k in range(1, total + 1):
        b = B @ T
        b[0] = TM + DT * np.cos(W_ANG * k * dt)
        T = Ainv @ b
        if k > total - pasos_por_periodo:
            hist.append(T.copy())
    return z, np.array(hist), dt


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS ILUSTRATIVOS: kappa, temperaturas y radio de poro inventados para la clase")
    print(f"delta = sqrt(2 kappa / w) = {DELTA:.4f} m (periodo {PERIODO / 86400:.2f} d)")
    z, H, dt = crank_nicolson()
    amp = (H.max(0) - H.min(0)) / 2
    print("z [m]   amplitud numerica [K]  amplitud analitica [K]  error relativo")
    mx = 0.0
    for zz in (0.0, DELTA, 2 * DELTA, 3 * DELTA):
        j = int(round(zz / 0.01))
        an = DT * np.exp(-z[j] / DELTA)
        er = abs(amp[j] - an) / an
        mx = max(mx, er)
        print(f"{z[j]:6.2f}   {amp[j]:9.4f}            {an:9.4f}               {100 * er:.2f} %")
    assert mx < 0.03, "la onda numerica no concuerda con la analitica"
    # desfase en z = delta: debe ser ~ 1 rad
    j = int(round(DELTA / 0.01))
    t_pico = np.argmax(H[:, j]) * dt
    t_pico0 = np.argmax(H[:, 0]) * dt
    lag = ((t_pico - t_pico0) % PERIODO) * W_ANG
    print(f"Desfase en z = delta: {lag:.3f} rad (analitico 1,000 rad)")
    assert abs(lag - 1.0) < 0.1
    # perdida de hielo enterrado a profundidad d
    print("Hielo enterrado: perdida anual por unidad de area, T(t) numerica frente a T media")
    print("d [m]  T media [K]  amp [K]  W        perdida/anio con T(t) [kg/m2]  con T media [kg/m2]  cociente")
    for d in (0.1, 0.2, 0.3, 0.5):
        j = int(round(d / 0.01))
        Tt = H[:, j]
        f_t = np.mean(flujo(Tt)) * transmision(d) * ANIO
        f_m = float(flujo(Tt.mean())) * transmision(d) * ANIO
        print(f"{d:5.2f}  {Tt.mean():8.3f}   {amp[j]:6.3f}  {transmision(d):.2e}  {f_t:14.4e}            {f_m:14.4e}      {f_t / f_m:.3f}")
        assert f_t >= f_m * (1 - 1e-9)    # desigualdad de Jensen (flujo convexo en T)
    # espesor de hielo perdido en 1e6 anios (densidad 917 kg/m3, referencia estandar no consultada)
    d = 0.3
    j = int(round(d / 0.01))
    f = np.mean(flujo(H[:, j])) * transmision(d)
    esp = f * 1e6 * ANIO / 917.0
    print(f"A d = {d} m: espesor de hielo perdido en 1e6 anios = {esp:.3f} m (solo la parte de vapor que escapa; cota superior)")
    # sensibilidad a la profundidad: duplicar d reduce W a la mitad, pero sobre todo amortigua la onda termica
    f1 = np.mean(flujo(H[:, 10])) * transmision(0.1)
    f2 = np.mean(flujo(H[:, 20])) * transmision(0.2)
    print(f"Perdida a 0,1 m / perdida a 0,2 m = {f1 / f2:.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
