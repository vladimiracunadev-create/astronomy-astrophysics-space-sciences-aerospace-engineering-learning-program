#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C30: atribucion de un incidente espacial SINTETICO con razonamiento bayesiano y fiabilidad de las fuentes (desinformacion).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no atribuye ningun incidente real a nadie.
Texto consultado (2026-11-11): Convenio de Registro (UNOOSA), art. VI: ayuda para identificar objetos causantes de dano o peligrosos, con informacion sobre el momento, la naturaleza y las circunstancias del suceso;
art. XI del tratado de 1967: informacion publica. NO consultado: ningun metodo oficial de atribucion ni caso real.
Hipotesis SINTETICAS: H1 falla tecnica (a priori 0.50), H2 accion deliberada de un actor A (0.25), H3 accion deliberada de un actor B (0.25). Cuatro evidencias independientes con verosimilitudes inventadas.
Regla (no consultada en una fuente concreta; verificada por actualizacion secuencial vs conjunta y por log-odds): P(H|e) proporcional a P(e|H) P(H).
Fiabilidad de una fuente: con probabilidad r la fuente informa correctamente; con 1 - r el informe es ruido (50 % a favor de cualquier hipotesis); se mezcla la verosimilitud como r L + (1 - r) 0.5.
Tolerancia: posterior secuencial == conjunto (1e-12); suma = 1 (1e-12).
"""
import itertools, json, math, platform

H = ["falla_tecnica", "actor_A", "actor_B"]
PRIOR = [0.50, 0.25, 0.25]
E = {   # P(evidencia observada | H)
    "e1_trayectoria_compatible_con_A": [0.10, 0.60, 0.20],
    "e2_sin_anomalia_telemetrica_previa": [0.20, 0.60, 0.60],
    "e3_comunicado_confuso": [0.50, 0.40, 0.40],
    "e4_imagen_no_verificada": [0.30, 0.60, 0.30],
}
def post(prior, ls):
    p = [pi * math.prod(l[i] for l in ls) for i, pi in enumerate(prior)]
    z = sum(p)
    return [x / z for x in p]
def actualizar_sec(prior, ls):
    p = prior
    for l in ls:
        p = post(p, [l])
    return p
ls = list(E.values())
conj = post(PRIOR, ls); sec = actualizar_sec(PRIOR, ls)
assert all(abs(a - b) < 1e-12 for a, b in zip(conj, sec)) and abs(sum(conj) - 1) < 1e-12
# orden de la evidencia no importa
for perm in itertools.permutations(ls):
    q = actualizar_sec(PRIOR, list(perm))
    assert all(abs(a - b) < 1e-12 for a, b in zip(q, conj))
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Incidente SINTETICO; art. VI (Registro) y XI consultados 2026-11-11; ningun metodo oficial de atribucion consultado.")
print("Posterior con las cuatro evidencias (nombres de las hipotesis: " + ", ".join(H) + "):", [round(x, 4) for x in conj])
# razon de verosimilitud actor A vs falla tecnica
lr = math.prod(l[1] / l[0] for l in ls)
print(f"Razon de verosimilitud conjunta A : falla = {lr:.2f} ; log10 = {math.log10(lr):.3f}")
# fiabilidad de la imagen no verificada
print("Efecto de la fiabilidad r de la imagen no verificada (e4) sobre P(actor_A):")
res = {}
for r in (0.0, 0.3, 0.6, 1.0):
    e4 = [r * x + (1 - r) * 0.5 for x in E["e4_imagen_no_verificada"]]
    q = post(PRIOR, [E["e1_trayectoria_compatible_con_A"], E["e2_sin_anomalia_telemetrica_previa"], E["e3_comunicado_confuso"], e4])
    res[r] = q
    print(f"   r = {r:.1f}: posterior {[round(x, 4) for x in q]}")
# sensibilidad al a priori
for p0 in (0.2, 0.5, 0.8):
    pr = [p0, (1 - p0) / 2, (1 - p0) / 2]
    q = post(pr, ls)
    print(f"   a priori de falla tecnica {p0:.1f}: posterior de A = {q[1]:.4f}")
# nivel de confianza ilustrativo
umbral = 0.95
print(f"Alguna hipotesis supera {umbral}? {'si' if max(conj) >= umbral else 'no'} (umbral ILUSTRATIVO)")
print("CLAVES " + json.dumps({"pf": "%.4f" % conj[0], "pa": "%.4f" % conj[1], "pb": "%.4f" % conj[2], "lr": "%.2f" % lr, "r0": "%.4f" % res[0.0][1], "r1": "%.4f" % res[1.0][1], "m": "%.4f" % max(conj)}))
print("Pruebas superadas.")
