# Plan de refinamiento curricular (Horizonte 0)

> **Actualización:** las líneas L2 a L5 se resolvieron al ubicar los 1.920 temas de los módulos de ruta en áreas y bloques (`catalogo/v0.2.0/colocacion/`) y producir el programa unificado de 2.077 clases. Este plan conserva el diagnóstico de la línea base.

**Fecha:** 5 de noviembre de 2026 · **Versión documental:** `0.1.0` · **Estado:** propuesta; ninguna clase cambia de estado con este documento.

Este plan se ejecuta **antes** de la resolución masiva de B01 del [plan de implementación](PLAN_DE_IMPLEMENTACION_Y_ESTADOS.md). Su objetivo es que el contenido que se redacte sea completo, diferenciado y no repetitivo, en lugar de redactar 5.120 clases sobre una estructura uniforme.

## 1. Diagnóstico de la línea base inicial

Mediciones reproducibles sobre `catalogo/clases.jsonl`:

| Hallazgo | Medición | Consecuencia |
|---|---|---|
| Estructura simétrica | 64 bloques × 20; 24 rutas × 8 módulos × 20 | La carga no refleja la complejidad de cada disciplina |
| Clases derivadas por plantilla | 1.920 de 3.840 clases de rutas (todas las pares) repiten el tema anterior con un prefijo fijo: «Caso práctico de…», «Análisis y evaluación de…», «Modelado o interpretación de…», «Validación de resultados de…», «Aplicación profesional de…» | Cada módulo tiene 10 temas propios, no 20; no hay casos distintos |
| Descripciones rotativas | Las descripciones preliminares son un conjunto reducido de frases que rotan por posición (p. ej. 192 módulos comparten la misma frase en la clase 4) | No informan decisión, dato ni evidencia de cada clase |
| Títulos defectuosos | 133 títulos de rutas concatenan el nombre del módulo (p. ej. «Equilibrio radiativo — Atmósferas estelares») | Corrección editorial |
| Solapamiento ruta/tronco | 88 temas de rutas casi idénticos a clases de bloques (p. ej. B43-C13 y R03-M04-C01; B25-C08 y R02-M05-C03) | Riesgo de duplicación; falta declarar reutilización o profundización |
| Dependencias | Solo recomendaciones por rangos de bloques en `MAPA_DE_RUTAS_PROFESIONALES.md` | No hay prerrequisitos por capacidad |
| Cierre uniforme | Los bloques terminan casi siempre en proyecto, diseño o simulación | Poca variación de evidencia |

El tronco común (1.280 títulos) no tiene duplicados ni plantillas; el problema principal está en las rutas y en la uniformidad de la estructura.

### Vacíos de contenido a evaluar

Detectados por búsqueda de títulos; cada uno debe confirmarse antes de crear unidades:

- misiones reales como casos de estudio (éxitos, anomalías y accidentes);
- planetas gigantes y Mercurio como cuerpos de estudio;
- inteligencia artificial y ciencia de datos aplicadas más allá de un módulo de R08;
- astronomía de transitorios y grandes sondeos del cielo;
- contexto de Chile y del hemisferio sur (observatorios, cielos oscuros, patrimonio);
- diversidad, inclusión y trayectorias en ciencia espacial.

## 2. Principios

1. **Aditivo.** No se borran, renumeran ni reubican IDs. Una unidad redundante se marca «consolidada» y apunta a la unidad que absorbe su alcance.
2. **Peso por necesidad.** El número de clases se justifica por la capacidad que se necesita demostrar, no por simetría. Una unidad puede ser *núcleo* (los IDs existentes), *ampliable* (IDs nuevos añadidos al final) o *consolidada*.
3. **Un caso, un dato, una evidencia.** Dos clases pueden compartir concepto solo si cambian decisión, nivel, método o evidencia (regla antirrepetición del estándar).
4. **Tronco enseña, ruta profundiza.** La ruta reutiliza explícitamente el tronco y declara qué agrega.
5. **Sin inflar estados.** Nada de este plan avanza una clase de E0.

## 3. Líneas de trabajo

### L1 · Auditoría reproducible

- Script de solo lectura en `herramientas/` que reporte: clases derivadas por plantilla, descripciones repetidas, títulos con nombre de módulo, pares ruta/tronco similares y huecos por palabra clave.
- Salida versionada en `metadatos/auditoria_refinamiento.json` con fecha y criterios.
- **Puerta:** el informe se puede regenerar y coincide con las cifras de la sección 1.

### L2 · Decisión de solapamientos

- Revisar los 88 pares ruta/tronco y asignar a cada uno: *reutilización*, *profundización con evidencia distinta* o *consolidación*.
- Registrar en `metadatos/relaciones_ruta_tronco.json` (ID, tipo, capacidad añadida por la ruta).
- **Puerta:** ningún par queda sin decisión; ninguna decisión borra ni renumera IDs.

### L3 · Sustitución del contenido de las clases-plantilla

