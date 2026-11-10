"""B88-C41: ley de control en doble precision (SIL), simple precision y punto fijo Q15 (tipo PIL) (SINTETICO)."""
import math, struct, sys
import numpy as np
print("Python", sys.version.split()[0], "| numpy", np.__version__)
print("Datos SINTETICOS: inercia 1 kg m^2, PD con Kp=4, Kd=4, referencia 1 rad, paso 0,05 s")

dt, T = 0.05, 20.0
n = int(T / dt)
def simular(tipo):
    th = tw = 0.0
    if tipo == "f64": th, w, Kp, Kd, d = np.float64(0), np.float64(0), np.float64(4), np.float64(4), np.float64(dt)
    if tipo == "f32": th, w, Kp, Kd, d = np.float32(0), np.float32(0), np.float32(4), np.float32(4), np.float32(dt)
    tray = []
    if tipo == "q15":
        # Q15: valores en [-1,1) como enteros de 16 bit; ganancias escaladas por 8 para caber (4 -> 0.5 con escala 8)
        S = 8.0
        th_q = 0; w_q = 0
        for _ in range(n):
            e = int(round((1.0 / S) * 32768)) - th_q
            e = max(-32768, min(32767, e))
            u = (4 * e - 4 * w_q)                    # Kp=Kd=4 sobre valores escalados
            u = max(-32768 * 4, min(32767 * 4, u))
            w_q += int(round(u * dt))                # w' = u
            w_q = max(-32768, min(32767, w_q))
            th_q += int(round(w_q * dt))
            th_q = max(-32768, min(32767, th_q))
            tray.append(th_q / 32768 * S)
        return np.array(tray)
    for _ in range(n):
        u = Kp * (type(th)(1) - th) - Kd * w
        w = w + u * d; th = th + w * d
        tray.append(float(th))
    return np.array(tray)
A = simular("f64"); B = simular("f32"); C = simular("q15")
print(f"Valor final: f64 = {A[-1]:.9f} ; f32 = {B[-1]:.9f} ; Q15 = {C[-1]:.6f}")
print(f"Error maximo |f32 - f64| = {np.max(np.abs(B - A)):.3e} rad")
print(f"Error maximo |Q15 - f64| = {np.max(np.abs(C - A)):.3e} rad")
print(f"Error final |f32 - f64| = {abs(B[-1]-A[-1]):.3e} ; |Q15 - f64| = {abs(C[-1]-A[-1]):.3e}")
print(f"epsilon f32 = {np.finfo(np.float32).eps:.3e} ; epsilon f64 = {np.finfo(np.float64).eps:.3e} ; LSB Q15 (escala 8) = {8/32768:.3e}")
# Tolerancia de aceptacion
tol = 1e-3
print(f"Criterio de aceptacion |error| < {tol:.0e} rad: f32 = {np.max(np.abs(B-A)) < tol} ; Q15 = {np.max(np.abs(C-A)) < tol}")
assert np.max(np.abs(B - A)) < 1e-3
print("Pruebas superadas.")
