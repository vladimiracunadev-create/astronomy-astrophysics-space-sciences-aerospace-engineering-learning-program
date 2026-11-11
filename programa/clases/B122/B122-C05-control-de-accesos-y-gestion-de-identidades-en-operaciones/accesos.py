#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C05: auditoria de una matriz de roles y permisos de operaciones de mision SINTETICA.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad. Datos SINTETICOS (inventados).
Marco conceptual (solo pagina de publicacion consultada el 2026-11-11): NIST SP 800-53 Rev. 5 (familia de control de acceso: la pagina
no detalla los controles; los principios de privilegio minimo y segregacion de funciones se usan como conceptos generales).
Reglas del laboratorio: (1) privilegio minimo: un usuario no debe tener permisos que su rol no incluye; (2) segregacion: pares de permisos
incompatibles no pueden coexistir en un usuario; (3) dos personas: acciones criticas exigen aprobacion de otra persona distinta.
Unidades: conteos y probabilidades. Sistema de referencia: ninguno. Tolerancias: conteos exactos; Monte Carlo de la regla de dos personas
(200000, semilla 122) vs analitico < 0.002.
"""
from __future__ import annotations
import platform, random

ROLES = {
    "operador": {"ver_telemetria", "enviar_telecomando_rutina"},
    "ingeniero_sistemas": {"ver_telemetria", "editar_procedimientos"},
    "aprobador": {"ver_telemetria", "aprobar_telecomando_critico"},
    "admin_ti": {"gestionar_cuentas", "ver_registros"},
    "auditor": {"ver_registros", "ver_telemetria"},
}
INCOMPATIBLES = [("enviar_telecomando_rutina", "aprobar_telecomando_critico"), ("gestionar_cuentas", "ver_registros")]
USUARIOS = {  # usuario -> (roles asignados, permisos adicionales directos)
    "u1": (["operador"], set()),
    "u2": (["operador"], {"aprobar_telecomando_critico"}),
    "u3": (["ingeniero_sistemas"], {"gestionar_cuentas"}),
    "u4": (["admin_ti"], {"ver_registros"}),
    "u5": (["aprobador", "auditor"], set()),
    "u6": (["admin_ti", "auditor"], set()),
}


def permisos(u):
    roles, extra = USUARIOS[u]
    p = set(extra)
    for r in roles:
        p |= ROLES[r]
    return p


def excesos(u):
    roles, extra = USUARIOS[u]
    return sorted(extra)  # permisos directos fuera de roles (excepciones no gestionadas)


def conflictos(u):
    p = permisos(u)
    return [(a, b) for a, b in INCOMPATIBLES if a in p and b in p]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: usuarios, roles y permisos son inventados.")
    n_exc = n_conf = 0
    for u in USUARIOS:
        e, c = excesos(u), conflictos(u)
        n_exc += len(e)
        n_conf += len(c)
        print(f"  {u}: roles={USUARIOS[u][0]} | permisos directos fuera de rol={e} | conflictos={c}")
    print(f"Total de permisos directos fuera de rol = {n_exc} ; conflictos de segregacion = {n_conf}")
    assert n_exc == 3 and n_conf == 3
    usuarios_con_hallazgo = [u for u in USUARIOS if excesos(u) or conflictos(u)]
    print(f"Usuarios con algun hallazgo: {usuarios_con_hallazgo} ({len(usuarios_con_hallazgo)} de {len(USUARIOS)})")
    # superficie: permisos medios por usuario con y sin la correccion de quitar permisos directos
    medio = sum(len(permisos(u)) for u in USUARIOS) / len(USUARIOS)
    corregido = sum(len(set().union(*[ROLES[r] for r in USUARIOS[u][0]])) for u in USUARIOS) / len(USUARIOS)
    print(f"Permisos medios por usuario: actual = {medio:.2f} ; sin permisos directos = {corregido:.2f}")
    # regla de dos personas: aprobadores validos = usuarios con aprobar_telecomando_critico
    aprob = [u for u in USUARIOS if "aprobar_telecomando_critico" in permisos(u)]
    emisores = [u for u in USUARIOS if "enviar_telecomando_rutina" in permisos(u)]
    pares = [(a, b) for a in emisores for b in aprob if a != b]
    print(f"Emisores={emisores} aprobadores={aprob} ; pares emisor-aprobador distintos = {len(pares)}")
    # probabilidad de que el aprobador coincida con el emisor si se eligiera al azar entre los aprobadores
    rng = random.Random(122)
    n = 200000
    coinc = sum(1 for _ in range(n) if rng.choice(emisores) == rng.choice(aprob))
    esperado = len(set(emisores) & set(aprob)) / (len(emisores) * len(aprob))
    print(f"P(emisor = aprobador al azar): analitica = {esperado:.4f} ; Monte Carlo = {coinc / n:.4f}")
    assert abs(esperado - coinc / n) < 0.002
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
