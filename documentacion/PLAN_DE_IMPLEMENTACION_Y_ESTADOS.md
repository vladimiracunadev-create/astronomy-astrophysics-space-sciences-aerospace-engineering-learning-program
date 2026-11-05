# Plan de implementación, resolución de contenidos y estados

**Última actualización:** 5 de noviembre de 2026 · **Versión documental:** `0.1.0`

Este plan separa tres dimensiones que no deben confundirse:

1. **cobertura del catálogo:** 5.120/5.120 IDs definidos;
2. **resolución editorial:** avance E0–E6 de cada clase;
3. **dominio del estudiante:** profundidad N0–N5 demostrada mediante evidencias.

## Estado de entrega actual

| Superficie | Estado |
|---|---|
| IDs, títulos y ubicación curricular | completo para la línea base `0.1.0` |
| Descripciones y fuentes preliminares | presentes, todavía no verificadas clase por clase |
| Clases en E0 · catalogada | 5.120 |
| Clases en E1 o superior | 0 |
| Clases completamente redactadas y verificadas | 0 |
| Visor del catálogo | disponible como archivo estático |
| Plataforma de aprendizaje, laboratorios y simuladores | no implementados |

## Estados editoriales E0–E6

Los criterios detallados están en el [estándar pedagógico](ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md). El estado se deriva de evidencia versionada; no se asigna por percepción.

| Estado | Significado | Cuenta como desarrollada y verificada |
|---|---|:---:|
| E0 · catalogada | título y referencia preliminar | No |
| E1 · especificada | contrato pedagógico y dependencias | No |
| E2 · documentada | fuentes trazables y límites | No |
| E3 · redactada | contenido completo según las 22 funciones | No |
| E4 · verificada | controles científicos y técnicos superados | No |
| E5 · validada | accesibilidad, evaluación y revisión disciplinar | Sí |
| E6 · pilotada | uso observado y mejora documentada | Sí |

## Estrategia de resolución por horizontes

### Horizonte A · infraestructura documental

**Objetivo:** impedir regresiones antes de redactar contenido.

- preservar los 5.120 IDs y los tres formatos de catálogo;
- validar cantidades, orden, estados y codificación en CI;
- publicar el visor estático;
- definir esquema de clase, fuentes, dependencias y estados;
- añadir inventarios de objetivos, técnicas y evidencias cuando comience E1.

**Cierre:** validadores verdes, documentación coherente, catálogo sincronizado y visor publicado.

### Horizonte 0 · refinamiento curricular

**Objetivo:** corregir la uniformidad estructural y las clases derivadas por plantilla antes de redactar. Ver [plan de refinamiento curricular](PLAN_DE_REFINAMIENTO_CURRICULAR.md).

**Cierre:** auditoría regenerable, solapamientos decididos, módulos de ruta diferenciados, dependencias por capacidad y piloto doble. Sin renumerar IDs ni avanzar estados.

### Horizonte B · piloto B01

**Objetivo:** resolver las 20 clases de B01 de E0 a E5 antes de escalar.

- especificar resultados y prerrequisitos de las 20 clases;
- verificar fuentes y registrar límites;
- redactar con el estándar de 22 funciones;
- construir ejercicios, soluciones, visuales accesibles y evaluación;
- revisar ciencia, matemática, unidades y referencias;
- medir repetición, carga y continuidad del bloque.

**Cierre:** 20 contratos E5, revisión documentada y un informe de lecciones editoriales. Hasta entonces, el estándar no se replica masivamente.

### Horizonte C · fundamentos observables B02–B08

**Objetivo:** consolidar historia, ciencias básicas, observación e informática inicial.

- incorporar prácticas seguras y realizables con distintos recursos;
- validar navegación pedagógica, diagnóstico y recuperación;
- probar accesibilidad de visuales astronómicos;
- producir el primer proyecto integrador y portafolio.

**Cierre:** bloques E5 con dependencias auditadas y evidencia de transferencia entre ellos.

### Horizonte D · núcleo cuantitativo B09–B16

**Objetivo:** establecer el lenguaje matemático, estadístico, computacional y de control.

- biblioteca canónica de símbolos, fórmulas, unidades y convenciones;
- datasets sintéticos o abiertos con procedencia;
- notebooks o código reproducible con pruebas;
- tolerancias, incertidumbre, sensibilidad y casos analíticos de control.

