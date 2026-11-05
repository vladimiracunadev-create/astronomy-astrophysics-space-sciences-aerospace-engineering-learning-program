# Guía de redacción de clases

Esta guía fija cómo se escribe cada clase para que las 5.120 sigan una misma voz, un mismo orden y los mismos controles. Se deriva de [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md), aprobada por el autor del programa, y del [estándar pedagógico](ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md), que prevalece si hay diferencias.

## 1. Dónde vive cada clase

- Carpeta: `programa/clases/<bloque>/<ID>-<slug>/`, con `<slug>` = título en minúsculas, sin tildes y con guiones (lo calcula `herramientas/actualizar_navegacion.py`).
- Archivos: `CLASE.md` (obligatorio), un script de laboratorio solo si la clase calcula algo, y `FICHA_EDITORIAL.md` (metadatos de producción; no es contenido del estudiante).
- Los IDs, títulos y el catálogo **no se modifican**. El estado de catálogo sigue siendo E0 hasta registrar revisión disciplinar (`AGENTS.md`).

## 2. Voz y estructura

La clase **enseña con prosa dirigida al estudiante** (segunda persona), no es una planificación docente. Las 22 funciones del estándar se conservan con la numeración de B01-C01:

1 ubicación y alcance · 2 por qué existe (pregunta motivadora y decisión central) · 3 resultados · 4 prerrequisitos con diagnóstico autocorregible · 5 caso real · 6 vocabulario · 7 modelo mental (diagrama con descripción textual) · 8 explicación paso a paso · 9 magnitudes y unidades · 10 convenciones · 11 fuentes · 12 visualización accesible · 13 ejemplo trabajado · 14 comparación de métodos · 15 práctica guiada (3) · 16 práctica autónoma (5), transferencia (3) e integrador (1) · 17 laboratorio · 18 errores frecuentes · 19 evaluación formativa · 20 evidencia y rúbrica · 21 ética, seguridad y límites · 22 cierre, glosario ES–EN y continuidad.

Reglas de voz:

- Un **ejemplo conductor** recorre la clase y se retoma en el ejemplo trabajado y en los ejercicios.
- Las tablas se reservan para referencia (símbolos, fuentes, rúbrica, resultados); la explicación va en párrafos.
- Cada analogía declara su límite. Cada concepto se define antes de usarse.
- **Coherencia:** cada ejercicio usa solo conceptos ya explicados y remite a la sección donde se enseñaron. Las soluciones son comentadas y van en `<details>` para que se intente primero.
- Mínimo 12 ejercicios (3 guiados, 5 autónomos, 3 de transferencia, 1 integrador), con dificultad progresiva.

## 3. Fuentes: qué cuenta como verificada

1. Cada cifra o afirmación relevante lleva un ID de fuente (`S1`…) y una fila en la tabla de la sección 11 con: autor u organismo, título, edición o versión, localizador (DOI, arXiv, URL), qué respalda, **fecha de consulta** y estado.
2. Solo se cita lo realmente consultado. Si solo se leyó el resumen, se escribe «resumen». Si una página no abrió, la fuente no se usa y no se inventa un localizador.
3. Prioridad: datos de misión con procedencia, artículos primarios, documentación oficial (BIPM, IAU, NASA, ESA, ESO), normas vigentes. Una fuente secundaria localiza, no sostiene decisiones críticas.
4. Se parafrasea; no se reproducen textos ni figuras. Se respeta la licencia: por ejemplo, el libro abierto *Astronomy 2e* de OpenStax prohíbe ingerirlo en sistemas de IA generativa sin permiso, por lo que no se usa como fuente de redacción; solo podría citarse bibliográficamente.
5. Los datos se rotulan **observados**, **estimados**, **sintéticos** o **simulados**.

## 4. Laboratorios

Un script de laboratorio declara en su cabecera: datos y su procedencia, modelo, supuestos, dominio de validez y tolerancia; incluye al menos una **prueba contra un caso analítico o una referencia independiente** que detenga la ejecución si falla; imprime las versiones de Python y bibliotecas; y se ejecuta antes de publicar la clase, copiando sus resultados reales a la sección 17.

## 5. Navegación

Cada clase abre y cierra con bloques delimitados por `<!-- nav:top -->…<!-- /nav -->` y `<!-- nav:bottom -->…<!-- /nav -->`. No se editan a mano: `python herramientas/actualizar_navegacion.py` los reescribe (enlazando a la clase anterior y siguiente y al bloque, y a la fila del bloque cuando la vecina aún no existe) y enlaza el ID en la guía del bloque. `--check` falla si algo está desactualizado y corre en CI.

## 6. Puertas antes de subir

- `python herramientas/validar_catalogo.py` aprobado.
- `python herramientas/actualizar_navegacion.py --check` al día.
- Scripts de laboratorio ejecutados y sus resultados copiados.
- Cifras de la clase comprobadas contra su fuente y contra un cálculo propio.
- `python herramientas/generar_manifiesto.py` ejecutado.
- Una clase por vez o por bloque en un commit; CI en verde en `main`.
