# Alcance y contrato obligatorio del repositorio

## 1. Identidad formal

**Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial**  
Repositorio: `astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program`  
Versión académica documental: `0.1.0`.  
Es un programa único, continuo, independiente, versionado y extensible; **no** una colección de subprogramas separados.

## 2. Inventario canónico

- 12 áreas y 133 bloques (64 de la línea base y 69 nuevos) con 2.077 clases: 1.280 de la línea base y 797 programadas (las 797, en A02 a A12, ya con texto).
- 24 rutas profesionales como recorridos sobre áreas y bloques; los 192 módulos de la línea base se conservan como equivalencias.
- Línea base `0.1.0` de 5.120 registros únicos y programa `0.2.0`; un identificador permanente para cada clase.
- La clasificación pedagógica de seis niveles: descubrimiento, fundamentos, aplicación, desarrollo, profesional, investigación.
- Prerrequisitos explícitos; posibilidad de diagnóstico inicial y reconocimiento de conocimientos demostrado mediante evaluaciones.
- Relación entre contenido fundamental y especializaciones para evitar duplicar temas ya explicados.

## 3. Estructura física actual del repositorio

```text
astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/
├── README.md
├── PROGRAMA_ACADEMICO_COMPLETO.md
├── catalogo/
│   ├── clases.csv
│   ├── clases.jsonl
│   └── clases.json
├── metadatos/
│   ├── programa.json
│   ├── areas.json
│   ├── bloques.json
│   ├── rutas.json
│   └── modulos.json
├── programa/
│   ├── tronco-comun/            (64 índices por bloque)
│   └── rutas-profesionales/     (24 índices de ruta, 192 índices de módulo)
├── documentacion/
├── fuentes/
├── visor/
├── herramientas/
├── instrucciones/
└── MANIFIESTO_SHA256.txt
```

## 4. Componentes exigidos para las fases de implementación posteriores

Los siguientes directorios son **contratos futuros**, no software presente en la versión actual. Deben crearse progresivamente, sin renombrar contenidos canónicos ni anticipar estados de funcionamiento:

```text
clases/                 # contenidos completos a redactar, una ficha verificable por clase
laboratorios/           # protocolos y ambientes simulados o físicamente seguros
simuladores/            # modelos, variables, unidades, códigos y límites
proyectos/              # proyectos por bloque, ruta y desafíos interdisciplinarios
evaluaciones/           # bancos de ítems, soluciones, rúbricas, progresión y evidencias
glosario/               # definiciones breves y formales; español e inglés
formulas/               # significado de símbolos, deducción, validez y unidades
bibliografia/           # referencias verificadas por lección con versiones
conocimiento-estructurado/ # exportaciones JSONL/JSON para búsqueda, RAG y especialistas IA
datasets/               # referencias y procedencia de datos; licencias, versiones
plataforma-web/          # interfaz accesible, búsqueda, progreso, visualizaciones
accesibilidad/          # contraste, teclado, lectores, alternativas textuales
internacionalizacion/   # idiomas, adaptaciones nacionales, normas por jurisdicción
calidad/                # matrices de cobertura, duplicación, integridad, V&V
scripts/                # generadores deterministas y auditorías reproducibles
tests/                  # pruebas científicas, semánticas, regresión y contratos
.github/workflows/      # validación documental actual y pruebas futuras según exista código
```

## 5. Diseño de contenido científico

Cada clase, cuando se desarrolle, debe contener: objetivo medible, prerrequisitos, problema motivador, definición informal, definición formal, variables y símbolos explicados antes de aparecer, fórmulas con unidades y condiciones, ejemplos desde lo elemental, 12 o más ejercicios sustantivos no repetitivos, soluciones comentadas, actividades experimentales o simuladas, riesgos y seguridad, recursos visuales accesibles, glosario, evaluación con rúbrica, fuentes verificadas y evidencia de aprendizaje.

**Prohibido:** títulos vacíos presentados como clases terminadas, referencias inventadas, problemas con soluciones no verificadas, duplicación mecánica de ejercicios, fórmulas sin unidades o explicaciones, copiar textos protegidos sin licencia, afirmaciones de certificación externa inexistente.

