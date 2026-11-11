#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C05: privacidad de un conjunto SINTETICO de participantes y consentimiento retirable.

Todo SINTETICO: 300 participantes inventados con banda de edad, comuna ficticia (Comuna A a H), tipo de equipo y coordenadas de su sitio de
observacion dentro de una region ficticia de 0.40 x 0.40 grados alrededor de (lat -33.50, lon -70.60) -- punto arbitrario, SIN relacion con
ninguna vivienda real. Nombre de usuario y correo ficticios.
Metodos (estandar, no consultados en una fuente concreta): minimizacion (no recoger lo innecesario), generalizacion (redondear coordenadas),
k-anonimato = tamano minimo de las clases de equivalencia de los cuasi-identificadores (banda de edad, comuna, equipo, celda de coordenadas).
Longitud de un grado de latitud = pi/180 * 6371.0 km = 111.195 km (esfera de radio medio 6371.0 km); un grado de longitud = eso * cos(lat).
Segunda via: k por agrupacion en diccionario y k por ordenacion; deben coincidir. Consentimiento: lista de eventos (concedido/retirado) con estado
por defecto "sin consentimiento"; tras una retirada no debe quedar ningun registro del participante en el conjunto derivado.
Semilla 129. Unidades: grados, km, personas.
"""
from __future__ import annotations
import math, platform, random
from collections import Counter

LAT0, LON0, ANCHO = -33.50, -70.60, 0.40
KM_GRADO = math.pi / 180 * 6371.0


def generar(rng, n=300):
    pers = []
    for i in range(n):
        pers.append({
            "id": f"P{i+1:03d}",
            "usuario": f"usuario{i+1:03d}",
            "edad": rng.choice(["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]),
            "comuna": "Comuna " + rng.choice("ABCDEFGH"),
            "equipo": rng.choice(["ojo", "prismaticos", "telescopio", "camara"]),
            "lat": round(LAT0 + rng.uniform(-ANCHO / 2, ANCHO / 2), 5),
            "lon": round(LON0 + rng.uniform(-ANCHO / 2, ANCHO / 2), 5),
        })
    return pers


def clave(p, dec, con_edad=True):
    c = (p["comuna"], p["equipo"], round(p["lat"], dec), round(p["lon"], dec)) if dec is not None else (p["comuna"], p["equipo"])
    return ((p["edad"],) + c) if con_edad else c


def k_dic(pers, dec, con_edad=True):
    cnt = {}
    for p in pers:
        cnt[clave(p, dec, con_edad)] = cnt.get(clave(p, dec, con_edad), 0) + 1
    return min(cnt.values()), sum(1 for v in cnt.values() if v == 1), len(cnt)


def k_orden(pers, dec, con_edad=True):
    ks = sorted(clave(p, dec, con_edad) for p in pers)
    grupos = []
    for k in ks:
        if grupos and grupos[-1][0] == k:
            grupos[-1][1] += 1
        else:
            grupos.append([k, 1])
    return min(g[1] for g in grupos)


def error_posicion(pers, dec):
    e = []
    for p in pers:
        dlat = (p["lat"] - round(p["lat"], dec)) * KM_GRADO
        dlon = (p["lon"] - round(p["lon"], dec)) * KM_GRADO * math.cos(math.radians(p["lat"]))
        e.append(math.hypot(dlat, dlon))
    return sum(e) / len(e)


class Registro:
    def __init__(self):
        self.eventos = []

    def conceder(self, pid):
        self.eventos.append((pid, "concedido"))

    def retirar(self, pid):
        self.eventos.append((pid, "retirado"))

    def estado(self, pid):
        s = "sin consentimiento"
        for p, e in self.eventos:
            if p == pid:
                s = e
        return s


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    pers = generar(rng)
    print(f"DATOS SINTETICOS: {len(pers)} participantes inventados; region ficticia de {ANCHO} x {ANCHO} grados; 1 grado de latitud = {KM_GRADO:.3f} km")
    print("1) Efecto de redondear las coordenadas (cuasi-identificadores: edad, comuna, equipo, celda)")
    print("   decimales  celda aprox  k    unicos  clases  error medio de posicion [km]")
    for dec in (5, 4, 3, 2, 1, 0):
        k, unicos, clases = k_dic(pers, dec)
        assert k == k_orden(pers, dec), "las dos vias de k no coinciden"
        celda = 10 ** (-dec) * KM_GRADO
        print(f"   {dec:9d}  {celda:9.3f} km  {k:2d}  {unicos:6d}  {clases:6d}  {error_posicion(pers, dec):10.3f}")
    # sin coordenadas
    k0, u0, c0 = k_dic(pers, None)
    print(f"   sin coordenadas (solo edad, comuna, equipo): k = {k0}, unicos = {u0}, clases = {c0}")
    k0b, u0b, c0b = k_dic(pers, None, con_edad=False)
    print(f"   sin coordenadas ni edad (solo comuna, equipo): k = {k0b}, unicos = {u0b}, clases = {c0b}")
    assert k_dic(pers, 5)[1] == len(pers), "con 5 decimales cada participante debe ser unico"
    # 2) minimizacion: que atributos y que precision permiten k >= 5
    objetivo = 5
    print(f"2) Busqueda de la menor generalizacion con k >= {objetivo} (atributos sueltos; decimales de las coordenadas)")
    print("   atributos                 decimales   k   unicos")
    def k_attr(attrs, dec):
        cnt = Counter((tuple(p[a] for a in attrs) + ((round(p["lat"], dec), round(p["lon"], dec)) if dec is not None else ())) for p in pers)
        return min(cnt.values()), sum(1 for v in cnt.values() if v == 1)
    hallado = None
    for attrs in (("edad", "comuna", "equipo"), ("edad", "comuna"), ("comuna",), ()):
        for dec in (2, 1, 0, None):
            k, u = k_attr(attrs, dec)
            print(f"   {'+'.join(attrs) or '(ninguno)':24s}  {str(dec):9s} {k:3d}  {u:6d}")
            if k >= objetivo and hallado is None:
                hallado = (attrs, dec, k)
    print(f"   Primera combinacion que cumple k >= {objetivo}: {hallado}")
    assert hallado is not None
    # 3) consentimiento
    reg = Registro()
    for p in pers[:200]:
        reg.conceder(p["id"])
    for p in pers[:10]:
        reg.retirar(p["id"])
    en_analisis = [p for p in pers if reg.estado(p["id"]) == "concedido"]
    print(f"3) Consentimiento: concedido a 200, retirado por 10 -> en el analisis quedan {len(en_analisis)}; "
          f"sin respuesta ({sum(reg.estado(p['id']) == 'sin consentimiento' for p in pers)}) no se usan")
    assert len(en_analisis) == 190
    assert all(reg.estado(p["id"]) != "retirado" for p in en_analisis)
    ids_retirados = {p["id"] for p in pers[:10]}
    assert not any(p["id"] in ids_retirados for p in en_analisis)
    # 4) lo que se publica: recuentos por celda de 0.1 grado, suprimiendo celdas con menos de 5 personas
    celdas = Counter((round(p["lat"], 1), round(p["lon"], 1)) for p in en_analisis)
    supr = {c: n for c, n in celdas.items() if n < objetivo}
    publicables = {c: n for c, n in celdas.items() if n >= objetivo}
    print(f"4) Publicacion como recuentos por celda de 0.1 grado (sin usuario, edad ni equipo): {len(celdas)} celdas, "
          f"{len(publicables)} publicables (n >= {objetivo}), {len(supr)} suprimidas con {sum(supr.values())} personas")
    assert all(n >= objetivo for n in publicables.values())
    assert sum(celdas.values()) == len(en_analisis)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
