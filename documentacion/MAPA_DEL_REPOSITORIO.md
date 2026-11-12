# Mapa del repositorio

[🏠 Inicio](../README.md) · [📖 Documentación](README.md) · [🧠 Estándar para generar contenidos](ESTANDAR_PARA_GENERAR_CONTENIDOS.md) · [🪜 Resolución por etapas](RESOLUCION_DE_CONTENIDOS_POR_ETAPAS.md)

Qué hay en cada carpeta, **qué se escribe a mano y qué se genera**, y cómo fluye el contenido desde el catálogo hasta los PDF y las aplicaciones. Sustituye a la lista «Qué contiene hoy» de la portada.

## Vista general

```text
.
├── README.md · STATUS.md · ROADMAP.md · CHANGELOG.md · VERSION   Portada, estado verificable, plan, cambios y versión
├── PROGRAMA_ACADEMICO_COMPLETO.md      Índice unificado de las 2.077 clases            (generado)
├── catalogo/                           Línea base inicial (5.120 registros) y estructura vigente (estructura, colocación)
├── programa/
│   ├── tronco-comun/                   133 guías de bloque (B01–B133)                  (escritas)
│   ├── clases/Bnn/<ID>-<slug>/         2.077 clases: CLASE.md + FICHA_EDITORIAL.md + laboratorio
│   └── rutas-profesionales/            Capa heredada: módulos de la línea base inicial
├── rutas/                              24 guías de rol (prosa escrita + ruta generada)
├── anexos/                             20 anexos históricos, pedagógicos y de cálculo  (escritos)
├── talleres/                           talleres integradores de misión (un taller por misión real; T01 Marte redactado)
├── glosario/                           Glosario completo (generado) y esencial (escrito)
├── documentacion/                      Contratos, estándares, planes y guías           (escritos)
├── metadatos/ · fuentes/ · instrucciones/   Inventarios, referencias preliminares y prompt maestro
├── visor/                              Explorador estático del catálogo
├── herramientas/                       Validadores, generadores y publicación
├── .github/workflows/                  validate.yml (controles) y pages.yml (sitio)
└── build/                              Salidas de la publicación (ignorado por git)
```

## Qué se escribe y qué se genera

| Contenido | Origen | Cómo se regenera |
|---|---|---|
| Clases (`CLASE.md`), guías de bloque, anexos, documentación | Escritos | — |
| Navegación anterior/siguiente de las clases | Generada | `python herramientas/actualizar_navegacion.py` |
| `PROGRAMA_ACADEMICO_COMPLETO.md` | Generado desde `catalogo/` | `python herramientas/generar_programa.py` |
| Ruta de áreas y bloques de cada rol (`rutas/*.md`) y su tabla en el README | Generada (la prosa del rol es escrita) | `python herramientas/generar_rutas_por_rol.py` |
| `RECORRIDO.md` de las rutas heredadas | Generado desde `metadatos/recorridos/` | `python herramientas/generar_recorridos.py` |
| Glosario completo (`glosario/*.md`, salvo `esencial/`) | Generado desde las clases | `python herramientas/generar_glosario.py` |
| Sección «Descargas y PDF» del README | Generada | `python herramientas/publicacion/readme.py` |
| `MANIFIESTO_SHA256.txt` | Generado | `python herramientas/generar_manifiesto.py` |
| Sitio, PDF y aplicaciones | Generados en `build/` | ver [`herramientas/publicacion/`](../herramientas/publicacion/README.md) |

## Cómo fluye el contenido

```text
catalogo/clases.*  (línea base, no se edita)
      │  colocación de los 192 módulos de ruta
      ▼
catalogo/estructura/  (estructura.json · clases_programadas.jsonl · equivalencias · colocacion/)
      │                                   │
      ▼                                   ▼
PROGRAMA_ACADEMICO_COMPLETO.md      programa/tronco-comun/  →  programa/clases/  →  rutas/ · glosario/
                                                      │
                                                      ▼
                                   herramientas/publicacion/  →  sitio HTML · PDF · APK · ZIP de Windows
                                                      │
                                                      ▼
                                      GitHub Pages (sitio)  y  GitHub Releases (PDF y aplicaciones)
```

Una clase pertenece a un **bloque**, un bloque a un **área**, y un **rol** es una ruta que ordena clases de varios bloques: los roles no tienen contenido propio.

## Herramientas

| Herramienta | Función |
|---|---|
| `validar_catalogo.py` | Cantidades, IDs, orden, estados y codificación de la línea base |
| `validar_colocacion.py` | Dónde vive, en áreas y bloques, cada tema de cada módulo de ruta |
| `validar_recorridos.py` | Qué clases usa cada rol y en qué orden |
| `consolidar_distribucion.py` · `candidatos_colocacion.py` | Reparto de los módulos de las rutas en el tronco común |
| `generar_programa.py` | Programa unificado con IDs estables |
| `generar_rutas_por_rol.py` · `generar_recorridos.py` | Guías y recorridos por rol |
| `actualizar_navegacion.py` | Enlaces entre clases y su guía de bloque |
| `generar_glosario.py` | Glosario alfabético con contexto de cada clase |
| `calculadora_cientifica.py` | Calculadora didáctica con `autotest` (ver el [Anexo I](../anexos/ANEXO-I-escalas-formulas-y-calculadora.md)) |
| `generar_manifiesto.py` | Huellas SHA-256 de los archivos versionables |
| `publicacion/` | Sitio, PDF, APK, lanzador de Windows y verificador de artefactos |

## Controles automáticos (CI)

- **`validate.yml`** ejecuta los validadores y comprueba que las guías y los índices estén al día.
- **`pages.yml`** genera el sitio completo y lo publica en GitHub Pages en cada cambio de `main`.

Estos controles verifican estructura; **no** certifican la corrección científica (ver [niveles de verificación](NIVELES_DE_VERIFICACION.md)).

## Dónde seguir

- ¿Quieres entender el alcance? [Alcance y contrato del repositorio](ALCANCE_Y_CONTRATO_DEL_REPOSITORIO.md).
- ¿Quieres saber cómo se escribe una clase? [Estándar para generar los contenidos](ESTANDAR_PARA_GENERAR_CONTENIDOS.md).
- ¿Quieres ver las 12 áreas con sus 133 bloques? [Mapa de áreas y bloques](MAPA_DE_AREAS_Y_BLOQUES.md).
- Índice general de archivos: [`FILE_INDEX.md`](../FILE_INDEX.md).
