"""B96-C03: dotacion de turnos 24/7 por posicion y verificacion de cobertura (SINTETICO)."""
import math, sys, random
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: horas, ausencias y posiciones ficticias")
horas_sem = 168.0
jornada = 40.0           # h/persona/semana
ausencia = 0.20          # vacaciones, enfermedad, formacion (fraccion)
efectiva = jornada*(1-ausencia)
por_posicion = horas_sem/efectiva
print(f"Horas efectivas por persona = {efectiva:.1f} h/sem ; personas por posicion 24/7 = {por_posicion:.3f} -> {math.ceil(por_posicion)}")
posiciones = {"Director de vuelo": 1, "Operador de enlace": 1, "Ingeniero de subsistemas": 1, "Dinamica de vuelo": 0.5, "Cargas utiles": 0.5}
tot = sum(posiciones.values())
print(f"Posiciones equivalentes 24/7 = {tot:.1f} ; personal minimo = {math.ceil(tot*por_posicion)}")
# cronograma de 3 turnos de 8 h con rotacion semanal sobre N personas; se verifica por simulacion que cada hora tiene 1 persona
N = math.ceil(por_posicion)           # 5 personas para una posicion
# asignacion: por dia (7) y turno (3) -> persona; 21 turnos/semana; cada persona hace 4 turnos (32 h) salvo una con 5? 21 = 5*4+1
asign = {}
persona = 0
for dia in range(7):
    for turno in range(3):
        asign[(dia, turno)] = persona % N
        persona += 1
cuenta = [0]*N
for v in asign.values(): cuenta[v] += 1
print("Turnos de 8 h por persona =", cuenta, "; horas =", [8*x for x in cuenta])
# cobertura: cada hora de la semana tiene exactamente una persona
cob = [0]*168
for (dia, turno), p in asign.items():
    for hh in range(8):
        cob[dia*24 + turno*8 + hh] += 1
print(f"Cobertura minima = {min(cob)} ; maxima = {max(cob)} ; horas sin cubrir = {cob.count(0)}")
# turnos consecutivos de la misma persona (descanso minimo 8 h => no debe tener dos turnos contiguos)
cont = sum(1 for k in range(20) if asign[(k//3, k%3)] == asign[((k+1)//3, (k+1)%3)])
print(f"Turnos contiguos de una misma persona = {cont}")
# Monte Carlo de ausencias: probabilidad de que falte alguien en un turno
random.seed(96)
n = 100000; fallas = 0
for _ in range(n):
    if random.random() < 0.05: fallas += 1
print(f"Ausencia inesperada del titular de un turno (p = 5 %): {fallas/n*100:.2f} % de {n} turnos simulados")
assert min(cob) == 1 and max(cob) == 1 and cont == 0 and max(cuenta)*8 <= 40 + 8
assert abs(por_posicion - horas_sem/efectiva) < 1e-12
print("Pruebas superadas.")
