# 📦 Descargas y PDF

Versión **0.2.0**. Todos los enlaces apuntan a la última versión publicada en [Releases](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/releases/latest) y no caducan. Cada versión adjunta `SHA256SUMS.txt`:

```bash
sha256sum -c SHA256SUMS.txt
```

## 📕 PDF general

- [**Programa general**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/releases/latest/download/Programa-General.pdf): portada, programa completo, guías de los 24 roles y de los 133 bloques, los 20 anexos, la documentación y los glosarios.

El release adjunta **solo este PDF** y las aplicaciones. El resto del contenido está completo en el sitio y en las aplicaciones sin conexión.

## 🗂️ PDF por área, por rol y por taller (generación local)

Los volúmenes por **área** (12), por **rol** (24) y por **taller de misión** (10) no se adjuntan a la versión; se generan en `build/dist/` con las herramientas de publicación:

```bash
python herramientas/publicacion/sitio.py
python herramientas/publicacion/pdf.py unidades
python herramientas/publicacion/pdf.py ensamblar
```

Requisitos y detalles: [`herramientas/publicacion/`](../herramientas/publicacion/README.md). Las guías de rol y de bloque también se leen directamente en [`rutas/`](../rutas/README.md) y en [`programa/`](../programa/tronco-comun).

## 🖥️ Aplicaciones sin conexión

| Descarga | Archivo | Para qué |
|---|---|---|
| [**Windows · instalador**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/releases/latest) | `Programa-Aeroespacial_v0.2.0_Windows_Setup.exe` | Instala por usuario (sin permisos de administrador), crea accesos directos en el menú Inicio y el escritorio y se desinstala desde «Aplicaciones instaladas» |
| [**Windows · portable**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/releases/latest) | `Programa-Aeroespacial_v0.2.0_Windows.zip` | Sin instalar: extraer todo el ZIP y abrir `ProgramaAeroespacial.exe` (usa Edge o Chrome ya instalados) |
| [**Android · instalador**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/releases/latest) | `Programa-Aeroespacial_v0.2.0_Android.apk` | Móvil y tableta (Android 7 o superior): el propio APK es el instalador; Android no tiene versión portable |

> El APK está firmado con una clave de publicación propia del proyecto, **no** procede de Google Play: se instala permitiendo «orígenes desconocidos». Los ejecutables de Windows (instalador y portable) **no están firmados digitalmente**; SmartScreen puede avisar. Comprueba siempre el `SHA256SUMS.txt` de la versión antes de ejecutarlos.

Volver al [README](../README.md) · [Índice de la documentación](README.md)