**Cierre:** resultados reproducibles en entornos declarados y revisión matemática/computacional.

### Horizonte E · ciencias del universo y los mundos B17–B40

**Objetivo:** resolver astrofísica, observación, ciencias planetarias, astrobiología y geociencias orbitales.

- datos reales con licencia y calibración documentada;
- separación entre medición, inferencia, modelo y simulación;
- casos de Chile, ALMA, ESO y observatorios cuando la evidencia lo permita;
- controles éticos para muestras, biosignaturas, ciencia ciudadana y patrimonio cultural.

**Cierre:** trazabilidad de datos y afirmaciones, revisión disciplinar por muestras y proyectos integradores.

### Horizonte F · astrodinámica e ingeniería B41–B64

**Objetivo:** resolver mecánica orbital, diseño de misiones, sistemas, operaciones, sostenibilidad, derecho y gestión.

- sistemas de referencia, escalas temporales y efemérides versionadas;
- simulaciones validadas contra casos independientes;
- requisitos, interfaces, tolerancias, fallos y criterios de aceptación;
- fronteras estrictas para propulsión, radiación, medicina, seguridad y dual use;
- normativa y estándares asociados a jurisdicción, versión y vigencia.

**Cierre:** modelos reproducibles, revisión de ingeniería y límites de uso visibles; ningún material se presenta como certificación operacional.

### Horizonte G · rutas profesionales R01–R24

**Objetivo:** profundizar sin duplicar el tronco transversal.

- diagnóstico de entrada y mapa de competencias por ruta;
- ocho módulos encadenados, con evidencia reutilizada explícitamente;
- proyectos y casos profesionales con revisión por disciplina;
- comparación antirrepetición con todos los bloques comunes.

**Cierre:** cada ruta tiene prerrequisitos, checkpoints, proyecto final, rúbrica y criterio de salida verificable. Sigue siendo una ruta dentro de un programa, no una titulación independiente.

### Horizonte H · pilotaje, publicación y mejora permanente

**Objetivo:** elevar clases E5 a E6 sin ocultar limitaciones.

- pilotos pequeños con consentimiento y datos minimizados;
- medición de tiempo, errores, abandono, accesibilidad y transferencia;
- revisión de fuentes, normas, software y datasets por versión;
- publicación de informes y cambios sin reescribir hitos históricos;
- interoperabilidad federada con otros programas mediante metadatos.

**Cierre:** informe de piloto, datos anonimizados, cambios trazables y asuntos abiertos.

## Flujo obligatorio por lote

```text
validar línea base → inventariar dependencias → especificar E1
→ documentar fuentes E2 → redactar E3 → verificar E4
→ validar E5 → pilotar E6 → registrar cambios
```

Un lote debe ser pequeño para permitir revisión sustantiva. La automatización puede comprobar estructura, enlaces, unidades declaradas, IDs y similitud; no sustituye el juicio disciplinar ni el pilotaje.

## Puertas de calidad

1. Ejecutar `python herramientas/validar_catalogo.py` antes y después de cada cambio.
2. No borrar, renumerar ni cambiar silenciosamente el significado de IDs existentes.
3. Registrar dependencias, estado anterior, estado nuevo, responsable, fecha y evidencia.
4. Verificar conceptos, fuentes, fórmulas, unidades, referencias, resultados y límites.
5. Completar práctica, soluciones, rúbrica, recuperación y bibliografía por clase.
6. Validar accesibilidad, navegación, integridad y no repetición.
7. Ejecutar pruebas y conservar fallos como evidencia hasta resolverlos.
8. Reportar la cantidad real de clases en cada estado; nunca convertir títulos en clases terminadas.
9. Exigir revisión humana para avanzar a E5 y evidencia de uso para E6.
10. Actualizar `STATUS.md`, el changelog y los manifiestos cuando cambie el estado verificable.

## Criterio para ampliar el catálogo

Una unidad nueva sólo se incorpora si aporta una capacidad que no puede resolverse mediante conexión o profundización de una unidad existente. La propuesta deberá incluir necesidad, público, fuentes, nivel, dependencia, evidencia y análisis antirrepetición. Los IDs actuales nunca se desplazan.
