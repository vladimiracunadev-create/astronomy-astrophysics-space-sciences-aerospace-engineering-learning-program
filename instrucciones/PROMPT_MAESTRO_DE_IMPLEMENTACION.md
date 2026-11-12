# Prompt maestro de implementación incremental

Repositorio **exacto**: `astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program`  
Nombre completo y obligatorio: **Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial**.  
No renombrar ni simplificar como CIETES o acrónimos equivalentes.

## Encargo

Transformar gradualmente la **malla documental (línea base de 5.120 registros; programa vigente de 2.077 clases)** en un programa educativo científico y profesional, preservando todas las convenciones, archivos y relaciones establecidas en la línea base inicial, sin inventar contenidos desarrollados ni sobrescribir trabajo válido. La línea base actual solo contiene títulos y referencias preliminares.

## Primera acción obligatoria

1. Leer `README.md`, `metadatos/programa.json`, `documentacion/ALCANCE_Y_CONTRATO_DEL_REPOSITORIO.md`, `documentacion/ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md`, `documentacion/MATRIZ_DE_COBERTURA.md` y los títulos concretos afectados.
2. Auditar `AGENTS.md`, `README`, `CHANGELOG`, tests y convenciones reales del repositorio; no asumir que un paquete local es la versión más reciente una vez publicado.
3. Ejecutar validaciones existentes; conservar salida de línea base.
4. Analizar duplicados, vacíos y dependencias. Proponer implementación **aditiva** sin romper IDs ni funcionamiento.
5. Trabajar en el bloque o módulo solicitado, sin consumir tokens procesando todos los registros innecesariamente.

## Contrato por clase

- Explicar todo concepto, símbolo, fórmula, unidad, comando y reserva del lenguaje antes de usarlo.
- Contenidos pedagógicos profundos; al menos 12 ejercicios sustantivos con soluciones comentadas y dificultad progresiva.
- Laboratorios seguros, ejemplos ejecutables cuando aplique, resultados verificables y márgenes de error.
- Glosario simple y técnico, ejemplos, errores frecuentes, evaluación, rúbrica, fuentes oficiales y evidencias.
- Diferenciar datos observados, simulados, sintéticos y supuestos de modelo.
- Nunca afirmar existencia de certificación, aval, cumplimiento normativo o hardware de vuelo real sin evidencia.
- Seguridad espacial tratada con estudio histórico, regulatorio, defensivo y de resiliencia, sin construir capacidades de daño.

## Contrato técnico

Preferir Python con `uv`, JavaScript con `pnpm`, datos canónicos JSON/CSV/Markdown, pruebas automatizadas y UI web accesible, sin imponer frameworks que aumenten dependencia sin beneficio. Mantener exportaciones estructuradas compatibles con RAG e IA de especialidad, y dependencias científicas con versiones.

## Criterio de entrega

Entregar archivos concretos, diferencias auditables, informes de fuentes, número de clases realmente desarrolladas, resultados de pruebas, matriz de cobertura y los errores que permanezcan. Si el contexto no permite completar un bloque, entregarlo parcial y honestamente rotulado, nunca como terminado.

## No tocar

Prohibido renombrar el repositorio, fusionar otras formaciones o modificar contenidos externos sin permiso. No alterar los IDs registrados en la línea base; las ampliaciones se documentan como extensiones nuevas del catálogo con controles de compatibilidad.