- Para cada uno de los 192 módulos, definir las 10 aplicaciones como casos distintos: contexto, dato o instrumento, método, producto y criterio de aceptación.
- Los datos se declaran como observados, estimados, sintéticos o simulados.
- Sin cambiar el ID: se enriquece título y descripción preliminar mediante metadatos adicionales (`metadatos/refinamiento_clases.jsonl`); el catálogo base solo cambia en una versión posterior documentada.
- **Puerta:** cero clases-plantilla en los módulos refinados; descripciones únicas.

### L4 · Peso diferenciado por unidad

- Clasificar cada bloque y módulo como núcleo, ampliable o consolidado, con justificación por capacidad.
- Las ampliaciones se proponen en `catalogo/ampliaciones/` con ID nuevo, necesidad, público, fuentes, nivel, dependencia, evidencia y análisis antirrepetición (criterio del plan de implementación).
- **Puerta:** cada ampliación supera el análisis de que no puede resolverse profundizando una unidad existente.

### L5 · Vacíos de contenido

- Confirmar cada vacío de la sección 1 con revisión humana del catálogo.
- Priorizar: (a) catálogo de misiones y casos reales; (b) IA y datos; (c) transitorios y sondeos; (d) Chile y hemisferio sur; (e) diversidad e inclusión; (f) planetas gigantes y Mercurio.
- Cada fuente nueva se registra con localizador y límite; no se copia documentación protegida.

### L6 · Dependencias por capacidad

- Sustituir los rangos de bloques por prerrequisitos de capacidad observable (tipo: prerrequisito, correquisito, recomendación, reutilización).
- Validador de ciclos y de saltos de nivel N0–N5.
- **Puerta:** grafo sin ciclos; cada ruta con diagnóstico de entrada y camino mínimo.

### L7 · Contraste metodológico (reemplaza la entrada directa a B01)

- Contraste doble: **un bloque del tronco (B01)** y **un módulo de ruta refinado** (por ejemplo R01-M01), porque la estructura de ruta no queda representada por B01.
- Medir carga real por clase y por función del estándar para recalibrar el peso (L4).
- **Puerta:** informe de lecciones y decisión explícita de escalar o corregir.

### L8 · Bloques pedagógicos

- Cada bloque y cada módulo de ruta tendrá una **guía pedagógica**: propósito, resultados, secuencia (diagrama con descripción textual), tabla de clases con *qué se aprende* y *evidencia*, hilos transversales, evaluación, seguridad y fuentes.
- Los resúmenes por clase se escriben a partir del refinamiento (L3, L5) y se rotulan «especificación propuesta» hasta tener revisión.
- **Primer resultado:** [B01](../programa/tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md) reescrito con ese formato. Es la plantilla para los 63 bloques restantes y los 192 módulos.
- **Voz pedagógica:** cada clase enseña con prosa explicativa dirigida al estudiante (motivación, ejemplo conductor, analogías con su límite, pausas para pensar y soluciones comentadas). Las tablas se reservan para referencia (símbolos, fuentes, rúbrica). Todo ejercicio debe usar solo conceptos ya explicados en el texto y remitir a la sección donde se enseñaron.
- **Navegación:** cada clase enlaza arriba y abajo a la anterior, a la siguiente y a su bloque; si la vecina aún no existe como página, el enlace lleva a su fila en la guía del bloque. Los metadatos editoriales (versión, autoría, revisores, estado) van en una ficha aparte y no en el cuerpo de la clase.
- **Puerta:** ninguna guía describe una clase como desarrollada si el catálogo la mantiene en E0.

## 4. Orden de ejecución

```text
L1 auditoría → L2 solapamientos → L3 módulos de ruta
→ L4 pesos ‖ L5 vacíos → L6 dependencias → L7 contraste doble
```

L8 se aplica bloque a bloque junto con L3 y L5. Primera clase resuelta: [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md) (22 funciones, laboratorio con prueba analítica), aprobada por el autor; el catálogo conserva E0.

L4 y L5 pueden avanzar en paralelo una vez cerrada L2. L3 se aplica por rutas en lotes pequeños para permitir revisión disciplinar.

## 5. Criterios de cierre del Horizonte 0

- [ ] Auditoría regenerable y publicada (L1).
- [ ] 88 solapamientos decididos (L2).
- [ ] 192 módulos con aplicaciones diferenciadas, sin plantillas (L3).
- [ ] Clasificación núcleo/ampliable/consolidado por unidad (L4).
- [ ] Vacíos confirmados, descartados o propuestos como ampliaciones (L5).
- [ ] Dependencias por capacidad sin ciclos (L6).
- [ ] Contraste doble con informe (L7).
- [ ] `python herramientas/validar_catalogo.py` verde antes y después de cada lote; `STATUS.md`, changelog y manifiestos actualizados.

## 6. Decisiones abiertas

1. ¿Se mantiene el recuento de 5.120 como base inmutable y se reporta aparte el catálogo ampliado?
2. ¿Dónde se guardan los títulos refinados: metadatos adicionales (recomendado) o una versión nueva del catálogo?
3. ¿Qué rutas se refinan primero? Propuesta: R01 (por el contraste), luego las de mayor demanda profesional.

## 7. Límites

Este plan no declara clases redactadas, impartidas ni verificadas. Las cifras de la sección 1 provienen de búsquedas automáticas sobre títulos y requieren confirmación humana antes de crear o consolidar unidades.
