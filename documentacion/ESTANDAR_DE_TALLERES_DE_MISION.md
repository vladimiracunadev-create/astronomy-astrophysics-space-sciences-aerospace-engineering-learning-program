# Estándar de los talleres de misión

Los **talleres integradores de misión** (carpeta [`talleres/`](../talleres/README.md)) reúnen lo aprendido en las 12 áreas para planificar, de principio a fin, una misión espacial **real**. Este documento fija cómo se escriben, qué deben cumplir, cómo se validan y cómo se añade uno nuevo.

## Qué es un taller y qué no es

| Es | No es |
|---|---|
| Un ejercicio de **integración**: el estudiante rehace la planificación de una misión real con su propia versión | Una clase del catálogo ni un anexo de lectura |
| Un documento **didáctico** con datos de referencia pública y cálculos reproducibles | Una fuente primaria ni una guía para diseñar u operar una misión |
| Un producto con **entregable evaluable** (el dossier de misión y su rúbrica) | Un curso con título, certificación o habilitación |

Un taller no tiene ID de clase (`Bnn-Cnn`) y **no cuenta** en las 2.077 clases ni en los 20 anexos. Su estado es **E0**: redactado, pendiente de revisión disciplinar.

## Estructura obligatoria

Cada taller es una carpeta `Txx-<área>-<misión>/` con:

| Archivo | Contenido |
|---|---|
| `README.md` | Ficha de la misión real, por qué es un buen caso, objetivos de aprendizaje, índice de capítulos y fuentes |
| `01-objetivo-y-requisitos.md` … `10-entregables-y-rubrica.md` | Diez capítulos con **la misma estructura** para poder comparar misiones |
| `laboratorio_Txx.py` | Cálculos en Python (solo biblioteca estándar) |
| `figuras_Txx.py` y `figuras/*.svg` | Esquemas SVG generados con el mismo modelo del laboratorio |

### Los diez capítulos

| # | Capítulo | Pregunta que contesta |
|---|---|---|
| 1 | Objetivo y requisitos | ¿Para qué vamos y cómo sabremos que se logró? |
| 2 | Ventana y trayectoria | ¿Cuándo salir y por dónde? |
| 3 | Lanzador, masas y vehículo | ¿Qué cohete y cuánto pesa cada parte? |
| 4 | Subsistemas | ¿Cómo se alimenta, se calienta, se comunica y piensa la nave? |
| 5 | La fase crítica | ¿Qué momento decide la misión y cómo se prepara? |
| 6 | Operaciones y comunicaciones | ¿Cómo se conduce a esa distancia? |
| 7 | Fiabilidad, fallos y contingencias | ¿Cómo no fallar y qué hacer si algo falla? |
| 8 | Seguridad y protección | ¿Qué daño puede hacer la misión y cómo se evita? |
| 9 | Costos, cronograma y derecho | ¿Cuánto cuesta, cuánto tarda y bajo qué reglas? |
| 10 | Entregables y rúbrica | ¿Qué se entrega y cómo se evalúa? |

El nombre del capítulo 5 y del 8 puede adaptarse a la misión (por ejemplo, «El perihelio» o «Seguridad y ética»), pero **la pregunta que contesta no cambia**.

Cada capítulo (salvo el 10) termina con **«Ejercicio del capítulo»**; el 10 contiene el dossier y la **rúbrica** (10 criterios de 0 a 4, aprobado con 24 puntos y ningún criterio en 0).

## Reglas de contenido

1. **Misión real y fuentes públicas.** Las cifras provienen de materiales públicos de las agencias y equipos (hojas de datos, kits de prensa, informes de auditoría, publicaciones abiertas). Se citan **por nombre y alcance**; no se reproducen documentos completos.
2. **Honestidad sobre la incertidumbre.** Toda cifra redondeada o dudosa lleva **⚠** y la instrucción de verificar en la fuente primaria. Si un dato no se puede respaldar, se redacta como **suposición** o se omite. No se inventan cifras: los repartos ilustrativos se rotulan como tales.
3. **Unidades, sistema de referencia y fecha.** Cada cifra lleva su unidad; cada trayectoria, su sistema de referencia y su fecha en **UTC**.
4. **Modelos con tolerancia.** El laboratorio declara en su encabezado `UNIDADES`, `SISTEMA DE REFERENCIA`, `MODELO` y `TOLERANCIA`, y los resultados se presentan como **diseño preliminar**; la tolerancia es la real del modelo (por ejemplo, ±30 % en el modelo radial de T03).
5. **Lecciones, no culpas.** Los fallos se cuentan para aprender (qué ocurrió, qué se hizo, qué lección queda), sin atribuir responsabilidades personales.
6. **Sin habilitación.** Un taller no habilita decisiones de vuelo, seguridad de la tripulación, nucleares, regulatorias ni de defensa planetaria. En los talleres tripulados (T02 y T09) y en el de defensa planetaria (T10) el aviso es explícito.
7. **Accesibilidad.** Cada figura tiene `<title>` y `<desc>` y, junto a cada diagrama Mermaid, una descripción textual. Las figuras SVG usan fondo blanco y texto oscuro para leerse en pantalla, en PDF y en modo oscuro, con letra de 12 px como mínimo.

