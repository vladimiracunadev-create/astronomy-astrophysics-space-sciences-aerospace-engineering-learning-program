#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C29: un servicio de mapas local INSPIRADO en el estilo WMS, y su cliente.

AVISO: el servicio NO es un WMS conforme: usa nombres de parámetros propios,
devuelve JSON para las «capacidades» y un mapa en formato PGM (imagen gris
portátil), no PNG ni JPEG, y no sigue la especificación WMS 1.3.0 (que no se
leyó). Ilustra la IDEA que resume el OGC para WMS: una interfaz HTTP simple para
pedir imágenes de mapas georreferenciadas. Solo escucha en 127.0.0.1, en un
puerto efímero, durante la ejecución.
Datos: SINTÉTICOS. La «capa» es la función f(lon, lat) = 128 + 100*sin(lon/10 deg)
*cos(lat/10 deg) redondeada a entero 8 bits, en el dominio lon [0, 40), lat [0, 40).
Modelo: GetMap-like: parámetros capa, minlon, minlat, maxlon, maxlat, ancho, alto;
cada píxel (fila, col) toma el valor de f en el centro del píxel, con la fila 0 en
el norte (maxlat) y la columna 0 en el oeste (minlon).
Supuestos: coordenadas planas lon/lat; sin proyecciones ni sistemas de referencia.
Validez: demostración del patrón petición-respuesta; no es interoperable con clientes WMS.
Tolerancia: los píxeles devueltos deben ser IDÉNTICOS al cálculo directo; los errores
de petición deben dar el código 400 con mensaje JSON.
"""
from __future__ import annotations
import json, math, platform, sys, threading
import urllib.error, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy as np

DOMINIO = (0.0, 0.0, 40.0, 40.0)    # minlon, minlat, maxlon, maxlat
MAX_PIX = 512


def valor(lon, lat):
    return np.clip(np.rint(128 + 100 * np.sin(np.radians(lon) * 5.7295779513) * np.cos(np.radians(lat) * 5.7295779513)), 0, 255).astype(np.uint8)


def mapa(minlon, minlat, maxlon, maxlat, ancho, alto):
    dx, dy = (maxlon - minlon) / ancho, (maxlat - minlat) / alto
    lon = minlon + (np.arange(ancho) + 0.5) * dx
    lat = maxlat - (np.arange(alto) + 0.5) * dy
    LON, LAT = np.meshgrid(lon, lat)
    return valor(LON, LAT)


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, codigo, obj):
        cuerpo = json.dumps(obj).encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        pet = q.get("peticion")
        if pet == "capacidades":
            return self._json(200, {"servicio": "mapas-demo", "capas": [{"nombre": "demo", "dominio": list(DOMINIO), "max_pixeles": MAX_PIX}],
                                    "formatos": ["image/x-portable-graymap"]})
        if pet == "mapa":
            req = ["capa", "minlon", "minlat", "maxlon", "maxlat", "ancho", "alto"]
            falta = [k for k in req if k not in q]
            if falta:
                return self._json(400, {"error": "faltan parámetros", "faltan": falta})
            try:
                minlon, minlat, maxlon, maxlat = (float(q[k]) for k in req[1:5])
                ancho, alto = int(q["ancho"]), int(q["alto"])
            except ValueError:
                return self._json(400, {"error": "parámetro no numérico"})
            if q["capa"] != "demo":
                return self._json(404, {"error": "capa desconocida", "capa": q["capa"]})
            if not (minlon < maxlon and minlat < maxlat):
                return self._json(400, {"error": "caja inválida (mín debe ser menor que máx)"})
            if not (1 <= ancho <= MAX_PIX and 1 <= alto <= MAX_PIX):
                return self._json(400, {"error": f"tamaño fuera de 1..{MAX_PIX}"})
            if minlon < DOMINIO[0] or minlat < DOMINIO[1] or maxlon > DOMINIO[2] or maxlat > DOMINIO[3]:
                return self._json(400, {"error": "caja fuera del dominio de la capa", "dominio": list(DOMINIO)})
            img = mapa(minlon, minlat, maxlon, maxlat, ancho, alto)
            cuerpo = f"P5\n{ancho} {alto}\n255\n".encode() + img.tobytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/x-portable-graymap")
            self.send_header("Content-Length", str(len(cuerpo)))
            self.end_headers()
            self.wfile.write(cuerpo)
            return
        return self._json(400, {"error": "petición desconocida", "peticiones": ["capacidades", "mapa"]})


def pedir(base, **params):
    url = base + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.status, r.headers.get("Content-Type"), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type"), e.read()


def leer_pgm(b):
    partes = b.split(b"\n", 3)
    assert partes[0] == b"P5"
    ancho, alto = map(int, partes[1].split())
    return np.frombuffer(partes[3], dtype=np.uint8).reshape(alto, ancho)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  (servicio local inspirado en WMS; NO conforme)")
    srv = HTTPServer(("127.0.0.1", 0), Manejador)
    hilo = threading.Thread(target=srv.serve_forever, daemon=True)
    hilo.start()
    base = f"http://127.0.0.1:{srv.server_address[1]}/"
    try:
        c, t, b = pedir(base, peticion="capacidades")
        cap = json.loads(b)
        print(f"capacidades: {c} {t}; capas = {[x['nombre'] for x in cap['capas']]}; formatos = {cap['formatos']}")
        prueba(c == 200 and cap["capas"][0]["nombre"] == "demo", "capacidades")

        c, t, b = pedir(base, peticion="mapa", capa="demo", minlon=0, minlat=0, maxlon=40, maxlat=40, ancho=64, alto=64)
        img = leer_pgm(b)
        print(f"mapa 64x64: {c} {t}; forma {img.shape}; min {img.min()}, max {img.max()}")
        prueba(c == 200 and img.shape == (64, 64), "forma del mapa")
        directo = mapa(0, 0, 40, 40, 64, 64)
        prueba(np.array_equal(img, directo), "píxeles idénticos al cálculo directo")
        print("píxeles idénticos al cálculo directo")

        # orientación: fila 0 al norte; columna 0 al oeste
        c, t, b = pedir(base, peticion="mapa", capa="demo", minlon=10, minlat=10, maxlon=30, maxlat=30, ancho=2, alto=2)
        p = leer_pgm(b)
        esp = np.array([[valor(15.0, 25.0), valor(25.0, 25.0)], [valor(15.0, 15.0), valor(25.0, 15.0)]])
        print(f"mapa 2x2 sobre [10,30]x[10,30]: {p.tolist()} (esperado {esp.tolist()}: fila 0 = norte, columna 0 = oeste)")
        prueba(np.array_equal(p, esp), "orientación")

        # errores
        casos = [
            ("faltan parámetros", dict(peticion="mapa", capa="demo"), 400),
            ("capa desconocida", dict(peticion="mapa", capa="otra", minlon=0, minlat=0, maxlon=1, maxlat=1, ancho=2, alto=2), 404),
            ("caja invertida", dict(peticion="mapa", capa="demo", minlon=5, minlat=0, maxlon=1, maxlat=1, ancho=2, alto=2), 400),
            ("fuera del dominio", dict(peticion="mapa", capa="demo", minlon=-5, minlat=0, maxlon=1, maxlat=1, ancho=2, alto=2), 400),
            ("tamaño excesivo", dict(peticion="mapa", capa="demo", minlon=0, minlat=0, maxlon=1, maxlat=1, ancho=10000, alto=2), 400),
            ("no numérico", dict(peticion="mapa", capa="demo", minlon="a", minlat=0, maxlon=1, maxlat=1, ancho=2, alto=2), 400),
            ("petición desconocida", dict(peticion="otra"), 400),
        ]
        for nombre, params, esperado in casos:
            c, t, b = pedir(base, **params)
            msg = json.loads(b)["error"]
            print(f"error «{nombre}»: {c} ({msg})")
            prueba(c == esperado and t == "application/json", f"error {nombre}")
    finally:
        srv.shutdown()
        srv.server_close()
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
