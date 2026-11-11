# Publicación: sitio HTML, PDF y aplicaciones

Herramientas que convierten el contenido Markdown del repositorio en los artefactos de cada versión. Todo se
genera en `build/` (ignorado por git) y se adjunta a la página de la versión (*Release*); no se guarda en el repositorio.

| Paso | Orden | Resultado |
|---|---|---|
| 1. Sitio sin conexión | `python herramientas/publicacion/sitio.py` | `build/web/` (HTML + búsqueda); lo usan las apps |
| 2. Unidades PDF | `python herramientas/publicacion/pdf.py unidades` | Un PDF por clase, guía, anexo y archivo del glosario |
| 3. Volúmenes PDF | `python herramientas/publicacion/pdf.py ensamblar` | General, 12 áreas y 24 roles, con marcadores y numeración |
| 4. Android | `python herramientas/publicacion/android.py` | `.apk` firmado (WebView + sitio en los assets) |
| 5. Windows | `python herramientas/publicacion/windows.py` | `.zip` portable con lanzador `.exe` |
| 6. Verificación | `python herramientas/publicacion/verificar.py` | Abre cada artefacto y cuenta su contenido |

## Requisitos

- Python 3.12 con `markdown`, `PyMuPDF` (`fitz`), `playwright` (con Chromium) y `Pillow`.
- Android: Android SDK (build-tools y plataforma 34) y un JDK (sirve el de Android Studio). No usa Gradle.
- Windows: el compilador de C# incluido en Windows (.NET Framework 4); la app usa Microsoft Edge o Google Chrome ya instalados.

## Decisiones

- **PDF por unidades.** Cada unidad se imprime una sola vez y después se ensamblan los volúmenes; así un rol (con solo
  sus clases) y un área (con todas) reutilizan el mismo PDF. Los tramos de ~300 páginas se deduplican para no repetir
  las fuentes incrustadas.
- **Apps = contenido Markdown convertido a HTML.** La app de Android es un `WebView` que abre `file:///android_asset/web/index.html`;
  la de Windows abre el mismo sitio en una ventana de aplicación de Edge o Chrome. Ninguna necesita conexión.
- **Clave de firma de Android.** Se crea una vez en `~/.android/programa-aeroespacial-release.jks` (con su contraseña en un
  archivo `.pass` al lado). **No está ni debe estar en el repositorio.** Sin ella no se pueden publicar actualizaciones
  que se instalen sobre la versión anterior: guarda una copia de seguridad.
- **Estado del contenido.** Todo está en nivel E0 (redactado, pendiente de revisión disciplinar): las versiones se publican como *pre-release*.

## Límites conocidos

- Los enlaces de los Markdown a archivos fuera del contenido (herramientas, catálogo en JSON) quedan como texto señalado en las apps.
- La aplicación de Windows no está firmada digitalmente: SmartScreen puede avisar.
- No hay aplicación para iOS ni para macOS en esta versión.
