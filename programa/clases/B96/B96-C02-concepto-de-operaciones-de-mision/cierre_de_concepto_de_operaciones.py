"""B96-C02: cierre de un concepto de operaciones para un satelite LEO SINTETICO (contactos y datos por dia)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: satelite, estacion y tasas ficticias")
mu = 398600.4418; RE = 6378.137; h = 550.0; el_min = 10.0
a = RE + h
P = 2*math.pi*math.sqrt(a**3/mu)           # periodo, s
lam = math.acos(RE/a*math.cos(math.radians(el_min))) - math.radians(el_min)  # semiangulo central, rad
dur_max = P*lam/math.pi                    # pasada cenital, s
print(f"Periodo = {P/60:.2f} min ; semiangulo central = {math.degrees(lam):.2f} grados ; duracion maxima de pasada = {dur_max/60:.2f} min")
rev_dia = 86400/P
print(f"Revoluciones por dia = {rev_dia:.2f}")
# pasadas utiles por dia (estimacion): fraccion de cobertura de una estacion a latitud media
pas_dia = 5.0                                # pasadas utiles/dia (sintetico, de la tabla de C04)
dur_media = 0.6*dur_max                       # duracion media de las pasadas (factor sintetico 0.6)
print(f"Pasadas utiles = {pas_dia:.0f}/dia ; duracion media = {dur_media/60:.2f} min ; contacto total = {pas_dia*dur_media/60:.1f} min/dia")
# datos
gen = 2.0e3*86400/8/1e9                      # 2 kbit/s continuos -> GB/dia
carga = 0.8                                  # GB/dia de carga util (sintetica)
gen_total = gen + carga
tasa_dl = 2.0e6                              # bit/s de bajada
eficiencia = 0.85                            # sobrecarga de protocolo (sintetica)
cap = pas_dia*dur_media*tasa_dl*eficiencia/8/1e9
print(f"Generado = {gen_total:.3f} GB/dia (plataforma {gen:.3f} + carga {carga:.1f}) ; capacidad de bajada = {cap:.3f} GB/dia")
margen = cap/gen_total - 1
print(f"Margen de datos = {margen*100:.1f} % ; cierra: {'SI' if margen >= 0.2 else 'NO'} (criterio sintetico >= 20 %)")
# horas de operador
min_op = pas_dia*(dur_media/60 + 10)           # 10 min de preparacion y cierre por pasada
print(f"Carga de trabajo = {min_op:.1f} min/dia de operador")
# comprobacion: despejar la carga util maxima que cierra con margen 20 %
carga_max = cap/1.2 - gen
print(f"Carga util maxima con margen 20 % = {carga_max:.3f} GB/dia")
assert abs((gen + carga_max)*1.2 - cap) < 1e-9
assert abs(P - 2*math.pi*math.sqrt(a**3/mu)) < 1e-9 and 90 < P/60 < 100
print("Pruebas superadas.")
