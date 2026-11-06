#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C31: una API HTTP mínima de datos, con paginación, validación y caché condicional.

Datos: SINTÉTICOS. 250 «escenas» ficticias {id, fecha, nubosidad_pct} generadas
de forma determinista (id = escena-000..249, fecha = 2026-01-01 + i//10 días,
nubosidad = (i*7) % 100). El servidor escucha solo en 127.0.0.1, en un puerto
efímero, durante la ejecución.
Modelo (diseño propio, inspirado en prácticas habituales de APIs REST, sin
seguir ninguna especificación): GET /v1/escenas?limite=&desplazamiento=&nubosidad_max=
devuelve JSON con total, limite, desplazamiento y elementos; GET /v1/escenas/{id}
devuelve un elemento o 404; parámetros inválidos dan 400 con mensaje JSON;
cada respuesta de un elemento lleva ETag (SHA-256 del cuerpo) y acepta
If-None-Match, devolviendo 304 sin cuerpo si coincide. Se genera además un
documento descriptivo (JSON, estilo OpenAPI SIMPLIFICADO, sin validar contra
la especificación) y se comprueba que cada respuesta cumple el esquema descrito.
Supuestos: un solo cliente; sin autenticación, límites de uso ni HTTPS.
Validez: demostración del contrato petición-respuesta; no es un servicio de producción.
Tolerancia: la paginación recorre las 250 escenas sin duplicados ni omisiones;
los códigos de estado coinciden con los esperados.
"""
from __future__ import annotations
import hashlib, json, platform, sys, threading
import urllib.error, urllib.parse, urllib.request
import datetime as dt
from http.server import BaseHTTPRequestHandler, HTTPServer

ESCENAS = [{"id": f"escena-{i:03d}", "fecha": (dt.date(2026, 1, 1) + dt.timedelta(days=i // 10)).isoformat(),
            "nubosidad_pct": (i * 7) % 100} for i in range(250)]
LIMITE_MAX = 100

DOCUMENTO = {
    "version_api": "v1",
    "rutas": {
        "/v1/escenas": {"parametros": {"limite": "entero 1..100 (por defecto 20)", "desplazamiento": "entero >= 0",
                                         "nubosidad_max": "entero 0..100"},
                        "respuestas": {"200": "lista paginada", "400": "parámetro inválido"}},
        "/v1/escenas/{id}": {"respuestas": {"200": "una escena", "304": "sin cambios", "404": "no existe"}},
    },
    "esquema_escena": {"id": "string", "fecha": "string (YYYY-MM-DD)", "nubosidad_pct": "integer 0..100"},
}


def cumple_esquema(e):
    return (isinstance(e.get("id"), str) and isinstance(e.get("fecha"), str) and len(e["fecha"]) == 10
            and isinstance(e.get("nubosidad_pct"), int) and 0 <= e["nubosidad_pct"] <= 100)


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _enviar(self, codigo, obj=None, etag=None):
        cuerpo = b"" if obj is None else json.dumps(obj, sort_keys=True).encode()
        self.send_response(codigo)
        if obj is not None:
            self.send_header("Content-Type", "application/json")
        if etag:
            self.send_header("ETag", etag)
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        if u.path == "/v1/escenas":
            try:
                limite = int(q.get("limite", 20))
                desp = int(q.get("desplazamiento", 0))
                nmax = int(q["nubosidad_max"]) if "nubosidad_max" in q else None
            except ValueError:
                return self._enviar(400, {"error": "parámetro no numérico"})
            if not (1 <= limite <= LIMITE_MAX) or desp < 0 or (nmax is not None and not 0 <= nmax <= 100):
                return self._enviar(400, {"error": "parámetro fuera de rango", "limite_max": LIMITE_MAX})
            lista = [e for e in ESCENAS if nmax is None or e["nubosidad_pct"] <= nmax]
            return self._enviar(200, {"total": len(lista), "limite": limite, "desplazamiento": desp, "elementos": lista[desp:desp + limite]})
        if u.path.startswith("/v1/escenas/"):
            ident = u.path.rsplit("/", 1)[1]
            e = next((x for x in ESCENAS if x["id"] == ident), None)
            if e is None:
                return self._enviar(404, {"error": "escena no encontrada", "id": ident})
            etag = '"' + hashlib.sha256(json.dumps(e, sort_keys=True).encode()).hexdigest()[:16] + '"'
            if self.headers.get("If-None-Match") == etag:
                return self._enviar(304, None, etag)
            return self._enviar(200, e, etag)
        if u.path == "/v1/documento":
            return self._enviar(200, DOCUMENTO)
        return self._enviar(404, {"error": "ruta desconocida"})


def pedir(base, ruta, cabeceras=None):
    req = urllib.request.Request(base + ruta, headers=cabeceras or {})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  (API local de demostración)")
    srv = HTTPServer(("127.0.0.1", 0), Manejador)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    try:
        c, h, b = pedir(base, "/v1/escenas?limite=5")
        d = json.loads(b)
        print(f"primera página: {c}; total = {d['total']}; devueltos = {len(d['elementos'])}")
        prueba(c == 200 and d["total"] == 250 and len(d["elementos"]) == 5, "primera página")

        ids, desp, paginas = [], 0, 0
        while True:
            c, h, b = pedir(base, f"/v1/escenas?limite=100&desplazamiento={desp}")
            d = json.loads(b)
            if not d["elementos"]:
                break
            ids += [e["id"] for e in d["elementos"]]
            desp += 100
            paginas += 1
        print(f"recorrido paginado: {paginas} páginas, {len(ids)} escenas, {len(set(ids))} distintas")
        prueba(len(ids) == 250 and len(set(ids)) == 250 and ids == [e["id"] for e in ESCENAS], "paginación completa y sin duplicados")

        c, h, b = pedir(base, "/v1/escenas?nubosidad_max=20&limite=100")
        d = json.loads(b)
        esperado = sum(1 for e in ESCENAS if e["nubosidad_pct"] <= 20)
        print(f"filtro nubosidad_max=20: total = {d['total']} (conteo independiente {esperado})")
        prueba(d["total"] == esperado, "filtro")

        # esquema de cada elemento
        c, h, b = pedir(base, "/v1/escenas?limite=100")
        prueba(all(cumple_esquema(e) for e in json.loads(b)["elementos"]), "todos cumplen el esquema")
        print("100 elementos de una página cumplen el esquema descrito")

        # elemento, ETag y 304
        c, h, b = pedir(base, "/v1/escenas/escena-042")
        etag = h["ETag"]
        print(f"elemento escena-042: {c}; ETag = {etag}")
        prueba(c == 200 and json.loads(b)["id"] == "escena-042", "elemento")
        c2, h2, b2 = pedir(base, "/v1/escenas/escena-042", {"If-None-Match": etag})
        print(f"con If-None-Match igual: {c2}; cuerpo de {len(b2)} bytes")
        prueba(c2 == 304 and b2 == b"", "304 sin cuerpo")
        c3, _, b3 = pedir(base, "/v1/escenas/escena-042", {"If-None-Match": '"otro"'})
        prueba(c3 == 200 and len(b3) > 0, "ETag distinto: 200")
        print("con If-None-Match distinto: 200 con cuerpo")

        # errores
        for nombre, ruta, esp in [("limite 0", "/v1/escenas?limite=0", 400), ("limite 1000", "/v1/escenas?limite=1000", 400),
                                  ("desplazamiento negativo", "/v1/escenas?desplazamiento=-1", 400),
                                  ("no numérico", "/v1/escenas?limite=abc", 400), ("nubosidad 150", "/v1/escenas?nubosidad_max=150", 400),
                                  ("id inexistente", "/v1/escenas/escena-999", 404), ("ruta desconocida", "/v2/escenas", 404)]:
            c, h, b = pedir(base, ruta)
            print(f"error «{nombre}»: {c} {json.loads(b)['error']}")
            prueba(c == esp, f"código de «{nombre}»")

        c, h, b = pedir(base, "/v1/documento")
        doc = json.loads(b)
        rutas = sorted(doc["rutas"])
        print(f"documento descriptivo: {c}; rutas = {rutas}")
        prueba(c == 200 and rutas == ["/v1/escenas", "/v1/escenas/{id}"], "documento")
    finally:
        srv.shutdown()
        srv.server_close()
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