## 6. Ingeniería de sistemas espaciales y validación

- Separar datos medidos, estimados, sintéticos y simulados; conservar procedencia.
- Definir sistema de referencia y escala temporal (UTC, TAI, TT, TDB, etc.) según el caso.
- Registrar constantes físicas, efemérides, kernels SPICE, versiones y fecha de acceso.
- Definir unidades SI, tolerancias, incertidumbres, comprobaciones de conservación y límites de modelo.
- Probar los algoritmos contra casos analíticos y, cuando sea apropiado, fuentes NASA/JPL/IAU/ESA.
- No presentar una simulación académica como certificación de vuelo, seguridad de lanzamiento o navegación real.

## 7. Seguridad, ética y legalidad

La ruta de defensa espacial es histórica, jurídica, estratégica, de monitoreo y resiliencia. Los ejercicios se realizan en entornos controlados y defensivos; no implican sistemas reales de ataque, sabotaje o interferencia. Las actividades físicas peligrosas (propulsión, láseres, presión, radiación) se enseñan con simuladores, protocolos y requisitos de laboratorio adecuados. No emitir credenciales médicas, jurídicas, de piloto o de astronauta por completar el repositorio.

El material fuente se cita y vincula, sin hacer copias masivas ni asumir que estar disponible públicamente significa estar libre de derechos. Separar licencias de código, texto, marcas, datasets, ilustraciones y estándares.

## 8. Plataforma visual y profesional

La interfaz futura debe proporcionar: portada académica, índice de áreas/bloques/rutas, buscador, navegación jerárquica, rutas según competencia, progreso local/por cuenta, accesibilidad WCAG, modo claro/oscuro, diagramas SVG y visualizaciones 2D/3D cuando aporten valor, glosario emergente, ejercicios graduales, soluciones disponibles de forma pedagógica, visualización de fórmulas, reportes de evidencia y exportación.

Evitar interfaces decorativas sin funcionalidad. Priorizar carga rápida, diseño adaptable a móvil/escritorio, modo sin conexión para el contenido autorizado y compatibilidad con navegadores modernos.

## 9. Política de desarrollo incremental

- Revisar siempre README, el catálogo, la estructura existente, las instrucciones de repositorio y el estado de pruebas antes de cambiar nada.
- No sobrescribir ni eliminar módulos, clases, rutas, fuentes o trabajos previos válidos.
- Conservar las 5.120 clases de la línea base; la reorganización `0.2.0` no borra ninguna, numera los bloques de forma consecutiva (B01–B133) y registra el número anterior de cada bloque.
- Cada etapa debe incluir matriz de cambios, pruebas automatizadas, registro de fuentes y contraste de cobertura.
- Por cada bloque implementado: pruebas de calidad, reporte de errores y documentación de evolución.
- Preferencias técnicas: `uv` para proyectos Python; `pnpm` para JS, evitando dependencias innecesarias. No imponer frameworks pesados.

## 10. Internacionalización y territorio

Idioma principal español de Chile, glosarios científicos bilingües español/inglés, unidades SI, fechas y zonas horarias explícitas, regulación internacional y comparativas por país. Casos de ALMA/ESO y observatorios de Chile, geociencias chilenas y riesgos climáticos. La regulación debe asociarse a país, fuente y vigencia; no asumir equivalencia jurídica entre jurisdicciones.

## 11. Interoperabilidad federada

El programa no debe absorber ni renombrar repositorios de matemática, física, ingeniería de software, IA, ciberseguridad, arquitectura, pedagogía, derecho o finanzas. Exportar capacidades, temas, prerrequisitos y evidencias mediante estructuras abiertas con IDs estables, para interoperabilidad con otros programas sin forzar carpetas compartidas.

## 12. Declaración de honestidad de completitud

El **inventario de títulos y referencias preliminares** está completo para el alcance fijado en esta versión. No puede garantizarse que la investigación espacial no genere temas nuevos o que se haya enumerado absolutamente toda subdisciplina existente. Para extensiones futuras se documentarán vacíos, impacto curricular, fuentes y nuevos IDs, sin desplazar los actuales.
