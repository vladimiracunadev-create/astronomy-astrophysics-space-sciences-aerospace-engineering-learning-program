# Simuladores del Sistema Solar 2027–2050

Simuladores interactivos en **JavaScript puro** (sin dependencias ni servidores) que funcionan en GitHub Pages. Dibujan posiciones **oficiales** de NASA/JPL Horizons entre el 1 de enero de 2027 y el 31 de diciembre de 2050, con tamaños y distancias reales.

- [Concentrador de simuladores](index.html)
- [Documentación](documentacion/README.md): [guía de uso](documentacion/GUIA_DE_USO.md), [datos y efemérides](documentacion/DATOS_Y_EFEMERIDES.md), [fuentes y modelos](documentacion/FUENTES_Y_MODELOS.md), [tabla de precisión](documentacion/TABLA_DE_PRECISION.md)

| Carpeta | Contenido |
|---|---|
| `datos/` | Efemérides de JPL empaquetadas (`.json` + `.bin`) y el archivo de verificación |
| `motor/` | Motor común: tiempo, interpolación, cámara 3D, esferas iluminadas, eclipses |
| `paginas/` | Configuración de cada simulador |
| `pruebas/` | Pruebas en Node (sin red) contra JPL y contra el catálogo de eclipses de la NASA |
| `img/` | Figuras SVG a escala generadas desde los datos |
| `documentacion/` | Documentación completa |

Se valida con `python herramientas/validar_simuladores.py` (datos, motor, páginas, enlaces y figuras). Código Apache-2.0; documentación CC BY-NC-SA 4.0; datos de NASA/JPL y Natural Earth en dominio público (véase [DATA_LICENSES.md](../DATA_LICENSES.md)).
