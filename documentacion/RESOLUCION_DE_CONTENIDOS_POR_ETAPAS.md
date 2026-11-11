# Resolución de contenidos por etapas

[🏠 Inicio](../README.md) · [📖 Documentación](README.md) · [🧠 Estándar para generar contenidos](ESTANDAR_PARA_GENERAR_CONTENIDOS.md) · [🗺️ Mapa del repositorio](MAPA_DEL_REPOSITORIO.md)

Este documento responde una pregunta que la portada del repositorio dejaba confusa: **¿qué significa que una clase esté «redactada» y en qué estado está de verdad?** Aquí se separan tres ideas que no deben mezclarse.

## Tres cosas distintas

| Idea | Qué es | Estado hoy |
|---|---|---|
| **Texto escrito** | La clase tiene sus 22 secciones, ejemplos, prácticas y laboratorio ejecutado | **2.077 de 2.077** |
| **Etapa editorial (E0–E6)** | Qué evidencia versionada respalda la clase | Todas siguen registradas en **E0** |
| **Clase aceptada** | Revisada por una persona competente y validada (etapa E5 o superior) | **0 de 2.077** |

Que una clase tenga el texto completo **no** la hace aceptada: el texto escrito equivale, en contenido, a un borrador completo (etapa E3), pero la etapa solo avanza cuando existe la evidencia de cada puerta. Por eso el catálogo conserva E0 hasta que se registre esa evidencia.

## Las etapas

Cada clase avanza **con evidencia, no por declaración manual**:

| Etapa | Resultado exigido | ¿Cuenta como clase aceptada? |
|---|---|:---:|
| `E0 · catalogada` | ID, título, ubicación y referencias preliminares | No |
| `E1 · especificada` | Propósito, resultados, prerrequisitos, decisión central y riesgos | No |
| `E2 · documentada` | Fuentes localizadas con función, alcance, versión y límites | No |
| `E3 · redactada` | Las 22 funciones con ejemplos, prácticas y soluciones | No |
| `E4 · verificada` | Revisión conceptual, matemática, dimensional y de referencias | No |
| `E5 · validada` | Accesibilidad, evaluación, pruebas técnicas y revisión disciplinar | **Sí** |
| `E6 · pilotada` | Evidencia de uso, errores observados y mejoras documentadas | Sí, con nivel superior |

## Qué se necesita para pasar de una etapa a otra

| De → a | Evidencia que se registra |
|---|---|
| E0 → E1 | Ficha con propósito, resultados observables, prerrequisitos y riesgos |
| E1 → E2 | Fuentes con localizador, versión y alcance (ver el [estándar de fuentes](ESTANDAR_DE_FUENTES.md)) |
| E2 → E3 | Clase completa y laboratorio que se ejecuta |
| E3 → E4 | Revisión de conceptos, matemática, unidades y referencias, con nombre y fecha |
| E4 → E5 | Revisión disciplinar, accesibilidad y evaluación probadas |
| E5 → E6 | Uso real con estudiantes y mejoras documentadas |

Cada paso queda registrado en la `FICHA_EDITORIAL.md` de la clase y en el catálogo; nunca se cambia el estado sin esa evidencia.

## Cómo se relaciona con los otros niveles

- **N0–N5** describen la profundidad que **demuestra el estudiante** (ver el [estándar pedagógico](ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md)).
- **V0–V5** describen la confianza en una **afirmación o artefacto** (ver los [niveles de verificación](NIVELES_DE_VERIFICACION.md)): hoy la validación automática del catálogo es V1 (estructural).
- **E0–E6** describen cuánto **trabajo editorial con evidencia** respalda una clase.

## Estrategia de avance

Se avanza primero con pilotos completos y pequeños, y después se escala por bloques y rutas. Las condiciones de cierre, los entregables y las puertas de calidad están en el [roadmap](../ROADMAP.md) y en el [plan de implementación y estados](PLAN_DE_IMPLEMENTACION_Y_ESTADOS.md).
