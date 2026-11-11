# Estándar para generar los contenidos

[🏠 Inicio](../README.md) · [📖 Documentación](README.md) · [🪜 Resolución por etapas](RESOLUCION_DE_CONTENIDOS_POR_ETAPAS.md) · [🗺️ Mapa del repositorio](MAPA_DEL_REPOSITORIO.md)

Este documento explica **cómo se escribió cada clase del programa y qué debe cumplir una clase nueva**. Antes vivía en la portada del repositorio; aquí se describe tal como se aplicó a las 2.077 clases de A01 a A12.

El contrato completo (criterios, rúbricas y niveles N0–N5) está en el [estándar pedagógico y de evaluación](ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md); la guía práctica de redacción, en la [guía de redacción de clases](GUIA_DE_REDACCION_DE_CLASES.md).

## La idea

Las clases siguen el estándar **`clase-profunda-cientifica`**. Una clase no vale por tener muchas palabras: debe **conectar necesidad, fundamento, fuente, actividad, evidencia, evaluación y continuidad**. Quien termina una clase tiene que poder hacer algo concreto, comprobarlo y saber hasta dónde llega lo que aprendió.

## Qué contiene una clase

Cada clase vive en `programa/clases/Bnn/<ID>-<slug>/` y tiene:

| Archivo | Para qué sirve |
|---|---|
| `CLASE.md` | La clase completa, con 22 secciones numeradas (ver abajo) |
| `FICHA_EDITORIAL.md` | Metadatos de producción (no son contenido de estudio): autoría, aprobación del autor, revisión disciplinar, estado en el catálogo y fecha de consulta de las fuentes |
| `*.py` (y salidas) | El laboratorio de la sección 17: se ejecuta, declara unidades, sistema de referencia, datos, versiones y tolerancias, y usa semilla fija cuando hay azar |

## Las 22 funciones y dónde están en `CLASE.md`

Cada función verificable corresponde a una sección con el mismo número:

| N.º | Función | Sección de `CLASE.md` |
|---:|---|---|
| 1 | Identidad y estado editorial | Ubicación, nivel y alcance |
| 2 | Propósito y decisión central | Por qué esta clase existe |
| 3 | Resultados observables | Lo que podrás hacer al terminar |
| 4 | Prerrequisitos y diagnóstico | Con qué llegas y cómo comprobarlo |
| 5 | Contexto científico o profesional | Un caso de contexto y casos de referencia |
| 6 | Vocabulario y definiciones operacionales | Vocabulario |
| 7 | Modelo mental y relaciones causales | Modelo mental |
| 8 | Desarrollo progresivo | La explicación, paso a paso |
| 9 | Magnitudes, símbolos y unidades | Magnitudes, símbolos y unidades |
| 10 | Sistema de referencia, escala temporal y convenciones | Convenciones y referencias |
| 11 | Evidencia y fuentes con alcance declarado | De dónde sale lo que afirmamos |
| 12 | Visualización accesible | Cómo ver el resultado |
| 13 | Ejemplo trabajado y reproducible | Ejemplo trabajado |
| 14 | Comparación de métodos y límites | Distintas formas de describir el problema |
| 15 | Práctica guiada | Práctica guiada |
| 16 | Práctica autónoma y transferencia | Práctica autónoma, transferencia e integrador |
| 17 | Laboratorio, observación o simulación | Laboratorio |
| 18 | Errores frecuentes y recuperación | Errores frecuentes y cómo corregirlos |
| 19 | Evaluación formativa | Cómo sabrás que vas bien |
| 20 | Evidencia de aprendizaje y rúbrica | Qué entregas y cómo se evalúa |
| 21 | Seguridad, ética, accesibilidad y límites profesionales | Ética, seguridad y límites |
| 22 | Síntesis, glosario, continuidad y bibliografía | Para cerrar y seguir |

## Reglas para datos, fórmulas y simulaciones

Cuando una clase usa fórmulas, datos o simulaciones, **declara siempre**:

- unidades y sistema de referencia;
- escala temporal y convenciones;
- procedencia, versión y fecha de consulta de los datos;
- supuestos, tolerancias, incertidumbre y límites de validez.

Un resultado **simulado nunca se presenta como observado ni como certificado**. Las fuentes siguen el [estándar de fuentes](ESTANDAR_DE_FUENTES.md): una referencia sin localizador, versión o alcance declarado no cuenta como evidencia.

## Cómo se aplicó en la práctica

1. **Primero la guía del bloque** (`programa/tronco-comun/Bnn-<slug>.md`): propósito, resultados y tabla de sus clases.
2. **Después las clases del bloque**, una por una, cada una con su laboratorio ejecutado.
3. **Por último los enlaces:** `herramientas/actualizar_navegacion.py` mantiene los vínculos anterior/siguiente y la guía del bloque enlaza todas sus clases.
4. **Controles automáticos** en CI (`validate.yml`): cantidades, IDs, orden y estados. Estos controles verifican la estructura; **no** certifican que el contenido sea correcto.

**Autoría declarada.** La redacción de las clases fue asistida por IA a pedido del autor, y así consta en la ficha editorial de cada una; la aprobación del autor y la revisión disciplinar figuran como **pendientes**.

## Qué sigue

Que una clase esté redactada no la hace una clase aceptada. El camino desde el borrador hasta una clase verificada y validada se describe en la [resolución por etapas](RESOLUCION_DE_CONTENIDOS_POR_ETAPAS.md).
