# Licencias y procedencia de datos

**Inventario revisado:** 5 de noviembre de 2026.

No existe una licencia única para cualquier dato presente o futuro. Esta política distingue la estructura editorial original, los hechos y localizadores externos, los datos científicos de terceros y los datos personales.

| Ruta o familia | Naturaleza | Régimen actual |
|---|---|---|
| `catalogo/clases.jsonl`, `catalogo/clases.json`, `catalogo/clases.csv` | catálogo editorial de 5.120 unidades | selección, redacción y estructura originales bajo `CC BY-NC-SA 4.0`; hechos y referencias externas excluidos |
| `metadatos/programa.json` | identidad, versión, estado y cifras canónicas | estructura y redacción originales bajo `CC BY-NC-SA 4.0` |
| `metadatos/areas.json`, `bloques.json`, `rutas.json`, `modulos.json` | taxonomía y relaciones curriculares | selección y estructura originales bajo `CC BY-NC-SA 4.0` |
| `metadatos/fuentes.json` | 25 referencias institucionales preliminares | selección y estructura bajo `CC BY-NC-SA 4.0`; títulos, URLs y obras externas conservan su régimen |
| `metadatos/trazabilidad_fuentes_preliminares.json` | 832 relaciones editoriales preliminares | estructura original bajo `CC BY-NC-SA 4.0`; no prueba lectura íntegra ni licencia de las fuentes |
| `MANIFIESTO_SHA256.txt` | huellas técnicas derivadas | puede redistribuirse con el repositorio; no concede derechos sobre los archivos identificados |
| datos embebidos en `visor/index.html` | copia generada del catálogo | mismo régimen del catálogo; el código separable del visor es Apache-2.0 |

## Datos externos futuros

Antes de incorporar un dataset se deberá registrar:

1. titular y fuente oficial;
2. versión, fecha y localizador;
3. licencia o permiso verificable;
4. campos incorporados y transformaciones;
5. redistribución, derivación y uso comercial permitidos;
6. jurisdicción, privacidad, consentimiento y retención;
7. checksum y método de actualización cuando corresponda.

Si la licencia es desconocida, el dataset no se incorpora: se conserva sólo el enlace y la referencia necesaria. Publicar, convertir o minificar un archivo no cambia la licencia de sus componentes.

## Datos científicos

Cada dato se marcará como **observado**, **estimado**, **sintético** o **simulado**. Efemérides, catálogos, imágenes, kernels SPICE y productos de misión conservarán las condiciones del proveedor. Un recurso público en internet no se presume de dominio público.

## Datos personales

No se publicarán credenciales, telemetría personal, correos privados, direcciones, identificadores gubernamentales, datos médicos, biometría ni evaluaciones identificables. Los futuros pilotos deberán minimizar, anonimizar y gobernar sus datos antes de cualquier publicación.
