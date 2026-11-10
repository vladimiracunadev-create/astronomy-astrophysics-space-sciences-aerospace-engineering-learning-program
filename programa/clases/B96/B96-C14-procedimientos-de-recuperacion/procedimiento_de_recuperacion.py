"""B96-C14: procedimiento de recuperacion SINTETICO con verificacion, reintentos y ventanas de contacto (Monte Carlo)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: pasos, duraciones y probabilidades ficticias; semilla 96")
# (nombre, duracion s, probabilidad de exito de un intento)
pasos = [("Confirmar estado SEGURO", 30, 0.99), ("Aislar causa (apagar carga)", 25, 0.98), ("Cargar tabla de recuperacion", 60, 0.95),
         ("Reiniciar subsistema", 40, 0.90), ("Verificar telemetria", 35, 0.97), ("Volver a NOMINAL", 30, 0.95)]
REINT = 2                    # reintentos permitidos por paso (3 intentos en total)
VENTANA = 420.0              # s de contacto por pasada
nominal = sum(d for _, d, _ in pasos)
print(f"Duracion nominal sin fallos = {nominal} s ; ventana = {VENTANA:.0f} s ; cabe en una pasada: {'SI' if nominal <= VENTANA else 'NO'}")
# probabilidad analitica de exito del procedimiento completo (hasta 3 intentos por paso)
p_ok = 1.0
for _, d, p in pasos: p_ok *= 1 - (1 - p)**(REINT + 1)
print(f"Probabilidad analitica de completar el procedimiento = {p_ok:.6f}")
def simula(rng):
    t = 0.0; ok = True
    for _, d, p in pasos:
        hecho = False
        for _ in range(REINT + 1):
            t += d
            if rng.random() < p: hecho = True; break
        if not hecho: ok = False; break
    return ok, t
rng = random.Random(96)
M = 200000
oks = 0; tiempos = []; en_una = 0; pasadas = []
for _ in range(M):
    ok, t = simula(rng)
    if ok:
        oks += 1; tiempos.append(t)
        if t <= VENTANA: en_una += 1
print(f"Monte Carlo ({M} corridas): exito = {oks/M:.6f} ; tiempo medio de los exitosos = {sum(tiempos)/len(tiempos):.1f} s ; max = {max(tiempos):.0f} s")
print(f"Exitos que terminan dentro de una pasada = {en_una/oks*100:.2f} % de los exitosos")
sig = (p_ok*(1-p_ok)/M)**0.5
print(f"Diferencia analitica/simulada = {abs(oks/M - p_ok):.2e} (4 sigma = {4*sig:.2e})")
assert abs(oks/M - p_ok) < 4*sig
assert nominal <= VENTANA
assert all(t >= nominal for t in tiempos)
# sensibilidad: sin reintentos
p0 = 1.0
for _, d, p in pasos: p0 *= p
print(f"Sin reintentos: probabilidad = {p0:.4f} ; con {REINT} reintentos = {p_ok:.4f}")
assert p_ok > p0
print("Pruebas superadas.")
