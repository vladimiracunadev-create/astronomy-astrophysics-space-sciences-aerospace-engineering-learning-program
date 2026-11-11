"""B121-C04 - Matriz de cobertura del marco espacial chileno (con nivel de evidencia).

Esto NO es asesoria legal ni un analisis juridico completo. Es un ejercicio de ordenar lo
CONSULTADO y rotular lo que NO se encontro o NO se consulto.
Consultado el 2026-11-11:
  [U1] UNOOSA, Status of International Agreements ... as at 1 January 2020 (PDF, PyMuPDF): Chile aparece
       con "R" en las 5 columnas de los tratados de la ONU (OST, ARRA, LIAB, REG, MOON). No se obtuvo
       la edicion 2024/2025 con la tabla (la CRP.9 de 2025 descargada no trae la tabla).
  [U2] UNOOSA, traduccion no oficial del Decreto Supremo 338 (2001-07-17; D.O. 2001-08-17): Comite Asesor
       Presidencial "Agencia Espacial de Chile"; asesora, coordina, propone politica y un proyecto de ley.
  [S1] Resultados de busqueda sobre Ley 18.168 (Subtel/ChileAtiende): concesion por decreto supremo
       para ciertos servicios de telecomunicaciones; texto de los articulos satelitales NO leido.
  [P1] Resultados de busqueda: existe una Politica Nacional Espacial reportada; decreto y fecha NO verificados.
Nivel de evidencia: 2 = texto o tabla leidos; 1 = solo resumen/indicio; 0 = sin evidencia hallada.
Solo biblioteca estandar.
"""
import sys
from datetime import date

# funcion regulatoria -> (instrumento chileno identificado, fuente, nivel de evidencia)
FUNCIONES = [
    ("Ser parte del Tratado del Espacio (OST)", "ratificacion (R) en tabla ONU", "U1", 2),
    ("Ser parte del Convenio de Responsabilidad", "ratificacion (R) en tabla ONU", "U1", 2),
    ("Ser parte del Convenio de Registro", "ratificacion (R) en tabla ONU", "U1", 2),
    ("Asesoria y coordinacion de politica espacial", "DS 338/2001 (comite asesor)", "U2", 2),
    ("Concesion de servicios de telecomunicaciones", "Ley 18.168 (por decreto supremo)", "S1", 1),
    ("Politica nacional espacial", "Politica Nacional Espacial (reportada)", "P1", 1),
    ("Autorizacion y supervision de operadores espaciales privados (OST art. VI)", "no se encontro un instrumento", "-", 0),
    ("Licencia de lanzamiento nacional", "no se encontro un instrumento", "-", 0),
    ("Licencia de teledeteccion", "no se encontro un instrumento", "-", 0),
    ("Requisitos de mitigacion de desechos", "no se encontro un instrumento", "-", 0),
]


def cobertura(filas):
    n = len(filas)
    return {nivel: sum(1 for f in filas if f[3] == nivel) / n for nivel in (0, 1, 2)}


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("EJERCICIO EDUCATIVO, no asesoria legal. Evidencia: 2 = leido, 1 = indicio, 0 = sin evidencia hallada (NO es prueba de ausencia).")
    print(f"{'#':>2s} {'funcion':74s}{'niv':>4s}  fuente")
    for i, (fn, ins, src, niv) in enumerate(FUNCIONES, 1):
        print(f"{i:2d} {fn[:73]:74s}{niv:4d}  {src:3s} {ins}")
    c = cobertura(FUNCIONES)
    # verificacion independiente: recuento por otro camino
    cuenta = {0: 0, 1: 0, 2: 0}
    for f in FUNCIONES:
        cuenta[f[3]] += 1
    assert all(abs(c[k] - cuenta[k] / len(FUNCIONES)) < 1e-12 for k in c)
    assert all((f[3] == 0) == (f[2] == "-") for f in FUNCIONES)  # sin fuente <=> sin evidencia
    print(f"Cobertura: nivel 2 = {c[2]:.0%}, nivel 1 = {c[1]:.0%}, nivel 0 = {c[0]:.0%} (de {len(FUNCIONES)} funciones)")
    d = date(2026, 11, 11) - date(2001, 8, 17)
    print(f"Dias desde la publicacion del DS 338/2001 (2001-08-17) hasta la consulta (2026-11-11): {d.days} d = {d.days/365.25:.1f} anos")
    print("Tratados de la ONU con R para Chile al 2020-01-01: 5 de 5 (OST, ARRA, LIAB, REG, MOON)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
