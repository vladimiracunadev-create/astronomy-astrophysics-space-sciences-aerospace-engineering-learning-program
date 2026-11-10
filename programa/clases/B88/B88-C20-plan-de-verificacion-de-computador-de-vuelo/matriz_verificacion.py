"""B88-C20: matriz de verificacion, cobertura y huerfanos (SINTETICO)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: 16 requisitos y 12 casos de verificacion inventados")

# (id, texto breve, metodo previsto) metodos: T=prueba A=analisis I=inspeccion D=demostracion
REQ = {
 "R01": ("Frecuencia del lazo de control 20 Hz", "T"), "R02": ("Tiempo de respuesta de tarea AOCS <= 12 ms", "T"),
 "R03": ("Utilizacion de CPU <= 70 %", "A"), "R04": ("Margen de RAM >= 30 %", "A"),
 "R05": ("Correccion de un bit en memoria", "T"), "R06": ("Deteccion de doble error en memoria", "T"),
 "R07": ("Watchdog reinicia en <= 140 ms", "T"), "R08": ("Rechazo de telecomando con CRC malo", "T"),
 "R09": ("Rechazo de repeticion de telecomando", "T"), "R10": ("Reversion tras 3 arranques fallidos", "D"),
 "R11": ("Sin recursion en el codigo", "I"), "R12": ("Sin memoria dinamica tras inicializar", "I"),
 "R13": ("Registro de eventos con limite de tasa", "T"), "R14": ("Telemetria HK a 1 Hz", "T"),
 "R15": ("Modo seguro alcanzable desde cualquier modo", "D"), "R16": ("Documento de interfaz aprobado", "I"),
}
# casos: id -> (metodo, requisitos que verifica)
CASOS = {
 "V01": ("T", ["R01", "R14"]), "V02": ("T", ["R02"]), "V03": ("A", ["R03", "R04"]), "V04": ("T", ["R05", "R06"]),
 "V05": ("T", ["R07"]), "V06": ("T", ["R08", "R09"]), "V07": ("D", ["R10"]), "V08": ("I", ["R11"]),
 "V09": ("T", ["R13"]), "V10": ("D", ["R15"]), "V11": ("T", ["R99"]), "V12": ("T", []),
}
cubiertos = {r: [c for c, (m, rs) in CASOS.items() if r in rs] for r in REQ}
sin_ver = sorted(r for r, cs in cubiertos.items() if not cs)
huerfanos = sorted(c for c, (m, rs) in CASOS.items() if not rs or any(r not in REQ for r in rs))
incoherentes = sorted((r, REQ[r][1], CASOS[c][0]) for r, cs in cubiertos.items() for c in cs if CASOS[c][0] != REQ[r][1])
n = len(REQ)
print(f"Requisitos = {n} ; con al menos un caso = {n-len(sin_ver)} ; cobertura = {100*(n-len(sin_ver))/n:.1f} %")
print(f"Requisitos sin verificacion: {sin_ver}")
print(f"Casos huerfanos (sin requisito valido): {huerfanos}")
print(f"Metodo previsto distinto del usado: {incoherentes}")
print("Matriz (requisito -> casos):")
for r in REQ:
    print(f"  {r} [{REQ[r][1]}] {REQ[r][0][:40]:40s} -> {cubiertos[r] if cubiertos[r] else 'SIN CASO'}")
por_metodo = {}
for r, (_, m) in REQ.items(): por_metodo[m] = por_metodo.get(m, 0) + 1
print("Requisitos por metodo previsto:", dict(sorted(por_metodo.items())))
assert sin_ver == ["R12", "R16"] and huerfanos == ["V11", "V12"]
print("Pruebas superadas.")
