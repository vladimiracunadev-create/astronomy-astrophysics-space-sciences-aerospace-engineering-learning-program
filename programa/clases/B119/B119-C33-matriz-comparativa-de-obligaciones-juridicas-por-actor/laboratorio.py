#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C33: matriz actor x obligacion con las obligaciones CONSULTADAS en el bloque; deteccion de vacios.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Obligaciones tomadas SOLO de lo consultado el 2026-11-11 (parafraseado): nota de legal.un.org sobre el Tratado del Espacio Ultraterrestre (arts. II, IV, VI, VIII, IX, XI); pagina de UNOOSA del Convenio de Registro
(arts. II, III, IV); pagina de UNOOSA del Acuerdo sobre la Luna (arts. 3, 11, 12); resumen de busqueda del Convenio de Responsabilidad (arts. II, III); pagina de la UIT-R (notificacion y coordinacion).
NO consultados: Acuerdo de Salvamento, art. VII del tratado, el Reglamento de Radiocomunicaciones y cualquier ley nacional; sus obligaciones NO se incluyen y se listan como "no consultadas".
Marca 1 = el texto consultado impone la obligacion directamente al actor; 0 = no la impone directamente (puede recaer indirectamente mediante el Estado). La asignacion es una LECTURA DIDACTICA, no una opinion juridica.
Verificaciones: suma de filas == suma de columnas == total de unos; distancia de Hamming entre actores simetrica.
"""
import itertools, json, platform

OBLIG = [
    "no_apropiacion (II)", "no_ADM_en_orbita (IV)", "responder_por_actividades_y_autorizar (VI)", "jurisdiccion_y_registro_del_objeto (VIII)",
    "consultar_ante_interferencia (IX)", "informar_actividades (XI)", "registrar_y_notificar_a_la_ONU (Reg. II-IV)", "responder_por_danos (Resp. II-III)",
    "notificar_frecuencias (UIT)", "informar_recursos_hallados_en_la_Luna (Luna 11)",
]
ACTORES = ["Estado_de_lanzamiento", "Estado_de_registro", "Operador_privado", "Organizacion_internacional", "Secretario_General_ONU", "Administracion_de_telecomunicaciones"]
M = {
    "Estado_de_lanzamiento":                [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    "Estado_de_registro":                   [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    "Operador_privado":                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Organizacion_internacional":           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Secretario_General_ONU":               [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    "Administracion_de_telecomunicaciones": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
}
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Matriz DIDACTICA con obligaciones consultadas (2026-11-11); Acuerdo de Salvamento, art. VII, Reglamento de Radiocomunicaciones y leyes nacionales NO consultados.")
filas = {a: sum(M[a]) for a in ACTORES}
cols = [sum(M[a][j] for a in ACTORES) for j in range(len(OBLIG))]
total = sum(filas.values())
assert total == sum(cols)
print(" obligaciones por actor:", filas)
sin_destinatario = [OBLIG[j] for j, c in enumerate(cols) if c == 0]
sin_obligaciones = [a for a in ACTORES if filas[a] == 0]
print(" obligaciones sin destinatario directo:", sin_destinatario or "ninguna")
print(" actores sin obligaciones directas:", sin_obligaciones)
solo_un_actor = [OBLIG[j] for j, c in enumerate(cols) if c == 1]
print(" obligaciones con un unico destinatario:", len(solo_un_actor), "->", solo_un_actor)
def ham(a, b): return sum(x != y for x, y in zip(M[a], M[b]))
for a, b in itertools.combinations(ACTORES, 2):
    assert ham(a, b) == ham(b, a)
par = min(itertools.combinations(ACTORES, 2), key=lambda p: ham(*p))
print(f" Actores mas parecidos por distancia de Hamming: {par[0]} y {par[1]} (d = {ham(*par)})")
print(f" Cobertura: {total} unos de {len(ACTORES) * len(OBLIG)} celdas = {total / (len(ACTORES) * len(OBLIG)):.3f}")
assert not sin_destinatario
assert sin_obligaciones == ["Operador_privado"]
print("CLAVES " + json.dumps({"total": total, "celdas": len(ACTORES) * len(OBLIG), "cob": "%.3f" % (total / (len(ACTORES) * len(OBLIG))), "nl": filas["Estado_de_lanzamiento"], "nr": filas["Estado_de_registro"], "nu": len(solo_un_actor), "par": par[0] + " y " + par[1], "dh": ham(*par)}))
print("Pruebas superadas.")
