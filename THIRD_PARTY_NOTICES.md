# Avisos de terceros

**Inventario revisado:** 5 de noviembre de 2026. Este documento no sustituye los textos de licencia ni los términos publicados por cada titular.

## Herramientas y automatización

| Componente | Uso | Licencia declarada por el proyecto de origen |
|---|---|---|
| Python | ejecución del validador y generador de manifiesto | [Python Software Foundation License](https://docs.python.org/3/license.html) |
| `actions/checkout` | descarga del repositorio en CI | [MIT](https://github.com/actions/checkout/blob/main/LICENSE) |
| `actions/setup-python` | preparación de Python en CI | [MIT](https://github.com/actions/setup-python/blob/main/LICENSE) |
| `actions/configure-pages` | configuración de GitHub Pages | [MIT](https://github.com/actions/configure-pages/blob/main/LICENSE) |
| `actions/upload-pages-artifact` | empaquetado del visor | [MIT](https://github.com/actions/upload-pages-artifact/blob/main/LICENSE) |
| `actions/deploy-pages` | despliegue del visor | [MIT](https://github.com/actions/deploy-pages/blob/main/LICENSE) |

Las acciones se invocan por versión y no se copian en el repositorio. Cada dependencia conserva su licencia y avisos.

## Fuentes científicas e institucionales

`metadatos/fuentes.json` registra 25 portales o documentos preliminares y `fuentes/REFERENCIAS_INSTITUCIONALES_PRELIMINARES.md` explica su carácter orientativo. El repositorio los enlaza para identificación y futura trazabilidad; no incorpora automáticamente sus textos completos ni los pone bajo Apache-2.0 o `CC BY-NC-SA 4.0`.

NASA, ESA, ESO, ALMA, IAU, JPL, NIST, USGS, ITU, OECD, OpenStax y los demás organismos, autores, productos y estándares mencionados conservan sus derechos, licencias y marcas. Una cita no implica patrocinio, conformidad, certificación ni permiso para redistribuir la obra.

## Datos de los simuladores

| Componente | Uso | Condiciones |
|---|---|---|
| NASA/JPL Horizons (API v1.2; efemérides DE441 y de satélites) | posiciones de planetas y lunas 2027–2050 en `simuladores/datos/` | Servicio y datos del JPL/NASA; se citan fuente y versión; no implica patrocinio |
| NASA GSFC, Five Millennium Catalog of Solar/Lunar Eclipses (Espenak y Meeus) | referencia de validación del cálculo de eclipses | Datos de la NASA; sólo se usan como contraste |
| Natural Earth 1:110m («land») vía `world-atlas` 2.0.2 | máscara tierra/mar de la Tierra renderizada | Dominio público |
| Node.js (22) | ejecución de las pruebas del motor en CI | [MIT y licencias de componentes](https://github.com/nodejs/node/blob/main/LICENSE) |
| `actions/setup-node` | preparación de Node.js en CI | [MIT](https://github.com/actions/setup-node/blob/main/LICENSE) |

## Obligación al contribuir

Antes de añadir texto extenso, imagen, dataset, software, norma o activo de terceros, documenta titular, URL, versión, licencia o permiso, alcance de reutilización y cambios. Si la licencia no está clara, enlaza en vez de copiar.
