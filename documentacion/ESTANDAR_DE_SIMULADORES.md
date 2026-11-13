# Estándar de los simuladores

Los **simuladores** (`simuladores/`) son material interactivo de apoyo: dibujan en el navegador, sin servidores, el Sistema Solar entre 2027 y 2050 con datos oficiales. **No son clases ni anexos ni talleres**: no cuentan en las 2.077 clases, ni en los 20 anexos, ni en los 10 talleres. Este estándar fija qué debe cumplir un simulador nuevo.

## Reglas

1. **Datos oficiales y trazables.** Toda posición sale de una efemérides pública con procedencia declarada (hoy, NASA/JPL Horizons). Nunca se estima ni se «completa» una posición: si no hay efemérides para una fecha, el cuerpo se oculta y la cobertura se documenta.
2. **Realismo explícito.** Tamaños y distancias reales. Todo factor de ampliación es una opción visible y el aviso de escala lo dice siempre.
3. **Error medido, no supuesto.** Cada cuerpo lleva su error de interpolación medido contra el proveedor en épocas que no son nodos; la tolerancia está en la [tabla de precisión](../simuladores/documentacion/TABLA_DE_PRECISION.md) y la validación automática la hace cumplir.
4. **Marco, unidades, tiempo, versiones y fecha de descarga** declarados en la documentación de cada simulador (regla del repositorio para toda simulación).
5. **Dato frente a ilustración.** Las texturas, los anillos, el fondo de estrellas y cualquier elemento decorativo se rotulan como ilustrativos; ninguno interviene en un cálculo.
6. **Validación independiente.** Todo fenómeno derivado (eclipses, fases, estaciones, Ls, oposiciones…) se contrasta con una fuente distinta de la que alimenta el cálculo (hoy: catálogo de eclipses de la NASA y API del U.S. Naval Observatory) y esa referencia se versiona para repetir la prueba sin red.
7. **Autónomo y accesible.** Sin dependencias, CDN ni llamadas a internet salvo la descarga de sus propios datos; funciona en GitHub Pages; controles con teclado, etiquetas, contraste suficiente y sin movimiento automático al abrir.
8. **Documentado.** Cada simulador tiene su página en `simuladores/documentacion/` (qué muestra, datos que calcula, validación, tolerancias, archivos) y una figura SVG a escala **generada desde los datos**.

## Estructura

| Ruta | Contenido |
|---|---|
| `simuladores/datos/<sistema>.json` y `.bin` | Efemérides empaquetadas (formato en [Datos y efemérides](../simuladores/documentacion/DATOS_Y_EFEMERIDES.md)) |
| `simuladores/motor/` | Motor común: tiempo, interpolación, cámara, esferas, eclipses, astronomía |
| `simuladores/paginas/<sistema>.js` y `<sistema>.html` | Configuración y página de cada simulador |
| `simuladores/pruebas/` | Pruebas en Node y referencias versionadas (NASA, USNO) |
| `simuladores/img/<sistema>.svg` | Figura a escala generada por `herramientas/efemerides/generar_svg.py` |
| `simuladores/documentacion/` | Documentación (una página por simulador más la guía, los datos y las fuentes) |
| `herramientas/efemerides/` | Descarga de Horizons, empaquetado, tabla de precisión y figuras |

## Cómo añadir un simulador

1. Añadir el sistema a `herramientas/efemerides/generar_efemerides.py` y ejecutar `python -X utf8 herramientas/efemerides/generar_efemerides.py --solo <sistema>`.
2. Crear `simuladores/<sistema>.html` y `simuladores/paginas/<sistema>.js` (copiar uno existente), añadirlo a `simuladores/motor/navegacion.js` y a `SIMULADORES` en `herramientas/publicacion/sitio.py`.
3. Regenerar la tabla de precisión (`python -X utf8 herramientas/efemerides/tabla_precision.py`) y las figuras (`python -X utf8 herramientas/efemerides/generar_svg.py`).
4. Escribir `simuladores/documentacion/<sistema>.md` y enlazarlo desde el índice.
5. Añadir las pruebas independientes que correspondan a `simuladores/pruebas/ejecutar.mjs`.
6. Ejecutar `python herramientas/validar_simuladores.py` (se ejecuta también en la integración continua).

## Qué valida `validar_simuladores.py`

Descripción de cada `.json`/`.bin` y tolerancias; pruebas del motor en Node (interpolación, tiempo, orientación, eclipses, fases, estaciones, Marte, estaciones de los gigantes); páginas sin recursos externos y con módulos existentes; enlaces e imágenes de los `.md`; tabla de precisión y figuras SVG al día; coherencia de la lista de simuladores entre la barra de navegación y el sitio. **No** valida la exactitud de las texturas (ilustrativas) ni sustituye la revisión humana de la redacción.