## Figuras

- Se generan con `figuras_Txx.py` a partir de `laboratorio_Txx.py` y de las utilidades comunes [`talleres/_comun/comun_taller.py`](../talleres/_comun/comun_taller.py).
- Los esquemas que no están a escala **lo dicen** en su subtítulo (por ejemplo, «escala radial comprimida»).
- Se versionan en `figuras/` y se enlazan desde los capítulos con texto alternativo descriptivo.
- Para el sitio, las apps y los PDF no hace falta convertirlas: ya son SVG vectorial.

## Cómo se publican

| Salida | Cómo |
|---|---|
| Markdown | La propia carpeta |
| HTML | El sitio incluye cada taller en su menú «Talleres», con las figuras y los laboratorios copiados |
| PDF | Un volumen por taller (`Taller-Txx-…pdf`) y el bloque «Talleres» del PDF general, con marcadores por capítulo |
| Apps | Windows y Android incluyen el sitio completo |

## Validación

```bash
python herramientas/validar_talleres.py
```

Comprueba, por taller: README y capítulos 01 a 10, ejercicio o rúbrica en cada uno, enlaces y figuras existentes, que el laboratorio se ejecuta y declara sus supuestos, que `figuras_Txx.py` regenera **exactamente** los SVG versionados y que ningún texto de las figuras se sale del lienzo o se solapa. Corre en la integración continua.

**Lo que no valida:** la **exactitud histórica** de los datos. Esa revisión es humana y se registra en la etapa E1 en adelante ([resolución por etapas](RESOLUCION_DE_CONTENIDOS_POR_ETAPAS.md)).

## Cómo añadir un taller nuevo

1. **Elegir una misión real** con documentación pública abundante y un reto que no repita el de los talleres existentes (ver la tabla del [índice](../talleres/README.md)).
2. **Copiar la estructura** de un taller existente (T01 es la plantilla) y reutilizar `talleres/_comun/comun_taller.py`.
3. **Escribir primero el laboratorio** y ejecutarlo: los números del texto salen de ahí, no al revés.
4. **Generar las figuras** y corregir con `python talleres/_comun/verificar_figuras.py` hasta cero problemas.
5. **Redactar los diez capítulos** marcando con ⚠ lo que deba verificarse.
6. **Añadir el taller** a la tabla de [`talleres/README.md`](../talleres/README.md) y a la del [`README.md`](../README.md) principal.
7. **Validar**: `python herramientas/validar_talleres.py`, y regenerar la página de descargas con `python herramientas/publicacion/readme.py`.
8. Registrar el cambio en [`CHANGELOG.md`](../CHANGELOG.md) y en [`STATUS.md`](../STATUS.md).

## Los diez talleres actuales

| Taller | Misión | Reto que domina |
|---|---|---|
| [T01](../talleres/T01-marte-mars-2020-perseverance/README.md) | Mars 2020 / Perseverance | Entrada, descenso y aterrizaje autónomos |
| [T02](../talleres/T02-luna-artemis-i/README.md) | Artemis I | Reentrada lunar y vuelo de prueba para personas |
| [T03](../talleres/T03-pluton-new-horizons/README.md) | New Horizons | Sobrevuelo único a 32 UA con asistencia de Júpiter |
| [T04](../talleres/T04-punto-l2-james-webb/README.md) | Telescopio James Webb | 344 despliegues sin posibilidad de reparación |
| [T05](../talleres/T05-saturno-cassini-huygens/README.md) | Cassini-Huygens | Cuatro asistencias, inserción y sonda en Titán |
| [T06](../talleres/T06-cometa-rosetta-philae/README.md) | Rosetta y Philae | Encuentro con un cometa y aterrizaje en gravedad casi nula |
| [T07](../talleres/T07-sol-parker-solar-probe/README.md) | Parker Solar Probe | Frenar con Venus y sobrevivir a 476 veces el calor terrestre |
| [T08](../talleres/T08-asteroide-osiris-rex/README.md) | OSIRIS-REx | Muestra de un asteroide y retorno a la Tierra |
| [T09](../talleres/T09-orbita-baja-crew-dragon-demo-2/README.md) | Crew Dragon Demo-2 | Vuelo tripulado, abortos y riesgo acumulado |
| [T10](../talleres/T10-defensa-planetaria-dart/README.md) | DART | Impacto cinético y medición de una desviación |

Volver al [índice de la documentación](README.md) · [README del programa](../README.md).
